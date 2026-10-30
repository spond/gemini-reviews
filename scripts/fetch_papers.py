from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
import os
import re
import json
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

os.makedirs(str(REPO_ROOT / "papers"), exist_ok=True)
os.makedirs(str(REPO_ROOT / "reviews"), exist_ok=True)

with open(str(REPO_ROOT / "cohorts.json")) as f:
    cohorts = json.load(f)

all_papers = cohorts["cohort_a"] + cohorts["cohort_b"] + cohorts["cohort_c"]

def normalize_inline_formulas(root):
    """Replace <inline-formula> and <disp-formula> LaTeX preambles with clean inline math text."""
    for tag in ("inline-formula", "disp-formula"):
        for elem in root.findall(f".//{tag}"):
            raw = "".join(elem.itertext())
            m = re.search(r"\\begin\{document\}\s*(?:\}\{\})?(.*?)\\end\{document\}", raw, re.S)
            if m:
                clean_math = m.group(1).strip()
                tail = elem.tail
                elem.clear()
                elem.text = f" {clean_math} "
                elem.tail = tail

def text_of(elem):
    if elem is None:
        return ""
    return " ".join("".join(elem.itertext()).split())

def table_to_md(table_wrap):
    label = text_of(table_wrap.find("label"))
    caption = text_of(table_wrap.find("caption"))
    out = [f"\n#### {label}: {caption}\n"]
    table = table_wrap.find(".//table")
    if table is not None:
        rows = table.findall(".//tr")
        for idx, tr in enumerate(rows[:40]):
            cells = [text_of(c).replace("|", "/") for c in tr.findall("./th") + tr.findall("./td")]
            if cells:
                out.append("| " + " | ".join(cells) + " |")
                if idx == 0:
                    out.append("| " + " | ".join(["---"] * len(cells)) + " |")
        if len(rows) > 40:
            out.append(f"... ({len(rows) - 40} additional rows truncated) ...")
    foot = text_of(table_wrap.find("table-wrap-foot"))
    if foot:
        out.append(f"*{foot}*\n")
    return "\n".join(out)

def parse_jats_xml(xml_bytes, meta):
    root = ET.fromstring(xml_bytes)
    normalize_inline_formulas(root)
    lines = [
        f"# {meta['cohort_id']} ({meta['pmcid']} / PMID:{meta['pmid']})",
        f"**Title:** {meta['title']}",
        f"**Authors:** {meta['authors']}",
        f"**Venue:** {meta['journal']} ({meta['year']}) | **DOI:** {meta.get('doi')}",
        ""
    ]
    # Abstract
    abstracts = root.findall(".//abstract")
    if abstracts:
        lines.append("## ABSTRACT")
        for ab in abstracts:
            lines.append(text_of(ab))
        lines.append("")

    # Body sections
    body = root.find(".//body")
    if body is not None:
        lines.append("## MAIN TEXT")
        for sec in body.findall("./sec"):
            sec_title = text_of(sec.find("title"))
            if sec_title:
                lines.append(f"\n### {sec_title}\n")
            for child in sec:
                if child.tag == "p":
                    lines.append(text_of(child) + "\n")
                elif child.tag == "sec":
                    sub_title = text_of(child.find("title"))
                    if sub_title:
                        lines.append(f"\n#### {sub_title}\n")
                    for subp in child.findall(".//p"):
                        lines.append(text_of(subp) + "\n")
                elif child.tag == "table-wrap":
                    lines.append(table_to_md(child))
        # Any top-level paragraphs if body has no <sec>
        if not body.findall("./sec"):
            for p in body.findall(".//p"):
                lines.append(text_of(p) + "\n")

    # Tables outside sections or all table-wraps
    tables = root.findall(".//table-wrap")
    if tables:
        lines.append("\n## TABLES\n")
        for tw in tables:
            lines.append(table_to_md(tw))

    # Figure captions
    figs = root.findall(".//fig")
    if figs:
        lines.append("\n## FIGURE CAPTIONS\n")
        for fg in figs:
            flabel = text_of(fg.find("label"))
            fcap = text_of(fg.find("caption"))
            lines.append(f"- **{flabel}:** {fcap}")

    return "\n".join(lines)

def fetch_one(meta):
    cid = meta["cohort_id"]
    pmcid = meta["pmcid"]
    out_path = f"{REPO_ROOT}/papers/{cid}_{pmcid}.md"
    if os.path.exists(out_path) and os.path.getsize(out_path) > 2000:
        return (cid, pmcid, "cached", os.path.getsize(out_path))
    
    # Try Europe PMC fullTextXml first
    urls = [
        f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXml",
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid}&retmode=xml"
    ]
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (lit-estimation)"})
            xml_bytes = urllib.request.urlopen(req, timeout=15).read()
            if b"<body" in xml_bytes or b"<abstract" in xml_bytes:
                md = parse_jats_xml(xml_bytes, meta)
                if len(md) > 1500:
                    with open(out_path, "w") as f:
                        f.write(md)
                    return (cid, pmcid, "fullxml", len(md))
        except Exception:
            pass

    # Fallback: fetch abstract + metadata from Europe PMC JSON
    try:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:{pmcid}&resultType=core&format=json"
        data = json.loads(urllib.request.urlopen(url, timeout=15).read().decode())
        r = data["resultList"]["result"][0]
        ab = r.get("abstractText", "")
        md = f"# {cid} ({pmcid} / PMID:{meta['pmid']})\n**Title:** {meta['title']}\n**Authors:** {meta['authors']}\n**Venue:** {meta['journal']} ({meta['year']}) | **DOI:** {meta.get('doi')}\n\n## ABSTRACT\n{ab}\n"
        with open(out_path, "w") as f:
            f.write(md)
        return (cid, pmcid, "abstract_only", len(md))
    except Exception as e:
        return (cid, pmcid, f"error:{e}", 0)

with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(fetch_one, all_papers))

full_cnt = sum(1 for r in results if r[2] in ("fullxml", "cached") and r[3] > 5000)
ab_only = [r for r in results if r[3] <= 5000]
print(f"Full text (>5KB) retrieved: {full_cnt}/75")
for r in ab_only:
    print("  Short/Abstract only:", r)
