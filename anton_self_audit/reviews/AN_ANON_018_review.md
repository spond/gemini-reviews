# Review of AN_ANON_018

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This correspondence introduces Trackster, a web-based interactive visual analysis environment integrated into an open genomic workflow platform. Rather than treating visualization as a static post-hoc step after genome-wide computation, Trackster runs integrated bioinformatics tools (such as Cufflinks, interval operations, and variant callers) on user-selected genomic regions (subsets), reducing execution time from hours to ~1–2 minutes and enabling interactive parameter-space sweeps and real-time dynamic attribute filtering. To demonstrate Trackster, the authors analyze the unconventional 26-bp IRE1-mediated cytoplasmic splicing of human *XBP1* (*XBP1u* vs. *XBP1s* isoforms) across 16 human tissues from the Illumina BodyMap 2.0 RNA-seq dataset (~160 million reads per tissue) and visualize ribosome-profiling footprints from cytosolic and endoplasmic reticulum (ER) fractions of HEK cells, confirming ER-specific translational pausing on *XBP1u*.

Coupling local-region parameter sweeps and dynamic visual filtering directly to a full workflow execution engine is a practical and well-implemented contribution to interactive genomics, and the complete workflows, histories, and live visualizations are openly shared online. However, the manuscript's methodological presentation of the *XBP1* case study has two notable limitations: (1) while the text emphasizes how difficult it was to tune Cufflinks parameters to resolve the 26-bp non-canonical *XBP1* intron and remove assembly artifacts, it never reports what the optimal Cufflinks parameter values or dynamic filtering thresholds actually were, nor does it evaluate whether local parameter tuning on a single gene (*XBP1*) degrades transcript assembly accuracy across the rest of the genome when applied globally; and (2) the relative expression levels of *XBP1s* and *XBP1u* across the 16 BodyMap tissues (the second biological question posed on line 39) are never summarized in the main text. Reporting the tuned parameters, evaluating local-to-global generalization, and summarizing the biological findings in the text would make the paper substantially more complete.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Running tools on genomic region subsets in Trackster reduces transcript assembly runtime from 3–8 hours (genome-wide) to 1–2 minutes (locus-level), enabling interactive parameter exploration: [Well Supported].**  
  Because local interval operations and locus-restricted Cufflinks runs scale with the number of reads overlapping the viewed window (a few kilobases at the *XBP1* locus vs. 3 Gb genome-wide), the ~100-fold reduction in iteration time and real-time browser-side attribute filtering (FPKM and Score) follow directly from the subsetting architecture and are demonstrated in Figures 1 and 2.

* **Parameter tuning of Cufflinks on the *XBP1* locus successfully resolves the non-canonical 26-bp IRE1-cleaved intron and quantifies *XBP1s*/*XBP1u* across 16 human tissues: [Moderately Supported].**  
  Figure 1 illustrates that default Cufflinks parameters fail to separate the 26-bp splice variant and that parameter-tree exploration recovers the *XBP1s* and *XBP1u* structures. However, the main text never specifies which Cufflinks parameters were modified (e.g., `--min-intron-length`, which defaults to 50 bp in TopHat/Cufflinks and therefore automatically filters out a 26-bp intron unless lowered, `--pre-mrna-fraction`, or `--small-anchor-fraction`), nor does the text check whether the upstream read mapper (TopHat/bowtie) was even configured to allow 26-bp splice junctions during initial alignment. Furthermore, the answer to the second biological question ("what are the relative amounts of XBP1s and XBP1u mRNAs in various tissues", line 39) is omitted from the main text and deferred entirely to Supplementary Table 1.

* **Parameter settings optimized visually on a single locus (*XBP1*) can be applied to run the tool on the complete genome-wide dataset: [Fragile].**  
  In lines 35, 41, and 46, the authors advocate using Trackster to visually tune parameters on a target region (*XBP1*) and then clicking a button to run those chosen settings across the complete genome-wide dataset. However, *XBP1* is explicitly chosen because its 26-bp non-canonical IRE1 spacer is an extreme biological outlier (standard human spliceosomal introns are >50–70 bp). Lowering minimum intron length or isoform fraction thresholds globally across all 16 tissues to accommodate a 26-bp cytoplasmic cleavage event in *XBP1* risks inflating false-positive micro-intron calls and fragmented transcript artifacts across the rest of the human transcriptome. No genome-wide precision/sensitivity check (e.g., against GENCODE/RefSeq annotations) is performed to test this trade-off.

* **Ribosome footprinting visualization in Trackster confirms ER-specific translational pausing of *XBP1u* mRNA: [Well Supported].**  
  Mapping the Reid and Nicchitta ribosome profiling data (reference 18) to the assembled *XBP1u* transcript (line 57, Fig. S1) reproduces the known pileup of ribosome footprints at the translational pause site specifically in the ER-associated fraction and not the cytosolic fraction.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Explicitly Report the Tuned Cufflinks/Mapper Parameters and Dynamic Filter Thresholds
* **WHY:** The central narrative of the *XBP1* case study (lines 39–53) is that default RNA-seq parameters miss the 26-bp *XBP1* intron and produce assembly artifacts, yet the text never tells the reader which parameters were swept, what their default vs. optimal values were, or how TopHat mapped reads across a 26-bp junction.
* **WHAT:** State the exact TopHat/Cufflinks parameter names, default values, sweep ranges, and final selected values in the main text (lines 41–48), along with the exact FPKM and Score cutoffs chosen in Figure 2C.
* **HOW:** Extract the parameter settings from the shared workflow (`http://[WORKFLOW_PLATFORM]/interactive-rnaseq`) and add 2–3 sentences detailing them (e.g., minimum intron length, isoform fraction, pre-mRNA fraction, and FPKM/Score cutoffs), as well as a 1–2 sentence summary of which of the 16 BodyMap tissues exhibited the highest *XBP1s*/*XBP1u* ratios from Supplementary Table 1.

#### 2. Evaluate the Genome-Wide Trade-Off of Locus-Tuned Parameters
* **WHY:** Visual parameter tuning on an atypical locus (*XBP1* with a 26-bp non-spliceosomal intron) can overfit to local peculiarities and degrade global assembly quality when applied genome-wide.
* **WHAT:** Compare the genome-wide Cufflinks assembly under default parameters versus the *XBP1*-tuned parameters across the whole human transcriptome.
* **HOW:** Using `cuffcompare` against reference gene annotations (e.g., Ensembl/RefSeq hg19) on one representative BodyMap tissue, report the genome-wide exon/intron sensitivity and false-discovery rate before and after applying the *XBP1*-tuned settings and the Figure 2C dynamic filters.

#### 3. Editorial and Typographical Cleanup
* **WHY:** The manuscript contains several duplicated words and spelling errors that detract from presentation quality.
* **WHAT & HOW:** Fix the following exact text errors:
  1. Line 27: "making it easy to **use use** visual inspection" $\to$ "making it easy to **use** visual inspection".
  2. Line 53 (Figure 2 caption): "Using Trackster to dynamically **filtering** transcript assemblies" $\to$ "Using Trackster to dynamically **filter** transcript assemblies"; "**inteval** dataset" $\to$ "**interval** dataset"; "filtering **simutaneously**" $\to$ "filtering **simultaneously**".
  3. Line 55: "and **filtering filtering** genome wide" $\to$ "and **filtering** genome-wide".
  4. Line 57: "Reid and **Niccitta** 18" $\to$ "Reid and **Nicchitta** 18".
  5. Line 59: "and **Tracker** visualizations used" $\to$ "and **Trackster** visualizations used".
  6. Line 61: "makes use of it when **it available**" $\to$ "makes use of it when **it is available**".
