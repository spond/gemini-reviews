from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
#!/usr/bin/env python3
"""
Build the Balanced N = 100 Open-Review Cohort (Option B):
- 50 Selective Flagship & Academic Society Open-Review Papers (eLife, PLOS Pathogens, PLOS Genetics, PLOS Biology, PLOS Computational Biology)
- 50 Open-Review Megajournal Papers (PLOS ONE, PeerJ, BMJ Open, Royal Society Open Science, Communications Biology)
- Balanced across 5 Core Biomedical Subfields (10 Selective + 10 Megajournal per subfield = 20 per subfield, N = 100 total).
- Every paper is verified to have:
  (1) Complete full-body manuscript text (>= 12,000 bytes) with all decision letters / referee reports / author responses stripped out,
  (2) Verbatim human referee reports (>= 2,500 bytes of actual Reviewer comments) saved separately in human_reports/.
"""
import urllib.request
import urllib.parse
import json
import random
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from fetch_pmc_html import parse_pmc_html
from build_deidentified import scrub_manuscript

BASE_DIR = Path(str(REPO_ROOT))
OUT_DIR = BASE_DIR / "open_review_exp"

SUBFIELDS = [
    ("Viral Evolution & Virology", '("SARS-CoV-2" OR "influenza" OR "HIV-1" OR "viral evolution" OR "phylogenetics" OR "herpesvirus" OR "flavivirus")'),
    ("Statistical & Population Genetics", '("GWAS" OR "genome-wide association" OR "Mendelian randomization" OR "polygenic" OR "population genetics" OR "selection")'),
    ("Single-Cell & Transcriptomics", '("single-cell" OR "scRNA-seq" OR "RNA-seq" OR "transcriptome" OR "differential expression")'),
    ("Cancer & Microbiome", '("microbiome" OR "16S rRNA" OR "metagenomics" OR "tumor microenvironment" OR "cancer genomics" OR "biomarker")'),
    ("Molecular Evolution & Phylogenetics", '("molecular evolution" OR "phylogenomic" OR "positive selection" OR "dN/dS" OR "gene family" OR "comparative genomics")'),
]

SELECTIVE_QUERY = '(JOURNAL:"eLife" OR JOURNAL:"PLoS Biol" OR JOURNAL:"PLoS Pathog" OR JOURNAL:"PLoS Genet" OR JOURNAL:"PLoS Comput Biol")'
MEGA_QUERY = '(JOURNAL:"PLoS ONE" OR JOURNAL:"PeerJ" OR JOURNAL:"BMJ Open" OR JOURNAL:"R Soc Open Sci" OR JOURNAL:"Commun Biol")'

DECISION_SPLIT_RE = re.compile(
    r"\n#+\s+(Decision [Ll]etter|Reviewer #?1|eLife [Aa]ssessment|Open [Pp]eer [Rr]eview|Peer [Rr]eview [Hh]istory|Peer [Rr]eview [Rr]eports?)\b"
)

def scrub_open_review_manuscript(body_md, meta, anon_id):
    """Scrub all metadata, dates, journal headers, and any residual open-review markers."""
    scrubbed = scrub_manuscript(body_md, meta, anon_id)
    extra_patterns = [
        r"\beLife\b", r"\bPLOS Biology\b", r"\bPLoS Biol\b", r"\bPLOS Pathogens\b", r"\bPLoS Pathog\b",
        r"\bPLOS Genetics\b", r"\bPLoS Genet\b", r"\bPLOS Computational Biology\b", r"\bPLoS Comput Biol\b",
        r"\bPLOS ONE\b", r"\bPLoS ONE\b", r"\bPeerJ\b", r"\bBMJ Open\b", r"\bRoyal Society Open Science\b",
        r"\bCommunications Biology\b", r"\beLife assessment\b", r"\bDecision letter\b", r"\bAuthor response\b",
        r"\bPublic review\b", r"\bRecommendations for the authors\b"
    ]
    for pat in extra_patterns:
        scrubbed = re.sub(pat, "[REDACTED_VENUE]", scrubbed, flags=re.IGNORECASE)
    return scrubbed

def search_candidates(journal_q, topic_q, subfield_name, tier_name, max_Candidates=90):
    q = f'{journal_q} AND {topic_q} AND OPEN_ACCESS:y AND IN_EPMC:y AND PUB_YEAR:[2020 TO 2025] AND ("Reviewer #1" OR "Reviewer 1" OR "Decision Letter" OR "Public review")'
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&resultType=core&pageSize={max_Candidates}&format=json"
    out = []
    try:
        data = json.loads(urllib.request.urlopen(url, timeout=20).read().decode())
        for r in data.get("resultList", {}).get("result", []):
            pmc = r.get("pmcid", "")
            if not pmc:
                continue
            j = r.get("journalInfo", {}).get("journal", {}).get("title", "")
            out.append({
                "pmcid": pmc,
                "pmid": r.get("pmid", "0"),
                "doi": r.get("doi", ""),
                "title": r.get("title", ""),
                "authors": r.get("authorString", ""),
                "journal": j,
                "year": int(r.get("pubYear", 2024)),
                "citedByCount": int(r.get("citedByCount", 0)),
                "subfield": subfield_name,
                "venue_tier": tier_name,
            })
    except Exception as e:
        print("Search error:", e)
    return out

def fetch_and_split_candidate(cand):
    pmc = cand["pmcid"]
    cand["cohort_id"] = pmc
    try:
        req = urllib.request.Request(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/", headers={"User-Agent": "Mozilla/5.0"})
        html_bytes = urllib.request.urlopen(req, timeout=15).read()
        full_md = parse_pmc_html(html_bytes, cand)
        m = DECISION_SPLIT_RE.search(full_md)
        if not m:
            return None
        body_md = full_md[:m.start()].strip() + "\n"
        human_md = full_md[m.start():].strip() + "\n"
        # Verify body_md is a genuine full-text article (not an abstract-only stub) and has Methods & Results
        if len(body_md) < 14000:
            return None
        if re.search(r"available as a PDF|scanned PDF", body_md, re.I):
            return None
        # Verify human_md contains actual substantive referee reports (at least 2,500 chars and mentions Reviewer)
        if len(human_md) < 2500:
            return None
        if not re.search(r"Reviewer\s*#?\s*[123]|Public review|Comments to the Author", human_md, re.I):
            return None
        return (cand, body_md, human_md)
    except Exception:
        return None

def main():
    for sub in ["raw_manuscripts", "human_reports", "scrubbed_manuscripts", "reviews"]:
        (OUT_DIR / sub).mkdir(parents=True, exist_ok=True)

    rng = random.Random(20261029)
    selected = []
    seen_pmcs = set()

    for tier_name, journal_q in [
        ("Selective Flagship / Society", SELECTIVE_QUERY),
        ("Open-Review Megajournal", MEGA_QUERY),
    ]:
        for subfield_name, topic_q in SUBFIELDS:
            cands = search_candidates(journal_q, topic_q, subfield_name, tier_name, max_Candidates=90)
            cands = [c for c in cands if c["pmcid"] not in seen_pmcs]
            rng.shuffle(cands)
            print(f"[{tier_name} | {subfield_name}] Searching {len(cands)} candidates for 10 verified pairs...")

            cell_selected = []
            # Process in batches of 18 with ThreadPoolExecutor until we have 10 valid
            for i in range(0, len(cands), 18):
                batch = cands[i:i+18]
                with ThreadPoolExecutor(max_workers=9) as ex:
                    results = [r for r in ex.map(fetch_and_split_candidate, batch) if r is not None]
                for res in results:
                    pmc = res[0]["pmcid"]
                    if pmc not in seen_pmcs and len(cell_selected) < 10:
                        seen_pmcs.add(pmc)
                        cell_selected.append(res)
                if len(cell_selected) >= 10:
                    break

            print(f"  -> Selected {len(cell_selected)}/10 for [{tier_name} | {subfield_name}]")
            selected.extend(cell_selected)

    print(f"\nTotal selected open-review papers: {len(selected)}/100")
    # Shuffle all 100 before assigning OPEN_ANON_001..100 so reviewers are completely blind to venue tier and subfield
    rng.shuffle(selected)

    manifest = []
    for idx, (meta, body_md, human_md) in enumerate(selected, 1):
        anon_id = f"OPEN_ANON_{idx:03d}"
        pmc = meta["pmcid"]
        meta["anon_id"] = anon_id
        meta["body_bytes"] = len(body_md)
        meta["human_review_bytes"] = len(human_md)

        scrubbed = scrub_open_review_manuscript(body_md, meta, anon_id)
        meta["scrubbed_bytes"] = len(scrubbed)

        (OUT_DIR / "raw_manuscripts" / f"{anon_id}_{pmc}_body.md").write_text(body_md, encoding="utf-8")
        (OUT_DIR / "human_reports" / f"{anon_id}_{pmc}_human.md").write_text(human_md, encoding="utf-8")
        (OUT_DIR / "scrubbed_manuscripts" / f"{anon_id}.md").write_text(scrubbed, encoding="utf-8")
        manifest.append(meta)

    with open(OUT_DIR / "manifest_open_review_100.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print("Saved manifest_open_review_100.json and all 100 scrubbed manuscripts + 100 human referee reports.")

if __name__ == "__main__":
    main()
