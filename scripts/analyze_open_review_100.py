from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
#!/usr/bin/env python3
"""
Analyze the N=100 Open-Review Cohort (Stage 1 Blinded AI Reviews + Verbatim Human Referee Reports)
and generate `/Users/sergei/Projects/lit-estimation/open_review_exp/open_review_results_100.json`.
"""

import json
import math
import re
import statistics
from pathlib import Path
from scipy import stats

ROOT = Path(str(REPO_ROOT))
OPEN_DIR = ROOT / "open_review_exp"
MANIFEST_PATH = OPEN_DIR / "manifest_open_review_100.json"
REVIEWS_DIR = OPEN_DIR / "reviews"
HUMAN_DIR = OPEN_DIR / "human_reports"
CONCORDANCE_DIR = OPEN_DIR / "concordance"
OUT_JSON = OPEN_DIR / "open_review_results_100.json"

SCORE_RE = re.compile(
    r"\*\*Composite Score:\*\*\s*([0-9.]+)\s*/\s*10(?:\.0)?\s*"
    r"\(\s*Rigor:\s*([0-9.]+)\s*/\s*3\.5\s*\|\s*"
    r"Claims:\s*([0-9.]+)\s*/\s*2\.5\s*\|\s*"
    r"Biology:\s*([0-9.]+)\s*/\s*2\.0\s*\|\s*"
    r"Reproducibility:\s*([0-9.]+)\s*/\s*2\.0\s*\)",
    re.I,
)

FIELD_RES = {
    "bias_category": re.compile(r"\*\*Bias Category:\*\*\s*(.+)"),
    "verdict": re.compile(r"\*\*Verdict:\*\*\s*(.+)"),
    "study_modality": re.compile(r"\*\*Study Modality:\*\*\s*(.+)"),
    "tech_maturity": re.compile(r"\*\*Technology Maturity:\*\*\s*(.+)"),
    "epistemic_stage": re.compile(r"\*\*Epistemic Stage:\*\*\s*(.+)"),
}

BOILERPLATE_PATTERNS = [
    r"Thank you for submitting your manuscript to",
    r"Please submit your revised manuscript by",
    r"A rebuttal letter that responds to each point",
    r"A marked-up copy of your manuscript",
    r"An unmarked version of your revised paper",
    r"If you would like to make changes to your financial disclosure",
    r"If applicable, we recommend that you deposit your laboratory protocols",
    r"When submitting your revision, we need you to address these additional requirements",
    r"Please ensure that your manuscript meets PLOS",
    r"While revising your submission, please upload your figure files to the Preflight",
    r"An invoice will be generated when your article is formally accepted",
    r"If your institution or institutions have a press office",
    r"At this stage, our production department will prepare your paper",
    r"You will receive an invoice from PLOS",
    r"Do you want your identity to be public for this peer review",
    r"If you choose “no”, your identity will remain anonymous",
    r"This is an open access article distributed under the terms of the Creative Commons",
]


def parse_ai_review(md_text: str) -> dict:
    m = SCORE_RE.search(md_text)
    if not m:
        raise ValueError("Missing Composite Score header")
    overall = float(m.group(1))
    rigor = float(m.group(2))
    claims = float(m.group(3))
    biology = float(m.group(4))
    repro = float(m.group(5))
    sci_core_8 = round(rigor + claims + biology, 2)

    fields = {}
    for k, pat in FIELD_RES.items():
        fm = pat.search(md_text)
        fields[k] = fm.group(1).strip() if fm else "Unknown"

    # Count numbered methodological critiques in Section 2
    sec2_match = re.search(
        r"###\s*2\.\s*Methodological.*?\n(.*?)(?=\n###\s*3\.|\Z)",
        md_text,
        re.S | re.I,
    )
    sec2_text = sec2_match.group(1) if sec2_match else ""
    ai_critiques = re.findall(r"(?:^|\n)\s*\d+\.\s+\*\*([^\n*]+)\*\*", sec2_text)
    if not ai_critiques:
        ai_critiques = re.findall(r"(?:^|\n)\s*\d+\.\s+([^\n]+)", sec2_text)

    # Extract claim tags in Section 3
    claim_tags = re.findall(
        r"`\[(Well Supported|Moderately Supported|Fragile|Overstated|Methodologically Flawed)\]`",
        md_text,
        re.I,
    )

    # Check if AI flagged arithmetic/statistical/table inconsistency
    sec2_lower = sec2_text.lower()
    has_table_math_error = any(
        kw in sec2_lower
        for kw in [
            "contradict",
            "impossible",
            "mismatch",
            "discrepanc",
            "arithmetic",
            "inverted",
            "reciprocal",
            "sum to",
            "sums to",
            "swapped",
            "degrees of freedom",
            "pseudoreplicat",
            "leakage",
            "unadjusted",
            "multiple testing",
        ]
    )

    ai_words = len(re.findall(r"\b\w+\b", md_text))

    return {
        "overall": overall,
        "rigor": rigor,
        "claims": claims,
        "biology": biology,
        "reproducibility": repro,
        "sci_core_8": sci_core_8,
        **fields,
        "ai_critique_count": len(ai_critiques),
        "ai_critique_titles": [c.strip().rstrip(":") for c in ai_critiques],
        "ai_claim_tags": claim_tags,
        "ai_flagged_hard_math_or_design_flaw": has_table_math_error,
        "ai_word_count": ai_words,
    }


def parse_human_report(md_text: str) -> dict:
    # Split out Author Response sections vs Decision Letter / Reviewer Report sections
    sections = re.split(r"\n#+\s+", "\n" + md_text)
    decision_And_reviewer_chunks = []
    author_response_chunks = []
    decision_rounds = 0

    for sec in sections:
        if not sec.strip():
            continue
        first_line = sec.splitlines()[0].strip().lower()
        if any(
            k in first_line
            for k in ["author response", "response to reviewers", "author's response"]
        ):
            author_response_chunks.append(sec)
        else:
            if any(
                k in first_line
                for k in [
                    "decision letter",
                    "elife assessment",
                    "reviewer #",
                    "reviewer 1",
                    "reviewer 2",
                    "reviewer 3",
                    "open peer review",
                    "peer review",
                ]
            ):
                if "decision letter" in first_line:
                    decision_rounds += 1
            decision_And_reviewer_chunks.append(sec)

    if decision_rounds == 0:
        decision_rounds = max(
            1,
            len(
                re.findall(
                    r"(?:Decision [Ll]etter|eLife [Aa]ssessment|Revision \d|Round \d)",
                    md_text,
                )
            ),
        )

    raw_rev_text = "\n".join(decision_And_reviewer_chunks)
    # Remove standard journal boilerplate paragraphs
    cleaned_lines = []
    for line in raw_rev_text.splitlines():
        l_strip = line.strip()
        if not l_strip:
            continue
        if any(re.search(pat, l_strip, re.I) for pat in BOILERPLATE_PATTERNS):
            continue
        cleaned_lines.append(l_strip)
    cleaned_rev_text = "\n".join(cleaned_lines)

    # Identify distinct reviewer numbers mentioned
    rev_nums = set()
    for m in re.finditer(r"Reviewer\s*#?\s*(\d+)", md_text, re.I):
        rev_nums.add(int(m.group(1)))
    num_reviewers = len(rev_nums) if rev_nums else 2

    human_words_total = len(re.findall(r"\b\w+\b", md_text))
    human_words_referee_clean = len(re.findall(r"\b\w+\b", cleaned_rev_text))
    author_rebuttal_words = len(
        re.findall(r"\b\w+\b", "\n".join(author_response_chunks))
    )

    # Detect coercive / self-citation / DOI-injection demands in referee text
    dois_in_referee = re.findall(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", cleaned_rev_text)
    # Filter out journal's own protocols.io or figshare/plos template DOIs
    external_dois = [
        d
        for d in dois_in_referee
        if not any(
            k in d.lower()
            for k in ["10.1371", "10.7554", "10.6084", "10.5281", "10.7717", "10.1098"]
        )
    ]
    has_citation_demand = bool(
        len(external_dois) >= 2
        or re.search(
            r"(?:cite|citing|include|incorporating|refer to).*?\([A-Z][a-z]+\s+et\s+al\.,\s*\d{4}.*?[A-Z][a-z]+\s+et\s+al\.,\s*\d{4}",
            cleaned_rev_text,
            re.I | re.S,
        )
    )

    return {
        "num_human_reviewers": num_reviewers,
        "decision_rounds": decision_rounds,
        "human_total_words": human_words_total,
        "human_referee_words_clean": human_words_referee_clean,
        "author_rebuttal_words": author_rebuttal_words,
        "human_external_dois_cited": external_dois,
        "human_coercive_citation_flag": has_citation_demand,
    }


def main():
    manifest = json.loads(MANIFEST_PATH.read_text())
    results = []
    missing = []

    # Load all concordance_XXX_YYY.json files
    conc_map = {}
    if CONCORDANCE_DIR.exists():
        for cp in sorted(CONCORDANCE_DIR.glob("concordance_*.json")):
            try:
                cdata = json.loads(cp.read_text(encoding="utf-8"))
                if isinstance(cdata, list):
                    for entry in cdata:
                        if isinstance(entry, dict) and entry.get("anon_id"):
                            conc_map[entry["anon_id"]] = entry
            except Exception as e:
                print(f"Warning reading {cp.name}: {e}")

    for item in manifest:
        aid = item["anon_id"]
        rev_path = REVIEWS_DIR / f"{aid}.md"
        if not rev_path.exists():
            missing.append(aid)
            continue
        rev_text = rev_path.read_text(encoding="utf-8")
        if "</Agent System Instructions>" in rev_text:
            rev_text = rev_text.split("</Agent System Instructions>", 1)[1].strip()
        rev_text = re.sub(r"^<Blinded Review:\s*(OPEN_ANON_\d+)>\s*", r"# Blinded Review: \1\n", rev_text)
        rev_text = re.sub(r"</Blinded Review:\s*OPEN_ANON_\d+>\s*$", "", rev_text).strip() + "\n"
        rev_path.write_text(rev_text, encoding="utf-8")

        ai_data = parse_ai_review(rev_text)

        hum_files = list(HUMAN_DIR.glob(f"{aid}_*_human.md"))
        hum_data = parse_human_report(hum_files[0].read_text(encoding="utf-8")) if hum_files else {}
        hum_rel_path = f"open_review_exp/human_reports/{hum_files[0].name}" if hum_files else ""

        conc_data = conc_map.get(aid)

        rec = {
            **item,
            **ai_data,
            **hum_data,
            "review_path": f"open_review_exp/reviews/{aid}.md",
            "human_review_path": hum_rel_path,
            "concordance": conc_data,
        }
        results.append(rec)

    print(f"Parsed {len(results)} / {len(manifest)} open-review papers (missing: {len(missing)}, concordance: {len(conc_map)})")
    if results:
        sel = [r for r in results if "Selective" in r["venue_tier"]]
        mega = [r for r in results if "Megajournal" in r["venue_tier"]]
        for label, grp in [("All", results), ("Selective", sel), ("Megajournal", mega)]:
            if not grp:
                continue
            scores = [r["overall"] for r in grp]
            cores = [r["sci_core_8"] for r in grp]
            f5 = sum(1 for s in scores if s < 5.0) / len(scores) * 100
            f65 = sum(1 for s in scores if s < 6.5) / len(scores) * 100
            h_words = [r.get("human_referee_words_clean", 0) for r in grp]
            cite_flags = sum(1 for r in grp if r.get("human_coercive_citation_flag"))
            print(
                f"  {label:12s} (n={len(grp):3d}): Mean={statistics.mean(scores):.2f} ± {statistics.stdev(scores) if len(scores)>1 else 0:.2f} "
                f"(Core8={statistics.mean(cores):.2f}) | Med={statistics.median(scores):.2f} | <5.0={f5:.1f}% | <6.5={f65:.1f}% | "
                f"Med Human Referee Words={int(statistics.median(h_words))} | Regex Citation Flags={cite_flags}"
            )

            # Stage 2 Concordance stats if available
            c_grp = [r["concordance"] for r in grp if r.get("concordance")]
            if c_grp:
                all_crit = [c for x in c_grp for c in x.get("human_substantive_critiques", [])]
                unres_crit = [c for c in all_crit if not c.get("resolved_in_published_text", False)]
                direct_all = sum(1 for c in all_crit if "Direct" in str(c.get("ai_recall", "")))
                partial_all = sum(1 for c in all_crit if "Partial" in str(c.get("ai_recall", "")))
                direct_unres = sum(1 for c in unres_crit if "Direct" in str(c.get("ai_recall", "")))
                partial_unres = sum(1 for c in unres_crit if "Partial" in str(c.get("ai_recall", "")))
                ai_only = sum(len(x.get("ai_only_critical_catches", [])) for x in c_grp)
                thorough = sum(1 for x in c_grp if "Thorough" in str(x.get("human_review_depth", "")))
                superficial = sum(1 for x in c_grp if "Superficial" in str(x.get("human_review_depth", "")))
                anoms = sum(1 for x in c_grp if str(x.get("human_reviewer_anomalies", "None")) != "None")
                rec_all_pct = (direct_all + partial_all) / len(all_crit) * 100 if all_crit else 0.0
                rec_unres_pct = (direct_unres + partial_unres) / len(unres_crit) * 100 if unres_crit else 0.0
                print(
                    f"    -> Concordance (n={len(c_grp)}): Total Human Critiques={len(all_crit)} "
                    f"(AI Recall={direct_all+partial_all}/{len(all_crit)} [{rec_all_pct:.1f}%]; "
                    f"Unresolved in Pub={direct_unres+partial_unres}/{len(unres_crit)} [{rec_unres_pct:.1f}%]) | "
                    f"AI-Only Critical Catches={ai_only} ({ai_only/len(c_grp):.1f}/paper) | "
                    f"Depth: Thorough={thorough}, Superficial={superficial} | Reviewer Anomalies={anoms}"
                )

    OUT_JSON.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
