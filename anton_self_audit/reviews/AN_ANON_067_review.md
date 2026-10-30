# Review of AN_ANON_067

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.1 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.3 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This short report introduces the ToolShed, a web-based repository and package management mechanism for extending integrative genomic workflow instances with version-controlled community tools, compiled dependencies, and functional tests. To illustrate the utility of the system, the authors re-analyze matched whole-genome sequencing (1 sample, NCBI SRA `SRR345592`) and RNA-seq data (20 samples, `SRR353635`–`SRR353654`) from a single human individual (Chen et al.) to compare mitochondrial heteroplasmy and RNA–DNA differences. By installing `FreeBayes` from the ToolShed, they identify two candidate mitochondrial sites with minor allele frequency $>2\%$: site 13,636 (a biallelic T/C heteroplasmy with a $22\%$ average minor allele frequency across the 21 datasets) and site 2,619 (invariable A in genomic DNA, but scored as heterozygous in RNA-seq with $11,086$ reference and $20,584$ primary alternative reads out of $40,132$ total coverage). Because `FreeBayes` reports only reference and primary alternative counts in this configuration—omitting the remaining $8,462$ reads at site 2,619—the authors develop two custom Python utilities, `Naïve Variant Caller` (NVC) and `Variant Annotator`, deposit them with dependency definitions and functional tests into the ToolShed, and generate full four-nucleotide allele count profiles across all 21 samples. Raw sequencing accessions and workflow supplements (Additional file 1) are fully documented.

As a software note and reproducibility case study, the manuscript effectively demonstrates how wrapping ad hoc custom scripts into versioned, testable repository packages prevents workflow fragmentation. The biological vignette clearly illustrates the difference between a germline/somatic mitochondrial heteroplasmy (site 13,636) and a transcriptomic post-transcriptional modification signature (site 2,619). The primary technical limitations are restricted to the brevity of the variant-calling pipeline description—specifically, relying on standard whole-genome read mapping with multimapper removal (which can be confounded by nuclear mitochondrial DNA segments, or NUMTs) and presenting raw four-nucleotide pileup counts from NVC without formal base-quality, strand-bias, or sequencing-error probability models—along with a coordinate typo in the main text (`13,636` vs. `13,363`). These issues can be addressed through minor methodological clarifications and text edits.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The ToolShed enables automated installation, dependency compilation, and reproducible sharing of both third-party (`FreeBayes`) and custom (`NVC`, `Variant Annotator`) analysis tools across web-based workflow instances: [Well Supported].**  
  The manuscript documents the end-to-end packaging lifecycle—including source retrieval, compilation, tool configuration XML/wrappers, dependency registration, and functional test execution—and demonstrates its application on a cloud instance (Amazon EC2).

* **Mitochondrial site 2,619 exhibits a multiallelic RNA-specific variation pattern (absent from matched genomic DNA) that is incompletely captured by biallelic variant reporting: [Well Supported].**  
  Across the 20 RNA-seq runs (`SRR353635`–`SRR353654`) and 1 WGS run (`SRR345592`), `FreeBayes` reports $11,086$ reference (A) and $20,584$ primary alternative (T) reads out of $40,132$ total reads ($31,670$ summed), leaving $8,462$ reads ($21.1\%$) unaccounted for. Applying `NVC` confirms that the remaining coverage consists of C and G mismatches restricted to the transcriptome data, consistent with reverse-transcriptase misincorporation at a modified mitochondrial rRNA nucleotide.

* **Mitochondrial site 13,636 (written as 13,363 in line 14) represents a biallelic T/C heteroplasmy with an average minor allele frequency of 22% maintained across genomic DNA and transcripts: [Moderately Supported].**  
  The concordance of T/C allele frequencies across the matched DNA and 20 RNA-seq samples supports a genuine heteroplasmy above the $2\%$ empirical threshold. However, the main text does not detail how nuclear mitochondrial pseudogenes (NUMTs) were handled when mapping against the full human reference genome and discarding multiply mapping reads, nor does it report strand-bias or base-quality filtering metrics for NVC.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Clarify NUMT Handling and Alignment Filtering in Mitochondrial Read Mapping
* **WHY:** Line 12 states that reads were mapped against the full human genome and reads mapping to multiple locations were removed. Because the human nuclear genome contains numerous high-identity NUMTs, aligning short reads simultaneously to the nuclear genome and chrM and discarding multimappers can both deplete coverage in conserved mtDNA regions and allow diverged NUMT reads to map uniquely to chrM (or vice versa), particularly when comparing gDNA and spliced/unspliced RNA-seq libraries.
* **WHAT:** Explicitly state in the main text how NUMT cross-mapping was controlled or bounded at sites 2,619 and 13,636.
* **HOW:** Report the read length and insert size of `SRR345592` and `SRR353635`–`SRR353654`, compare allele fractions at sites 2,619 and 13,636 when mapping to chrM-only versus the full human reference genome, and state the minimum mapping quality (MAPQ) and base quality (Phred) thresholds passed to `FreeBayes` and `NVC`.

#### 2. Document Error-Control Thresholds and Flagging in `Naïve Variant Caller` (NVC)
* **WHY:** While reporting exact four-nucleotide counts is essential for multiallelic sites and pooled/viral samples, raw pileup counts conflate biological variants with platform-specific sequencing errors and reverse-transcription artifacts unless stratified by base quality and read strand.
* **WHAT:** Specify the filtering parameters supported by `NVC` and `Variant Annotator`.
* **HOW:** Add a brief sentence on line 14 noting whether `NVC` stratifies allele counts by forward/reverse strand and minimum base/mapping quality scores in its VCF output, and state the exact command-line flags used to generate Figure 1c,d.

#### 3. Technical and Editorial Cleanup
* **WHY:** A nucleotide coordinate inconsistency in the main text can confuse readers attempting to cross-reference the mitochondrial locus.
* **WHAT & HOW:**
  * **Line 14:** Correct `"Site 13,363 is a textbook example of a heteroplasmy"` to `"Site 13,636 is a textbook example of a heteroplasmy"` so that it matches the coordinate reported in the preceding sentence (`"2,619 and 13,636"`) and the Figure 1 caption (`"sites 13,636 and 2,619"`).
