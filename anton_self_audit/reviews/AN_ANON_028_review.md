# Review of AN_ANON_028

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.3 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.7/3.5 | Claims: 1.9/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This correspondence presents a federated, open-access global genomic surveillance platform for SARS-CoV-2 raw sequencing reads deployed across three major public compute clouds (XSEDE in the United States, ELIXIR in the European Union, and Nectar Cloud in Australia). The system is structured as a two-stage pipeline (Figure 1): Stage 1 executes standardized, BioConda-packaged workflows for quality control, read trimming, mapping, deduplication, allelic variant (AV) calling, filtering, consensus genome generation, and reporting across four sequencing modalities (Illumina paired-end, Illumina single-end, tiled-amplicon ARTIC, and Oxford Nanopore Technologies); Stage 2 uses interactive browser-based notebooks and an automated dashboard to track temporal AV dynamics, co-occurrence patterns, selection signatures, and antibody-escape mutations. The authors demonstrate the platform on two public SARS-CoV-2 cohorts: 619 Illumina samples from early transmission in Boston (PRJNA622837) and ~100,000 samples from COG-UK (PRJEB37886). All workflows, notebooks, dashboards, and raw data accessions are openly available.

As a short correspondence/resource announcement, the manuscript delivers a timely, high-capacity, and fully transparent bioinformatic infrastructure that democratizes raw-read viral genomic analysis (providing 250 GB of expandable storage and free HPC execution to researchers worldwide without commercial cloud billing barriers). Its main scientific limitations lie in the brief treatment of low-frequency intra-host variant artifacts—specifically, inferring "shared intra-host dynamics" and "early warnings" from low-frequency allelic variants in high-throughput public surveillance datasets (such as COG-UK amplicon data) without explicitly detailing in the main text the minimum allele frequency cutoffs, strand-bias filters, primer-dimer/adapter masking, or cross-sample contamination controls required to separate true intra-patient minor variants from RT-PCR and sequencing noise. Addressing these technical parameters directly in the main text and tempering the epidemiological early-warning claim will strengthen the report.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Pooling public HPC infrastructure across US, European, and Australian instances provides a scalable, zero-cost, reproducible two-stage workflow platform capable of processing >100,000 SARS-CoV-2 raw-read datasets: [Well Supported].**  
  The platform's capacity and end-to-end execution are directly demonstrated by the automated processing of 619 Boston samples (PRJNA622837) and ~100,000 COG-UK samples (PRJEB37886) using BioConda-pinned tools and standardized workflows across four sequencing protocols (Figure 1, Supplementary Tables 1–3).

* **Analyzing raw sequencing reads rather than static consensus assemblies enables systematic tracking of minor allelic variants (AVs) and traceable provenance: [Well Supported].**  
  Consensus FASTA repositories discard sub-consensus read support and masking thresholds. Retaining standardized VCF and TSV allelic variant tables directly linked to raw SRA/ENA accessions (PRJNA622837, PRJEB37886) allows re-inspection of variant call quality, read depth, and allele frequency distributions.

* **Non-random associations among common low-frequency AVs in public surveillance cohorts reflect "shared intra-host dynamics": [Fragile].**  
  In line 72, the authors highlight "non-random associations among common low-frequency AVs that may reflect shared intra-host dynamics (Supplementary Fig. 1 and Supplementary Table 2)." In multi-center amplicon and metagenomic sequencing cohorts (such as COG-UK and Boston), recurrent co-occurring low-frequency variants across samples frequently arise from systematic technical artifacts—including unmasked ARTIC primer-binding site mismatches, primer dimers, index hopping / barcode cross-talk on Illumina patterned flowcells, laboratory batch contamination, or recurrent homopolymer/polymerase errors—rather than independent within-host evolutionary selection.

* **Surveillance of intra-patient minor AV frequencies can yield "early warnings of epidemiological conditions conducive to the emergence of variants with altered pathogenicity, vaccine sensitivity or drug resistance": [Moderately Supported].**  
  While intra-host diversity in chronic infections is a plausible source of antigenic evolution, routine population surveillance samples are predominantly acute diagnostic swabs with tight transmission bottlenecks (1–3 virions) and unknown viral load (Ct values), where low-frequency intra-host variants rarely transmit forward at the population level.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Specify the Exact Variant Calling, Primer-Trimming, and Minimum Allele Frequency Filters in the Main Text
* **WHY:** Because the correspondence's central scientific argument rests on calling minor intra-host allelic variants (AVs) from raw reads across Illumina WGS, ARTIC amplicon, and ONT protocols (lines 70–74), readers need to know the exact variant callers (e.g., `ivar`, `lofreq`, `medaka`) and minimum allele frequency / depth / strand-bias thresholds without digging through external links.
* **WHAT:** Add 2–3 sentences to the main text (around line 70) stating the exact variant calling tools, primer-trimming steps, minimum read depth, and minimum allele frequency (AF) thresholds used to define a reportable minor AV.
* **HOW:** Explicitly state the tool names and cutoffs from Supplementary Table 1 directly in paragraph 4 (e.g., `lofreq` for Illumina WGS/amplicon, `ivar`/`ivarremovereads` for ARTIC primer trimming and amplicon drop-out filtering, `medaka` for ONT, minimum depth $\ge 10\times$, strand-bias filter, and AF $\ge 0.05$).

#### 2. Discuss Technical Confounders of Co-Occurring Low-Frequency Variants in Amplicon Sequencing
* **WHY:** Co-occurring low-frequency AVs in large multi-site datasets (PRJEB37886 / PRJNA622837) are notoriously prone to batch-specific index hopping, cross-well contamination, and incomplete primer trimming when viral load is low (high Ct).
* **WHAT:** Qualify the interpretation of co-occurring low-frequency AVs on line 72 by acknowledging batch/amplicon artifacts and describing how the Stage 2 notebooks filter or flag them.
* **HOW:** Revise line 72 to note that while non-random co-occurrence of minor AVs can reflect shared intra-host selection or co-infection, it can also arise from amplicon primer artifacts or sequencing batch cross-contamination, and point to specific diagnostic checks (such as clustering by sequencing center/run accession or proximity to amplicon ends) in the Stage 2 notebooks.
