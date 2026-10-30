# Review of AN_ANON_034

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.8/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents KegAlign, a high-performance GPU+CPU pairwise whole-genome aligner that refactors SegAlign and `lastZ` to eliminate CPU tail latency and GPU starvation during whole-genome local alignment. The authors diagnose why SegAlign suffers from severe hardware underutilization on closely related genomes (where a single 10×10 Mbp chunk can contain $>10^7$ high-scoring ungapped segment pairs [HSPs], causing one single-threaded `lastZ` gapped-extension job to run for $>27$ hours while 31 CPU cores and the GPU sit idle, and overflowing the 64 KiB UNIX pipe buffer). To solve this without duplicating straddling alignments, KegAlign introduces (1) a **diagonal partitioning strategy** that dynamically splits large HSP segment files along forward and reverse alignment diagonals at the upper-quartile segment count threshold, (2) a superlinear speedup in `lastZ` gapped extension due to bounding the size of `lastZ`'s quadratic-time internal HSP linked list, and (3) **pipeline and GPU utilization optimizations** including lowered `lastZ` thread priority (`nice`), disk-backed command buffering, and chromosome bin packing (Longest-Processing-Time-First) across NVIDIA Multi-Instance GPU (MIG) and Multi-Process Service (MPS) partitions. On 32 Xeon cores and 1 NVIDIA A100 GPU, KegAlign reduces human–chimpanzee (`hs1` vs. `panTro6`) whole-genome alignment time from 38 hours (SegAlign) to 8.5 hours ($4.5\times$ speedup over SegAlign) and completes human–mouse (`hg38` vs. `mm39`) alignment in ~5.6 hours while retaining `lastZ`-level sensitivity on divergent sequences. Source code (MIT license), Conda packages, Zenodo archives, and public cloud workflows are fully available.

This is a well-engineered systems bioinformatics paper with a clear algorithmic insight: recognizing that `lastZ` anchor consumption is directional along the alignment diagonal and that partitioning HSP segment files diagonally (rather than row- or column-wise) bounds per-task work and quadratic linked-list overhead while minimizing duplicate straddling extensions. The primary areas for improvement are: (1) providing a direct, nucleotide-level alignment equivalence benchmark (precision, recall, and exact fraction of straddling/duplicate alignment bases) comparing KegAlign against unpartitioned `lastZ` and baseline SegAlign across the vertebrate genome pairs; (2) ensuring symmetric parameter tuning in the motivating aligner sensitivity comparison (where `last` was run with human/chimp parameters on a 0–40% divergence and human–mouse benchmark); and (3) fixing recurring terminology mix-ups in the text and figure captions between "gap-free" (ungapped) and "gapped" extension, as well as conflicting hardware specifications between Table 3 and the Methods.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Diagonal partitioning of HSP segment files resolves CPU tail latency in `lastZ` gapped extension and avoids the output bloat caused by row-wise partitioning, reducing human–chimpanzee alignment runtime from 38 h (SegAlign) to 8.5 h (KegAlign): [Well Supported].**  
  Figures 3, 4, 7, and 8 clearly demonstrate the root cause of SegAlign's tail latency (a single 27-hour `lastZ` extension job and quadratic linked-list overhead) and show that diagonal partitioning dramatically reduces both total CPU gapped-extension time and maximum task duration while keeping total output file size nearly flat across segment file size thresholds (Figure 7).

* **Lowering `lastZ` thread priority, replacing UNIX pipe buffers with disk buffers, and running chromosome-binned instances under NVIDIA MIG/MPS increases GPU utilization and yields a further 10–20% runtime reduction across all divergence levels: [Well Supported].**  
  Figure 3B and Figure 8 validate that eliminating pipe backpressure and scheduling multiple concurrent SegAlign processes via LPT chromosome binning and MIG/MPS keeps the A100 GPU saturated and provides consistent 10–20% speedups across both closely related (`hs1`/`panTro6`/`gorGor6`) and divergent (`mm39`/`galGal6`) vertebrate pairs.

* **KegAlign maintains `lastZ`-level alignment sensitivity while reducing straddling alignments and midpoint-anchor approximations to a "negligible number": [Moderately Supported].**  
  While Figure 7 plots aggregate `Output Size (GB)` as a proxy for duplicate straddling alignments, the manuscript does not report exact base-level concordance metrics (e.g., Jaccard base overlap, percentage of identical MAF blocks, bases lost due to placing the anchor at the HSP midpoint instead of `lastZ`'s exact maximum-score point, or bases duplicated at diagonal partition boundaries) between KegAlign and single-threaded `lastZ` / baseline SegAlign on the vertebrate benchmarks.

* **`lastZ` (and KegAlign) achieves substantially higher alignment coverage on divergent sequences (up to 40% divergence and human–mouse coding exons) than `minimap2`, `fastga`, and `last` (Figure 1A–B): [Moderately Supported].**  
  While `lastZ`'s high sensitivity on divergent sequences is well established, the comparison in Figure 1A–B and Table 4 is not symmetrically tuned with respect to `last`: Table 4 states that `last` was run using **"Human/chimp parameters"** (which penalize substitutions heavily for ~1–2% primate divergence) when aligning sequences up to **40% divergence** and **human vs. mouse (`hg38` vs. `mm39`)**! Running `last` with primate parameters on a rodent comparison predictably degrades its sensitivity at $>15\%$ divergence compared to `lastZ`'s default `HOXD70` mammalian matrix.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Quantify Nucleotide-Level Alignment Concordance Between KegAlign, SegAlign, and Baseline `lastZ`
* **WHY:** KegAlign introduces two approximations relative to baseline `lastZ`/SegAlign: (i) splitting HSP segment files into diagonal bands of size $M$ (which can still split gapped alignments that cross a diagonal boundary in dense repeat/anchor regions), and (ii) approximating the HSP anchor coordinate as the exact midpoint rather than computing `lastZ`'s exact optimal anchor position (Results, line 79). Aggregate MAF file size in GB (Figure 7) does not distinguish whether 0.1% or 2% of aligned bases differ or are duplicated.
* **WHAT:** Report a table comparing KegAlign against baseline SegAlign (and against standard `lastZ` on chromosome 1) using exact alignment concordance metrics: (1) total aligned target/query bases after `bedtools merge`, (2) base-level recall and precision relative to `lastZ`, and (3) fraction of redundant/overlapping alignment bases caused by diagonal boundary straddling before merging.
* **HOW:** Using the existing MAF outputs from Figure 7 and Figure 8 (`hg38` vs. `hs1`, `panTro6`, `mm39`, `galGal6`), run `bedtools intersect` and `bedtools jaccard` between KegAlign's MAF intervals and SegAlign/`lastZ`'s MAF intervals, and report the exact percentages in the Results section.

#### 2. Add a Symmetrically Tuned `last` Baseline (`HOXD70` / `last-train` Mammal Parameters) to Figure 1
* **WHY:** In Table 4, `last` was configured with human/chimp parameters (`[GITLAB_REPO_REDACTED]`) while `lastZ` used its default `HOXD70` matrix tuned for human–mouse divergence (~35–40% substitution rate).
* **WHAT:** Re-run `last` on the simulated 0–40% divergence dataset (Figure 1A) and on `hg38` vs. `mm39` chr1/whole-genome (Figure 1B) using mammal-appropriate parameters (e.g., `lastdb -uMAM8` / `HOXD70` scoring or `last-train` on human–mouse) alongside the human/chimp curve.
* **HOW:** Add a second curve/bar for `last (MAM8 /last-train)` in Figure 1A–B so readers can see an apples-to-apples comparison of seed-and-extend sensitivity at mammalian divergence.

#### 3. Reconcile Hardware Specifications Between Table 3 and Methods and Correct Terminology Mix-Ups
* **WHY:** Several sections swap the terms "gap-free" (ungapped) and "gapped" extension, and the hardware node specification in Methods conflicts with Table 3.
* **WHAT & HOW:**
  * **Figure 4 caption (lines 55, 61):** Change `"lastZ gap-free extension runtimes, within the SegAlign pipeline"` to `"lastZ gapped extension runtimes, within the SegAlign pipeline"` (in SegAlign, gap-free extension is the Filter step on the GPU, whereas `lastZ` on the CPU runs *gapped* extension).
  * **Results (line 65):** Change `"SegAlign, which runs on GPU, performs the seed and extend steps"` to `"performs the seed and filter (ungapped extension) steps"`.
  * **Results (lines 67 and 77):** Change `"an HSP where ungapped alignment begins"` (line 67) and `"the anchor in which the ungapped alignment will begin"` (line 77) to `"where gapped alignment begins"` (an HSP *is* the ungapped alignment; the anchor is the seed point from which `lastZ` initiates *gapped* Y-drop extension).
  * **Table 3 (line 100) vs. Methods (chunk 2, line 25):** Table 3 states that the GPU portion (KegAlign) ran on `32 cores, 1 A100 GPU` with peak memory up to `28.0 Gb` (and GPU memory is 12 GB per SegAlign instance across multiple MIG/MPS instances on an 80 GB A100, line 88), whereas Methods (chunk 2, line 25) states that KegAlign ran on a `g3.medium node at https://jetstream-cloud.org/ . The node provides eight CPUs and one A100 GPU as well as 30 and 10 Gb of RAM for CPUs and GPU, respectively`. Update the Methods to state the actual node flavor (e.g., `g3.xl` or 32-core / 80 GB A100 node) used to generate Table 3.
  * **Methods (chunk 2, line 19):** The text states `"The total number on each chromosome was divided by the number of exons covered by alignments, obtaining the final fraction for each tool."` Reverse the numerator and denominator in the text to `"The number of exons covered by alignments on each chromosome was divided by the total number of exons"` to match Figure 1B.
  * **Methods (Table 4 vs. chunk 2, line 7):** Reconcile the `fastga` Git commit hash (`170a178d` in Table 4 vs. `74d5666` in chunk 2, line 7).
