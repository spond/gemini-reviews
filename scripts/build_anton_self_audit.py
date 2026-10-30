from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
#!/usr/bin/env python3
"""
Fetch, extract, and strictly de-identify all full-text PubMed Central papers matching:
  nekrutenko[au] OR nekrutenko a[au]
Saves:
- /Users/sergei/Projects/lit-estimation/anton_self_audit/raw_papers/AN_RAW_XXX_PMCXXXX.md
- /Users/sergei/Projects/lit-estimation/anton_self_audit/anon_papers/AN_ANON_XXX.md
- /Users/sergei/Projects/lit-estimation/anton_self_audit/manifest.json
"""
import json
import random
import re
import threading
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from bs4 import BeautifulSoup

ncbi_lock = threading.Lock()

base_dir = Path(str(REPO_ROOT))
an_dir = base_dir / "anton_self_audit"
for sub in ["raw_papers", "anon_papers", "reviews"]:
    (an_dir / sub).mkdir(parents=True, exist_ok=True)

COMMON_SURNAMES = {
    "smith", "brown", "white", "green", "black", "young", "hall", "allen",
    "wright", "scott", "adams", "baker", "nelson", "carter", "mitchell",
    "perez", "roberts", "turner", "phillips", "campbell", "parker", "evans",
    "edwards", "collins", "stewart", "sanchez", "morris", "rogers", "reed",
    "cook", "morgan", "bell", "murphy", "bailey", "rivera", "cooper",
    "richardson", "cox", "howard", "ward", "torres", "peterson", "gray",
    "ramirez", "james", "watson", "brooks", "kelly", "sanders", "price",
    "bennett", "wood", "barnes", "ross", "henderson", "coleman", "jenkins",
    "perry", "powell", "long", "patterson", "hughes", "flores", "washington",
    "butler", "simmons", "foster", "gonzales", "bryant", "alexander",
    "russell", "griffin", "diaz", "hayes", "taylor", "thomas", "jackson",
    "martin", "lee", "thompson", "harris", "clark", "lewis", "robinson",
    "walker", "miller", "davis", "garcia", "rodriguez", "wilson", "martinez",
    "anderson", "moore", "johnson", "williams", "jones", "huang", "zhang",
    "wang", "chen", "liu", "yang", "zhao", "zhou", "wu", "xu", "sun", "ma",
    "zhu", "hu", "guo", "he", "lin", "luo", "zheng", "liang", "xie", "tang",
    "han", "cao", "xiong", "deng", "fischer", "weber", "meyer", "wagner",
    "becker", "schulz", "hoffmann", "koch", "bauer", "richter", "klein",
    "wolf", "schroeder", "neumann", "schwarz", "zimmermann", "braun",
    "krueger", "hofmann", "hartmann", "lange", "schmitt", "werner", "schmitz",
    "krause", "meier", "lehmann", "schmid", "schulze", "maier", "koehler",
    "herrmann", "koenig", "walter", "mayer", "huber", "kaiser", "fuchs",
    "peters", "lang", "scholz", "moeller", "weiss", "jung", "hahn", "keller",
    "vogel", "friedrich", "gunther", "berger", "winkler", "roth", "beck",
    "lorenz", "baumann", "franke", "albrecht", "schuster", "simon", "ludwig",
    "boehm", "winter", "kraus", "martin", "schumacher", "kramer", "vogt",
    "stein", "jaeger", "otto", "sommer", "gross", "seidel", "heinrich",
    "brandt", "haas", "schreiber", "graf", "dietrich", "ziegler", "kuhn",
    "kuehn", "pohl", "engel", "horn", "busch", "bergmann", "thomas", "voigt",
    "sauer", "arnold", "wolff", "pfeiffer", "model", "power", "field",
    "fields", "group", "table", "figure", "method", "methods", "result",
    "results", "study", "studies", "sample", "samples", "human", "mouse",
    "virus", "viral", "cancer", "tumor", "normal", "control", "controls",
    "value", "values", "score", "scores", "level", "levels", "state",
    "states", "class", "classes", "order", "orders", "family", "families",
    "species", "genus", "branch", "branches", "tree", "trees", "site",
    "sites", "codon", "codons", "gene", "genes", "protein", "proteins",
    "sequence", "sequences", "align", "alignment", "alignments", "blank",
    "knight", "church", "house", "cross", "stone", "grave", "graves",
    "marsh", "banks", "wells", "woods", "burns", "sharp", "grant", "mason",
    "hunter", "weaver", "tucker", "peters", "mills", "nichols", "palmer"
}

def clean_text(el):
    if el is None:
        return ""
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()

def extract_surnames(author_str: str) -> list[str]:
    surnames = []
    for part in author_str.rstrip(".").split(","):
        p = part.strip()
        if not p:
            continue
        tokens = p.split()
        if len(tokens) >= 2:
            surname = " ".join(tokens[:-1]).strip()
        else:
            surname = tokens[0].strip()
        surname_clean = re.sub(r"[^A-Za-z\-]", "", surname)
        if len(surname_clean) >= 3:
            surnames.append(surname_clean)
    return surnames

def scrub_anton_manuscript(raw_md: str, meta: dict, anon_id: str) -> str:
    lines = raw_md.splitlines()
    body_lines = []
    in_body = False
    for line in lines:
        if line.strip().startswith("## Abstract"):
            in_body = True
        if in_body:
            body_lines.append(line)
    text = "\n".join(body_lines) if body_lines else raw_md

    # Scrub title
    title = meta.get("title", "")
    if title and len(title) > 12:
        text = re.sub(re.escape(title), "[TITLE REDACTED]", text, flags=re.IGNORECASE)
        t_clean = re.sub(r"<[^>]+>", "", title).strip().rstrip(".")
        if len(t_clean) > 12:
            text = re.sub(re.escape(t_clean), "[TITLE REDACTED]", text, flags=re.IGNORECASE)

    # Scrub journal
    journal = meta.get("journal", "")
    if journal and len(journal) > 3:
        text = re.sub(re.escape(journal), "[JOURNAL REDACTED]", text, flags=re.IGNORECASE)

    # Scrub identifiers
    for k in ("pmcid", "pmid", "doi"):
        val = str(meta.get(k, "")).strip()
        if val:
            text = re.sub(re.escape(val), f"[{k.upper()}_REDACTED]", text, flags=re.IGNORECASE)

    # Scrub Anton Nekrutenko and co-author self-citations
    text = re.sub(r"\bNekrutenko\b", "[AUTHOR]", text, flags=re.IGNORECASE)
    surnames = extract_surnames(meta.get("authors", ""))
    for s in surnames:
        text = re.sub(rf"\b{re.escape(s)}\s+et\s+al\.", "[AUTHOR et al.]", text, flags=re.IGNORECASE)
        if len(s) >= 5 and s.lower() not in COMMON_SURNAMES:
            text = re.sub(rf"\b{re.escape(s)}\b", "[AUTHOR]", text, flags=re.IGNORECASE)

    # Scrub correspondence lines, emails, lab domains, and recognizable software/platform/institution identifiers
    text = re.sub(r"(?im)^.*(?:to whom correspondence|correspondence should be addressed|corresponding author|e-?mail:).*$", "[CORRESPONDENCE_REDACTED]", text)
    text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}", "[EMAIL_REDACTED]", text)
    text = re.sub(r"https?://[^\s\)\]>]*usegalaxy[^\s\)\]>]*", "[GALAXY_URL_REDACTED]", text, flags=re.IGNORECASE)
    text = re.sub(r"[A-Za-z0-9._-]*nekrut[A-Za-z0-9._/-]*", "[AUTHOR_HANDLE_REDACTED]", text, flags=re.IGNORECASE)
    text = re.sub(r"\b(?:Galaxy|UseGalaxy|GalaxyProject|Planemo|DuNovo|Du\s+Novo|BioBlend|Pulsar|CloudMan|CVMFS|HyPhy|Datamonkey|HIV-TRACE)\b", "[SOFTWARE]", text, flags=re.IGNORECASE)
    text = re.sub(r"\b(?:Pennsylvania\s+State\s+University|Penn\s+State)\b", "[INSTITUTION_REDACTED]", text, flags=re.IGNORECASE)

    # Scrub GitHub / GitLab / Bitbucket repo links
    text = re.sub(r"(?:https?://)?(?:www\.)?(?:github\.com|gitlab\.com|bitbucket\.org)/[A-Za-z0-9_.\-]+(?:/[A-Za-z0-9_.\-]+)*", "[CODE_REPO_REDACTED]", text, flags=re.IGNORECASE)

    # Scrub 4-digit years (19XX / 20XX) for temporal blinding
    text = re.sub(r"\b(19\d{2}|20[0-2]\d)\b", "[YEAR]", text)

    # Cut trailing Acknowledgments / Author Contributions / Funding / Competing Interests sections
    text = re.sub(
        r"\n##\s*(Acknowledgments|Acknowledgements|Funding|Author Contributions|Competing Interests|Conflict of Interest|Declarations|References|Bibliography)\b.*",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    header = (
        f"# De-Identified Manuscript: {anon_id}\n\n"
        f"> **Blinding Note:** All title, author, affiliation, journal, year, software, and identifier metadata have been scrubbed for unbiased methodological review.\n\n"
    )
    return header + text.strip() + "\n"

def determine_authorship_role(author_str: str) -> tuple[str, int]:
    al = [x.strip() for x in author_str.rstrip(".").split(",") if x.strip()]
    n_auth = max(len(al), 1)
    if not al:
        return ("Co-Author (Middle)", 1)
    first_match = "nekrutenko" in al[0].lower()
    last_match = "nekrutenko" in al[-1].lower()
    if first_match and n_auth == 1:
        return ("First Author (Solo)", 1)
    elif first_match:
        return ("First Author", n_auth)
    elif last_match:
        return ("Senior / Last Author", n_auth)
    else:
        return ("Co-Author (Middle)", n_auth)

def fetch_one_paper(h: dict):
    pmcid = h.get("pmcid", "")
    pmid = str(h.get("pmid", ""))
    title = re.sub(r"<[^>]+>", "", h.get("title", "")).strip()
    journal = h.get("journalInfo", {}).get("journal", {}).get("title", "") or h.get("journalTitle", "")
    yr = int(h.get("pubYear", 2020))
    author_str = h.get("authorString", "")
    role, n_auth = determine_authorship_role(author_str)
    if yr < 2010:
        decade = "2000s (2000–2009)"
    elif yr < 2020:
        decade = "2010s (2010–2019)"
    else:
        decade = "2020s (2020–2026)"

    meta = {
        "pmcid": pmcid,
        "pmid": pmid,
        "doi": h.get("doi", ""),
        "title": title,
        "authors": author_str,
        "author_count": n_auth,
        "authorship_role": role,
        "is_first_or_senior": role.startswith("First") or role.startswith("Senior"),
        "journal": journal,
        "year": yr,
        "decade": decade,
        "citedByCount": int(h.get("citedByCount", 0)),
    }

    # 1. Try Europe PMC JATS XML
    for attempt in range(3):
        try:
            url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            xml_bytes = urllib.request.urlopen(req, timeout=15).read()
            soup = BeautifulSoup(xml_bytes, "xml")
            # Strip ref-list
            for rl in soup.find_all("ref-list"):
                rl.decompose()
            body = soup.find("body")
            if body and len(body.get_text(" ", strip=True)) >= 2500:
                abs_el = soup.find("abstract")
                abs_txt = clean_text(abs_el) if abs_el else ""
                lines = [
                    f"# {pmcid} ({yr})",
                    f"**Title:** {title}",
                    f"**Authors:** {author_str}",
                    f"**Journal:** {journal} ({yr})",
                    "",
                    "## Abstract",
                    abs_txt,
                    "",
                    "## Main Text",
                ]
                for el in body.find_all(["sec", "p", "preformat", "table-wrap", "fig"]):
                    if el.name == "sec":
                        st = el.find("title")
                        if st and el.parent == body:
                            lines.append(f"\n## {clean_text(st)}\n")
                    elif el.name in ("p", "preformat"):
                        if el.find_parent(["table-wrap", "fig"]):
                            continue
                        t = clean_text(el)
                        if len(t) > 20:
                            lines.append(t + "\n")
                    elif el.name == "fig":
                        cap = clean_text(el.find("caption"))
                        if cap:
                            lines.append(f"\n**Figure:** {cap}\n")
                    elif el.name == "table-wrap":
                        cap = clean_text(el.find("caption"))
                        if cap:
                            lines.append(f"\n**Table:** {cap}\n")
                        for tr in el.find_all("tr")[:35]:
                            cells = [clean_text(c) for c in tr.find_all(["th", "td"])]
                            if cells:
                                lines.append("| " + " | ".join(cells) + " |")
                # Extract Data/Code Availability from <back> if present
                back = soup.find("back")
                if back:
                    for el in back.find_all(["sec", "notes", "fn-group"]):
                        txt = clean_text(el)
                        if any(k in txt.lower() for k in ["data availability", "code availability", "availability of data", "accession", "bioproject", "sra", "zenodo", "figshare"]):
                            lines.append(f"\n## Data and Code Availability\n{txt}\n")
                md = "\n".join(lines)
                if len(md) >= 3500:
                    return (meta, md)
            break
        except Exception:
            time.sleep(0.4)

    # 2. Fallback to NCBI PMC HTML (serialized via ncbi_lock to prevent HTTP 429)
    for attempt in range(3):
        try:
            with ncbi_lock:
                time.sleep(0.5)
                url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                html = urllib.request.urlopen(req, timeout=20).read()
            soup = BeautifulSoup(html, "html.parser")
            art = soup.find("article")
            if not art:
                break
            for r in art.find_all("section", class_="ref-list"):
                r.decompose()
            lines = [
                f"# {pmcid} ({yr})",
                f"**Title:** {title}",
                f"**Authors:** {author_str}",
                f"**Journal:** {journal} ({yr})",
                "",
                "## Abstract",
            ]
            for el in art.find_all(["h2", "h3", "p", "table"]):
                if el.name in ("h2", "h3"):
                    t = clean_text(el)
                    if t and t.lower() not in ("references", "acknowledgments", "acknowledgements"):
                        lines.append(f"\n## {t}\n")
                elif el.name == "p":
                    t = clean_text(el)
                    if len(t) > 20:
                        lines.append(t + "\n")
                elif el.name == "table":
                    for tr in el.find_all("tr")[:35]:
                        cells = [clean_text(c) for c in tr.find_all(["th", "td"])]
                        if cells:
                            lines.append("| " + " | ".join(cells) + " |")
            md = "\n".join(lines)
            if len(md) >= 3500:
                return (meta, md)
            break
        except Exception:
            time.sleep(1.0)

    return None

def main():
    q_epmc = '(AUTH:"Nekrutenko" OR AUTH:"Nekrutenko A")'
    u_epmc = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q_epmc)}&format=json&pageSize=500&resultType=core"
    hits = json.loads(urllib.request.urlopen(u_epmc, timeout=15).read()).get("resultList", {}).get("result", [])

    seen_pmcids = set()
    cands = []
    for h in hits:
        pmcid = h.get("pmcid", "")
        pmid = str(h.get("pmid", ""))
        if not pmcid or pmcid in seen_pmcids:
            continue
        if "nekrutenko" not in h.get("authorString", "").lower():
            continue
        t_low = h.get("title", "").lower()
        if any(w in t_low for w in ["erratum", "correction to:", "corrigendum", "author correction", "publisher correction", "retraction"]):
            continue
        if not pmid:
            continue
        seen_pmcids.add(pmcid)
        cands.append(h)

    print(f"Candidate non-errata PubMed Central articles with PMCID: {len(cands)}")

    fetched = []
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(fetch_one_paper, h): h for h in cands}
        for idx, fut in enumerate(as_completed(futs), 1):
            res = fut.result()
            if res:
                fetched.append(res)
            if idx % 20 == 0 or idx == len(cands):
                print(f"  Progress: {idx}/{len(cands)} checked | {len(fetched)} full texts extracted")

    fetched.sort(key=lambda x: (x[0]["year"], x[0]["pmid"]))
    print(f"Successfully extracted full text for {len(fetched)} papers!")

    for sub in ["raw_papers", "anon_papers"]:
        for f in (an_dir / sub).glob("*.md"):
            f.unlink()

    for idx, (meta, md) in enumerate(fetched, 1):
        meta["an_id"] = f"AN_RAW_{idx:03d}"
        (an_dir / "raw_papers" / f"{meta['an_id']}_{meta['pmcid']}.md").write_text(md, encoding="utf-8")

    rng = random.Random(20261029)
    shuffled = list(fetched)
    rng.shuffle(shuffled)

    manifest = {"papers": [], "anon_to_an": {}}
    for idx, (meta, md) in enumerate(shuffled, 1):
        anon_id = f"AN_ANON_{idx:03d}"
        meta["anon_id"] = anon_id
        scrubbed = scrub_anton_manuscript(md, meta, anon_id)
        meta["scrubbed_bytes"] = len(scrubbed)
        (an_dir / "anon_papers" / f"{anon_id}.md").write_text(scrubbed, encoding="utf-8")
        manifest["anon_to_an"][anon_id] = meta["an_id"]
        manifest["papers"].append(meta)

    manifest["papers"].sort(key=lambda x: x["an_id"])
    with open(an_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)

    roles = {}
    decades = {}
    for m, _ in fetched:
        roles[m["authorship_role"]] = roles.get(m["authorship_role"], 0) + 1
        decades[m["decade"]] = decades.get(m["decade"], 0) + 1
    print("Breakdown by Authorship Role:", roles)
    print("Breakdown by Decade:", decades)

if __name__ == "__main__":
    main()
