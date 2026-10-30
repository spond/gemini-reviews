# Review of AN_ANON_023

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces StructureFold, a four-module software pipeline integrated into a web-based workflow platform for deriving transcriptome-wide nucleotide structural reactivities from high-throughput sequencing (Structure-Seq / chemical or nuclease probing) and predicting experimentally restrained RNA secondary structures. The four modules perform (1) iterative 5'/3' read trimming and Bowtie mapping to a reference transcriptome, (2) nucleotide-level reverse transcriptase (RT) stop counting (assigning stops 1 nt 5' of the cDNA terminus for chemical probes or at the cleavage site for nucleases), (3) log-transformed, transcript-length-and-abundance-normalized reactivity derivation followed by 2–8% normalization and capping to produce Final Structural Reactivities (FSRs), and (4) secondary structure prediction via RNAstructure (v5.6, using pseudo-free energy soft restraints $\Delta G(i) = 1.8 \ln[\text{Reactivity}(i)+1] - 0.6$) or ViennaRNA (v2.1.9, hard restraints). The authors validate StructureFold on *Arabidopsis* in vivo DMS-probed 18S and 25S rRNAs against PAGE gel intensities ($R = 0.69$, matching ROC curves against phylogenetic rRNA structures) and against Mod-seeker ($r = 0.91$ and $0.93$).

StructureFold provides a practical, accessible web-based pipeline that bridges raw structure-probing reads and thermodynamic folding packages. However, several methodological and validation gaps limit the strength of its broader claims: (1) all empirical validations (gel comparison, ROC curves, and Mod-seeker concordance) are restricted exclusively to two highly abundant ribosomal RNAs (18S and 25S), leaving the central claim that FSRs are "directly comparable" across mRNAs of varying abundance and length untested; (2) the log-average denominator in Equations (1)–(2) conflates transcript coverage depth with intrinsic structural openness (mean log stop count per base); (3) DMS reactivity is computed and restrained across all four bases (A, C, G, U) in Equations (1)–(3) even though DMS specifically methylates Watson-Crick faces of A and C; and (4) Equation (2) contains a mathematical bracket typo in the denominator. These issues can be addressed by adding cross-transcript coverage sensitivity benchmarks, restricting DMS restraints and ROC analyses to A/C bases (or documenting G/U handling), and correcting the equation typography.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **StructureFold FSRs on 18S and 25S rRNAs closely match classical PAGE gel-based DMS intensities ($R = 0.69$) and Mod-seeker reactivities ($r = 0.91$–$0.93$), achieving comparable ROC discrimination of phylogenetically single-stranded nucleotides: [Well Supported].**  
  Across four regions of *Arabidopsis* 18S (nt 17–86, 87–207, 298–428) and 25S (nt 1217–1303) rRNA, StructureFold FSRs track normalized PAGE band intensities and yield ROC curves well above the random diagonal. In Table 3, high-reactivity bases ($\ge 0.6$) correspond to single-stranded or helix-end/defect positions in 96.7% (18S) and 93.1% (25S) of cases, slightly outperforming Mod-seeker (93.1% and 91.8%).

* **Equations (1) and (2) properly normalize for transcript abundance and length so that in vivo reactivities on different RNAs across a transcriptome are "directly comparable": [Fragile].**  
  In Equation (1), $P(i) = \frac{\ln[P_r(i) + 1]}{(\sum_{i=0}^{l} \ln[P_r(i) + 1]) / l}$. Because the nonlinearity of $\ln(x + 1)$ is applied *before* dividing by the transcript-wide average, this normalization is not scale-invariant with respect to transcript abundance (sequencing depth $\lambda$). Specifically, for a high-abundance transcript where $P_r(i) = \lambda p_i \gg 1$, $\ln(\lambda p_i + 1) \approx \ln \lambda + \ln p_i$, so as $\lambda \to \infty$, the ratio $P(i) \to 1$ for all bases, compressing dynamic range on abundant transcripts while remaining linear ($P_r(i) \ll 1 \implies \ln(1+P_r(i)) \approx P_r(i)$) on low-abundance transcripts. Furthermore, the denominator divides by the average log-stops across the transcript, which means a highly structured transcript (few single-stranded bases) and an unstructured transcript (many single-stranded bases) at the exact same expression level will be scaled differently. Finally, the manuscript presents zero validation on mRNAs of differing abundance (only 18S and 25S rRNA are benchmarked).

* **Iterative 5'/3' read trimming followed by Bowtie re-alignment accurately maps adapter-contaminated or mismatched reads without introducing mapping bias: [Moderately Supported].**  
  While iterative trimming recovers reads containing variable-length 3' adapters, repeatedly stripping $k$ nucleotides from unmapped reads until they reach the minimum length threshold risks mapping short, over-trimmed fragments to non-unique or paralogous transcriptome loci, or shifting the apparent 5' cDNA terminus (which defines the exact RT stop nucleotide) if 5' trimming is enabled.

* **Applying SHAPE-derived pseudo-free energy parameters ($\Delta G(i) = 1.8 \ln[\text{Reactivity}(i)+1] - 0.6$) and all-nucleotide counting to DMS probing data is biochemically appropriate: [Moderately Supported].**  
  In Section 1 (line 73), the authors note that DMS methylates only the N1 of adenine and N3 of cytosine. Yet in Section 2 (lines 121, 131, 162, 217), Get RT Stop Counts, Reactivity Calculation, ROC curve generation, and $\Delta G(i)$ pseudo-energy restraints are defined over "all four nucleotides (A, C, G, U)." Unreactive G and U bases in DMS experiments have near-zero FSRs, which under Equation (3) ($\Delta G = 1.8 \ln(0 + 1) - 0.6 = -0.6\text{ kcal/mol}$) applies an artificial stabilizing bonus toward base-pairing on every G and U nucleotide unless G/U bases are masked as missing data.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Benchmark Cross-Transcript Abundance Invariance and Fix Non-Linear Log-Depth Distortion
* **WHY:** Because $\frac{\ln(\lambda p_i + 1)}{\frac{1}{l}\sum \ln(\lambda p_j + 1)}$ converges toward 1 as sequencing depth $\lambda$ increases, FSRs are mathematically dependent on transcript read depth, contradicting the claim that reactivities across low- and high-abundance RNAs are directly comparable.
* **WHAT:** Evaluate how StructureFold FSRs behave across expression levels by downsampling the 18S/25S rRNA reads across 4 orders of magnitude (e.g., 100%, 10%, 1%, 0.1% of reads) and comparing the resulting FSRs against the full-depth profile.
* **HOW:** Subsample the aligned BAM files for 18S and 25S rRNA across coverage tiers from 100,000$\times$ down to 10$\times$ average stops per nucleotide, compute the Pearson correlation and mean absolute error of FSRs across depths, and compare against normalizing raw counts by transcript abundance *prior* to log-transformation: $\ln\left(1 + \frac{P_r(i)}{\frac{1}{l+1}\sum_{j=0}^l P_r(j)}\right)$.

#### 2. Mask Non-Target Nucleotides (G and U) in DMS Reactivity Scaling, ROC Curves, and Folding Restraints
* **WHY:** DMS probes Watson-Crick positions of A and C only; including G and U nucleotides in the 2–8% normalization percentile, ROC sensitivity/specificity calculations, and Equation (3) pseudo-free energy restraints ($\Delta G = -0.6\text{ kcal/mol}$ when $\text{FSR}=0$) biases both validation metrics and structure predictions.
* **WHAT:** Add a probe-specificity option in Modules 3 and 4 (`--bases AC` for DMS vs. `--bases ACGU` for SHAPE/nuclease) so that unprobed bases are set to `-999` (the standard RNAstructure missing-data code) rather than `0.0`.
* **HOW:** Update the Reactivity Calculation module to compute the 2–8% normalization factor exclusively over target bases (A/C for DMS), output `-999` for G/U in the `.shape`/restraint file passed to `Fold` in RNAstructure, and report A/C-only vs. all-base ROC AUCs in Figure 5 and Table 3.

#### 3. Prevent 5'-End Iterative Trimming from Shifting Assigned RT Stop Coordinates
* **WHY:** In chemical and nuclease structure probing, the RT stop site is determined by the exact 5' end of the cDNA (3' end of the RNA fragment in directional libraries). Allowing users to iteratively trim unmapped reads from the end that defines the RT termination site (line 119) shifts the mapped stop coordinate downstream by the trim step size.
* **WHAT:** Restrict iterative trimming in Module 1 to the 3' cDNA end (opposite the RT stop site), while permitting only fixed-length barcode/adapter stripping at the 5' cDNA end before alignment.
* **HOW:** Modify the Iterative Mapping wrapper so that iterative unmapped-read truncation operates solely via Bowtie's `-3` flag, and add a warning in the user interface explaining that trimming the RT-stop end alters single-nucleotide reactivity assignment.

#### 4. Correct the Mathematical Typo in Equation (2) and Report Numerical AUC Values in Figure 5
* **WHY:** In Equation (2) (line 143), the denominator is written as $(\sum_{i=0}^{l} \ln[M_r(i)] + 1) / l$, placing the $+1$ outside the natural logarithm $\ln[M_r(i)]$, which is undefined ($\ln 0 = -\infty$) whenever $M_r(i) = 0$ and contradicts both the text in Step 1 (line 129) and Equation (1) ($\ln[P_r(i) + 1]$). Additionally, Figure 5 plots five pairs of ROC curves without reporting their quantitative Area Under the Curve (AUC) values or confidence intervals.
* **WHAT & HOW:** Fix Equation (2) on line 143 to read:
  $$M(i) = \frac{\ln[M_r(i) + 1]}{\left(\sum_{i=0}^{l} \ln[M_r(i) + 1]\right) / (l + 1)}$$
  (and note that summing from $i=0$ to $l$ includes $l+1$ terms, so the divisor should be $l+1$ or explicitly justified as $l$). Calculate and print the exact ROC AUC values and DeLong 95% confidence intervals for both StructureFold and gel-based intensities on panels 5c–5g.
