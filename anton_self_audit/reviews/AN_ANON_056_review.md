# Review of AN_ANON_056

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.9 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces `Galaxy2 ENCODE`, a web-based data portal and interactive analysis workspace built for the ENCODE Consortium that integrates >100 tools for genomic interval operations, multiple sequence alignment manipulation (`MAF-to-FASTA`), and molecular evolutionary inference (`[SOFTWARE_PACKAGE]`) with a persistent user history system and 19 instructional QuickTime screencasts. To illustrate the platform's capabilities, the authors present two "cookbook" analyses on ENCODE regions: (1) an annotation screen of 9,191 Non-GENCODE expressed sequence tags (ESTs; 27,202 exons) classified as intronic, intergenic, or intertwined, evaluating their coding potential via `Exoniphy`, sequence conservation via `phastCons`, and transcriptional corroboration via overlap with Affymetrix `transfrags`; and (2) a maximum-likelihood estimation of mammalian neutral substitution rates across 364 kb of autosomal ancestral repeats (ARs) in human, chimpanzee, mouse, rat, and dog using a general time-reversible (`REV`) model. The software distribution, source code, and screencasts are publicly available online.

As an integrative bioinformatics platform, `Galaxy2 ENCODE` delivers a clean, extensible architecture that removes file-parsing barriers between genomic interval algebra, whole-genome alignments, and maximum-likelihood phylogenetic software. The second vignette (ancestral repeat substitution rates with profile-likelihood confidence intervals) is methodologically sound and reproduces genome-wide mammalian neutral divergence benchmarks in seven minutes. However, the first illustrative vignette (Non-GENCODE ESTs) contains three methodological and numerical flaws: (1) an asymmetric, circularly constrained `Random Intervals` control in Experiment B (generating random intervals matching the size of EST exons rather than `transfrags`, explicitly excluding `transfrag` regions, and intersecting them back against EST exons in a single un-replicated run); (2) an arithmetic contradiction in line 91 where the three exhaustive subcategories of conserved Non-GENCODE ESTs (`942 intronic + 221 intergenic + 9 intertwined = 1,172`) fail to sum to the stated total of `2,180` ESTs; and (3) overstating a moderate `phastCons` $\ge 0.2$ cutoff across predominantly intronic ESTs as evidence of independent transcripts under "strong purifying selection." Correcting the random-interval null comparison, reconciling the EST counts, and tempering the functional claims can be accomplished directly within the existing platform.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`Galaxy2 ENCODE` streamlines complex multi-step genomic interval, alignment, and evolutionary analyses into reproducible web histories with minimal developer overhead for adding CLI tools: [Well Supported].**  
  The software architecture, automated ENCODE file partitioning and naming portal, set-algebra interval operations (union, intersection, subtraction, complement, proximity, and coverage), and two-step CLI wrapper integration are clearly documented and backed by 19 step-by-step screencasts and open-source code.

* **Nucleotide substitution rates in ENCODE autosomal ancestral repeats (364 kb across five mammals) match genome-wide neutral divergence estimates: [Well Supported].**  
  Applying the `REV` substitution model in `[SOFTWARE_PACKAGE]` yields branch lengths (`human: 0.006`, `chimp: 0.007`, `mouse: 0.084`, `rat: 0.112`, `dog: 0.231`) with profile-likelihood 95% confidence intervals (Table 3) that closely match published genome-wide mammalian consortia estimates.

* **Only one Non-GENCODE EST (`DR731323`) overlaps $\ge 75\%$ with `Exoniphy` ab initio protein-coding exon predictions, whereas >2,000 Non-GENCODE ESTs are under "strong purifying selection" and likely represent functional non-coding transcripts: [Overstated].**  
  While the `Exoniphy` screen showing negligible missing protein-coding genes (`DR731323`, a 3' extension of `ENST00000355799`) is convincing, claiming in the Abstract and Results that 2,180 unannotated ESTs are under *"strong purifying selection that are likely functional"* based on a mean exon `phastCons` threshold of $\ge 0.2$ is overstated. First, `phastCons` is a posterior probability ($0 \le P \le 1$) of belonging to the conserved phylo-HMM state, so a mean score of $0.2$ is a permissive filter rather than evidence of strong purifying selection. Second, the vast majority of the reported ESTs (`942` of the `1,172` itemized in line 91, or 80.4%) are **intronic**; single-pass intronic ESTs frequently represent unspliced pre-mRNA introns or genomic contamination within known GENCODE host genes that happen to overlap conserved intronic cis-regulatory elements, rather than independent functional non-coding RNAs. Third, the subcategory counts in line 91 (`942 intronic + 221 intergenic + 9 intertwined = 1,172`) contradict the reported total of `2,180` ESTs by 1,008 transcripts.

* **Comparing Experiment A and Experiment B demonstrates statistically non-random overlap between Non-GENCODE EST exons and Affymetrix `transfrags`: [Methodologically Flawed].**  
  In line 93, Experiment A intersects `Non-GENCODE EST exons` ($E$) with `Affymetrix transfrags` ($T$). For the null control (Experiment B), instead of generating random intervals $R_T$ matching the chromosome and length distribution of `transfrags` ($T$) across the ENCODE regions and computing $|E \cap R_T|$, the authors generated random intervals $R_E$ that *"mimic the length distribution of Non-GENCODE EST exons but lie outside transfrags"* and computed $|E \cap R_E|$. This test is invalid for two reasons: (1) total base coverage of $R_E$ equals the footprint of EST exons ($|E|$) rather than the footprint of `transfrags` ($|T|$), making the expected intersection $|E \cap R_E|$ incommensurable with $|E \cap T|$; and (2) restricting $R_E$ to *lie outside transfrags* ($R_E \subset \text{ENCODE} \setminus T$) while testing overlap with $E$ (which overlaps $T$) circularly depletes $|E \cap R_E|$ by forbidding random intervals from landing in $T$. Moreover, Experiment B was executed only once without computing an empirical null distribution or $p$-value.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Redesign the `Random Intervals` Permutation Control (Experiment B) for EST–Transfrag Overlap
* **WHY:** Intersecting `Non-GENCODE EST exons` ($E$) with random intervals mimicking $E$ that are explicitly excluded from `transfrags` ($T$) creates a circular, footprint-mismatched comparison that artificially suppresses the null overlap in Table 2.
* **WHAT:** Perform a symmetric Monte Carlo permutation test (e.g., $N = 1,000$ replicates) that preserves interval lengths and total base coverage across the ENCODE regions without excluding $T$.
* **HOW:** Using the `Random Intervals` tool in `Galaxy2 ENCODE`:
  1. Generate $N = 1,000$ independent random interval sets $R_E^{(1)}, \dots, R_E^{(1000)}$ within the ENCODE regions (optionally masked only for assembly gaps/GENCODE exons, **not** masked for `transfrags`) matching the exact chromosome and length distribution of `Non-GENCODE EST exons`.
  2. Intersect each random set $R_E^{(i)}$ with the **actual Affymetrix `transfrags` ($T$)** to obtain the null distribution of base-pair overlap $|R_E^{(i)} \cap T|$.
  3. Report the mean, standard deviation, fold-enrichment, and empirical $p$-value of the observed overlap $|E \cap T|$ (Experiment A) relative to $\left\{|R_E^{(i)} \cap T|\right\}_{i=1}^{1000}$ in Table 2.

#### 2. Reconcile the Arithmetic Discrepancy in Conserved Non-GENCODE EST Counts (2,180 vs. 1,172)
* **WHY:** Line 77 defines three exhaustive categories of Non-GENCODE ESTs (intronic, intergenic, and intertwined), but line 91 states: *"we identified 2180 such ESTs (942 intronic, 221 intergenic, and nine intertwined, respectively)"*, leaving $2,180 - (942 + 221 + 9) = 1,008$ ESTs unaccounted for.
* **WHAT:** Check the relational join/filtering history in Screencast 16/17 to determine whether `2,180` is the number of *exons* (or single-exon + multi-exon ESTs before category splitting) or whether one of the subcategory numbers (`942`, `221`, `9`) was mis-transcribed.
* **HOW:** Update line 91 and the Abstract/Introduction so that the total number of conserved Non-GENCODE ESTs equals the exact sum of its intronic, intergenic, and intertwined components.

#### 3. Temper the "Strong Purifying Selection" Framing and Distinguish Intronic Pre-mRNA Fragments from Intergenic Transcripts
* **WHY:** A mean `phastCons` score $\ge 0.2$ indicates moderate evolutionary conservation rather than strong purifying selection, and intronic ESTs (which make up ~80% of the itemized conserved set) can reflect unspliced pre-mRNA introns overlapping conserved intronic enhancers rather than independent non-coding transcripts.
* **WHAT:** Revise the Abstract, Introduction, and line 91 to describe these regions as *"evolutionarily conserved unannotated transcripts (`phastCons` $\ge 0.2$)"* rather than *"under strong purifying selection"*, and discuss intronic vs. intergenic ESTs separately.
* **HOW:** Report the `phastCons` distribution and splice-site support (spliced vs. unspliced ESTs) separately for the 221 intergenic ESTs and 942 intronic ESTs.
