# Review of AN_ANON_013

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.0 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This correspondence/resource manuscript presents the Vertebrate Genomes Project (VGP) and European Reference Genome Atlas (ERGA) automated genome assembly pipeline (version 2.1), implemented as 10 modular workflows across 8 analysis trajectories on the public Galaxy platform. Designed to support the Earth BioGenome Project's goal of scaling eukaryotic reference genome production, the pipeline integrates PacBio HiFi long reads with long-range scaffolding data (Hi-C and/or Bionano optical maps) and parental Illumina short reads across three primary assembly modes: solo (HiFi only), Hi-C phased/scaffolded, and trio-binned phased assemblies, alongside dedicated mitochondrial genome assembly and exogenous/mitochondrial decontamination workflows. The authors validate the workflows initially on the zebra finch (*Taeniopygia guttata*) reference genome and subsequently across 51 vertebrate species with PacBio HiFi and Hi-C data, comparing the resulting assembly metrics (genome size vs. GenomeScope estimates, scaffold NG50, Merqury k-mer completeness, BUSCO vertebrate ortholog completeness, and scaffold counts; Figure 2) against 19 earlier PacBio continuous long-read (CLR) assemblies.

The manuscript delivers a high-utility, openly accessible, and thoroughly documented bioinformatics resource backed by public cloud infrastructure, training tutorials, and open data deposition in GenomeArk and NCBI BioProject PRJNA489243. Its primary weakness lies in the extreme brevity of the main text, which omits concrete quantitative summary statistics for the 51 HiFi assemblies versus the 19 CLR baseline assemblies (deferring all numerical values to Figure 2 and Supplementary Table 5), provides no explanation in the main text of the "analyses on XBP1" mentioned in the author contributions (line 129), and asserts coverage recommendations (30$\times$–60$\times$ HiFi and 30$\times$ Hi-C per haplotype) and cross-kingdom generalizability (to plants, fungi, and invertebrates) without presenting empirical downsampling curves or non-vertebrate validation runs in the main article. Expanding the quantitative reporting of the 51-genome benchmark and clarifying the orphaned *XBP1* reference can be accomplished directly from the existing supplementary data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Claim 1: The VGP–Galaxy pipeline (v2.1) automates phased, chromosome-scale genome assembly across solo, Hi-C, and trio trajectories with integrated quality control and decontamination: [Well Supported].**  
  The pipeline architecture (Figure 1) systematically chains k-mer profiling (GenomeScope), contig assembly and phasing (Hifiasm), scaffolding (Hi-C / Bionano), decontamination (exogenous viral/bacterial and mitochondrial remnant removal), mitogenome assembly, and multi-metric QC (Merqury k-mer completeness and phasing, BUSCO gene completeness, contiguity statistics). Executing this successfully across 51 vertebrate species on public Galaxy instances demonstrates operational maturity and end-to-end reproducibility.

* **Claim 2: The 51 PacBio HiFi + Hi-C vertebrate assemblies confirm and extend improvements in assembly quality and haplotype resolution over 19 previous PacBio CLR-based genomes of similar size and complexity: [Moderately Supported].**  
  While the visual summary in Figure 2 and reference to Supplementary Table 5 and Supplementary Figure 6 support high completeness and contiguity across the 51 vertebrate genomes (spanning up to ~9 Gb in Figure 2), the main text reports zero numerical summary statistics (no median or interquartile range for contig N50, scaffold NG50, Merqury QV, switch error rate, or BUSCO completeness, and no formal statistical comparison against the 19 CLR assemblies). Furthermore, because the 51 HiFi species and 19 CLR species are not paired biological replicates of the same genomes (outside of benchmark species like zebra finch), differences in repeat architecture, heterozygosity, and sample preservation partially confound the cross-technology comparison unless explicitly controlled.

* **Claim 3: At least 30$\times$ PacBio HiFi coverage (and up to 60$\times$ for highly repetitive regions) plus 30$\times$ Hi-C coverage per haplotype is required for uniform Poisson sampling and accurate assembly: [Moderately Supported].**  
  In line 137, the authors recommend 30$\times$–60$\times$ HiFi coverage and 30$\times$ Hi-C coverage per haplotype, citing Lander-Waterman Poisson sampling theory (reference 7). While biologically and practically sensible, the main text does not show whether this threshold was empirically derived from coverage titration/downsampling experiments on zebra finch or across the 51 vertebrate datasets (where actual sequencing depths likely varied).

* **Claim 4: The vertebrate-tested pipeline principles and workflows can be applied to plant, fungal, or invertebrate genomes simply by modifying a few parameters such as BUSCO clades: [Fragile].**  
  In line 159, the authors state that although all 51 assemblies are vertebrates, the pipeline applies to plants, fungi, and other animals by changing minor parameters like BUSCO lineage clades. Non-vertebrate eukaryotes frequently exhibit polyploidy (auto- and allopolyploidy in plants), extreme heterozygosity (>5% in marine invertebrates), or somatic diminution/aneuploidy that violate diploid phasing assumptions in standard Hifiasm/Hi-C trajectories. Claiming seamless generalization without testing at least one polyploid plant or high-heterozygosity invertebrate dataset overstates the ease of cross-kingdom transfer.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Explicit Quantitative Summary Statistics for the 51 HiFi vs. 19 CLR Benchmark in the Main Text
* **WHY:** Readers should not have to visually estimate logarithmic radial bars in Figure 2 or dig into Supplementary Table 5 to learn the actual contiguity, base accuracy, and completeness achieved by the pipeline.
* **WHAT:** Add exact median and interquartile range (IQR) statistics for the 51 HiFi assemblies and the 19 CLR comparison assemblies directly in the main text (lines 150–157).
* **HOW:** Extract from Supplementary Table 5 and report in the text: (1) median (IQR) contig NG50, scaffold NG50, Merqury consensus quality value (QV), Merqury k-mer completeness (%), and BUSCO complete/duplicated (%) across the 51 HiFi genomes vs. the 19 CLR genomes, along with a two-sample Mann-Whitney $U$ test or regression controlling for genome size and repeat content; and (2) the exact metrics for the three zebra finch assembly trajectories (solo, Hi-C, and trio) mentioned in line 148.

#### 2. Resolve the Orphaned *XBP1* Analysis Reference in the Author Contributions
* **WHY:** Line 129 states in the Author Contributions: *"A.N. performed the analyses on XBP1."* However, the gene *XBP1* is never mentioned anywhere in the main text, figures, or figure legends of the manuscript.
* **WHAT:** Clarify or reconcile the reference to *XBP1* between the main text, supplementary note, and author contributions.
* **HOW:** If the *XBP1* locus was analyzed in the Supplementary Note as an illustrative gene-level validation of assembly completeness or phasing accuracy (e.g., resolving a GC-rich or previously gapped coding locus in zebra finch or other vertebrates), add a 1–2 sentence summary of that validation finding in the main text (around line 148–150) with a pointer to the specific Supplementary Figure/Note.

#### 3. Qualify Cross-Kingdom Generalizability for Polyploid and High-Heterozygosity Genomes
* **WHY:** The pipeline's phasing and scaffolding trajectories (workflows 3–9, Figure 1) are explicitly structured around two phased haplotypes ("once for maternal and once for paternal," line 146), which assumes a diploid genome.
* **WHAT:** Temper the claim in line 159 that applying the pipeline to plants, fungi, and non-vertebrate animals only requires changing QC parameters like BUSCO clades.
* **HOW:** Explicitly state that the current v2.1 workflows assume diploidy (or haploidy) and note how polyploidy (common in plants), extreme heterozygosity (>3–5% in many invertebrates), or haplotig purging parameters in Hifiasm/purge_dups must be adjusted when applying the workflows outside diploid vertebrates.

#### 4. Fix Minor Textual and Formatting Artifacts in Figure 2 Legend and Data Availability
* **WHY:** In the Figure 2 legend (line 155), ring `(ix)` is described as *"genome size in gigabytes, with lines at 9, 2, 3, 4, 6 and 8 Gb"* (confusing gigabases [Gb/Gbp] with gigabytes, and listing `9` before `2, 3, 4, 6 and 8`, which is almost certainly a typo for `1, 2, 3, 4, 6 and 8 Gb`). Additionally, the Data Availability statement is duplicated verbatim in lines 182–185 and 195–198.
* **WHAT & HOW:** Change `"gigabytes"` to `"gigabase pairs (Gb)"` and `"9, 2, 3, 4, 6 and 8 Gb"` to `"1, 2, 3, 4, 6 and 8 Gb"` in the Figure 2 legend (line 155), and remove the duplicate Data Availability section at the end of the manuscript.
