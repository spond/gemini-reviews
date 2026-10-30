# Review of AN_ANON_003

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.2 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.4/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study evaluates the utility of the nonsynonymous-to-synonymous substitution rate ratio ($K_A/K_S$) likelihood ratio test (LRT) for identifying protein-coding exons from human–mouse comparative genomic alignments. Using a curated LocusLink dataset of 153 orthologous human–mouse gene pairs comprising 1,244 coding exons (including 25 single-exon genes), the authors align orthologous protein sequences with CLUSTALW 1.81, back-translate to codon alignments, slice the alignments into individual exons using known human exon coordinates, and apply the maximum-likelihood F3$\times$4 codon model in PAML (`codeml`) to test whether $K_A/K_S < 1$ at $\alpha = 0.05$ ($\chi^2_1$ test). They report that 90.5% (1,126/1,244) of exons—and 100% (87/87) of exons $\ge 300\text{ bp}$—satisfy $K_A/K_S < 1$ ($P < 0.05$), yielding a nominal false-negative rate of 9.5%. To estimate the false-positive rate in noncoding sequences, they simulate 24,000 pairs of random sense-codon sequences across six lengths (51–1,002 bp) and four divergence levels (5%–20%), reporting an average false-positive rate of 2.6%. Links to the curated exon dataset and analysis archive (`ka_ks_data.html` and `ka_ks_analysis.tar.gz`) are provided.

While the empirical characterization of selective constraint across human–mouse exons of varying lengths and positions is informative, the manuscript's headline claims that the test has "a false-positive rate lower than all current methods" and a false-negative rate directly competitive with *ab initio* gene predictors rest on three methodological flaws. First, the ~2.6% false-positive rate in Table 3 is not an empirical discovery of high specificity, but a mathematical artifact of applying a two-sided $\chi^2_1$ critical value at $\alpha = 0.05$ ($LR > 3.841$) while only rejecting in one tail ($K_A/K_S < 1$), which has a theoretical null rejection probability of $\alpha/2 = 2.5\%$. Second, the null simulation generates single-frame, stop-codon-free sequences with uniform codon usage and no transition/transversion or CpG bias, whereas scanning real unannotated conserved noncoding regions requires testing up to six reading frames, which inflates the per-region false-positive rate. Third, the empirical pipeline conditions on known full-length protein alignments and exact human exon boundaries, bypassing the splice-site, reading-frame, and indel alignment errors faced by actual gene prediction tools. These issues can be resolved through computational re-analysis using realistic noncoding alignments and six-frame scanning alongside a reframing of the comparative benchmarks.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Human–mouse orthologous exons $\ge 100\text{ bp}$ and $\ge 300\text{ bp}$ exhibit strong purifying selection detectable by the $K_A/K_S$ LRT: [Well Supported].**  
  Across 1,244 annotated exons, the median $K_A/K_S$ is 0.054 (mean 0.105), 93.8% (649/692) of internal exons in the 100–150 bp classes pass the LRT, and 100% (87/87) of exons $\ge 300\text{ bp}$ (including all 25 single-exon genes) achieve $K_A/K_S < 1$ at $P < 0.05$ (Table 2, Figure 1A).

* **The $K_A/K_S$ test has a false-positive rate of ~2.6% on noncoding regions, "lower than all current methods": [Methodologically Flawed].**  
  Under the null hypothesis $K_A/K_S = 1$, $LR = 2(\ln ML_1 - \ln ML_2) \sim \chi^2_1$. Testing $LR > 3.841$ ($P < 0.05$) is a two-tailed test of $K_A/K_S \ne 1$; restricting positives to the lower tail ($K_A/K_S < 1$) halves the nominal Type I error rate to 2.5%. The simulated 2.6% average false-positive rate in Table 3 simply recovers this nominal $\alpha/2 = 2.5\%$ threshold in a single predetermined reading frame after artificially mutating away stop codons. Moreover, comparing a single-frame hypothesis test at a fixed $\alpha/2$ against the genome-wide exon false discovery rate of *ab initio* predictors (7%–28% in Rogic et al.) is an apples-to-oranges comparison.

* **The test achieves a 9.5% false-negative rate comparable to or better than existing gene predictors (8%–32%): [Overstated].**  
  The 9.5% false-negative rate is obtained on pre-extracted coding sequences aligned at the full-length protein level via CLUSTALW and sliced using known human RefSeq exon coordinates (Methods, steps 1–4), while excluding alignments $< 30\text{ bp}$ and assuming identical mouse exon–intron structures. In realistic genome annotation, local genomic alignments include frame-shifting indels, unaligned splice boundaries, and unknown reading frames, which will increase the operational false-negative rate.

* **Failure rates do not differ significantly between initial (16%), terminal (14%), and internal (8%) exons: [Methodologically Flawed].**  
  In "The $K_A/K_S$ Ratio Test" section, the authors report failure rates of 16% ($N = 114$), 14% ($N = 114$), and 8% ($N = 991$) and state "although this difference was not statistically significant, internal exons tend to be recognized best." In fact, a $3 \times 2$ contingency table test on their exact counts ($\sim 18/114$, $16/114$, and $79/991$, summing to $113$ or $118$ failing multi-exon units) yields $\chi^2 = 10.8, \text{df} = 2, P = 0.0045$ (and $P = 0.006$ comparing initial vs. internal exons directly). The authors erroneously inferred non-significance from visual inspection of wide binomial confidence intervals.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Statistical Interpretation of the One-Sided LRT and Account for Six-Frame Testing
* **WHY:** Comparing $LR = 2(\ln ML_1 - \ln ML_2)$ to $\chi^2_1(\alpha = 0.05)$ while requiring $K_A/K_S < 1$ is a one-sided test with nominal size $\alpha/2 = 0.025$. Furthermore, in an unannotated conserved genomic block between human and mouse, the reading frame and coding strand are unknown, requiring evaluation of all stop-free reading frames among the 6 possible frames.
* **WHAT:** Explicitly state that a $\chi^2_1$ threshold at $P = 0.05$ corresponds to a 2.5% one-tail nominal error rate per tested reading frame, and quantify the family-wise false-positive rate across all open reading frames in a conserved noncoding segment.
* **HOW:** Re-run the simulation (or empirical intronic/intergenic alignments) by scanning all 6 reading frames in each simulated alignment, running `codeml` on every frame lacking internal stop codons, and reporting the proportion of noncoding alignments where *at least one* reading frame yields $K_A/K_S < 1$ at $P < 0.05$ (and after Bonferroni correction for the number of open frames tested).

#### 2. Evaluate False-Positive Rates on Real Conserved Noncoding Sequences (CNS) or Realistic Sequence Simulations
* **WHY:** The current simulation generates codons uniformly (1/61), applies Jukes-Cantor-like uniform nucleotide substitutions without transition/transversion bias ($\kappa$) or CpG hypermutability, and actively replaces any mutation that introduces a stop codon (Methods, "Computer Simulation"). Real mammalian conserved noncoding regions exhibit strong transition bias ($\kappa \approx 2$–$4$), CpG dinucleotide decay, and natural stop codons.
* **WHAT:** Benchmark the false-positive rate on authentic human–mouse conserved noncoding alignments (e.g., aligned introns or 5'/3' UTRs from the same 153 LocusLink genes).
* **HOW:** Extract orthologous human–mouse 5' UTR, 3' UTR, and conserved intronic segments ($\ge 30\text{ bp}$ and $\ge 80\%$ identity) from the 153 LocusLink entries, identify maximal stop-free reading frames $\ge 30\text{ bp}$, and run the exact `codeml` pipeline to measure the empirical false-positive rate on real noncoding DNA.

#### 3. Test Sensitivity to Local Genomic Nucleotide Alignment Instead of Protein-Guided Full-CDS Alignment
* **WHY:** Aligning full-length translated proteins with CLUSTALW before slicing into exons (Methods, steps 2–4) leaks global protein reading-frame information that is unavailable when evaluating an unannotated genomic block.
* **WHAT:** Evaluate how the $K_A/K_S$ test performs when exons are aligned directly at the nucleotide level.
* **HOW:** Align the 1,244 orthologous exon pairs directly as nucleotide sequences using a local aligner (e.g., BLASTN or Smith–Waterman), trim to the longest stop-free reading frame, and report the resulting false-negative rate alongside the protein-guided baseline.

#### 4. Correct the Contingency Table Test for Exon Position and Temper Claims Against *Ab Initio* Predictors
* **WHY:** The claim that the difference in false-negative rates across initial (16%), terminal (14%), and internal (8%) exons is "not statistically significant" is contradicted by a standard $\chi^2$ test ($P < 0.005$), and the abstract claim that the test has "a false-positive rate lower than all current methods" conflates a single-frame LRT nominal $\alpha/2$ level with full-gene prediction specificity.
* **WHAT:** Report the exact $\chi^2$ or Fisher's exact test $P$-value for exon categories and revise the Abstract and Discussion to frame the $K_A/K_S$ test as a complementary comparative filter rather than a standalone competitor with a lower false-positive rate than all gene finders.
* **HOW:** Replace "although this difference was not statistically significant" (page 3, "The $K_A/K_S$ Ratio Test") with the exact $\chi^2$ statistic and $P$-value, and revise point (3) of the Abstract to state that the test achieves a 9.5% false-negative rate on aligned orthologous exons at a nominal 2.5% per-frame false-positive threshold.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several numerical and typographical errors appear in Tables 1, 2, and 3.
* **WHAT & HOW:**
  1. **Table 1:** Under `% Identity with mouse`, the sub-headers `overall` and `third pos.` are misaligned with the data columns (`All c` has 8 columns while `Initial d`, `Internal`, `Terminal d`, and `Single-exon genes` have 7 columns, missing the third-position identity or overall identity column). Restore the missing column values for those four rows.
  2. **Table 2:** In the `All` row under `Ka range`, `0–0.863` is inconsistent with the component rows (`Internal` reaches `1.863` and `Last` reaches `1.340`). Correct `0–0.863` to `0–1.863`. Also fix the header typo `mean (S)` under `Ks` to `mean (SD)`.
  3. **Table 3:** In the first column header under `Length (codons/nucleotides)`, change `17/5` to `17/51` (17 codons = 51 nucleotides). In the `20%` divergence row under column `34/102`, check `2.9 (1.5–3.5)`—a binomial proportion of $29/1000$ (2.9%) has a 95% CI of `(1.9–3.9)`, whereas `2.5%` has `(1.5–3.5)`.
  4. **Results ("Set of Orthologous Exons"):** Correct the spelling of `lamilin α 2 chain gene` to `laminin α2 chain gene`.
  5. **Discussion (paragraph 5):** Correct the spelling of `LocuLink` to `LocusLink`.
