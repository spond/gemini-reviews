# Anonymous Manuscript ID: TIME_ANON_0338

*(All identifying metadata, author names, journal titles, DOIs, and publication/citation calendar years have been scrubbed for temporally blinded review.)*

## Abstract

The Genetic Analysis Workshop 14 simulated data presents an interesting, challenging, and plausible example of a complex disease interaction in a dataset. This paper summarizes the ease of detection for each of the simulated Kofendrerd Personality Disorder (KPD) genes across all of the replicates for five standard linkage statistics. Using the KPD affection status, we have analyzed the microsatellite markers flanking each of the disease genes, plus an additional 2 markers that were not linked to any of the disease loci. All markers were analyzed using the following two-point linkage methods: 1) a MMLS, which is a standard admixture LOD score maximized over θ, α, and mode of inheritance, 2) a MLS calculated by GENEHUNTER, 3) the Kong and Cox LOD score as computed by MERLIN, 4) a MOD score (standard heterogeneity LOD maximized over θ, α, and a grid of genetic model parameters), and 5) the PPL, a Bayesian statistic that directly measures the strength of evidence for linkage to a marker. All of the major loci (D1–D4) were detectable with varying probabilities in the different populations. However, the modifier genes (D5 and D6) were difficult to detect, with similar distributions under the null and alternative across populations and statistics. The pooling of the four datasets in each replicate ( n = 350 pedigrees) greatly improved the chance of detecting the major genes using all five methods, but failed to increase the chance to detect D5 and D6.

The Genetic Analysis Workshop 14 simulated data presents an interesting, challenging, and plausible example of a complex disease interaction in a dataset. This paper summarizes the ease of detection for each of the simulated Kofendrerd Personality Disorder (KPD) genes across all of the replicates for five standard linkage statistics. Using the KPD affection status, we have analyzed the microsatellite markers flanking each of the disease genes, plus an additional 2 markers that were not linked to any of the disease loci. All markers were analyzed using the following two-point linkage methods: 1) a MMLS, which is a standard admixture LOD score maximized over θ, α, and mode of inheritance, 2) a MLS calculated by GENEHUNTER, 3) the Kong and Cox LOD score as computed by MERLIN, 4) a MOD score (standard heterogeneity LOD maximized over θ, α, and a grid of genetic model parameters), and 5) the PPL, a Bayesian statistic that directly measures the strength of evidence for linkage to a marker. All of the major loci (D1–D4) were detectable with varying probabilities in the different populations. However, the modifier genes (D5 and D6) were difficult to detect, with similar distributions under the null and alternative across populations and statistics. The pooling of the four datasets in each replicate ( n = 350 pedigrees) greatly improved the chance of detecting the major genes using all five methods, but failed to increase the chance to detect D5 and D6.


## Background

In this study we used the simulated the Genetic Analysis Workshop 14 (GAW14) data using the Kofendrerd Personality Disorder (KPD) affection status as our phenotype. We did this with full knowledge of the generating model. We chose to examine the performance of the statistics by comparing markers flanking a known disease gene location to a pair of markers from a chromosome containing no disease genes. Our data consist of 13 markers: two markers flanking D1, D3, D4, D5, and D6, a single marker flanking D2 (because it falls at the end of chromosome 3), and our arbitrarily chosen unlinked markers, D04S128 and D04S129, which we refer to as markers flanking unlinked locus U1. We analyzed the data from all 100 replicates in each of the four populations as well as creating a pooled dataset of 350 pedigrees created by combining the data from all four populations.


## Methods


## MMLS

The first statistic we examined was the maximized maximum LOD score (MMLS) [ 1 - 3 ] that is a standard admixture heterogeneity LOD score (HLOD) maximized over θ, α, and mode of inheritance (dominant/recessive). MMLS scores were computed using MLIP [ 4 ]. For both the dominant and the recessive model the penetrance for an individual not carrying any disease alleles was set to 1% while the penetrance for genetically affected individuals was set to 80%. The risk allele frequency assumed was 1% under the dominant model and 10% under the recessive model. Note that this differs from the MMLS reported in Hodge et al. [ 2 ], in which homogeneity and different genetic model parameters were assumed.


## MLS

Risch's maximum LOD score statistics (MLS scores) [ 5 , 6 ] were computed using GENEHUNTER [ 7 ], allowing for dominance variance. GENEHUNTER was run, discarding the unaffected individuals. A max-bits setting of 24 was used for all datasets except for replicate 43 of the NY data, which would not finish unless the max-bits was set to 22. All pairs were used with unequal weight to reflect the appropriate per-pedigree influence. Note that GENEHUNTER estimates the identical-by-descent (IBD) sharing under the triangle constraint.


## Kong and Cox LOD scores

Two-point Kong and Cox LOD scores (KCLS) [ 8 ], were computed using MERLIN's [ 9 ] single-point option. A max-bits setting of 50 was used, which caused 26 pedigrees (across all replicates) to be dropped from the analysis. Specifically, 22 replicates of the NY dataset had one pedigree that exceeded 50 bits and two replicates of the NY dataset had two pedigrees which exceeded 50 bits. No replicates had more than two pedigrees that exceeded 50 bits.


## PPL

We examined the performance of a Bayesian statistic, the posterior probability of linkage (PPL) [ 10 - 13 ]. The PPL directly measures the probability that a disease gene is linked to a particular marker (or genomic location in the multipoint case). The PPL incorporates an unknown genetic model by placing priors on the elements of the genetic model and integrating them out of the likelihood [ 14 - 16 ]. We present the results for the PPL in the combined dataset in two ways. First, the PPL-p, which is simply the PPL computed for the entire dataset, and second, the PPL-seq, which is the PPL computed for the entire dataset by sequentially updating across all 4 populations, using the posterior distribution of the recombination fraction, θ, from one analysis as the prior distribution for the next analysis.


## MOD

Finally, we present the results of the MOD [ 17 ] score, which is a standard admixture LOD score (HLOD) maximized over θ, the proportion of linked pedigrees (α), and the genetic model parameters. The MOD scores were computed using MLIP and were maximized over the same set of model parameters used to compute the PPL. Of course, maximizing over a larger portion of the space will result in MOD scores that are greater than MMLS scores for both the linked and unlinked markers.


## Results

The mean and maximum scores for flanking markers at each disease locus and each of the methods for each of the populations and the pooled data are contained in Table 1 . In the interest of space, both flanking markers have been pooled into a single score for each disease locus (mean/max are across both replicates and flanking markers) except in the case of disease locus 2, which had only a single flanking marker.

In general, MMLS and MOD scores are larger than MLS and KCLS scores. However, the MMLS and MOD scores were also higher for the unlinked locus than the other two methods, so that the increase in score does not necessarily indicate an increase in power. Nonetheless, there are a few things that can be determined from Table 1 . While disease loci 1–4 are relatively easy to identify, the results for loci 5 and 6 do not deviate far from their behavior under the null. Additionally, the means varied as a function of the population for each dataset. Pooling the data greatly increased the mean scores for the linked loci. This occurred despite the fact that the underlying disease mechanism varied widely from locus to locus.

Table 2 presents the value of P, which we define as the percentage of replicates in which the maximum score for one of the flanking markers exceeded the maximum value received under the null distribution, once again across replicates. P represents a rough approximation to the chance that each marker would be detected by a 0.01 size test (except for the D2 case for which P would be conservative). The method receiving the highest score at each population/locus is indicated in bold font in the tables. Perhaps surprisingly, there is no clear winner when the performance of these statistics were compared in this way. As indicated by the means, D5 and D6 were particularly difficult to detect, with no statistic/dataset combination able to achieve a P greater than 7%.


## Conclusion

We have compared the performance of five statistics, the MMLS, the MLS, the KCLS, the MOD, and the PPL, by examining markers flanking the known disease locations in the GAW14 simulated data. By computing P, which is an empirical measure of the power, we are able to compare statistics that have different scales. We find that none of the statistics emerges a clear victor, with different statistics having greater power depending on which disease locus and population were examined. However, it is surprising that the MMLS and MOD score, which make use of the entire pedigree structure (as opposed to the MLS, which uses only affected sib pairs, and KCLS, which uses affected relative pairs), and whose scores were calculated without any trimming or dropping of large pedigrees, were not able to utilize this information to their advantage in the NY population, where the sample consists of extended pedigrees. This is due to the high values of these statistics obtained under the null. The PPL performs better in the NY dataset, using data from the entire pedigree, without a similar inflation of null values. D1–D4 appear detectable, with maximum scores in the range that would indicate linkage. However, values of P were surprisingly low for these loci, especially since the maximum values under the null, presented in Table 1 , would scarcely be considered adequate to conclude linkage. Pooling the samples for D1–D4 increased power to the range where linkage was consistently detectable, despite the fact that variation in the diagnostic schemes causes the genetic model to differ from dataset to dataset. Loci D5 and D6 were not readily detectable in any of the populations or in the pooled data.


## Authors' contributions

MWL performed analyses and prepared a draft of the manuscript. MWL, MAS, and VJV contributed computing resources. All authors contributed to study design and editing, and approved the final manuscript.