# Review of AN_ANON_028

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 2.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This correspondence presents a federated, open-access platform for global SARS-CoV-2 genomic surveillance and raw-read intrahost allelic variant (AV) analysis, deployed across three public computational infrastructures in the United States, the European Union, and Australia. The system is organized into two stages (Figure 1): Stage 1 executes four standardized, BioConda-packaged workflows for quality control, read trimming, mapping, deduplication, variant calling, and consensus assembly across Illumina (whole-genome and amplicon, paired- and single-end) and Oxford Nanopore sequencing data; Stage 2 processes the resulting standardized variant tables using browser-based interactive notebooks and dashboards to track temporal variant dynamics, co-occurrence patterns, and intersections with selection and antibody-escape sites. The authors demonstrate the platform's scalability by reanalyzing 619 early transmission samples from Boston (PRJNA622837) and ~100,000 samples from the UK (COG-UK, PRJEB37886).

Pooling public high-performance computing across three continents to enable free, standardized reanalysis of raw SARS-CoV-2 sequencing reads (rather than relying solely on static consensus assemblies) is a major practical contribution to global pathogen genomics and data equity. The primary scientific limitation lies in the biological interpretation of low-frequency minor allelic variants (AVs) in large multi-center amplicon datasets: while the manuscript highlights "non-random associations among common low-frequency AVs that may reflect shared intra-host dynamics," low-frequency co-occurring variants in high-throughput SARS-CoV-2 amplicon sequencing are notoriously confounded by untrimmed primer dimers, systematic RT-PCR/polymerase errors, homoplasies, and inter-sample cross-contamination or index hopping during multiplexed runs (especially in low-viral-load samples). Explicitly documenting the minimum allele-frequency filters, strand-bias checks, primer-site masking, and contamination controls in the main text is essential to prevent overinterpretation of technical artifacts as intrahost co-evolution.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Pooling public computational infrastructure across US, EU, and Australian instances with BioConda-packaged workflows enables scalable, accessible raw-read SARS-CoV-2 reanalysis (~100,000 samples): [Well Supported].**  
  The two-stage architecture (Figure 1) and its execution on 619 PRJNA622837 samples and ~100,000 PRJEB37886 (COG-UK) samples demonstrate that the federated platform can handle pandemic-scale raw sequencing throughput while providing open access (250 GB expandable storage per user) without commercial cloud procurement barriers.

* **Standardized raw-read workflows provide full provenance from FASTQ files to annotated variant tables and consensus sequences across Illumina and Nanopore platforms: [Well Supported].**  
  All four primary analysis workflows and the downstream Reporting and Consensus workflows are versioned, publicly accessible via the project portal, and linked directly to public ENA/SRA accessions.

* **Co-occurrence patterns among common low-frequency allelic variants in PRJNA622837 and COG-UK reflect shared intra-host evolutionary dynamics: [Fragile].**  
  While the authors appropriately use cautious phrasing ("may reflect shared intra-host dynamics", "suggesting possible intra-host dynamics"), calling genuine intrahost minor variants from clinical SARS-CoV-2 specimens—especially without replicate sequencing or viral copy-number ($C_t$) filtering—is highly vulnerable to batch-specific amplicon primer artifacts, reverse-transcription errors, and plate/flowcell cross-contamination. When two lineages co-contaminate a sequencing batch or share an amplicon dropout/primer-binding artifact, they produce strong non-random co-occurrence of low-frequency AVs across samples that mimics intrahost linkage.

* **Tracking intra-patient minor AV frequencies provides early warning of variants with altered pathogenicity, vaccine sensitivity, or drug resistance: [Moderately Supported].**  
  Intersecting raw-read AV tables with deep mutational scanning antibody-escape maps and natural selection sites is a sound surveillance strategy (particularly for chronic infections), provided that technical false positives in minor variant calls are rigorously filtered out.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Specify Quantitative Filtering Criteria and Contamination Controls for Minor Allelic Variants
* **WHY:** Without explicit quality, depth, strand-bias, and allele-frequency thresholds, recurrent sequencing or primer-trimming artifacts in 100,000 amplicon datasets can easily be mistaken for shared intrahost minor variants.
* **WHAT:** State the exact numerical thresholds applied in the Stage 1 variant-calling and filtering workflows and in the Stage 2 co-occurrence analyses.
* **HOW:** Add 2–3 sentences in the main text (and detail in Supplementary Table 1) specifying: (i) the variant caller(s) used (e.g., `lofreq`, `ivar`, `medaka`), (ii) the minimum read depth, base quality, strand-bias filter, and minor allele frequency cutoff (e.g., $\text{AF} \ge 0.05$) required to retain an AV, (iii) how amplicon primer binding sites and problematic homoplasy/artifact sites are masked, and (iv) how batch-level cross-contamination is flagged in the Stage 2 notebooks.

#### 2. Benchmark Variant-Calling Accuracy and Report Computational Throughput Metrics
* **WHY:** Readers and public-health laboratories evaluating the four workflows need quantitative verification of both variant-calling precision/recall and expected turnaround times on the three public instances.
* **WHAT:** Summarize benchmark performance on synthetic/control SARS-CoV-2 mixtures and report wall-clock processing throughput on the COG-UK dataset.
* **HOW:** Include a brief summary in the text or Supplementary Table 1 reporting sensitivity and false-positive rates for consensus and minor AV calls on control datasets, along with average runtime and CPU-hours per 1,000 paired-end samples across the US, EU, and Australian instances.

#### 3. Add an Explicit Caveat on Viral Load ($C_t$) and Amplicon Artifacts in Intrahost Interpretation
* **WHY:** Low-template ($C_t > 30$) clinical samples exhibit high stochastic RT-PCR bottlenecking and elevated background contamination, making minor allele frequencies unreliable without viral load metadata.
* **WHAT:** Add a brief caveat in the final paragraph or Stage 2 notebook documentation regarding the interpretation of low-frequency AVs when $C_t$ values and technical replicates are unavailable in public SRA/ENA submissions.
* **HOW:** Note in the text that while raw-read reanalysis uncovers candidate minor variants, distinguishing true intrahost selection from co-infection or sequencing batch effects requires checking whether co-occurring minor alleles match defining mutations of contemporaneous circulating clades in the same sequencing center/run.
