from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
import os
import re
import json
import random

os.makedirs(str(REPO_ROOT / "papers_anon"), exist_ok=True)
os.makedirs(str(REPO_ROOT / "reviews_anon"), exist_ok=True)

with open(str(REPO_ROOT / "cohorts.json")) as f:
    cohorts = json.load(f)

ab_papers = cohorts["cohort_a"] + cohorts["cohort_b"]
rng = random.Random(20261028)
shuffled = list(ab_papers)
rng.shuffle(shuffled)

anon_map = {}

def extract_inline_formulas_from_xml(xml_text):
    """Ensure any <inline-formula> / <tex-math> tags in raw XML/HTML text are unwrapped into inline LaTeX."""
    def _repl(match):
        inner = match.group(1)
        m = re.search(r"\\begin\{document\}\s*(?:\}\{\})?(.*?)\\end\{document\}", inner, re.S)
        if m:
            return f" {m.group(1).strip()} "
        cleaned = re.sub(r"<[^>]+>", " ", inner)
        return " " + " ".join(cleaned.split()) + " "
    return re.sub(r"<(?:inline-formula|disp-formula)[^>]*>(.*?)</(?:inline-formula|disp-formula)>", _repl, xml_text, flags=re.S)

def extract_unified_jats_text(xml_text):
    """
    Unified JATS XML extractor (Issue #20): extracts <abstract>, <body>, <back> (excluding
    <ref-list>, <ack>, and author contributions), and <front>//<custom-meta> Data/Code
    Availability fields while preserving anchor href URLs prior to handle scrubbing.
    """
    xml_text = extract_inline_formulas_from_xml(xml_text)
    # Preserve <ext-link xlink:href="..."> URLs inline before tag stripping
    xml_text = re.sub(
        r'<ext-link[^>]*xlink:href=["\']([^"\']+)["\'][^>]*>(.*?)</ext-link>',
        lambda m: m.group(2) if m.group(1) in m.group(2) else f"{m.group(2)} ({m.group(1)})",
        xml_text,
        flags=re.I | re.S,
    )
    # Extract PLoS / JATS front-matter custom-meta Data Availability if present
    avail_blocks = []
    for m in re.finditer(r"<custom-meta[^>]*>.*?<meta-name>[^<]*data\s*availability[^<]*</meta-name>\s*<meta-value>(.*?)</meta-value>.*?</custom-meta>", xml_text, flags=re.I | re.S):
        val = re.sub(r"<[^>]+>", " ", m.group(1)).strip()
        if val:
            avail_blocks.append(f"## Data Availability\n{val}\n")
    # Remove <ref-list>, <ack>, and <author-notes> from <back>
    xml_text = re.sub(r"<ref-list[^>]*>.*?</ref-list>", "", xml_text, flags=re.I | re.S)
    xml_text = re.sub(r"<ack[^>]*>.*?</ack>", "", xml_text, flags=re.I | re.S)
    xml_text = re.sub(r"<author-notes[^>]*>.*?</author-notes>", "", xml_text, flags=re.I | re.S)
    return xml_text + ("\n" + "\n".join(avail_blocks) if avail_blocks else "")

def scrub_manuscript(txt, meta, anon_id="ANON"):
    txt = extract_unified_jats_text(txt)
    txt = re.sub(r'(?:https?://)?\b(?:github\.com|gitlab\.com|bitbucket\.org)/(?!spond/gemini-reviews\b)[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*', '[CODE_REPO_REDACTED]', txt, flags=re.I)
    lines = txt.splitlines()
    # Drop the top metadata header lines (# A01..., **Title:**..., **Authors:**..., **Venue:**...)
    cleaned_lines = []
    in_body = False
    skip_section = False
    for line in lines:
        s = line.strip()
        if not in_body:
            if s.startswith("## ABSTRACT") or s.startswith("## Abstract") or s.startswith("## MAIN TEXT") or s.startswith("### Abstract") or s.startswith("### Background") or s.startswith("## Introduction") or s.startswith("### Introduction"):
                in_body = True
                cleaned_lines.append(line)
            continue
        # Detect and skip Acknowledgements, Author Contributions, Funding, and Retraction banner sections
        if re.match(r"^#{1,4}\s*(acknowledg|author\s+contribution|funding|competing\s+interest|conflict\s+of\s+interest|retraction)", s, flags=re.IGNORECASE):
            skip_section = True
            continue
        elif re.match(r"^#{1,4}\s+\S", s):
            skip_section = False
        if skip_section:
            continue
        # Skip journal courtesy / license / correspondence / retraction boilerplate lines
        if any(pat in s for pat in [
            "Articles from ",
            "courtesy of ",
            "Corresponding author",
            "Correspondence:",
            "contributed equally",
            "This article is published and distributed under",
            "This article is made available via the PMC Open Access",
            "This article has been retracted",
            "RETRACTED:",
            "Retraction Notice",
            "Received 20",
            "Accepted 20",
            "Published online",
            "Competing interests:",
            "Conflict of interest",
            " Author ",
        ]):
            continue
        cleaned_lines.append(line)

    # Fallback if in_body didn't trigger early enough
    if len("\n".join(cleaned_lines)) < 3000:
        cleaned_lines = []
        for line in lines[5:]:
            s = line.strip()
            if s.startswith("### ") and len(s) < 45 and "," not in s and not any(w in s.lower() for w in ["abstract", "introduction", "method", "result", "discussion", "background", "data", "model", "statistical", "analysis", "conclusion"]):
                # Likely an author name heading from PMC HTML
                continue
            if any(pat in s for pat in ["Articles from ", "courtesy of ", "Corresponding author", "Correspondence:", "contributed equally", "Received 20", "This article has been retracted", "RETRACTED:"]):
                continue
            cleaned_lines.append(line)

    body = "\n".join(cleaned_lines)

    # Strip RETRACTED: / WITHDRAWN: title prefixes anywhere in text
    body = re.sub(r"\b(RETRACTED|WITHDRAWN)\s*:\s*", "", body, flags=re.IGNORECASE)

    # Scrub exact Title (with or without RETRACTED: prefix), DOI, PMCID, PMID, and Journal name
    if meta.get("title"):
        t_clean = re.sub(r"^(RETRACTED|WITHDRAWN)\s*:\s*", "", meta["title"], flags=re.IGNORECASE).rstrip(".")
        if len(t_clean) > 15:
            body = re.sub(re.escape(t_clean), "[REDACTED_TITLE]", body, flags=re.IGNORECASE)
    if meta.get("doi"):
        body = body.replace(meta["doi"], "[REDACTED_DOI]")
    if meta.get("pmcid"):
        body = body.replace(meta["pmcid"], "[REDACTED_ID]")
    if meta.get("pmid"):
        body = body.replace(str(meta["pmid"]), "[REDACTED_ID]")
    if meta.get("journal") and len(meta["journal"]) > 4:
        body = re.sub(r"\b" + re.escape(meta["journal"]) + r"\b", "[REDACTED_VENUE]", body, flags=re.IGNORECASE)

    # Scrub GitHub / GitLab / Bitbucket / Zenodo / Figshare / Galaxy / WorkflowHub URLs, emails, and correspondence lines
    body = re.sub(r"(?im)^.*(?:to whom correspondence|correspondence should be addressed|corresponding author|e-?mail:).*$", "[CORRESPONDENCE_REDACTED]", body)
    body = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}", "[EMAIL_REDACTED]", body)
    body = re.sub(r"(?:https?://)?(?:www\.)?(?:github\.com|gitlab\.com|bitbucket\.org)/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*", "[CODE_REPO_REDACTED]", body, flags=re.IGNORECASE)
    body = re.sub(r"https?://[^\s\)\]>]*usegalaxy[^\s\)\]>]*/u/[A-Za-z0-9_.-]+[^\s\)\]>]*", "[GALAXY_URL_REDACTED]", body, flags=re.IGNORECASE)
    body = re.sub(r"https?://(?:www\.)?workflowhub\.eu/[^\s\)\]>]+", "[WORKFLOWHUB_REDACTED]", body, flags=re.IGNORECASE)
    body = re.sub(r"https?://(?:www\.)?(?:zenodo\.org/records?/\d+|figshare\.com/[^\s\)\]>]+|osf\.io/[A-Za-z0-9]+)", "[ARCHIVE_DOI_REDACTED]", body, flags=re.IGNORECASE)

    # Scrub author surnames from the author list (including short surnames when followed by et al. or year citations)
    common_words = {"wang", "chen", "zhang", "yang", "long", "park", "hill", "wood", "hall", "king", "west", "cole", "ross", "cook", "bell", "ward", "cox", "gray", "hunt", "pond", "love", "berg", "field"}
    if meta.get("authors"):
        for part in meta["authors"].split(","):
            tokens = part.strip().split()
            if tokens:
                surname = tokens[0].strip(".")
                # Always scrub 'Surname et al.' self-citations regardless of surname length
                if len(surname) >= 3:
                    body = re.sub(r"\b" + re.escape(surname) + r"\s+et\s+al\.?", "[AUTHOR et al.]", body, flags=re.IGNORECASE)
                if len(surname) >= 5 and surname.lower() not in common_words:
                    body = re.sub(r"\b" + re.escape(surname) + r"\b", "[AUTHOR]", body)

    # Scrub any post-t0 year mentions (years strictly greater than publication year t0)
    pub_year = meta.get("year")
    if isinstance(pub_year, int) and 1990 <= pub_year <= 2026:
        for future_yr in range(pub_year + 1, 2028):
            body = re.sub(r"\b" + str(future_yr) + r"\b", "[POST_T0_YEAR_REDACTED]", body)

    header = [
        f"# De-Identified Manuscript `{anon_id}`",
        "**Title:** [REDACTED FOR BLINDED REVIEW]",
        "**Authors:** [REDACTED FOR BLINDED REVIEW]",
        "**Venue / Year:** [REDACTED FOR BLINDED REVIEW]",
        "",
    ]
    return "\n".join(header) + "\n" + body

if __name__ == "__main__":
    for idx, meta in enumerate(shuffled, 1):
        anon_id = f"ANON_{idx:02d}"
        pmcid = meta["pmcid"]
        cid = meta["cohort_id"]
        src_path = f"{REPO_ROOT}/papers/{cid}_{pmcid}.md"
        raw_txt = open(src_path).read()
        scrubbed = scrub_manuscript(raw_txt, meta, anon_id)
        out_path = f"{REPO_ROOT}/papers_anon/{anon_id}.md"
        with open(out_path, "w") as f:
            f.write(scrubbed)
        anon_map[anon_id] = {
            "anon_id": anon_id,
            "cohort_id": cid,
            "cohort": meta["cohort"],
            "pmcid": pmcid,
            "pmid": meta["pmid"],
            "title": meta["title"],
            "journal": meta["journal"],
            "year": meta["year"],
            "domain": meta["domain"],
            "scrubbed_bytes": len(scrubbed)
        }

    with open("/tmp/anon_map_ab.json", "w") as f:
        json.dump(anon_map, f, indent=2)

    min_sz = min(v["scrubbed_bytes"] for v in anon_map.values())
    print(f"Created 50 de-identified manuscripts in papers_anon/ (min size: {min_sz} bytes)")
