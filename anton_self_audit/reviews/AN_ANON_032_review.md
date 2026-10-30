# Review of AN_ANON_032

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.9 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This protocol manuscript provides five step-by-step tutorials demonstrating how experimental biologists can perform web-based genomic and high-throughput sequencing analyses without command-line programming: (1) Basic Protocol 1 joins human chromosome 22 RefSeq coding exons (`hg19`) with common SNPs (`snp132Common`) from the UCSC Table Browser to identify the top 100 exons with the most overlapping SNPs; (2) Basic Protocol 2 demonstrates importing ENCODE mouse ChIP-seq FASTQ files (`mm9`, chr19) from shared data libraries and uploading MPromDB promoter annotations via FTP, followed by column manipulation and conversion to Interval and BED6 formats; (3) Basic Protocol 3 walks through ChIP-seq FASTQ quality score grooming (`FASTQ Groomer`), short-read alignment (`Bowtie`), and CTCF peak calling (`MACS`); (4) Basic Protocol 4 illustrates genomic interval operations (`Intersect`, `Subtract`, `Concatenate`, `Merge`, `Base Coverage`, `Coverage`, `Complement`, `Cluster`, and `Join`) comparing chr22 coding exons against RepeatMasker (`rmsk`) transposable elements; and (5) Basic Protocol 5 extracts and formats multi-species alignments (`46-way multiZ MAF`) across 10 primate species using `Extract MAF blocks`, `MAF Coverage Stats`, and `Stitch Gene blocks`. Companion screencasts, example data libraries, and published workflows are hosted online.

As an educational and practical resource, the manuscript clearly explains histories, metadata management, genomic coordinate formats, and multi-step workflow construction. However, the protocols contain one primary analytical flaw in Basic Protocol 1 and several step-by-step execution bugs across Basic Protocols 1, 2, 4, and 5 that will cause users following the text literally to obtain incorrect results or encounter errors: (1) Basic Protocol 1 claims to identify the 100 coding exons with the *"highest SNP density"*, but it ranks exons by the **raw count** of overlapping SNPs without dividing by exon length, and it groups by column 4 (`c4`, the RefSeq transcript/exon identifier in uncollapsed UCSC `refGene` BED output), which conflates exon length and overlapping alternative transcript isoforms with SNP density; and (2) several procedural steps are omitted or mislabeled in the text (e.g., missing track-switching instructions when fetching `snp132Common` in Basic Protocol 1, omitted tool parameters for splitting `chromosome:start..stop` in Basic Protocol 2, naming the history `"Basic Protocol 3"` instead of `"Basic Protocol 4"` in Basic Protocol 4, and a malformed Python quote string in Basic Protocol 5). Fixing these protocol steps and normalizing SNP counts by exon length will make all five tutorials reproducible and analytically sound.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Basic Protocol 1 identifies the 100 human coding exons on chromosome 22 with the highest SNP density: [Methodologically Flawed].**  
  Basic Protocol 1 is titled *"FINDING HUMAN CODING EXONS WITH HIGHEST SNP DENSITY"* and states in the text that sorting by the `Count` output yields *"a list of the 100 exons with the highest SNP density"* (lines 43, 45, 149, 169). However, the protocol joins exons (`Exons hg19 chr22`) with SNPs (`SNPs hg19 chr22`) and counts occurrences of column 4 (`c4`) without dividing by exon length ($L = \text{end} - \text{start} = c_3 - c_2$). Ranking by raw SNP count selects the *longest* exons (e.g., large terminal coding exons spanning several kilobases) rather than the exons with the highest SNP density (SNPs per bp or per kb). Furthermore, in the UCSC `refGene` table, alternative transcript isoforms of the same gene produce multiple redundant rows for the same genomic exon (or share transcript-derived identifiers in column 4), causing exons belonging to genes with many RefSeq splice isoforms to be duplicated in the top 100 list and inflating join counts when joining back on `c4` in Step 19 (`Compare two datasets`).

* **Basic Protocol 2 accurately converts custom MPromDB promoter coordinates (`chr:start..stop`) into standard Interval and BED6 formats: [Moderately Supported].**  
  The conceptual workflow—splitting `chr:start..stop` into three columns, pasting them onto the original table, assigning Interval metadata, and cutting columns into BED6 order (`chr, start, end, name, score, strand`)—is valid, though MPromDB 1-based start coordinates converted via text splitting without subtracting 1 from the start position differ by 1 bp from UCSC 0-based half-open BED conventions. In addition, the step-by-step instructions in lines 279–288 state only the intermediate outputs (*"The resulting dataset contains only one column..."*, *"The output dataset has two columns..."*) while omitting the exact tool names and parameters (`Cut`, `Convert delimiters to TAB`, `Paste`) required to perform those four transformations.

* **Basic Protocol 3 demonstrates an end-to-end ChIP-seq peak-calling pipeline using FASTQ Groomer, Bowtie, and MACS on mouse chr19 CTCF data: [Well Supported].**  
  The protocol provides a clear, reproducible walkthrough of format standardization (`FASTQ Groomer`), alignment to `mm9` (`Bowtie`), and peak calling (`MACS` with control input). As a best-practice note for users, running Bowtie with `-y` ("Try hard") without setting `-m 1` retains randomly placed multi-mapping reads in repetitive regions, and subsetting reads to `chr19` reduces the pool of high-confidence peaks (`MFOLD=32`) available for MACS paired-peak shift estimation.

* **Basic Protocols 4 and 5 demonstrate genomic interval set operations (`bx-python`) and multi-species MAF alignment extraction and coverage summarization: [Well Supported].**  
  Basic Protocol 4 clearly contrasts whole-interval vs. piece-wise `Intersect` and `Subtract`, `Concatenate` + `Merge`, `Base Coverage`, `Coverage`, `Complement`, `Cluster`, and inner/outer `Join` operations on chr22 exons and repeats. Basic Protocol 5 effectively demonstrates extracting primate MAF blocks, computing per-region and per-species alignment coverage, and stitching coding blocks into species-specific FASTA files.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Normalize SNP Counts by Exon Length and Deduplicate Overlapping Exon Isoforms in Basic Protocol 1
* **WHY:** Counting raw SNPs per exon without dividing by exon length ($\text{end} - \text{start}$) measures total SNP count (driven by exon size) rather than SNP density (SNPs per base pair), and UCSC `refGene` exports duplicate exons across alternative transcript isoforms.
* **WHAT:** Either (a) add a `Compute` step (`Text Manipulation -> Compute an expression on every row`) to divide the SNP count by exon length (`c5 / (c3 - c2)`) after deduplicating exon coordinates, or (b) simpler yet, replace the `Join` + `Count` + `Compare two datasets` steps with the `Coverage` tool (`Operate on Genomic Intervals -> Coverage`, already taught in Basic Protocol 4!), which directly appends both the SNP count and the length-normalized density fraction to every exon in a single step while preserving all 6 BED columns.
* **HOW:** In Basic Protocol 1, after importing `Exons hg19 chr22` and `SNPs hg19 chr22`, run `Operate on Genomic Intervals -> Coverage` with `"What portion of" = Exons hg19 chr22` and `"is covered by" = SNPs hg19 chr22`. Then sort descending on column 8 (fraction of exon bases covered by SNPs, i.e., true SNP density) using `Filter and Sort -> Sort`, and take the top 100 with `Select first`. This eliminates 4 intermediate steps, preserves BED coordinates/strand automatically, and computes true SNP density.

#### 2. Restore Missing Step-by-Step Instructions in Basic Protocols 1 and 2
* **WHY:** Users following Basic Protocol 1 (lines 117–127) and Basic Protocol 2 (lines 279–288) cannot reproduce the outputs because key UI actions were omitted from the text.
* **WHAT & HOW:**
  * **Basic Protocol 1, Step 7 (lines 117–127):** Between clicking `"UCSC Main"` (line 117) and clicking `"get output"` (line 119), the text omits the instruction to change `"group:"` to `"Variation and Repeats"` and `"track:"` to `"Common SNPs(132)"` (and in line 123 it erroneously instructs the user to *"Select the 'Whole Gene' radio button"*, which belongs to the `refGene` track rather than `snp132Common`). Replace line 123 with the correct UCSC Table Browser track selection for `snp132Common` (`output format: BED - browser extensible data`, then `"Send query to [SOFTWARE]"`).
  * **Basic Protocol 2, Step 6 (lines 279–288):** Insert the explicit tool calls that split column 2 (`chr19:start..stop`) into three tab-delimited columns: (i) `Text Manipulation -> Cut columns from a table` (`Cut columns: c2`), (ii) `Text Manipulation -> Convert delimiters to TAB` (converting `:` and `.` to tabs), and (iii) `Text Manipulation -> Paste two files side by side` to prepend the 3 coordinate columns to the original 10 columns.

#### 3. Note Best Practices for Multi-Mapping Reads in Basic Protocol 3
* **WHY:** In ChIP-seq peak calling, retaining multi-mapping reads without a uniqueness filter (`-m 1` in Bowtie) can produce false-positive CTCF peaks over repetitive elements.
* **WHAT & HOW:** Add a brief note in Basic Protocol 3 (Step 5, lines 453–460) explaining that for production ChIP-seq analyses, setting Bowtie's `"Suppress all alignments for a read if more than n reportable alignments exist (-m):"` to `1` and enabling MACS duplicate removal prevents repeat-driven peak artifacts.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several typos in history names, filter expressions, and regular expressions will cause execution failures when users copy-paste them.
* **WHAT & HOW:**
  * **Basic Protocol 4, Step 1b vs. Step 2d (lines 557, 567):** Line 557 instructs the user: *"Name the new history by clicking on the text 'Unnamed History' and entering 'Basic Protocol 3'"*, and then line 567 instructs them: *"Under the 'Destination History' pulldown select 'Basic Protocol 4'"*. Correct line 557 to `'Basic Protocol 4'`.
  * **Basic Protocol 5, Part C, Step 8d (lines 953–955):** The filter condition is printed as `"len(c2.replace('-', ")) > 0"`, where the two single quotes `''` inside `replace('-', '')` were collapsed into a single double-quote character `"`, which causes a Python syntax error. Change to `len(c2.replace('-', '')) > 0`.
  * **Basic Protocol 5, Figure 10.5.36 legend (line 1009):** Correct `"start with 'rheMac.'"` to `"start with 'rheMac2.'"`, matching the regex `^rheMac2\.` in line 963.
  * **Basic Protocol 4 (line 543):** Fix the institution typo `"Penn Sate University"` to `"Penn State University"`.
