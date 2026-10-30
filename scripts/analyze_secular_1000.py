from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
#!/usr/bin/env python3
"""
Unblind and analyze the scaled N = 1,000 Secular Cohort (1991-2025, 7 five-year windows, 4 tracks)
and the Combined Wild Corpus (N = 1,161: 1,000 Secular + 101 Cohort C + 60 OOD).
"""
import json
import re
import math
from pathlib import Path
from collections import Counter
import numpy as np
from scipy import stats

base_dir = Path(str(REPO_ROOT))
sec_dir = base_dir / "secular_trend_exp"

manifest = json.loads((sec_dir / "manifest_1000.json").read_text())
pub_vol = json.loads((sec_dir / "pubmed_annual_volume.json").read_text())

stub_pats = re.compile(
    r"(archival stub|database stub|abstract\s*\+\s*references|abstract and references only|main text.{0,30}missing|body.{0,20}unextracted|full text is available as a pdf|only.{0,20}abstract.{0,20}references|entire main text.{0,20}missing|truncated database|archival truncation|refs-only stub)",
    re.I,
)

def parse_review(md_path: Path):
    txt = md_path.read_text(encoding="utf-8")
    m_comp = re.search(
        r"\*\*Composite Score:\*\*\s*([0-9.]+)\s*/\s*10(?:\.0)?\s*\(Rigor:\s*([0-9.]+)/3\.5\s*\|\s*Claims:\s*([0-9.]+)/2\.5\s*\|\s*Biology:\s*([0-9.]+)/2\.0\s*\|\s*Reproducibility:\s*([0-9.]+)/2\.0\)",
        txt,
    )
    if not m_comp:
        raise ValueError(f"Could not parse score in {md_path}")
    overall = float(m_comp.group(1))
    rigor = float(m_comp.group(2))
    claims = float(m_comp.group(3))
    biology = float(m_comp.group(4))
    repro = float(m_comp.group(5))
    sci_core = round(rigor + claims + biology, 2)

    def extract_field(label):
        m = re.search(rf"\*\*{label}:\*\*\s*(.+)", txt)
        return m.group(1).strip() if m else "Unknown"

    m_dec = re.search(r"(?:ESTIMATED_DECADE|Estimated Decade)[^0-9\n]*([12][09][0-9]0s)", txt, re.I)
    est_dec = m_dec.group(1) if m_dec else "Unknown"

    is_stub = bool(stub_pats.search(txt))

    return {
        "overall": overall,
        "rigor": rigor,
        "claims": claims,
        "biology": biology,
        "reproducibility": repro,
        "sci_core_8": sci_core,
        "sci_core_scaled_10": round(sci_core * 10.0 / 8.0, 2),
        "bias_category": extract_field("Bias Category"),
        "verdict": extract_field("Verdict"),
        "study_modality": extract_field("Study Modality"),
        "tech_maturity": extract_field("Technology Maturity"),
        "epistemic_stage": extract_field("Epistemic Stage"),
        "estimated_decade": est_dec,
        "is_stub": is_stub,
    }

PURE_MEGA = {
    "plos one", "scientific reports", "sci rep", "frontiers", "front ",
    "international journal of molecular sciences", "int j mol sci", "animals",
    "viruses", "genes", "cells", "cancers", "microorganisms", "plants",
    "peerj", "heliyon", "medicine (baltimore)", "bmc ", "nutrients",
    "biomolecules", "antibiotics", "pathogens", "vaccines", "molecules",
    "biomedicines", "curr issues mol biol", "life (basel)", "diversity",
    "ijms", "agronomy", "forests", "insects", "metabolites", "pharmaceutics",
    "toxins", "water", "atmosphere", "sustainability", "appl sci", "applied sciences",
    "biology (basel)", "diagnostics", "healthcare", "j clin med", "medicina",
    "ijierph", "int j environ res public health", "scientific world journal",
    "hindawi", "biomed res int", "evid based complement alternat med",
    "oncotarget", "aging (albany ny)", "cell death discov", "commun biol",
    "communications biology", "iscience", "aip adv", "royal society open science",
    "r soc open sci", "febs open bio", "g3 (bethesda)", "ecol evol",
    "ecology and evolution", "microbiologyopen", "open biol", "bmj open"
}

def is_megajournal(j_name: str) -> bool:
    jl = (j_name or "").lower()
    return any(k in jl for k in PURE_MEGA) or "(basel)" in jl

def normalize_modality(m: str) -> str:
    ml = (m or "").lower()
    if "hybrid" in ml:
        return "Hybrid Computational + Wet-Lab"
    if "wet-lab" in ml or "wet lab" in ml or "experimental" in ml:
        return "Wet-Lab Primary Experimental"
    if "theory" in ml or "simulation" in ml or "methods" in ml:
        return "Dry-Lab Theory/Methods/Simulation"
    if "secondary" in ml or "cohort" in ml or "database" in ml:
        return "Dry-Lab Secondary Cohort/Database"
    return "Dry-Lab Secondary Cohort/Database"

def normalize_tech(t: str) -> str:
    tl = (t or "").lower()
    if "commodity" in tl or "hype" in tl or "template" in tl:
        return "Commodity/Hype-Cycle Template"
    if "mid-stage" in tl or "high-throughput" in tl or "emerging" in tl:
        return "Mid-Stage High-Throughput"
    return "Mature/Classical"

def normalize_stage(s: str) -> str:
    sl = (s or "").lower()
    if "translational" in sl or "preclinical" in sl or "biomarker" in sl:
        return "Translational/Preclinical/Biomarker"
    if "clinical" in sl or "observational" in sl or "epidemiolog" in sl:
        return "Clinical/Observational"
    return "Basic/Mechanistic Discovery"

def normalize_bias(b: str) -> str:
    bl = (b or "").lower()
    if "none" in bl or "sound" in bl:
        return "None (Methodologically Sound)"
    if "statistical" in bl or "design" in bl:
        return "Statistical/Design"
    if "technical" in bl or "assay" in bl:
        return "Technical/Assay"
    if "algorithmic" in bl or "model" in bl:
        return "Algorithmic/Model"
    if "over-interpretation" in bl or "clinical" in bl:
        return "Over-Interpretation/Clinical"
    return "Statistical/Design"

sec_papers = []
for p in manifest["papers"]:
    anon_id = p["anon_id"]
    rev_path = sec_dir / "reviews" / f"{anon_id}.md"
    rev = parse_review(rev_path)
    rev["study_modality"] = normalize_modality(rev["study_modality"])
    rev["tech_maturity"] = normalize_tech(rev["tech_maturity"])
    rev["epistemic_stage"] = normalize_stage(rev["epistemic_stage"])
    rev["bias_category"] = normalize_bias(rev["bias_category"])
    p_full = {**p, **rev}
    yr_str = str(p["year"])
    v_info = pub_vol.get(yr_str, {"total_indexed": 1000000, "open_access": 100000, "core_domain_volume": 200000})
    p_full["pubmed_total_vol"] = v_info["total_indexed"]
    p_full["pubmed_oa_vol"] = v_info["open_access"]
    p_full["pubmed_core_vol"] = v_info["core_domain_volume"]
    p_full["log10_core_vol"] = round(math.log10(max(v_info["core_domain_volume"], 1)), 4)
    p_full["log10_oa_vol"] = round(math.log10(max(v_info["open_access"], 1)), 4)
    p_full["is_megajournal"] = is_megajournal(p["journal"])
    yr = p["year"]
    if yr < 2000:
        p_full["decade"] = "1990s (1991–1999)"
        p_full["true_decade_short"] = "1990s"
    elif yr < 2010:
        p_full["decade"] = "2000s (2000–2009)"
        p_full["true_decade_short"] = "2000s"
    elif yr < 2020:
        p_full["decade"] = "2010s (2010–2019)"
        p_full["true_decade_short"] = "2010s"
    else:
        p_full["decade"] = "2020s (2020–2025)"
        p_full["true_decade_short"] = "2020s"
    p_full["dataset"] = f"Secular Wild ({p_full['window_label']})"
    sec_papers.append(p_full)

with open(sec_dir / "secular_results_1000.json", "w") as f:
    json.dump(sec_papers, f, indent=2)

# Build pooled wild 1,161 (1,000 secular + 101 Cohort C + 60 OOD)
old_pooled = json.loads((sec_dir / "pooled_wild_230.json").read_text())
non_secular_wild = []
for x in old_pooled:
    if not str(x.get("dataset", "")).startswith("Secular"):
        x_copy = dict(x)
        x_copy["study_modality"] = normalize_modality(x_copy.get("study_modality"))
        x_copy["tech_maturity"] = normalize_tech(x_copy.get("tech_maturity"))
        x_copy["epistemic_stage"] = normalize_stage(x_copy.get("epistemic_stage"))
        x_copy["is_megajournal"] = is_megajournal(x_copy.get("journal", ""))
        non_secular_wild.append(x_copy)

print(f"Non-secular wild papers (Cohort C + OOD): {len(non_secular_wild)}")
pooled_wild_1161 = non_secular_wild + sec_papers
print(f"Total Pooled Wild Corpus: {len(pooled_wild_1161)}")
with open(sec_dir / "pooled_wild_1161.json", "w") as f:
    json.dump(pooled_wild_1161, f, indent=2)

print("\n=== 1. SECULAR TREND BY 5-YEAR WINDOW (N = 1,000) ===")
windows = [
    ("W1_1991_1995", "1991–1995"),
    ("W2_1996_2000", "1996–2000"),
    ("W3_2001_2005", "2001–2005"),
    ("W4_2006_2010", "2006–2010"),
    ("W5_2011_2015", "2011–2015"),
    ("W6_2016_2020", "2016–2020"),
    ("W7_2021_2025", "2021–2025"),
]
for w_code, w_label in windows:
    sub = [x for x in sec_papers if x["window_code"] == w_code]
    sc = [x["overall"] for x in sub]
    core8 = [x["sci_core_8"] for x in sub]
    rig = [x["rigor"] for x in sub]
    clm = [x["claims"] for x in sub]
    bio = [x["biology"] for x in sub]
    rep = [x["reproducibility"] for x in sub]
    auths = [x["author_count"] for x in sub]
    mega = sum(1 for x in sub if x["is_megajournal"]) * 100.0 / len(sub)
    f5 = sum(1 for s in sc if s < 5.0) * 100.0 / len(sc)
    f6 = sum(1 for s in sc if s < 6.0) * 100.0 / len(sc)
    print(
        f"{w_label:10s} (n={len(sub):3d}): Composite={np.mean(sc):.2f}±{np.std(sc,ddof=1):.2f} (Med={np.median(sc):.2f}) | "
        f"SciCore(/8)={np.mean(core8):.2f} (Scaled10={np.mean(core8)*10/8:.2f}) | "
        f"R={np.mean(rig):.2f} C={np.mean(clm):.2f} B={np.mean(bio):.2f} Rep={np.mean(rep):.2f} | "
        f"<5.0={f5:4.1f}% <6.0={f6:4.1f}% | Authors={np.mean(auths):.1f} | Mega={mega:4.1f}%"
    )

print("\n=== 2. SECULAR TREND BY DECADE (N = 1,000) ===")
for dec in ["1990s (1991–1999)", "2000s (2000–2009)", "2010s (2010–2019)", "2020s (2020–2025)"]:
    sub = [x for x in sec_papers if x["decade"] == dec]
    sc = [x["overall"] for x in sub]
    core8 = [x["sci_core_8"] for x in sub]
    rep = [x["reproducibility"] for x in sub]
    auths = [x["author_count"] for x in sub]
    mega = sum(1 for x in sub if x["is_megajournal"]) * 100.0 / len(sub)
    f5 = sum(1 for s in sc if s < 5.0) * 100.0 / len(sc)
    f6 = sum(1 for s in sc if s < 6.0) * 100.0 / len(sc)
    print(
        f"{dec:18s} (n={len(sub):3d}): Composite={np.mean(sc):.2f}±{np.std(sc,ddof=1):.2f} (Med={np.median(sc):.2f}) | "
        f"SciCore(/8)={np.mean(core8):.2f} (Scaled10={np.mean(core8)*10/8:.2f}) | Rep={np.mean(rep):.2f} | "
        f"<5.0={f5:4.1f}% <6.0={f6:4.1f}% | Authors={np.mean(auths):.1f} | Megajournal={mega:4.1f}%"
    )

print("\n=== 4. STEPHANIE'S STRUCTURAL PARTITIONS IN N = 1,000 SECULAR & N = 1,161 WILD ===")
for ds_name, ds in [("N = 1,000 SECULAR COHORT", sec_papers), ("N = 1,161 POOLED WILD CORPUS", pooled_wild_1161)]:
    print(f"\n******************** {ds_name} ********************")
    mega_p = [x["overall"] for x in ds if x.get("is_megajournal")]
    leg_p = [x["overall"] for x in ds if not x.get("is_megajournal")]
    mega_c8 = [x["sci_core_8"] for x in ds if x.get("is_megajournal")]
    leg_c8 = [x["sci_core_8"] for x in ds if not x.get("is_megajournal")]
    print(f"  Legacy/Society/Selective (n={len(leg_p):3d}): Comp={np.mean(leg_p):.2f}±{np.std(leg_p,ddof=1):.2f} (Med={np.median(leg_p):.2f}) | Core8={np.mean(leg_c8):.2f} (Scaled10={np.mean(leg_c8)*10/8:.2f}) | <5.0={np.mean([s<5.0 for s in leg_p])*100:.1f}% | <6.0={np.mean([s<6.0 for s in leg_p])*100:.1f}%")
    print(f"  Commercial Megajournals  (n={len(mega_p):3d}): Comp={np.mean(mega_p):.2f}±{np.std(mega_p,ddof=1):.2f} (Med={np.median(mega_p):.2f}) | Core8={np.mean(mega_c8):.2f} (Scaled10={np.mean(mega_c8)*10/8:.2f}) | <5.0={np.mean([s<5.0 for s in mega_p])*100:.1f}% | <6.0={np.mean([s<6.0 for s in mega_p])*100:.1f}%")
    print(f"  Megajournal vs Legacy gap: {np.mean(mega_p)-np.mean(leg_p):+.2f} pts, Welch p={stats.ttest_ind(leg_p, mega_p, equal_var=False).pvalue:.3e}")

    for field_key, title in [
        ("study_modality", "Study Modality"),
        ("tech_maturity", "Technology Maturity"),
        ("epistemic_stage", "Epistemic Stage"),
    ]:
        print(f"\n--- {title} ({ds_name}) ---")
        groups = {}
        for x in ds:
            val = x.get(field_key, "Unknown")
            groups.setdefault(val, []).append(x)
        all_groups_sc = [ [z["overall"] for z in sub] for sub in groups.values() if len(sub) >= 2 ]
        kw_stat, kw_p = stats.kruskal(*all_groups_sc)
        f_stat, f_p = stats.f_oneway(*all_groups_sc)
        print(f"  Omnibus ANOVA F={f_stat:.2f} (p={f_p:.3e}) | Kruskal-Wallis H={kw_stat:.2f} (p={kw_p:.3e})")
        for k, sub in sorted(groups.items(), key=lambda kv: -np.mean([z["overall"] for z in kv[1]])):
            sc = [z["overall"] for z in sub]
            c8 = [z["sci_core_8"] for z in sub]
            f5 = sum(1 for s in sc if s < 5.0) * 100.0 / len(sc)
            f6 = sum(1 for s in sc if s < 6.0) * 100.0 / len(sc)
            yr_m = np.mean([z["year"] for z in sub])
            print(
                f"  {k:40s} (n={len(sub):3d}, meanYr={yr_m:.1f}): "
                f"Comp={np.mean(sc):.2f}±{np.std(sc,ddof=1) if len(sc)>1 else 0:.2f} (Med={np.median(sc):.2f}) | "
                f"SciCore(/8)={np.mean(c8):.2f} (Scaled10={np.mean(c8)*10/8:.2f}) | <5.0={f5:4.1f}% | <6.0={f6:4.1f}%"
            )

print("\n=== 5. COMPOSITIONAL SHIFT VS WITHIN-TIER / WITHIN-JOURNAL DRIFT (N = 1,000) ===")
# Oaxaca-Blinder decomposition between Pre-2010 (1991-2010, W1-W4) and Post-2015 (2016-2025, W6-W7)
# and between 1990s (1991-1999) and 2020s (2020-2025)
def oaxaca_blinder(early_list, late_list, label):
    def make_X(lst):
        rows = []
        for x in lst:
            rows.append([
                1.0,
                1.0 if x["is_megajournal"] else 0.0,
                1.0 if x["tech_maturity"] == "Commodity/Hype-Cycle Template" else 0.0,
                1.0 if x["study_modality"] == "Dry-Lab Secondary Cohort/Database" else 0.0,
                1.0 if x["epistemic_stage"] in ("Clinical/Observational", "Translational/Preclinical/Biomarker") else 0.0,
            ])
        return np.array(rows)
    X_e = make_X(early_list)
    y_e = np.array([x["overall"] for x in early_list])
    X_l = make_X(late_list)
    y_l = np.array([x["overall"] for x in late_list])
    X_pool = np.vstack([X_e, X_l])
    y_pool = np.concatenate([y_e, y_l])
    # Pooled OLS with group indicator (Neumark / Jann pooled reference coefficients)
    g_ind = np.concatenate([np.zeros(len(y_e)), np.ones(len(y_l))])[:, None]
    X_aug = np.hstack([X_pool, g_ind])
    beta_aug, _, _, _ = np.linalg.lstsq(X_aug, y_pool, rcond=None)
    beta_star = beta_aug[:-1]
    mean_diff = np.mean(y_e) - np.mean(y_l)
    dX = np.mean(X_e, axis=0) - np.mean(X_l, axis=0)
    explained_comp = float(np.dot(dX, beta_star))
    unexplained_drift = mean_diff - explained_comp
    print(f"  Oaxaca-Blinder ({label}): Total Drop = {mean_diff:.3f} pts ({np.mean(y_e):.2f} -> {np.mean(y_l):.2f})")
    print(f"    Explained by Compositional Shift (Megajournal + Commodity Template + Secondary DB + Clinical/Transl): {explained_comp:.3f} pts ({explained_comp/mean_diff*100:.1f}%)")
    print(f"    Unexplained / Within-Stratum Drift: {unexplained_drift:.3f} pts ({unexplained_drift/mean_diff*100:.1f}%)")

oaxaca_blinder(
    [x for x in sec_papers if x["decade"] == "1990s (1991–1999)"],
    [x for x in sec_papers if x["decade"] == "2020s (2020–2025)"],
    "1990s vs 2020s"
)
oaxaca_blinder(
    [x for x in sec_papers if x["window_code"] == "W2_1996_2000"],
    [x for x in sec_papers if x["window_code"] == "W7_2021_2025"],
    "1996-2000 Peak vs 2021-2025"
)

# Within-journal fixed-effects regression for journals spanning >= 10 years and >= 5 papers
j_counts = Counter(x["journal"].lower() for x in sec_papers)
multi_j = [x for x in sec_papers if j_counts[x["journal"].lower()] >= 5]
# Demean year and score within each journal
j_groups = {}
for x in multi_j:
    j_groups.setdefault(x["journal"].lower(), []).append(x)
multi_span_j = {k: v for k, v in j_groups.items() if max(z["year"] for z in v) - min(z["year"] for z in v) >= 8}
dy_list, dsc_list, dc8_list = [], [], []
for k, v in multi_span_j.items():
    ym = np.mean([z["year"] for z in v])
    sm = np.mean([z["overall"] for z in v])
    cm = np.mean([z["sci_core_8"] for z in v])
    for z in v:
        dy_list.append(z["year"] - ym)
        dsc_list.append(z["overall"] - sm)
        dc8_list.append(z["sci_core_8"] - cm)
dy_arr = np.array(dy_list)
dsc_arr = np.array(dsc_list)
dc8_arr = np.array(dc8_list)
sl_fe, _, r_fe, p_fe, _ = stats.linregress(dy_arr, dsc_arr)
sl_fe8, _, r_fe8, p_fe8, _ = stats.linregress(dy_arr, dc8_arr)
print(f"\n  Within-Journal Fixed Effects ({len(multi_span_j)} multi-year journals, n={len(dy_arr)} papers):")
print(f"    Composite slope = {sl_fe:+.4f} pts/yr ({sl_fe*10:+.2f} pts/decade), r={r_fe:+.3f}, p={p_fe:.3e}")
print(f"    SciCore8  slope = {sl_fe8:+.4f} pts/yr ({sl_fe8*10:+.2f} pts/decade), r={r_fe8:+.3f}, p={p_fe8:.3e}")
