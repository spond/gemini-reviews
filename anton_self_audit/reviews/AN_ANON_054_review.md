# Review of AN_ANON_054

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.5 / 8.0**  
* **Score Breakdown:** Rigor: 2.7/3.5 | Claims: 2.2/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This software application note presents an open-source Python toolset (built on `bx-python` and integrated into both a command-line interface and a public web-based workflow platform) for querying, converting, filtering, and stitching whole-genome multiple sequence alignments stored in Multiple Alignment Format (MAF). To handle multi-hundred-gigabyte alignments (such as the 28-way mammalian and 46-way vertebrate UCSC datasets) without manual scripting, the suite implements compressed positional-binning disk indexes, automatic reconciliation of MAF reverse-complement negative-strand coordinates into standard 0-based half-open (`BED`) intervals, interval-based block extraction, `MAF`-to-`FASTA` conversion, species filtering and adjacent block joining, attribute-based block filtering, interval coverage summaries, and `MAF` stitchers for standard genomic intervals and `BED12` protein-coding gene models. Source code is released under the Academic Free License, and a live online supplement provides interactive histories and workflows.

The toolset solves a genuine practical barrier in comparative genomics—specifically the error-prone handling of negative-strand coordinate numbering in MAF files and random-access extraction from hundred-gigabyte multi-chromosome alignment archives. However, as a software note, the manuscript has two notable omissions: first, it provides no quantitative performance benchmarks (index construction time, compressed disk footprint, or query execution time and peak RAM when extracting genome-wide gene sets from the 28-way or 46-way MAF archives); second, the `BED12` protein-coding stitcher discards insertions in non-reference species while retaining deletions relative to the reference genome, which can introduce artificial frameshifts in non-reference coding sequences when compensatory indels occur within an exon. Both points can be addressed with a small benchmark table and explicit documentation/options for codon-frame handling.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The toolset provides an accessible, reproducible GUI and CLI workflow for extracting, filtering, and converting whole-genome MAF alignments while transparently resolving negative-strand coordinate conventions: [Well Supported].**  
  The software architecture directly addresses the mismatch between MAF's reverse-complement `-` strand coordinate system and standard genomic interval formats (`BED`/`GFF`), and exposes all eight core operations (`Extract`, `MAF to FASTA`, `MAF to Interval`, `Stitch`, `Filter species`, `Join by species`, `Filter by attributes`, and `Coverage Stats`) through both CLI scripts and reproducible web workflows.

* **Positional-binning indexes over compressed MAF chunks enable scalable extraction from hundred-gigabyte vertebrate alignments: [Moderately Supported].**  
  While the indexing architecture (positional binning paired with compressed block lookup tables across the 49 chromosome-partitioned MAF files of the 28-way alignment) is sound and well-established, the manuscript reports no empirical timing, memory, or compression ratios to quantify scalability for end users.

* **The `BED12` MAF stitcher generates ready-to-use concatenated protein-coding gene alignments across species by projecting onto the reference sequence and resolving block overlaps via alignment scores: [Moderately Supported].**  
  Projecting onto reference genomic positions (discarding non-reference insertions) and resolving overlapping MAF blocks per species by total block score produces a clean 1-to-1 coordinate mapping relative to the reference species. However, in protein-coding exons (`BED12`), discarding a non-reference insertion (e.g., +1 bp) while keeping a nearby compensatory deletion (-1 bp) in the same non-reference species shifts the reading frame for that species downstream of the indel. Furthermore, selecting fragments from overlapping blocks solely by whole-block score on a per-species basis can stitch paralogous or non-syntenic alignment fragments into a single chimeric sequence if synteny filtering is not applied beforehand.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add Quantitative Runtime, Memory, and Disk-Footprint Benchmarks on the 28-Way and 46-Way MAF Datasets
* **WHY:** The introduction motivates the toolset by citing the hundred-gigabyte scale and millions of blocks in the 28-way mammalian and 46-way vertebrate alignments, but the text contains zero quantitative performance data.
* **WHAT:** Include a compact benchmark table reporting wall-clock runtime, peak memory usage, and disk footprint for common operations on the 28-way and 46-way MAF sets.
* **HOW:** Measure and report (1) uncompressed vs. compressed MAF + index + lookup table disk size, (2) on-the-fly index generation time for a user-uploaded 1 GB MAF file, and (3) execution time to extract and stitch all human RefSeq protein-coding genes (~20,000 `BED12` records) from the cached 28-way and 46-way alignments.

#### 2. Document and Mitigate Frame-Shift Artifacts in the `BED12` Protein-Coding Stitcher
* **WHY:** In Section 2 (line 33), the `BED12` stitcher discards insertions in aligning species relative to the reference species while keeping reference-relative deletions (as gaps). When a non-reference species carries a non-triplet insertion (discarded) paired with a nearby compensatory deletion (retained), or when an exon boundary shifts by 1–2 nt in a non-reference lineage, projecting strictly onto reference coordinates introduces false frameshifts and premature stop codons in downstream codon models (`dN/dS`).
* **WHAT:** Warn users in the text and tool help interface about reference-projection frameshifts in coding alignments, and explain how to pair the `BED12` stitcher with synteny filtering and reading-frame validation.
* **HOW:** Add a note in Section 2 explaining that (1) users should run `Filter MAF by specified attributes` (enforcing syntenic chromosomes/strands) prior to stitching when paralogous overlapping blocks are present, and (2) when non-reference insertions are discarded during `BED12` stitching, downstream codon-aware analyses should mask out-of-frame segments or retain frame-preserving triplet gaps.
