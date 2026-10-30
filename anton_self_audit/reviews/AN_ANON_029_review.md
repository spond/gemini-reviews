# Review of AN_ANON_029

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.5 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.8 / 8.0**  
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.6/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates the relationship between early childhood weight-gain trajectories (from birth to two years of age) and the oral and gut microbiota sampled at age two in 236 mother-child dyads from the INSIGHT cohort (retaining 214 child oral, 189 child stool, and 215 maternal oral 16S rRNA V3–V4 samples after quality control). Using Functional Data Analysis (PACE curve reconstruction, temporal curve registration, function-on-scalar regression, and Functional Linear Adaptive Mixed Estimation [FLAME]) alongside traditional conditional weight gain (CWG, 0–6 months) Mann-Whitney comparisons and LEfSe, the authors report that children's oral microbiota at age two—specifically lower phylum-level $\alpha$-diversity ($p = 0.041$) and higher Firmicutes-to-Bacteroidetes (F:B) ratio ($p = 0.0015$)—is associated with higher weight-for-length trajectories and rapid infant weight gain, whereas the age-two gut microbiota shows no marginal association with growth curves until diet covariates are included in a joint regression (where gut $\alpha$-diversity becomes positively associated with growth, $p = 0.020$). Raw sequencing reads (SRA `PRJNA420339`), phenotype data (dbGaP `phs001498.v1.p1`), and analysis workflows/R scripts are publicly archived.

While integrating longitudinal functional data analysis with pediatric microbiome profiling is a creative methodological contribution, the core conclusions are undermined by four primary methodological and statistical flaws: (1) computing ecological $\alpha$-diversity (Inverse Simpson) and $\beta$-diversity on **phylum-level** counts rather than OTU/ASV or genus-level counts, which collapses richness/evenness to a near-collinear proxy of the dominant phyla; (2) modeling longitudinal growth from birth to age two as the *response* ($Y(t), t \in [0, 2]$) regressed on a cross-sectional microbiota measurement taken at the *end* of the window ($t = 2$ years), and performing post-selection inference (`bestglm` followed by unadjusted OLS $t$-tests) without multiple-testing correction across the primary hypotheses; (3) applying Pearson's chi-squared `prop.test` to group-averaged relative abundances multiplied by sample size $N$, which violates binomial independence and ignores inter-individual variance and dyad pairing; and (4) concatenating unmerged 2×300 bp V3–V4 read pairs with `"NNNNN"` spacers prior to k-mer taxonomic classification. These issues can be resolved through computational re-analysis of the existing 16S reads at genus/ASV resolution without generating new sequencing data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Children's oral microbiota $\alpha$-diversity ($p = 0.041$ FDA; $p = 0.049$ CWG) and F:B ratio ($p = 0.0015$ FDA; $p = 0.019$ CWG) at age two are associated with rapid weight gain from birth to age two: [Fragile].**  
  First, $\alpha$-diversity was computed by applying the Inverse Simpson formula to rarefied *phylum-level* abundance counts (Results, line 23; Methods, line 140), where Firmicutes and Bacteroidetes dominate total reads, making phylum-level Inverse Simpson mathematically coupled to the F:B ratio rather than a valid measure of species or genus diversity. Second, the $p$-values for oral $\alpha$-diversity ($p = 0.041$ two-sided Choi test; $p = 0.049$ one-tailed Mann-Whitney U test) and maternal oral $\alpha$-diversity ($p = 0.018$ FDA; $p = 0.036$ CWG) are not corrected for multiple testing across the six primary function-on-scalar regressions and six CWG tests; under Benjamini-Hochberg FDR or Bonferroni adjustment, only the child oral F:B ratio ($p = 0.0015$) remains significant in the FDA model. Third, regressing historical growth ($0\text{–}24$ months) on age-two microbiota reverses temporal ordering.

* **Phylum proportions differ significantly between child gut, child oral, and maternal oral microbiota ($p = 1.1 \times 10^{-14}$ to $2.9 \times 10^{-3}$ via Pearson's chi-squared test): [Methodologically Flawed].**  
  In Methods (line 140), the authors state that for `prop.test` they took "the average of all individual proportions ... multiplied by the number of subjects to obtain the 'probability of successes'". Feeding $N \times \bar{p}$ into a two-sample binomial chi-squared test treats each subject as a single Bernoulli trial while ignoring within-subject read counts, between-subject biological variance (overdispersion), compositional closure, and the paired dependency between a child's oral and gut samples and their mother's oral sample.

* **Diet at age two explains 20.79% of variance in gut F:B ratio ($p = 9.45 \times 10^{-9}$) and 5.94% in gut $\alpha$-diversity ($p = 3.76 \times 10^{-3}$), and controlling for diet reveals a positive association between gut $\alpha$-diversity and child growth curves ($p = 0.020$): [Fragile].**  
  The regression models in Table 2 were fit after running exhaustive subset selection (`bestglm`) across 17 candidate covariates and then evaluating standard OLS $t$-statistics and $p$-values on the selected variables in the same dataset (Methods, chunk 2, line 15). This post-selection inference procedure inflates Type I error and $R^2$ estimates. Furthermore, because both diet and gut microbiota were measured cross-sectionally at age two while growth curves span $0\text{–}24$ months, conditioning a past trajectory ($Y(t), t \in [0,2]$) on two post-trajectory variables ($M_{t=2}$ and $D_{t=2}$, where $D_{t=2} \to M_{t=2}$) can induce collider bias if early growth or parental feeding behavior influences age-two diet.

* **FLAME and LEfSe identify specific phylogenetically aggregated genus groups associated with growth trajectories and rapid infant weight gain: [Moderately Supported].**  
  Using adaptive LASSO penalization in function-on-scalar regression (FLAME) with cross-validated tuning parameters is mathematically sound for high-dimensional taxon selection, and the phylogenetic tree-based aggregation of sparse genera reduces zero-inflation. However, in the two-stage aggregation procedure (Methods, chunk 2, line 19), stage 1 *sums* counts of sparse sibling nodes ($<5$ counts in $>90\%$ of samples) whereas stage 2 *averages* counts of correlated sibling nodes ($r > 0.7$). Mixing summation and averaging across internal tree merges distorts the relative abundance scale of merged groups depending on whether they were merged at stage 1 or stage 2.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Recompute $\alpha$- and $\beta$-Diversity at Genus or ASV/OTU Resolution and Replace `prop.test` with Paired Compositional Models
* **WHY:** Computing Inverse Simpson diversity and Bray-Curtis NMDS on phylum-level counts discards >95% of taxonomic information and makes $\alpha$-diversity redundant with phylum ratios, while `prop.test` on $N \times \bar{p}$ is statistically invalid for microbiome relative abundances.
* **WHAT:** Recompute Shannon, Inverse Simpson, and Bray-Curtis distances at the genus level (or ASV level via DADA2/VSearch) and test between-site differences using paired Dirichlet-multinomial, Wilcoxon signed-rank, or ALDEx2/ANCOM-BC models.
* **HOW:** Using the existing Kraken genus-level abundance tables (prior to phylum collapsing), run `vegan::diversity(..., index = "invsimpson")` and `vegan::metaMDS` on the rarefied genus table. Re-run the six function-on-scalar regressions (`Growth ~ genus_alpha_diversity`) and CWG Mann-Whitney tests, and apply Benjamini-Hochberg FDR correction across all six tests in Supplementary Table S1. Replace the 24 `prop.test` comparisons with paired Wilcoxon signed-rank tests (for child oral vs. child gut and child oral vs. maternal oral) with Holm-Bonferroni correction.

#### 2. Account for Post-Selection Inference and Reverse Temporal Conditioning in Growth Curve Models
* **WHY:** Evaluating standard OLS $p$-values on predictors chosen by `bestglm` on the same sample overstates significance (Table 2), and using age-2 microbiota as a predictor of $0\text{–}24$ month growth reverses temporal ordering.
* **WHAT:** Validate the covariate selection via bootstrap stability or sample splitting, and invert the functional regression to a scalar-on-function model (`Microbiota_age2 ~ Growth_Curve(0..24m) + Diet_age2`).
* **HOW:** Since the microbiota is measured at $t = 24$ months and growth is measured longitudinally over $t \in [0, 24]$ months, fit a scalar-on-function regression (e.g., `refund::pfr` in R) with age-2 oral/gut diversity or F:B ratio as the scalar response and the aligned growth curve $X_i(t)$ as the functional predictor, controlling for covariates. For Table 2, perform 1,000 nonparametric bootstrap resamples of the entire `bestglm` selection step to report inclusion frequencies and bootstrap-corrected confidence intervals and $p$-values.

#### 3. Remove Artificially Concatenated (`"NNNNN"`) Non-Overlapping V3–V4 Read Pairs and Standardize Taxonomic Tree Aggregation
* **WHY:** The 16S V3–V4 amplicon (~460 bp) sequenced with 2×300 bp MiSeq reads has an expected overlap of ~140 bp; read pairs that fail `fastq-join` (minimum 6 bp overlap) represent low-quality 3' tails, primer dimers, or off-target products. Concatenating them with `"NNNNN"` creates chimeric pseudo-amplicons and inflates k-mer false positives in Kraken. Additionally, summing counts in stage 1 of the phylogenetic merger while averaging counts in stage 2 alters total sample library sizes.
* **WHAT:** Filter out unmergeable read pairs instead of concatenating them with `"NNNNN"`, and use summation consistently in both stages of the phylogenetic tree aggregation.
* **HOW:** Re-run the Kraken classification pipeline using only the successfully merged `fastq-join` contigs, and update the two-stage tree aggregation script in the GitHub repository so that stage-2 correlated node merges sum (rather than average) read counts, preserving compositional additivity up the taxonomic tree before running FLAME and LEfSe.

#### 4. Propagate Curve Registration Uncertainty in FDA Regressions
* **WHY:** Aligning individual growth curves with `register.fd` removes phase variation by warping the time axis prior to function-on-scalar regression, but treating the registered curves as fixed data ignores phase-warping variance and narrows point-wise confidence bands.
* **WHAT:** Report sensitivity analyses comparing functional regression results on unregistered PACE curves (Supplementary Fig. S3B) versus registered curves (Fig. 1b), and test whether phase-warping functions themselves associate with microbiota measures.
* **HOW:** Run the L2, PCA, and Choi tests directly on the unregistered PACE curves and include the results alongside registered curve p-values in Supplementary Table S1.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Table 1 contains systematic percentage calculation errors that misrepresent the demographic distribution of the cohort.
* **WHAT & HOW:**
  * **Table 1 (lines 38–44, "Annual household income N (%)"):** The reported percentages (`3 of 99 (1.4)`, `5 of 99 (2.3)`, `12 of 99 (5.5)`, `29 of 99 (13.4)`, `26 of 99 (12)`, `24 of 99 (11)` in column 1, and `4 of 118 (1.8)`, ..., `39 of 118 (18.0)` in column 2) were mistakenly calculated by dividing each cell count by the *combined cohort total* ($99 + 118 = 217$) instead of the column denominators ($99$ and $118$), causing the column percentages to sum to 45.6% and 54.4% instead of 100%. Recompute all percentages using the column denominators (e.g., `29 of 99 (29.3%)` and `39 of 118 (33.1%)`).
  * **Results (line 68):** Correct the terminology `"Mann-Whitney one-tailed t-test"` to `"one-tailed Mann-Whitney U test"`.
