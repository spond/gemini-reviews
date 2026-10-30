# Review of AN_ANON_039

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.5 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.0 / 8.0**  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.6/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript is an abridged or condensed version of a five-part bioinformatics protocol unit ("Basic Protocols 1–5") introducing experimental biologists to web-based genomic data acquisition, interval manipulation, ChIP-seq peak calling, and multiple sequence alignment extraction. The five protocols cover: (1) identifying the top 100 human chromosome 22 RefSeq protein-coding exons (`hg19`) overlapping the largest number of `dbSNP` build 134 variants; (2) loading mouse chromosome 19 ENCODE ChIP-seq data (`mm9`) from shared libraries and uploading external promoter annotations (`MPromDB`) via FTP to convert them into `Interval` and `BED6` formats; (3) running `FASTQ Groomer`, `Bowtie`, and `MACS` to call CTCF ChIP-seq binding peaks on mouse chromosome 19; (4) executing `bx-python` genomic interval operations (`Intersect`, `Subtract`, `Concatenate`, `Merge`, `Base Coverage`, `Coverage`, `Complement`, `Cluster`, and `Join`) between human chromosome 22 exons and transposable elements (`RepeatMasker`); and (5) extracting primate multiple alignment blocks (`Extract MAF blocks`), conservation coverage statistics (`MAF Coverage Stats`), and stitched coding-region FASTA sequences (`Stitch Gene blocks`) for rhesus macaque (`rheMac2`) from the UCSC 46-way `multiZ` track. Live histories, workflows, and video screencasts are hosted on a public web server.

While the overarching pedagogical design and online companion resources ("Using Galaxy: A live supplement") are well conceived, the text of this manuscript is severely truncated across all five protocols, omitting the majority of the actual numbered procedural steps while retaining only isolated fragments and figure legends. For example, Basic Protocol 1 stops at Step 4 (*"Click Statistics in the Tools panel"*, line 57) before the `Join`, `Count`, `Sort`, `Select first`, and `Compare two datasets` operations are ever described, even though Basic Protocol 5 (lines 169–179) subsequently instructs the user to import the output of *"Basic Protocol 1, step 20: top 100 SNP containing human coding exons"*. Similarly, Basic Protocol 2 stops at Step 3 (naming the history, line 91) and omits Step 4 entirely, yet Basic Protocol 3 (line 117) requires *"Results from Basic Protocol 2, step 4"*, and the Troubleshooting section (line 277) refers to *"Basic Protocol 2, step 6"*. Beyond this structural truncation, Basic Protocol 1 conflates raw SNP counts per exon with length-normalized *SNP density* ($\text{SNPs/bp}$). Restoring the missing numbered procedure steps across Protocols 1–5 and normalizing SNP counts by exon length are necessary to make the document self-contained and methodologically sound.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The web platform's history system, metadata editor, and workflow manager provide an accessible framework for reproducible browser-based genomic analysis: [Well Supported].**  
  The Introduction, Commentary, and live supplement links clearly explain how datasets, genome build metadata, and multi-step tool chains are tracked, shared, and re-executed without Unix command-line administration.

* **Basic Protocols 1–5 provide complete, self-contained step-by-step instructions that a reader can follow to reproduce the example analyses: [Methodologically Flawed].**  
  Every single protocol in the manuscript text is missing the core procedural steps required to produce its stated output, creating broken internal cross-references throughout the document:
  1. **Basic Protocol 1 (Lines 49–58):** Lists only five top-level clicks (login, click `Get Data`, click `UCSC Main`, click `Operate on Genomic Intervals`, click `Statistics`) and omits Steps 5–20 (configuring UCSC Table Browser queries for `refGene` and `snp132Common`, running `Join`, `Count`, `Sort`, `Select first 100`, and `Compare two datasets`). Yet Basic Protocol 5 (lines 169, 171, 179) repeatedly references *"Basic Protocol 1, step 20: SNP Coding Exons chr22"*.
  2. **Basic Protocol 2 (Lines 87–92):** Ends immediately after creating and naming `"Basic Protocol 2"` (Step 3), omitting Steps 4–6 (importing the ENCODE mouse ChIP-seq data library, uploading the `MPromDB` promoter file via FileZilla FTP, splitting `chr:start..stop` coordinates with `Cut`, and changing datatypes to `interval` and `bed`). Yet Basic Protocol 3 (line 117) requires *"Results from Basic Protocol 2, step 4"*, and Commentary (line 277) cites *"Basic Protocol 2, step 6"*.
  3. **Basic Protocol 3 (Lines 109–134):** Contains zero numbered procedural steps—only the introductory paragraph, materials list, and five figure captions (`Copy History`, `FASTQ Groomer`, `Bowtie`, `MACS`, and `HTML report`).
  4. **Basic Protocol 4 (Lines 151–156):** Lists only creating the `"Basic Protocol 4"` history and renaming `"Exons"`, omitting all instructions for retrieving `"Repeats"` and running `Intersect`, `Subtract`, `Concatenate`, `Merge`, `Coverage`, `Complement`, `Cluster`, and `Join`.
  5. **Basic Protocol 5 (Lines 202–238):** Retains only the species tables and three redundant lines (*"Click on Convert Formats in the left Tool panel to expand the list"* repeated twice at lines 233 and 235, followed by *"Click on 'FASTA manipulation'"* at line 237), omitting the `Extract MAF blocks`, `MAF Coverage Stats`, `Stitch Gene blocks`, `FASTA-to-Tabular`, `Filter`, and `Select` parameters.

* **Basic Protocol 1 identifies the 100 human coding exons with the "highest density of SNPs": [Methodologically Flawed].**  
  As shown by the tool sequence summarized in the Figure 10.5.6 caption (line 69: `Join (A), Count (B), Sort (C), Select first lines (D), and Compare two datasets (E)`) and the Basic Protocol 5 description (line 169: *"top 100 SNP containing human coding exons"*), the workflow ranks exons by the **unnormalized count of overlapping SNPs** rather than **SNP density** ($\text{SNP count} / \text{exon length in bp}$). Because human coding exons vary in length by more than two orders of magnitude (from $<50\text{ bp}$ to $>10\text{ kb}$), ranking by raw count selects the longest exons rather than those with the highest polymorphism density per nucleotide.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Restore the Missing Numbered Procedural Steps Across Basic Protocols 1–5
* **WHY:** Because the numbered substeps (e.g., Basic Protocol 1 Steps 5–20, Basic Protocol 2 Steps 4–8, all steps of Basic Protocol 3, Basic Protocol 4 Steps 3–12, and Basic Protocol 5 Steps 1–8) were stripped or omitted from the text while cross-references to them (`"Basic Protocol 1, step 20"`, `"Basic Protocol 2, step 4"`, `"Basic Protocol 2, step 6"`) remain in place, a reader cannot execute any of the five protocols from the manuscript text.
* **WHAT:** Re-insert the complete numbered step-by-step instructions and parameter settings for all five protocols.
* **HOW:** Restore the full procedural text for Basic Protocol 1 (Steps 1–20), Basic Protocol 2 (Steps 1–8), Basic Protocol 3 (Steps 1–7, including `FASTQ Groomer`, `Bowtie`, and `MACS` parameter values), Basic Protocol 4 (Steps 1–12), and Basic Protocol 5 (Parts A, B, and C, removing the duplicated `"Click on Convert Formats"` lines at 233–235).

#### 2. Normalize Exon SNP Counts by Exon Length to Compute True SNP Density in Basic Protocol 1
* **WHY:** Counting overlapping SNPs per exon (`Join` + `Count`) measures total SNPs per exon rather than SNP density ($\text{SNPs/bp}$), contradicting the protocol title (*"Finding Human Coding Exons with Highest SNP Density"*).
* **WHAT:** Compute the length-normalized SNP density (either via the `Coverage` interval tool or via `Text Manipulation -> Compute` dividing SNP count by $\text{end} - \text{start}$) before sorting and selecting the top 100 exons.
* **HOW:** Replace the `Join` + `Count` + `Compare two datasets` steps with `Operate on Genomic Intervals -> Coverage` (querying `Exons hg19 chr22` against `SNPs hg19 chr22`), which outputs every exon alongside the count of covered bases and the fraction of the exon covered by SNPs (density), and sort descending on the fraction column.

#### 3. Fix Residual Typographical Errors in the Text and Figure Captions
* **WHY:** Minor typos in regular expressions and prose reduce clarity.
* **WHAT & HOW:**
  1. **Figure 10.5.36 Caption (Line 255):** The caption states that the select string extracts lines starting with `"rheMac."`, whereas the Rhesus assembly build identifier in the table (lines 210 and 232) is `rheMac2` (`"^rheMac2\."`). Update `"rheMac."` to `"rheMac2."`.
  2. **Part B Caption (Line 227):** Fix the word transposition `"divided the by the total length"` to `"divided by the total length"`.
  3. **Acknowledgements (Line 283):** Remove spurious line-break hyphens in proper names (`"Ist-van Albert"` $\to$ `"Istvan Albert"`, `"France De-noeud"` $\to$ `"France Denoeud"`).
