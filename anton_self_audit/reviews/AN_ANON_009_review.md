# Review of AN_ANON_009

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.8 / 8.0**  
* **Score Breakdown:** Rigor: 2.4/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 2.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents `rdeval` (v0.0.7), a multithreaded C++ and R toolkit developed within the Vertebrate Genomes Project (VGP) to compute sequencing read summary metrics, filter and downsample reads, perform linear-time homopolymer compression, convert across FASTA, FASTQ, SAM/BAM, and CRAM formats (via `htslib`), and store per-read length, quality, and base-composition summaries in compact, gzip-compressed binary `.rd` "snapshot" files (including source file MD5 checksums). The `.rd` snapshots enable rapid regeneration of static (PDF/HTML) and interactive (`plotly`) reports without re-reading multi-terabyte raw datasets. The authors benchmark `rdeval` across 84 VGP Illumina ($n=37$) and PacBio ($n=47$) datasets and 5 downsampled (11 Gbp) human reference datasets (CHM13 and HG002 across Illumina, 10x, AVITI, PacBio HiFi, and ONT UL), and deploy it across 3,010 VGP long-read SRA runs totaling 63.5 Tbp (4.4 billion reads, ~50 TB of `.fastq.gz`), compressing their read metrics into 9.5 GB of `.rd` files. Precompiled binaries, C++/R source code, automated test workflows, Bioconda/workflow wrappers, and analysis scripts are openly available under an MIT license.

`rdeval` is a well-engineered, highly practical utility with exemplary open-science availability (code, documentation, and 3,010 public snapshots on GenomeArk). However, three methodological and statistical issues affect the secondary comparative and biological analyses presented in the paper: (1) the file-format benchmark concluding that CRAM v3.1 offers only a "marginal" compression advantage over BAM evaluates *unaligned* reads downloaded via `fasterq-dump`, disabling the reference-based delta encoding that is CRAM's primary compression mechanism; (2) per-read average quality is computed as the arithmetic mean of Phred scores (`mean(QUAL)`) rather than converting Phred scores to error probabilities ($P = 10^{-Q/10}$), averaging in probability space, and converting back to Phred scale, which systematically inflates read quality estimates whenever intraread quality varies; and (3) the clade-stratified regressions of assembly contig N50 against PacBio HiFi coverage (Figure 3c) exclude "outliers" without stating a formal statistical threshold and omit sample sizes, slopes, $R^2$, and $p$-values while leaving karyotype chromosome length and repeat content uncontrolled. Addressing these analytical points will align the empirical benchmarks with the high quality of the software tool.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`rdeval` computes read metrics in $O(N)$ time and compresses per-read length/quality distributions by 650- to 9,000-fold into `.rd` snapshots: [Well Supported].**  
  The C++ implementation processes 30$\times$ human long-read datasets in 5–10 minutes (~30 minutes for short reads) using $<4\text{ GB}$ RAM on average (4 cores), and shrinks 63.5 Tbp across 3,010 VGP long-read SRA runs (~50 TB of gzipped FASTQ) into 9.5 GB of `.rd` files that render reports in 7–95 seconds (Figure 2e–f).

* **While CRAM v3.1 achieves the smallest file sizes, its compression gain over BAM is marginal, making BAM the best compromise: [Overstated].**  
  As noted in Section 2 (lines 32 and 41), the format comparison was run on SRA reads converted to FASTQ via `fasterq-dump` and then written to *unaligned* BAM and CRAM files. Because CRAM is specifically designed for reference-oriented compression—storing only base calls that differ from an aligned reference genome (Section 1, line 14)—benchmarking CRAM solely on unaligned reads disables its core delta-compression algorithm and tests only its column-block/rans entropy coder (`CRAM v3.1`). The conclusion should be explicitly restricted to *unaligned* raw read storage.

* **Per-read average quality calculations (`mean(QUAL)`) and cross-platform quality comparisons (Figure 2c, Figure 3b): [Methodologically Flawed].**  
  In Figure 3b, per-read quality is computed as the arithmetic mean of the per-base Phred `QUAL` integers: $\bar{Q}_{\text{arith}} = \frac{1}{L}\sum_{i=1}^L Q_i$. Because Phred quality is logarithmic ($Q_i = -10\log_{10} P_i$), averaging $Q_i$ computes the geometric mean of error probabilities rather than the true per-read error rate $\bar{P} = \frac{1}{L}\sum_{i=1}^L 10^{-Q_i/10}$, where $Q_{\text{true}} = -10\log_{10} \bar{P}$. By Jensen's inequality, $\bar{Q}_{\text{arith}} \ge Q_{\text{true}}$, often overestimating read accuracy by 5–15 Phred units when low-quality bases are present (and explaining why PacBio's probability-averaged `rq` tag differs systematically from `mean(QUAL)` on uncapped reads).

* **Increasing PacBio HiFi coverage correlates positively with assembly contig N50 across vertebrate clades except sharks (Figure 3c): [Fragile].**  
  Section 2 (line 32) states that "regression lines were computed excluding outliers," and Section 2 (line 50) highlights six biological outliers, but no formal outlier definition (e.g., studentized residuals, Cook's distance, or IQR threshold) is provided, nor are per-clade sample sizes ($n$), correlation coefficients ($r$ or $R^2$), regression slopes, or $p$-values reported. Moreover, contig N50 is bounded by physical chromosome sizes (e.g., avian microchromosomes vs. macrochromosomes) and confounded by assembler version and read length N50.

* **Runtime and feature superiority over existing sequence QC tools (FastQC, SeqKit, seqtk): [Moderately Supported].**  
  While Supplementary Table 1 compares supported features qualitatively, the manuscript presents no head-to-head wall-clock runtime or peak memory benchmarks running `rdeval` against `SeqKit stats`, `seqtk fqchk`, `fastp`, or `Cramino` on the same 84 VGP datasets.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Compute True Probability-Space Per-Read Average Quality Alongside Arithmetic `mean(QUAL)`
* **WHY:** Averaging logarithmic Phred scores directly ($\frac{1}{L}\sum Q_i$) is a well-known bioinformatics pitfall that understates the true expected number of errors in a read ($\sum 10^{-Q_i/10}$) and distorts comparisons between technologies with uniform quality (e.g., Q40-capped Revio HiFi) and technologies with wider intraread quality variance (e.g., ONT UL or Illumina).
* **WHAT:** Implement probability-space read quality averaging ($Q_{\text{prob}} = -10\log_{10}\left(\frac{1}{L}\sum_{i=1}^L 10^{-Q_i/10}\right)$ via a fast 94-element lookup table in C++) as the default or co-reported per-read quality metric in `rdeval`.
* **HOW:** Precompute `double prob_table[94]` where `prob_table[q] = pow(10.0, -q / 10.0)` at startup in `rdeval`, accumulate the sum of error probabilities across each read in $O(L)$ time with zero `pow()` overhead per base, convert the mean probability back to Phred scale at the end of the read, and clarify the mathematical distinction between `mean(QUAL)` and probability-averaged `rq` in the caption of Figure 3b.

#### 2. Report Formal Regression Statistics, Outlier Criteria, and Normalized Contiguity in Figure 3c
* **WHY:** Visual trend lines drawn after ad-hoc outlier removal without reporting $n$, $R^2$, $p$-values, or the outlier exclusion rule cannot be statistically evaluated, and raw contig N50 is heavily confounded by species karyotype (chromosome N50) and genome size.
* **WHAT:** State the exact mathematical rule used to flag and exclude outliers in Figure 3c, report $n$, slope, $R^2$, and $p$-value for each vertebrate clade (both with and without outliers), and test whether the coverage relationship holds when contig N50 is normalized by scaffold/chromosome N50 (or in a multiple regression controlling for genome size and read N50).
* **HOW:** Using the existing VGP metadata table (Supplementary Table 5), run a linear model (`contig_N50 ~ coverage + read_N50 + genome_size`, or `contig_N50 / scaffold_N50 ~ coverage`) in R for each clade, define outliers reproducibly (e.g., $|\text{standardized residual}| > 3$), and annotate each clade's $n$, $R^2$, and $p$-value directly on Figure 3c or in the main text (line 50).

#### 3. Qualify the CRAM vs. BAM Compression Conclusions and Add a Direct Runtime Baseline Against `SeqKit` / `seqtk`
* **WHY:** Readers may interpret the Abstract claim ("while CRAM achieves the best compression, the gain compared to BAM is marginal") as applying to CRAM generally, rather than specifically to *unaligned* SRA reads lacking a reference sequence. Furthermore, empirical runtime comparisons against established fast C/Go tools (`seqtk`, `SeqKit`) would substantiate the performance claims in Section 3.
* **WHAT:** Explicitly insert the word "unaligned" in the Abstract and Discussion when comparing BAM and CRAM compression ratios, and add a runtime/memory comparison of `rdeval` against `SeqKit stats` and `seqtk` on a subset of the human benchmark datasets (Table 3).
* **HOW:** Update the Abstract ("while unaligned CRAM achieves the best compression, the gain compared to unaligned BAM is marginal") and run `seqkit stats -a -j 4` and `fastqc -t 4` on the five 11 Gbp human datasets from Table 3 to include as a benchmark column or supplementary table.

#### 4. Technical and Editorial Cleanup
* **WHY:** Minor inaccuracies appear in the Figure 2a legend and text.
* **WHAT & HOW:**
  1. **Figure 2a Legend (line 37):** Change `"Inputs include genome assemblies in fasta, fa*[.gz], BAM, CRAM formats"` to `"Inputs include sequencing reads (or assemblies) in FASTA, FASTQ[.gz], SAM/BAM, and CRAM formats"`.
  2. **Section 2 (line 32):** Clarify the theoretical size calculation `"2 bytes per base (sequence and quality) * ~60Tb considering a gzip compression factor of ~2.5x"` by writing out the units explicitly ($\frac{2\text{ bytes/bp} \times 63.5\text{ Tbp}}{2.5} \approx 50.8\text{ TB}$), avoiding confusion between Terabits (`Tb`), Terabase pairs (`Tbp`), and Terabytes (`TB`).
