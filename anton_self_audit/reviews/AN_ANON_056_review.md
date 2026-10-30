# Review of AN_ANON_056

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.3 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces `Galaxy2 ENCODE`, an open-source web application and data integration portal for the ENCODE Consortium that links standardized consortium datasets with over 100 genomic interval, multiple sequence alignment (`MAF`), and molecular evolution tools, documented via an interactive history system and 19 screencasts. To illustrate the platform, the authors present two rapid (<15 min) analyses across the ENCODE regions: (1) identifying `9,191` "Non-GENCODE" expressed sequence tags (`ESTs`, comprising `27,202` exons) outside GENCODE annotations, testing their overlap with `Exoniphy` protein-coding predictions (`1` EST match, `DR731323`), `phastCons` vertebrate conservation scores ($\ge 0.2$), and Affymetrix `transfrags`; and (2) estimating mammalian nucleotide substitution branch lengths under a general reversible (`REV`) model across `364 kb` of autosomal ancestral repeats (`ARs`) in five mammals (`human, chimpanzee, mouse, rat, dog`).

As a bioinformatics software resource and consortium data portal, `Galaxy2 ENCODE` is well engineered, lowers technical barriers for interval and comparative genomic workflows, and provides a clean neutral evolutionary rate benchmark showing that ENCODE autosomal ancestral repeats match genome-wide mammalian substitution rates. However, the biological vignette on Non-GENCODE ESTs contains three methodological and numerical flaws: (1) the null control for `EST`–`transfrag` overlap (`Experiment B`, line 93) intersects `EST` exons with simulated `EST`-sized intervals explicitly restricted to lie *outside* `transfrags`, creating an asymmetric and circular baseline; (2) the counts of conserved Non-GENCODE EST subcategories in line 91 (`942 intronic + 221 intergenic + 9 intertwined = 1,172`) do not sum to the reported total of `2,180`; and (3) interpreting intronic `phastCons` $\ge 0.2$ as purifying selection on independent transcripts overlooks conserved intronic cis-regulatory elements and pre-mRNA/genomic contamination. Re-running the random-interval permutation test symmetrically, reconciling the `2,180` vs. `1,172` EST count, and tempering the functional transcript claim will bring the biological showcase in line with the quality of the software platform.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`Galaxy2 ENCODE` integrates interval operations, comparative genomics, and phylogenetic tools with transparent history tracking: [Well Supported].**  
  The platform provides a unified web interface, automated ENCODE file standardization and region partitioning (`encode-upload`), user histories, and simple command-line tool wrapping, backed by open-source code and 19 screencasts.

* **Nucleotide substitution rates in ENCODE autosomal ancestral repeats match genome-wide mammalian estimates: [Well Supported].**  
  Fitting the general reversible (`REV`) model with profile-likelihood 95% confidence intervals across `364 kb` of 5-species ancestral repeat alignments yields branch lengths (`human: 0.006`, `chimp: 0.007`, `mouse: 0.084`, `rat: 0.112`, `dog: 0.231`) that are consistent with whole-genome consortium estimates, confirming that ENCODE autosomal regions are representative of average euchromatic neutral divergence.

* **Scarcity of unannotated multi-exon protein-coding genes among Non-GENCODE ESTs: [Well Supported].**  
  Intersecting the `27,202` Non-GENCODE EST exons with `Exoniphy` ab initio coding exon predictions ($\ge 75\%$ base coverage across $\ge 3$ consecutive exons) identifies only a single transcript (`DR731323`), which represents a 3'-end extension of `ENST00000355799`.

* **Over 2,000 (`2,180`) unannotated ESTs are under strong purifying selection and likely represent functional transcripts: [Overstated].**  
  First, the breakdown reported in line 91 (`942` intronic, `221` intergenic, and `9` intertwined) sums to `1,172`, leaving `1,008` of the claimed `2,180` transcripts unaccounted for. Second, at least `80%` (`942 / 1,172`) of the categorized transcripts are *intronic*. Because `phastCons` measures DNA sequence conservation across vertebrates rather than RNA-level purifying selection, unspliced intronic EST fragments (which frequently arise from pre-mRNA or genomic DNA priming) overlapping conserved intronic enhancers or splicing regulatory elements will exhibit `phastCons` $\ge 0.2$ without representing independent functional non-coding RNAs.

* **Overlap between Non-GENCODE EST exons and Affymetrix `transfrags` is statistically nonrandom (`Experiment A` vs. `Experiment B`, Table 2): [Methodologically Flawed].**  
  In line 93, `Experiment A` measures the intersection between `Non-GENCODE EST exons` and `transfrags` ($\text{EST} \cap \text{TF}$). To construct the null control (`Experiment B`), instead of generating random intervals matched to `EST exons` across the whole non-GENCODE space and intersecting them with `transfrags` ($R_{\text{EST}} \cap \text{TF}$), the authors generated random intervals $R_{\text{EST}}$ mimicking the length distribution of `Non-GENCODE EST exons` **constrained to lie outside `transfrags`**, and then intersected `Non-GENCODE EST exons` with $R_{\text{EST}}$ ($\text{EST} \cap R_{\text{EST}}$). This test is invalid for three reasons: (1) total base coverage of $R_{\text{EST}}$ equals the total length of `EST exons`, not the total length of `transfrags`; (2) forcing $R_{\text{EST}}$ to lie strictly outside `transfrags` guarantees that the subset of `EST exons` overlapping `transfrags` has zero overlap with $R_{\text{EST}}$; and (3) only a single random draw was performed (`n = 1` replicate, no empirical $p$-value).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Redesign the `Random Intervals` Overlap Test (`Experiment B`) to Perform a Symmetric Monte Carlo Permutation Test
* **WHY:** Intersecting `EST exons` with `EST`-sized random intervals placed outside `transfrags` (`Experiment B`, line 93) does not test the null hypothesis that `EST exons` and `transfrags` assort independently across non-GENCODE genomic space.
* **WHAT:** Generate $N = 1,000$ random interval sets $R^{(k)}$ matched in number, length distribution, and chromosomal/intronic/intergenic compartment to `Non-GENCODE EST exons` across the eligible non-GENCODE ENCODE space *without* masking out `transfrags`, and compute the null distribution of base-pair overlap with `transfrags` ($R^{(k)} \cap \text{TF}$).
* **HOW:** Using the `Random Intervals` tool in `Galaxy2 ENCODE`, sample intervals within the non-GENCODE mask (preserving intronic vs. intergenic regional proportions), intersect each of the `1,000` random draws with the Affymetrix `transfrags` track (`Experiment B'`), and report the mean, standard deviation, fold-enrichment, and empirical $p$-value in Table 2.

#### 2. Reconcile the Arithmetic Discrepancy in Conserved Non-GENCODE EST Counts (`2,180` vs. `1,172`)
* **WHY:** Line 91 states that `2,180` Non-GENCODE ESTs have all exons with average `phastCons` $\ge 0.2$, itemized as *"942 intronic, 221 intergenic, and nine intertwined"*, which sum to $942 + 221 + 9 = 1,172$.
* **WHAT:** Audit the relational join / grouping step in Screencast 16 and update line 91 (and the Abstract if total $< 2,000$) so that the category counts sum exactly to the total number of unique EST transcripts.
* **HOW:** Check whether `2,180` was the number of *exons* belonging to those `1,172` ESTs (out of the `3,705` conserved exons) or whether one category count was truncated during table transcription, and report both the exact transcript count and exon count for each of the three categories.

#### 3. Stratify Conserved Non-GENCODE ESTs by Splicing Status and Temper Functional Non-Coding Transcript Claims
* **WHY:** Unspliced single-exon intronic ESTs overlapping conserved intronic DNA (`phastCons` $\ge 0.2$) frequently reflect intronic cis-regulatory elements or pre-mRNA carryover rather than independent functional transcripts.
* **WHAT:** Report what fraction of the conserved intronic (`942`) and intergenic (`221`) ESTs are multi-exon spliced transcripts with canonical splice sites versus single-exon fragments, and temper the Abstract/Discussion framing accordingly.
* **HOW:** Filter the conserved Non-GENCODE EST set by exon count ($\ge 2$ exons vs. $1$ exon) in `Galaxy2 ENCODE`, report both counts in Section 3, and revise the Abstract to note that these conserved unannotated regions represent candidate functional non-coding transcripts *or intronic cis-regulatory elements*.
