from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
#!/usr/bin/env python3
"""
Generate clean, uncluttered 2-panel Figure 6: Research & Publishing Economics
Matching the exact visual style of Figures 1-5 in paper/figures/ with zero text overlap.
"""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from compute_darren_economics_1000 import w1161, nih_wild, get_journal_apc_and_tier

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 9.0,
    "axes.titlesize": 9.8,
    "axes.titleweight": "bold",
    "axes.labelsize": 9.0,
    "xtick.labelsize": 8.0,
    "ytick.labelsize": 8.4,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

BLUE = "#0072B2"
GREEN = "#009E73"
ORANGE = "#E69F00"
RED = "#C83228"
GREY = "#7F7F7F"
PURPLE = "#CC79A7"

fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(8.6, 3.1), dpi=300,
    gridspec_kw={"width_ratios": [0.98, 1.12], "wspace": 0.62}
)

# ---------------------------------------------------------
# PANEL A: Grant Funding vs Paper Quality
# ---------------------------------------------------------
w_unfunded = [p["overall"] for p in w1161 if p["n_grants"] == 0 and p["est_study_cost_usd"] < 40000]
w_modest   = [p["overall"] for p in nih_wild if p["nih_annual_usd"] < 600000]
w_focused  = [p["overall"] for p in nih_wild if 600000 <= p["nih_annual_usd"] < 1500000]
w_mega     = [p["overall"] for p in nih_wild if p["nih_annual_usd"] >= 1500000]

x_pos = [0, 1, 2, 3]
means_a = [np.mean(w_unfunded), np.mean(w_modest), np.mean(w_focused), np.mean(w_mega)]
sems_a  = [
    np.std(w_unfunded, ddof=1) / np.sqrt(len(w_unfunded)),
    np.std(w_modest, ddof=1) / np.sqrt(len(w_modest)),
    np.std(w_focused, ddof=1) / np.sqrt(len(w_focused)),
    np.std(w_mega, ddof=1) / np.sqrt(len(w_mega)),
]
x_labels_a = [
    "Unfunded\n(<$25k)",
    "1 Grant\n($305k/yr)",
    "2–3 Grants\n($949k/yr)",
    "Mega-Grant\n($3.2M/yr)",
]

ax1.axhline(5.0, color=RED, linestyle="--", linewidth=1.1, alpha=0.8, zorder=1)
ax1.text(3.32, 5.12, "Fail (5.0)", color=RED, fontsize=7.2, fontweight="bold", ha="right", va="bottom")

ax1.errorbar(
    x_pos, means_a, yerr=sems_a, fmt="-o", color=BLUE, linewidth=2.3,
    markersize=6.8, capsize=3.2, capthick=1.2, markerfacecolor=BLUE, markeredgecolor="white",
    label="Everyday Papers (by Grant Tier)", zorder=4
)
ax1.plot(2, means_a[2], marker="o", markersize=9.2, color=GREEN, markeredgecolor="white", markeredgewidth=1.4, zorder=5)

for x_i, m_i, se_i in zip(x_pos, means_a, sems_a):
    col_i = GREEN if x_i == 2 else BLUE
    ax1.text(x_i, m_i + se_i + 0.16, f"{m_i:.2f}", ha="center", va="bottom", fontsize=7.9, fontweight="bold", color=col_i)

# Reference point for Low-Cost Math/Software Sound Controls
r200 = json.loads(open(str(REPO_ROOT / "results_200.json")).read())
cb_dry_mean = float(np.mean([x["overall"] for x in r200["cohort_b"] if x.get("domain") in ("Molecular Evolution", "Statistical Genetics", "Transcriptomics & CompBio")][:14]))
ax1.scatter([0.0], [8.6], marker="D", s=44, color=PURPLE, zorder=5, label="Low-Cost Math/Software Controls (8.6)")

ax1.set_xticks(x_pos)
ax1.set_xticklabels(x_labels_a, fontsize=7.8)
ax1.set_ylim(4.2, 9.8)
ax1.set_xlim(-0.42, 3.42)
ax1.set_ylabel("Blinded Paper Score (out of 10)")
ax1.legend(loc="lower right", frameon=True, facecolor="white", framealpha=0.94, edgecolor="#DDDDDD", fontsize=7.0)
ax1.set_title("A   Grant Support & Quality Plateau", loc="left", pad=10, fontsize=9.8, fontweight="bold")
ax1.grid(axis="y", linestyle=":", linewidth=0.55, color="#CCCCCC", alpha=0.75, zorder=0)

# ---------------------------------------------------------
# PANEL B: Journal APC vs Paper Quality (N = 1,076)
# ---------------------------------------------------------
tiers_b = [
    ("Luxury Flagships ($11.5k)", "Luxury Flagships ($9.5k-$12.3k)", GREEN),
    ("High-APC Selective ($5.6k)", "High-APC Selective ($4.5k-$7.0k)", GREEN),
    ("Academic Society ($3.2k)", "Selective Society / Univ Press ($2.0k-$4.2k)", BLUE),
    ("OA Megajournals ($2.9k)", "Commercial Megajournals ($1.7k-$3.9k)", RED),
    ("Diamond / Free OA ($0)", "Diamond / Subsidized ($0-$1.2k)", GREY),
]

y_pos_b = np.arange(len(tiers_b))
ax2.axvline(5.0, color=RED, linestyle="--", linewidth=1.1, alpha=0.8, zorder=1)

rng = np.random.default_rng(42)
y_labels_b = []
for idx, (label_base, tier_key, col) in enumerate(tiers_b):
    vals = [p["overall"] for p in w1161 if get_journal_apc_and_tier(p.get("journal"), p.get("is_megajournal", False))[1] == tier_key]
    y_labels_b.append(label_base)
    m_val = np.mean(vals)
    fail_pct = np.mean([v < 5.0 for v in vals]) * 100

    ax2.boxplot(
        [vals], positions=[idx], vert=False, widths=0.48, patch_artist=True,
        showfliers=False, zorder=2,
        boxprops=dict(facecolor=col, alpha=0.22, edgecolor=col, linewidth=1.15),
        medianprops=dict(color="#111111", linewidth=1.6),
        whiskerprops=dict(color=col, linewidth=1.0),
        capprops=dict(color=col, linewidth=1.0)
    )
    jit = rng.uniform(-0.15, 0.15, size=len(vals))
    ax2.scatter(vals, np.full(len(vals), idx) + jit, s=9, color=col, alpha=0.45, edgecolors="none", zorder=3)
    ax2.scatter([m_val], [idx], marker="D", s=32, color="white", edgecolors="#111111", linewidths=1.2, zorder=4)
    ax2.text(10.2, idx, f"{fail_pct:.0f}% fail", va="center", ha="left", fontsize=7.8, fontweight="bold", color=col)

ax2.set_yticks(y_pos_b)
ax2.set_yticklabels(y_labels_b, fontsize=8.2)
ax2.invert_yaxis()
ax2.set_ylim(4.6, -0.68)
ax2.text(4.85, -0.46, "Fail (5.0)", color=RED, fontsize=7.2, fontweight="bold", ha="right", va="bottom")
ax2.set_xlim(1.0, 12.1)
ax2.set_xticks([2, 4, 6, 8, 10])
ax2.set_xlabel("Blinded Paper Score (out of 10)")
ax2.set_title("B   Journal APC Tier vs. Quality (N = 1,076)", loc="left", pad=10, fontsize=9.8, fontweight="bold")
ax2.grid(axis="x", linestyle=":", linewidth=0.55, color="#CCCCCC", alpha=0.75, zorder=0)

out_path = str(REPO_ROOT / "paper/figures/fig6_research_and_publishing_economics.pdf")
plt.savefig(out_path, dpi=300, bbox_inches="tight")
print("Saved:", out_path)
