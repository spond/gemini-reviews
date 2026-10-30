# Review of AN_ANON_004

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.1 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript is a step-by-step bioinformatics protocol unit introducing experimental biologists to interactive genomic analysis, workflow construction, and multi-species alignment extraction using the web-based `[SOFTWARE]` platform (`[WORKFLOW_PLATFORM]`). Structured into five Basic Protocols and four Support Protocols (accompanied by six online video screencasts), the tutorial walks users through: (1) intersecting human TAF1 ChIP-seq binding intervals with putative RefSeq gene promoters (1,000 bp flanking regions on hg18); (2) identifying coding exons on human chromosome 22 (and chromosome X) harboring the highest counts of dbSNP build 129 variants via interval joining, grouping, sorting, and filtering; (3) converting interactive analysis histories into reusable, editable, and shareable multi-step workflows; (4) building a workflow from scratch in the graphical editor to extract the 50 longest genomic intervals from a BED file; and (5) extracting human FASTA sequences and 5-way mammalian Multiz multiple alignment format (MAF) blocks stitched into per-exon pseudo-global alignments for the 109 high-SNP chr22 exons. Example input datasets (`TAF1_CHiP.txt`), UCSC Table Browser query instructions, and screencast URLs are provided.

Evaluated as an educational protocol and software tutorial rather than a hypothesis-testing primary study, the step-by-step instructions are clear, modular, and directly executable in a web browser. However, several bioinformatic and biological caveats in the worked examples are left unaddressed and can mislead novice experimentalists: Basic Protocol 2 ranks exons by raw SNP counts (`c2 >= 10`) without normalizing by exon length or accounting for overlapping alternative transcript isoforms in the UCSC Genes track; Basic Protocol 4 sorts BED interval lengths in ascending order by default unless descending order is specified; and Basic Protocol 5 stitches genomic MAF blocks across coding exons without preserving reading frame or handling reverse-strand complementation for downstream phylogenetic codon models. Addressing these concrete protocol pitfalls will substantially strengthen its pedagogical rigor.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`[SOFTWARE]` enables browser-based genomic interval intersection, tabular manipulation, and UCSC Genome Browser visualization without programming: [Well Supported].**  
  Basic Protocols 1 and 2 provide complete, verifiable UI sequences for uploading interval data, fetching hg18 RefSeq and dbSNP 129 annotations from the UCSC Table Browser, computing flanking regions, performing inner interval and key-column joins, and building UCSC custom tracks.

* **Analysis histories can be automatically converted into parameterized, reusable, and shareable workflows: [Well Supported].**  
  Basic Protocol 3, Support Protocols 3.1–3.3, and Basic Protocol 4 accurately demonstrate history-to-workflow extraction, canvas-based node wiring (`Input Dataset` $\rightarrow$ `Compute` $\rightarrow$ `Sort` $\rightarrow$ `Select first`), parameter modification (`c2 >= 50`), re-execution on chromosome X, and link-based sharing.

* **Basic Protocol 2 identifies the most polymorphic coding exons on chromosome 22 via raw SNP counts (`c2 >= 10`): [Fragile].**  
  Counting raw dbSNP entries overlapping each UCSC Genes coding exon record (`Group by column c4`, `Count on c4`) confounds SNP density (polymorphisms per kilobase) with exon length, and because the UCSC Genes track contains multiple overlapping isoform transcripts sharing identical coding exons under distinct transcript IDs (or conversely, multiple exons per transcript if `c4` stores the transcript ID rather than a unique exon ID), grouping on `c4` either double-counts shared exons or aggregates SNPs across entire multi-exon transcripts depending on how the UCSC BED export names records.

* **Stitched MAF alignments of coding exons (Basic Protocol 5) are directly "suitable for downstream analysis in most phylogenetic software packages": [Moderately Supported].**  
  While `Extract MAF blocks` followed by `Stitch MAF blocks` produces 109 five-species FASTA alignments (545 sequences), Multiz whole-genome alignments are anchored on the positive genomic strand and frequently contain frame-shifting indels or missing-species blocks padded with `-`. Without reverse-complementing minus-strand exons and enforcing in-frame codon alignment, feeding these stitched FASTA blocks directly into codon-based phylogenetic packages will produce corrupted reading frames on the negative strand.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Disambiguate Transcript vs. Exon Identifiers and Normalize by Exon Length in Basic Protocol 2
* **WHY:** When exporting `Coding Exons` as BED from the UCSC Table Browser (`UCSC Genes` track, Basic Protocol 2, Step 1), column 4 (`c4`) contains the UCSC transcript identifier (or `transcript_exon` label), and alternative isoforms share identical genomic exons. Furthermore, ranking exons by raw SNP count (`c2 >= 10`) selects long exons rather than exons with elevated polymorphism density.
* **WHAT:** Clarify what `c4` represents in the UCSC BED export, collapse duplicate genomic intervals, and demonstrate how to normalize SNP counts by exon length using the `Compute` tool.
* **HOW:** In Basic Protocol 2, after joining exons with SNPs, either group by genomic coordinates (`c1, c2, c3`) or add a `Compute` step (`SNP_count / (c3 - c2) * 1000`) after Step 7 (`Join two Queries`) to report SNPs per kilobase alongside raw SNP counts.

#### 2. Specify Sort Order and Column Type Explicitly in Basic Protocols 2 and 4
* **WHY:** In Basic Protocol 2 (Step 5) and Basic Protocol 4 (Step 8), the instructions state to set `Sort` `on column` to `c2` or `7` and click `Execute` to find the "highest SNP count" or "50 longest intervals." If the user does not verify that `Numerical sort` and `Descending order` are selected in the `Sort` tool parameters, lexicographical or ascending sorting will return the shortest intervals or misordered counts.
* **WHAT:** Explicitly state the sort type (`Numerical`) and order (`Descending`) in the step-by-step instructions.
* **HOW:** In Basic Protocol 2 (line 311) and Basic Protocol 4 (line 572), add a sentence instructing the user to ensure "Flavor" is set to "Numerical sort" and "Order" is set to "Descending".

#### 3. Clarify Upstream vs. Bidirectional Flanking in Basic Protocol 1 and Strand Handling in Basic Protocol 5
* **WHY:** In Basic Protocol 1 (Step 4), `Get flanks` is run on RefSeq genes with `Length of the flanking region/s` set to `1000` without specifying whether the user should select "Upstream" (5' of transcription start site, strand-aware) vs. "Both" or "Whole feature" vs. "Start". Similarly, in Basic Protocol 5 (Steps 3–5), extracting genomic DNA and stitching MAF blocks requires strand awareness so that minus-strand coding exons are reverse-complemented.
* **WHAT:** Document the exact `Region` and `Location of the flanking region` settings in `Get flanks` (Figure 4) and note how `Extract Genomic DNA` and `Stitch MAF blocks` handle the BED strand column (`c6`).
* **HOW:** Add explicit parameter selections in Basic Protocol 1 Step 4 (`Region: Whole feature`, `Location: Upstream`, `Length: 1000`) and a technical note in Basic Protocol 5 explaining that `Stitch MAF blocks` reverses and complements alignments for intervals annotated with `-` in the strand column when strand metadata is properly assigned.

#### 4. Technical and Editorial Cleanup
* **WHY:** Several minor formatting and placeholder artifacts remain in the manuscript text.
* **WHAT & HOW:**
  1. **Introduction & Basic Protocol 1:** Standardize the capitalization of `CHiP-seq` to `ChIP-seq` throughout the text (lines 50, 75, 78, 80, 85, 91, 99, 60).
  2. **Basic Protocol 4 (line 491):** Remove the production placeholder text `Insert Figure 9 here.` from the main paragraph.
  3. **Basic Protocol 4 (line 554):** Close the missing quotation mark in `"Select first lines from a Query"`.
  4. **Basic Protocol 5 (line 591):** Close the missing parenthesis in `(the result is sometimes called a "pseudo-global" alignment)`.
