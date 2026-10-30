# Review of AN_ANON_053

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents `MoleRate`, a maximum-likelihood phylogenetic method implemented in `[SOFTWARE_PACKAGE]` ($\ge 2.5.71$) to detect lineage-specific shifts in nucleotide or amino acid substitution rates on focal ("labeled") branches relative to a genome-wide reference tree $T_\theta$. `MoleRate` fits a hierarchy of nested branch-scaling models (`Proportional`, `Proportional Partitioned`, `Unconstrained Test`, `Unconstrained`, and single-branch `Proportional + 1`), performs Holm–Bonferroni-corrected likelihood ratio tests (LRTs), and introduces a branch-by-branch outlier filter to exclude genes whose rate shift is driven by a single aberrant lineage (e.g., local assembly or alignment errors). The authors benchmark `MoleRate` on 30,000 simulated alignments on a 40-species avian tree and apply it to 19,149 mammalian gene alignments across 62 species from UCSC for three convergent phenotypes (subterranean, marine, and hairless) plus a 6-species random control, cross-validating candidate genes with codon-based `RELAX` analyses, STRING v12.0 pathway enrichment, and precision–recall comparisons against `RERconverge`. Source code, simulated alignments, Python summary utilities, and interactive ObservableHQ notebooks are publicly available.

`MoleRate` is a fast (~12 seconds per alignment), practical screening tool whose single-branch outlier test directly addresses a pervasive failure mode in comparative genomics—where >50% of raw significant gene calls arise from single-species alignment or assembly artifacts (illustrated by `SEPT7` in the star-nosed mole). The inclusion of a 6-species random lineage control and follow-up `RELAX` tests showing that ~70% of accelerated genes reflect relaxed purifying selection rather than positive selection reflect strong biological and interpretive rigor. However, several statistical and editorial issues need resolution: (1) in empirical mammalian data, unmodeled background branch-rate overdispersion (heterotachy) causes the 1-d.f. `Proportional` vs. `Proportional Partitioned` LRT to reject the null at $q \le 0.01$ for 13.1% of the genome (2,520 / 19,164 genes) even on 6 random branches; (2) the second outlier LRT (`Proportional + 1` vs. `Unrestricted Test`) is described as having 1 degree of freedom despite differing by $L - 1$ parameters in Table 1; and (3) Table 3 (`KRT10`), Table 2, Figure 4, and the Supplementary Table captions contain multiple numerical and copy-paste errors.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Over 50% of statistically significant lineage-specific rate shifts in empirical genome-wide alignments are driven by single-branch outliers (often alignment/assembly errors), which `MoleRate`'s outlier filter effectively removes: [Well Supported].**  
  Across all four mammalian analyses in Table 4, single-branch outliers account for 1,121 to 1,954 of the FDR $\le 0.01$ calls. The `SEPT7` vs. `LIM2` comparison (Fig. S5) clearly demonstrates how a 3' sequence assembly/alignment error in a single subterranean species (`conCri1`) creates a spurious $R_L / R_\theta > 4$ signal that vanishes upon masking or outlier filtering.

* **Candidate accelerated and decelerated genes surviving multi-branch and outlier filtering recover biologically expected sensory and structural pathways, driven primarily by relaxed or intensified purifying selection: [Well Supported].**  
  Filtered candidate genes show strong (>10×) functional enrichments for eye/lens development and olfaction in subterranean mammals, olfactory receptors in marine mammals, and epidermal/cornified envelope pathways in hairless mammals—whereas the 6-species random control yields zero enriched functional categories despite 92 genes passing filters. Follow-up `RELAX` tests confirm that 80/113 subterranean, 82/120 marine, and 30/39 hairless accelerated genes experience relaxed selection ($K < 1, p \le 0.05$).

* **`MoleRate` achieves higher precision than `RERconverge` on eye-related benchmark gene sets when background species sampling is small (20 species): [Moderately Supported].**  
  On the pruned 20-species tree (Fig. 4), `MoleRate`—particularly with outlier filtering—achieves higher log-fold enrichment at matched recall on Lens Morphology and Expressed Ocular gene sets than `RERconverge`, while both methods perform similarly on the full 62-species tree (Fig. S6). Because only a single 20-species subsample was evaluated on one phenotype, testing across replicated random 20-species background subsamples would strengthen the generality of this comparison.

* **The primary `Proportional` vs. `Proportional Partitioned` LRT is well-calibrated under the null hypothesis: [Moderately Supported].**  
  While Type I error is $\le 0.05$ at $\alpha = 0.05$ in parametric simulations where every background branch evolves strictly as $g_i = R_\theta t_i$ (Fig. 3), empirical genes exhibit substantial residual branch-to-branch rate variation (heterotachy, incomplete lineage sorting, and generation-time effects) as shown by the `Proportional` vs. `Unconstrained` test. Because the 1-d.f. `Proportional` vs. `Proportional Partitioned` test assumes zero residual rate variance across branches, empirical overdispersion inflates the test statistic, causing 2,520 of 19,164 genes (13.1%) to pass $\text{FDR} \le 0.01$ when labeling 6 random species (Table 4). Thus, calibration in empirical data relies heavily on the post-hoc heuristic filters ($R_L / R_\theta \ge 2$ or $\le 0.5$, $\ge N/2$ informative branches, and 0 outliers).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Clarify the Formulation and Degrees of Freedom of the Second Outlier LRT (`All but this branch` Test)
* **WHY:** In the Outlier Detection section (lines 105–109), the text states: *"Two LR tests (each with a single degree of freedom) are then performed... Proportional + 1 (null) vs Unrestricted Test (alternative)."* However, in Table 1, `Proportional + 1` has 2 branch-scaling parameters ($R$ and $g_k$), whereas `Unconstrained Test` (`Unrestricted Test`) estimates $L + 1$ parameters ($R_\theta$ and $L$ independent foreground branch lengths), which yields $(L + 1) - 2 = L - 1$ degrees of freedom, not 1. Conversely, if the test actually has 1 d.f., the alternative model must be a 3-parameter `Proportional Partitioned + 1` model where $b_k$ has length $g_k$, the remaining $L - 1$ labeled branches share a common scalar $R_{L \setminus \{k\}}$, and background branches share $R_\theta$.
* **WHAT:** Specify the exact parameterization and degrees of freedom for the second outlier test in Table 1, Table 2, and lines 105–109.
* **HOW:** If the code fits `Proportional + 1` (2 params) vs. `Unconstrained Test` ($L+1$ params), update line 105 to state that the second test has $L - 1$ degrees of freedom; if the code fits a 3-parameter model scaling $B \setminus \{b_k\}$ proportionally, add `Proportional Partitioned + 1` to Table 1 and update line 109 accordingly.

#### 2. Discuss Empirical LRT Inflation Under Background Heterotachy and Provide an Empirical Null Calibration Option
* **WHY:** In Table 4, testing 6 random species yields 2,520 genes at $\text{FDR} \le 0.01$ (13.1% of tested genes), demonstrating that parametric $\chi^2_1$ $p$-values from `Proportional` vs. `Proportional Partitioned` are anti-conservative on real alignments due to pervasive branch-rate overdispersion around the reference tree $T_\theta$.
* **WHAT:** Explicitly point out in the Results and Discussion that raw `Proportional` vs. `Proportional Partitioned` $q$-values are inflated by background heterotachy in empirical data (as shown by the 2,520 random-lineage hits), which is why combining the LRT with the outlier filter, $\ge N/2$ informative-branch requirement, and effect-size threshold ($R_L / R_\theta \ge 2$ or $\le 0.5$) is essential for empirical specificity.
* **HOW:** Additionally, note that users analyzing small trees can divide the LRT statistic $2 \Delta \ln L$ by an empirical overdispersion factor $\hat{\phi} = \frac{2(\ln L_{\text{Unconstrained}} - \ln L_{\text{PP}})}{N - 2}$ (an $F$-test analog comparing between-group rate shift to within-group residual branch rate deviance) or calibrate empirical FDR against random branch permutations.

#### 3. Correct the Corrupt Log-Likelihoods and Caption in Table 3 (`KRT10`) and Fix All Table/Text Typos
* **WHY:** Table 3 contains log-likelihood values that mathematically contradict the reported `~0` $p$-values, along with several mislabeled captions and copy-paste errors across the manuscript.
* **WHAT & HOW:**
  1. **Table 3 log-likelihoods and caption (lines 146–155):**
     - The caption of Table 3 (line 148) reads *"MoleRate applied to the KRT10 gene with the three subterranean ."* Change *"three subterranean"* to *"hairless mammals (all-descendants labeling strategy)"*.
     - In Table 3, $\ln L$ is listed as `-10473.6` (`Proportional`), `-10471.9` (`Proportional Partitioned`), and `-10471.1` (`Unconstrained Test`). Those numbers yield $2 \Delta \ln L = 3.4$ ($p = 0.065$, not `~0`) for `Prop.` vs. `Prop. Partitioned` and $2 \Delta \ln L = 1.6$ on $L-1$ d.f. ($p > 0.9$, not `~0`) for `Prop. Partitioned` vs. `Unconstrained Test`, contradicting the `~0` $p$-values in the right-hand columns and the 6 outlier branches in Figure 2C. Extract the exact $\ln L$ values from the `KRT10` JSON file and update Table 3. Also reconcile *"~1.6x"* in line 146 with $R_L = 1.75, R_\theta = 0.69$ ($R_L / R_\theta = 2.54$) in Table 3.
  2. **Table 2 degrees of freedom (line 96):** For `Proportional` (1 parameter, $R$) vs. `Unconstrained*` ($N$ parameters), change `D.F.` from `N` to `N-1`.
  3. **RELAX parameter sign typo (line 247):** Change *"intensified selection (RELAX K<1)"* to *"intensified selection (RELAX K>1)"*.
  4. **Copy-paste errors in phenotype sections (lines 252 and 263):** In line 252 (Marine section), change *"same procedure as for the marine phenotype"* to *"subterranean phenotype"*. In line 263 (Hairless section), change *"for marine decelerated genes, 20/37 genes"* to *"for hairless decelerated genes, 20/37 genes"*.
  5. **Figure 4 caption contradiction (line 297):** The main text (lines 295, 299) states that Figure 4 shows the pruned tree with **20 background species** (while Figure S6 shows all background species), but the Figure 4 caption (line 297) says *"using all background species"*. Correct the Figure 4 caption to *"using 20 background species"*.
  6. **Supplementary Table captions S2–S6 (second part, lines 25–33):**
     - In Table S2 caption, change `(>=2 ratio)` to `(<=0.50 ratio)`.
     - In Table S4 and Table S6 captions, change *"Genes with accelerated rates"* to *"Genes with decelerated rates"*.
     - In Tables S3–S4 and S5–S6 captions, change *"comparing subterranean branches with the rest of the tree"* to *"comparing marine branches..."* and *"comparing hairless branches..."*, respectively.
