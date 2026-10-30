# Review of AN_ANON_042

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.9 / 8.0**  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript reports the construction, indexing, and evolutionary application of the UCSC 28-way vertebrate whole-genome alignment referenced to the human genome (NCBI Build 36 / hg18), expanding the prior 17-way track by adding 11 new species and updating six assemblies. The dataset integrates two finished genomes (human, mouse), 16 higher-coverage draft shotgun assemblies (5.1$\times$–8.5$\times$), and 10 low-coverage (~2$\times$) mammalian assemblies using pairwise BLASTZ alignments, `axtChain`/`axtNet` chaining and netting (with syntenic filtering for high-coverage mammals and reciprocal-best filtering for 2$\times$ mammals), progressive multiple alignment via MULTIZ along an assumed 28-species tree, and phylogenetic hidden Markov model (phylo-HMM) conservation scoring via `phastCons` (`phyloFit` REV model on fourfold degenerate [4D] sites from Gencode). To support scalable querying, the authors introduce an LZO-compressed chunk indexing scheme and Python toolkit (`bx-python`) for semi-random access to Multiple Alignment Format (MAF) blocks and gap-aware alignability calculation (`maf_interval_alignability.py`). The utility of the resource is demonstrated through three comparative genomic investigations: (1) coding insertions and deletions (indels), identifying 209 unambiguous indels along the human placental lineage, 11 human-specific coding indels (*SULF1*, *GFM2*), and a permutation test of conservation at *PAH* deletion sites; (2) differential evolutionary drift of start versus stop codons across 11,729 reviewed RefSeq genes; and (3) the phylogenetic decay of alignability across 251,000 coding exons, 481 ultraconserved elements (UCEs), 92,269 predicted regulatory regions (PRPs), and 3,900 ENCODE ChIP-chip putative transcriptional regulatory regions (pTRRs).

The primary deliverable—the 28-way vertebrate alignment, `phastCons` conservation tracks, and `bx-python` LZO-indexed MAF processing suite—is a rigorously engineered, foundational community resource accompanied by open data, open source code, and remarkably candid discussion of methodological limitations (including `phastCons` gap handling, tree topology dependence, and human polymorphism in *GFM2*). Within the three illustrative biological applications, several methodological caveats warrant attention: the parametric bootstrap test claiming a slowdown in coding indel accumulation along the human lineage ($P < 10^{-3}$, from ~4 to <2 indels/Myr) is vulnerable to taxon-sampling and coverage-dropout ascertainment bias across internal branches; the start/stop codon drift comparisons rely on univariate two-proportion tests rather than a joint multivariable model controlling for coverage depth and GC/CpG content; and the alignability lag phase observed for PRPs and UCEs relative to biochemically defined ENCODE pTRRs is partially circular because PRPs and UCEs were originally ascertained using mammalian sequence conservation. None of these secondary analytical caveats detract from the high value of the primary alignment resource.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The 28-way BLASTZ/axtChain/axtNet/MULTIZ alignment and `phastCons` conservation resource captures >79% of human protein-coding intervals even in distant vertebrates and 2$\times$ draft mammals: [Well Supported].**  
  Table 1 and the Methods document a carefully tuned pipeline that adapts chaining matrices and filtering stringency (syntenic vs. reciprocal-best) to assembly quality, while `maf_interval_alignability.py` explicitly distinguishes true unaligned sequence (contiguous gap annotation in both species) from missing draft sequence data.

* **Biochemically identified regulatory regions (ENCODE ChIP-chip pTRRs) undergo rapid evolutionary turnover outside eutherian mammals (~70% conserved within eutherians vs. ~30% outside), decaying exponentially like neutral background DNA but with a rightward constraint shift: [Well Supported].**  
  Because ENCODE pTRRs (and CTCF binding sites) were identified experimentally without reference to sequence conservation, their alignability decay curve (Figure 7B–C) and low column-level similarity scores (Figure 7A) provide an unbiased demonstration that functional cis-regulatory occupancy tolerates substantial sequence and indel turnover compared to coding exons.

* **Apparent accelerated drift of human start codons relative to stop codons in non-mouse assemblies is substantially driven by sequencing dropout in CpG islands and alignment failure in short (<100 bp) initial coding exons: [Well Supported].**  
  The observation that finished mouse shows slightly higher start than stop alignability (97.7% vs. 96.8%, Table 1), combined with the stratification in Table 3 showing no significant start/stop disparity within placental mammals for non-CpG genes ($P = 0.16$) and a major recovery of start alignability in exons $\ge 100$ bp ($P < 10^{-3}$), convincingly separates technical draft-assembly and local-alignment boundary artifacts from pure evolutionary drift.

* **Predicted regulatory regions (PRPs) and ultraconserved elements (UCEs) experience distinct evolutionary periods of stringent selection across eutherians and amniotes before decaying: [Moderately Supported].**  
  While the fitted decay curves (Figure 7C) accurately describe the empirical alignment data, interpreting the flat eutherian plateau of PRPs and amniote plateau of UCEs as biological regimes of stringent selection is partially circular: PRPs were constructed by intersecting PReMods with intervals required to maintain high Regulatory Potential (`RP >= 0.05` over $\ge 200$ bp) across a 7-way eutherian alignment (human, chimp, macaque, mouse, rat, dog, cow), and UCEs were defined by 100% identity across human, mouse, and rat. Their near-100% alignability within eutherians is guaranteed by their selection criteria.

* **Coding indels accumulated at a significantly higher rate in early placental evolution (~4 per Myr) than on recent branches leading to human (<2 per Myr; parametric bootstrap $P < 10^{-3}$): [Fragile].**  
  To be counted among the 209 indels in Figure 3, an indel had to be unambiguously assigned to a sampled human-lineage branch with strict agreement across the 16 other placental mammals (matching human or elephant/opossum) and meet flanking coding sequence requirements. Because 10 of those 16 comparative mammals are ~2$\times$ shotgun assemblies with high missing-data rates, and because branch lengths and divergence times (taken as fixed point estimates without fossil calibration uncertainty) vary in sister-clade sampling density, differential missing-data dropout, reciprocal-best filtering losses, and incomplete lineage sorting across deep versus shallow nodes confound the inferred per-Myr branch rates. Furthermore, the 11 "human-specific" indels on the terminal branch include unsegregated human polymorphisms (e.g., *GFM2*), which inflate terminal rates when unmasked or distort comparisons depending on reference allele ascertainment.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Control for Missing-Data Ascertainment and Divergence Time Uncertainty in the Coding Indel Rate Test
* **WHY:** Requiring unambiguous branch assignment across 16 comparative placental mammals—10 of which have ~2$\times$ coverage—introduces branch-specific ascertainment bias (deep branches with multiple descendant species vs. shallow primate branches with single draft assemblies) and treats disputed molecular clock branch durations as exact constants.
* **WHAT:** Re-evaluate the uniform-rate hypothesis on a restricted sub-alignment of high-coverage (finished and 5$\times$–8.5$\times$) genomes using a probabilistic indel model that marginalizes over missing data and branch-length uncertainty.
* **HOW:** Re-run the indel branch assignment using only the finished and high-coverage eutherian assemblies (human, chimp, macaque, mouse, rat, dog, cow, horse) with explicit missing-data masking, exclude polymorphic human indels by cross-referencing dbSNP/EST traces (as done manually for *GFM2*), and repeat the parametric bootstrap across a range of plausible fossil-calibrated branch durations.

#### 2. Decouple Ascertainment Circularity When Comparing PRP and pTRR Alignability Decay
* **WHY:** PRPs were selected based on high Regulatory Potential scores across 7 eutherian mammals, making their ~100% alignability across those same eutherian lineages in Figure 7B–C an artifact of ascertainment rather than an independent test of evolutionary retention.
* **WHAT:** Evaluate PRP alignability exclusively on out-of-sample species not used in the 7-way RP or PReMod discovery set, or define a human-only/primate-only regulatory prediction set for symmetric comparison against ENCODE pTRRs.
* **HOW:** In Figure 7C and Supplemental Table S4, fit the exponential decay model for PRPs using only species excluded from the 7-way RP training alignment (e.g., horse, cat/shrew/hedgehog/tenrec/armadillo/elephant, opossum, platypus, chicken, lizard, frog, and fish), and explicitly annotate the 7 training species on the plot.

#### 3. Fit a Joint Multivariable Model for Start vs. Stop Codon Alignability
* **WHY:** Table 3 evaluates CpG island overlap, initial coding exon length (<100 bp vs. $\ge 100$ bp), and alternative promoters via separate marginal stratifications, leaving their collinearity (e.g., CpG island promoters frequently co-occurring with short 5' exons) and interaction with sequencing coverage depth unquantified.
* **WHAT:** Quantify the independent contribution of exon length, CpG island overlap, alternative promoter status, and assembly coverage tier to the difference between start and stop codon alignability.
* **HOW:** Using the 11,729 RefSeq genes across the 27 target species, fit a logistic regression (or generalized linear mixed model with gene and species random effects) predicting `I(Start Aligns) - I(Stop Aligns)` as a function of `log(Exon_Length)`, `CpG_Overlap`, `Alt_Promoter`, `4D_Distance`, and `Coverage_Tier` (Finished vs. 5–8$\times$ vs. 2$\times$).
