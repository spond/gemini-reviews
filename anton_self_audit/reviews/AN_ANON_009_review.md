# Review of AN_ANON_009

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.4 / 10.0** (Strong / Sound)  
**Scientific Core Score:** **6.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 2.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces `rdeval` (v0.0.7), a multithreaded C++ and R command-line tool and reporting suite developed within the Vertebrate Genomes Project (VGP) and `gfastar` ecosystem to compute sequencing read summary statistics, filter/downsample reads, perform in-place linear-time homopolymer compression, convert among FASTA, FASTQ[`.gz`], SAM/BAM, and CRAM (v3.1 via HTSlib), and store highly compressed binary read "snapshots" (`.rd` files). Each `.rd` file records source file MD5 checksums (via OpenSSL) and gzip-compressed binary arrays of per-read lengths, quality scores, and base compositions, achieving 650-fold (short-read) to 9,000-fold (long-read) size reductions over original read files and enabling interactive (`plotly`) or static (`ggplot2`/PDF/HTML) visualization in seconds without re-parsing raw reads. The authors benchmark runtime, memory (<4 GB typical, ~10 GB maximum), and format compression across 84 VGP datasets (37 Illumina, 47 PacBio) and 11-Gbp downsampled human T2T-CHM13, HG002, and HPRC AVITI datasets, and generate `.rd` snapshots for 3,010 VGP long-read SRA runs (63.5 Tbp across 4.4 billion reads, compressed from ~50 TB of FASTQ.gz into 9.5 GB of `.rd` files). Precompiled binaries, MIT-licensed C++/R source code, ReadTheDocs format specifications, Bioconda/Galaxy wrappers, figure scripts, and the 3,010 GenomeArk snapshots are all publicly available.

`rdeval` is a well-engineered, high-utility software contribution backed by exemplary open-source distribution and a massive 63.5-Tbp empirical demonstration across the VGP archive. There are, however, three methodological and statistical areas where the manuscript should be tightened: (1) per-read average quality is computed as the arithmetic mean of the Phred `QUAL` integers (`mean(QUAL)`, Figure 3b legend), which averages logarithmic scores rather than averaging base error probabilities $P_i = 10^{-Q_i/10}$ prior to Phred transformation; (2) the Abstract states generally that "while CRAM achieves the best compression, the gain compared to BAM is marginal," without specifying that the benchmark evaluated **unaligned** raw read archives where CRAM cannot use reference-based delta encoding; and (3) the regression analysis of PacBio HiFi coverage versus contig N50 across vertebrate clades (Figure 3c, lines 32 and 50) excludes outliers without stating an objective outlier threshold and reports no correlation coefficients ($r$, $R^2$), slopes, or $p$-values in the text.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`rdeval` processes up to 150 Gbp of short- or long-read data in under 1 hour on 4 cores (<4 GB typical RAM) and compresses 63.5 Tbp (3,010 VGP SRA runs) into 9.5 GB of `.rd` snapshots: [Well Supported].**  
  The runtime, memory, and sublinear `.rd` scaling benchmarks across 84 VGP datasets and downsampled human reference runs (CHM13, HG002, AVITI; Figure 2e–f) thoroughly validate the tool's $O(N)$ streaming architecture and the 650$\times$–9,000$\times$ compression ratio of the `.rd` binary format.

* **Across 3,010 VGP long-read runs, PacBio read lengths increased from Sequel CLR (mean 10,803 bp) to Sequel II CLR (15,599 bp) and Sequel II HiFi (16,116 bp), then decreased on Revio HiFi (12,516 bp) alongside Q40 quality capping: [Well Supported].**  
  This large-scale consortium audit (Figure 3a–b) clearly separates genuine instrument/chemistry shifts in read length and consensus pass count from representational changes caused by Phred score binning and Q40 capping on the Revio platform.

* **While CRAM achieves the smallest file sizes, its compression gain over BAM is marginal (combined 1.2-fold over `FASTQ.gz`), making BAM the best compromise between compression and runtime speed: [Moderately Supported].**  
  Within the context of **unaligned** raw sequencing reads (which is what `rdeval` converts from SRA FASTQ files in Figure 2d), this finding is accurate because unaligned CRAM v3.1 relies solely on column-oriented rANS/bit-packing compression without reference-based differential encoding. However, because CRAM was primarily designed for reference-aligned reads (where storing only mismatches against a reference genome yields substantial compression gains over BAM), stating in the Abstract without qualification that CRAM's compression gain over BAM is "marginal" can mislead readers who assume the benchmark included coordinate-sorted aligned reads.

* **Per-read quality evaluation via the arithmetic mean of the BAM `QUAL` field (`mean(QUAL)`, Figure 3b): [Fragile].**  
  In the Figure 3b caption (line 48), the authors note that average read quality is computed as the arithmetic mean of the per-base Phred scores in the BAM `QUAL` field, and observe that the PacBio `rq` tag can differ from `mean(QUAL)`. Because Phred scores are logarithmic ($Q_i = -10 \log_{10} P_i$), the arithmetic mean $\bar{Q} = \frac{1}{L}\sum_{i=1}^L Q_i$ corresponds to the geometric mean of base error probabilities rather than the expected per-base error rate of the read, $\bar{P} = \frac{1}{L}\sum_{i=1}^L 10^{-Q_i/10}$. By Jensen's inequality, arithmetic averaging of Phred scores systematically overstates read accuracy whenever base quality varies within a read (for example, a read with 90% Q40 bases and 10% Q10 bases has an actual error rate of $\approx 1\% \implies Q_{\text{effective}} = 20$, whereas its arithmetic `mean(QUAL)` is $37$).

* **PacBio HiFi sequencing coverage correlates positively with assembly contig N50 across vertebrate clades except sharks (Figure 3c): [Moderately Supported].**  
  While the visual trend in Figure 3c is plausible, the statistical reporting is incomplete: (1) line 32 states that "regression lines were computed excluding outliers," without defining the mathematical rule used to identify outliers; (2) no sample sizes ($n$ per clade), correlation coefficients ($r$ or $R^2$), regression slopes, or $p$-values are reported in the text (line 50); and (3) raw contig N50 (in Mbp) is bounded above by a species' biological chromosome lengths (as illustrated by the king vulture, rock iguana, and coelacanth macrochromosome outliers), so correlating coverage against raw contig N50 without normalizing by chromosome/scaffold N50 or genome size confounds sequencing depth with karyotype architecture.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Support Probability-Space Mean Read Quality ($-10\log_{10}\overline{P_{\text{err}}}$) Alongside Arithmetic `mean(QUAL)`
* **WHY:** Computing per-read quality as $\frac{1}{L}\sum Q_i$ averages logarithmic quantities and systematically inflates read quality compared to the true expected error rate per base, $\bar{P} = \frac{1}{L}\sum 10^{-Q_i/10}$ (which is how standard PacBio `rq` and ONT/NanoPlot mean read qualities are defined prior to capping).
* **WHAT:** Add a precomputed lookup table $P(Q) = 10^{-Q/10}$ (for integer $Q \in [0, 93]$) in the C++ read parser to compute the Phred-scaled mean error probability $Q_{\text{prob}} = -10\log_{10}(\frac{1}{L}\sum_{i=1}^L P(Q_i))$ at zero runtime cost, and clarify the distinction between arithmetic `mean(QUAL)` and probability-space mean quality in the text and Figure 3b legend.
* **HOW:** In `rdeval`'s C++ per-read loop, accumulate `sum_error_prob += phred_to_prob_lut[q]` alongside `sum_q += q`, and store or report $-10\log_{10}(\text{sum\_error\_prob} / L)$. In the Figure 3b caption (line 48), explicitly explain how Jensen's inequality and Revio Q40 capping each contribute to differences between `mean(QUAL)` and the BAM `rq` tag.

#### 2. Explicitly Specify "Unaligned BAM and CRAM" in the Abstract and Discussion
* **WHY:** Readers scanning the Abstract ("while CRAM achieves the best compression, the gain compared to BAM is marginal") may not realize that all 84 VGP datasets in the format comparison (line 41) are unaligned raw read files converted from FASTQ, where CRAM cannot exploit reference-based delta compression.
* **WHAT:** Insert the word "unaligned" before "BAM and CRAM" in the Abstract (line 6) and Discussion (line 57), and note in Section 2 (line 41) that reference-aligned CRAM achieves higher compression ratios once reads are mapped.
* **HOW:** Change the Abstract sentence to: *"Overall, for unaligned raw reads, while CRAM v3.1 achieves the best compression, the gain compared to unaligned BAM is marginal, and BAM achieves the best compromise between data compression and access speed."*

#### 3. Report Exact Regression Statistics, Outlier Criteria, and Karyotype-Normalized Contig N50 in Figure 3c
* **WHY:** Line 32 notes that outliers were excluded before fitting the regression lines in Figure 3c, and line 50 claims clade-specific correlations without providing $n$, $r$, $R^2$, or $p$-values.
* **WHAT:** State the exact statistical rule used to flag and exclude outliers (e.g., $> 3\text{ SD}$ or $1.5 \times \text{IQR}$), report the per-clade sample size $n$, Pearson/Spearman $r$, and $p$-value in the text on line 50, and test whether the coverage correlation strengthens when contig N50 is normalized by scaffold/chromosome N50 (i.e., the ratio $\text{contig N50} / \text{scaffold N50} \in (0, 1]$).
* **HOW:** Using the metadata already compiled in Supplementary Table S5, add $(n, r, p)$ parenthetically for each vertebrate clade in line 50, state the outlier definition in line 32, and report the correlation of HiFi coverage with the relative contiguity ratio ($\text{contig N50} / \text{scaffold N50}$) so species with giant macrochromosomes (e.g., *Cyclura pinguis*, *Sarcoramphus papa*) are evaluated on a karyotype-normalized scale.

#### 4. Include `samtools stats` and `NanoPlot` / `cramtools` in the Baseline Tool Discussion
* **WHY:** In the Discussion (line 59), `rdeval` is compared against `FastQC`, `SeqKit`, and `seqtk`, noting that `SeqKit` and `seqtk` lack BAM/CRAM support and `FastQC` is tailored to short reads. In long-read and VGP/T2T workflows, `samtools stats` (HTSlib C) and `NanoPlot` / `NanoStat` are the primary baseline tools that natively read BAM/CRAM.
* **WHAT:** Briefly note how `rdeval` compares with `samtools stats` and `NanoPlot` (specifically highlighting `rdeval`'s unique `.rd` binary snapshot format for instant multi-run re-plotting and on-the-fly homopolymer compression).
* **HOW:** Add two sentences to the third paragraph of the Discussion (line 59) contrasting `rdeval` with `samtools stats` and `NanoPlot`.
