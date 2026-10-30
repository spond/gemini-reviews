#!/usr/bin/env python3
"""
Unblind and analyze all N = 74 full-text PubMed Central papers by Anton Nekrutenko
and generate ANTON_SELF_AUDIT.md dynamically from the parsed reviews.
"""
import json
import re
from pathlib import Path
import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parent
base_dir = ROOT.parent if ROOT.name == "scripts" else ROOT
an_dir = base_dir / "anton_self_audit"

manifest = json.loads((an_dir / "manifest.json").read_text())

def parse_review(md_path: Path):
    txt = md_path.read_text(encoding="utf-8")
    m_comp = re.search(
        r"\*\*Composite Score:\*\*\s*([0-9.]+)\s*(?:/\s*10\.0)?\s*\(Rigor:\s*([0-9.]+)/3\.5\s*\|\s*Claims:\s*([0-9.]+)/2\.5\s*\|\s*Biology:\s*([0-9.]+)/2\.0\s*\|\s*Reproducibility:\s*([0-9.]+)/2\.0\)",
        txt,
    )
    if m_comp:
        overall = float(m_comp.group(1))
        rigor = float(m_comp.group(2))
        claims = float(m_comp.group(3))
        biology = float(m_comp.group(4))
        repro = float(m_comp.group(5))
    else:
        def find_sub(pat):
            m = re.search(pat, txt, re.IGNORECASE)
            if not m:
                raise ValueError(f"Could not match {pat} in {md_path}")
            return float(m.group(1))

        rigor = find_sub(r"(?:Methodological\s+)?Rigor[^0-9\n]*([0-9.]+)\s*/\s*3\.5")
        claims = find_sub(r"Claim(?:[–\-]Evidence\s+Alignment|s)[^0-9\n]*([0-9.]+)\s*/\s*2\.5")
        biology = find_sub(r"Biolog(?:ical\s+Plausibility|y)[^0-9\n]*([0-9.]+)\s*/\s*2\.0")
        repro = find_sub(r"Reproducibility[^0-9\n]*([0-9.]+)\s*/\s*2\.0")
        m_ov = re.search(r"(?:Overall(?:\s+Composite)?\s+Score|Composite\s+Score)[^0-9\n]*([0-9.]+)\s*/\s*10\.0", txt, re.IGNORECASE)
        overall = float(m_ov.group(1)) if m_ov else round(rigor + claims + biology + repro, 2)

    sci_core = round(rigor + claims + biology, 2)

    m_sum = re.search(r"##+\s*1\.\s*SUMMARY[^\n]*\n+(.*?)(?=\n---|\n##+)", txt, re.DOTALL | re.IGNORECASE)
    summary_note = ""
    if m_sum:
        paras = [x.strip() for x in m_sum.group(1).strip().split("\n\n") if x.strip() and not x.strip().startswith("---")]
        if paras:
            s = paras[-1] if len(paras) > 1 else paras[0]
            s = re.sub(r"\s+", " ", s)
            summary_note = s[:550] + "..." if len(s) > 550 else s

    return {
        "overall": overall,
        "rigor": rigor,
        "claims": claims,
        "biology": biology,
        "reproducibility": repro,
        "sci_core_8": sci_core,
        "summary_note": summary_note,
    }

def fmt_row(label, subset, bold=False, counts_in_pct=True):
    n = len(subset)
    ov = [p["overall"] for p in subset]
    co = [p["sci_core_8"] for p in subset]
    re_ = [p["reproducibility"] for p in subset]
    mean_ov = np.mean(ov)
    sd_ov = np.std(ov, ddof=1) if n > 1 else 0.0
    med_ov = np.median(ov)
    q25, q75 = np.percentile(ov, [25, 75])
    mean_co = np.mean(co)
    mean_re = np.mean(re_)
    n_lt5 = sum(1 for x in ov if x < 5.0)
    n_lt6 = sum(1 for x in ov if x < 6.0)
    n_ge8 = sum(1 for x in ov if x >= 8.0)
    if counts_in_pct:
        s_lt5 = f"{100*n_lt5/n:.1f}% (`{n_lt5}/{n}`)"
        s_lt6 = f"{100*n_lt6/n:.1f}% (`{n_lt6}/{n}`)"
        s_ge8 = f"{100*n_ge8/n:.1f}% (`{n_ge8}/{n}`)"
    else:
        s_lt5 = f"{100*n_lt5/n:.1f}%"
        s_lt6 = f"{100*n_lt6/n:.1f}%"
        s_ge8 = f"{100*n_ge8/n:.1f}%"
    if bold:
        return f"| **{label}** | **{n}** | **{mean_ov:.2f} ± {sd_ov:.2f}** | **{med_ov:.2f} (`{q25:.2f}–{q75:.2f}`)** | **{mean_co:.2f}** | **{mean_re:.2f}** | **{s_lt5}** | **{s_lt6}** | **{s_ge8}** |"
    return f"| {label} | {n} | {mean_ov:.2f} ± {sd_ov:.2f} | {med_ov:.2f} (`{q25:.2f}–{q75:.2f}`) | {mean_co:.2f} | {mean_re:.2f} | {s_lt5} | {s_lt6} | {s_ge8} |"

def main():
    papers = []
    for p in manifest["papers"]:
        anon_id = p["anon_id"]
        rev_path = an_dir / "reviews" / f"{anon_id}_review.md"
        if not rev_path.exists():
            rev_path = an_dir / "reviews" / f"{anon_id}.md"
        rev = parse_review(rev_path)
        papers.append({**p, **rev})

    with open(an_dir / "anton_results_74.json", "w") as f:
        json.dump(papers, f, indent=2)

    by_score = sorted(papers, key=lambda x: (-x["overall"], -x["sci_core_8"], -x["year"]))
    by_year = sorted(papers, key=lambda x: (x["year"], x["pmcid"]))

    ov_all = [p["overall"] for p in papers]
    co_all = [p["sci_core_8"] for p in papers]
    ri_all = [p["rigor"] for p in papers]
    cl_all = [p["claims"] for p in papers]
    bi_all = [p["biology"] for p in papers]
    re_all = [p["reproducibility"] for p in papers]
    q25, q75 = np.percentile(ov_all, [25, 75])

    lt5_papers = [p for p in papers if p["overall"] < 5.0]
    lt6_papers = [p for p in papers if p["overall"] < 6.0]
    ge8_papers = [p for p in papers if p["overall"] >= 8.0]
    ge85_papers = [p for p in papers if p["overall"] >= 8.5]
    t70_84 = [p for p in papers if 7.0 <= p["overall"] < 8.5]
    t50_69 = [p for p in papers if 5.0 <= p["overall"] < 7.0]

    senior = [p for p in papers if "Senior" in p["authorship_role"]]
    first = [p for p in papers if "First" in p["authorship_role"]]
    middle = [p for p in papers if "Middle" in p["authorship_role"]]
    d2000 = [p for p in papers if 2000 <= p["year"] <= 2009]
    d2010 = [p for p in papers if 2010 <= p["year"] <= 2019]
    d2020 = [p for p in papers if p["year"] >= 2020]
    d2020_lead = [p for p in d2020 if "Senior" in p["authorship_role"] or "First" in p["authorship_role"]]

    lt6_desc = ", ".join(f"`{p['anon_id']}` at `{p['overall']:.1f}`" for p in sorted(lt6_papers, key=lambda x: x["overall"]))

    lines = [
        "# Blinded Career Self-Audit: Anton Nekrutenko (`N = 74` PMC Papers, 2000–2026)",
        "",
        "## 1. Executive Summary",
        "",
        "- **Total Full-Text PMC Corpus Audited Blind:** `74 / 74` (`100%` of non-errata PubMed Central articles matching `AUTH:\"Nekrutenko\"`, spanning 2000–2026, with strict software/platform/domain de-identification).",
        f"- **Overall Composite Score (`/10.0`):** Mean **`{np.mean(ov_all):.2f} ± {np.std(ov_all, ddof=1):.2f}`** | Median **`{np.median(ov_all):.2f}`** (`IQR {q25:.2f}–{q75:.2f}`), Range **`{min(ov_all):.1f}–{max(ov_all):.1f}`**.",
        f"- **Scientific Core Score (`/8.0`, excluding Reproducibility):** Mean **`{np.mean(co_all):.2f} / 8.0`** (`Rigor {np.mean(ri_all):.2f}/3.5`, `Claims {np.mean(cl_all):.2f}/2.5`, `Biology {np.mean(bi_all):.2f}/2.0`, `Reproducibility {np.mean(re_all):.2f}/2.0`).",
        f"- **Fundamental Flaws (`< 5.0`):** **`{len(lt5_papers)} / 74` (`{100*len(lt5_papers)/74:.1f}%`)** — compared to `13.4%` in the 320-paper everyday biomedical literature.",
        f"- **Major Flaws (`< 6.0`):** **`{len(lt6_papers)} / 74` (`{100*len(lt6_papers)/74:.1f}%`)** ({lt6_desc}) — compared to `35.0%` in the 320-paper everyday literature and `2.4%` (`4/164`) in Sergei Kosakovsky Pond's self-audit.",
        f"- **Strong / Exemplary Papers (`>= 8.0`):** **`{len(ge8_papers)} / 74` (`{100*len(ge8_papers)/74:.1f}%`)**, and **`{len(ge85_papers)} / 74` (`{100*len(ge85_papers)/74:.1f}%`)** in the `>= 8.5` Exemplary tier.",
        "",
        "---",
        "",
        "## 2. Comparison Across Benchmarks",
        "",
        "| Corpus / Subgroup | Papers ($N$) | Mean ± SD (`/10`) | Median (`IQR`) | Scientific Core (`/8.0`) | Repro (`/2.0`) | `< 5.0` (Fundamental) | `< 6.0` (Major) | `>= 8.0` (Exemplary) |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        fmt_row("Anton Nekrutenko — All Papers (2000–2026)", papers, bold=True, counts_in_pct=True),
        fmt_row("— Senior / Last Author", senior, counts_in_pct=True),
        fmt_row("— First Author (2000–2022)", first, counts_in_pct=True),
        fmt_row("— Middle Co-Author (Consortium / Multi-Lab)", middle, counts_in_pct=True),
        "| **Anton Nekrutenko — By Decade** | | | | | | | | |",
        fmt_row("— 2000s (`2000–2009`)", d2000, counts_in_pct=False),
        fmt_row("— 2010s (`2010–2019`)", d2010, counts_in_pct=False),
        fmt_row("— 2020s (`2020–2026`, All)", d2020, counts_in_pct=False),
        fmt_row("— 2020s (`2020–2026`, First/Senior Only)", d2020_lead, counts_in_pct=False),
        "| **Reference Benchmarks** | | | | | | | | |",
        "| — S. Kosakovsky Pond Self-Audit (`2004–2026`) | 164 | 7.66 ± 0.65 | 7.70 (`7.30–8.10`) | 5.95 | 1.70 | 0.0% | 2.4% | 36.6% |",
        "| — Everyday Biomedical Literature (`8 Fields`) | 320 | 6.13 ± 1.18 | 6.30 (`5.40–7.00`) | 4.65 | 1.48 | 13.4% | 35.0% | 4.4% |",
        "| — Verified Sound Controls (`Cohort B`) | 50 | 8.35 ± 0.69 | 8.50 (`7.90–8.90`) | 6.56 | 1.79 | 0.0% | 0.0% | 76.0% |",
        "| — Retracted / Refuted Controls (`Cohort A`) | 50 | 3.95 ± 1.24 | 4.00 (`3.20–4.60`) | 2.86 | 1.09 | 86.0% | 94.0% | 0.0% |",
        "",
        "---",
        "",
        "## 3. Top 15 Highest-Scoring Papers in Anton's Corpus",
        "",
        "| Rank | Blinded ID | PMCID | Year | Role | Score (`/10`) | Core (`/8`) | Repro (`/2`) | Journal | Title |",
        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |",
    ]

    for idx, p in enumerate(by_score[:15], 1):
        lines.append(
            f"| {idx} | `{p['anon_id']}` | `{p['pmcid']}` | {p['year']} | {p['authorship_role']} | **{p['overall']:.1f}** | {p['sci_core_8']:.1f} | {p['reproducibility']:.1f} | *{p['journal']}* | {p['title']} |"
        )

    lines += [
        "",
        "---",
        "",
        "## 4. The 7 Lowest-Scoring Papers and What BARS Caught Blind",
        "",
    ]

    for p in sorted(papers, key=lambda x: x["overall"])[:7]:
        lines += [
            f"### `{p['anon_id']}` — **{p['overall']:.1f} / 10.0** (`Core {p['sci_core_8']:.1f}/8.0`, `Repro {p['reproducibility']:.1f}/2.0`) — `{p['pmcid']}` ({p['year']})",
            f"- **Citation:** {p['authors']} ({p['year']}). *{p['title']}*. **{p['journal']}** (`{p['authorship_role']}`).",
            f"- **Blinded Diagnostic Summary:** {p['summary_note']}",
            "",
        ]

    lines += [
        "---",
        "",
        "## 5. Complete 74-Paper Master Ledger (Chronological, 2000–2026)",
        "",
        "| # | Year | PMCID | Blinded ID | Role | Score (`/10`) | Rigor (`/3.5`) | Claims (`/2.5`) | Biology (`/2.0`) | Repro (`/2.0`) | Core (`/8.0`) | Journal | Title |",
        "| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |",
    ]

    for idx, p in enumerate(by_year, 1):
        lines.append(
            f"| {idx} | {p['year']} | `{p['pmcid']}` | `{p['anon_id']}` | {p['authorship_role']} | **{p['overall']:.1f}** | {p['rigor']:.1f} | {p['claims']:.1f} | {p['biology']:.1f} | {p['reproducibility']:.1f} | {p['sci_core_8']:.1f} | *{p['journal']}* | {p['title']} |"
        )

    out_md = "\n".join(lines) + "\n"
    (base_dir / "ANTON_SELF_AUDIT.md").write_text(out_md, encoding="utf-8")
    (an_dir / "ANTON_SELF_AUDIT.md").write_text(out_md, encoding="utf-8")
    print(f"Wrote ANTON_SELF_AUDIT.md ({len(out_md)} bytes)")
    print(f"Summary: mean={np.mean(ov_all):.2f} ± {np.std(ov_all, ddof=1):.2f}, med={np.median(ov_all):.2f}, min={min(ov_all):.1f}, max={max(ov_all):.1f}")
    print(f"Core8={np.mean(co_all):.2f}, Rigor={np.mean(ri_all):.2f}, Claims={np.mean(cl_all):.2f}, Bio={np.mean(bi_all):.2f}, Repro={np.mean(re_all):.2f}")
    print(f"Tiers: >=8.5={len(ge85_papers)} ({100*len(ge85_papers)/74:.1f}%), 7.0-8.4={len(t70_84)} ({100*len(t70_84)/74:.1f}%), 5.0-6.9={len(t50_69)} ({100*len(t50_69)/74:.1f}%), <5.0={len(lt5_papers)} ({100*len(lt5_papers)/74:.1f}%)")
    print(f"<6.0={len(lt6_papers)} ({100*len(lt6_papers)/74:.1f}%), >=8.0={len(ge8_papers)} ({100*len(ge8_papers)/74:.1f}%)")
    r_yr, p_yr = stats.pearsonr([p["year"] for p in papers], ov_all)
    print(f"Year trend r={r_yr:.2f}, p={p_yr:.4f}")

if __name__ == "__main__":
    main()
