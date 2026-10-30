from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
#!/usr/bin/env python3
"""
Build the Balanced 7-Window Secular Cohort (N = 1,000 total across 1991-2025):
  - W1_1991_1995: 140 papers (10 existing + 130 new)
  - W2_1996_2000: 140 papers (10 existing + 130 new)
  - W3_2001_2005: 144 papers (10 existing + 134 new)
  - W4_2006_2010: 144 papers (10 existing + 134 new)
  - W5_2011_2015: 144 papers (10 existing + 134 new)
  - W6_2016_2020: 144 papers (10 existing + 134 new)
  - W7_2021_2025: 144 papers (10 existing + 134 new)
Total = 1,000 papers (70 existing TIME_ANON_01..70 preserved + 930 new TIME_ANON_0071..TIME_ANON_1000).
"""
import urllib.request
import urllib.parse
import json
import random
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

sec_dir = Path(str(REPO_ROOT / "secular_trend_exp"))
raw_dir = sec_dir / "raw_papers"
anon_dir = sec_dir / "anon_papers"
rev_dir = sec_dir / "reviews"

def clean_text(el):
    if el is None:
        return ""
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()

def parse_epmc_xml(xml_bytes, meta):
    soup = BeautifulSoup(xml_bytes, "xml")
    body = soup.find("body")
    if not body:
        return ""
    lines = [
        f"# {meta['pmcid']} ({meta['year']})",
        f"**Title:** {meta['title']}",
        f"**Authors:** {meta['authors']}",
        f"**Journal:** {meta['journal']} ({meta['year']}) | **PMID:** {meta.get('pmid','')}",
        ""
    ]
    abstract = soup.find("abstract")
    if abstract:
        lines.append("\n## Abstract\n")
        for p in abstract.find_all("p"):
            t = clean_text(p)
            if t:
                lines.append(t + "\n")
        if len(lines) <= 7:
            t = clean_text(abstract)
            if t:
                lines.append(t + "\n")
    for el in body.find_all(["sec", "p", "preformat", "table-wrap", "fig"]):
        if el.name == "sec":
            title_el = el.find("title", recursive=False)
            if title_el:
                t = clean_text(title_el)
                if t and t.lower() not in ("references", "supplementary material", "acknowledgments", "acknowledgements", "funding", "author contributions", "competing interests"):
                    lines.append(f"\n## {t}\n")
        elif el.name in ("p", "preformat"):
            if el.find_parent("table-wrap") or el.find_parent("fig") or el.find_parent("abstract") or el.find_parent("ref-list"):
                continue
            t = clean_text(el)
            if len(t) > 20:
                lines.append(t + "\n")
        elif el.name == "table-wrap":
            lbl = clean_text(el.find("label"))
            cap = clean_text(el.find("caption"))
            lines.append(f"\n### {lbl}: {cap}\n")
            tbl = el.find("table")
            if tbl:
                for tr in tbl.find_all("tr")[:35]:
                    cells = [clean_text(c) for c in tr.find_all(["th", "td"])]
                    if cells:
                        lines.append("| " + " | ".join(cells) + " |")
        elif el.name == "fig":
            lbl = clean_text(el.find("label"))
            cap = clean_text(el.find("caption"))
            if cap:
                lines.append(f"\n> **{lbl}:** {cap}\n")
    md = "\n".join(lines)
    if len(md) < 8500:
        raw_b = clean_text(body)
        if len(raw_b) >= 7500:
            md = "\n".join(lines[:7]) + "\n\n## Main Text\n\n" + raw_b
    return md

def parse_pmc_html(pmcid, meta):
    req = urllib.request.Request(
        f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    html = urllib.request.urlopen(req, timeout=10).read()
    soup = BeautifulSoup(html, "html.parser")
    art = soup.find("article")
    if not art:
        return ""
    for r in art.find_all("section", class_="ref-list"):
        r.decompose()
    lines = [
        f"# {pmcid} ({meta['year']})",
        f"**Title:** {meta['title']}",
        f"**Authors:** {meta['authors']}",
        f"**Journal:** {meta['journal']} ({meta['year']}) | **PMID:** {meta.get('pmid','')}",
        "",
        "## Abstract & Main Text",
    ]
    for el in art.find_all(["h2", "h3", "p", "table"]):
        if el.name in ("h2", "h3"):
            t = clean_text(el)
            if t and t.lower() not in ("references", "acknowledgments", "acknowledgements"):
                lines.append(f"\n## {t}\n")
        elif el.name == "p":
            t = clean_text(el)
            if len(t) > 25:
                lines.append(t + "\n")
        elif el.name == "table":
            for tr in el.find_all("tr")[:30]:
                cells = [clean_text(c) for c in tr.find_all(["th", "td"])]
                if cells:
                    lines.append("| " + " | ".join(cells) + " |")
    md = "\n".join(lines)
    if len(md) < 9000:
        body_sec = art.find("section", class_="body") or art
        raw_t = clean_text(body_sec)
        if len(raw_t) >= 8000:
            md = "\n".join(lines[:6]) + "\n\n" + raw_t
    return md

def scrub_temporal_manuscript(raw_text, meta, anon_id):
    lines = raw_text.splitlines()
    body_start = 0
    for idx, line in enumerate(lines):
        if line.strip().startswith("## Abstract") or line.strip().startswith("## Introduction") or line.strip().startswith("## INTRODUCTION"):
            body_start = idx
            break
    if body_start == 0:
        body_start = min(6, len(lines))
    body_lines = []
    skip_section = False
    skip_headers = (
        "acknowledg", "funding", "author contribution", "competing interest",
        "conflict of interest", "declaration", "ethics", "publisher", "citation",
        "copyright", "correspondence", "footnote", "abbreviations", "open access",
        "supplementary", "additional information", "contributor information"
    )
    for line in lines[body_start:]:
        s = line.strip()
        if s.startswith("#"):
            hdr = s.lstrip("#").strip().lower()
            if any(k in hdr for k in skip_headers):
                skip_section = True
                continue
            else:
                skip_section = False
        if not skip_section:
            body_lines.append(line)
    text = "\n".join(body_lines)
    if meta.get("doi"):
        text = text.replace(meta["doi"], "[REDACTED_DOI]")
    if meta.get("pmcid"):
        text = text.replace(meta["pmcid"], "[REDACTED_ID]")
    if meta.get("pmid"):
        text = text.replace(str(meta["pmid"]), "[REDACTED_ID]")
    if meta.get("journal"):
        j = meta["journal"]
        if len(j) > 3:
            text = re.sub(re.escape(j), "[REDACTED_VENUE]", text, flags=re.IGNORECASE)
    for token in re.split(r"[,;\s]+", meta.get("authors", "")):
        t = token.strip(".")
        if len(t) >= 4 and t.lower() not in (
            "with", "from", "university", "group", "consortium", "study", "team",
            "gene", "cell", "data", "long", "high", "west", "east", "hall", "king",
            "wood", "hill", "bell", "ward", "page", "cole", "ross", "cook", "reed",
            "lane", "ford"
        ):
            text = re.sub(r"\b" + re.escape(t) + r"\b", "[REDACTED_AUTHOR]", text)
    text = re.sub(r"\b(19[89]\d|20[0-2]\d)\b", "[YEAR]", text)
    header = (
        f"# Anonymous Manuscript ID: {anon_id}\n\n"
        "*(All identifying metadata, author names, journal titles, DOIs, and publication/citation calendar years have been scrubbed for temporally blinded review.)*\n\n"
    )
    return header + text

# Load all existing PMCIDs across the repository to guarantee zero overlap
existing_pmcids = set()
for mf in [
    Path(str(REPO_ROOT / "cohorts_200.json")),
    Path(str(REPO_ROOT / "ood_exp/manifest.json")),
    Path(str(REPO_ROOT / "peer_review_exp/manifest.json")),
    Path(str(REPO_ROOT / "self_audit_exp/manifest.json")),
    sec_dir / "manifest.json",
]:
    if mf.exists():
        for m in re.findall(r"PMC\d+", mf.read_text()):
            existing_pmcids.add(m)

old_manifest = json.loads((sec_dir / "manifest.json").read_text())
existing_70 = old_manifest["papers"]
print(f"Loaded {len(existing_70)} existing secular papers and {len(existing_pmcids)} total excluded PMCIDs.")

# Target NEW papers per window and per track:
# Windows W1, W2: 130 new each (total 140 each: 35 per track) -> 32, 32, 33, 33 new across the 4 tracks
# Windows W3..W7: 134 new each (total 144 each: 36 per track) -> 33, 33, 34, 34 new across the 4 tracks
windows = [
    ("W1_1991_1995", "1991–1995", 1991, 1995, [32, 32, 33, 33]),
    ("W2_1996_2000", "1996–2000", 1996, 2000, [32, 32, 33, 33]),
    ("W3_2001_2005", "2001–2005", 2001, 2005, [33, 33, 34, 34]),
    ("W4_2006_2010", "2006–2010", 2006, 2010, [33, 33, 34, 34]),
    ("W5_2011_2015", "2011–2015", 2011, 2015, [33, 33, 34, 34]),
    ("W6_2016_2020", "2016–2020", 2016, 2020, [33, 33, 34, 34]),
    ("W7_2021_2025", "2021–2025", 2021, 2025, [33, 33, 34, 34]),
]

tracks = [
    ("Molecular Evolution & Phylogenetics", "(phylogenetic OR phylogeny OR substitution OR divergence OR homology) AND (sequence OR gene OR protein OR evolution)"),
    ("Viral Evolution & Virology", "(virus OR viral OR retrovirus OR HIV OR influenza OR hepatitis OR coronavirus OR phage) AND (sequence OR mutation OR replication OR genome)"),
    ("Population & Statistical Genetics", "(genetics OR polymorphism OR allele OR locus OR linkage OR genotype OR haplotype OR heritability) AND (population OR human OR chromosome OR mutation)"),
    ("Gene Expression & Functional Genomics", "(expression OR mRNA OR transcript OR promoter OR transcription OR cDNA OR regulation) AND (gene OR cell OR protein OR tissue)"),
]

rng = random.Random(20261029)
new_papers = []

for w_code, w_label, y1, y2, track_quotas in windows:
    print(f"\n=== Sampling Window {w_label} (Target new: {sum(track_quotas)}) ===")
    w_picked = []
    for (track_name, q_terms), target_n in zip(tracks, track_quotas):
        q = f'OPEN_ACCESS:Y AND IN_EPMC:Y AND PUB_YEAR:[{y1} TO {y2}] AND {q_terms} AND NOT PUB_TYPE:"review"'
        u = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&resultType=lite&pageSize=600&format=json"
        try:
            d = json.loads(urllib.request.urlopen(u, timeout=25).read().decode())
            cands = [
                r for r in d.get("resultList", {}).get("result", [])
                if r.get("pmcid") and r.get("journalTitle") and r["pmcid"] not in existing_pmcids
                and "retraction" not in r.get("title", "").lower()
                and "correction" not in r.get("title", "").lower()
                and "erratum" not in r.get("title", "").lower()
            ]
        except Exception as e:
            print("Search err:", e)
            cands = []
        rng.shuffle(cands)

        def try_fetch(r):
            pmcid = r["pmcid"]
            auth_str = r.get("authorString", "")
            auth_cnt = len([x for x in auth_str.split(",") if x.strip()]) if auth_str else 1
            meta = {
                "pmcid": pmcid,
                "pmid": str(r.get("pmid", "")),
                "doi": r.get("doi", ""),
                "title": r.get("title", ""),
                "authors": auth_str,
                "author_count": max(1, auth_cnt),
                "journal": r.get("journalTitle", ""),
                "year": int(r.get("pubYear", y1)),
                "citedByCount": int(r.get("citedByCount", 0)),
                "window_code": w_code,
                "window_label": w_label,
                "track": track_name,
            }
            try:
                u_xml = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
                xb = urllib.request.urlopen(u_xml, timeout=10).read()
                if b"<body" in xb and len(xb) > 10000:
                    md = parse_epmc_xml(xb, meta)
                    if len(md) >= 8500 and "## " in md:
                        return (meta, md)
            except Exception:
                pass
            if y1 <= 2005:
                try:
                    md = parse_pmc_html(pmcid, meta)
                    if len(md) >= 8500 and "## " in md:
                        return (meta, md)
                except Exception:
                    pass
            return None

        picked = []
        step = 24
        for i in range(0, len(cands), step):
            batch = [c for c in cands[i:i+step] if c["pmcid"] not in existing_pmcids]
            if not batch:
                continue
            with ThreadPoolExecutor(max_workers=12) as ex:
                res_list = [x for x in ex.map(try_fetch, batch) if x is not None]
            for meta, md in res_list:
                if meta["pmcid"] not in existing_pmcids and len(picked) < target_n:
                    existing_pmcids.add(meta["pmcid"])
                    picked.append((meta, md))
            if len(picked) >= target_n:
                break

        w_picked.extend(picked)
        print(f"  [{w_label} | {track_name[:22]:22s}] {len(picked)}/{target_n} fetched")

    # If any track in 1991-1995 or 1996-2000 fell slightly short, top up from broader window pool
    needed = sum(track_quotas) - len(w_picked)
    if needed > 0:
        print(f"  Topping up {needed} papers in {w_label}...")
        q_broad = f'OPEN_ACCESS:Y AND IN_EPMC:Y AND PUB_YEAR:[{y1} TO {y2}] AND (gene OR sequence OR virus OR mutation OR protein OR cell)'
        u_broad = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q_broad)}&resultType=lite&pageSize=1000&format=json"
        d_b = json.loads(urllib.request.urlopen(u_broad, timeout=25).read().decode())
        cands_b = [
            r for r in d_b.get("resultList", {}).get("result", [])
            if r.get("pmcid") and r.get("journalTitle") and r["pmcid"] not in existing_pmcids
        ]
        rng.shuffle(cands_b)
        for i in range(0, len(cands_b), 24):
            batch = [c for c in cands_b[i:i+24] if c["pmcid"] not in existing_pmcids]
            with ThreadPoolExecutor(max_workers=12) as ex:
                res_list = [x for x in ex.map(try_fetch, batch) if x is not None]
            for meta, md in res_list:
                if meta["pmcid"] not in existing_pmcids and needed > 0:
                    existing_pmcids.add(meta["pmcid"])
                    w_picked.append((meta, md))
                    needed -= 1
            if needed <= 0:
                break

    new_papers.extend(w_picked)
    print(f"Window {w_label} new total: {len(w_picked)}/{sum(track_quotas)}")

print(f"\nTotal new papers fetched: {len(new_papers)}/930")

# Assign SEC_0071..SEC_1000 and shuffled TIME_ANON_0071..TIME_ANON_1000
for idx, (meta, md) in enumerate(new_papers, 71):
    meta["sec_id"] = f"SEC_{idx:04d}"
    pmcid = meta["pmcid"]
    sec_id = meta["sec_id"]
    (raw_dir / f"{sec_id}_{pmcid}.md").write_text(md, encoding="utf-8")

shuffled_new = list(new_papers)
rng.shuffle(shuffled_new)

manifest_1000 = {
    "papers": list(existing_70),
    "anon_to_sec": dict(old_manifest["anon_to_sec"]),
}

for idx, (meta, md) in enumerate(shuffled_new, 71):
    anon_id = f"TIME_ANON_{idx:04d}"
    meta["anon_id"] = anon_id
    scrubbed = scrub_temporal_manuscript(md, meta, anon_id)
    meta["scrubbed_bytes"] = len(scrubbed)
    (anon_dir / f"{anon_id}.md").write_text(scrubbed, encoding="utf-8")
    manifest_1000["anon_to_sec"][anon_id] = meta["sec_id"]
    manifest_1000["papers"].append(meta)

with open(sec_dir / "manifest_1000.json", "w") as f:
    json.dump(manifest_1000, f, indent=2)

print(f"Saved manifest_1000.json with {len(manifest_1000['papers'])} total papers (TIME_ANON_01..70 + TIME_ANON_0071..1000)!")
