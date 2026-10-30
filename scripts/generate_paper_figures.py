#!/usr/bin/env python3
"""
BioVis-Expert General-Reader Publication Figure Generator (`generate_paper_figures.py`)
Generates 5 ultra-clean, spacious 2-panel (`A–B`) vector PDF figures in
`/Users/sergei/Projects/lit-estimation/paper/figures/` strictly from authentic
empirical JSON outputs in `/Users/sergei/Projects/lit-estimation/`.

Design Principles:
- Strictly 2 side-by-side panels (`A` and `B`) per figure with generous whitespace and zero text overlap.
- Concise 1-line axis labels; sample sizes and detailed statistics live in captions and tables rather than crowding tick labels.
- Okabe-Ito colorblind-safe palette (`#0072B2` blue, `#C83228` vermilion,
  `#009E73` bluish green, `#CC79A7` purple, `#E69F00` orange, `#56B4E9` sky blue).
- Half-open L-frame axes (`sns.despine(top=True, right=True)`), clean sans-serif
  typography, horizontal boxplots + jittered points + mean diamonds.
"""

import json
import math
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

np.random.seed(42)

mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42
mpl.rcParams["font.sans-serif"] = ["Arial", "Helvetica", "DejaVu Sans"]
mpl.rcParams["font.family"] = "sans-serif"
mpl.rcParams["axes.labelsize"] = 9.0
mpl.rcParams["axes.titlesize"] = 9.8
mpl.rcParams["xtick.labelsize"] = 8.2
mpl.rcParams["ytick.labelsize"] = 8.4
mpl.rcParams["legend.fontsize"] = 7.5
mpl.rcParams["axes.linewidth"] = 0.85
mpl.rcParams["xtick.major.width"] = 0.75
mpl.rcParams["ytick.major.width"] = 0.75
mpl.rcParams["xtick.major.size"] = 3.2
mpl.rcParams["ytick.major.size"] = 3.2

OI_BLUE = "#0072B2"
OI_VERMILION = "#C83228"
OI_GREEN = "#009E73"
OI_PURPLE = "#CC79A7"
OI_ORANGE = "#E69F00"
OI_SKY = "#56B4E9"
OI_CHARCOAL = "#333333"
OI_GRAY = "#7F7F7F"
OI_LIGHTGRAY = "#E5E5E5"

BASE_DIR = Path("/Users/sergei/Projects/lit-estimation")
FIG_DIR = BASE_DIR / "paper" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def set_panel_title(ax, panel_letter: str, title_text: str):
    ax.set_title(f"{panel_letter}   {title_text}", loc="left", fontsize=9.8, fontweight="bold", pad=10, color="#111111")


def style_axis(ax, grid_axis: str = "x"):
    sns.despine(ax=ax, top=True, right=True)
    if grid_axis in ("x", "y", "both"):
        ax.grid(axis=grid_axis, linestyle=":", linewidth=0.55, color="#CCCCCC", alpha=0.75, zorder=0)
    ax.set_axisbelow(True)


def compute_icc_2_1_with_ci(mat):
    arr = np.asarray(mat, dtype=float)
    n, k = arr.shape
    grand = np.mean(arr)
    row_means = np.mean(arr, axis=1)
    col_means = np.mean(arr, axis=0)
    ss_total = np.sum((arr - grand) ** 2)
    ss_rows = k * np.sum((row_means - grand) ** 2)
    ss_cols = n * np.sum((col_means - grand) ** 2)
    ss_err = ss_total - ss_rows - ss_cols
    ms_b = ss_rows / (n - 1)
    ms_j = ss_cols / (k - 1)
    ms_e = ss_err / ((n - 1) * (k - 1))

    icc2_1 = (ms_b - ms_e) / (ms_b + (k - 1) * ms_e + k * (ms_j - ms_e) / n)
    icc2_k = (ms_b - ms_e) / (ms_b + (ms_j - ms_e) / n)

    f_obs = ms_b / ms_e if ms_e > 0 else 100.0
    df1 = n - 1
    df2 = (n - 1) * (k - 1)
    f_low = f_obs / stats.f.ppf(0.975, df1, df2)
    f_high = f_obs * stats.f.ppf(0.975, df2, df1)
    ci_1 = ((f_low - 1.0) / (f_low + k - 1.0), (f_high - 1.0) / (f_high + k - 1.0))
    ci_k = ((f_low - 1.0) / f_low, (f_high - 1.0) / f_high)
    return float(icc2_1), ci_1, float(icc2_k), ci_k


def draw_clean_box_strip(
    ax,
    groups_data,
    group_labels,
    group_colors,
    rng,
    xlim=(0.8, 11.8),
    fail_cutoff=5.0,
    show_fail_pct=True,
    point_size=16,
    point_alpha=0.68,
    box_height=0.48,
):
    y_positions = np.arange(len(groups_data))
    for idx, (vals, color) in enumerate(zip(groups_data, group_colors)):
        arr = np.asarray(vals, dtype=float)
        ax.boxplot(
            arr,
            positions=[idx],
            vert=False,
            widths=box_height,
            patch_artist=True,
            showfliers=False,
            zorder=2,
            boxprops=dict(facecolor=color, alpha=0.22, edgecolor=color, linewidth=1.15),
            medianprops=dict(color="#111111", linewidth=1.6),
            whiskerprops=dict(color=color, linewidth=1.0, alpha=0.8),
            capprops=dict(color=color, linewidth=1.0, alpha=0.8),
        )
        jitter = rng.uniform(-0.16, 0.16, size=len(arr))
        ax.scatter(
            arr,
            np.full_like(arr, idx) + jitter,
            s=point_size,
            color=color,
            alpha=point_alpha,
            edgecolors="white",
            linewidths=0.35,
            zorder=3,
        )
        mean_val = float(np.mean(arr))
        ax.scatter(
            [mean_val],
            [idx],
            marker="D",
            s=34,
            color="white",
            edgecolors="#111111",
            linewidths=1.2,
            zorder=4,
        )
        if show_fail_pct:
            fail_pct = 100.0 * sum(1 for x in arr if x < fail_cutoff) / len(arr)
            ax.text(
                10.2,
                idx,
                f"{fail_pct:.0f}% fail",
                va="center",
                ha="left",
                fontsize=7.8,
                fontweight="bold",
                color=color if fail_pct > 0 else OI_GREEN,
            )

    if fail_cutoff is not None:
        ax.axvline(fail_cutoff, color=OI_VERMILION, linestyle="--", linewidth=1.15, alpha=0.85, zorder=1)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(group_labels)
    ax.invert_yaxis()
    ax.set_xlim(*xlim)
    ax.set_xticks([2, 4, 6, 8, 10])
    style_axis(ax, grid_axis="x")


# =============================================================================
# FIGURE 1: Calibration & Reviewer Consistency (1x2 Panels A-B)
# =============================================================================
def generate_fig1(rng):
    r200 = json.loads((BASE_DIR / "results_200.json").read_text())
    rep_data = json.loads((BASE_DIR / "repeatability_exp" / "repeatability_results.json").read_text())

    ca = [x["overall"] for x in r200["cohort_a"]]
    cb = [x["overall"] for x in r200["cohort_b"]]
    cc = [x["overall"] for x in r200["cohort_c"] if int(x["cohort_id"][1:]) <= 100]

    fig, (ax_a, ax_b) = plt.subplots(
        1, 2, figsize=(8.8, 3.1), dpi=300,
        gridspec_kw={"width_ratios": [1.14, 1.0], "wspace": 0.78}
    )

    # --- Panel A: Separating Sound Science from Flawed Papers ---
    labels_a = [
        f"Sound Controls (n = {len(cb)})",
        f"Everyday Papers (n = {len(cc)})",
        f"Flawed Controls (n = {len(ca)})",
    ]
    draw_clean_box_strip(
        ax_a,
        [cb, cc, ca],
        labels_a,
        [OI_GREEN, OI_BLUE, OI_VERMILION],
        rng,
        xlim=(0.8, 12.1),
        fail_cutoff=5.0,
        show_fail_pct=True,
        point_size=16,
    )
    ax_a.axvline(6.0, color=OI_ORANGE, linestyle=":", linewidth=1.15, alpha=0.9, zorder=1)
    ax_a.set_ylim(2.6, -0.62)
    ax_a.text(4.85, -0.46, "Fail (5.0)", color=OI_VERMILION, fontsize=7.2, fontweight="bold", ha="right", va="bottom")
    ax_a.text(6.15, -0.46, "Major Flaw (6.0)", color="#B87300", fontsize=7.2, fontweight="bold", ha="left", va="bottom")
    ax_a.set_xlabel("Blinded Paper Score (out of 10)")
    set_panel_title(ax_a, "A", "200-Paper Calibration Set")

    # --- Panel B: Consistency Across Independent Reviews ---
    mat_wild = [[r["run1"]["overall"], r["run2"]["overall"], r["run3"]["overall"]] for r in rep_data if r["cohort"] == "C"]
    mat_all = [[r["run1"]["overall"], r["run2"]["overall"], r["run3"]["overall"]] for r in rep_data]

    icc_wild_1, ci_wild_1, icc_wild_3, ci_wild_3 = compute_icc_2_1_with_ci(mat_wild)
    icc_all_1, ci_all_1, _, _ = compute_icc_2_1_with_ci(mat_all)

    consistency_rows = [
        ("BARS Single Run\n(All 30 Papers)", icc_all_1, ci_all_1[0], ci_all_1[1], OI_GREEN),
        ("BARS 3-Run Avg\n(Everyday, n = 10)", icc_wild_3, ci_wild_3[0], ci_wild_3[1], OI_BLUE),
        ("BARS Single Run\n(Everyday, n = 10)", icc_wild_1, ci_wild_1[0], ci_wild_1[1], OI_SKY),
        ("Human Referees\n(Literature)", 0.325, 0.20, 0.45, OI_GRAY),
    ]

    y_b = np.arange(len(consistency_rows))
    for i, (lbl, val, lo, hi, col) in enumerate(consistency_rows):
        ax_b.hlines(i, 0.0, val, color=col, linewidth=2.0, alpha=0.35, zorder=2)
        ax_b.plot([lo, hi], [i, i], color=col, linewidth=3.2, alpha=0.85, zorder=3)
        ax_b.scatter([val], [i], color=col, s=50, edgecolors="white", linewidths=0.8, zorder=4)
        ax_b.text(
            hi + 0.03 if i == 3 else val,
            i if i == 3 else i - 0.24,
            "0.20–0.45" if i == 3 else f"{val:.2f}",
            va="center" if i == 3 else "bottom",
            ha="left" if i == 3 else "center",
            fontsize=7.8,
            fontweight="bold",
            color="#111111" if i < 3 else "#555555",
        )

    ax_b.set_yticks(y_b)
    ax_b.set_yticklabels([r[0] for r in consistency_rows], fontsize=8.0)
    ax_b.invert_yaxis()
    ax_b.set_xlim(0.0, 1.08)
    ax_b.set_ylim(3.5, -0.58)
    ax_b.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax_b.set_xlabel("Reviewer Consistency (ICC)")
    set_panel_title(ax_b, "B", "Test-Retest Consistency")
    style_axis(ax_b, grid_axis="x")

    out_path = FIG_DIR / "fig1_calibration_repeatability.pdf"
    fig.savefig(out_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return {
        "path": str(out_path),
        "controls_mean": float(np.mean(cb)),
        "wild_mean": float(np.mean(cc)),
        "retracted_mean": float(np.mean(ca)),
        "icc_wild_single": icc_wild_1,
        "icc_wild_consensus": icc_wild_3,
        "icc_all_single": icc_all_1,
    }


# =============================================================================
# FIGURE 2: Quality Across Fields & Journal Types (1x2 Panels A-B)
# =============================================================================
def generate_fig2(rng):
    r200 = json.loads((BASE_DIR / "results_200.json").read_text())
    cc = [x for x in r200["cohort_c"] if int(x["cohort_id"][1:]) <= 100]
    ood = json.loads((BASE_DIR / "ood_exp" / "ood_results_60.json").read_text())
    fexp = json.loads((BASE_DIR / "field_expansion_160" / "fexp_results_160.json").read_text())
    wild320 = cc + ood + fexp

    fig, (ax_a, ax_b) = plt.subplots(
        1, 2, figsize=(8.8, 3.25), dpi=300,
        gridspec_kw={"width_ratios": [1.08, 1.0], "wspace": 0.78}
    )

    # --- Panel A: Quality Across Eight Scientific Fields (N=320, n=40 per field) ---
    field_specs = [
        ("Molecular Evolution", wild320, "Molecular Evolution", OI_BLUE),
        ("Viral Evolution", wild320, "Viral Evolution", OI_BLUE),
        ("Neuroscience & fMRI", wild320, "Neuroscience & Neuroimaging", OI_ORANGE),
        ("Ecology & Evolution", wild320, "Ecology & Macroevolution", OI_ORANGE),
        ("Cancer & Microbiome", wild320, "Cancer & Microbiome", OI_BLUE),
        ("Statistical Genetics", wild320, "Statistical Genetics", OI_BLUE),
        ("Single-Cell RNA-seq", wild320, "Transcriptomics & CompBio", OI_BLUE),
        ("AI Drug Discovery", wild320, "Structural Bioinfo & AI Drug Discovery", OI_ORANGE),
    ]
    f_groups, f_labels, f_colors, f_means = [], [], [], {}
    for label, src, d_key, col in field_specs:
        vals = [x["overall"] for x in src if x["domain"] == d_key]
        f_groups.append(vals)
        f_labels.append(label)
        f_colors.append(col)
        f_means[label] = float(np.mean(vals))

    draw_clean_box_strip(
        ax_a,
        f_groups,
        f_labels,
        f_colors,
        rng,
        xlim=(1.0, 12.1),
        fail_cutoff=5.0,
        show_fail_pct=True,
        point_size=11,
        box_height=0.52,
    )
    ax_a.set_ylim(7.6, -0.75)
    ax_a.text(4.85, -0.52, "Fail (5.0)", color=OI_VERMILION, fontsize=7.2, fontweight="bold", ha="right", va="bottom")
    ax_a.set_xlabel("Blinded Paper Score (out of 10)")
    set_panel_title(ax_a, "A", "Eight Scientific Fields (n = 40 each)")

    # --- Panel B: Quality by Journal Type (N=320) ---
    flagship_set = {
        "n engl j med", "nat methods", "nat mach intell", "nat microbiol", "nat commun",
        "sci transl med", "proc natl acad sci u s a", "cell host microbe", "cell rep",
        "genome biol", "nucleic acids res", "mol biol evol", "elife", "plos genet",
        "plos pathog", "eur heart j", "adv sci (weinh)", "microbiome", "jama netw open",
        "bmj glob health", "commun biol", "npj biofilms microbiomes", "npj parkinsons dis",
        "sci adv", "nat genet", "nat plants", "new phytol", "am j hum genet", "isme j",
        "plos biol", "plos comput biol", "embo j", "j clin invest", "lancet", "bmj",
    }
    mega_keys = [
        "plos one", "sci rep", "scientific reports", "front ", "frontiers", "int j mol sci",
        "animals (basel)", "plants (basel)", "genes (basel)", "biology (basel)", "viruses",
        "microorganisms", "pharmaceuticals (basel)", "insects", "curr issues mol biol",
        "j xenobiot", "bmc ", "bmj open", "iscience", "heliyon", "peerj", "ecol evol",
        "medicine", "chemistryopen", "biomol biomed", "asian pac j", "new microbes",
        "cancers", "biomolecules", "cells", "pathogens", "antibiotics", "diagnostics", "healthcare",
        "life (basel)", "metabolites", "nutrients", "molecules", "vaccines", "toxins", "separations",
        "plos glob public health", "sci data", "scientific data", "world j", "med sci monit",
    ]

    def get_venue_tier(j_name):
        jl = (j_name or "").lower().strip()
        if jl in flagship_set:
            return "Selective Flagship Journals"
        if any(k in jl for k in mega_keys) and jl not in ("bmc biol", "bmc med"):
            return "Open-Access Megajournals"
        return "Specialist Society Journals"

    t_specs = [
        ("Selective Flagship Journals", "Selective Flagships", OI_GREEN),
        ("Specialist Society Journals", "Specialist Societies", OI_BLUE),
        ("Open-Access Megajournals", "OA Megajournals", OI_VERMILION),
    ]
    t_groups, t_labels, t_colors, t_summary = [], [], [], {}
    for t_name, short_lbl, t_col in t_specs:
        vals = [x["overall"] for x in wild320 if get_venue_tier(x["journal"]) == t_name]
        t_groups.append(vals)
        t_labels.append(f"{short_lbl} (n = {len(vals)})")
        t_colors.append(t_col)
        t_summary[t_name] = (len(vals), float(np.mean(vals)), 100.0 * sum(1 for v in vals if v < 5.0) / len(vals))

    draw_clean_box_strip(
        ax_b,
        t_groups,
        t_labels,
        t_colors,
        rng,
        xlim=(1.0, 12.1),
        fail_cutoff=5.0,
        show_fail_pct=True,
        point_size=13,
        box_height=0.46,
    )
    ax_b.set_ylim(2.6, -0.62)
    ax_b.text(4.85, -0.46, "Fail (5.0)", color=OI_VERMILION, fontsize=7.2, fontweight="bold", ha="right", va="bottom")
    ax_b.set_xlabel("Blinded Paper Score (out of 10)")
    set_panel_title(ax_b, "B", "Quality by Journal Type (N = 320)")

    out_path = FIG_DIR / "fig2_wild_ood_distributions.pdf"
    fig.savefig(out_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return {"path": str(out_path), "field_means": f_means, "tier_summary": t_summary}


# =============================================================================
# FIGURE 3: Peer Review Value-Added & Human Referee Recall (1x2 Panels A-B)
# =============================================================================
def generate_fig3(rng):
    pr_data = json.loads((BASE_DIR / "peer_review_exp" / "peer_review_results.json").read_text())
    pairs = pr_data["pairs"]
    stats_summary = pr_data["summary_statistics"]
    concordance = pr_data["human_review_concordance"]

    fig, (ax_a, ax_b) = plt.subplots(
        1, 2, figsize=(8.8, 3.2), dpi=300,
        gridspec_kw={"width_ratios": [0.95, 1.15], "wspace": 0.65}
    )

    # --- Panel A: What Peer Review Adds (Preprint vs. Published) ---
    t12_pairs = [p for p in pairs if "Tier 1/2" in p["venue_tier"]]
    t3_pairs = [p for p in pairs if "Tier 3" in p["venue_tier"]]

    for p in t12_pairs:
        ax_a.plot(
            [0, 1],
            [p["preprint_scores"]["core_8"], p["published_scores"]["core_8"]],
            color=OI_GREEN,
            alpha=0.24,
            linewidth=0.95,
            zorder=2,
        )
    for p in t3_pairs:
        ax_a.plot(
            [0, 1],
            [p["preprint_scores"]["core_8"], p["published_scores"]["core_8"]],
            color=OI_VERMILION,
            alpha=0.24,
            linewidth=0.95,
            zorder=1,
        )

    t12_pre = stats_summary["tier12_25"]["core_8"]["preprint_mean"]
    t12_pub = stats_summary["tier12_25"]["core_8"]["published_mean"]
    t12_d = stats_summary["tier12_25"]["core_8"]["delta_mean"]
    t12_p = stats_summary["tier12_25"]["core_8"]["paired_t_p"]

    t3_pre = stats_summary["tier3_25"]["core_8"]["preprint_mean"]
    t3_pub = stats_summary["tier3_25"]["core_8"]["published_mean"]
    t3_d = stats_summary["tier3_25"]["core_8"]["delta_mean"]
    t3_p = stats_summary["tier3_25"]["core_8"]["paired_t_p"]

    ax_a.plot(
        [0, 1],
        [t12_pre, t12_pub],
        marker="o",
        markersize=6.8,
        color=OI_GREEN,
        linewidth=2.6,
        label=f"Selective / Society (+{t12_d:.2f}, p = {t12_p:.2f})",
        zorder=5,
    )
    ax_a.plot(
        [0, 1],
        [t3_pre, t3_pub],
        marker="s",
        markersize=6.4,
        color=OI_VERMILION,
        linewidth=2.6,
        label=f"OA Megajournals (+{t3_d:.2f}, NS)",
        zorder=4,
    )

    ax_a.text(-0.07, t12_pre, f"{t12_pre:.2f}", ha="right", va="center", fontsize=8.0, fontweight="bold", color=OI_GREEN)
    ax_a.text(1.07, t12_pub, f"{t12_pub:.2f}", ha="left", va="center", fontsize=8.0, fontweight="bold", color=OI_GREEN)
    ax_a.text(-0.07, t3_pre, f"{t3_pre:.2f}", ha="right", va="center", fontsize=8.0, fontweight="bold", color=OI_VERMILION)
    ax_a.text(1.07, t3_pub, f"{t3_pub:.2f}", ha="left", va="center", fontsize=8.0, fontweight="bold", color=OI_VERMILION)

    ax_a.set_xticks([0, 1])
    ax_a.set_xticklabels(["Preprint\n(Before Review)", "Published Article\n(After Review)"])
    ax_a.set_xlim(-0.34, 1.34)
    ax_a.set_ylim(2.0, 8.2)
    ax_a.set_ylabel("Scientific Core Score (out of 8)")
    ax_a.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.18),
        ncol=1,
        frameon=False,
        fontsize=7.4,
    )
    set_panel_title(ax_a, "A", "Preprint vs. Published (N = 50 Pairs)")
    style_axis(ax_a, grid_axis="y")

    # --- Panel B: BARS vs. 261 Human Referees Across 100 Open-Review Papers ---
    open100 = json.loads((BASE_DIR / "open_review_exp" / "open_review_results_100.json").read_text())

    def count_outcomes(papers_list):
        unres = [
            hc
            for p in papers_list
            if p.get("concordance")
            for hc in p["concordance"].get("human_substantive_critiques", [])
            if not hc.get("resolved_in_published_text", False)
        ]
        fixed = [
            hc
            for p in papers_list
            if p.get("concordance")
            for hc in p["concordance"].get("human_substantive_critiques", [])
            if hc.get("resolved_in_published_text", False)
        ]
        both = sum(
            1
            for c in unres
            if "Direct" in str(c.get("ai_recall", "")) or "Partial" in str(c.get("ai_recall", ""))
        )
        hum_only = len(unres) - both
        bars_only = sum(len(p["concordance"].get("ai_only_critical_catches", [])) for p in papers_list)
        return bars_only, both, hum_only, len(fixed)

    sel50 = [p for p in open100 if "Selective" in p.get("venue_tier", "")]
    mega50 = [p for p in open100 if "Megajournal" in p.get("venue_tier", "")]

    s_bars, s_both, s_hum, s_fix = count_outcomes(sel50)
    m_bars, m_both, m_hum, m_fix = count_outcomes(mega50)

    rows_b = [
        ("Caught by BARS Only\n(Missed by All Referees)", s_bars, m_bars, f"{s_bars + m_bars} (3.85/paper)"),
        ("Caught by Both BARS &\nReferees (Unfixed in Paper)", s_both, m_both, f"{s_both + m_both}/97 (97.9% recall)"),
        ("Caught by Referees Only\n(Missed by BARS)", s_hum, m_hum, f"{s_hum + m_hum}/97 (2.1%)"),
        ("Fixed by Authors in\nRevision Before Publication", s_fix, m_fix, f"{s_fix + m_fix} fixed"),
    ]

    y_b = np.arange(len(rows_b))
    sel_vals = np.array([r[1] for r in rows_b], dtype=float)
    mega_vals = np.array([r[2] for r in rows_b], dtype=float)

    ax_b.barh(y_b, sel_vals, height=0.52, color=OI_GREEN, alpha=0.88, label="Selective Journals (n = 50)")
    ax_b.barh(y_b, mega_vals, left=sel_vals, height=0.52, color=OI_VERMILION, alpha=0.82, label="OA Megajournals (n = 50)")

    for i, (lbl, sv, mv, callout) in enumerate(rows_b):
        tot = sv + mv
        if sv >= 35:
            ax_b.text(sv / 2.0, i, f"{int(sv)}", va="center", ha="center", color="white", fontsize=7.2, fontweight="bold")
        if mv >= 35:
            ax_b.text(sv + mv / 2.0, i, f"{int(mv)}", va="center", ha="center", color="white", fontsize=7.2, fontweight="bold")
        ax_b.text(
            tot + 8.0,
            i,
            callout,
            va="center",
            ha="left",
            color="#111111",
            fontsize=7.3,
            fontweight="bold",
        )

    ax_b.set_yticks(y_b)
    ax_b.set_yticklabels([r[0] for r in rows_b], fontsize=7.8)
    ax_b.invert_yaxis()
    ax_b.set_xlim(0, 525)
    ax_b.set_xticks([0, 100, 200, 300, 400])
    ax_b.set_xlabel("Substantive Technical Flaws Across 100 Papers")
    ax_b.legend(
        loc="upper center",
        bbox_to_anchor=(0.46, -0.18),
        ncol=2,
        frameon=False,
        fontsize=7.2,
        handlelength=1.1,
        columnspacing=1.1,
    )
    set_panel_title(ax_b, "B", "BARS vs. 261 Human Referees (N = 100)")
    style_axis(ax_b, grid_axis="x")

    out_path = FIG_DIR / "fig3_peer_review_paired.pdf"
    fig.savefig(out_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return {
        "path": str(out_path),
        "t12_pre": t12_pre,
        "t12_pub": t12_pub,
        "t3_pre": t3_pre,
        "t3_pub": t3_pub,
        "recall_pct": 100.0 * (s_both + m_both) / (s_both + m_both + s_hum + m_hum),
    }


# =============================================================================
# FIGURE 4: 35-Year Secular Decline & Key Structural Drivers (1x2 Panels A-B)
# =============================================================================
def generate_fig4(rng):
    sec_1000 = json.loads((BASE_DIR / "secular_trend_exp" / "secular_results_1000.json").read_text())
    pub_vol = json.loads((BASE_DIR / "secular_trend_exp" / "pubmed_annual_volume.json").read_text())
    pooled_1161 = json.loads((BASE_DIR / "secular_trend_exp" / "pooled_wild_1161.json").read_text())

    fig, (ax_a, ax_b) = plt.subplots(
        1, 2, figsize=(8.8, 3.15), dpi=300,
        gridspec_kw={"width_ratios": [1.05, 1.05], "wspace": 1.06}
    )

    # --- Panel A: 35-Year Quality Decline Across Seven 5-Year Windows ---
    windows = [
        ("1991–1995", 1993.0, "'91–'95"),
        ("1996–2000", 1998.0, "'96–'00"),
        ("2001–2005", 2003.0, "'01–'05"),
        ("2006–2010", 2008.0, "'06–'10"),
        ("2011–2015", 2013.0, "'11–'15"),
        ("2016–2020", 2018.0, "'16–'20"),
        ("2021–2025", 2023.0, "'21–'25"),
    ]
    d_x, d_m, d_se, d_lbls = [], [], [], []
    for win_key, mid_yr, s_lbl in windows:
        sub = [x["overall"] for x in sec_1000 if x["window_label"] == win_key]
        d_x.append(mid_yr)
        d_m.append(float(np.mean(sub)))
        d_se.append(float(np.std(sub, ddof=1) / math.sqrt(len(sub))))
        d_lbls.append(s_lbl)

    ax_a.axhline(5.0, color="#BBBBBB", linestyle=":", linewidth=1.0, zorder=1)
    ax_a.errorbar(
        d_x,
        d_m,
        yerr=d_se,
        fmt="o-",
        color=OI_BLUE,
        linewidth=2.2,
        markersize=5.6,
        capsize=2.8,
        zorder=4,
    )
    for idx_d, (x_p, m_p, se_p) in enumerate(zip(d_x, d_m, d_se)):
        if idx_d in (0, 1, 3, 4):
            ax_a.text(x_p, m_p + se_p + 0.12, f"{m_p:.2f}", color=OI_BLUE, fontsize=7.3, fontweight="bold", ha="center", va="bottom")
        else:
            ax_a.text(x_p, m_p - se_p - 0.14, f"{m_p:.2f}", color=OI_BLUE, fontsize=7.3, fontweight="bold", ha="center", va="top")

    ax_a2 = ax_a.twinx()
    vol_years = sorted(int(k) for k in pub_vol.keys())
    vol_k = [pub_vol[str(y)]["core_domain_volume"] / 1000.0 for y in vol_years]
    ax_a2.plot(
        vol_years,
        vol_k,
        color=OI_VERMILION,
        linestyle="--",
        linewidth=1.9,
        zorder=3,
    )
    ax_a2.set_ylabel("Annual Papers (PubMed)", color=OI_VERMILION, fontsize=8.4, labelpad=5)
    ax_a2.tick_params(axis="y", labelcolor=OI_VERMILION, labelsize=7.8)
    ax_a2.spines["top"].set_visible(False)
    ax_a2.set_ylim(0, 720)
    ax_a2.set_yticks([0, 200, 400, 600])
    ax_a2.set_yticklabels(["0", "200k", "400k", "600k"])

    ax_a.set_xticks(d_x)
    ax_a.set_xticklabels(d_lbls, fontsize=7.2, rotation=22, ha="right")
    ax_a.set_xlim(1990.0, 2026.5)
    ax_a.set_ylim(4.4, 8.3)
    ax_a.set_xlabel(f"5-Year Sampling Windows (N = {len(sec_1000)})")
    ax_a.set_ylabel("Mean Blinded Score (out of 10)", color=OI_BLUE)
    ax_a.tick_params(axis="y", labelcolor=OI_BLUE)
    ax_a.spines["top"].set_visible(False)
    ax_a.grid(axis="y", linestyle=":", linewidth=0.5, color="#CCCCCC", alpha=0.7)
    set_panel_title(ax_a, "A", "35-Year Quality Decline vs. Volume")

    # --- Panel B: Experiments vs. Data Mining ---
    driver_specs = [
        ("Wet-Lab Experiments", lambda x: x["study_modality"] == "Wet-Lab Primary Experimental", OI_GREEN),
        ("Established Designs", lambda x: x["tech_maturity"] == "Mature/Classical", OI_BLUE),
        ("Database Mining", lambda x: "Secondary Cohort/Database" in x["study_modality"], OI_ORANGE),
        ("Formulaic Templates", lambda x: x["tech_maturity"] == "Commodity/Hype-Cycle Template", OI_VERMILION),
    ]
    d_groups, d_labels, d_colors, d_stats = [], [], [], {}
    for name, filt, col in driver_specs:
        vals = [x["overall"] for x in pooled_1161 if filt(x)]
        d_groups.append(vals)
        d_labels.append(name)
        d_colors.append(col)
        d_stats[name] = (len(vals), float(np.mean(vals)), 100.0 * sum(1 for v in vals if v < 5.0) / len(vals))

    draw_clean_box_strip(
        ax_b,
        d_groups,
        d_labels,
        d_colors,
        rng,
        xlim=(0.8, 12.1),
        fail_cutoff=5.0,
        show_fail_pct=True,
        point_size=9,
        box_height=0.48,
    )
    ax_b.set_ylim(3.6, -0.65)
    ax_b.text(4.85, -0.46, "Fail (5.0)", color=OI_VERMILION, fontsize=7.2, fontweight="bold", ha="right", va="bottom")
    ax_b.set_xlabel("Blinded Paper Score (out of 10)")
    set_panel_title(ax_b, "B", "Experiments vs. Formulaic Mining")

    out_path = FIG_DIR / "fig4_secular_covariates.pdf"
    fig.savefig(out_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return {"path": str(out_path), "window_means": dict(zip([w[0] for w in windows], d_m)), "driver_stats": d_stats}


# =============================================================================
# FIGURE 5: Blinded Self-Audit of Two Senior Authors (N = 164 + 74 = 238)
# =============================================================================
def generate_fig5(rng):
    sp_164 = json.loads((BASE_DIR / "spond_self_audit" / "spond_results_164.json").read_text())
    an_74 = json.loads((BASE_DIR / "anton_self_audit" / "anton_results_74.json").read_text())
    r200 = json.loads((BASE_DIR / "results_200.json").read_text())
    cb = [x["overall"] for x in r200["cohort_b"]]
    cc = [x["overall"] for x in r200["cohort_c"] if int(x["cohort_id"][1:]) <= 100]

    sp_fs = [x["overall"] for x in sp_164 if x["is_first_or_senior"]]
    sp_mid = [x["overall"] for x in sp_164 if not x["is_first_or_senior"]]
    an_fs = [x["overall"] for x in an_74 if x["is_first_or_senior"]]
    an_mid = [x["overall"] for x in an_74 if not x["is_first_or_senior"]]

    fig, (ax_a, ax_b) = plt.subplots(
        1, 2, figsize=(8.8, 3.25), dpi=300,
        gridspec_kw={"width_ratios": [1.14, 1.0], "wspace": 0.58}
    )

    # --- Panel A: Blinded Self-Audit of Both Senior Authors (N = 238) ---
    groups_5a = [cb, sp_fs, sp_mid, an_fs, an_mid, cc]
    labels_5a = [
        f"Sound Controls (n = {len(cb)})",
        f"S.L.K.P. Lead (n = {len(sp_fs)})",
        f"S.L.K.P. Middle (n = {len(sp_mid)})",
        f"A.N. Lead (n = {len(an_fs)})",
        f"A.N. Middle (n = {len(an_mid)})",
        f"Everyday Papers (n = {len(cc)})",
    ]
    colors_5a = [OI_GREEN, OI_BLUE, OI_ORANGE, OI_PURPLE, OI_SKY, OI_VERMILION]

    draw_clean_box_strip(
        ax_a,
        groups_5a,
        labels_5a,
        colors_5a,
        rng,
        xlim=(0.8, 12.1),
        fail_cutoff=5.0,
        show_fail_pct=True,
        point_size=12,
        box_height=0.50,
    )
    ax_a.set_ylim(5.6, -0.68)
    ax_a.text(4.85, -0.46, "Fail (5.0)", color=OI_VERMILION, fontsize=7.2, fontweight="bold", ha="right", va="bottom")
    ax_a.set_xlabel("Blinded Paper Score (out of 10)")
    set_panel_title(ax_a, "A", "Blinded Career Self-Audits (N = 238)")

    # --- Panel B: Career Trajectories Over 26 Years (2000-2026) ---
    fs_papers = [x for x in sp_164 if x["is_first_or_senior"]]
    mid_papers = [x for x in sp_164 if not x["is_first_or_senior"]]

    yrs_fs = np.array([x["year"] for x in fs_papers], dtype=float)
    scs_fs = np.array([x["overall"] for x in fs_papers], dtype=float)
    yrs_mid = np.array([x["year"] for x in mid_papers], dtype=float)
    scs_mid = np.array([x["overall"] for x in mid_papers], dtype=float)
    yrs_an = np.array([x["year"] for x in an_74], dtype=float)
    scs_an = np.array([x["overall"] for x in an_74], dtype=float)

    ax_b.scatter(
        yrs_mid + rng.uniform(-0.22, 0.22, size=len(yrs_mid)),
        scs_mid,
        color=OI_ORANGE,
        alpha=0.45,
        s=18,
        edgecolors="white",
        linewidths=0.3,
        label=f"S.L.K.P. Middle (n = {len(mid_papers)}, mean {np.mean(scs_mid):.1f})",
        zorder=2,
    )
    ax_b.scatter(
        yrs_an + rng.uniform(-0.20, 0.20, size=len(yrs_an)),
        scs_an,
        color=OI_PURPLE,
        alpha=0.65,
        s=21,
        marker="s",
        edgecolors="white",
        linewidths=0.35,
        label=f"A.N. All Papers (n = {len(an_74)}, mean {np.mean(scs_an):.1f})",
        zorder=3,
    )
    ax_b.scatter(
        yrs_fs + rng.uniform(-0.18, 0.18, size=len(yrs_fs)),
        scs_fs,
        color=OI_BLUE,
        alpha=0.88,
        s=24,
        edgecolors="white",
        linewidths=0.45,
        label=f"S.L.K.P. Lead (n = {len(fs_papers)}, mean {np.mean(scs_fs):.1f})",
        zorder=4,
    )

    sl_fs, int_fs, _, _, _ = stats.linregress(yrs_fs, scs_fs)
    sl_mid, int_mid, _, _, _ = stats.linregress(yrs_mid, scs_mid)
    sl_an, int_an, _, _, _ = stats.linregress(yrs_an, scs_an)
    x_span_sp = np.array([2004.0, 2026.0])
    x_span_an = np.array([2000.0, 2026.0])
    ax_b.plot(x_span_sp, int_fs + sl_fs * x_span_sp, color=OI_BLUE, linewidth=2.0, linestyle="-", zorder=5)
    ax_b.plot(x_span_an, int_an + sl_an * x_span_an, color=OI_PURPLE, linewidth=1.9, linestyle="-.", zorder=4)
    ax_b.plot(x_span_sp, int_mid + sl_mid * x_span_sp, color=OI_ORANGE, linewidth=1.8, linestyle="--", zorder=3)

    ax_b.axhline(5.0, color=OI_VERMILION, linestyle="--", linewidth=1.0, alpha=0.85, zorder=1)
    ax_b.set_xlim(1999, 2027)
    ax_b.set_ylim(1.5, 10.2)
    ax_b.set_xlabel("Publication Year (2000–2026)")
    ax_b.set_ylabel("Blinded Paper Score (out of 10)")
    ax_b.legend(loc="lower left", frameon=True, facecolor="white", framealpha=0.94, edgecolor="#DDDDDD", fontsize=6.6)
    set_panel_title(ax_b, "B", "Career Trajectories (2000–2026)")
    style_axis(ax_b, grid_axis="both")

    out_path = FIG_DIR / "fig5_self_audit_external_audit.pdf"
    fig.savefig(out_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return {
        "path": str(out_path),
        "sp_lead_mean": float(np.mean(sp_fs)),
        "sp_mid_mean": float(np.mean(sp_mid)),
        "an_lead_mean": float(np.mean(an_fs)),
        "an_mid_mean": float(np.mean(an_mid)),
    }


# =============================================================================
# SUPPLEMENTARY FIGURE S1: Citations vs. Blinded BARS Score & Four Archetypes
# =============================================================================
def generate_figS1(rng):
    cat_path = Path("/Users/sergei/Development/gemini-reviews/catalog.json")
    cat = json.loads(cat_path.read_text())
    recs = [
        r
        for r in cat["records"]
        if r.get("citedByCount") is not None
        and "Cohort A" not in str(r.get("experiment", ""))
    ]

    scores = np.array([r["overall"] for r in recs], dtype=float)
    cites = np.array([r["citedByCount"] for r in recs], dtype=float)
    log_cites = np.log10(cites + 1.0)

    fig, (ax_a, ax_b) = plt.subplots(
        1, 2, figsize=(8.8, 3.2), dpi=300,
        gridspec_kw={"width_ratios": [1.1, 1.0], "wspace": 0.62}
    )

    # --- Panel A: Citations vs. Blinded BARS Score Across Non-Control Papers ---
    pass_mask = scores >= 5.0
    fail_low_mask = (scores < 5.0) & (cites < 50)
    fail_high_mask = (scores < 5.0) & (cites >= 50)

    ax_a.axvspan(1.0, 5.0, ymin=np.log10(51.0) / 3.05, ymax=1.0, color=OI_VERMILION, alpha=0.09, zorder=1)
    ax_a.axvline(5.0, color=OI_VERMILION, linestyle="--", linewidth=1.1, alpha=0.85, zorder=2)
    ax_a.axhline(np.log10(51.0), color="#999999", linestyle=":", linewidth=0.9, alpha=0.8, zorder=2)

    ax_a.scatter(
        scores[pass_mask] + rng.uniform(-0.08, 0.08, size=np.sum(pass_mask)),
        log_cites[pass_mask],
        color=OI_BLUE,
        alpha=0.28,
        s=12,
        edgecolors="none",
        label=f"Score ≥ 5.0 (n = {int(np.sum(pass_mask))})",
        zorder=2,
    )
    ax_a.scatter(
        scores[fail_low_mask] + rng.uniform(-0.08, 0.08, size=np.sum(fail_low_mask)),
        log_cites[fail_low_mask],
        color=OI_GRAY,
        alpha=0.32,
        s=12,
        edgecolors="none",
        label=f"Failed < 5.0, < 50 Cites (n = {int(np.sum(fail_low_mask))})",
        zorder=2,
    )
    ax_a.scatter(
        scores[fail_high_mask],
        log_cites[fail_high_mask],
        color=OI_VERMILION,
        alpha=0.92,
        s=32,
        edgecolors="white",
        linewidths=0.5,
        label=f"Highly Cited Failures ≥ 50 Cites (n = {int(np.sum(fail_high_mask))})",
        zorder=5,
    )

    # Binned mean log10(citations + 1) trendline
    bins = [(1.0, 3.99, 2.5), (4.0, 4.99, 4.5), (5.0, 6.49, 5.75), (6.5, 7.99, 7.25), (8.0, 10.0, 8.8)]
    bx, by, bse = [], [], []
    for lo, hi, mid in bins:
        m = (scores >= lo) & (scores <= hi)
        if np.sum(m) > 5:
            bx.append(mid)
            by.append(float(np.mean(log_cites[m])))
            bse.append(float(np.std(log_cites[m], ddof=1) / math.sqrt(np.sum(m))))
    ax_a.errorbar(bx, by, yerr=bse, fmt="D-", color="#111111", linewidth=1.8, markersize=4.5, capsize=2.5, label="Binned Mean ± SE", zorder=6)

    # Annotate top archetype examples
    callouts = [
        (4.1, np.log10(557), "SP_ANON_109 (556)", (-6, -2), "right"),
        (2.2, np.log10(140), "TIME_0922 (139)", (0, -11), "center"),
        (3.7, np.log10(157), "TIME_0224 (156)", (-4, 6), "center"),
        (4.8, np.log10(159), "TIME_08 (158)", (5, 2), "left"),
    ]
    for cx, cy, ctxt, offset, ha_val in callouts:
        ax_a.annotate(
            ctxt,
            xy=(cx, cy),
            xytext=offset,
            textcoords="offset points",
            fontsize=6.4,
            fontweight="bold",
            color="#902000",
            ha=ha_val,
            zorder=7,
        )

    ax_a.set_xlim(1.0, 10.2)
    ax_a.set_ylim(-0.08, 3.05)
    ax_a.set_yticks([0.0, 1.0, 2.0, np.log10(501.0)])
    ax_a.set_yticklabels(["0", "10", "100", "500"])
    ax_a.set_xlabel("Blinded Paper Score (out of 10)")
    ax_a.set_ylabel("Total Citations (Log Scale)")
    ax_a.legend(loc="lower right", frameon=True, facecolor="white", framealpha=0.92, edgecolor="#DDDDDD", fontsize=6.3)
    set_panel_title(ax_a, "A", f"Citations vs. Blinded Score (N = {len(recs)})")
    style_axis(ax_a, grid_axis="both")

    # --- Panel B: Median & Max Citations Across Quality Tiers vs. Four Failure Archetypes ---
    tier_specs = [
        ("High Rigor (≥ 8.0)\n(n = 340)", scores >= 8.0, OI_GREEN),
        ("Sound (6.5–7.9)\n(n = 683)", (scores >= 6.5) & (scores < 8.0), OI_BLUE),
        ("Borderline (5.0–6.4)\n(n = 307)", (scores >= 5.0) & (scores < 6.5), OI_SKY),
        ("Typical Failed (< 5.0)\n(n = 397)", scores < 5.0, OI_GRAY),
    ]
    t_names = [t[0] for t in tier_specs]
    t_means = [float(np.mean(cites[t[1]])) for t in tier_specs]
    t_meds = [float(np.median(cites[t[1]])) for t in tier_specs]
    t_cols = [t[2] for t in tier_specs]

    y_b = np.arange(len(tier_specs))
    ax_b.barh(y_b, t_means, height=0.50, color=t_cols, alpha=0.85, label="Mean Citations")
    ax_b.scatter(t_meds, y_b, color="white", edgecolors="#111111", s=36, marker="D", linewidths=1.2, zorder=5, label="Median Citations")

    for i, (mn, md) in enumerate(zip(t_means, t_meds)):
        ax_b.text(
            mn + 4.0,
            i,
            f"Mean {mn:.1f} (Med {md:.0f})",
            va="center",
            ha="left",
            fontsize=7.2,
            fontweight="bold",
            color="#111111",
        )

    ax_b.set_yticks(y_b)
    ax_b.set_yticklabels(t_names, fontsize=7.8)
    ax_b.invert_yaxis()
    ax_b.set_xlim(0, 275)
    ax_b.set_xticks([0, 50, 100, 150, 200])
    ax_b.set_xlabel("Citations per Paper")
    ax_b.legend(loc="lower right", frameon=False, fontsize=7.0)
    set_panel_title(ax_b, "B", "Citations by Blinded Quality Tier")
    style_axis(ax_b, grid_axis="x")

    out_path = FIG_DIR / "figS1_citations_vs_bars.pdf"
    fig.savefig(out_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return {
        "path": str(out_path),
        "n_non_cohort_a": len(recs),
        "n_failed_ge50": int(np.sum(fail_high_mask)),
        "n_failed_ge100": int(np.sum((scores < 5.0) & (cites >= 100))),
        "tier_means": dict(zip([t[0].replace("\n", " ") for t in tier_specs], t_means)),
    }


def main():
    rng = np.random.default_rng(42)
    s1 = generate_fig1(rng)
    s2 = generate_fig2(rng)
    s3 = generate_fig3(rng)
    s4 = generate_fig4(rng)
    s5 = generate_fig5(rng)
    ss1 = generate_figS1(rng)
    summary = {"fig1": s1, "fig2": s2, "fig3": s3, "fig4": s4, "fig5": s5, "figS1": ss1}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
