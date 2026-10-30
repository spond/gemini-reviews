# Review of AN_ANON_004

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound)  
**Scientific Core Score:** **5.8 / 8.0**  
* **Score Breakdown:** Rigor: 2.4/3.5 | Claims: 1.9/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript is a comprehensive methodological protocol unit introducing experimental biologists to web-based genomic data manipulation, interval intersection, and workflow automation using the public `[WORKFLOW_PLATFORM]` (Galaxy) server. Structured as five progressive Basic Protocols and four Support Protocols (accompanied by online video screencasts), the paper walks users through: (1) intersecting human TAF1 binding intervals (`TAF1_CHiP.txt` on assembly `hg18`) with 1,000 bp upstream flanking regions of RefSeq genes and visualizing custom tracks in the UCSC Genome Browser; (2) identifying coding exons on chromosome 22 (`UCSC Genes`) containing $\ge 10$ single nucleotide polymorphisms (`dbSNP build 129`) via interval joins, grouping/counting, sorting, filtering, and relational key joins; (3) saving and sharing histories, extracting reusable workflows from an analysis history, modifying filter parameters ($\ge 50$ SNPs), and re-executing the workflow on chromosome X; (4) constructing a de novo workflow in the graphical Workflow Editor to compute BED interval lengths (`c3 - c2`), sort, and extract the 50 longest intervals; and (5) fetching FASTA sequences and stitching 5-way MultiZ whole-genome alignment blocks (`Extract MAF blocks` and `Stitch MAF blocks`) across the 109 high-SNP exons on chromosome 22. Example input files (`TAF1_CHiP.txt`) and screencast URLs are provided.

As an instructional protocol resource, the unit succeeds in translating multi-step relational and genomic interval operations into clear, reproducible browser steps that require no command-line programming. However, several bioinformatic and biological pitfalls are embedded in the illustrative protocols without warning to novice users: (1) Basic Protocol 1 defines promoters strictly as 1,000 bp *upstream* flanks (`Get flanks`) outside the transcribed RefSeq coordinates, which excludes the transcription start site (TSS) and 5' untranslated region where TFIID/TAF1 actually binds; (2) Basic Protocol 2 ranks exons by raw SNP count (`c2 >= 10`) without normalizing by exon length or collapsing redundant alternative-splice isoforms in the `UCSC Genes` track, confounding polymorphism enrichment with exon length and isoform multiplicity; and (3) several step instructions omit critical non-default parameter selections (such as numerical descending sort order in Basic Protocol 4) while instructing readers to leave unmentioned options at their defaults. Addressing these bioinformatic caveats will make the protocols substantially more rigorous for experimentalists applying them to their own research data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The `[WORKFLOW_PLATFORM]` history and workflow engine captures step-by-step tool parameters and enables point-and-click conversion of interactive analyses into reusable, shareable pipelines: [Well Supported].**  
  Basic Protocols 2–4 and Support Protocols 2.1–3.3 concretely demonstrate how an interactive seven-step analysis on `chr22` can be converted into a parameterized workflow, edited in the graphical canvas, shared via URL or user account, and re-executed on `chrX` inputs without re-specifying intermediate joins or column cuts.

* **Basic Protocol 5 reliably extracts and stitches fragmented local MultiZ MAF blocks into per-exon projected ("pseudo-global") multi-species FASTA alignments: [Well Supported].**  
  The two-stage procedure (`Extract MAF blocks` retrieving 387 local alignment blocks overlapping the 109 exons, followed by `Stitch MAF blocks` projecting them onto the 109 human reference intervals to yield 545 sequences across 5 mammals) accurately handles fragmented local alignments and missing orthologous sequence blocks.

* **Basic Protocol 1 accurately identifies gene promoters bound by TAF1 from a ChIP experiment: [Moderately Supported].**  
  While the interval intersection mechanics work as intended, there are two domain-level caveats:
  1. *Exclusion of the TSS and 5' leader region:* Step 4 uses `Get flanks` with `Length = 1000` upstream of the `Whole Gene` RefSeq coordinates. Because TAF1 ($\text{TBP}$-associated factor 1, the largest subunit of the core general transcription factor TFIID) binds directly across the initiator/downstream promoter element ($[-200\text{ bp}, +200\text{ bp}]$ relative to the TSS), taking only the $[-1000\text{ bp}, -1\text{ bp}]$ upstream flank discards TAF1 binding peaks located immediately downstream of the annotated +1 TSS. Defining promoters as $[-1000\text{ bp}, +200\text{ bp}]$ around the 5' start site (`Around Start`) is biologically much more appropriate for TAF1 and RNA Polymerase II ChIP datasets.
  2. *Assay attribution:* The text repeatedly refers to the Kim et al. dataset (`TAF1_CHiP.txt`) as a "CHiP-seq experiment" (lines 50, 78–85, 91), whereas the classic Kim et al. human fibroblast TAF1 dataset was generated by high-density tiling microarray (**ChIP-chip**, not ChIP-seq).

* **Basic Protocol 2 identifies coding exons with the highest polymorphism burden on chromosomes 22 and X: [Fragile].**  
  As a biological query, ranking exons by raw SNP count (`c2 >= 10` on `chr22` or `c2 >= 50` on `chrX`) has three unacknowledged confounders:
  1. *Confounding by exon length:* Raw SNP count scales linearly with exon length. Terminal coding exons can exceed 2–5 kb whereas internal coding exons average ~130 bp; filtering on `c2 >= 10` primarily selects the longest exons rather than exons with high SNP density (SNPs per kb).
  2. *Transcript isoform multiplicity in `UCSC Genes`:* Exporting `Coding Exons` from the `UCSC Genes` track outputs separate BED rows for every alternative transcript isoform sharing the same chromosomal exon, and `dbSNP (129)` contains multi-bp indels/duplications alongside true SNPs. Counting rows grouped by `c4` without collapsing unique genomic exon coordinates or deduplicating `(exon_id, snp_id)` pairs inflates counts when multiple SNP records or overlapping transcript annotations exist.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Include Downstream TSS Window ($[-1000, +200]$) or Warn Users About TSS-Overlapping Factors in Basic Protocol 1
* **WHY:** In Basic Protocol 1 (lines 141–153), `Get flanks` creates strictly upstream intervals $[-1000, -1]$ that stop 1 bp before the RefSeq TSS, missing TAF1 peaks centered on or immediately downstream of the TSS. Furthermore, line 89 instructs users to leave unmentioned dropdowns at default values, but `Get flanks` requires explicit verification of `Region` (`Whole feature` vs. `Around Start`) and `Location` (`Upstream` vs. `Both`).
* **WHAT:** Explicitly specify the `Region` and `Location` dropdown settings in Step 4 of Basic Protocol 1, and add an instructional note explaining how to capture $[-1000, +200]$ windows around the TSS.
* **HOW:** In Basic Protocol 1, Step 4 (lines 145–151), explicitly state the settings for `Region` and `Location of the flanking region/s`, and add a short note explaining that for core promoter factors like TAF1/Pol II that bind across the TSS, users can either select `Around Start` or extend the flank downstream into the 5' UTR.

#### 2. Add a Length-Normalization Note (SNP Density vs. Raw Count) and Isoform Caveat to Basic Protocol 2
* **WHY:** Experimentalists adapting Basic Protocol 2 to find hyper-polymorphic or hyper-mutated exons will be misled if they filter on raw SNP counts (`c2 >= 10`) instead of length-normalized SNP density ($\text{SNPs} / \text{bp}$), or if they do not realize that `UCSC Genes` contains redundant exon rows across alternative splice isoforms.
* **WHAT:** Add a paragraph in the Basic Protocol 2 commentary (or an optional `Compute` step after Step 7) showing how to divide the SNP count by exon length (`c3 - c2`) to obtain SNP density per kilobase, and caution users about transcript isoform redundancy in `UCSC Genes`.
* **HOW:** After Step 7 of Basic Protocol 2 (line 341), note that `Dataset #7` now contains both the exon coordinates (`c2`, `c3`) and the SNP count (`c8`), so running `Text Manipulation -> Compute` with the expression `c8 / (c3 - c2) * 1000` yields the length-normalized SNP density per kb.

#### 3. Explicitly Specify Sort Type and Sort Order Parameters in Basic Protocol 2 (Step 5) and Basic Protocol 4 (Step 12)
* **WHY:** Line 89 states: *"If other menus and options are not referenced, leave those settings in their default or existing condition."* In Basic Protocol 2 (lines 307–313) and Basic Protocol 4 (lines 568–574), the instructions tell the user to select `Sort` and set `on column` to `c2` or `7`, without specifying `Flavor` (`Numerical sort` vs. `Alphabetical sort`) or `Order` (`Descending` vs. `Ascending`). If `Alphabetical sort` or `Ascending` order is used in Basic Protocol 4 before `Select first 50`, the workflow will return the 50 *shortest* (or lexicographically sorted) intervals instead of the 50 *longest* intervals.
* **WHAT:** Explicitly instruct the user to set `Flavor` to `Numerical sort` and `Order` to `Descending order` in both Basic Protocol 2 (Step 5) and Basic Protocol 4 (Step 12).
* **HOW:** Add a sub-bullet in Basic Protocol 2 (after line 311) and Basic Protocol 4 (after line 572): *"Make sure 'with flavor' is set to 'Numerical sort' and 'everything in' is set to 'Descending order'."*

#### 4. Technical and Editorial Cleanup
* **WHY:** Minor capitalization, figure-placeholder, and terminology inconsistencies remain in the manuscript text.
* **WHAT & HOW:**
  1. *ChIP Capitalization and Assay Type (lines 50, 75, 78–85, 91, 95, 99, Screencast 1):* Replace `"CHiP-seq"` with `"ChIP-seq"` (or `"ChIP-chip"` when referring specifically to the Kim et al. tiling array dataset `TAF1_CHiP.txt`).
  2. *Production Note Left in Text (line 491):* Remove the literal placeholder text `"Insert Figure 9 here."` at the end of the Basic Protocol 4 introduction paragraph.
  3. *Missing Punctuation / Unclosed Quote (line 554):* In `"Click 'Text Manipulation' from the Tools menu on the left and then 'Select first lines from a Query in the left panel."`, close the quotation mark after `"Select first lines from a Query"`.
