# Review of AN_ANON_074

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.8 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.8/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This web server manuscript describes `ETOPE` (`http://nekrut.uchicago.edu/etope/`), an online comparative genomics tool designed to validate computationally predicted exons and gene models (such as `Genscan` predictions) that lack supporting EST or expression evidence. Given a query nucleotide sequence or `Genscan` output from one species, `ETOPE` searches a pre-indexed transcript or gene-prediction database from a moderately diverged mammal (10–30% coding divergence; Table 1) using discontinuous `MEGABLAST` (`-W 16 -t 11 -q -2`), selects the highest-scoring alignment devoid of stop codons, translates both sequences into amino acids, realigns the translations globally using `ClustalW 1.8` to enforce codon-to-codon nucleotide alignment, estimates synonymous ($K_S = S_S/L_S$) and nonsynonymous ($K_A = S_N/L_N$) substitution rates using the approximate method of Yang and Nielsen (2000) in `PAML`, and tests $K_A/K_S < 1$ ($P < 0.05$) using a $2 \times 2$ Fisher's exact test on changed versus unchanged sites. An illustrative application to a 150-kb candidate interval on rat chromosome 1 (`38,050,000–38,200,000`) confirms 8 of 15 computational gene predictions against human UniGene sequences.

Using evolutionary purifying selection ($K_A/K_S < 1$) to distinguish true protein-coding exons from false-positive ab initio predictions is biologically well-founded and addresses a practical gap in genome annotation for species with sparse EST coverage. However, the statistical and algorithmic implementation in `ETOPE` has three substantive methodological flaws: (1) feeding continuous, multiple-hit-corrected substitution estimates ($S_S, S_N$) and effective site counts ($L_S, L_N$) from Yang–Nielsen (`YN00`) into a $2 \times 2$ Fisher's exact test of "changed vs. unchanged sites" violates the binomial/hypergeometric assumptions of Fisher's test and underestimates estimation variance, (2) selecting a database hit conditioned on having zero stop codons and then realigning the translated amino acid sequences with `ClustalW` introduces an alignment bias that artificially depresses $K_A/K_S$ on non-coding sequences, and (3) testing individual short `Genscan` exons (often 30–50 codons) suffers from low statistical power that is not quantified for users.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Testing for purifying selection ($K_A/K_S < 1$) between homologous sequences at 10–30% divergence is an effective evolutionary criterion for validating unannotated protein-coding regions: [Well Supported].**  
  Prior theoretical, simulation, and RT–PCR validation studies (Nekrutenko et al., ref. 7; Guigó et al., ref. 4) establish that functional protein-coding exons experience purifying selection against nonsynonymous substitutions ($K_A < K_S$), providing an orthogonal evolutionary signal to hexamer composition and splice-site motifs used by single-genome ab initio predictors.

* **Constructing a $2 \times 2$ contingency table of changed ($S_S, S_N$) and unchanged ($L_S - S_S, L_N - S_N$) sites from Yang–Nielsen (`YN00`) output and applying Fisher's exact test provides a valid test of $K_A/K_S < 1$: [Methodologically Flawed].**  
  In line 40, `ETOPE` takes the effective site counts ($L_S, L_N$) and multiple-hit-corrected substitution counts ($S_S = K_S L_S, S_N = K_A L_N$) from Yang and Nielsen (2000) and plugs them into a $2 \times 2$ Fisher's exact test with columns `[changed (S), unchanged (L - S)]`. This procedure is statistically invalid for three reasons: (a) $L_S, L_N, S_S, S_N$ in `YN00` are continuous (non-integer) expected quantities rather than discrete integer counts; (b) `YN00` corrects for multiple substitutions per site under a Markov codon model, meaning $S_S$ is an expected branch-length sum whose sampling variance is strictly greater than the hypergeometric variance assumed by Fisher's exact test; and (c) whenever synonymous divergence $K_S \ge 1.0$ (which occurs in fast-evolving rodent–human comparisons or poorly aligned segments), $S_S \ge L_S$, making the "unchanged synonymous sites" cell $L_S - S_S \le 0$ and causing Fisher's exact test to break down or become anti-conservative. `YN00` directly outputs analytical standard errors for $K_A$ and $K_S$, and `PAML` (`codeml`) provides an exact 1-df likelihood ratio test against $\omega = 1$, either of which avoids this ad hoc contingency-table approximation.

* **The `ETOPE` alignment pipeline (`MEGABLAST` best stop-free hit followed by `ClustalW` amino-acid realignment) preserves the 3% nominal false-positive rate (at $\alpha = 0.05$) established in prior benchmark simulations: [Fragile].**  
  Line 29 cites a 3% false-positive rate at $P < 0.05$ (and 0.7% at $P < 0.01$) from ref. 7, which evaluated pre-aligned, gapless sequence pairs. In contrast, `ETOPE` (lines 36–38) first filters database hits to retain only matches with zero stop codons in the query reading frame, translates both sequences into amino acids, and then *realigns the amino acid translations using `ClustalW`* before back-translating to codons. When two homologous non-coding sequences (e.g., conserved intronic or UTR elements) contain small indels, `ClustalW` optimizes amino acid similarity by placing codon gaps that maximize amino acid identity (reducing apparent nonsynonymous changes $S_N$) while forcing nucleotide mismatches into third codon positions (inflating apparent synonymous changes $S_S$). Without benchmarking the complete `MEGABLAST` + stop-filter + `ClustalW` pipeline on known non-coding conserved sequences (e.g., 3' UTRs or conserved intronic regions between human and mouse), the true false-positive rate of `ETOPE` is unknown and likely exceeds 3%.

* **The `Genscan` interface accurately validates individual suboptimal exons ($P < 0.75$): [Moderately Supported].**  
  While testing individual suboptimal exons (lines 62, 71–72) is a useful feature when an ab initio gene model fuses a false exon to true exons, the median mammalian internal exon is ~120–150 bp (40–50 codons, or $L_S \approx 30$–$40$ synonymous sites). At 10–15% divergence, a 120-bp exon may accumulate only 3–5 synonymous changes, giving low statistical power to detect moderate purifying selection ($K_A/K_S \approx 0.4$–$0.6$) and a high false-negative rate if users interpret $P \ge 0.05$ as evidence against coding potential.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace the Ad Hoc Fisher's Exact Test on `YN00` Counts with a Likelihood Ratio Test or $Z$-Test
* **WHY:** Plugging continuous, multiple-hit-corrected substitution expectations ($S_S, S_N$) and $L_S - S_S$ from `YN00` into Fisher's exact test (line 40) underestimates the variance of $K_S$ and fails when $K_S \ge 1$.
* **WHAT:** Use the analytical standard errors of $K_A$ and $K_S$ already computed by `YN00` in `PAML` (or a 1-df likelihood ratio test in `codeml` comparing $\omega = \text{free}$ vs. $\omega = 1$) to compute the $P$-value for $K_A < K_S$.
* **HOW:** Since `PAML` is already installed and invoked by `ETOPE` (line 34), parse the `K_A +- SE` and `K_S +- SE` fields directly from the `yn00` output and compute the one-sided $Z$-statistic $Z = (K_S - K_A) / \sqrt{\text{SE}(K_S)^2 + \text{SE}(K_A)^2}$ (or invoke `codeml` with `model = 0`, `fix_omega = 0` vs. `fix_omega = 1`), and report this calibrated $P$-value in the web output.

#### 2. Benchmark the Full `ETOPE` Pipeline on Conserved Non-Coding Controls (Introns and UTRs)
* **WHY:** Filtering for stop-codon-free hits (line 36) and realigning amino acid translations with `ClustalW` (line 38) biases gapped alignments toward lower $K_A/K_S$, so citing the 3% false-positive rate from gapless simulations (ref. 7) is insufficient.
* **WHAT:** Measure the empirical false-positive rate of the end-to-end `ETOPE` pipeline on authentic non-coding sequences.
* **HOW:** Run 1,000 known human 5'/3' UTRs and 1,000 conserved intronic sequences (or false-positive `Genscan` exons located inside annotated introns) through `ETOPE` against the mouse `ug_mm_119` and `gs_mm_10_3` databases, and report the percentage of non-coding queries that pass the `MEGABLAST` stop-codon filter and yield $K_A/K_S < 1$ at $P < 0.05$ and $P < 0.01$. Also consider aligning at the nucleotide level first and masking gapped regions rather than letting `ClustalW` optimize amino acid similarity across indels.

#### 3. Report Minimum Exon Length / Power Guidance for Single-Exon Queries
* **WHY:** Users testing individual short suboptimal `Genscan` exons (lines 71–72) may discard true coding exons that lack enough synonymous sites ($L_S$) to reach $P < 0.05$.
* **WHAT:** Display power guidance in the `ETOPE` output when an aligned region is short (e.g., $< 100$ bp or $S_S + S_N < 6$).
* **HOW:** Add a warning banner to the `ETOPE` results page whenever the aligned nucleotide length is $< 90$ bp (30 codons) or the total number of observed substitutions is $< 6$, advising the user that the test has low statistical power on short exons.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Unit errors of three orders of magnitude and inconsistent author spellings should be corrected.
* **WHAT & HOW:**  
  1. **Line 82 (1,000-fold genomic interval unit error):** Correct `"identified a 150 000 kb candidate locus on rat chromosome 1 between positions 38 050 000 and 38 200 000"` to `"identified a 150 kb (150,000 bp) candidate locus on rat chromosome 1 between positions 38,050,000 and 38,200,000"` ($38,200,000 - 38,050,000 = 150,000\text{ bp} = 150\text{ kb}$, not $150,000\text{ kb}$).  
  2. **Line 29 (Author name spelling):** Correct `"Yang and Neilsen ( 5 )"` to `"Yang and Nielsen ( 5 )"` to match line 40.  
  3. **Source Code Availability:** Make the Perl CGI scripts and `PAML` wrapper code downloadable from `http://nekrut.uchicago.edu/etope/` so that users can run batch validations locally once the Pentium III web server is retired.
