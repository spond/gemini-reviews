# Review of AN_ANON_034

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.1 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.2 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.9/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces `KegAlign`, a refactored and parallelized GPU-enabled pairwise whole-genome aligner built upon `SegAlign` and `lastZ`. The authors diagnose why `SegAlign` suffers from severe CPU and GPU underutilization (tail latency) when aligning closely related vertebrate genomes: equal-area ($10 \times 10\text{ Mbp}$) chunks produce wildly skewed numbers of high-scoring segment pairs (HSPs, from $1$ to $>10^7$), leaving a single single-threaded CPU `lastZ` gapped-extension task running for up to $27\text{ h}$ while the GPU and remaining CPU cores sit idle, compounded by $64\text{ KiB}$ UNIX pipe backpressure. To resolve these bottlenecks, `KegAlign` introduces (1) **diagonal partitioning** of segment files along the forward ($+$) and reverse ($-$) alignment diagonals with an adaptive upper-quartile segment threshold to balance CPU gapped-extension workloads without generating excessive straddling/duplicate alignments, (2) **pipeline decoupling** (`nice` CPU priority tuning and disk-backed command buffers, packaged into `KegAlign` GPU seed-and-filter and `batched-lastZ` CPU gapped-extension stages), and (3) **NVIDIA Multi-Instance GPU (MIG) and Multi-Process Service (MPS)** bin scheduling across ~200 Mbp chromosome bins via longest-processing-time-first (LPT) bin packing. On a single node with $32$ Intel Xeon Gold 6330 CPUs and $1$ NVIDIA A100 GPU, `KegAlign` reduces human–chimpanzee (`hs1` vs. `panTro6`) whole-genome alignment walltime from $38\text{ h}$ (`SegAlign`) to $8.5\text{ h}$, and completes human–mouse (`hg38` vs. `mm39`) seed-and-filter + extension in under $6\text{ h}$. Source code (MIT license), Conda packages, Zenodo archives, and public workflow definitions are openly available.

`KegAlign` represents a well-engineered systems bioinformatics contribution that directly targets the computational bottleneck of vertebrate-scale comparative genomics (`lastZ`). The root-cause profiling of `SegAlign` (Figure 3, Figure 4) and the algorithmic insight of partitioning HSP anchors along diagonals rather than rows/columns to preserve `lastZ`'s internal anchor-shadowing linked list (Figures 5–7) are technically convincing. However, three methodological and reporting issues merit correction: (1) an arithmetic/definition error in the Methods description of how exon coverage fractions were normalized for Figure 1B; (2) an incomplete accuracy audit of the diagonal partitioning approximation (which replaces `lastZ`'s exact anchor selection with the HSP midpoint and permits boundary straddling without quantifying nucleotide-level sensitivity/precision loss relative to unpartitioned `lastZ`); and (3) hardware-configuration mismatches between the single-node benchmarks (`32` cores + `1` A100) and the split cloud/HPC workflow (`Jetstream2` `8`-CPU/`10 GB` A100 slice vs. `Stampede3` `80`-core CPU node vs. Table 3 header).

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`lastZ` retains a substantial sensitivity advantage over faster modern aligners (`minimap2 -x asm20`, `fastga`, `last`) on divergent coding sequences ($>20\%$ divergence, human vs. mouse): [Well Supported].**  
  Synthetic sequence benchmarks ($1,000$ to $10,000\text{ nt}$, $0\text{--}40\%$ divergence with $1\%$ short indels; Figure 1A) and empirical whole-genome human–mouse (`hg38` vs. `mm39`) coding-exon overlap benchmarks (Figure 1B) demonstrate that `minimap2` and `fastga` lose sensitivity rapidly beyond $15\text{--}20\%$ divergence, whereas `lastZ`/`KegAlign` and `last` maintain high alignment coverage across divergent vertebrate exons.

* **Diagonal partitioning of segment files eliminates CPU tail latency and superlinearly reduces total `lastZ` gapped-extension CPU time on closely related genomes while avoiding the output explosion of row-wise partitioning: [Well Supported].**  
  Because `lastZ` suppresses extension of downstream anchors crossed by a prior extension and queries a linked list of ungapped segments with $O(N^2)$ traversal overhead, splitting large segment files diagonally along the extension direction both caps the maximum per-task runtime (from $27\text{ h}$ down to minutes) and reduces the quadratic linked-list search cost per CPU thread (Figure 7), cutting `hs1` vs. `panTro6` walltime from $38\text{ h}$ to $8.5\text{ h}$ on 32 CPUs + 1 A100 GPU (Figure 3, Figure 8).

* **Approximating `lastZ` anchor coordinates by the HSP midpoint and partitioning diagonally introduces only a "negligible" difference in final alignment blocks: [Moderately Supported].**  
  In the Results (lines 77–79), the authors note two approximations relative to native `lastZ`: (i) instead of computing the exact highest-scoring sub-point along each HSP as the anchor, `KegAlign` uses the geometric midpoint of the HSP start and end coordinates; and (ii) densely clustered anchors near diagonal partition boundaries can still straddle partitions, producing duplicate/overlapping extensions or altered dynamic-programming tiebreaker paths. While Figure 7 tracks total `Output Size` (in bytes/MB) as a proxy for duplication, the manuscript does not report the exact base-level Jaccard similarity, precision/recall of aligned base pairs, or MAF block concordance between native unpartitioned `lastZ`/`SegAlign` and `KegAlign` across `hs1/panTro6` and `hg38/mm39`.

* **The Methods formula for computing the fraction of coding exons covered by alignments in Figure 1B is mathematically consistent: [Methodologically Flawed].**  
  In the Methods section (page 2 of chunk 2, lines 9 and 19), the authors state: *"These data were then aggregated by chromosome by counting the number of exons that overlap alignment blocks for each aligner. The total number on each chromosome was divided by the number of exons covered by alignments, obtaining the final fraction for each tool."* Dividing *"the number of exons that overlap alignment blocks"* by *"the number of exons covered by alignments"* would yield $1.0$ ($100\%$) identically for every aligner on every chromosome, contradicting Figure 1B. Clearly, the denominator in the notebook was the **total number of merged protein-coding exons on each chromosome** (not the number of exons covered by alignments), or the metric was base-pair coverage across merged exons.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Quantify Exact Alignment Concordance (Sensitivity and Duplication Rate) Between `KegAlign` and Unpartitioned `SegAlign`/`lastZ`
* **WHY:** Diagonal partitioning relies on an HSP midpoint heuristic for anchor coordinates and introduces partition boundaries that can split gapped extensions across indels. Showing only aggregate output file size in Figure 7 leaves open whether alignment coordinates or scores shift near partition boundaries.
* **WHAT:** Report the exact base-pair overlap (recall, precision, and percentage of duplicate/overlapping bases) of `KegAlign` (with dynamic upper-quartile diagonal partitioning) against baseline `SegAlign` (infinite max segment size) and native `lastZ` (on chromosome 1 of `hs1/panTro6` and `hg38/mm39`).
* **HOW:** Using the existing `bedtools merge` and `bedtools intersect` workflow, compute (a) the fraction of native `lastZ` aligned base pairs recovered by `KegAlign`, (b) the fraction of `KegAlign` aligned base pairs present in native `lastZ`, and (c) the redundant base-pair inflation ratio ($\text{sum of raw MAF block lengths} / \text{merged interval length}$) before and after diagonal partitioning.

#### 2. Reconcile Hardware Specifications Between the Methods Text and Table 3
* **WHY:** There is a discrepancy between the compute node specifications described in the Methods text and those reported in Table 3.
* **WHAT & HOW:**
  1. In Methods (chunk 2, lines 25–27), the `KegAlign` cloud node is described as a `g3.medium` node on Jetstream2 providing *"eight CPUs and one A100 GPU as well as 30 and 10 Gb of RAM for CPUs and GPU, respectively"*. However, Table 3 (line 100) lists the GPU portion as `KegAlign (32 cores, 1 A100 GPU)` with peak memory reaching `26.4 Gb` (`hg38/hs1`) and `28.0 Gb` (`hg38/panTro6`), and earlier text (line 88) states that each 200 Mbp bin uses roughly `12 GB` of GPU memory on an `80 GB` A100. Clarify which exact node (`g3.xl` / full A100 vs. `g3.medium`) was used to generate Table 3, and specify whether the Peak Memory column in Table 3 reports host RAM or GPU VRAM.
  2. Note in Methods (chunk 2, line 7) that `fastga` commit `74d5666` is listed for the whole-genome exon benchmark whereas Table 4 (line 144) lists `170a178d`; clarify whether two different commits were used.

#### 3. Correct the Exon Coverage Denominator Description and Dynamic Partitioning Heuristic Details
* **WHY:** Readers reproducing Figure 1B or re-implementing the dynamic upper-quartile segment threshold need exact mathematical definitions.
* **WHAT & HOW:**
  1. **Exon Coverage Denominator (Methods, chunk 2, lines 9 & 19):** Change *"divided by the number of exons covered by alignments"* to *"divided by the total number of merged protein-coding exons on each chromosome"*.
  2. **Cold-Start Behavior of Dynamic Upper-Quartile Heuristic (Line 86):** Line 86 states that whenever a segment file is made, `KegAlign` sets the maximum segment file size to the upper quartile ($75\text{th}$ percentile) of the unpartitioned sizes of previously generated segment files in the shared folder. Specify the initial fallback threshold used for the very first segment file(s) before a meaningful empirical distribution of segment file sizes exists, and note how race conditions across concurrent processes reading/writing the shared folder are handled.
