# Review of AN_ANON_023

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.8 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.8/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces StructureFold, a four-module software pipeline integrated into a web-based workflow platform (and available for local installation) for transcriptome-wide RNA secondary structure reactivity derivation and restrained structure prediction from high-throughput reverse transcription (RT) stop sequencing data (such as Structure-Seq, DMS-seq, or nuclease probing). The four modules perform iterative Bowtie read mapping with end-trimming, 5'-offset RT stop counting for (+) and (–) reagent libraries, log-transformed transcript-abundance/length normalization followed by 2–8% scaling to compute Final Structural Reactivities (FSRs), and secondary structure prediction via RNAstructure (using pseudo-free energy soft restraints) or ViennaRNA. The authors validate StructureFold reactivities on *Arabidopsis thaliana* 18S and 25S rRNAs against conventional PAGE gel intensities ($R = 0.69$, matching ROC curves against phylogenetic rRNA structures) and against Mod-seeker reactivities ($r = 0.91$ and $0.93$).

StructureFold provides a practical, end-to-end bioinformatic workflow that lowers the barrier for experimentalists analyzing high-throughput RNA structure-probing datasets, and its rRNA validation against PAGE gel probing and phylogenetic structures is solid. The primary methodological limitation is a disconnect between the mathematical normalization in Equations (1)–(2) and the headline claim that StructureFold renders nucleotide reactivities "directly comparable" across transcripts of varying abundance and length: dividing $\ln(\text{count}+1)$ by the transcript-mean of $\ln(\text{count}+1)$ does not make reactivities invariant to sequencing depth $N$ (because a multiplicative change in abundance $N$ adds $\ln N$ to both numerator and denominator, compressing the differences $P(i) - M(i)$ as $1/\ln N$ on highly expressed transcripts). Moreover, all empirical validations (Section 3.1 and Section 3.2) are restricted to two hyper-abundant transcripts (18S and 25S rRNA), leaving cross-transcript comparability across low- and moderate-abundance mRNAs untested. These issues can be addressed through mathematical clarification and stratified benchmarking on existing transcriptome-wide datasets.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **StructureFold automates read mapping, RT-stop counting, reactivity calculation, and restrained RNA structure prediction in an accessible modular pipeline: [Well Supported].**  
  The four modules (Iterative Mapping, Get RT Stop Counts, Reactivity Calculation, and RNA Structure Prediction) are logically chained, account for the 1-nt 5' offset of RT termination relative to chemical modification/cleavage sites, and wrap established folding engines (RNAstructure v5.6 and ViennaRNA v2.1.9).

* **StructureFold FSRs on *Arabidopsis* 18S and 25S rRNAs closely match classical PAGE gel band intensities and Mod-seeker reactivities and accurately discriminate single-stranded from base-paired nucleotides: [Well Supported].**  
  Figure 5 and Table 3 demonstrate strong concordance with gel-based DMS probing ($R = 0.69$ on 25S nt 1217–1303; matching ROC curves across four 18S/25S regions) and high correlation with Mod-seeker ($r = 0.91$ on 18S, $r = 0.93$ on 25S), with 86.7% (96.7% including helix ends/defects) of high-reactivity 18S sites being single-stranded in the comparative phylogenetic structure.

* **Normalizing by the mean log-count in Equations (1) and (2) makes structural reactivities directly comparable across transcripts of different abundances and lengths: [Fragile].**  
  In Equations (1) and (2), the authors define $P(i) = \ln[P_r(i)+1] / \left(\frac{1}{l}\sum_{j=0}^l \ln[P_r(j)+1]\right)$. If raw stop counts scale with transcript abundance $N$ as $P_r(i) \approx N p_i$, then $\ln(P_r(i)+1) \approx \ln N + \ln p_i$. Dividing by the transcript mean $\approx \ln N + \overline{\ln p}$ yields $P(i) - M(i) \approx \frac{\ln(p_i/m_i)}{\ln N + \text{const}}$, meaning that the scale of raw structural reactivities (RSRs) is inversely proportional to $\ln N$ rather than invariant to transcript abundance $N$. When a single global 2–8% normalization is subsequently applied across the entire transcriptome, low-abundance transcripts will systematically exhibit inflated variance and higher extreme RSRs than high-abundance transcripts. No empirical benchmark across transcripts of varying abundance is presented to validate cross-transcript comparability.

* **Incorporating StructureFold in vivo restraints substantially alters and improves mRNA secondary structure predictions transcriptome-wide (e.g., *AT5G53300.3* in Fig. 4): [Moderately Supported].**  
  While pseudo-free energy restraints ($\Delta G(i) = 1.8 \ln[\text{Reactivity}(i)+1] - 0.6$ kcal/mol) are well established for rRNAs and benchmarked in Supplementary Table S1, Figure 4 only shows that the restrained and unrestrained minimum free energy structures of *AT5G53300.3* differ visually, without an orthogonal structural ground truth for that mRNA.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Benchmark Reactivity Comparability and Coverage Thresholds Across Transcript Abundances
* **WHY:** All validation in the main text is conducted on 18S and 25S rRNA, which have massive read depth, whereas Equations (1) and (2) exhibit a $1/\ln N$ scaling dependence on transcript read depth $N$ and discrete count noise at low coverage.
* **WHAT:** Evaluate the stability and distribution of FSRs across transcripts spanning a wide range of expression levels, or perform subsampling of the 18S/25S rRNA reads to simulate lower-abundance mRNAs.
* **HOW:** Downsample the mapped (+) and (–) DMS reads on 18S and 25S rRNA across serial orders of magnitude (e.g., 100%, 10%, 1%, 0.1%, 0.01% of reads), recompute StructureFold FSRs alongside other transcriptome transcripts, and plot the Pearson correlation and ROC AUC against the full-depth phylogenetic truth as a function of average RT stops per nucleotide.

#### 2. Compare Log-Ratio / Count-Based Normalization Against Ratio-of-Logs Normalization
* **WHY:** Dividing $\ln(P_r(i)+1)$ by the mean of $\ln(P_r(j)+1)$ mixes additive log-space abundance shifts with multiplicative scaling. In contrast, normalizing raw counts by transcript coverage first—e.g., $\tilde{P}_r(i) = P_r(i) / \left(\frac{1}{l+1}\sum_{j=0}^l P_r(j)\right)$—before taking $\ln(\tilde{P}_r(i)+1)$ or computing $\ln\frac{\tilde{P}_r(i)+\epsilon}{\tilde{M}_r(i)+\epsilon}$ makes the estimator mathematically invariant to transcript abundance $N$.
* **WHAT:** Test whether normalizing raw stop counts by total transcript stops prior to log-transformation removes depth dependence across transcripts of different abundances.
* **HOW:** Implement coverage-first normalization as an option in Module 3 and compare the distribution of RSRs across high-, medium-, and low-abundance *Arabidopsis* mRNAs against Equations (1)–(2).

#### 3. Clarify Nucleotide Filtering for Base-Specific Chemical Probes (DMS vs. SHAPE)
* **WHY:** DMS modifies only unpaired adenines (A) and cytosines (C), whereas SHAPE and nucleases probe all four bases. Module 2 outputs counts for all four nucleotides (A, C, G, U), and Module 3 applies 2–8% normalization across the data. Including unreactive G and U bases in the denominator sum of Equations (1)–(2), in the 2–8% quantile calculation, or as zero-reactivity pseudo-energy restraints in Module 4 can skew both scaling and folding.
* **WHAT:** Specify explicitly in Sections 2 and 3.1 whether G and U nucleotides are masked (set to missing/`-999` in RNAstructure) during DMS reactivity normalization, ROC generation, and structure folding.
* **HOW:** Add a parameter description in Module 3 and Module 4 documenting base-specific masking (A/C-only for DMS vs. A/C/G/U for SHAPE), and state in Section 2.1 whether the 18S/25S ROC curves were computed over A/C bases only or all four nucleotides.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** A misplaced bracket in Equation (2) makes the formula mathematically undefined when $M_r(i) = 0$.
* **WHAT & HOW:**
  * **Section 2, Equation (2) (line 143):** Correct the denominator from $(\sum_{i=0}^l \ln[M_r(i)] + 1)/l$ to $(\sum_{i=0}^l \ln[M_r(i) + 1])/l$ so that the $+1$ pseudocount is inside the natural logarithm, matching Step 1 and Equation (1). Also note that summing from $i = 0$ to $l$ includes $l + 1$ positions (including the 5'-runoff count at $i = 0$), so the average per position is division by $l + 1$ (or clarify why $l$ is used).
