# Manuscript ID: ANON_44

## ABSTRACT

A major challenge of biology is understanding the relationship between molecular genetic variation and variation in quantitative traits, including fitness. This relationship determines our ability to predict phenotypes from genotypes and to understand how evolutionary forces shape variation within and between species. Previous efforts to dissect the genotype-phenotype map were based on incomplete genotypic information. Here, we describe the  Drosophila melanogaster  Genetic Reference Panel (DGRP), a community resource for analysis of population genomics and quantitative traits. The DGRP consists of fully sequenced inbred lines derived from a natural population. Population genomic analyses reveal reduced polymorphism in centromeric autosomal regions and the  X  chromosome, evidence for positive and negative selection, and rapid evolution of the  X  chromosome. Many variants in novel genes, most at low frequency, are associated with quantitative traits and explain a large fraction of the phenotypic variance. The DGRP facilitates genotype-phenotype mapping using the power of  Drosophila  genetics.

## MAIN TEXT

Understanding how molecular variation maps to phenotypic variation for quantitative traits is central for understanding evolution, animal and plant breeding, and personalized medicine 1 , 2 . The principles of mapping quantitative trait loci (QTLs) by linkage to, or association with, marker loci are conceptually simple 1 , 2 . However, we have not yet achieved our goal of explaining genetic variation for quantitative traits in terms of the underlying genes; additive, epistatic, and pleiotropic effects as well as phenotypic plasticity of segregating alleles; and the molecular [REDACTED_VENUE], population frequency and evolutionary dynamics of causal variants. Efforts to dissect the genotype-phenotype map in model organisms 3 , 4  and humans  5 - 7  have revealed unexpected complexities, implicating many, novel loci; pervasive pleiotropy; and context-dependent effects.

Model organism reference populations of inbred strains that can be shared among laboratories studying diverse phenotypes, and for which environmental conditions can be controlled and manipulated, greatly facilitate efforts to dissect the genetic architecture of quantitative traits 3 , 4 . Measuring many individuals of the same homozygous genotype increases the accuracy of the estimates of genotypic value 1  and the power to detect variants; and genotypes of molecular markers need only be obtained once. We constructed the  Drosophila melanogaster  Genetic Reference Panel (DGRP) as such a community resource. Unlike previous populations of recombinant inbred lines derived from limited samples of genetic variation, the DGRP consists of 192 inbred strains derived from a single outbred population. The DGRP contains a representative sample of naturally segregating genetic variation, has an ultra-fine grained recombination map suitable for precise localization of causal variants, and has almost complete euchromatic sequence information.

Here, we describe molecular and phenotypic variation in 168 re-sequenced lines comprising Freeze 1.0 of the DGRP, population genomic inferences of patterns of polymorphism and divergence and their correlation with genomic features, local recombination rate and selection acting on this population, genome wide association mapping analyses for three quantitative traits, and tools facilitating the use of this resource.


## Molecular variation in the DGRP


We constructed the DGRP by collecting mated females from the Raleigh, USA population, followed by 20 generations of full-sib inbreeding of their progeny. We sequenced 168 DGRP lines using a combination of Illumina and 454 sequencing technology: 29 of the lines were sequenced using both platforms, 129 lines have only Illumina sequence, and 10 lines have only 454 sequence. We mapped sequence reads to the  D. melanogaster  reference genome, re-calibrated base quality scores, and locally re-aligned Illumina reads. Mean sequence coverage was 21.4x per line for Illumina sequences and 12.1x per line for 454 sequences ( Supplementary Table 1 ). On average, we assayed 113.5Mb (94.25%) of the euchromatic reference sequence with ~22,000 read mapping gaps per line ( Supplementary Table 2 ). We called 4,672,297 single nucleotide polymorphisms (SNPs) using the Joint Genotyper for Inbred Lines (JGIL) 8 , which takes into account coverage and quality sequencing statistics, and expected allele frequencies after 20 generations of inbreeding from an outbred population initially in Hardy-Weinberg equilibrium. In cases where base calls were made by both technologies, concordance was 99.36% ( Supplementary Table 3 ).

The SNP site frequency distribution ( Fig. 1a ) is characterized by a majority of low frequency variants. The numbers of SNPs vary by chromosome and site class ( Fig. 1b ). Linkage disequilibrium 9  (LD) decays to  r 2  = 0.2 on average within 10 bp on autosomes and 30 bp on the  X  chromosome ( Fig. 1c ,  Supplementary Fig. 1 ). This difference is expected because the population size of the  X  chromosome is ¾ that of autosomes, and the  X  chromosome can experience greater purifying selection due to exposure of deleterious recessive alleles in hemizygous males. There is little evidence of global population structure in the DGRP ( Fig. 1d ,  Supplementary Fig. 2 ). The rapid decline in LD locally and lack of global population structure are favorable for genome wide association mapping.

Not all SNPs are fixed within individual DGRP lines ( Supplementary Table 4 ). The expected inbreeding coefficient ( F ) after 20 generations of full-sib inbreeding 1  is  F  = 0.986; therefore, we expect some SNPs to remain segregating by chance. Segregating SNPs can also arise from new mutations, or if natural selection opposes inbreeding, due to true overdominance for fitness at individual loci or associative overdominance due to complementary deleterious alleles that are closely linked or in segregating inversions.

We identified 390,873 microsatellite loci, 105,799 of which were polymorphic ( Supplementary Table 5 ); 36,810 transposable element (TE) insertion sites and 197,402 total insertions ( Supplementary Table 6 ). On average, each line contained 1,175 TE insertions ( Supplementary Table 6 ), although most TE insertion sites (25,562) were present in only one line ( Supplementary Table 7 ). We identified 149 TE families. The number of copies per family varied greatly from an average of 315.7  INE-1  elements per line to an average of 0.003  Gandalf-Dkoe-like  elements per line ( Supplementary Table 8 ).

Wolbachia pipientis  is a maternally inherited bacterium found in insects, including  Drosophila , and can affect reproduction 10 . We assessed  Wolbachia  infection status in the DGRP lines to account for it in analyses of genotype-phenotype associations, and found 51.2% of lines harboring sufficient  Wolbachia  DNA to imply infection ( Supplementary Table 9 ).


## Polymorphism and divergence


We used the DGRP Illumina sequence data and genome sequences from  D. simulans  and  D. yakuba 11  to perform genome wide analyses of polymorphism and divergence, assess the association of these parameters with genomic features and the recombination landscape, and infer the historical action of selection on a much larger scale than had been possible previously 12 - 17 . We computed polymorphism ( π 18  and  θ 19 ) and divergence ( k 20 ) for the whole genome, by chromosome arm ( X ,  2L ,  2R ,  3L ,  3R ), by chromosome region (three regions of equal size in Mb – telomeric, middle and centromeric), in 50 kbp non-overlapping windows, and by site class (synonymous and non-synonymous sites within coding sequences, and intronic, UTR and intergenic sites) ( Supplementary Tables 10  and  11 ).

Averaged over the entire genome,  π  = 0.0056 and  θ  = 0.0067, similar to previous estimates from North American populations 17 , 21 . Average polymorphism on the  X  chromosome ( π X  = 0.0040) is reduced relative to the autosomes ( π A  = 0.0060) ( X / A  ratio = 0.67, Wilcoxon test  p  = 0), even after correcting for the  X / A  effective population size ( X 4/3  = 0.0054, Wilcoxon test  p  < 0.00002;  Supplementary Table 10 ). Autosomal nucleotide diversity is reduced on average 2.4 fold in centromeric regions relative to non-centromeric regions, and at the telomeres ( Fig. 2a ,  Supplementary Table 10 ), while diversity is relatively constant along the  X  chromosome. Thus,  π X  >  π A  in centromeric regions, but  π A  >  π X  in other chromosomal regions ( Fig. 2a ,  Supplementary Table 10 ).

Genes on the  X  chromosome evolve faster ( k X  = 0.140) than autosomal genes ( k A  = 0.126) ( X/A  ratio = 1.131, Wilcoxon test  p  =0) ( Figure 2b ,  Supplementary Table 10 ). Divergence is more uniform ( CV k  = 0.2841) across chromosome arms than is polymorphism ( CV π  = 0.4265). The peaks of divergence near the centromeres could be attributable to the reduced quality of alignments in these regions. Patterns of divergence are similar regardless of the outgroup species used ( Fig. 2b ,  Supplementary Table 11 ).

The pattern of polymorphism and divergence by site class is consistent within and among chromosomes ( π ( k ) Synonymous  >  π ( k ) Intron  >  π ( k ) Intergenic  >  π ( k ) UTR  >  π ( k ) Non-synonymous ), in agreement with previous studies on smaller data sets 13 , 16  ( Supplementary Figs. 3  and  4 ,  Supplementary Table 11 ). Polymorphism levels between synonymous and non-synonymous sites differ by an order of magnitude. Variation and divergence patterns within the site classes generally follow the same patterns observed overall, with reduced polymorphism for all site classes on the  X  chromosome relative to autosomes, increased  X  chromosome divergence relative to autosomes for all but synonymous sites, decreased polymorphism in centromeric regions, and greater variation among regions and arms for polymorphism than for divergence. Other diversity measures and more detailed patterns at different window-sizes for each chromosome arm can be accessed from the Population  Drosophila  Browser (PopDrowser) ( Table 1 ,  Supplementary Methods ).


## Recombination landscape


Evolutionary models of hitchhiking and background selection 22 , 23  predict a positive correlation between polymorphism and recombination rate. This expectation is realized in regions where recombination is < 2  cM/Mb  (Spearman’s  ρ  = 0.471,  p  = 0), but recombination and polymorphism are independent in regions where recombination exceeds 2  cM/Mb  (Spearman’s  ρ  = −0.0044,  p  = 0.987) ( Fig. 2a ,  Supplementary Table 12 ). The average rate of recombination of the  X  chromosome (2.9 cM/Mb) is greater than that of autosomes (2.1 cM/Mb), which may account for the low overall  X -linked correlation between recombination rate and  π.  The lack of correlation between recombination and divergence ( Supplementary Table 12 ) excludes mutation associated with recombination as the cause of the correlation. We assessed the independent effects of recombination rate, divergence, chromosome region and gene density on nucleotide variation of autosomes and the  X  chromosome ( Supplementary Table 13 ). Recombination is the major predictor of polymorphism on the  X  chromosome and autosomes; however, the significant effect of autosomal chromosome region remains after accounting for variation in recombination rates between centromeric and non-centromeric regions.


## Selection regimes


We used the standard 24  and generalized 13 , 25 , 26  McDonald Kreitman tests (MKT) to scan the genome for evidence of selection. These tests compare the ratio of polymorphism at a selected site with that of a neutral site to the ratio of divergence at a selected site to divergence at a neutral site. The standard MKT is applied to coding sequences, and synonymous and non-synonymous sites are used as putative neutral and selected sites, respectively. The generalized MKT is applied to non-coding sequences and uses four-fold degenerate sites as neutral sites. Using polymorphism and divergence data avoids confounding inference of selection with mutation rate differences, and restricting the tests to closely linked sites controls for shared evolutionary history 27 - 29 . We infer adaptive divergence when there is an excess of divergence relative to polymorphism, and segregation of slightly deleterious mutations when there is an excess of polymorphism over divergence. Estimates of  α , the proportion of adaptive divergence, are biased downwards by low frequency, slightly deleterious mutations 30 , 31 . Rather than eliminate low frequency variants 32 , we incorporated information on the site frequency distribution to the MKT test framework to obtain estimates of the proportion of sites that are strongly deleterious ( d ), weakly deleterious ( b ), neutral ( f ), and recently neutral ( ) at segregating sites, as well as unbiased estimates of  α  ( Supplementary Methods ).


## Deleterious and neutral sites


Averaged over the entire genome, we infer that 58.5% of the segregating sites are neutral or nearly neutral, 1.9% are weakly deleterious, and 39.6% are strongly deleterious. However, these proportions vary between the  X  chromosome and autosomes, site classes, and chromosome regions ( Supplementary Tables 14 - 16 ,  Fig. 3 ). Non-synonymous sites are the most constrained ( d  = 77.6%), while in non-coding sites  d  ranges from 29.1% in 5′UTRs to 41.3% in 3′intergenic regions. The inferred pattern of selection differs between autosomal centromeric and non-centromeric regions:  d  is reduced and  f  is increased in centromeric regions for all site categories ( Fig. 3 ). We observe an excess of polymorphism relative to divergence in autosomal centromeric regions, even after correcting for weakly deleterious mutations, implying a relaxation of selection from the time of separation of  D. melanogaster  and  D. yakuba . Since selection coefficients depend on the effective population size 33  ( N e ), this could occur if the recombination rate has specifically diminished in centromeric regions during the divergence between  D. melanogaster  and  D. yakuba ; or with an overall reduction of  N e  associated with the colonization of North American habitats 34 , 35 . In the latter case, we expect a genome-wide signature of an excess of low frequency polymorphisms and of polymorphism relative to divergence, exacerbated in regions of low recombination. We indeed find an excess of low frequency polymorphism relative to neutral expectation as indicated by the negative estimates of Tajima’s  D  statistic 36  (  D  = −0.686 averaged over the whole genome and  D  = −0.997 in autosomal centromeric regions). In contrast, the  X  chromosome does not show a differential pattern of selection in the centromeric region, has a lower fraction of relaxation of selection, fewer neutral alleles, and a higher percentage of strongly deleterious alleles for all site classes and regions ( Fig. 3 ,  Supplementary Tables 14 - 16 ).

TE insertions are thought to be largely deleterious. There are more singleton insertions in regions of high recombination (≥ 2cM/Mb) and more insertions shared in multiple lines in regions of low recombination (< 2cM/Mb) (Fisher’s exact test  p  = 0), and comparison of observed and expected site occupancy spectra reveals an excess of singleton insertions ( p  = 0,  Supplementary Fig. 5 ).


## Adaptive fixation


We find substantial evidence for positive selection in autosomal non-centromeric regions and the  X  chromosome ( Fig. 2c ,  Supplementary Tables 15 ,  17 ). We estimated  α  by aggregating all sites in each region analyzed to avoid underestimation by averaging across genes 37  in comparisons of chromosomes, regions and site classes. We also computed the Direction of Selection,  DoS 38 , which is positive with adaptive selection, zero under neutrality, and negative when weakly deleterious or new nearly neutral mutations are segregating. Estimates of  α  from the standard and generalized MKT indicate that on average 25.2% of the fixed sites between  D. melanogaster  and  D. yakuba  are adaptive, ranging from 30% in introns to 7% in UTR sites ( Supplementary Fig. 6 ). Estimates of  DoS  and  α  are negative for non-synonymous and UTR sites in the autosomal centromeres, consistent with underestimating the fraction of adaptive substitutions in regions of low recombination because weakly deleterious or nearly neutral mutations are more common than adaptive fixations. The majority of adaptive fixation on autosomes occurs in non-centromeric regions ( Fig. 2c ). We find over four times as many adaptive fixations on the  X  chromosome relative to autosomes. The pattern holds for all site classes, in particular non-synonymous sites and UTRs, as well as individual genes; and is not solely due to the autosomal centromeric effect ( Supplementary Table 15 ;  Supplementary Figs. 6  and  7 ). Finally, when we consider  DoS  in recombination environments above and below 2 cM/Mb, we find greater adaptive propensity in genes whose recombination context is ≥ 2 cM/Mb (Wilcoxon test,  p  = 0) ( Supplementary Fig. 8 ).

To understand the global patterns of divergence and constraint across functional classes of genes, we examined the distributions of  ω  ( d N /d S , the ratio of non-synonymous to synonymous divergence) and  DoS  across Gene Ontology (GO) categories. The 4.9% GO categories with significantly elevated  DoS  include the biological process categories of behavior, developmental process involved in reproduction, reproduction and ion transport ( Supplementary Table 18 ). Recombination context is the major determinant of variation in  DoS  ( Supplementary Table 19 ) while GO category is as important as recombinational context for predicting variation in  ω  ( Supplementary Table 19 ).

GO categories enriched for positive  DoS  values differ from those associated with high values of  ω  ( Supplementary Table 18 ), indicating that positive selection does not occur necessarily on genes with high  ω  values. If adaptive substitutions are common, high values of  ω  reflect the joint contributions of neutral and adaptive substitutions. Further, equating high constraint (low  ω ) with functional importance overlooks the functional role of adaptive changes 16 . Unlike  ω, DoS  takes into account the constraints inferred from the current polymorphism, distinguishing negative, neutral and adaptive selection.


## Genome wide association of phenotypes with molecular variation


We measured resistance to starvation stress, chill coma recovery time, and startle response 39  in the DGRP. We found considerable genetic variation for all traits, with high broad sense heritabilities. We also found variation in sex dimorphism for starvation resistance and chill coma recovery with cross-sex genetic correlations significantly different from unity ( Supplementary Tables 20 - 22 ).

We performed genome wide association (GWA) analyses for these traits, using the 2,490,165 SNPs and 77,756 microsatellites for which the minor allele was represented in four or more lines, using single locus analyses pooled across sexes and separately for males and females. At  p  < 10 −5  ( p  < 10 −6 ), we find 203 (32) SNPs and 2 (0) microsatellites associated with starvation resistance; 90 (7) SNPs and 4 (2) microsatellites associated with startle response; and 235 (45) SNPs and 5 (3) microsatellites associated with chill coma recovery time ( Fig. 4a ,  Supplementary Fig. 9 ,  Supplementary Tables 23  and  24 ). The minor allele frequencies for most of the associated SNPs are low, and there is an inverse relationship between effect sizes and minor allele frequency ( Supplementary Fig. 10 ).

The DGRP is a powerful tool for rapidly reducing the search space for molecular variants affecting quantitative traits from the entire genome to candidate polymorphisms and genes. While we cannot infer which of these polymorphisms are causal due to LD between SNPs in close physical proximity as well as occasional spurious long range LD ( Fig. 4a ,  Supplementary Fig. 9 ), the candidate gene lists are likely to be enriched for causal variants. The majority of associations are in computationally predicted genes or genes with annotated functions not obviously associated with the three traits. However, genes previously associated with startle response 40  ( Sema-1a  and  Eip-75B ) and starvation resistance 41  ( pnt ) were identified in this study; and a SNP in  CG3213 , previously identified in a  Drosophila  obesity screen 42 , is associated with variation in starvation resistance. Several genes associated with quantitative traits are rapidly evolving ( psq ,  Egfr ;  Supplementary Tables 17 ,  23 ) or are plausible candidates based on SNP or Gene Ontology annotations ( Supplementary Table 23 ).


## Predicting phenotypes from genotypes


We used regression models to predict trait phenotypes from SNP genotypes and estimate the total variance explained by SNPs. The latter cannot be done by summing the individual contributions of the single marker effects because markers are not completely independent, and estimates of effects of single markers are biased when more than one locus affecting the trait segregates in the population. We derived gene-centered multiple regression models to estimate the effects of multiple SNPs simultaneously. In all cases 6-10 SNPs explain from 51-72% of the phenotypic variance and 65-90% of the genetic variance ( Supplementary Tables 25  and  26 ;  Supplementary Figs. 11 - 13 ). We also derived partial least square regression models using all SNPs for which the single marker effect was significant at  p  < 10 −5 . These models explain 72-85% of the phenotypic variance ( Fig. 4b-c ,  Supplementary Fig. 14 ).


## Discussion


The DGRP lines, sequences, variant calls, phenotypes, and web tools for molecular population genomics and GWA analysis are publicly available ( Table 1 ). The DGRP lines contain at least 4,672,297 SNPs, 105,799 polymorphic microsatellites and 36,810 TEs, as well as insertion/deletion events and copy number variants and are a valuable resource for understanding the genetic architecture of quantitative traits of ecological and evolutionary relevance as well as  Drosophila  models of human quantitative traits. These novel mutations have survived the sieve of natural selection and will enhance the functional annotation of the  Drosophila  genome, complementing the  Drosophila  Gene Disruption Project 43  and the  Drosophila  modENCODE project 44 . .

Genome-wide molecular population genetic analyses show that patterns of polymorphism, but not divergence, differ by autosomal chromosome region, and between the  X  chromosome and autosomes. Polymorphism is lower in autosomal centromeric than non-centromeric regions, but not for the  X  chromosome. We hypothesize that the correlation of polymorphism with recombination in regions where recombination is < 2 cM/Mb is due to the reduced effective population size in regions of low recombination 9 . Selection is less efficient in regions of low recombination 33 , consistent with our observation that the fraction of strongly deleterious mutations and positively selected sites are reduced in these regions.

All molecular population genomic analyses support the ‘faster  X ’ hypothesis 45 . Relative to the autosomes, the  X  chromosome exhibits lower polymorphism, faster rates of molecular evolution, a higher percentage of gene regions undergoing adaptive evolution, a higher fraction of strongly deleterious sites, and a lower level of weak negative selection and relaxation of selection. New  X -linked mutations are directly exposed to selection each generation in hemizygous males, and the  X  chromosome has greater recombination than autosomes 45 ; both of these factors could contribute to this observation.

GWA analyses of three fitness-related quantitative traits reveal hundreds of novel candidate genes, highlighting our ignorance of the genetic basis of complex traits. Most variants associated with the traits are at low frequency, and there is an inverse relationship between frequency and effect. Given that low frequency alleles are likely to be deleterious for traits under directional or stabilizing selection, these results are consistent with the mutation-selection balance hypothesis 1  for the maintenance of quantitative genetic variation. Regression models incorporating significant SNPs explain most of the phenotypic variance of the traits, in contrast with human association studies, where significant SNPs have tiny effects and together explain a small fraction of the total phenotypic variance 7 . If the genetic architecture of human complex traits is also dominated by low frequency causal alleles, we expect estimates of effect size based on LD with common variants to be strongly biased downwards.

In the future, the full power of  Drosophila  genetics can be applied to validating marker-trait associations: mutations, RNAi constructs and QTL mapping populations. The DGRP is an ideal resource for systems genetics analyses of the relationship between molecular variation, causal molecular networks, and genetic variation for complex traits 4 , 39 , 46 , and will anchor evolutionary studies in comparison with sequenced  Drosophila  species to assess to what extent variation within a species corresponds to variation among species.


## Supplementary Material


1

8

9

10

11

2

3

4

5

6

7


### Table 1: Community resources


Resource | Location

DGRP Lines | Bloomington  Drosophila  Stock Center http://flystocks.bio.indiana.edu/Browse/RAL.php

Sequences | Baylor College of Medicine Human Genome Sequencing Center http://www.hgsc.bcm.tmc.edu/project-species-i-DGRP_lines.hgsc National Center for Biotechnology Information Short Read Archive http://www.ncbi.nlm.nih.gov/sra?term=DGRP [AUTHOR] Laboratory http://dgrp.gnets.ncsu.edu/

Read Alignments | Baylor College of Medicine Human Genome Sequencing Center http://www.hgsc.bcm.tmc.edu/projects/dgrp/

SNPs | Baylor College of Medicine Human Genome Sequencing Center http://www.hgsc.bcm.tmc.edu/projects/dgrp/freeze1_July_2010/snp_calls/ National Center for Biotechnology Information dbSNP http://www.ncbi.nlm.nih.gov/SNP/snp_viewBatch.cgi?sbid=1052186 [AUTHOR] Laboratory http://dgrp.gnets.ncsu.edu/

Microsatellites | Baylor College of Medicine Human Genome Sequencing Center http://www.hgsc.bcm.tmc.edu/projects/dgrp/freeze1_July_2010/microsat_calls/ [AUTHOR] Laboratory http://genome.vbi.vt.edu/public/DGRP/

TEs | [AUTHOR] Laboratory http://dgrp.gnets.ncsu.edu/

Molecular Population Genomics | PopDrowser http://PopDrowser.uab.cat

Phenotypes | [AUTHOR] Laboratory http://dgrp.gnets.ncsu.edu/

GWA Analysis | [AUTHOR] Laboratory http://dgrp.gnets.ncsu.edu/