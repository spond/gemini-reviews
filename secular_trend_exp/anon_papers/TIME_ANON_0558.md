# Anonymous Manuscript ID: TIME_ANON_0558

*(All identifying metadata, author names, journal titles, DOIs, and publication/citation calendar years have been scrubbed for temporally blinded review.)*

## Abstract

The amount of functional genomic information has been growing rapidly but remains largely unused in genomic selection. Genomic prediction and estimation using haplotypes in genome regions with functional elements such as all genes of the genome can be an approach to integrate functional and structural genomic information for genomic selection. Towards this goal, this article develops a new haplotype approach for genomic prediction and estimation.

A multi-allelic haplotype model treating each haplotype as an ‘allele’ was developed for genomic prediction and estimation based on the partition of a multi-allelic genotypic value into additive and dominance values. Each additive value is expressed as a function of h − 1 additive effects, where h = number of alleles or haplotypes, and each dominance value is expressed as a function of h(h − 1)/2 dominance effects. For a sample of q individuals, the limit number of effects is 2q − 1 for additive effects and is the number of heterozygous genotypes for dominance effects. Additive values are factorized as a product between the additive model matrix and the h − 1 additive effects, and dominance values are factorized as a product between the dominance model matrix and the h(h − 1)/2 dominance effects. Genomic additive relationship matrix is defined as a function of the haplotype model matrix for additive effects, and genomic dominance relationship matrix is defined as a function of the haplotype model matrix for dominance effects. Based on these results, a mixed model implementation for genomic prediction and variance component estimation that jointly use haplotypes and single markers is established, including two computing strategies for genomic prediction and variance component estimation with identical results.

The multi-allelic genetic partition fills a theoretical gap in genetic partition by providing general formulations for partitioning multi-allelic genotypic values and provides a haplotype method based on the quantitative genetics model towards the utilization of functional and structural genomic information for genomic prediction and estimation.

Keywords: Haplotype, Genomic selection, Variance component, Heritability, BLUP, REML


## Background

Genomic best linear unbiased prediction (GBLUP) using genome-wide single nucleotide polymorphism (SNP) markers can utilize a wealth of theoretical results and computational strategies of best linear unbiased prediction (BLUP) [ 1 ] that has become a standard approach for genetic evaluation, with dairy cattle having the most widespread use of BLUP worldwide [ 2 – 5 ]. The implementation of GBLUP within the BLUP framework is made possible by a genomic relationship matrix that replaces the pedigree relationship matrix in BLUP [ 6 ]. With genomic relationship matrix established, genomic estimation of variance components can also readily use the method of restricted maximum likelihood estimation (REML) [ 7 ], to be referred to as GREML (genomic REML). Using a quantitative genetics model as the unifying model, genomic relationship matrix is formulated by equaling the covariance of genomic values between two individuals to the corresponding pedigree covariance [ 8 , 9 ]. Previously defined genomic relationships based on standardization of SNP coding [ 6 , 8 , 10 , 11 ] can be considered as special cases of this unifying approach [ 9 ]. The quantitative genetics model partitions a genotypic value as the summation of a common mean, breeding value and dominance deviation [ 12 – 18 ]. Using matrix notations, this partition can be expressed as: g = 1 μ + a + d = 1 μ + W α α + W δ δ , where μ = common mean, 1 = column vector of 1’s, a = breeding values (additive values), d = dominance deviations (dominance values), α = SNP additive effects, δ = SNP dominance effects, W α = model matrix of α as a function of SNP allele frequencies, and W δ = model matrix of δ as a function of SNP allele frequencies. With the factorization of a = W α α and d = W δ δ , genomic additive relationship is a function of W α W α ' and genomic dominance relationship is a function of W δ W δ ' [ 9 ]. This approach for defining genomic relationships was only available for bi-allelic loci. Although SNPs are bi-allelic loci, the issue of multi-allelic loci for genomic prediction and estimation arises if each haplotype is treated as an ‘allele’ and the haplotype block containing the haplotypes is treated as a ‘locus’. For a multi-allelic locus, the partition of a genotypic value into additive and dominance values ( g = 1 μ + a + d ) was available [ 17 ] and the multi-allelic factorization of a = W α α and d = W δ δ was available for three alleles [ 19 ]. However, general factorization formulations for an arbitrary number of alleles were unavailable, and a method using such multi-allelic haplotype model for genomic prediction and estimation was unavailable.

Haplotype analysis is advantageous over single-locus analysis for several reasons: a haplotype is a functional unit [ 20 ], a haplotype contains combined effects of tightly linked cis-acting causal variants [ 21 , 22 ], a phenotype is affected by multiple causal loci with weak LD (LD = linkage disequilibrium) [ 23 ], or a genomic region is subjected to selection with stronger LD than genome regions unaffected by selection [ 24 , 25 ]. Haplotype analysis has been widely used in genetic and genomic studies [ 22 , 26 – 28 ]. Relatively limited studies were available on using haplotypes compared to the literature on using single SNPs for genomic prediction. Methods to define haplotype blocks for genomic prediction included a constant number of SNPs per SNP block [ 29 , 30 ], fixed block length [ 31 ], or LD blocks [ 32 ]. Haplotype coding methods for genomic prediction and estimation included 2-1-0 copies of a haplotype in the two-haplotype genotype [ 30 , 33 ], or maternal or paternal haplotype [ 29 ]. Haplotype mixed model methods based on the quantitative genetics model with multi-allelic factorization of additive and dominance values were unavailable for genomic prediction and estimation. Functional genomic information has been growing rapidly but remains largely unused in genomic selection. Simulation study showed that genomic prediction using causal mutations could substantially improve prediction accuracy [ 34 ], and using SNPs in transcriptional regions [ 35 ] or location specific priors based on QTL mapping results [ 36 ] improved prediction accuracy. Haplotype analysis can be a useful tool to account for joint allelic effects unaccounted for by single-SNP analysis and we have obtained encouraging preliminary results of using haplotype analysis of functional genomic information [ 37 , 38 ].

The purpose of this article is to develop a quantitative genetics based multi-allelic haplotype model as an alternative method to single-SNP analysis towards the integration of functional and structural genomic information for genomic selection. This development includes deriving general multi-allelic partition of genotypic values with factorization for defining genomic relationships using haplotypes, and deriving mixed model formulations for genomic prediction and estimation that can use haplotypes separately or jointly with single SNPs.


## Methods


## Allelic mean and population mean of multi-allelic genotypic values

A set of m SNP markers are assumed available, and r haplotype blocks are defined from some of the m SNPs across the genome. Each haplotype block is treated as a ‘locus’ and each haplotype within the haplotype block is treated as an ‘allele’. Each locus (haplotype block) is assumed to have h alleles (haplotypes) denoted by A i , …, A h , with allele frequency of p i for A i , i = 1, …, h, and ∑ i = 1 h p i = 1. The allelic array in the population is ∑ i = 1 h p i A i . Let P ij = frequency of A i A j genotype, ∑ i = 1 h ∑ j = 1 h P ij A i A j = the genotypic array of the population, and g ij = genotypic value of A i A j genotype, i,j = 1,…,h. Hardy-Weinberg equilibrium (HWE) is assumed so that the genotypic array of the population is the squared allelic array, i.e., ∑ i = 1 h ∑ j = 1 h P ij A i A j = (∑ i = 1 h p i A i ) 2 . Allele frequency of A i is calculated as:

The allelic mean of A i allele is the weighted mean of all genotypic values with the A i allele, with each genotypic value weighted by the number of copies of the A i allele the genotype carries. The general expression of the allelic mean without requiring HWE is a conditional mean [ 13 ] and simplifies to a weighted average of genotypic values with allele frequencies as the weights under the HWE assumption [ 13 , 17 ], i.e.,

The population mean is the mean of all genotypic values in the population. The general formula without requiring HWE and its expression as a weighted average of allelic means with allele frequencies as the weights requiring HWE are:

The expressions of μ i = ∑ j = 1 h p j g ij and μ = ∑ k = 1 h p k μ k play an important role in the derivations to factorize additive and dominance values and in defining fundamental genetic parameters of quantitative traits.


## Multi-allelic effect, additive effect, additive value

The allelic effect (average effect) of allele A i (i = 1,…h) is the deviation of the allelic mean from the population mean. From Eqs. 2 and 3 , the allelic effect of A i is:

where α ij is the additive effect or the average effect of gene substitution that is the difference between the allelic effects of the two alleles defined by Eq. 4 , i.e.,

For h alleles, h(h − 1)/2 α ij parameters of Eq. 5 are possible but these parameters are not independent for all ij values. An example of this dependency is:

Based on Eq. 6 , h-1 independent additive effects can be defined:

where μ 1 = allelic mean of allele 1 that is used as the reference allele (e.g., defining the most frequent allele as ‘allele 1’). It is readily seen that α ii = 0. The derivation process will allow the presence of α ii but the final results will be based on the h−1 independent additive effects of α lk defined by Eq. 7 . All the h(h − 1)/2 possible α ij parameters can be expressed in terms of the h−1 independent α lk parameters through Eq. 6 . The additive value (breeding value) of genotype A i A j is the summation of the two allelic effects of the genotype, i.e.,

Each additive value defined by Eq. 8 will be shown to be a function of all h−1 additive effects defined by Eq. 7 .


## Dominance effect and dominance value

Dominance effect of A i A j genotype (δ ij ) is the deviation of the heterozygous genotypic value from the average of the two homozygous genotypic values, i.e.,

With the above definition, dominance effect is the unique effect of a heterozygous genotype. Therefore, the number of dominance effects is the same as number of heterozygous genotypes, and the maximum number of dominance effects is h(h − 1)/2. It is readily seen from Eq. 9 that δ ii = 0. The derivation process will allow the presence of δ ii but the final results will not have δ ii . Dominance value or dominance deviation is the deviation of the genotypic value from the common mean and additive value, i.e.,

An important difference between ‘dominance value’ and ‘dominance effect’ is that a homozygous genotype may have non-zero dominance value but always has zero dominance effect. Each dominance value defined by Eq. 10 will be shown to be a function of all h(h − 1)/2 dominance effects defined by Eq. 9 .


## Multi-allelic partition of genotypic value and variance

The genotypic value of a multi-allelic genotype has the same partition as for a bi-allelic locus [ 17 ], i.e.,

with E(a ij ) = 0 and E(d ij ) = 0. The multi-allelic genotypic variance (σ g 2 ) also has the same partition as for a bi-allelic locus [ 17 ], i.e., σ g 2 = σ a 2 + σ d 2 , where σ a 2 = additive variance, and σ d 2 = dominance variance. The multi-allelic haplotype model to be developed starts with the factorization of the additive and dominance values in Eq. 11 .


## Results and discussion


## Factorization of additive and dominance values

From Eqs. 4 – 7 , an allelic effect can be expressed as:

where α lk is defined by Eq. 7 . Equation 12 shows that an allelic effect is a function of all h-1 parameters of additive effects denoted by α lk . The additive values (breeding values) of A i A j and A i A i genotypes can be expressed as:

In Eqs. 13 and 14 , α li = 0 if i = 1 and α 1j = 0 if j = 1. From Eqs. 1 – 3 and 9 – 10 , the dominance value of the A i A j genotype can be expressed as

In Eq. 15 , the quantity g ij − g ik − g jf + g kf has two positive terms and two negative terms, and each subscript is associated with a positive term and a negative term. Using this fact and the definition of dominance effect (δ ij ) of Eq. 9 with δ ii = 0, g ij − g ik − g jf + g kf can be expressed as:

Combining Eqs. 15 and 16 with Eq. 10 and using p j = 1 − ∑ k ≠ j h p k (Eq. 1 ) yields:

Combining Eqs. 17 and 18 yields:

Equations 13 and 14 show that each additive value is a function of all h − 1 additive effects defined by Eq. 7 , and Eqs. 19 – 20 show that each dominance value is a function of all h(h − 1)/2 dominance effects defined by Eq. 9 . Equations 13 and 14 provide the additive coding and Eqs. 19 and 20 provide the dominance coding of each multi-allelic genotype for the mixed model implementation.


## Multi-allelic haplotype model based on multi-allelic genetic partition

Using the results of factorization of additive and dominance values given by Eqs. 13 – 14 and 19 – 20 , the multi-allelic haplotype model treating each haplotype as an ‘allele’ by Eq. 11 can be expressed as:

In w α ij,k , superscripts ij are for the genotype of A i A j and superscript k is for α lk . In w δ ij,kf , superscripts ij are for d ij and superscripts kf are for δ kf . From Eqs. 13 and 14 , the additive coding (w α ij,k ) of a multi-allelic genotype is:

From Eqs. 19 and 20 , the dominance coding (w δ ij,kf ) of a multi-allelic genotype is:

For convenience of computer programming, Eqs. 22 – 24 can be characterized by whether a ij and α lk share no common allele (Eq. 22 ), or 1 common allele when i ≠ j (Eq. 23 ) or 1 common allele when i = j (Eq. 24 ). Similarly, between d ij and δ kf , Eq. 25 shares two common alleles, Eqs. 26 and 27 share 1 common allele with i ≠ j, Eq. 28 shares one common allele with i = j, and Eq. 29 share no common allele. In Eqs. 25 – 29 , p i or p j is the allele frequency of the shared allele between d ij and δ kf and p k or p f is the allele frequency of the non-shared allele between d ij and δ kf . From Eqs. 21 – 29 , the multi-allelic haplotype model for h(h + 1)/2 possible genotypic values ( g ) of a given haplotype block with h haplotypes can be expressed as:

where μ = common mean, 1 = [h(h + 1)/2] × 1 column vector of 1’s, a h = W αh α h = [h(h + 1)/2] × 1 column vector of additive values (breeding values), d h = W δh δ h = [h(h + 1)/2] × 1 column vector of dominance values (dominance deviations), W αh = [h(h + 1)/2] × (h − 1) model matrix of α h with w α ij,k defined by Eqs. 22 – 24 , d h = [h(h + 1)/2] × 1 column vector of dominance values (dominance deviations), W δh = [h(h + 1)/2] × [h(h − 1)/2] matrix of δ h with w δ ij,kf defined by Eqs. 25 – 29 , and α h = (h − 1) × 1 column vector with α lk defined by Eq. 7 , and δ h = [h(h − 1)/2] × 1 column vector with δ kf defined by Eq. 9 .


## Numerical example of multi-allelic genetic partition

A hypothetical numerical example is used to illustrate the genetic partition of multi-allelic genotypic values described by Eqs. 21 – 30 . Four haplotypes as ‘alleles’ are assumed with frequencies in Table 1 and genotypic values in Table 2 . The common mean of the genotypic values using Eq. 3 is: μ = 22.09. The additive effects of the four haplotypes defined by Eqs. 5 – 7 , are:

and the dominance effects defined by Eq. 9 are:


### Table 1: Four hypothetical haplotypes and their frequencies (h = 4)

| Haplotype | 1 | 2 | 3 | 4 |
| Frequency | 0.4 | 0.3 | 0.2 | 0.1 |

### Table 2: Genotypic values of haplotype genotypes (g ij = g ji )

| Haplotype | 1 | 2 | 3 | 4 |
| 1 | g 11 = 25 | g 12 = 18 | g 13 = 15 | g 14 = 10 |
| 2 |  | g 22 = 30 | g 23 = 33 | g 24 = 40 |
| 3 |  |  | g 33 = 17 | g 34 = 12 |
| 4 |  |  |  | g 44 = 35 |
Using Eqs. 13 – 14 and 22 – 24 , the additive values (breeding values) are:

Using Eqs. 19 – 20 and 25 – 29 , the dominance values (dominance deviations) are:

The genotypic values calculated as the summation of the additive and dominance values are:

By comparing with the genotypic values in Table 2 , the above result verifies that the multi-allelic partition of g = 1 μ + a h + d h = 1 μ + W αh α h + W δh δ h described by Eqs. 21 – 30 is correct. With the note that g ij = g ji , a ij = a ji and d ij = d ji , the genotypic variance (σ g 2 ), additive variance (σ a 2 ) and dominance variance (σ d 2 ) are:

It is readily seen that σ g 2 = σ a 2 + σ d 2 .


## Mixed model and multi-allelic genomic relationship matrices

A mixed model to implement the multi-allelic haplotype model of Eq. 30 can be established with appropriate changes of matrix dimensions for W αh , W δh , a h , d h , α h and δ h in Eq. 30 . A set of m SNP markers are assumed available, and r haplotype blocks of the m SNPs are defined across the genome. Haplotypes of all individuals are assumed known (e.g., constructed using a phasing or imputing software). Each haplotype block is treated as a ‘locus’ and each haplotype within a haplotype block is treated as an ‘allele’. The i th haplotype block has h i haplotypes, h i −1 additive effects, and n δi dominance effects or heterozygous genotypes. Let n α = total number of additive effects of all r haplotype blocks, n δ = total number of dominance effects (or heterozygous genotypes) of all r haplotype blocks. Then, n α = ∑ i = 1 r h i − r, and n δ = ∑ i = 1 r n δi . For a given sample of q individuals, the limit number of effects is 2q-1 for additive effects and is the number of heterozygous genotypes for dominance effects. For a sample with N observations on q individuals, the mixed model to implement the multi-allelic haplotype model of Eq. 30 can be expressed as:

where Z = N × q incidence matrix allocating phenotypic observations to each individual = identity matrix for one observation per individual (N = q), α h = n α × 1 column vector of haplotype additive effects, W αh = q × n α model matrix of α h , δ h = n δ × 1 column vector for dominance effects of haplotype genotypes, W δh = q × n δ model matrix of δ h , α s = m × 1 column vector of single-SNP additive effects, b = c × 1 column vector of fixed effects such as heard-year-season in dairy cattle (c = number of fixed effects), and X = N × c model matrix of b . To define two equivalent models with complementary computing advantages and identical GBLUP and GREML results, the mixed model of Eq. 31 needs to be expressed as [ 8 ]:

where a h = T αh α h = multi-allelic genomic breeding values, d h = T δh δ h = multi-allelic genomic dominance values, and each T matrix can be defined by any of the six definitions of genomic relationships we previously discussed and implemented [ 9 ]. For simplicity of notations, the T matrices are defined as: T αh = W αh /k αh 1/2 , T δh = W δh /k δh 1/2 , where k αh = the average of diagonal elements of W αh W αh ', and k δh = the average of diagonal elements of W δh W δh '. The genomic relationship matrices of Eq. 31 can thus be defined as:


## Interpretation of multi-allelic and haplotype genomic relationship matrices

The multi-allelic genomic relationships of Eqs. 33 and 34 using multi-allelic markers such as microsatellite markers have the same interpretation and theoretical expectation as using SNP markers that are bi-allelic, e.g., a genomic additive relationship is expected to be twice the coancestry coefficient [ 8 , 9 ]. Using either multi-allelic or bi-allelic markers under the assumption of no inbreeding, the theoretical expectation of genomic additive relationships is 0.5, 0.5, 0.25 and 0 for parent-offspring, full-sibs, half-sibs and unrelated individuals respectively, and the corresponding theoretical expectation of genomic dominance relationships is 0, 0.25, 0 and 0.

It is important to distinguish between single-locus multi-allelic markers such as microsatellite markers from haplotypes where each haplotype is treated as an ‘allele’ and each haplotype block is treated as a ‘locus’, because recombination between loci within a haplotype block generally exists, leading to lowered haplotype similarity than single-locus similarity among relatives. As the number of loci increases in each haplotype block, genomic relationships using haplotypes are expected to decrease from those using single-locus markers. Therefore, the utility of haplotype genomic relationships using Eqs. 33 and 34 is for genomic prediction using haplotypes, not for measuring relationships among individuals. The optimal block size and hence the number of haplotypes per block is an important issue for genomic prediction and could be determined by validation studies, as to be further discussed towards the end of this article.


## Two equivalent mixed models with complementary computing strategies

To establish mixed models using multi-allelic markers or haplotypes, assumptions for the first and second moments of the mixed model of Eq. 32 are: E( y ) = Xb , E( α h ) = E( δ h ) = E( α s ) = E( δ s ) = 0, Var( α h ) = σ αh 2 I nα , Var( a h ) = G αh = σ αh 2 A h , Var( δ h ) = σ δh 2 I nδ , Var( d h ) = G δh = σ δh 2 D h , and Var( e ) = R = σ e 2 I N , where σ αh 2 = variance of multi-allelic additive effects, σ δh 2 = variance of multi-allelic dominance effects, σ e 2 = residual variance, and I nα , I nδ , I m and I N are identity matrices of orders n α , n δ , m and N, respectively. All random effects are assumed to be uncorrelated so that the phenotypic variance-covariance matrix is:

To simply notations for the two equivalent mixed models, terms in Eqs. 32 – 35 are re-written as α h = τ 1 , δ h = τ 2 ; T αh = T 1 , T δh = T 2 ; u i = T i τ i , i = 1,2; A h = S 1 , D h = S 2 ; and σ αh 2 = σ 1 2 , σ δh 2 = σ 2 2 . Then, Eqs. 32 and 35 can be expressed as:

By defining Z i = ZT i , an equivalent model of Eqs. 36 and 37 can be re-written as:

Equations 36 and 37 will be referred to as Model-I, and Eqs. 38 and 39 as Model-II. Model-I and Model-II are equivalent models because both models have identical E( y ) and V , but these two models have different computational advantages that can be complementary to each other. For each model, two methods can be established for genomic prediction and estimation: the method of conditional expectation (CE) and the method of mixed model equations (MME), yielding a total of four methods for the two equivalent models. Model-I using CE is the best method for large numbers of SNP markers and multiple genetic factors, Model-II using MME is the best method for large numbers of individuals, and Model-I using MME and Model-II using CE have no computing advantage. Therefore, Model-I using CE and Model-II using MME will be used for genomic prediction and estimation. Using our previous naming of these two methods, GBLUP and GREML of Model-I using CE will be referred to as the CE set of formulations, and GBLUP and GREML of Model-II using MME as the QM set of formulation, where QM means ‘q > m’. These two methods yield identical results of prediction and estimation and are applicable to singular genomic relationship matrices. Assuming one observation per individual, CE based on Eqs. 36 and 37 is approximately easier to compute than QM based on Eqs. 38 and 39 if q < c + n α + n δ according to the size of the largest matrix to invert for each method (Table 3 ). Model-I using MME has no computing advantage over Model-I using CE due to the large coefficient matrix of MME and the requirement for full-rank relationship matrices; and Model-II using CE has no computing advantage over Model-I using CE due to the large T matrices to store in memory.


### Table 3: Comparison of computational feasibility of four methods from the two equivalent models with haplotypes and SNPs for GBLUP and GREML

|  |  | Method of for calculating GBLUP |
|  | Conditional expectation (CE) | Mixed model equations (MME) |
| Model I, Eqs. 36 and 37 | Largest matrix to invert | V , phenotypic variance-covariance matrix | C , coefficient matrix of MME |
| Size of largest matrix to invert | q × q, assuming one observation per individual | c + 2q for C |
| Largest matrix to store in memory | q × q P matrix | c + 2q for C |
| Applicable to singular genomic relationship matrices | Yes, inverse relationship matrices avoided | No, inverse relationship matrices required |
| Model II, Eqs. 38 and 39 | Largest matrix to invert | V , phenotypic variance-covariance matrix | C , coefficient matrix of MME |
| Size of largest matrix to invert | q × q, assuming one observation per individual | c + n α + n δ for C |
| Largest matrix to store in memory | q × n α and q × n δ T matrices, q × q P matrix | c + n α + n δ for C |
| Applicable to singular genomic relationship matrices | Yes, inverse relationship matrices avoided | Yes, inverse relationship matrices avoided |

## Genomic best linear unbiased prediction of genetic values (GBLUP)

Using the CE method of Model-I (Eqs. 36 and 37 ), GBLUP of the i th type of genetic values for individuals in the training population is obtained as:

where b ^ = X ' V − 1 X − X ' V − 1 y = best linear unbiased estimator (BLUE) of fixed non-genetic effects, P = V − 1 − V − 1 X ( X ' V − 1 X ) − X ' V − 1 , and ε i = σ i 2 Z ' V − 1 y − X b ^ = Z ' P y = q × 1 column vector of regressed phenotypic values of the training population as a regression of the i th type of genetic values on the phenotypic values in the training population. Two equivalent methods with identical results can be used to predict genetic values of individuals without phenotypic observations (validation population): placing all individuals with or without records in the same mixed model by setting to zero the Z matrix for the validation population, or calculate predictions separately based on the regressed phenotypic values of the training population [ 8 , 39 ]. Using this second method, GBLUP of the i th type of genetic values for individuals in the validation population is calculated as:

where S i01 = q 0 × q genomic relationship matrix between the training and validation populations for the i th type of genetic values (q 0 = number of individuals in the validation population).

Using the QM method (MME method of Model-II of Eqs. 38 and 39 ), genomic prediction first calculates the GBLUP of haplotype effects and then calculates GBLUP of genetic values. GBLUP of haplotype effects is obtained from solving the following MME:

where τ ^ = τ ^ 1 τ ^ 2 , Z g = ( Z 1 , Z 2 ), λ i = σ e 2 /σ i 2 , t = n α , n δ , m and N for i = 1,2, respectively, and ⊕ denotes direct sum that defines a block diagonal matrix. With haplotype and SNP effects from Eq. 42 , GBLUP of the i th type of genetic values for individuals in the training and validation populations are obtained as:

where T i0 = the T i matrix calculated using SNPs of the validation population. Equations 43 and 44 yield identical results as those of Eqs. 40 and 41 . The prediction of total genotypic values in either training or validation population can be obtained from Eqs. 40 and 41 or 43 and 44 as: ĝ = ∑ i = 1 2 û i = predicted genotypic values of all individuals, and ĝ 0 = ∑ i = 1 2 û i0 = predicted genotypic values of the validation population. Prediction reliabilities of additive, dominance and genotypic predictions as the squared correlations between the genomic and true values has the same formulations as the R ai 2 , R di 2 and R gi 2 formulae in [ 8 ], and prediction accuracy is obtained as the square root of the reliability estimate.


## Genomic restricted maximum likelihood estimation (GREML) of variance components

Using the CE method of Model-I (Eqs. 36 and 37 ), the EM type GREML estimates of variance components are:

where k = iteration number. Using the QM method (Eqs. 38 and 39 ), the EM type GREML estimates of variance components are

where r is the rank of the coefficient matrix of Eq. 42 , e ^ = y − X b ^ − ∑ i = 1 2 Z i τ ^ i , and C ii is defined by:

where M = I N − X ( X ' X ) − X ', and ti = n α for i = 1 and ti = n δ for i = 2.

The EM-REML of Eqs. 45 – 48 are known to be slow but reliable to yield non-negative estimates of variance components. The AI-REML algorithm is fast but may be sensitive to starting values of variance components and may fail for extreme heritability levels. Formulations of AI-REML for the multi-allelic haplotype model in this article are straightforward extensions of the formulations we implemented for GVCBLUP [ 40 ].


## Integration of haplotype and single SNP effects in genomic prediction and estimation

Haplotype analysis and single SNP analysis can be analyzed jointly for genomic prediction in the same mixed model by adding single SNP effects from our previous work [ 8 ] to the mixed model of Eq. 31 , i.e.,

where α s = m × 1 column vector of SNP additive effects, T αs = q × m model matrix of α s , δ s = m × 1 column vector of SNP dominance effects, T δs = q × m model matrix of δ s , Var( α s ) = σ αs 2 I m , Var( a s ) = G αs = σ αs 2 A s , Var( δ s ) = σ δs 2 I m , Var( d s ) = G δs = σ δs 2 D s , A s = genomic additive relationship matrix, and D s = SNP genomic dominance relationship matrix, and where A s = T αs T αs ' and D s = T δs T δs '. Let α s = τ 3 , δ = τ 4 ; u i = T i τ i , i = 1,…,4; A s = S 3 , D h = S 4 ; and σ αs 2 = σ 3 2 , σ δs 2 = σ 4 2 . The GBLUP and GREML formulations to jointly include haplotype and single SNP additive and dominance effects essentially entails to extending the range of the subscript i from 2 to 4 for Eqs. 38 –50.

GREML estimation using the joint mixed model with haplotype and SNP effects offer flexibility to estimate the heritability for various types of functional genomic information in any given autosome regions based on formulations we implemented in GVCBLUP [ 40 ], e.g., the additive and dominance heritabilities of haplotype blocks of all genes, all LD blocks, or all single SNPs. The heritability estimate for each type of genetic effects is: h i 2 = σ i 2 /σ y 2 , where σ y 2 = ∑ i = 1 4 σ i 2 + σ e 2 = phenotypic variance. The total heritability of all types of genetic effects is the summation of all effect heritabilities, i.e., H 2 = ∑ i = 1 4 h i 2 . Genomic heritability estimation has flexibility unavailable from heritability estimation using pedigree relationships: the heritability estimation for a single SNP, a chromosome region, or a set of selected SNPs. Using the GREML formulae of Eqs. 35 and 36 , the heritability for haplotype block j or SNP set j can be estimated as: h i j 2 = τ ^ i j ' τ ^ i j / τ ^ i ' τ ^ i h i 2 , where τ ^ i j = subset j of τ ^ i , i = 1,…,4. Given sufficient computing power and sample sizes for extensive validation studies, these heritability estimates could help identify genomic regions and genes relevant to phenotypes within the framework of genomic prediction.


## Defining haplotype blocks using functional genomic information

The multi-allelic haplotype model can be used for the integration of functional genomic information with genomic prediction and estimation. This integration defines haplotype blocks using functional genomic information under the hypothesis that a chromosome region with functional information required more than a single point to affect a phenotype, followed by genomic prediction and estimation using a haplotype analysis such as the methods developed in this article. Each gene could be a ‘natural haplotype block’ and the use of gene blocks improved the prediction accuracy for some human phenotypes in our preliminary results [ 37 ]. Other types of functional information can also be used to define haplotype blocks, including ChIP-seq sites, DNA methylation sites, CNV, protein interaction, pathway information, GWAS results and selection signatures (Fig. 1 ). Other than ‘natural haplotype blocks’, the optimal block sizes for functional information with best prediction accuracy could be determined by extensive validation studies.


> **Fig. 1:** Integration of functional and structural genomic information for genomic selection. Haplotype blocks are defined using functional genomic information and are analyzed using the multi-allelic haplotype model in this article for genomic prediction and estimation. Single SNPs as structural genomic information can be used jointly with the haplotype analysis. (DHS = DNase I hypersensitive site)


## Rare haplotypes, missing genotypic values

The mixed model approach outlined above allows rare haplotypes. In the extreme case of rare haplotypes with one observation per haplotype or haplotype frequency of 1/h when h is large, the multi-allelic model with the mixed model implementation still is applicable for additive effects and values. Missing genotypic values is a problem for dominance effects and values. The dominance effect defined by Eq. 9 requires the availability of all three genotypic values of a haplotype pair. Consequently, dominance effect is undefined with any missing genotypic value. We currently recommend ignoring any haplotype pair with missing genotypic value or values for defining dominance effects. For large haplotype blocks, nearly all individuals could be heterozygous so that such large blocks may not contribute to genomic prediction and estimation of dominance effects and values. This loss of dominance information should be a factor to consider in defining the block size.


## Conclusions

A multi-allelic haplotype model for genomic prediction and estimation is established using the quantitative genetics model that partitions a multi-allelic genotypic value into additive and dominance values, factorizes each additive value into a product between a function of allele frequencies and additive effect, and factorizes each dominance value into a product between a function of allele frequencies and dominance effect. Haplotype genomic additive and dominance relationship matrices and formulations are then derived for GBLUP and GREML utilizing haplotypes in haplotype blocks. These results fill a gap in the theory of quantitative genetics for multi-allelic genetic partition and provide a haplotype approach within the theory of quantitative genetics towards the integration of functional and structural genomic information for genomic selection.


## Availability of supporting data

The only data set used in this article is shown in Tables 1 – 2 .

This research was supported by USDA National Institute of Food and Agriculture Grant no. [YEAR]-67015-30333 and by project MN-16-043 of the Agricultural Experiment Station at the University of Minnesota. Dzianis Prakapenka and Chunkao Wang implemented the methodology in this article by the GVCHAP computer program. Cheng Tan and Dzianis Prakapenka evaluated the methodology. John R. Garbe provided summary and discussion of human functional genomic information. Li Ma processed a dataset for methodology evaluation.

