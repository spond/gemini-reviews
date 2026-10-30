# Review of AN_ANON_058

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.3 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a practical quality-control methodology and five open-source workflow tools (`Naive Variant Caller`, `Variant Annotator`, `Get FASTA from Variants Table`, `Phylorelatives`, and `MAF Boxplot`) to detect and trace cross-sample contamination in deep next-generation re-sequencing of non-diploid mixtures, demonstrated on `56` human mitochondrial DNA (`mtDNA`) samples from blood and buccal tissues. The workflow flags contaminated samples by combining minor allele counts ($\ge 2\%$ frequency passing double-stranded filters) with minor allele frequency (`MAF`) dispersion boxplots (Figure 1), and then identifies the contaminating donor by reconstructing a Neighbor-Joining (`NJ`) tree (`1,000` bootstraps) that includes synthetic minor-allele consensus sequences (`<sample>_MINOR`) alongside all major-allele consensus sequences (Figure 2). Applying this pipeline reveals that samples `F41M52` and `F41M52C1` (from family `F41`) were cross-contaminated by adjacent 96-well plate samples from family `F46`. All raw sequencing data, tools, and workflows are openly accessible online.

The study addresses an important and frequently overlooked failure mode in ultra-deep organellar, viral, and somatic re-sequencing, and the combination of MAF tight-clustering diagnostics with phylogenetic source tracing (`F41` minor alleles clustering within `F46`) is clear and effective. Three methodological and experimental design points merit improvement: (1) constructing `<sample>_MINOR` sequences from a hard $\ge 2\%$ per-strand threshold yields chimeric sequences when contamination is near the detection limit (`1%–3%`) or when true heteroplasmies coexist with contamination, whereas querying raw read counts at known donor-recipient haplogroup difference sites avoids thresholding artifacts; (2) the default `complete deletion` setting in `Phylorelatives` interacts poorly with `N`-filled positions from `Get FASTA from Variants Table` whenever any sample in a cohort experiences regional coverage or strand-bias dropout; and (3) the proposed exogenous spike-in protocol using bacteriophage $\phi\text{X174}$ and `pUC18` prior to library preparation conflicts with standard Illumina sequencing protocols that spike in $\phi\text{X174}$ as an on-flowcell control, and cannot detect contamination occurring earlier during DNA extraction or long-range PCR.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Excess heteroplasmy counts ($\ge 10$) paired with a narrow MAF interquartile range / MAD diagnose cross-sample carryover: [Well Supported].**  
  When DNA from a distinct mtDNA haplogroup contaminates a sample at fraction $c$, all $K$ fixed nucleotide differences between the two haplogroups appear simultaneously as apparent heteroplasmies with expected minor allele frequency $c$. Figure 1 clearly distinguishes uncontaminated samples (`0–3` heteroplasmies with wide MAF dispersion) from contaminated samples (`10–35+` sites with tightly clustered MAFs).

* **Phylogenetic clustering of minor-allele consensus sequences (`F41M52_MINOR` and `F41M52C1_MINOR`) traces contamination to plate-adjacent family `F46`: [Well Supported].**  
  Replacing heteroplasmic positions with their minor alleles places both `F41` minor-allele sequences firmly inside the `F46` family clade with strong bootstrap support (Figure 2), and physical plate records confirm that `F41M52`/`F41M52C1` and `F46` occupied adjacent wells on the 96-well plate sent to the sequencing facility.

* **`Phylorelatives` minor-allele consensus NJ tree construction is broadly robust across contamination levels and cohort sizes: [Moderately Supported].**  
  Two algorithmic behaviors limit `Phylorelatives` in "gray-zone" scenarios: (1) because `Variant Annotator` zeroes out any site where the minor allele fails the $\ge 2\%$ threshold on either strand individually (line 82), contamination at `1.5%–3.0%` will randomly pass at some donor SNPs and fail at others due to binomial strand sampling; at failing donor SNPs, `Get FASTA from Variants Table` substitutes the recipient's *major* allele, turning `<sample>_MINOR` into a synthetic recombinant chimera between the recipient and donor haplogroups that will branch basally rather than clustering cleanly with the donor; and (2) `Get FASTA from Variants Table` leaves unreported or strand-discordant positions as `N` (line 87), while `Phylorelatives` defaults to `complete deletion` (`pairwise.deletion = FALSE`, line 94), meaning a single sample with coverage dropout or strand-bias filtering (`count = 0`) at a diagnostic site causes that site to be deleted across all samples in the tree.

* **Striped `pUC18` and $\phi\text{X174}$ spike-ins added prior to barcoded library preparation provide a reliable general control for sequencing contamination: [Fragile].**  
  First, the manuscript presents no empirical data validating the `pUC18`/$\phi\text{X174}$ spike-in protocol. Second, Illumina sequencing facilities routinely spike unindexed $\phi\text{X174}$ libraries (`1%–5%`) into sequencing lanes for real-time matrix/phasing calibration; although unindexed $\phi\text{X174}$ reads mostly land in the undetermined bin, index hopping and barcode misassignment on multiplexed lanes routinely leak $\phi\text{X174}$ reads into barcoded sample bins, confounding $\phi\text{X174}$ as a sample-specific contamination marker. Third, adding spike-ins *prior to barcoded library preparation* (line 120)—after blood/buccal DNA extraction and 30-cycle long-range mtDNA PCR (lines 60–68)—cannot detect cross-contamination occurring during DNA extraction or PCR strip handling.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Change the `Phylorelatives` Default to Pairwise Deletion and Mask Recipient-Major Sites When Building Minor Consensus Sequences
* **WHY:** Under `complete deletion` (line 94), any site left as `N` by `Get FASTA from Variants Table` or zeroed by the `Variant Annotator` strand-bias filter in even one sample is dropped from the distance matrix for the entire cohort. Furthermore, filling non-heteroplasmic or sub-threshold sites in `<sample>_MINOR` with the recipient's major allele creates a recipient–donor chimera whenever a subset of contaminant SNPs falls just below the `2%` threshold.
* **WHAT:** Default `Phylorelatives` to `pairwise deletion` (`pairwise.deletion = TRUE` in `ape::dist.dna`) and add an option in `Get FASTA from Variants Table` to restrict distance calculations for `<sample>_MINOR` to the heteroplasmic positions of the focal sample (or lower the secondary lookup threshold to `0.5%` once a sample is flagged).
* **HOW:** In the `Phylorelatives` Python/R wrapper, set `pairwise.deletion = TRUE` as the default parameter, and add a direct donor-likelihood / proportion-explained column reporting, for each candidate donor $j$, the fraction of sites where donor $j$'s major allele differs from recipient $i$'s major allele that show $\ge 0.5\%$ reads matching donor $j$ in recipient $i$'s `Naive Variant Caller` `NC` counts.

#### 2. Add a Formal Quantitative Statistic Alongside the Visual `MAF Boxplot`
* **WHY:** While the authors prefer a visual boxplot over a single summary statistic (line 138), automated pipelines screening hundreds of multiplexed samples benefit from a quantitative flag that combines polymorphism count ($K$) and MAF dispersion ($\text{MAD} / \text{median}$).
* **WHAT:** Include the coefficient of dispersion ($\text{MAD} / \text{median MAF}$) and a binomial/beta-binomial homogeneity test $p$-value in the `MAF Boxplot` text report.
* **HOW:** In the `MAF Boxplot` script, for any sample with $K \ge 5$ heteroplasmic sites, compute a $\chi^2$ or likelihood-ratio test of the null hypothesis that all $K$ minor alleles share a single common contamination fraction $p_0 = \sum m_k / \sum n_k$ (or report $\text{MAD} / \text{median}$), flagging samples where $K \ge 5$ and $\text{MAD} / \text{median} < 0.25$.

#### 3. Replace $\phi\text{X174}$ with Orthogonal Non-Illumina Spike-Ins Added Prior to PCR or DNA Extraction
* **WHY:** Because $\phi\text{X174}$ is used by Illumina sequencers as a lane control, barcode misassignment or index hopping can introduce $\phi\text{X174}$ reads into samples that never received the $\phi\text{X174}$ spike-in; additionally, spiking after PCR misses extraction and PCR carryover.
* **WHAT:** Recommend synthetic or non-standard plasmid/phage spike-ins (or short artificial barcoded amplicons flanked by the `L*2817/H*11570` primer binding sites) added at the DNA extraction or pre-PCR stage rather than $\phi\text{X174}$ at the pre-library stage.
* **HOW:** Update the best-practices guidelines in lines 120–129 to warn readers against using $\phi\text{X174}$ when sequencing on Illumina lanes spiked with $\phi\text{X174}$ control DNA, and recommend using distinct non-homologous plasmids (e.g., `pUC18`, `pBR322`, or synthetic ERCC-like standards) added prior to long-range PCR.
