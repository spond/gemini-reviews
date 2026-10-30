# Anonymous Manuscript ID: TIME_ANON_0514

*(All identifying metadata, author names, journal titles, DOIs, and publication/citation calendar years have been scrubbed for temporally blinded review.)*

## Abstract

The Collaborative Cross (CC) was designed to facilitate rapid gene mapping and consists of hundreds of recombinant inbred lines descended from eight diverse inbred founder strains. A decade in production, it can now be applied to mapping projects. Here, we provide a proof of principle for rapid identification of major-effect genes using the CC. To do so, we chose coat color traits since the location and identity of many relevant genes are known. We ascertained in 110 CC lines six different coat phenotypes: albino, agouti, black, cinnamon, and chocolate coat colors and the white-belly trait. We developed a pipeline employing modifications of existing mapping tools suitable for analyzing the complex genetic architecture of the CC. Together with analysis of the founders’ genome sequences, mapping was successfully achieved with sufficient resolution to identify the causative genes for five traits. Anticipating the application of the CC to complex traits, we also developed strategies to detect interacting genes, testing joint effects of three loci. Our results illustrate the power of the CC and provide confidence that this resource can be applied to complex traits for detection of both qualitative and quantitative trait loci.

Keywords: The Collaborative Cross, gene mapping, complex traits, genetic analyses, Collaborative Cross (CC), quantitative trait locus mapping, Multiparent Advanced Generation Inter-Cross (MAGIC), multiparental populations, MPP

THE Collaborative Cross (CC) project has been in progress for a decade ( Churchill et al. [YEAR] ; Chesler et al. [YEAR] ; Iraqi et al. [YEAR] ; [REDACTED_AUTHOR] et al. [YEAR] ; Collaborative Cross Consortium [YEAR] ). The CC began from 56 nonreciprocal crosses of eight parental strains: A/J, C57BL/6J, 129S1SvImJ, NOD/LtJ, NZO/HILtJ, CAST/EiJ, PWK/PhJ, and WSB/EiJ. (For convenience, these strains are referred to below as A/J, C57BL/6J, 129S1, NOD, NZO, CAST, PWK and WSB.) Whole-genome sequencing showed that >85% of common species genetic variability was encompassed within these founder strains ( Yalcin et al. [YEAR] ). Our breeding program generated over 900 lines ( [REDACTED_AUTHOR] et al. [YEAR] ), with over 100 CC strains currently at inbreeding generation 15 or beyond.

The CC strains display a vast amount of variation in obvious attributes such as coat color, behavior, body weight, growth size, etc. ( Collaborative Cross Consortium [YEAR] ). Over 38M SNPs and Indels have been identified among the CC founder strains, ensuring genetic diversity within the CC ( Munger et al. [YEAR] ). A major advantage of the CC over conventional genetic approaches is that only one round of genotyping is required, and these data can be used whenever a new trait is characterized. Many of the CC strains have been genotyped using the MegaMUGA Illumina array, which provides a dense coverage genome-wide by typing 77,808 SNP markers. The founder haplotypes at each genomic interval can then be imputed using these genotypes ( Mott et al. [YEAR] ; Yalcin et al. [YEAR] ; Zhang et al. [YEAR] ; Collaborative Cross Consortium [YEAR] ; also see Materials and Methods ).

Application of these genetic data to analyze phenotypes of interest allows rapid detection of relevant loci. There are several factors that control the reliability of gene mapping with the CC. These include the number of lines tested for a trait of interest; the founder haplotype diversity present per locus among these strains; the effect of covariant factors on the desired trait of interest; the multigenic nature of the trait; the effect size of the gene on the trait of interest; and the presence of phenocopies. In the case of a monogenic trait, a group of CC lines sharing a common trait will share the same founder haplotype(s) at the causative genetic locus. In a polygenic trait, there will be some inconsistencies in the sharing of founder alleles and hence a linear mixed model can be used to evaluate the maximum-likelihood estimate (derived LOD score) for each genomic position with a suitable significance threshold to differentiate signal from noise. Recently, Bayesian Networks based analysis methods have also been proposed to map polygenic traits ( Scutari et al. [YEAR] ). In the case of a categorical trait, we show below that an analysis using logistic regression or even Fisher’s exact test is appropriate, especially in the case of small sample sizes.

The power of the CC was formally calculated by Valdar et al. ([YEAR]) . They determined that 500 CC strains provided 67% power to detect a QTL with a 5% additive effect; power rose to ∼100% when the QTL effect size exceeded 10%. Unfortunately, it seems unlikely that there will be 500 CC strains available for testing; most groups may be able to test fewer than 100 strains. Therefore, we sought empirical evidence for mapping genes using this lower number. In this report, we validated the utility of this reasonable number of CC strains for rapid mapping of genes mediating specific phenotypes. For this proof-of-principle exercise, we analyzed several coat color phenotypes, as this approach offered the advantage of easily ascertained phenotypes whose [REDACTED_VENUE] have been well established ( cf . Silvers 1979 ). In addition, we present a step-by-step guide that may be useful to researchers using the CC for the first time.


## Materials and Methods


## CC strains

The CC strains used in this study were bred by Geniad and housed in a specific pathogen-free facility at the Animal Resources Centre (Murdoch, WA, Australia) as described ( [REDACTED_AUTHOR] et al. [YEAR] ). The Australian Code for the Care and Use of Animals for Scientific Purposes was followed, and the mice were maintained with appropriate ethics approvals. CC mice and data were kindly provided by Geniad. Genotypes for a further 25 CC strains produced at the other two CC colonies were obtained from a publicly available database ( http://csbio.unc.edu/CCstatus/index.py?run=AvailableLines ).


## Quality control and preprocessing

First we obtained genotypes for the eight founders (eight replicates each) on the MegaMUGA genotyping platform from the University of North Carolina CC web site ( http://csbio.unc.edu/CCstatus/index.py?run=GeneseekMM ). We took consensus calls for each of eight replicates for each founder type. Among the 77,000 SNPs, some 69,245 SNPs were robustly homozygous in these inbred founder lines. Hence we extracted these 69,245 SNPs. For each strain, SNPs with a missing call were removed. PedPhase v3 ( Li and Li [YEAR] ) was applied to determine the phase of the raw genotypes and to correct any genotyping errors.


## Haplotype reconstruction

The phased and cleaned genotypes were separated into two sets of genotypes per strain, namely homozygous genotypes of allele 1 and homozygous genotypes of allele 2 for the genome to be treated as haploid (inbred). These data were used in HAPPY ( Mott et al. [YEAR] ) in conjunction with 69,245 homozygous genotypes of the eight founder strains. We use the method “hdesign” in HAPPY to estimate the founder haplotype having the maximum-likelihood probability for genotype sets of allele 1 and 2 separately. A consensus of the resulting haplotype assignment was taken as the final call. In the regions where the genomes were heterozygous, the haplotype calls for alleles 1 and 2 differed. These data were recoded as 0, 1, and 0.5 for each of eight founder alleles at each marker, where 0 refers to nonfounder haplotype; 1, homozygous founder haplotype; and 0.5, heterozygous founder haplotype.


## Candidate gene mapping

A step-by-step guide is presented in Figure 1 , with a more detailed description in Supporting Information , File S1 . The guide illustrates the steps involved in preprocessing genotyped SNPs, phasing, haplotype estimation, determining consensus haplotype code, and verification followed by qualitative/quantitative mapping methods using haplotype data. Most users will not need to concern themselves with the haplotype imputation steps. A detailed description of the mapping pipeline is provided in the Supporting Information .


> **Figure 1:** Overview of analytic pipeline. The methods are divided into two parts: (Top) genotyping and haplotyping analysis illustrates steps involved in the transfer from MegaMUGA genotypes to eight founder haplotypes and (Bottom) gene mapping illustrates the steps involved in testing identified phenotype values against genome-wide haplotype information, followed by identification of candidate causal genes.

Briefly, coat color traits were coded as cases and controls. A logistic regression model was fitted for the trait at each locus using the recoded eight variable haplotype data set (with 7 degrees of freedom). A one-way ANOVA chi-square test was used to estimate the P -value of association. In the case of the multinominal analysis, the coat colors were treated as qualitative values from 1 to 5. A false discovery rate (FDR) ( Benjamini and Yekutieli [YEAR] ) correction method was used to define the genome-wide significant linkage peaks. Peaks were deemed significant after applying an FDR P -value correction, with an FDR of P < 0.001, while FDR P < 0.01 values were treated as suggestive. The founder strain(s) contributing to each trait were determined by deriving coefficients (log odds ratio) of the fit from the logistic/multinominal regression model and using plotting tools implemented in the DOQTL R package ( [REDACTED_AUTHOR] et al. [YEAR] ). Then a list of putative genes at each locus was obtained by comparing founder alleles. From this list, identity of the candidate gene was arrived at by its relevance to the tissue studied ( e.g. , skin and hair follicle).


## Results


## Genotyping and imputation of founder haplotypes

The coat phenotypes of the CC strains tested here are listed in Table S1 . Genotypes were determined from CC breeders at inbreeding generation N16 and beyond. The raw genotype reads were subject to quality control, and the SNPs were positioned with reference to the mm9/build37 assembly. Residual heterozygosity per strain was calculated to be <10% ( Table S2 ).

The founder haplotypes were reconstructed using data for 77,000 SNPs genome-wide (see Materials and Methods ). Phasing was performed with PedPhase 3 ( Li and Li [YEAR] ), and then for each marker the most likely founder haplotype was returned using HAPPY ( Mott et al. [YEAR] ). The assigned haplotype call was then used to reconstruct allele calls for each marker, and this data set was compared against the raw genotyping data for purposes of confirmation. Matching was over 97% for all strains.

An NxMxK weight matrix (where N = 118 strains, M = 8 founders, K = 77,000 SNPs) was used to summarize the genotype data. The eight founder weights were assigned based on reconstructed haplotypes as either homozygous weight = 1, heterozygous weight = 0.5 (split between the two founder alleles), or 0 otherwise. Kinship between the CC lines was calculated using raw genotypes and was generally found to be <60% ( Table S3 ). Figure S1 shows the genome-wide correlation in the reconstructed haplotypes of the CC lines. No two CC lines had kinship >80%, demonstrating the genetic diversity of the CC population.


## Extraction of nonsynonymous SNPs and common variants

There were ∼69,000 SNPs on the MegaMUGA that were homozygous in the eight founders. We obtained founder genotypes for 170,000 SNPs at common variants typed in the JAX Mouse Diversity Genotyping Array ( Yang et al. [YEAR] ). A further 85,000 nonsynonymous (ns) variants from the Sanger Mouse genome sequence project ( Yalcin et al. [YEAR] ) were extracted by parsing query to their web interface. For these Diversity Array and nsSNPs, we imputed genotypes for each CC strain based on the haplotype calls ( Yalcin et al. [YEAR] ). This yielded a genome-wide set of ∼329,141 SNPs that could be used for SNP-wise association analyses.


## Mapping strategy

An overview of the mapping strategy (including the haplotype inference steps described above) is shown in Figure 1 . For the experiments below, we performed a logistic regression fit for the eight founder alleles at each locus (using R-GLM). We also tested the traits using Fisher’s exact test (8 × 2 contingency table, with eight CC founders, two phenotypic values) per SNP (see Supporting Information ). We found that Fisher’s exact test was just as effective as the logistic regression model in finding QTL positions. However, its utility was limited for more complex studies since it cannot handle covariates.


## Proof of principle: mapping the albino locus

Of 110 genotyped strains, 30 were albino. The phenotype was encoded as a binomial value (1, albino; 0, colored). Mapping was performed using a logistic regression model (LRM) fit over the reconstructed haplotype matrix. The resulting genome-wide distribution of P (ANOVA chi-squared) is shown in Figure 2A , together with FDR thresholds. The position of the peak SNP was at 93 Mb on chromosome 7. Applying a −1 −log 10 ( P ) drop restricted the locus interval to between 91 and 96 Mb. The coefficients (log odds ratio) of the fit from the LRM for the chromosome 7 region, together with the corresponding ANOVA test –log 10 ( P ) values are shown in Figure 2B . This analysis clearly showed that haplotypes of the two albino founders (NOD and A/J) contributed to the phenotype.


> **Figure 2:** Mapping the albino trait. (A) Genome-wide scan comparing albino vs. colored CC strains. The x -axis shows the chromosomal position and the y -axis shows the −log 10 ( P ) values; the P -values were derived from linkage haplotype data. The two threshold lines drawn represent 99.99% (adjusted P < 0.0001) confidence and 99.9% (adjusted P < 0.0001) confidence. (B) Founder coefficient plot for the chromosome carrying the peak locus. (Top) The plot of the calculated log-odds ratio of eight founder alleles over the chromosome where the founders are color coded. (Bottom) The –log 10 ( P ) values at this chromosome.

The catalog of 329,141 genome-wide SNPs (derived as described above) was assessed as an exercise in identifying the causative gene. Within the target region, there were only 9 genes (and 10 missense SNPs) in which the reference allele was present only in the colored group and the variant allele was present only in the albino group. Examining these 9 genes in the GXD gene expression database ( Smith et al. [YEAR] ) showed that only the Tyrosinase ( Tyr ) gene had significant expression in skin and hair follicle; the G allele of the Tyr missense SNP rs31191169 encodes an amino acid change (Cys to Ser) that is predicted by PROVEAN ( Choi et al. [YEAR] ) to have a damaging effect on the protein (Protein seq. ID: NP_035791 ). The albino trait is known to be due to tyrosinase deficiency ( Russell and Russell 1948 ), and mutations in Tyr have been functionally validated as causing albino coat color ( Tanaka et al. [YEAR] ).

Thus, in a few simple steps we could rapidly map and identify the causative gene and variant for this example trait. This demonstrated the power of the CC for rapid gene identification.


## Analyzing the agouti trait

Next, we compared 64 pigmented strains. Fifteen of these had black coats while the rest were agouti. A genome scan was conducted using the same methods as above. As shown in Figure 3A , the peak SNP was at 154 Mb of chromosome 2; the –log 10 ( P )−1 confidence interval was between 153.8 and 158.0 Mb. The B6 and A/J founder strains clearly showed allelic differentiation at this locus ( Figure 3B ). A SNP-wise analysis of 329,141 SNPs revealed 23 significantly associated SNPs in the candidate region ( Figure 3C ). Among these, there were 11 nsSNPs in seven genes, but none of these were expressed in skin or hair follicle. A query of the Sanger database yielded a total of two SNPs overlapping the agouti gene with appropriate allelic distribution between the strains. However, neither of these SNPs was nonsynonymous. Thus, although we could rapidly identify associated SNPs, this low-level approach could not detect the genetic variant responsible for the agouti trait. This is perhaps not surprising since the molecular basis of the non-agouti trait in C57BL/6J strains is the insertion of a retrotransposon into an intron of the agouti gene ( Bultman et al. [YEAR] ). [Note that although A/J is albino, it too carries a non-agouti allele ( Bultman et al. [YEAR] ).]


> **Figure 3:** Mapping the agouti trait. (A) Genome-wide scan comparing agouti vs. non-agouti CC strains. Other details are as for Figure 2 . (B) Founder coefficient plot for the chromosome carrying the peak locus. Details are as for Figure 2 . (C) SNP-wise genome-wide scan. The P -values were derived from SNP-genotype data. Other details are as for Figure 2 .


## Analyzing the cinnamon coat trait

Cinnamon (or brown agouti) is a coat color dilution trait that is not exhibited by any of the CC founder strains. However, 15 of the 64 pigmented CC strains showed this trait, so we investigated their [REDACTED_VENUE]. The linkage plot is shown in Figure 4A , and the coefficients of the fit for chromosome 4 are shown in Figure 4B . The peak was on chromosome 4, with a confidence threshold between 78 and 81 Mb. The peak was defined by A/J founder alleles; all strains with the cinnamon trait had the A/J haplotype at the locus. In this region, there was only one missense SNP whose alleles showed the appropriate strain distribution pattern: rs28091500 , located in Tyrp1 . The A allele was present in the strains with cinnamon coats. This allele encodes the amino acid substitution C110Y, predicted by PROVEAN ( Choi et al. [YEAR] ) to be deleterious. Tyrp1 encodes tyrosinase-related protein, which has been shown to cause the brown color dilution trait ( Bennett et al. [YEAR] ).


> **Figure 4:** Mapping the cinnamon coat trait. (A) Genome scan comparing cinnamon vs. other colored CC strains. Other details are as for Figure 2 . (B) Founder coefficient plot for the chromosomes carrying the peak locus. Details are as for Figure 2 .


## Analyzing the chocolate coat trait

Chocolate may be considered as a darker shade of brown than cinnamon. It is another color dilution trait that is not evident in the CC founder strains. We compared the 64 pigmented strains, of which 9 had chocolate-colored coats. Two significant peaks were seen ( Figure 5A ): between 79.5 and 80.5 Mb on chromosome 4 and between 149 and 156 Mb of chromosome 2. The coefficients are summarized in Figure 5, B and C . The chocolate and cinnamon coat mice shared the same chromosome 4 gene/allele ( i.e. , Tyrp1 ). However, all the chocolate coat mice had either a C57BL/6 or an A/J allele at the agouti locus compared to the cinnamon mice, suggesting the non-agouti allele at chromosome 2 interacts with Tyrp1 to produce the chocolate brown coat. Hence, analysis of CC data could rapidly generate a model in which these genes interact to produce the trait of interest.


> **Figure 5:** Mapping the chocolate coat trait. (A) Genome-wide scan comparing chocolate vs. other colored CC strains. Other details are as for Figure 2 . (B & C) Founder coefficient plots for the chromosome carrying the peak loci on chromosome 2 and 4.


## White-belly gene mapping

Some CC strains have paler fur in the belly area. This trait was also apparent in the 129S1 founder strain. We compared 64 pigmented strains of which 14 displayed a white belly. There was only a single linkage peak. This was on chromosome 2 and overlapped the region harboring the agouti ( a ) gene, as shown in Figure 6 . Only the 129S1 haplotype contributed to the allelic differentiation. This strain bears an agouti mutation (A w ) that is known to induce hypo-pigmentation in the belly area ( Dickie 1969 ).


> **Figure 6:** Mapping the white-belly trait. Founder coefficient plot for the chromosome carrying the peak locus after comparing genotypes of white-bellied vs. other colored CC strains.


## Modeling coat color as a complex trait

To extend the utility of the CC to mapping genes for complex traits, we tested whether loci could be mapped robustly in a three-gene system. To do so, we modeled coat color as a complex trait, considering all five coat traits displayed by our CC strains. Two analytical methods were used. First, modeling was done with the traits distributed as multinominal categories, and multinominal logistic regression analysis was performed using R-Multinom fit and the P -value was obtained from an ANOVA chi-square test. In the second method, coat color was naively assigned a number on a scale from zero (white) through cinnamon, agouti, and chocolate to black (100%) and analyzed using a linear model; the P -value was obtained by an ANOVA F -test. The results are shown in Figure 7 , together with a conservative FDR threshold. Both methods could readily detect linkage to the agouti and albino loci. The multinominal method also correctly identified the contribution of the third locus ( Tyrp ). This example shows that the level of complexity found in a three-gene interaction system could be successfully analyzed using our panel of CC strains and suggests a simple method for accurately mapping the genes of interest.


> **Figure 7:** Modeling coat color as a complex trait. Genome-wide scan comparing all CC strains with different coat colors considered as individual traits. The P -values were derived from linkage haplotype data. The red lines were derived from multinominal analysis of coat color traits; blue lines were derived from analysis of coat color traits given a quantitative value. The threshold line represents 99.99% (adjusted P < 0.0001) confidence that applies to both analyses.


## Reliability of gene mapping using a smaller sample of CC strains

We envision that researchers will prefer to ascertain phenotypes in a smaller set of strains, using these data to map key genes, and validate these in a second, smaller set of CC strains selected to maximize mapping power. To enable such a scenario, it is important to evaluate the reliability of mapping in a set of strains smaller than the 110 used above. Therefore, we evaluated linkage in >1000 randomly selected sets of 50 strains. Of 1150 permutations, 27 showed genome-wide significance at all three genes with no significant false positives in any of the 27 permutations ( Table 1 ). A total of 885 scans (77% of the total) resulted in at least one of three test loci being detected with genome-wide significance, while 316 scans (27% of the total) resulted in at least suggestive significance at all three test loci. Only 6 scans (<1%) resulted in false positives at the genome-wide significance level.


### Table 1: Empirical testing of likelihood of successful gene mapping using 50 strains

|  | No. of loci |
| No. of trials | Significant | Suggestive | NS | FP |
| 27 | 3 | 0 | 0 | 0 |
| 86 | 2 | 1 | 0 | 2 |
| 65 | 2 | 0 | 1 | 1 |
| 133 | 1 | 2 | 0 | 1 |
| 292 | 1 | 1 | 1 | 2 |
| 282 | 1 | 0 | 2 | 0 |
| 70 | 0 | 3 | 0 | 0 |
| 100 | 0 | 2 | 1 | 0 |
| 72 | 0 | 1 | 2 | 0 |
| 23 | 0 | 0 | 3 | 0 |
| Total: | 1150 |

## Minimum number of strains required for analysis of uncommon traits

In our characterization of CC strains, we have observed some traits that are exhibited by only a small number of strains. To determine the minimum number of strains required for reliable mapping of an unusual trait, we used the chocolate coat color as a model. All 501 combinations of between two and eight of the nine chocolate strains were tested to determine what the minimum number of strains would be required for successful mapping of uncommon traits, with comparison to all other colored strains. The comparison group was all other non-albino strains. As shown in Table 2 , both loci that contribute to the trait achieved better signals than background using at least six strains, while genome-wide significance was achieved using at least seven strains.


### Table 2: Evaluation of the minimum number of strains required to map interacting major-effect loci

|  |  | −log 10 ( P ) |
|  |  | Chromosome 2: a locus | Chromosome 4: Tyrp1 locus | Other |
| No. of test strains ( n ) | No. of combinations (9C n ) | Minimum | Maximum | Minimum | Maximum | Maximum |
| 2 | 36 | 1.67 | 1.94 | 1.44 | 1.67 | 1.94 |
| 3 | 84 | 2.65 | 2.97 | 2.36 | 2.65 | 2.65 |
| 4 | 126 | 3.57 | 3.94 | 3.24 | 3.57 | 3.57 |
| 5 | 126 | 4.45 | 4.84 | 4.08 | 4.45 | 4.45 |
| 6 | 84 | 5.27 | 5.69 | 4.88 | 5.27 | 4.02 |
| 7 | 36 | 6.05 | 6.05 | 5.64 | 6.05 | 4.48 |
| 8 | 9 | 6.8 | 6.8 | 6.37 | 6.8 | 3.76 |

## Discussion

The purpose of this study was to provide the proof of principle for applying the CC resource for rapid mapping and identification of genes responsible for traits of interest. Although it was originally planned to produce 1000 CC strains, a combination of factors including poor breeding performance and insufficient funding precluded a resource of this magnitude. Therefore, it was important to establish whether a smaller panel of CC strains would be sufficient to support robust gene mapping in view of the published power estimates calculated for 500 CC strains ( Valdar et al. [YEAR] ).

Our results showed that a panel of ∼100 CC strains supported rapid mapping of each of five coat color traits. A sixth trait (white head blaze) was also assigned to the Kitl gene( Zsebo et al. , [YEAR] ) (not shown because this had been demonstrated in analyses of the “pre-CC” by Aylor et al. [YEAR] ). In addition to gene mapping, this CC panel was also able to support not only identification of the causative gene, but also the genetic variants responsible for determining the albino, chocolate, and cinnamon coat traits.

Mapping of genes for dichotomous traits in the CC is therefore likely to be a very powerful application of this resource. Pilot studies in a screen of only 50 CC strains could identify those with phenotypes at the extremes of the range. A dichotomous test of the extreme phenotype strains should reveal likely candidates for major-effect genes. More complex traits may also be successfully analyzed, as demonstrated with the multinominal analysis of five coat colors. We also demonstrated that major-effect genes could be readily mapped using LRM analyses of CC data.

We investigated how few strains were needed for reliable mapping of genes of interest using the CC resource. Our results suggest positive identification of least one of three loci at genomic significance in every 3 of 4 random scans of mapping using a subset of 50 CC strains, while all but 23 scans ( i.e. , 98%) resulted in detection of one or more of the test loci ( a , Tyrp1 , and Tyr ) with at least suggestive significance. Furthermore, there was a very low rate of false positives (<1%). This work supports a two-stage strategy for mapping using CC strains: an initial scan of phenotypes in 50 strains is likely to detect loci that can be validated in a second stage using CC strains selected to maximize mapping power. Finally, our modeling to determine how few strains were needed to map an uncommon trait showed that as few as 6 strains may be sufficient to obtain suggestive true positives at the candidate loci. These results provide the basis for future investigations using the CC.

The plot of the log-odds of each founder allele calculated at each locus is an accurate way of representing and interpreting the founder haplotype bearing the causative allele. A follow-up SNP-based analysis using a catalog of well-annotated variants would help to narrow down the locus interval and to identify the likely causative gene. With the application of cluster computing, analyses could be expanded to utilize the millions of variants identified from sequencing the founders’ genomes ( Yalcin et al. [YEAR] ). Another useful resource for investigating candidate SNPs is the ECCO database ( Nguyen et al. [YEAR] ), which enables researchers to interrogate sequence variation of functional elements for each of 19 tissues/cell types. ECCO catalogs sequence variation in ∼300,000 functional elements ( e.g. , promoters, enhancers, and CTCF-binding sites) active across 17 inbred mouse strains, including the CC founders. Thus, candidate SNPs can be evaluated for effects on cis -acting regulatory elements.

This proof-of-principle study tested monogenic traits for which single genes exerted large effects. We demonstrated the suitability of the CC for efficient mapping of major-effect genes and defining the underlying causative genetic variants. Obviously, more complex traits, affected by factors such as epistasis and plieotropy, will be more challenging. Nevertheless, the results presented here showing the rapid and robust identification of genes for qualitative categorical traits provide confidence that future studies of quantitative phenotypes with complex genetic architectures will also benefit from the power of the CC.

This work was supported by Discovery Project Grant DP110102067 from the Australian Research Council; by Program Grant 1037321 and Project Grant 1069173 from the National Health and Medical Research Council of Australia; and by the Diabetes Research Foundation of Western Australia. R.R. is supported by the Sunsuper Ride to Conquer Cancer in association with the Harry Perkins Institute of Medical Research. D.M.G. was supported by National Institutes of Health grants P50 GM076468 and R01 GM070683.


## Literature Cited


## Associated Data

