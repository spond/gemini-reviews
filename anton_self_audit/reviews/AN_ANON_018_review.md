# Review of AN_ANON_018

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.7 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.0 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 1.9/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This Letter to the Editor introduces Trackster, a web-based interactive visual analysis environment integrated directly into the Galaxy platform that tightly couples genome browser visualization with parameter space exploration and dynamic filtering of next-generation sequencing (NGS) tools. Rather than running computationally expensive tools across an entire genome (which requires hours) and only inspecting static outputs afterward, Trackster executes integrated Galaxy tools on user-selected genomic regions (reducing runtime to seconds or minutes), renders outputs immediately in parallel tracks, supports systematic parameter-tree sweeps, and offers real-time dynamic attribute filtering (`Score`, `FPKM`) before launching the finalized configuration on the complete dataset. The authors demonstrate Trackster through an investigation of the human *XBP1* locus across 16 human tissues from the Illumina BodyMap 2.0 RNA-seq dataset (~160 million reads per tissue, mapped to `hg19`) and ribosome profiling data from cytosolic and endoplasmic reticulum (ER) fractions of HEK cells (Reid and Nicchitta, reference 18). Using Trackster's localized parameter sweeps on the *XBP1* region, they tune `Cufflinks` to resolve the non-canonical 26-bp IRE1-cleaved cytoplasmic intron distinguishing unspliced (*XBP1u*) and spliced (*XBP1s*) transcripts across tissues (Figures 1–2; Supplementary Table 1), and visualize ER-specific translational pausing on *XBP1u* mRNA via ribosome footprint pileups (Figure S1).

The manuscript presents an elegant, well-engineered paradigm for interactive genomic computing ("subset-tune-scale") and validates it on a biologically challenging, non-canonical splicing and translational pausing locus (*XBP1*), complete with shared live Galaxy visualizations and workflows (`http://[WORKFLOW_PLATFORM]/interactive-rnaseq`). The primary methodological limitation is that tuning tool parameters visually on a single target locus (*XBP1*) to match a known ground-truth isoform structure and then applying those locus-tuned parameters genome-wide across all 16 tissues risks severe local overfitting: `Cufflinks` parameters forced to accept a 26-bp non-canonical intron (well below normal spliceosome minimum intron lengths of ~50–70 bp) will likely generate numerous false-positive micro-intron splits across the rest of the transcriptome. Furthermore, while the *XBP1* biological questions (relative tissue abundance of *XBP1s* vs. *XBP1u* and ER ribosome pausing coordinates) are posed as core aims in line 39, the actual biological findings are summarized only qualitatively in the text without reporting tissue-level *XBP1s*/*XBP1u* ratios or exact pausing coordinates. Addressing local-to-global parameter overfitting and reporting the quantitative *XBP1* results in the main text would significantly strengthen the paper.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Claim 1: Running genomic analysis tools on localized genomic subsets inside Trackster reduces parameter exploration runtime from hours/days to 1–2 minutes while supporting systematic parameter-tree sweeps and dynamic visual filtering: [Well Supported].**  
  The architectural integration of Trackster with Galaxy's tool wrapper framework (lines 33–35, 55, Figures 1–2) convincingly demonstrates that region-restricted execution of `Cufflinks` takes ~1–2 minutes per setting compared to ~3–8 hours genome-wide, and that dynamic client-side filtering on `FPKM` and `Score` operates in real time vs. 10–20 minutes for batch genome-wide filtering. The authors also thoughtfully discuss the exact algorithmic boundary conditions where localized subset execution breaks down—specifically tools that estimate global background models (e.g., peak callers or `Cufflinks` global fragment length/abundance models) or read mappers requiring whole-genome indexes—and explain how cached global models or relaxed-parameter dynamic filtering address those cases (line 61).

* **Claim 2: Parameter space exploration in Trackster identifies `Cufflinks` settings that successfully assemble the non-canonical 26-bp IRE1-spliced *XBP1s* and unspliced *XBP1u* isoforms across the 16 BodyMap 2.0 human tissues: [Moderately Supported].**  
  Figure 1 visually confirms that default `Cufflinks` settings (track `d`) fail to resolve the dual *XBP1u*/*XBP1s* isoform structure at the *XBP1* locus, whereas sweeping `Cufflinks` parameters on the *XBP1* region (tracks `e`–`g` and bottom parameter tree `i`–`iii`) recovers both isoforms. However, the manuscript never states in the main text *which* specific `Cufflinks` parameters and numerical values (e.g., `--min-intron-length`, `--pre-mrna-fraction`, `--small-anchor-fraction`, `--min-isoform-fraction`) were required to detect the 26-bp spacer, nor does it report the actual quantitative tissue expression ratios of *XBP1s* to *XBP1u* across the 16 BodyMap tissues (which was explicitly posed as Question 2 on line 39, but deferred entirely to Supplementary Table 1).

* **Claim 3: Applying locus-tuned `Cufflinks` parameters (optimized visually on *XBP1*) to assemble transcripts across the complete genome dataset produces improved genome-wide assemblies: [Fragile].**  
  In lines 35, 41, and 46, the authors describe the workflow as finding "good parameter settings" via visual inspection on a target region (*XBP1*) and then clicking a button to *"run the tool with the chosen settings on the complete dataset."* Biologically, the 26-bp *XBP1* intron is excised in the cytosol by the endoribonuclease IRE1 rather than the nuclear spliceosome, which almost never splices introns shorter than ~50 bp in mammals. Lowering `Cufflinks`'s minimum intron length threshold to $\le 26$ bp to force assembly of *XBP1s* will cause `Cufflinks` to interpret short alignment gaps, indels, or mapping artifacts across the rest of the human genome as spurious micro-introns. Visual tuning on an atypical locus without evaluating global precision/recall against a reference annotation (`GENCODE`/`RefSeq`) risks degrading genome-wide assembly quality.

* **Claim 4: Mapping ribosome profiling reads from HEK cytosolic and ER fractions to the assembled *XBP1u* transcript in Trackster confirms ER-specific translational pausing: [Well Supported].**  
  Using the ribosome footprinting dataset of Reid and Nicchitta (reference 18), the custom *XBP1u* transcript browser in Trackster (line 57, Figure S1) confirms a localized pileup of ribosome footprints at the translational pausing site specifically in the ER-associated fraction and absent from the cytosolic fraction, consistent with known *XBP1u* nascent-peptide arrest mechanism.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report the Exact `Cufflinks` Parameters and Quantitative *XBP1s* / *XBP1u* Tissue Ratios in the Main Text
* **WHY:** Line 39 poses three explicit biological questions: (1) whether RNA-seq tools can detect the 26-bp non-canonical intron, (2) what the relative amounts of *XBP1s* and *XBP1u* mRNAs are across the 16 human tissues, and (3) what can be learned about *XBP1u* translational pausing. Yet the main text never states the parameter values that solved Question 1 or the tissue expression numbers that answered Question 2.
* **WHAT:** Add the exact `Cufflinks` parameter names and values discovered via Trackster and summarize the quantitative *XBP1s*/*XBP1u* FPKM ratios across the 16 BodyMap tissues directly in the text (lines 41–48).
* **HOW:** Specify which `Cufflinks` flags (e.g., `--min-intron-length 20`, `--min-isoform-fraction`, `--junc-alpha`) enabled detection of the 26-bp IRE1 cleavage site in Figure 1, and include 2–3 sentences summarizing which of the 16 BodyMap tissues exhibited the highest and lowest *XBP1s*:*XBP1u* ratios from Supplementary Table 1 (e.g., secretory tissues such as liver, thyroid, or leukocyte/lymph node vs. skeletal muscle or brain).

#### 2. Quantify the Genome-Wide Tradeoff of Applying *XBP1*-Tuned Parameters to the Full Transcriptome
* **WHY:** *XBP1* is a famous biological outlier (a 26-bp cytoplasmic IRE1-cleaved intron). Optimizing `Cufflinks` parameters on an outlier locus and running those settings genome-wide (line 41) risks inflating false-positive micro-introns and fragmented transcripts across canonical spliceosomal genes.
* **WHAT:** Evaluate genome-wide transcript assembly accuracy under default `Cufflinks` parameters versus the *XBP1*-tuned parameters before and after Trackster's dynamic `FPKM`/`Score` filtering.
* **HOW:** Using `cuffcompare` against the `hg19` reference annotation (Ensembl/RefSeq) on one representative BodyMap tissue, report the sensitivity and precision at the intron and transcript levels for (a) default `Cufflinks`, (b) unfiltered *XBP1*-tuned `Cufflinks`, and (c) *XBP1*-tuned `Cufflinks` after applying the dynamic filter criteria (`Score` and `FPKM` thresholds from Figure 2C). Discuss in the text how users should select multi-locus representative benchmarks when tuning parameters intended for genome-wide runs.

#### 3. Fix Minor Typographical Errors in the Text and Figure 2 Legend
* **WHY:** Several minor typographical errors appear in the manuscript text and figure legends:
  1. Line 27: `"making it easy to use use visual inspection"` (duplicate word `"use"`).
  2. Line 53 (Figure 2 legend): `"Using Trackster to dynamically filtering transcript assemblies"`, `"genomic inteval dataset"`, and `"filtering simutaneously by FPKM"`.
  3. Line 55: `"and filtering filtering genome wide takes ~10–20 minutes"` (duplicate word `"filtering"`).
  4. Line 57: `"Reid and Niccitta 18"` (author surname is spelled `"Nicchitta"`).
  5. Line 59: `"and Tracker visualizations used"` (should be `"Trackster visualizations"`).
  6. Line 61: `"makes use of it when it available"` (should be `"when it is available"`).
* **WHAT & HOW:** Correct each of these six typographical errors in the manuscript text and Figure 2 caption.
