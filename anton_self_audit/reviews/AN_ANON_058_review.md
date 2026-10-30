# Review of AN_ANON_058

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This technical methodology report addresses cross-sample contamination in high-depth next-generation re-sequencing of non-diploid mixtures, specifically human mitochondrial DNA (mtDNA) amplified via two overlapping ~9 kb PCR products across 56 blood and buccal samples. The authors introduce five modular tools integrated into a public workflow platform (`Naive Variant Caller`, `Variant Annotator`, `Get FASTA from Variants Table`, `Phylorelatives`, and `MAF Boxplot`) and propose a two-step diagnostic workflow: first flagging samples that exhibit an elevated number of apparent heteroplasmies (MAF $\ge 2\%$) with tightly clustered minor allele frequencies (low median absolute deviation), and second reconstructing Neighbor-Joining (NJ) trees (1,000 bootstraps, raw $p$-distance) that combine major-allele consensus sequences from all samples with minor-allele synthetic consensus sequences from suspected contaminated samples (`F41M52_MINOR` and `F41M52C1_MINOR`) to trace the donor lineage (identifying carryover from adjacent plate wells containing family `F46`). They also propose an experimental protocol incorporating alternating exogenous DNA spike-ins (pUC18 and $\phi$X174) prior to barcoded library preparation. Raw sequencing data and interactive workflows are provided via a dedicated web page.

The manuscript provides a practical, reproducible quality-control pipeline and an instructive empirical demonstration of well-to-well carryover on a 96-well plate. However, its quantitative rigor is limited by heuristic decision rules and unmodeled edge cases: the flagging threshold ($\ge 10$ minor alleles) and MAF dispersion criteria lack formal statistical calibration or false-positive/false-negative benchmarking across varying haplogroup distances and contamination fractions; the synthetic minor-allele consensus sequence substitutes the minor allele only at detected heteroplasmic sites while retaining the recipient's major allele everywhere else, creating a chimeric haplotype when contamination originates from multiple sources or overlaps true endogenous heteroplasmies; and the proposed alternating pUC18/$\phi$X174 spike-in protocol is presented purely as a conceptual recommendation without empirical validation data showing spike-in read mapping rates or sensitivity thresholds. These limitations can be resolved through synthetic mixture simulations, a formal probabilistic likelihood or dispersion test for MAF clustering, and reporting quantitative validation data for the spike-in assay.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Two-step visual MAF boxplot and NJ phylogenetic clustering detects well-to-well carryover in the 56-sample mtDNA cohort (`F41M52` and `F41M52C1` contaminated by `F46`): [Well Supported].**  
  In the empirical dataset of 56 samples, the expected baseline is 0–3 heteroplasmies per individual. Samples `F41M52` and `F41M52C1` display an anomalously high count of minor alleles with tightly concentrated MAFs (Figure 1), and their minor-allele consensus sequences cluster with high bootstrap support inside family `F46` rather than their own family `F41` (Figure 2), which is independently corroborated by physical adjacency on the 96-well plate sent to the sequencing provider.

* **The `Phylorelatives` minor-allele consensus tree approach is more generalizable and scalable than haplogroup-database (`Haplogrep`/`Phylotree`) or pairwise comparison methods: [Moderately Supported].**  
  While avoiding dependence on a pre-existing haplogroup database allows the workflow to be applied to non-human or poorly cataloged non-recombining genomes, the claim of broad superiority over pairwise comparison methods (e.g., Li and Stoneking) is not backed by runtime benchmarks, scaling curves, or accuracy comparisons. Moreover, constructing a single chimeric sequence (`_MINOR`) assumes a single contaminating donor and non-recombining clonal inheritance; if two distinct wells contaminate a sample or if a sample harbors 1–3 high-frequency endogenous heteroplasmies alongside low-level carryover, the resulting synthetic sequence is a phylogenetic mosaic that can experience branch attraction toward basal nodes rather than the true donor.

* **Suspicious samples can be reliably identified using a threshold of $\ge 10$ polymorphic sites with $\text{MAF} \ge 2\%$ and visual inspection of MAF variation: [Fragile].**  
  The $\ge 10$ heteroplasmic site cutoff works only when the contaminating and recipient mtDNA genomes belong to sufficiently divergent haplogroups (differing at $\ge 10$ fixed positions) and when the contamination level exceeds the $2\%$ MAF cutoff across all diverging sites. Between closely related maternal lineages or intra-haplogroup samples differing at only 2–6 sites, cross-contamination at $2\%\text{--}5\%$ will fall into the "gray zone" (acknowledged briefly in Supplementary Figure S1) and evade the $\ge 10$ count filter. The authors explicitly decline to provide a formal summary test statistic for MAF dispersion ("we feel that a single summarizing statistic would be misleading and prefer a visual approach"), leaving users without calibrated type I/II error rates.

* **Alternating pUC18 and $\phi$X174 DNA spike-ins prior to barcoded library preparation reliably detects pre-sequencing cross-contamination: [Overstated].**  
  Although alternating orthogonal spike-ins (spike-in 1, spike-in 2, no spike-in) in a striped plate layout is a sound experimental design principle, the manuscript presents zero experimental data, read counts, or pre-sequencing PCR/qPCR sensitivity assays demonstrating this protocol in practice. Note also that $\phi$X174 is routinely added by Illumina sequencing facilities as an unindexed control library during clustering, which could confound post-sequencing read mapping against $\phi$X174 if unindexed reads or index-hopping events are not strictly filtered out.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Formulate a Quantitative Statistical Test for MAF Clustering and Benchmark via In Silico Mixtures
* **WHY:** Relying on a fixed heuristic threshold of $\ge 10$ heteroplasmic sites and visual inspection of boxplots fails when contaminating and recipient samples share the same haplogroup (fewer than 10 fixed differences) or when contamination is near the $2\%$ boundary where binomial read-sampling noise truncates half of the donor variants.
* **WHAT:** Supplement the visual `MAF Boxplot` tool with a formal likelihood-ratio or dispersion test comparing a single-proportion binomial mixture model (carryover from a uniform donor fraction $p_c$) against an overdispersed Beta-Binomial null model of endogenous heteroplasmy, and benchmark sensitivity/specificity across simulated mixtures.
* **HOW:** Using the major-allele consensus sequences of the 56 empirical samples, generate in silico read mixtures across all $\binom{56}{2} = 1,540$ pairs at contamination fractions $c \in \{0.01, 0.02, 0.03, 0.05, 0.10\}$ and read depths $D \in \{500, 2000, 5000\}$. Report the True Positive Rate and False Positive Rate of the `Variant Annotator` + `Phylorelatives` pipeline as a function of pairwise nucleotide distance $d_{ij}$ and contamination fraction $c$.

#### 2. Deconvolve Endogenous Heteroplasmies from Donor Carryover in `Get FASTA from Variants Table`
* **WHY:** Replacing all sites with $\text{MAF} \ge 2\%$ by their minor allele conflates pre-existing high-frequency endogenous heteroplasmies (e.g., $\text{MAF} = 35\%$) with low-level plate carryover (e.g., $\text{MAF} = 2.5\%$), creating a chimeric sequence in `Phylorelatives`.
* **WHAT:** Filter the sites substituted into the `_MINOR` FASTA sequence by restricting to variants within a bounded MAF window around the sample's median minor allele frequency ($\text{median}(\text{MAF}) \pm 2 \times \text{MAD}$).
* **HOW:** Add an optional `--maf-band` or `--mad-filter` argument to `Get FASTA from Variants Table` so that outlier endogenous heteroplasmies (whose allele frequencies lie more than $3\text{ MAD}$ away from the contamination cluster) remain masked as `N` rather than distorting the NJ distance matrix.

#### 3. Address $\phi$X174 Control Library Confounding and Provide Empirical Spike-In Validation
* **WHY:** The manuscript recommends $\phi$X174 and pUC18 as barcoded sample spike-ins without providing validation data, and overlooks the standard use of $\phi$X174 by Illumina platforms as a spike-in control during sequencing runs, which can introduce background $\phi$X174 reads via index hopping or imperfectly demultiplexed reads.
* **WHAT:** Document empirical read counts or qPCR detection limits for the pUC18/$\phi$X174 striped plate protocol if available, or explicitly frame the spike-in section as a prospective protocol recommendation while addressing Illumina $\phi$X174 control interference.
* **HOW:** Either include a supplementary table of mapped pUC18 and $\phi$X174 read fractions across a test plate, or revise lines 120–129 to warn users to verify whether their sequencing provider spikes in $\phi$X174 at the flowcell level and to substitute an alternative non-homologous plasmid if $\phi$X174 is used by the core facility.

#### 4. Clarify Complete vs. Pairwise Deletion Behavior in `Phylorelatives`
* **WHY:** In the `Get FASTA from Variants Table` tool (lines 87–89), positions not present in the variants table remain `N`. Yet in `Phylorelatives` (line 94), "Sites with missing information are excluded by default (complete deletion)." If non-variant sites are encoded as `N` rather than the reference/major allele, complete deletion would drop nearly the entire 16,569 bp alignment.
* **WHAT:** Clarify whether `Variant Annotator` outputs all 16,569 covered positions (including invariant major-allele sites with $\text{MAF} = 0$) to `Get FASTA from Variants Table`, and specify how low-coverage (`N`) sites in a single sample affect complete-deletion NJ tree reconstruction across all 56 samples.
* **HOW:** Explicitly state in the `Variant Annotator` and `Get FASTA from Variants Table` sections that all covered reference positions pass into the major/minor allele table, and recommend `pairwise.deletion = TRUE` in `ape::dist.dna` as the default so that a single low-coverage region in one sample does not censor informative sites across the remaining samples.
