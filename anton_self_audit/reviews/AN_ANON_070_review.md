# Review of AN_ANON_070

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.1 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.2 / 8.0**  
* **Score Breakdown:** Rigor: 2.7/3.5 | Claims: 1.8/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This foundational genomic resource manuscript presents the whole-genome sequences of an indigenous Kalahari hunter-gatherer (KB1, sequenced to 10.2-fold shotgun and 12.3-fold long-insert paired-end coverage on Roche/454 Titanium plus 23.2-fold on Illumina; and NB1 at 2-fold 454 coverage) and a southern African Bantu individual (ABT, sequenced to >30-fold coverage on ABI SOLiD 3.0 plus 7.2-fold on Illumina), accompanied by Nimblegen 2.1M array exome capture (≥16-fold 454 coverage, 1.5–1.9 Gb per person) across five southern African men (four Kalahari hunter-gatherers: KB1, NB1, TK1, MD8; and ABT). The authors generate a de novo `Phusion` assembly of KB1 (2.79 Gb in contigs with N50 = 5.5 kb; 3.09 Gb in scaffolds with N50 = 156 kb), identify ~1.3 million novel SNPs and 13,146 novel nonsynonymous variants relative to hg18 and existing databases, validate segmental duplications and gene copy-number differences via custom array-CGH, and perform autosomal PCA (`EIGENSTRAT` on 174,272 array SNPs) and mtDNA/Y-chromosome haplogrouping. All raw reads (`SRA010356`), variant calls (`dbSNP` handle `BUSHMAN`), array data (`GSE19048`), interactive UCSC browser tracks, and Galaxy workflows are openly deposited, with full multi-institutional IRB and government permit documentation.

The primary resource deliverable is technically rigorous: the authors cross-validate KB1 and ABT variant calls across three orthogonal sequencing chemistries (454, Illumina, SOLiD), high-density genotyping arrays (Illumina 1M), array-CGH, and Sanger/TaqMan assays, establishing an empirical false-positive SNP rate of 0.0009 and false-negative rate of 0.09 for KB1. They also provide a clear empirical demonstration of SNP array ascertainment bias in southern Africans (where Illumina 1M arrays underestimate heterozygosity in KB1 relative to a European control, whereas WGS confirms 59–60% heterozygous SNPs). The main methodological limitations lie in (1) comparing raw and "novel" SNP counts across personal genomes sequenced at vastly different depths and processed with unharmonized platform-specific variant callers (`Newbler`, `Corona Lite`, `MAQ`), and (2) over-interpreting single-variant genotypes in 1–4 individuals as putative evolutionary adaptations to foraging and desert physiology without population-genetic selection scans.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Indigenous southern African hunter-gatherers harbor extensive novel nucleotide diversity (~1.3 million novel SNPs across the five participants; 1.2 exomic differences/kb between pairs of Bushmen vs. 1.0/kb between a European and an Asian) that is systematically missed by commercial genotyping arrays: [Well Supported].**  
  The high pairwise exomic divergence (sequenced on the same Nimblegen/454 platform to ≥16x across all five individuals), the chimpanzee outgroup polarization of KB1's 743,714 novel SNPs (showing 87% are derived along the KB1 lineage while only 6% match the ancestral chimpanzee allele, line 208), the deep L0 mitochondrial divergence (up to 84 pairwise differences within haplogroup L0), and the direct comparison of Illumina 1M array heterozygosity versus WGS heterozygosity (line 210) provide strong, multi-layered support for this core finding.

* **KB1 carries an African 17q21.3 H2 inversion haplotype lacking the 75-kb duplication characteristic of European H2 haplotypes, as well as 193 array-CGH-validated gene copy-number differences relative to Yoruban genome NA18507: [Well Supported].**  
  Both structural findings are verified by orthogonal experimental methods: the 17q21.3 H2 inversion hotspot (2.5-fold SNP enrichment across 650 kb, $P < 10^{-5}$; Figure 3a) is confirmed by diagnostic variants, direct typing of a 238-bp indel, read depth, and array-CGH showing absence of the 75-kb European duplication; similarly, the 58 segmental duplication intervals (>20 kb) and 193 RefSeq gene copy-number differences between KB1 and NA18507 are directly validated on a targeted oligonucleotide CGH array (lines 228–230).

* **Cross-genome comparisons of total and novel SNP counts in Table 1 and Figure 2 accurately reflect biological divergence across KB1, ABT, and eight previously published personal genomes: [Fragile].**  
  In Table 1, genomic and coding SNP counts are compared across datasets generated on different platforms (454, SOLiD, Illumina), at different depths (e.g., 2x for NB1, 10.2x 454 + 23.2x Illumina for KB1, >30x SOLiD for ABT), and called with different software (`Newbler`, `Corona Lite`, `MAQ`). Notably, Table 1 itself shows that for the *same individual* (ABT), `ABT SOLiD` calls 17,342 coding-exon SNPs whereas `ABT exome` (Nimblegen/454) calls 18,994 coding-exon SNPs—a 9.5% (1,652 SNP) intra-individual discrepancy driven purely by platform and capture differences. Without downsampling WGS reads to a uniform callable depth and applying a unified variant-calling filter across all personal genomes, differences in total and novel SNP counts in Table 1 confound biological diversity with platform sensitivity and false-negative rates.

* **Specific coding variants and gene copy numbers observed in the four Bushmen (e.g., `CLCNKB` renal chloride channel in KB1, `ACTN3`, `VDR`, `TAS2R38`, `AMY1A` copy number = 15) reflect evolutionary adaptations to a Kalahari foraging lifestyle and arid environment: [Overstated].**  
  Although the authors include an appropriate caveat in line 216 that these genotype-phenotype links are "only candidates for the suggested functions", lines 222, 230, and 241 repeatedly frame variants found in 1 to 4 individuals (such as a single heterozygous `CLCNKB` allele in KB1 or `AMY1A` copy number = 15 in KB1 despite hunter-gatherers historically consuming lower-starch diets than agriculturalists, cf. Perry et al. ref. 21) as adaptive traits for desert foraging. Observing a common global polymorphism in $N=1$ to $4$ individuals provides no statistical evidence of positive selection in the Khoisan population.

* **Elevated SNP density at promoter nucleosome boundaries in Bushmen genomes (Figure 3b) may drive human phenotypic evolution: [Fragile].**  
  Figure 3b plots raw SNP density relative to the transcription start site (TSS) and nucleosome-free region (NFR), showing peaks flanking the NFR. However, the analysis does not normalize by human–chimpanzee divergence ($d$) or local GC/CpG dinucleotide composition; mammalian promoters are enriched for CpG islands and transcription-associated mutagenic processes that elevate neutral mutation rates independently of adaptive selection.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Harmonize Callable Space and Coverage Depth for Table 1 Cross-Genome Comparisons
* **WHY:** Comparing raw SNP totals across genomes sequenced at 2x to >30x on three different platforms with three different variant callers (`Newbler`, `Corona Lite`, `MAQ`) confounds population divergence with technical sensitivity (as evidenced by the 1,652 coding-SNP gap between `ABT SOLiD` and `ABT exome` in Table 1).
* **WHAT:** Report a coverage-normalized and callable-site-restricted pairwise divergence comparison alongside the raw Table 1 numbers.
* **HOW:** Restrict the whole-genome comparison of KB1 (using its 23.2x Illumina data), ABT, NA18507, NA19240, European, and Asian genomes to the intersection of genomic bases covered at $\ge 15\times$ with mapping quality $\ge 30$, and compute pairwise nucleotide diversity ($\pi$, differences per callable kilobase) and novel SNP fractions within that identical callable mask.

#### 2. Quantify Exome vs. WGS Concordance Within ABT and KB1
* **WHY:** Table 1 lists `ABT SOLiD` (17,342 coding SNPs) and `ABT exome` (18,994 coding SNPs) as separate rows without explaining why whole-genome SOLiD sequencing missed >1,600 coding SNPs detected by 454 exome capture (or conversely, how many 454 exome calls were homopolymer false positives).
* **WHAT:** Provide an explicit concordance matrix comparing WGS (454/Illumina/SOLiD), Nimblegen 454 exome capture, and Illumina 1M BeadChip genotypes across the targeted coding exons for both KB1 and ABT.
* **HOW:** Stratify the coding-exon SNP calls in KB1 and ABT into shared calls, WGS-only calls, and exome-only calls, and use the Illumina 1M array genotypes at overlapping coding sites to report platform-specific false-positive and false-negative rates for the 454 exome capture versus SOLiD WGS.

#### 3. Test Candidate Adaptive Loci Using Population-Level Genotyping Array Data
* **WHY:** Inferring desert or foraging adaptation from genotypes in $N=1$–$4$ sequenced individuals (`CLCNKB`, `VDR`, `ACTN3`, `TAS2R38`) has no statistical power against genetic drift.
* **WHAT:** Leverage the larger genotyping cohort already analyzed in Figure 4 (15 Bushmen [10 study + 5 HGDP San], 20 Xhosa, 20 Yoruba, 20 Europeans) to test whether candidate loci show population differentiation or extended haplotype homozygosity.
* **HOW:** Compute locus-specific $F_{ST}$ and iHS/XP-EHH statistics across the 174,272 autosomal SNPs in the Figure 4 cohort for the genomic intervals containing `CLCNKB`, `VDR`, `ACTN3`, `TAS2R38`, `LCT`, and `DARC`, and report where these candidate genes fall in the genome-wide empirical distribution of differentiation between Khoisan and Bantu/Yoruba populations.

#### 4. Normalize Promoter/Nucleosome SNP Profiles by CpG Context and Outgroup Divergence
* **WHY:** The promoter SNP peak near $-1$ and $+1$ nucleosomes in Figure 3b can arise from CpG hypermutability and base-composition biases around TSSs rather than adaptive regulatory evolution.
* **WHAT:** Control for CpG dinucleotides and interspecies mutation rate variation in Figure 3b.
* **HOW:** Re-compute the Figure 3b TSS/nucleosome SNP density profiles after (a) excluding all CpG sites and (b) dividing human polymorphism density ($\pi$) by human–chimpanzee divergence ($d$) in each 10-bp window from $-1000$ to $+1000$ bp around the TSS.
