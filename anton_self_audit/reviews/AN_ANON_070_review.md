# Review of AN_ANON_070

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.9 / 10.0** (Strong / Sound) | **Scientific Core Score:** **7.0 / 8.0**  
* **Score Breakdown:** Rigor: 3.0/3.5 | Claims: 2.1/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This foundational genomic resource manuscript presents the complete genome sequences of an indigenous Kalahari hunter-gatherer (KB1, Tuu speaker) and a Southern Bantu individual (ABT, Sotho-Tswana and Nguni speaker), alongside low-coverage whole-genome sequencing (NB1, $2\times$) and Nimblegen $2.1\text{M}$ array exome capture ($>16\times$ coverage across $117\text{ Mb}$) for three additional Kalahari hunter-gatherers (NB1, TK1, and MD8) representing distinct linguistic and geographical groups in Namibia. The primary genomic deliverables are supported by extensive orthogonal validation: KB1 was sequenced to $10.2\times$ coverage on Roche/454 GS FLX Titanium ($350\text{ bp}$ reads), $12.3\times$ clone coverage in long-insert ($\le 17\text{ kb}$) 454 paired-end libraries, and $23.2\times$ coverage on Illumina, while ABT was sequenced to $>30\times$ on SOLiD 3.0 and $7.2\times$ on Illumina, supplemented by Illumina 1M SNP genotyping arrays, custom oligonucleotide array-CGH, TaqMan, and Sanger validation. The authors generate a Phusion *de novo* assembly of KB1 ($2.79\text{ Gb}$ contigs, N50 $5.5\text{ kb}$; $3.09\text{ Gb}$ scaffolds, N50 $156\text{ kb}$), identify $1.3\text{ million}$ novel SNPs genome-wide (including $13,146$ novel coding variants across $7,720$ genes) with an estimated KB1 SNP false-positive rate of $0.0009$ and false-negative rate of $0.09$, validate $193$ genes with copy-number differences relative to Yoruba NA18507, and perform principal component and admixture analyses across $174,272$ autosomal SNPs. All raw sequencing reads (`SRA010356`), variants (dbSNP `BUSHMAN`), and array data (GEO `GSE19048`) are publicly deposited alongside interactive workflow and browser portals.

The study is a landmark contribution to human evolutionary genomics that redresses the severe under-representation of basal southern African hunter-gatherer lineages in reference databases and demonstrates how European-biased commercial SNP arrays systematically underestimate heterozygosity in Khoisan populations. The multi-platform cross-validation of SNPs, indels, and segmental duplications is highly rigorous. The primary methodological limitations are restricted to secondary comparative and exploratory analyses: (1) Table 1 compares raw SNP counts across personal genomes sequenced on different platforms (`Newbler`/454, `Corona Lite`/SOLiD, `MAQ`/Illumina) at widely varying depths without normalizing to a shared callable genome mask; (2) the observation of elevated SNP density around promoter nucleosome borders (Figure 3b) does not control for local CpG hypermutability or human–chimpanzee divergence; and (3) while explicitly caveated as hypothesis-generating, several single-gene physiological narratives (e.g., *ACTN3*, *VDR*, *CLCNKB*, *AMY1A*) are based on $N=1\text{–}4$ individuals and require population-level selection scans to distinguish local adaptation from standing variation.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Southern African hunter-gatherers harbor substantially higher nucleotide diversity than non-African populations ($1.2\text{ differences/kb}$ between pairs of Bushmen in $117\text{ Mb}$ of exome-containing sequence vs. $1.0\text{/kb}$ between European and Asian individuals) and contribute $1.3\text{ million}$ novel SNPs: [Well Supported].**  
  The orthogonal combination of 454 Titanium, Illumina, SOLiD, Nimblegen exome capture, and 1M SNP arrays yields an empirically validated false-positive rate of $0.0009$ in KB1 ($4,053,781$ total SNPs; $743,714$ novel). Comparison with the chimpanzee genome confirms that $87\%$ of KB1's novel variants are derived alleles accumulated along the Bushman lineage rather than retained ancestral alleles ($6\%$) or sequencing errors ($\sim 3,600$ expected false positives).

* **Current commercial genotyping arrays suffer from severe ascertainment bias in southern African populations, artificially depressing apparent heterozygosity in KB1 compared to whole-genome sequencing ($59\%$ heterozygous SNPs in KB1 and $60\%$ in ABT): [Well Supported].**  
  Directly comparing Illumina 1M array heterozygosity against high-depth WGS on the exact same individual (KB1) provides definitive proof that marker ascertainment in European/HapMap cohorts distorts diversity estimates in basal African lineages.

* **KB1 carries an ancestral form of the chromosome 17q21.3 H2 inversion haplotype lacking the $75\text{-kb}$ duplication characteristic of European H2 alleles, and validates $193$ gene copy-number differences relative to Yoruba NA18507: [Well Supported].**  
  The 17q21.3 H2 haplotype in KB1 is confirmed by diagnostic SNPs, direct typing of the $238\text{-bp}$ indel, localized $2.5\times$ SNP enrichment across $650\text{ kb}$ ($P < 10^{-5}$), and both sequencing read depth and array-CGH confirming absence of the $75\text{-kb}$ duplication. Similarly, the $193$ RefSeq gene CNVs and $58$ KB1-specific segmental duplications ($>20\text{ kb}$) are orthogonally validated by custom oligonucleotide array-CGH.

* **Uniparental markers and autosomal PCA ($174,272$ SNPs) demonstrate genetic distinctiveness of Juu and Tuu hunter-gatherers alongside sex-specific gene flow with Southern Bantu populations: [Well Supported].**  
  EIGENSTRAT PCA clearly separates Khoisan from Niger–Congo and European populations (Tracy–Widom $P < 10^{-12}$), while whole-mitochondrial phylogeny and Y-chromosome haplotyping demonstrate that ABT carries a Bushman-specific maternal L0d mtDNA lineage alongside a Bantu E1b1a8a Y chromosome, whereas MD8 carries a Bantu Y chromosome alongside Khoisan autosomal ancestry.

* **Elevated SNP density around promoter nucleosome borders (Figure 3b) and specific candidate variants (*VDR*, *ACTN3*, *CLCNKB*, *TAS2R38*, *AMY1A*) reflect functional diversification or desert foraging adaptation in Bushmen: [Fragile].**  
  In Figure 3b, the peak of SNP density flanking the nucleosome-free region near transcription start sites is not normalized by human–chimpanzee divergence or CpG dinucleotide density, leaving neutral mutational rate heterogeneity (e.g., CpG methylation/deamination and transcription-coupled repair gradients) unseparated from selection. Similarly, while the authors appropriately caution that phenotypic associations in *VDR*, *ACTN3*, and *CLCNKB* are untested candidates (line 216), observing globally common alleles in $1\text{–}4$ individuals provides no statistical evidence of hunter-gatherer adaptation without population-wide allele frequency comparisons or haplotype homozygosity tests.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Normalize Cross-Genome SNP Comparisons in Table 1 by Jointly Callable Genomic Masks
* **WHY:** Table 1 lists raw `"Genomic SNPs"` and `"Novel SNPs"` across whole-genome datasets sequenced on different platforms and coverages (e.g., KB1 at $10.2\times$ 454 + $23.2\times$ Illumina with $4,053,781$ SNPs; J. Watson at $7.4\times$ 454 with $2,060,544$ SNPs; NB1 at $2\times$ 454 with $1,181,663$ SNPs; and MD8/TK1 with exome-only data yielding $125,848$ and $136,985$ SNPs). Presenting raw counts across unaligned coverage tiers conflates true biological divergence with callable-space and caller sensitivity differences (`Newbler`, `Corona Lite`, `MAQ`).
* **WHAT:** Add a normalized SNP rate column (SNPs per callable megabase) restricted to genomic intervals jointly covered at $\ge 10\times$ across the personal genomes, and clearly separate exome-only samples from WGS samples in Table 1.
* **HOW:** Intersect the per-base coverage masks of KB1, ABT, and the $117\text{ Mb}$ Nimblegen capture target regions (where all 5 study participants have $\ge 16\times$ coverage), compute the per-kilobase variant and novel-variant rates within the identical callable footprint, and add these normalized columns to Table 1.

#### 2. Control for Mutational Bias and CpG Content in the Promoter / Nucleosome SNP Profile (Figure 3b)
* **WHY:** Promoter regions and $-1/+1$ nucleosome boundaries have distinct GC/CpG compositions and transcription-coupled mutation/repair dynamics. Attributing elevated SNP density near nucleosome borders to potential phenotypic diversification (line 214) without controlling for neutral mutation rate variation can conflate mutational hotspots with selection.
* **WHAT:** Normalize the TSS/nucleosome SNP density profiles in Figure 3b by local human–chimpanzee divergence and repeat the calculation after masking CpG dinucleotides.
* **HOW:** Using the existing human–chimpanzee alignments already employed in line 208, compute the ratio of polymorphism (SNPs in Bushmen and non-Bushmen) to fixed human–chimpanzee divergence in sliding windows across the $\pm 1\text{ kb}$ TSS interval, both with and without CpG sites, and plot the divergence-normalized curve alongside Figure 3b.

#### 3. Quantify Population Differentiation for Candidate Adaptive Variants
* **WHY:** Reporting that 1 to 4 individuals carry literature-annotated alleles in *VDR*, *UGT1A3*, *ACTN3*, *CLCNKB*, or *TAS2R38* (line 222) cannot distinguish whether these variants are enriched in Kalahari hunter-gatherers relative to other African or global populations.
* **WHAT:** Where candidate SNPs (or tagging proxies) are present on the Illumina 1M / 610K genotyping arrays typed across the larger cohort ($10$ Bushmen, $20$ Xhosa, $20$ Yoruba, $20$ Europeans, and $5$ HGDP San), report their empirical allele frequencies and $F_{ST}$ values.
* **HOW:** Query the existing $N=75$ array dataset used for Figure 4 to tabulate allele frequencies and pairwise $F_{ST}$ (Khoisan vs. Bantu/Yoruba/European) in Supplementary Table 6 for all candidate loci captured on the array.
