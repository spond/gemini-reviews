from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
import urllib.request
import urllib.parse
import json
import random
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

root = Path(str(REPO_ROOT))
pr_dir = root / "peer_review_exp"

def clean_text(el):
    if el is None:
        return ""
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()

def parse_xml_manuscript(xml_bytes, meta, label_id):
    soup = BeautifulSoup(xml_bytes, "xml")
    body = soup.find("body")
    if not body:
        return ""
    lines = [
        f"# {label_id}",
        f"**Title:** {meta.get('title','')}",
        f"**Authors:** {meta.get('authors','')}",
        f"**Venue:** {meta.get('journal','Preprint')} ({meta.get('year','')})",
        "",
    ]
    abstract = soup.find("abstract")
    if abstract:
        lines.append("\n## Abstract\n")
        for p in abstract.find_all("p"):
            t = clean_text(p)
            if t:
                lines.append(t + "\n")
    for el in body.find_all(["sec", "p", "table-wrap", "fig"]):
        if el.name == "sec":
            title_el = el.find("title", recursive=False)
            if title_el:
                t = clean_text(title_el)
                if t and t.lower() not in ("references", "supplementary material", "acknowledgments", "acknowledgements", "funding", "author contributions", "competing interests", "decision letter", "author response", "peer review"):
                    lines.append(f"\n## {t}\n")
        elif el.name == "p":
            if el.find_parent("table-wrap") or el.find_parent("fig") or el.find_parent("abstract") or el.find_parent("ref-list") or el.find_parent("sub-article"):
                continue
            t = clean_text(el)
            if len(t) > 20:
                lines.append(t + "\n")
        elif el.name == "table-wrap":
            if el.find_parent("sub-article"):
                continue
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
            if el.find_parent("sub-article"):
                continue
            lbl = clean_text(el.find("label"))
            cap = clean_text(el.find("caption"))
            if cap:
                lines.append(f"\n> **{lbl}:** {cap}\n")
    back = soup.find("back")
    if back:
        for sec in back.find_all(["sec", "notes"]):
            sec_type = (sec.get("sec-type") or sec.get("notes-type") or "").lower()
            title_el = sec.find("title", recursive=False)
            t = clean_text(title_el) if title_el else ""
            t_low = t.lower()
            is_avail = (
                "data-availability" in sec_type
                or "availability" in sec_type
                or any(k in t_low for k in ("availability", "data", "code", "software", "accession", "repository", "resource"))
            )
            if is_avail and t_low not in ("references", "acknowledgments", "acknowledgements", "funding", "author contributions", "competing interests"):
                heading = t if t else "Data and Code Availability"
                lines.append(f"\n## {heading}\n")
                for p in sec.find_all("p"):
                    pt = clean_text(p)
                    if pt:
                        lines.append(pt + "\n")
    return "\n".join(lines)

def scrub_doc(raw_text, meta, anon_id):
    lines = raw_text.splitlines()
    body_start = 0
    for idx, line in enumerate(lines):
        if line.strip().startswith("## Abstract") or line.strip().startswith("## Introduction"):
            body_start = idx
            break
    if body_start == 0:
        body_start = min(5, len(lines))
    body_lines = []
    skip_section = False
    skip_headers = (
        "acknowledg", "funding", "author contribution", "competing interest",
        "conflict of interest", "declaration", "ethics", "publisher", "citation",
        "copyright", "correspondence", "footnote", "open access", "decision letter",
        "author response", "peer review", "reviewer report", "elife assessment"
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
    text = f"# {anon_id}\n\n" + "\n".join(body_lines)
    for key in ("doi", "ppr_doi", "pmcid", "pmid", "ppr_id"):
        val = str(meta.get(key, "") or "")
        if len(val) > 3:
            text = text.replace(val, "[REDACTED]")
    if meta.get("journal") and len(meta["journal"]) > 3:
        text = re.sub(re.escape(meta["journal"]), "[REDACTED_VENUE]", text, flags=re.IGNORECASE)
    for pat in [
        r"\bbioRxiv\b", r"\bmedRxiv\b", r"\bResearch Square\b", r"\bpreprint\b",
        r"CC-BY-NC-ND", r"CC-BY", r"has not been certified by peer review",
        r"author/funder, who has granted", r"copyright holder for this",
        r"\beLife assessment\b", r"\bDecision letter\b", r"\bAuthor response\b"
    ]:
        text = re.sub(pat, "[REDACTED]", text, flags=re.IGNORECASE)
    return text

def is_tier12(j):
    jl = j.lower().strip()
    t12_set = {
        "nature", "nat genet", "nature genetics", "nat commun", "nature communications",
        "nat microbiol", "nature microbiology", "nat methods", "nature methods",
        "nat biotechnol", "nature biotechnology", "nat struct mol biol", "nature structural & molecular biology",
        "nat ecol evol", "nature ecology & evolution", "nat med", "nature medicine",
        "science", "sci adv", "science advances", "cell", "cell rep", "cell reports",
        "cell host microbe", "cell host & microbe", "cell syst", "cell systems",
        "mol cell", "molecular cell", "genome biol", "genome biology",
        "genome res", "genome research", "nucleic acids res", "nucleic acids research",
        "elife", "plos biol", "plos biology", "plos genet", "plos genetics",
        "plos pathog", "plos pathogens", "plos comput biol", "plos computational biology",
        "mol biol evol", "molecular biology and evolution", "proc natl acad sci u s a",
        "proceedings of the national academy of sciences of the united states of america",
        "syst biol", "systematic biology", "am j hum genet", "american journal of human genetics",
        "bioinformatics", "brief bioinform", "briefings in bioinformatics", "gigascience",
        "isme j", "the isme journal", "microbiome", "genome biol evol", "genome biology and evolution",
        "virus evol", "virus evolution", "j virol", "journal of virology", "embo j", "the embo journal",
        "embo rep", "embo reports", "mol syst biol", "molecular systems biology", "genetics",
        "curr biol", "current biology", "dev cell", "developmental cell", "new phytol", "new phytologist"
    }
    return jl in t12_set

def is_tier3(j):
    if is_tier12(j):
        return False
    jl = j.lower().strip()
    if any(ex in jl for ex in ("bmc biol", "bmc med", "nat ", "nature", "plos biol", "plos genet", "plos pathog", "plos comput", "genome", "elife", "pnas", "nucleic acids", "current biol", "plant cell")):
        return False
    t3_keys = [
        "sci rep", "scientific reports", "plos one", "front ", "frontiers",
        "bmc genomics", "bmc microbiol", "bmc bioinform", "bmc plant", "bmc evol", "bmc infect", "bmc cancer", "bmc med genom",
        "viruses", "genes", "microorganisms", "int j mol sci", "international journal of molecular sciences",
        "cancers", "peerj", "msystems", "msphere", "microbiol spectr", "microbiology spectrum",
        "sci data", "scientific data",
        "infect genet evol", "j med virol", "antibiotics", "pathogens", "animals",
        "heliyon", "plos glob public health", "ecol evol", "ecology and evolution",
        "iscience", "life (basel)", "biomolecules", "cells", "ijms", "nar genom bioinform"
    ]
    return any(k in jl for k in t3_keys)

if __name__ == "__main__":
    manifest_orig = json.loads((pr_dir / "manifest.json").read_text())
    manifest_orig["pairs"] = [p for p in manifest_orig["pairs"] if int(p["pair_id"].split("_")[1]) <= 20]
    manifest_orig["wave1_map"] = {k: v for k, v in manifest_orig["wave1_map"].items() if int(k.split("_")[2]) <= 20}
    manifest_orig["wave2_map"] = {k: v for k, v in manifest_orig["wave2_map"].items() if int(k.split("_")[2]) <= 20}
    (pr_dir / "manifest.json").write_text(json.dumps(manifest_orig, indent=2))

    used_pmids = set()
    used_pmcids = set()
    used_pprs = set()

    for jpath in [
        root / "cohorts_200.json",
        root / "ood_exp/manifest.json",
        root / "open_review_exp/manifest_open_review_100.json",
        root / "peer_review_exp/manifest.json",
        root / "secular_trend_exp/manifest_1000.json",
        root / "spond_self_audit/manifest.json",
    ]:
        if not jpath.exists():
            continue
        data = json.loads(jpath.read_text())
        items = data if isinstance(data, list) else [x for v in data.values() if isinstance(v, list) for x in v]
        for it in items:
            if isinstance(it, dict):
                if it.get("pmid"):
                    used_pmids.add(str(it["pmid"]))
                if it.get("pmcid"):
                    used_pmcids.add(str(it["pmcid"]))
                if it.get("ppr_id"):
                    used_pprs.add(str(it["ppr_id"]))

    print(f"Exclusions loaded: {len(used_pmids)} PMIDs, {len(used_pmcids)} PMCIDs, {len(used_pprs)} PPRs")

    queries = [
        'SRC:PPR AND HAS_FT:Y AND PUB_YEAR:2025 AND ("evolution" OR "genomic" OR "transcriptom" OR "microbiome" OR "single-cell" OR "GWAS" OR "phylogen" OR "virus" OR "RNA-seq" OR "metagenom")',
        'SRC:PPR AND HAS_FT:Y AND PUB_YEAR:2024 AND ("evolution" OR "genomic" OR "transcriptom" OR "microbiome" OR "single-cell" OR "GWAS" OR "phylogen" OR "virus" OR "RNA-seq" OR "metagenom")',
        'SRC:PPR AND HAS_FT:Y AND PUB_YEAR:2025',
        'SRC:PPR AND HAS_FT:Y AND PUB_YEAR:2024',
    ]

    raw_pairs = []
    seen_pmids = set(used_pmids)

    for q in queries:
        cursor = "*"
        for _ in range(20):
            url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&resultType=core&pageSize=100&cursorMark={urllib.parse.quote(cursor)}&format=json"
            try:
                d = json.loads(urllib.request.urlopen(url, timeout=15).read().decode())
                res = d.get("resultList", {}).get("result", [])
                next_cursor = d.get("nextCursorMark")
                if not res:
                    break
                for r in res:
                    ppr_id = r.get("id", "")
                    if not ppr_id.startswith("PPR") or ppr_id in used_pprs:
                        continue
                    if int(ppr_id[3:]) < 950000:
                        continue
                    ppr_date = r.get("firstPublicationDate", "")
                    ccl = r.get("commentCorrectionList", {}).get("commentCorrection", [])
                    for c in ccl:
                        if c.get("type") == "Preprint of" and c.get("source") == "MED":
                            pmid = str(c.get("id", ""))
                            if pmid and pmid not in seen_pmids:
                                seen_pmids.add(pmid)
                                raw_pairs.append({
                                    "ppr_id": ppr_id,
                                    "ppr_doi": r.get("doi", ""),
                                    "ppr_year": int(r.get("pubYear", 0)),
                                    "ppr_date": ppr_date,
                                    "pmid": pmid,
                                    "title": r.get("title", ""),
                                })
                if not next_cursor or next_cursor == cursor:
                    break
                cursor = next_cursor
            except Exception:
                break

    print("Total candidate linked pairs:", len(raw_pairs))

    matched_pairs = []
    for i in range(0, len(raw_pairs), 40):
        batch = raw_pairs[i:i+40]
        pmids_q = " OR ".join(["EXT_ID:" + x["pmid"] for x in batch])
        u2 = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=({urllib.parse.quote(pmids_q)})%20AND%20HAS_FT:Y%20AND%20OPEN_ACCESS:Y&resultType=lite&pageSize=100&format=json"
        try:
            d2 = json.loads(urllib.request.urlopen(u2, timeout=15).read().decode())
            med_map = {str(m.get("pmid")): m for m in d2.get("resultList", {}).get("result", [])}
            for p in batch:
                m = med_map.get(p["pmid"])
                if m and m.get("pmcid") and m.get("pmcid") not in used_pmcids:
                    j = m.get("journalTitle", "")
                    p["pmcid"] = m.get("pmcid")
                    p["journal"] = j
                    p["year"] = int(m.get("pubYear", 0))
                    p["doi"] = m.get("doi", "")
                    p["authors"] = m.get("authorString", "")
                    p["citedByCount"] = int(m.get("citedByCount", 0))
                    matched_pairs.append(p)
        except Exception:
            pass

    t12_pool = [p for p in matched_pairs if is_tier12(p["journal"])]
    t3_pool = [p for p in matched_pairs if is_tier3(p["journal"])]
    print(f"Matched pools with HAS_FT:Y -> Tier 1/2: {len(t12_pool)} | Tier 3: {len(t3_pool)}")

    rng = random.Random(20261029)
    rng.shuffle(t12_pool)
    rng.shuffle(t3_pool)

    def try_fetch_pair(p):
        ppr_id = p["ppr_id"]
        pmcid = p["pmcid"]
        try:
            u_ppr = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{ppr_id}/fullTextXML"
            xml_ppr = urllib.request.urlopen(u_ppr, timeout=12).read()
            ppr_md = parse_xml_manuscript(xml_ppr, p, ppr_id)
            if len(ppr_md) < 12000:
                return None
            u_pub = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
            xml_pub = urllib.request.urlopen(u_pub, timeout=12).read()
            pub_md = parse_xml_manuscript(xml_pub, p, pmcid)
            if len(pub_md) < 12000:
                return None
            return (p, ppr_md, pub_md)
        except Exception:
            return None

    def collect_k(pool, k=15, label="Tier"):
        valid = []
        for cand in pool:
            if len(valid) >= k:
                break
            item = try_fetch_pair(cand)
            if item is not None:
                valid.append(item)
                print(f"  [{label} {len(valid)}/{k}] {item[0]['ppr_id']} -> {item[0]['pmcid']} [{item[0]['journal']}]", flush=True)
        return valid

    t12_valid = collect_k(t12_pool, 15, "T12")
    t3_valid = collect_k(t3_pool, 15, "T3")

    print(f"Fetched valid full-text pairs -> Tier 1/2: {len(t12_valid)} | Tier 3: {len(t3_valid)}")
    assert len(t12_valid) == 15 and len(t3_valid) == 15, f"Got {len(t12_valid)} T12, {len(t3_valid)} T3"

    manifest = json.loads((pr_dir / "manifest.json").read_text())
    existing_pairs = [p for p in manifest["pairs"] if int(p["pair_id"].split("_")[1]) <= 20]

    new_selected = []
    for tier_label, valid_list in [
        ("Tier 1/2 (Selective Flagship/Society)", t12_valid),
        ("Tier 3 (Megajournal / Open-Threshold)", t3_valid),
    ]:
        for p_meta, ppr_md, pub_md in valid_list:
            pair_num = 20 + len(new_selected) + 1
            pair_id = f"PAIR_{pair_num:02d}"
            p_meta["pair_id"] = pair_id
            p_meta["cohort_id"] = pair_id
            p_meta["venue_tier"] = tier_label
            ppr_id = p_meta["ppr_id"]
            pmcid = p_meta["pmcid"]
            (pr_dir / "raw_preprints" / f"{pair_id}_{ppr_id}.md").write_text(ppr_md, encoding="utf-8")
            (pr_dir / "raw_published" / f"{pair_id}_{pmcid}.md").write_text(pub_md, encoding="utf-8")
            new_selected.append((p_meta, ppr_md, pub_md))

    wave1_items = []
    wave2_items = []
    for idx, (p_meta, ppr_md, pub_md) in enumerate(new_selected):
        if idx % 2 == 0:
            wave1_items.append((p_meta, "preprint", ppr_md))
            wave2_items.append((p_meta, "published", pub_md))
        else:
            wave1_items.append((p_meta, "published", pub_md))
            wave2_items.append((p_meta, "preprint", ppr_md))

    rng.shuffle(wave1_items)
    rng.shuffle(wave2_items)

    pair_dict = {p["pair_id"]: p for p, _, _ in new_selected}

    for idx, (p_meta, ver, md) in enumerate(wave1_items, 21):
        w1_id = f"PR_W1_{idx:02d}"
        scrubbed = scrub_doc(md, p_meta, w1_id)
        (pr_dir / "wave1_papers" / f"{w1_id}.md").write_text(scrubbed, encoding="utf-8")
        manifest["wave1_map"][w1_id] = {"pair_id": p_meta["pair_id"], "version": ver}
        pair_dict[p_meta["pair_id"]][f"{ver}_anon_id"] = w1_id
        pair_dict[p_meta["pair_id"]][f"{ver}_wave"] = 1
        pair_dict[p_meta["pair_id"]][f"{ver}_bytes"] = len(scrubbed)

    for idx, (p_meta, ver, md) in enumerate(wave2_items, 21):
        w2_id = f"PR_W2_{idx:02d}"
        scrubbed = scrub_doc(md, p_meta, w2_id)
        (pr_dir / "wave2_papers" / f"{w2_id}.md").write_text(scrubbed, encoding="utf-8")
        manifest["wave2_map"][w2_id] = {"pair_id": p_meta["pair_id"], "version": ver}
        pair_dict[p_meta["pair_id"]][f"{ver}_anon_id"] = w2_id
        pair_dict[p_meta["pair_id"]][f"{ver}_wave"] = 2
        pair_dict[p_meta["pair_id"]][f"{ver}_bytes"] = len(scrubbed)

    manifest["pairs"] = existing_pairs + list(pair_dict.values())
    with open(pr_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Successfully expanded peer_review_exp to {len(manifest['pairs'])} pairs (PR_W1_21..50 and PR_W2_21..50)!")
