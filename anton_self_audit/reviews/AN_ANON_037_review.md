# Review of AN_ANON_037

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.7 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.8 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 1.8/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This short software application note describes an open-source, cross-platform Python tool suite for parsing, validating, interconverting, summarizing, trimming, and filtering next-generation sequencing (NGS) FASTQ files across all standard and legacy quality-score encodings (`Sanger` Phred+33, `Solexa` log-odds+64, and `Illumina 1.3+` Phred+64), integrated into a public web-based analysis platform. The suite comprises eight primary utilities: (1) `Combine FASTA and QUAL into FASTQ`, (2) `FASTQ Groomer` (which enforces quality-score minimums/maximums, interconverts ASCII/decimal encodings, and reports observed ASCII ranges alongside compatible FASTQ variants as a user sanity check), (3) `FASTQ Summary Statistics by column` (paired with `Boxplot` visualization), (4) `FASTQ Trimmer by column` (supporting absolute or percentage-of-read-length $5'$ and $3'$ offsets), (5) `Filter FASTQ reads by quality score and length` (supporting whole-read or sub-region offset aggregation operators), (6) `Manipulate FASTQ reads on various attributes` (regex-based selection and transformation on headers, nucleotide/color-space sequences, or quality strings, alongside `FASTQ-to-Tabular` conversion), and (7–8) `FASTQ Joiner` and `FASTQ Splitter` for paired-end reads. The tools are continuously tested against the standard Cock et al. FASTQ benchmark suite and distributed as open-source software with online test histories and video tutorials.

Evaluated as a brief bioinformatics software note, the toolkit addresses a critical source of silent downstream error in early short-read genomics: incompatible FASTQ quality score offsets (`Phred+33` vs. `Phred+64` vs. `Solexa` log-odds) and ad-hoc read preprocessing. Integrating automated functional regression tests using the Cock et al. reference test cases and reporting observed ASCII bounds (`<59` for Sanger) in `FASTQ Groomer` are sound software engineering practices. The primary technical limitations lie in (1) how paired-end read synchrony is handled when `Filter FASTQ reads` or regex removal in `Manipulate FASTQ reads` is applied to paired-end datasets (where dropping one mate without dropping or routing its partner breaks mate-pair ordering for downstream aligners unless `FASTQ Joiner`/`Splitter` are used, which in turn fails on variable-length reads), and (2) the ausencia of runtime throughput and memory benchmarks to substantiate the claim of having *"no known data size limitations"* for a pure-Python implementation.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`FASTQ Groomer` accurately validates and interconverts between divergent FASTQ variants (`Sanger`, `Solexa`, `Illumina 1.3+`) while flagging user-selected encoding mismatches: [Well Supported].**  
  The tool validates conformity against the Cock et al. reference test suite (integrated into automated continuous regression testing; Section 3, line 38) and prints the observed ASCII character and decimal ranges alongside the list of compatible FASTQ variants (Section 2, line 21), enabling immediate detection of mis-specified input formats (e.g., ASCII `< 59` when `Solexa` was selected).

* **Column-wise summary statistics, offset-based trimming, and region-aggregated quality filtering provide a flexible, code-free read QC workflow: [Well Supported].**  
  Computing per-base-position minimums, maximums, means, quartiles, and nucleotide frequencies (`FASTQ Summary Statistics by column`) followed by absolute or percentage-based $5'/3'$ trimming (`FASTQ Trimmer by column`) and configurable regional quality aggregation (`Filter FASTQ reads`) covers the core preprocessing operations required prior to short-read mapping.

* **`FASTQ Joiner` and `FASTQ Splitter` reliably manage paired-end read files across sequencing workflows: [Moderately Supported].**  
  In Section 2 (line 31), the authors state that `FASTQ Joiner` concatenates paired-end reads from two separate files into a single entry, while `FASTQ Splitter` *"takes a single FASTQ file and splits each read in half, creating two separate FASTQ files."* Splitting a concatenated read *"in half"* only recovers the original forward and reverse mates if both mates have **identical lengths**. If one mate was trimmed to a different length prior to joining (or originates from a variable-length platform or trimmed adapter workflow), splitting at the $50\%$ midpoint shifts bases from the longer mate into the shorter mate and corrupts the read boundary. Furthermore, the note does not clarify whether `Filter FASTQ reads` preserves mate-pair synchronization when applied to separate forward and reverse FASTQ files without prior concatenation.

* **The Python-based toolkit has "no known data size limitations" (Introduction, line 14): [Overstated].**  
  While streaming line-by-line parsing in Python avoids $O(N)$ memory exhaustion, pure-Python regular expression matching, character-by-character Phred/Solexa math in `FASTQ Groomer`, and per-column quartile/outlier accumulation across tens or hundreds of millions of Illumina reads incur substantial CPU walltime (and memory overhead if per-column arrays are held in RAM for `Summary Statistics`). No walltime or memory scaling numbers (e.g., MB/s or minutes per $10^7$ reads) are reported in the manuscript.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Document Paired-End Synchrony Requirements and Variable-Length Mate Handling in `FASTQ Joiner` / `Splitter`
* **WHY:** If users apply `Filter FASTQ reads` or length-altering regex trimming independently to forward (`/1`) and reverse (`/2`) FASTQ files, mates will become desynchronized; conversely, if they join two variable-length or unequally trimmed mates with `FASTQ Joiner` and later run `FASTQ Splitter` (which splits each concatenated read *"in half"*), the mate boundary will be corrupted.
* **WHAT:** Clarify in Section 2 (line 31) how paired-end synchronization is maintained during quality filtering and warn against using `FASTQ Splitter` on unequal-length mates.
* **HOW:** State explicitly that (a) to filter paired-end reads without losing mate pairing, users must join the equal-length forward and reverse reads with `FASTQ Joiner` first, apply `Filter FASTQ reads` (using $0\text{--}50\%$ and $50\text{--}100\%$ percentage offsets for mate 1 and mate 2), and then split them with `FASTQ Splitter`, and (b) `FASTQ Splitter` requires both concatenated mates to have equal length.

#### 2. Report Empirical Throughput and Memory Benchmarks on a Standard Multi-Million-Read FASTQ File
* **WHY:** Claiming *"no known data size limitations"* without reporting processing speed (reads/sec) or peak RAM usage leaves users unable to gauge whether grooming and summarizing a full Illumina lane ($>20\text{--}100$ million reads) takes minutes or days.
* **WHAT:** Add a brief benchmark sentence or table reporting walltime and peak memory for `FASTQ Groomer`, `FASTQ Summary Statistics by column`, and `Filter FASTQ reads` on a standard dataset (e.g., $10^7$ 36-bp or 100-bp reads).
* **HOW:** Time the Python tools on a single CPU core for $10^6$ and $10^7$ reads, and specify whether `FASTQ Summary Statistics by column` computes exact quartiles in memory or uses bounded histograms across base positions.

#### 3. Clarify Color-Space (`AB SOLiD`) Adapter Base Handling During Trimming and Grooming
* **WHY:** Section 2 (line 29) mentions color-space sequence manipulation (changing the leading primer/adapter base), and `FASTQ Trimmer` (line 25) trims $5'$ and $3'$ ends. In AB SOLiD color-space FASTQ files, the first character of the sequence string is a nucleotide primer base followed by di-base color transitions (`0123`), so $5'$ trimming or reverse-complementing requires special offset handling to avoid desynchronizing the quality string length from the transition string.
* **WHAT & HOW:** Add one sentence in Section 2 clarifying how `FASTQ Groomer` and `FASTQ Trimmer` handle the leading primer base and quality-string length offset in color-space (`csfastq`) files.
