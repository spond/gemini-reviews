# Review of AN_ANON_032

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.0 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.9/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript is a comprehensive methodological protocol and tutorial guide presenting five step-by-step bioinformatic workflows ("Basic Protocols 1–5") executed within a web-based genomic workbench. The protocols illustrate how experimental biologists can perform large-scale comparative and functional genomics without command-line programming: (1) intersecting human chromosome 22 RefSeq coding exons ($\sim 7,100$ intervals in `hg19`) with `dbSNP` (`snp132Common`, $\sim 170,000$ SNPs) to identify the 100 exons with the highest SNP counts; (2) importing legacy Illumina FASTQ files (`mm9` chr19 ENCODE CTCF ChIP-seq control and tag datasets) and converting custom promoter annotations from the Mammalian Promoter Database (`MPromDB`, $\sim 8,600$ promoters) into standard 6-column BED format; (3) grooming quality scores (`FASTQ Groomer`), aligning short reads with `Bowtie`, and calling CTCF binding peaks with `MACS`; (4) performing relational and set-theoretic genomic interval operations (`Intersect`, `Subtract`, `Concatenate`, `Merge`, `Base Coverage`, `Coverage`, `Complement`, `Cluster`, and `Join`) between human chr22 coding exons and `RepeatMasker` transposable elements ($\sim 75,000$ repeats); and (5) extracting primate multiple sequence alignment blocks (`46-way multiZ` MAF) and syntenic transcript FASTA sequences (`Stitch Gene blocks`) for rhesus macaque (`rheMac2`). All example datasets, shared data libraries, published workflows, and accompanying video screencasts are publicly hosted.

Evaluated as a primary educational resource and software protocol unit, the manuscript is logically structured, pedagogically clear, and grounded in authentic public genomic datasets (UCSC Table Browser, ENCODE, MPromDB, 46-way multiZ). However, several technical and quantitative flaws in the protocol steps should be corrected so that users do not adopt biased analytical habits. Most notably, Basic Protocol 1 promises in its title and introduction to identify coding exons with the *"highest SNP density"*, but the actual workflow ranks exons strictly by **raw SNP count per exon** without dividing by exon length, thereby confounding polymorphism density with exon size and duplicate RefSeq isoform intervals. Additionally, Basic Protocol 3 instructs users to set the `FASTQ Groomer` input quality score type to `"Sanger"` for a legacy Illumina dataset after stating in Basic Protocol 2 that the reads are in a *"legacy Illumina FASTQ format"*, and uses the whole-genome mouse effective size ($1.87 \times 10^9\text{ bp}$) in `MACS` on a pre-filtered chromosome 19 subset, which distorts the local/global Poisson background calculation.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Web-based history tracking, metadata assignment, and modular interval/alignment wrappers enable end-to-end reproducible execution of complex genomic queries without command-line scripting: [Well Supported].**  
  Protocols 1 through 5 thoroughly document every parameter, input/output format transformation (e.g., splitting `chr:start..stop` strings into 0-based `BED6` coordinates in Basic Protocol 2; converting multi-species `Stitch Gene blocks` output into filtered single-species `rheMac2` FASTA via `FASTA-to-Tabular` and regex filtering in Basic Protocol 5), and reusable workflow export.

* **Basic Protocol 1 identifies the 100 human chromosome 22 protein-coding exons with the "highest SNP density": [Methodologically Flawed].**  
  In Basic Protocol 1 ("Finding Human Coding Exons with Highest SNP Density"), the workflow joins `Exons hg19 chr22` ($\sim 7,100$ rows) with `SNPs hg19 chr22` ($\sim 170,000$ rows) to produce $\sim 4,800$ overlapping pairs, runs `Statistics -> Count` on column 4 (the RefSeq transcript/exon identifier), sorts descending by count, and selects the top 100 rows. There are two flaws in this procedure:
  1. **Raw Count vs. Length-Normalized Density:** Counting SNPs per exon without dividing by exon length ($\text{end} - \text{start}$) measures total SNP count, not SNP density ($\text{SNPs/bp}$). Long coding exons (e.g., terminal coding exons spanning several kilobases) naturally accumulate more SNPs under neutral evolution than short $100\text{-bp}$ exons even when their per-base SNP density is lower.
  2. **RefSeq Transcript Isoform Multiplicity (`column 4`):** In UCSC `refGene` BED exports of coding exons, column 4 stores the transcript accession plus exon suffix (e.g., `NM_XXXXXX_exon_Y_...`), and alternative transcript isoforms of the same gene share identical physical exons, or conversely, if gene/transcript names are shared across exons in certain table exports, grouping by column 4 without collapsing overlapping genomic coordinates (`chr`, `start`, `end`) either double-counts shared exons across isoforms or aggregates across distinct intervals.

* **Basic Protocol 3 demonstrates a best-practice ChIP-seq alignment and `MACS` peak-calling pipeline on `mm9` chromosome 19 CTCF data: [Moderately Supported].**  
  While the mechanics of running `FASTQ Groomer`, `Bowtie`, and `MACS` are clearly illustrated, two parameter choices conflict with the dataset description:
  1. Basic Protocol 2 (lines 233 and 241) explicitly states that `Control Chr19 ungroomed` and `Tags Chr19 ungroomed` are in a *"legacy Illumina FASTQ format"* (which historically used Phred+64 `Solexa`/`Illumina 1.3+` ASCII encoding) and therefore require grooming into standard Sanger Phred+33 format. However, Basic Protocol 3 (line 425) instructs the user to set `"Input FASTQ quality scores type:"` to `"Sanger"`. If the input file is genuinely legacy Illumina Phred+64, specifying `"Sanger"` as the input type fails to subtract 31 from the ASCII values, inflating base quality scores during `Bowtie -e 80` mismatch filtering.
  2. To speed up execution, the input FASTQ files were pre-filtered to reads mapping to chromosome 19 ($\sim 61.3\text{ Mb}$), yet the `MACS` step specifies `"Effective genome size:" = 1.87e+9` (the entire mouse genome). In `MACS`, the global background tag rate $\lambda_{\text{BG}} = N_{\text{tags}} \times d / G_{\text{eff}}$ scales inversely with $G_{\text{eff}}$; supplying a whole-genome $G_{\text{eff}}$ that is $\sim 30\text{-fold}$ larger than chr19 artificially depresses $\lambda_{\text{BG}}$ and inflates peak significance whenever local control coverage is sparse.

* **Basic Protocols 4 and 5 accurately demonstrate genomic interval algebra (`bx-python`) and multi-species alignment (`multiZ` MAF) extraction: [Well Supported].**  
  The distinction between returning whole overlapping intervals ($\sim 220$ exons) versus overlapping interval pieces ($\sim 250$ subregions) in `Intersect`, whole-interval vs. subregion `Subtract` ($\sim 7,000$ vs. $\sim 7,300$ regions), `Concatenate` + `Merge` ($\sim 82,000$ combined intervals flattened to $\sim 59,000$), `Base Coverage` ($\sim 17\text{ Mb}$), and `Cluster` ($\sim 13,500$ repeat clusters within $100\text{ bp}$) is mathematically exact and clearly explained.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Compute True Length-Normalized SNP Density in Basic Protocol 1
* **WHY:** Ranking exons by raw SNP count (`Count` on column 4) biases the top-100 list toward the longest exons rather than those with the highest polymorphism density per base pair.
* **WHAT:** Replace or augment the `Join` + `Count` steps in Basic Protocol 1 with the `Coverage` interval tool (introduced in Basic Protocol 4) or a `Text Manipulation -> Compute` step that normalizes SNP count by exon length.
* **HOW:** Instead of running `Join` followed by `Count`, either:
  1. Run `Operate on Genomic Intervals -> Coverage` with `"What portion of"` set to `Exons hg19 chr22` and `"is covered by"` set to `SNPs hg19 chr22` (which directly appends both the number of overlapping SNP bases and the fraction of the exon covered by SNPs as columns 7 and 8 without losing the BED coordinates in columns 1–6), and then `Sort` descending on column 8 (fraction/density); or
  2. After linking the exon coordinates back in Step 19, run `Text Manipulation -> Compute` with the expression `c7 / (c3 - c2)` (where `c7` is the SNP count and `c3 - c2` is exon length in bp) and sort on the resulting density column.

#### 2. Clarify Input Quality Encoding and Effective Genome Size in Basic Protocol 3
* **WHY:** Specifying `"Input FASTQ quality scores type: Sanger"` on a file described as *"legacy Illumina FASTQ format"* is confusing to learners, and using $G_{\text{eff}} = 1.87 \times 10^9$ on a single-chromosome dataset biases `MACS` Poisson $p$-values without an explanatory caveat.
* **WHAT:** Clarify the exact Phred offset of the shared library files (`Illumina 1.3-1.7` Phred+64 vs. `Sanger` Phred+33) and add a pedagogical note explaining the effect of `Effective genome size` on chromosome-subsetted tutorials.
* **HOW:** In Basic Protocol 3, Step 3d (line 425), if the UCSC ENCODE FASTQ file (`wgEncodeSydhTfbsMelCtcf...`) uses Sanger Phred+33 encoding, revise Basic Protocol 2 (lines 233/241) to clarify why grooming is still performed (e.g., wrapping/header standardization); if it uses legacy Phred+64 (`Solexa`/`Illumina 1.3+`), update Step 3d to select `"Illumina 1.3-1.7"`. In Step 5c (line 483), add a note stating that while $1.87 \times 10^9$ is the standard whole-genome parameter for `mm9`, restricting reads to `chr19` ($\sim 6.1 \times 10^7\text{ bp}$) in a tutorial setting alters the global background estimate unless scaled to the chromosome's mappable length ($\sim 5.0 \times 10^7\text{ bp}$).

#### 3. Fix Step-by-Step Typographical Errors and Missing Substeps
* **WHY:** Users following click-by-click instructions will encounter naming mismatches or missing tool selections where substeps were accidentally omitted during formatting.
* **WHAT & HOW:**
  1. **Basic Protocol 1 (Line 123):** When importing `snp132Common` from UCSC Table Browser, line 123 instructs the user to *"Select the 'Whole Gene' radio button"*, which is a copy-paste artifact from the `refGene` import; for a SNP track in BED format, the UCSC Table Browser displays `"all fields from selected table"` or `"BED - browser extensible data"` (with `"WholeFeature"`). Correct this label.
  2. **Basic Protocol 2 (Lines 280–287):** Between viewing `MPromDB Promoters chr19` (line 279) and renaming the 13-column interval file (line 289), the actual tool invocation steps (`Cut` column 2, `Convert delimiters` on `:` and `..`, and `Paste` columns back) were omitted, leaving only the four result descriptions (*"The resulting dataset contains only one column..."*, *"The output dataset has two columns..."*, etc.). Restore the explicit `Cut`, `Convert`, and `Paste` tool selection lines corresponding to Figure 10.5.11 and Figure 10.5.13.
  3. **Basic Protocol 4 (Line 557):** Step 2 instructs the user to name the new history `"Basic Protocol 3"`, while Step 3d (line 567) copies datasets into `"Basic Protocol 4"`. Change line 557 to `"Basic Protocol 4"`.
  4. **Basic Protocol 5 (Line 953 vs. Line 1009):** In Step 8c (line 953), the filter string is printed with mismatched quotes `len(c2.replace('-', ")) > 0` (a double quote instead of two single quotes `''`), and in Figure 10.5.36 caption (line 1009), `"rheMac."` is missing the `2` (`"rheMac2."`). Fix both strings.
