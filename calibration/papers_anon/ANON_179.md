# De-Identified Manuscript `ANON_179`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Estimates from genome-wide association studies (GWAS) of unrelated individuals capture effects of inherited variation (direct effects), demography (population stratification, assortative mating) and relatives (indirect genetic effects). Family-based GWAS designs can control for demographic and indirect genetic effects, but large-scale family datasets have been lacking. We combined data from 178,086 siblings from 19 cohorts to generate population (between-family) and within-sibship (within-family) GWAS estimates for 25 phenotypes. [AUTHOR]-sibship GWAS estimates were smaller than population estimates for height, educational attainment, age at first birth, number of children, cognitive ability, depressive symptoms and smoking. Some differences were observed in downstream SNP heritability, genetic correlations and Mendelian randomization analyses. For example, the within-sibship genetic correlation between educational attainment and body mass index attenuated towards zero. In contrast, analyses of most molecular phenotypes (for example, low-density lipoprotein-cholesterol) were generally consistent. We also found within-sibship evidence of polygenic adaptation on taller height. Here, we illustrate the importance of family-based GWAS data for phenotypes influenced by demographic and indirect genetic effects.

Subject terms: Population genetics, Genome-wide association studies

[AUTHOR]-sibship genome-wide association analyses using data from 178,076 siblings illustrate differences between population-based and within-sibship GWAS estimates for phenotypes influenced by demographic and indirect genetic effects.


## Main

GWAS have identified thousands of genetic variants associated with complex phenotypes 1 , 2 , typically using samples of non-closely related individuals 3 . GWAS associations can be interpreted as estimates of direct individual genetic effects, that is, the effect of inheriting a genetic variant (or a correlated variant) on a phenotype 4 – 6 . However, there is growing evidence that GWAS associations for some phenotypes estimated from samples of unrelated individuals also capture effects of demography 7 , 8 (assortative mating 9 – 11 and population stratification 12 ) and indirect genetic effects of relatives 13 – 19 (Fig. 1 ). For example, Lee et al. 14 found that within-sibship GWAS estimates for educational attainment variants were around 40% lower than estimates from unrelated individuals, indicating the presence of demographic and indirect genetic effects. These nondirect sources of genetic associations are themselves of interest for estimating parental effects 13 , 18 , understanding human mate choice 9 – 11 and genomic prediction 14 , 19 . However, they can also impact downstream analyses using GWAS summary data such as biological annotation, heritability estimation 20 – 22 , genetic correlations 23 , Mendelian randomization (MR) 7 , 24 , 25 and polygenic adaptation tests 26 – 29 .


### Fig. 1. Demographic and indirect genetic effects.


> **Figure/Table Caption:** Population stratification: population stratification is defined as the distortion of associations between a genotype and a phenotype when ancestry A influences both genotype G (via differences in allele frequencies) and the phenotype X . Principal components and linear mixed model methods control for ancestry but they may not completely control for fine-scale population structure. Assortative mating: assortative mating is a phenomenon where individuals select a partner based on phenotypic (dis)similarities. For example, tall individuals may prefer a tall partner. Assortative mating can induce correlations between causes of an assorted phenotype in subsequent generations. If a phenotype X is influenced by two independent genetic variants G1 and G2 then assortment on X (represented by effects of X on mate choice M ) will induce positive correlations between G1 in parent 1 and G2 in parent 2 and vice versa. Parental transmission will then induce correlations between otherwise independent G1 and G2 in offspring. These correlations can distort genetic association estimates. Indirect genetic effects: indirect genetic effects are effects of relative genotypes (via relative phenotypes and the shared environment) on the index individual’s phenotype. These indirect effects influence population GWAS estimates because relative genotypes are also associated with genotypes of the index individual. Indirect genetic effects of parents on offspring are of most interest because they are likely to be the largest. However, indirect genetic effects of siblings or more distal relatives are also possible.

[AUTHOR]-family genetic association estimates, such as those obtained from samples of siblings, can provide less biased estimates of direct genetic effects because they are unlikely to be affected by demographic and indirect genetic effects of parents 7 , 17 , 30 – 34 . GWAS using siblings (within-sibship GWAS) (Fig. 2 ) have been previously limited by available data, but are now feasible by combining well-established family studies with recent large biobanks that incidentally or by design contain thousands of sibships 35 – 39 .


### Fig. 2. Population GWAS estimate the association between raw genotypes G and phenotypes X .


> **Figure/Table Caption:** As outlined in Fig. 1 , estimates from population GWAS may not fully control for demography (population stratification and assortative mating) and may also capture indirect genetic effects of relatives. For simplicity we use N to represent all sources of associations between G and X that do not relate to direct effects of G . Circles indicate unmeasured variables and squares indicate measured variables. If parental genotypes are known, G can be separated into nonrandom (determined by parental genotypes) and random (relating to segregation at meiosis) components. [AUTHOR]-sibship GWAS include the mean genotype across a sibship ( G F ) (a proxy for the mean of the paternal and maternal genotypes G P, M ) as a covariate to capture associations between G and X relating to parents. The within-sibship estimate is defined as the effect of the random component: that is, the association between family-mean-centered genotype G C (that is, G − G F ) and X . Demography and indirect genetic effects of parents ( N ) will be captured by G F . The association between G C and X will not be influenced by these sources of association but could be affected by indirect effects of the siblings themselves, which are not controlled for.

Here, we report findings from a within-sibship GWAS of 25 phenotypes using data from 178,076 siblings from 19 studies, the largest GWAS conducted within sibships to date (Fig. 3 ). Our results are broadly consistent with previous studies comparing population and within-sibship genetic effect estimates in smaller sample sizes 13 , 14 , 19 , 40 . We found that within-sibship meta-analysis GWAS estimates are smaller than population estimates for seven phenotypes (height, educational attainment, age at first birth, number of children, cognitive ability, depressive symptoms and smoking). We show that these differences in GWAS estimates, which are likely to partially reflect demographic and indirect genetic effects, can affect downstream analyses such as estimates of heritability, genetic correlations and MR. However, we find that genetic associations with most clinical phenotypes, such as lipids, are less strongly affected. We found strong evidence of polygenic adaption on taller human height using within-sibship data. Our study illustrates the importance of collecting genome-wide data from families to understand the effects of inherited genetic variation on phenotypes that are affected by assortative mating, population stratification and indirect genetic effects.


### Fig. 3. A flowchart of analyses undertaken in this project.


> **Figure/Table Caption:** We started by performing quality control and running GWAS models in 19 individual cohorts. We then meta-analyzed GWAS data from 18 of these cohorts with European-ancestry individuals. We then used the European meta-analysis data for downstream analyses including LDSC, MR and polygenic adaptation testing. We performed analyses in the China Kadoorie Biobank separately. QC, quality control.


## Results


### [AUTHOR]-sibship and population-based GWAS comparison

For GWAS analyses we used data from 178,076 individuals (with one or more genotyped siblings) from 77,832 sibships in 19 studies. Sample sizes for individual phenotypes ranged from 13,375 to 163,748 (median: 82,760, mean: 79,794). More information on sample sizes from individual cohorts and for each phenotype is contained in Supplementary Table 1 . We used within-sibship models which use deviations of the individual’s genotype from the mean genotype within the sibship (that is, all siblings in the family present in the study). For example, in a sibling pair where one sibling has two risk alleles and the other sibling has one risk allele, the mean sibship genotype is 1.5 risk alleles and the individual’s deviations are +0.5 and −0.5, respectively. The within-sibship model includes the mean sibship genotype as a covariate to capture the between-family contribution of the SNP 14 . For comparison, we also applied a standard population GWAS model; a covariate-adjusted linear regression of the outcome on raw genotype, which does not account for the mean sibship genotype. Standard errors were clustered by sibship. Age, sex and principal components were included as covariates in both models. All GWAS analyses were performed in individual cohort studies separately using R (v.3.5.1) and meta-analyses were conducted across these using summary data. Amongst the phenotypes analyzed, the largest available sample sizes in a meta-analysis of European cohorts were for height ( N = 149,174), body mass index (BMI) ( N = 140,883), educational attainment ( N = 128,777), ever smoking ( N = 124,791) and systolic blood pressure (SBP) ( N = 109,588) (Supplementary Table 2 ). We also report stratified results from non-European samples including 13,856 individuals from the China Kadoorie Biobank. Sample sizes here refer to the number of individuals across all sibships.

Previous studies have found that association estimates of height and educational attainment genetic variants are smaller in within-family models 13 , 14 , 40 . We aimed to investigate whether similar shrinkage in association estimates is observed for other phenotypes by comparing within-sibship and population genetic association estimates for 25 phenotypes that were widely available in family-based studies. We observed the largest within-sibship shrinkage (% decrease in association estimates from population to within-sibship models) for genetic variants associated with number of children (67%; 95% confidence interval (95% CI) 4%, 130%), age at first birth (52%; 30%, 75%), depressive symptoms (50%; 18%, 82%) and educational attainment (47%; 41%, 52%). We also found evidence of shrinkage for cognitive ability (22%; 6%, 37%), ever smoking (19%; 9%, 30%) and height (10%; 8%, 12%). In contrast, within-sibship association estimates for C-reactive protein (CRP) were larger than population estimates (−9%; −15%, −2%). We found limited evidence of within-sibship differences for the remaining 17 phenotypes, including BMI and SBP (Fig. 4 and Supplementary Table 3 ).


#### Fig. 4. Estimates of shrinkage between population and within-sibship models with corresponding 95% CIs.


> **Figure/Table Caption:** Shrinkage is defined as the % decrease in association between the relevant weighted score and phenotype when comparing the population estimate with the within-sibship estimate. Shrinkage was computed as the ratio of two weighted score association estimates with standard errors derived using leave-one-out jackknifing. The number of individuals contributing to each phenotype ranged from n = 149,174 for height to n = 13,375 for age at menopause. Further information on the sample sizes of each phenotype is contained in Supplementary Table 2 . S G , weighted score at genome-wide significance ( P < 5 × 10 −8 ); S L , weighted score at more liberal threshold ( P < 1 × 10 −5 ); Education, educational attainment; EverSmk, ever smoking; WHR, waist-to-hip ratio; Alcohol, weekly alcohol consumption; Menarche, age at menarche; AFB, age at first birth; Children, number of biological children; Menopause, age at menopause; Cognition, cognitive ability; Depressive, depressive symptoms; PA, physical activity; CPD, cigarettes per day; LDL, low-density lipoprotein-cholesterol; HDL, HDL-cholesterol; TG, triglycerides; eGFR, estimated glomerular filtration rate; FEV1, forced expiratory volume; FEV1FVC, ratio of FEV1/forced vital capacity; HbA1c, hemoglobin A1C.

We investigated possible heterogeneity in shrinkage for height and educational attainment genetic variants across variants and between cohorts. Using the meta-analysis results, we did not observe strong evidence of heterogeneity in shrinkage across variants that were strongly associated with height and educational attainment. This suggests that shrinkage may be largely uniform across these signals for these phenotypes. We also found limited evidence of cohort heterogeneity in shrinkages for height (heterogeneity P = 0.89) and educational attainment ( P = 0.40) across the European-ancestry cohorts (Extended Data Figs. 1 and 2 ). In contrast, there was limited evidence for shrinkage on height in the China Kadoorie Biobank (shrinkage −3%; 95% CI −13%, 7%; heterogeneity with European meta-analysis P = 0.006) but some evidence of shrinkage on ever smoking (shrinkage = 134%; 10%, 258%) (Extended Data Fig. 3 ).


#### Extended Data Fig. 1. [AUTHOR]-sibship shrinkage for height across European ancestry cohorts.


> **Figure/Table Caption:** AMDTSS = Australian Mammographic Density Twin Study, DTR = Danish Twins Registry, NTR = Netherlands Twin Registry, QIMR = QIMR Berghofer Medical Research Institute (QIMR), TEDS = Twins Early Development Study. Extended Data Figure 1 shows estimates of within-sibship shrinkage and 95% confidence intervals for height variants in all of the cohorts contributing to the European meta-analysis as well as the meta-analysis GWAS. Shrinkage is defined as the % decrease in association between the relevant weighted score and phenotype when comparing the population estimate to the within-sibship estimate. Shrinkage was computed as the ratio of two weighted score association estimates with standard errors derived using leave-one-out jackknifing. These estimates used the weighted score for each phenotype at the more liberal threshold (P < 1×10 −5 ). The total number of individuals in the meta-analysis was n = 149,174 with individual study sample sizes ranging from n = 601 for the Colorado based CADD study to n = 40,068 for UK Biobank. Further information on samples with height data in each cohort are contained in Supplementary Table 1 .


#### Extended Data Fig. 2. [AUTHOR]-sibship shrinkage for educational attainment across European ancestry cohorts.


> **Figure/Table Caption:** AMDTSS = Australian Mammographic Density Twin Study, DTR = Danish Twins Registry, NTR = Netherlands Twin Registry, QIMR = QIMR Berghofer Medical Research Institute (QIMR).Extended Data Figure 2 shows estimates of within-sibship shrinkage and 95% confidence intervals for educational attainment variants in all of the cohorts contributing to the European meta-analysis as well as the meta-analysis GWAS. Shrinkage is defined as the % decrease in association between the relevant weighted score and phenotype when comparing the population estimate to the within-sibship estimate. Shrinkage was computed as the ratio of two weighted score association estimates with standard errors derived using leave-one-out jackknifing. These estimates used the weighted score for each phenotype at the more liberal threshold (P < 1×10 −5 ). The total number of individuals in the meta-analysis was n = 128,777 with individual study sample sizes ranging from n = 742 for STR Psych Cohort 1 to n = 39,531 for UK Biobank. Further information on samples with educational attainment data in each cohort are contained in Supplementary Table 1 .


#### Extended Data Fig. 3. [AUTHOR]-sibship shrinkage estimates from China Kadoorie Biobank.


> **Figure/Table Caption:** S G = score including variants with P < 5×10 −8 , S L = score including variants with P < 1×10 −5 , BMI = body mass index, SBP = systolic blood pressure, EverSmk = ever smoking. Extended Data Figure 3 contains within-sibship shrinkage estimates and 95% confidence intervals for height, BMI, educational attainment, systolic blood pressure and ever-smoking genetic variants in China Kadoorie Biobank. Shrinkage is defined as the % decrease in association between the relevant weighted score and phenotype when comparing the population estimate to the within-sibship estimate. Shrinkage was computed as the ratio of two weighted score association estimates with standard errors derived using leave-one-out jackknifing. The figure includes genetic variants from the genome-wide significant (blue) and liberal (red) thresholds. Note that the genetic variants tested were identified in UK Biobank, but any ancestral differences will likely equally affect both the population and within-sibship estimates, meaning that the shrinkage estimate are unlikely to be biased by ancestral differences. Data was available from n = 13,856 individuals for each of the 6 phenotypes.


### [AUTHOR]-sibship SNP heritability estimates

Linkage disequilibrium (LD) score regression (LDSC) can use GWAS data to estimate SNP heritability, the proportion of phenotypic variation explained by common SNPs 20 , 23 . We used simulations to investigate the applicability of LDSC when using within-sibship GWAS data, finding evidence that LDSC can estimate SNP heritability using both population and within-sibship model GWAS data if effective sample sizes (based on standard errors) are used to account for differences in power between the models ( Methods ).

To evaluate the impact of controlling for demographic and indirect genetic effects, we compared LDSC SNP heritability estimates based on population and within-sibship effect estimates for 25 phenotypes. Theoretically, within-sibship shrinkage in GWAS estimates will also lead to attenuations in within-sibship SNP heritability estimates ( Methods ). The within-sibship SNP heritability point estimate for educational attainment attenuated by 76% from the population estimate (population h 2 : 0.13; within-sibship h 2 : 0.04; difference P = 5.3 × 10 −26 ), with attenuations also observed for cognitive ability (population h 2 : 0.24; within-sibship h 2 : 0.14; attenuation 44%; difference P = 0.011), ever smoking (population h 2 : 0.10; within-sibship h 2 : 0.07; attenuation 25%; difference P = 0.029) and height (population h 2 : 0.41; within-sibship h 2 : 0.34; attenuation 17%; difference P = 1.6 × 10 −3 ). The observed attenuations were consistent with theoretical expectation (Supplementary Table 4 ), suggesting that the lower within-sibship SNP heritability estimates are explained by genetic association estimate shrinkage. Across the 21 additional phenotypes, population and within-sibship SNP heritability estimates were relatively consistent (Fig. 5 and Supplementary Table 5 ). SNP heritability estimates using SumHer 21 with the LDAK-Thin model (expected heritability contribution of each SNP is dependent on allele frequencies and local LD) provided consistent evidence for within-sibship attenuations in SNP heritability for height, educational attainment and cognitive ability (Supplementary Table 6 and Extended Data Fig. 4 ).


#### Fig. 5. LDSC SNP h 2 estimates for 25 phenotypes using population and within-sibship meta-analysis data with corresponding 95% CIs.


> **Figure/Table Caption:** The number of individuals contributing to each phenotype ranged from n = 149,174 for height to n = 13,375 for age at menopause. BMI, body mass index; Education, educational attainment; EverSmk, ever smoking; SBP, systolic blood pressure; WHR, waist-hip ratio; Alcohol, weekly alcohol consumption; Menarche, age at menarche; AFB, age at first birth; Children, number of biological children; Menopause, age at menopause; Cognition, cognitive ability; Depressive, depressive symptoms; PA, physical activity; CPD, cigarettes per day; LDL, LDL cholesterol; HDL, HDL cholesterol; TG, triglycerides; CRP, C-reactive protein; eGFR, estimated glomerular filtration rate; FEV1, forced expiratory volume; FEV1FVC, ratio of FEV1/forced vital capacity; HbA1c, Haemoglobin A1C. Further information on the sample sizes of each phenotype is contained in Supplementary Table 2 .


#### Extended Data Fig. 4. SumHer SNP heritability estimates.


> **Figure/Table Caption:** BMI = body mass index, Education = educational attainment, EverSmk = ever smoking, SBP = systolic blood pressure, WHR = waist-hip ratio, Alcohol = weekly alcohol consumption, Menarche = age at menarche, AFB = age at first birth, Children = number of biological children, Menopause = age at menopause, Cognition = cognitive ability, Depressive = depressive symptoms, PA = physical activity, CPD = cigarettes per day, LDL = LDL cholesterol, HDL = HDL cholesterol, TG = triglycerides, CRP = C-reactive protein, eGFR = estimated glomerular filtration rate, FEV1 = forced expiratory volume, FEV1FVC = ratio of FEV1/forced vital capacity, HbA1c = Haemoglobin A1C. Extended Data Figure 4 displays SumHer SNP h 2 (LDAK-thin model) estimates and corresponding 95% confidence intervals for 25 phenotypes using population and within-sibship meta-analysis data. The number of individuals contributing to each phenotype ranged from n = 149,174 for height to n = 13,375 for age at menopause. Further information on the sample sizes of each phenotype are contained in Supplementary Table 2 .


### [AUTHOR]-sibship r g with educational attainment

We used LDSC 23 to estimate cross-phenotype genome-wide genetic correlations ( r g ) between educational attainment and 20 phenotypes with sufficient heritability (population/within-sibship h 2 point estimate > 0) and statistical power. To determine the effects of demographic and indirect genetic effects on r g , we compared estimates of r g using population and within-sibship estimates.

There was strong evidence using population estimates that educational attainment is negatively correlated with BMI ( r g = −0.32; −0.37, −0.26), ever smoking ( r g = −0.41; −0.49, −0.34) and CRP ( r g = −0.46; −0.67, −0.25). However, these correlations attenuated towards zero when using within-sibship estimates: BMI ( r g = −0.05; −0.22, 0.12), ever smoking ( r g = −0.14; −0.42, 0.14) and CRP ( r g = −0.06; −0.43, 0.30), with some evidence at nominal significance for differences between population and within-sibship r g estimates (BMI difference P = 5.3 × 10 −4 , ever smoking difference P = 0.040, CRP difference P = 0.039). These attenuations indicate that genetic correlations between educational attainment and these phenotypes from population estimates may be inflated by demographic and indirect genetic effects (Fig. 6 and Supplementary Table 7 ).


#### Fig. 6. LDSC r g estimates between educational attainment and 20 phenotypes using population and within-sibship meta-analysis data with corresponding 95% CIs.


> **Figure/Table Caption:** The number of individuals contributing to the educational attainment GWAS was n = 128,777 with sample sizes for outcomes ranging from n = 149,174 for height to n = 27,638 for cognitive ability. BMI, body mass index; Education, educational attainment; EverSmk, ever smoking; SBP, systolic blood pressure; WHR, waist-hip ratio; Alcohol, weekly alcohol consumption; Menarche, age at menarche; AFB, age at first birth; Children, number of biological children; Menopause, age at menopause; Cognition, cognitive ability; Depressive, depressive symptoms; CPD, cigarettes per day; LDL, LDL cholesterol; HDL, HDL cholesterol; TG, triglycerides; CRP, C-reactive protein; eGFR, estimated glomerular filtration rate; FEV1, forced expiratory volume; HbA1c, Haemoglobin A1C. Further information on the sample sizes of each phenotype is contained in Supplementary Table 2 .


### [AUTHOR]-sibship MR (WS-MR): effects of height and BMI

MR uses genetic variants as instrumental variables to assess the causal effect of exposure phenotypes on outcomes 24 , 41 . MR was originally conceptualized in the context of parent–offspring trios where offspring inherit a random allele from each parent 24 . However, with limited family data, most MR studies have used data from unrelated individuals. WS-MR is largely robust against demographic and indirect genetic effects that could distort estimates from nonfamily designs 7 , 25 . Here, we used population MR and WS-MR to estimate the effects of height and BMI on 23 phenotypes. These provide a useful comparison as we find evidence of shrinkage in GWAS estimates for height but little evidence of shrinkage for BMI, and both height and BMI have large sample sizes.

WS-MR estimates for height and BMI on the 23 outcome phenotypes were largely consistent with population MR estimates for height based on the slope of a regression of the WS-MR and population MR estimates (−3%; 95% CI −16%, 10%) and BMI (−5%; 95% CI −14%, 4%). However, in agreement with the genetic correlation analyses, we observed differences between population MR and WS-MR estimates of height and BMI on educational attainment. Population MR estimates provided strong evidence that taller height and lower BMI increase educational attainment (0.06 s.d. increase in education per s.d. taller height; 95% CI 0.04, 0.07; 0.19 s.d. decrease in education per s.d. higher BMI; 0.16, 0.22). In contrast, WS-MR estimates for these relationships were greatly attenuated (height: 0.02 s.d. increase; −0.01, 0.04; difference P = 1.2 × 10 −3 ; BMI: 0.05 s.d. decrease; 0.01, 0.09; difference P = 2.8 × 10 −7 ). We also observed similar attenuation from population MR and WS-MR estimates for BMI on age at first birth (difference P = 2.3 × 10 −3 ) and cognitive ability (difference P = 0.020); phenotypes highly correlated with education. These differences illustrate instances where population-based MR estimates might be distorted by demographic and indirect genetic effects or other factors (Table 1 ).


#### Table 1.

WS-MR: effects of height and BMI on 23 phenotypes



| Outcome (units) | IVW estimate of effect of s.d. increase in height on outcome (95% CI) | Diff P | IVW estimate of effect of s.d. increase in BMI on outcome (95% CI) | Diff P |
| --- | --- | --- | --- | --- |
| Population | [AUTHOR]-sibship | Population | [AUTHOR]-sibship |
| Age at first birth (years) | 0.27 (0.16, 0.39) | 0.08 (−0.12, 0.29) | 0.052 | −0.79 (−1.04, −0.54) | −0.25 (−0.63, 0.13) | 0.0023 |
| Alcohol consumption (units) | 0.03 (−0.03, 0.09) | 0.03 (−0.07, 0.14) | 0.87 | −0.15 (−0.28, −0.02) | −0.19 (−0.39, 0.02) | 0.71 |
| Cigarettes per day | 0.23 (0.01, 0.46) | 0.29 (−0.12, 0.69) | 0.78 | 0.74 (0.24, 1.23) | 0.56 (−0.21, 1.33) | 0.66 |
| CRP (s.d.) | −0.03 (−0.05, −0.01) | −0.00 (−0.04, 0.03) | 0.078 | 0.28 (0.24, 0.33) | 0.25 (0.18, 0.32) | 0.30 |
| Number of children | −0.02 (−0.04, 0.01) | −0.00 (−0.05, 0.04) | 0.52 | 0.04 (−0.01, 0.10) | 0.07 (−0.01, 0.15) | 0.48 |
| Cognitive ability (s.d.) | 0.07 (0.04, 0.10) | 0.05 (0.00, 0.10) | 0.43 | −0.20 (−0.27, −0.13) | −0.08 (−0.18, 0.01) | 0.020 |
| Depressive symptoms (s.d.) | −0.02 (−0.04, 0.00) | −0.02 (−0.06, 0.02) | 0.94 | 0.04 (−0.01, 0.09) | −0.01 (−0.09, 0.07) | 0.18 |
| Educational attainment (s.d.) | 0.06 (0.04, 0.07) | 0.02 (−0.01, 0.04) | 0.0012 | −0.19 (−0.22, −0.16) | −0.05 (−0.09, −0.01) | <0.001 |
| Ever smoking (risk difference) | −0.01 (−0.01, 0.00) | 0.01 (−0.01, 0.02) | 0.058 | 0.07 (0.05, 0.08) | 0.04 (0.02, 0.07) | 0.065 |
| FEV1 (s.d.) | −0.02 (−0.04, 0.00) | −0.03 (−0.07, 0.01) | 0.67 | −0.17 (−0.22, −0.12) | −0.17 (−0.25, −0.09) | 1.00 |
| FEV1FVC (s.d.) | 0.02 (−0.00, 0.04) | 0.02 (−0.02, 0.06) | 0.96 | −0.02 (−0.06, 0.03) | −0.02 (−0.09, 0.05) | 0.87 |
| HbA1c (s.d.) | −0.00 (−0.02, 0.02) | 0.02 (−0.02, 0.06) | 0.21 | 0.15 (0.11, 0.20) | 0.14 (0.07, 0.22) | 0.77 |
| HDL-cholesterol (s.d.) | −0.01 (−0.03, 0.01) | −0.02 (−0.05, 0.00) | 0.31 | −0.32 (−0.36, −0.29) | −0.33 (−0.38, −0.28) | 0.79 |
| Low-density lipoprotein-cholesterol (s.d.) | −0.05 (−0.06, −0.03) | −0.03 (−0.06, −0.00) | 0.31 | 0.02 (−0.02, 0.06) | 0.02 (−0.03, 0.08) | 0.86 |
| Age at menarche (years) | 0.09 (0.04, 0.13) | 0.07 (−0.00, 0.14) | 0.63 | −0.62 (−0.71, −0.52) | −0.62 (−0.76, −0.49) | 0.93 |
| Age at menopause (years) | −0.17 (−0.37, 0.02) | −0.15 (−0.51, 0.20) | 0.89 | −0.49 (−0.93, −0.05) | −0.35 (−1.02, 0.31) | 0.72 |
| Neuroticism (s.d.) | −0.02 (−0.03, 0.00) | 0.01 (−0.02, 0.04) | 0.14 | 0.00 (−0.04, 0.04) | −0.03 (−0.09, 0.03) | 0.28 |
| Physical activity (risk difference) | −0.00 (−0.01, 0.01) | −0.01 (−0.03, 0.00) | 0.12 | −0.04 (−0.05, −0.02) | −0.03 (−0.06, 0.00) | 0.63 |
| SBP (mmHg) | −0.77 (−1.04, −0.50) | −0.64 (−1.11, −0.17) | 0.56 | 3.17 (2.57, 3.78) | 3.21 (2.33, 4.10) | 0.93 |
| Triglycerides (s.d.) | −0.02 (−0.03, −0.00) | 0.01 (−0.02, 0.04) | 0.051 | 0.27 (0.23, 0.31) | 0.27 (0.21, 0.33) | 0.96 |
| Waist-to-hip ratio adjusted for BMI (WHR × 100) | 0.00 (0.00, 0.00) | 0.00 (0.00, 0.00) | 0.26 | 0.01 (0.01, 0.01) | 0.01 (0.01, 0.01) | 0.29 |
| Wellbeing (s.d.) | 0.01 (−0.01, 0.03) | −0.01 (−0.04, 0.03) | 0.39 | −0.05 (−0.09, −0.00) | −0.05 (−0.12, 0.01) | 0.85 |
| eGFR | −0.67 (−0.92, −0.43) | −0.86 (−1.28, −0.45) | 0.36 | −0.10 (−0.64, 0.44) | 0.32 (−0.47, 1.11) | 0.22 |


Table 1 contains population MR and WS-MR estimates of height and BMI on 23 phenotypes. Units are presented in terms of a standard deviation increase in height or BMI. Difference (Diff) P values refer to evidence of differences between population and within-sibship estimates which were derived using a difference-of-two-means test with standard errors derived using leave-one-out jackknifing.


### Polygenic adaptation

Polygenic adaptation is a process via which phenotypic changes in a population over time are induced by small shifts in allele frequencies across thousands of variants. One method of testing for polygenic adaptation is to compare Singleton Density Scores (SDS), measures of natural selection over the previous 2,000 years (ref. 28 ), with GWAS P values. However, this approach is sensitive to population stratification as illustrated by recent work using UK Biobank data which showed that population stratification in GWAS data likely confounded previous estimates of polygenic adaptation on height 26 , 27 . [AUTHOR]-sibship GWAS data are particularly useful in this context as they are robust against population stratification 26 , 27 , 29 . Here, we recalculated Spearman’s rank correlation ( r ) between tSDS (SDS aligned with the phenotype-increasing allele) and our population/within-sibship GWAS P values for 25 phenotypes, with standard errors estimated using jackknifing over blocks of genetic variants.

We found strong evidence for polygenic adaptation on taller height in the European meta-analysis GWAS using both population ( r = 0.022; 95% CI 0.014, 0.031) and within-sibship GWAS estimates ( r = 0.012; 0.003, 0.020) (Extended Data Figs. 5 and 6 ). These results were supported by several sensitivity analyses: (1) evidence of enrichment for positive tSDS (mean = 0.18, s.e. = 0.06, P = 0.003) amongst 310 putative height loci from the within-sibship meta-analysis results (Extended Data Fig. 7 ); (2) positive LDSC r g between height and tSDS in the meta-analysis results (Supplementary Table 8 ); and (3) evidence for polygenic adaptation on taller height when meta-analyzing correlation estimates from eight individual studies (for example, SDS using only UK Biobank GWAS summary data) for population ( r = 0.013; 0.010, 0.015) and within-sibship ( r = 0.004; 0.002, 0.007) estimates (Fig. 7 ). There was also some putative within-sibship evidence for polygenic adaptation on increased number of children ( P = 0.024) and lower high-density lipoprotein (HDL)-cholesterol ( P = 0.024) (Extended Data Fig. 5 ).


#### Extended Data Fig. 5. Evidence of polygenic adaption using SDS for 25 phenotypes.


> **Figure/Table Caption:** BMI = body mass index, EverSmk = ever smoking, SBP = systolic blood pressure, WHR = waist-hip ratio, AFB = age at first birth, PA = physical activity, CPD = cigarettes per day, TG = triglycerides, CRP = C-reactive protein, eGFR = estimated glomerular filtration rate, FEV1 = forced expiratory volume, FEV1FVC = ratio of FEV1/forced vital capacity, HbA1c = Haemoglobin A1C. Extended Data Figure 5 displays spearman rank correlation estimates and corresponding 95% confidence intervals between tSDS (SDS aligned with phenotype increasing alleles) and absolute phenotype Z scores for 25 phenotypes. The phenotype Z scores were taken from both the meta-analysis of population (blue) and within-sibship (red) estimates. Positive correlations indicate evidence of historical positive selection on phenotype increasing alleles. The number of individuals contributing to each phenotype ranged from n = 149,174 for height to n = 13,375 for age at menopause. Further information on the sample sizes of each phenotype are contained in Supplementary Table 2 .


#### Extended Data Fig. 6. Scatter plot of SDS p-value bins against mean tSDS (of the bin) using the within-sibship height meta-analysis GWAS data.


> **Figure/Table Caption:** In Extended Data Figure 6 each data point is the mean tSDS (SDS alligned with height increasing allele) in a set of 1000 genetic variants. Genetic variants were ordered by height P-value (from within-sibship meta-analysis GWAS data) and divided into bins. The plot illustrates evidence of a correlation between decreasing height P-value and higher mean tSDS suggestive of polygenic adaptation on height increasing alleles. The within-sibship European GWAS meta-analysis data (n = 149,174 individuals) were used for this analysis.


#### Extended Data Fig. 7. Histogram of tSDS for independent variants associated with height in the within-sibship meta-analysis data (P < 1×10 −5 ).


> **Figure/Table Caption:** Extended Data Figure 7 Extended Data Figure 7 is a histogram of the distribution of tSDS (SDS aligned with height increasing alleles) amongst 310 putative independent height loci identified from the within-sibship meta-analysis data (P < 1×10 −5 ). The plot indicates that the mean tSDS of these loci is higher than 0, consistent with polygenic adaptation on height increasing alleles. The within-sibship European GWAS meta-analysis data (n = 149,174 individuals) were used for this analysis.


#### Fig. 7. Spearman rank correlation estimates and corresponding 95% CIs between tSDS (SDS aligned with height-increasing alleles) and absolute height Z scores.


> **Figure/Table Caption:** Positive correlations indicate evidence of historical positive selection on height-increasing alleles. The pooled estimate is a meta-analysis of the correlation estimates from the individual studies shown above while the European meta-analysis estimate is the correlation estimate using the meta-analysis GWAS data. The number of individuals in the meta-analysis estimate was n = 149,174 with the sample sizes for the displayed individual studies ranging from n = 40,068 in UK Biobank to 4,708 in the Netherlands Twin Register. Further information on available height data in each phenotype is contained in Supplementary Table 1 . QIMR, Queensland Institute of Medical Research.


## Discussion

Here, we report results from the largest within-sibship GWAS to date which included 25 phenotypes and combined data from 178,076 siblings. Consistent with previous studies 13 , 14 , 19 , 40 , we found that GWAS results and downstream analyses of behavioral phenotypes (for example, educational attainment, smoking behavior) as well as some anthropometric phenotypes (for example, height, BMI) are affected by demographic and indirect genetic effects. However, we found that most analyses involving more molecular phenotypes, such as lipids, were not strongly affected. This suggests that the best strategy for gene discovery and polygenic prediction for these phenotypes remains to maximize sample sizes using unrelated individuals. For phenotypes sensitive to demographic and indirect genetic effects, such as educational attainment, family-based estimates are likely to provide less biased estimates of direct genetic effects.

A key aim of GWAS is to estimate direct genetic effects on phenotypes, but other sources of genetic associations can be extremely informative. For example, knowledge of indirect genetic effects can be used to elucidate maternal effects 15 , 42 or the extent to which health outcomes are mediated by family environments 13 , 18 . Future family-based GWAS could also provide further estimates of indirect genetic effects 6 , 18 , 43 .

We found little evidence of heterogeneity in shrinkage estimates at genetic variants strongly associated ( P < 1 × 10 −5 ) with height and educational attainment, although power was limited by available samples. The limited detectable heterogeneity could indicate that the observed shrinkage is largely driven by assortative mating or indirect genetic effects. Both of these tend to influence associations proportional to the direct effect, whereas population stratification is likely to have larger effects on ancestrally informative markers. Notably, twin studies have indicated effects of the common environment on many of the phenotypes for which we observed shrinkage, such as educational attainment 44 , cognitive ability 45 and smoking 46 , potentially consistent with indirect genetic effects of parents. In contrast, twin studies do not find strong evidence for common environmental effects on height, where shrinkage is more likely to be a consequence of assortative mating 10 , 46 , 47 .

The weak evidence for within-sibship shrinkage in the association between BMI genetic variants and BMI is in contrast to the strong evidence from MR analyses (and genetic correlation analyses) that the association between BMI genetic variants and educational attainment does attenuate. These results indicate cross-trait shrinkage in association estimates for BMI genetic variants even in the absence of same-trait shrinkage.

[AUTHOR]-sibship GWAS data can be useful for validating results from larger samples of unrelated individuals. Here, we showed that population MR and WS-MR estimates of the effects of height and BMI were generally consistent for 23 outcome phenotypes. However, we observed differences between within-sibship and population MR estimates of height (on educational attainment) and BMI (on educational attainment, cognitive ability and age at first birth). This suggests the MR assumptions do not hold for these relationships in samples of unrelated individuals. In subsequent studies, WS-MR could be used as a sensitivity analysis when including phenotypes likely to be affected by demographic or indirect genetic effects 7 , 25 .

We used non-European data from the China Kadoorie Biobank to evaluate whether demographic and indirect genetic effects influence GWAS analyses conducted in the Chinese population. In this sample, we found minimal evidence of shrinkage for height genetic variants but—consistent with the European meta-analysis—suggestive evidence of shrinkage for variants associated with smoking initiation. The absence of shrinkage for height suggests that demographic effects such as assortative mating may differ between populations. Larger within-family studies in non-European populations could be used to evaluate population differences in demographic and indirect effects.

We also used the within-sibship GWAS data to evaluate evidence for recent selection. A previous study reporting polygenic adaptation on height in the UK population was found to be biased by population stratification in the Genetic Investigation of ANthropometric Traits (GIANT) consortium 26 – 28 . Previous evidence for adaptation on height using siblings in UK Biobank was suggestive of some adaptation, but statistically inconclusive 26 . Here, using within-sibship GWAS estimates from a larger (~4-fold) sample of siblings, we found strong evidence of polygenic adaptation on increased height and some evidence of adaptation on number of children and HDL-cholesterol. We anticipate that future studies on human evolution will benefit from using large within-family datasets such as our resource.

[AUTHOR]-family GWAS are limited by both available family data and statistical inefficiency (homozygosity within families). To help address this issue, future population-based biobanks could recruit the partners, siblings and offspring of study participants. In contrast, conventional population GWAS designs sampling unrelated individuals are likely to be the optimal approach to maximize statistical power for discovery GWAS for genetic associations. Indeed, we found that many genotype–phenotype associations from population GWAS models were also observed in within-sibship GWASs, albeit sometimes attenuated towards zero. A notable limitation of within-sibship models is that they do not control for indirect genetic effects of siblings, that is, effects of sibling genotypes on the shared environment. Sibling effects have been estimated to be modest compared with parental effects 6 , 48 but could have impacted our GWAS estimates. Another limitation is that while assortative mating is unlikely to affect within-sibship GWAS estimates, it can bias within-sibship estimates of heritability downwards 49 and so may have affected our LDSC SNP heritability and genetic correlation estimates. However, the within-sibship shrinkage in GWAS estimates and LDSC heritability estimates were largely consistent, suggesting any such bias is unlikely to have impacted our conclusions. Our findings are also limited to adult phenotypes. [AUTHOR]-family GWAS (for example, using parent–offspring trios) could use data from children to evaluate if childhood phenotypes are more strongly affected by indirect genetic effects.


## Methods


### Study participants

Nineteen cohorts contributed data to the overall study (Supplementary Table 1 ). These cohorts were selected on the basis of having at least 500 genotyped siblings (an individual with 1 or more siblings in the study sample) with at least 1 of the 25 phenotypes that were analyzed in the study. Phenotypes were selected based on available data and to include a range of different phenotypes. Detailed information on genotype data, quality control and imputation processes are provided in the Cohort Descriptions in the Supplementary Materials. Individual cohorts defined each phenotype based on suggested definitions from an analysis plan (see the Phenotype Definitions in the Supplementary Materials).


### GWAS analyses

GWAS analyses were performed uniformly across individual studies using automated scripts and a preregistered analysis plan ( [GITHUB_REPO_REDACTED] ). Scripts checked strand alignment, imputation scores and allele frequencies for the genetic data as well as missingness for covariates and phenotypes. Scripts also summarized covariates and phenotypes and set phenotypes to missing for sibships if only one individual in the sibship had nonmissing phenotype data. To harmonize variants for meta-analysis, genetic variants were renamed in a format including information on chromosome, base pair and polymorphism type (SNP or INDEL: insertion or deletion). The automated pipeline restricted analyses to common genetic variants (minor allele frequency (MAF) > 0.01) and removed poorly imputed variants (INFO: information score < 0.3). Analyses were restricted to include individuals in a sibship, that is, a group of two or more full siblings in the study. Monozygotic twins were included if they had an additional sibling in the study.

GWAS analyses involved fitting both population and within-sibship models to the same samples. The population model is synonymous with a conventional principal component adjusted model, and was fit using linear regression in R (v.3.5.1). The within-sibship model is an extension of the population model including the mean sibship genotype (the mean genotype of siblings in each sibship) as a covariate to account for family structure, with each individual’s genotype centered around the mean sibship genotype 7 , 14 . Age, sex and up to 20 principal components (10 principal components were included in smaller studies at the discretion of study co-authors) were included as covariates in both models. The pipeline used imputed ‘best guess’ genotype calls rather than dosage data.

For individual j in sibship i with ni > 2 siblings:



| Phenotype i j ~ G i j + Sex i j + Age i j + PC 1 i j + PC 2 0 i j |
| --- |


[AUTHOR]-sibship model:



| Phenotype i j ~ G i j C + G i F + Sex i j + Age i j + PC 1 i j + PC 2 0 i j |
| --- |


where G i F = ∑ 1 n G i j n and G i j C = G i j − G i F

G ij , genotype of sibling j in sibship i ; G i F , mean family genotype for sibship i over n siblings; G i j C , genotype of sibling j in sibship i centered around G i F ; PC, principal component.

Standard errors from both estimators were clustered over families at the sibling level to account for nonrandom clustering of siblings within families. Note that this clustering accounts for sibling relationships but does not account for further relatedness present in each sample. For example, a sibling pair could be related to another sibling pair (that is, two pairs of siblings who are first-cousins). We performed simulations, described below, confirming that such relatedness can lead to underestimating standard errors in the population model and has no effect on the standard errors of the within-sibship model.

GWAS models were performed in individual studies, harmonized and then meta-analyzed for each phenotype using a fixed-effects model in METAL 50 with population and within-sibship data meta-analyzed separately. We performed meta-analyses using only samples of European ancestry. We used data from 13,856 individuals from the China Kadoorie Biobank separately in downstream analyses. Information on sample sizes for individual phenotypes is contained in Supplementary Table 2 . Information on further quality control performed before meta-analysis is detailed in the Supplementary Methods .


### Meta-analysis

Phenotypes were harmonized between studies using phenotypic summary data on means and standard deviations. GWAS of study-specific phenotypes that did not conform to analysis plan definitions (for example, binary instead of continuous) were excluded from meta-analyses. GWAS presented in different continuous units (for example, not standardized) were transformed before meta-analysis by dividing association estimates and standard errors by the standard deviation of the phenotype as measured in the cohort. Meta-analyses for 25 phenotypes were performed using a fixed-effects model in METAL 50 .


### [AUTHOR]-sibship and population-based GWAS comparison


#### Overview

We hypothesized that the within-sibship estimates would differ compared with population-based estimates due to the exclusion of effects from demographic and familial pathways. In general, these effects have been shown to inflate (rather than shrink) population-based estimates, so we estimated within-sibship shrinkage (the % difference from population to within-sibship estimates). To estimate this shrinkage, we required estimates of the associations with a phenotype from each within-sibship and population-based analysis that was not affected by winner’s curse. Hence, we adopted a strategy where we used an independent reference dataset to select the variants associated with a phenotype. Using the meta-analysis results to obtain association estimates for these variants, we generated summary-based weighted scores of those association estimates in the within-sibship and population-based analyses and estimated the ratio of those scores. We used the UK Biobank dataset excluding sibling data as the independent reference dataset.


#### GWAS in independent reference discovery dataset

We performed GWAS in an independent sample of UK Biobank (excluding siblings) for each phenotype using a linear mixed model as implemented in BOLT-LMM 51 . We started with a sample of 463,006 individuals of ‘European’ ancestry derived using in-house k -means cluster analysis performed using the first four principal components provided by UK Biobank with standard exclusions also removed 52 . To remove sample overlap, we then excluded the sibling sample ( N = 40,276), resulting in a final sample of 422,730 individuals. To model population structure in the sample, we used 143,006 directly genotyped SNPs, obtained after filtering on MAF > 0.01; genotyping rate > 0.015; Hardy–Weinberg equilibrium P < 0.0001; and LD pruning to an r 2 threshold of 0.1 using PLINK v.2.0 (ref. 53 ). Age and sex were included in the model as covariates.

All 25 phenotypes (conforming to our phenotype definition) were available in UK Biobank data except for a continuous measure of depressive symptoms. For depressive symptoms, we performed a GWAS of binary depression which was excluded from the meta-analysis (see definition in Supplementary Materials). Using the BOLT-LMM UK Biobank GWAS summary data, we performed strict LD clumping in PLINK v.2.0 (ref. 53 ) ( r 2 < 0.001, physical distance threshold = 10,000 kb) using the 1000 Genomes Phase 3 EUR reference panel 54 to generate independent variants associated with each phenotype at genome-wide significance ( P < 5 × 10 −8 ) and at a more liberal threshold ( P < 1 × 10 −5 ).


#### Summary-based weighted scores

For a particular phenotype the sets of independent variants obtained from the independent UK Biobank GWAS were used to generate a summary-based weighted score using an inverse variance weighting (IVW) approach 55 , 56 :



| S = ∑ k M w k β k σ k 2 ∑ k M w k 2 σ k 2 |
| --- |




| σ S = 1 ∑ k M w k 2 σ k 2 |
| --- |


Here, the score S represents the weighted average of the association estimates of the M variants on a phenotype, where β and σ represent the beta coefficients and standard errors from the within-sibship (W) or population-based (P) meta-analysis results. The discovery association estimates from the UK Biobank GWAS were used as weights ( w ). The set of M variants were determined using either the genome-wide significance (G) or the more liberal threshold (L). Hence, depending on which model is used to determine the association estimates and which set of SNPs are used, four scores can be calculated for each phenotype— S P,G , S P,L , S W,G and S W,L .

These sets of scores were obtained for each of the 25 phenotypes with weights for binary depression used as a substitute for depressive symptoms because a suitable measure was unavailable in UK Biobank. The scores were strongly associated with the set of phenotypes in the meta-analysis data based on determining P values from their Z scores. The S W,L scores were nominally associated at P < 0.05 for 24 of 25 (exception: number of children) of the phenotypes, with the S P,L scores associated with all 25 phenotypes at this threshold (Supplementary Table 9 ).


#### Estimating shrinkage from population to within-sibship estimates

We used the within-sibship and population-based scores to calculate the average shrinkage ( δ , that is, proportion decrease) of genetic variant–phenotype associations



| δ = 1 − S W , S P , |
| --- |


The standard errors of δ could be estimated using the delta method as below using the standard errors of the scores and the covariance between the scores Cov( S w , S P ,):



| σ δ ~ S W , S P , σ S W , 2 S W , 2 + σ S P , 2 S P , 2 − 2 Cov S w , , S P , S W , S P , |
| --- |


However, we do not have an estimate of this covariance term because the two GWAS were fit in separate regression models. We therefore used the jackknife to estimate σ δ . For a score of M variants, we removed each variant in turn and repeated IVW and shrinkage analyses as above, extracting the shrinkage point estimate in each of the M iterations. We then calculated σ δ as follows:



| σ δ = M − 1 M ∑ k M ( σ δ , k − μ ) 2 |
| --- |




| μ = ∑ k M σ δ , k M |
| --- |


As a sensitivity analysis, we investigated the effects of positive covariance between the population and within-sibship models on the shrinkage standard errors using individual-level participant data from UK Biobank. Analyzing shrinkage on height, we used seemingly unrelated regression to estimate the covariance term between the population and within-sibship estimators. We found that standard errors for shrinkage estimates decreased by around 15% when the covariance was modeled (Supplementary Table 10 ). Seemingly unrelated regression standard errors were consistent with the jackknife approach standard errors.

As the primary analysis, we reported shrinkage results using the liberal threshold ( P < 1 × 10 −5 ), with results using the genome-wide threshold ( P < 5 × 10 −8 ) reported as a sensitivity analysis. In the main text, we report the shrinkage estimates that reach nominal significance ( P < 0.05). We presented shrinkage estimates in terms of % (multiplying by 100).

As a sensitivity analysis, we also presented study-level shrinkage estimates for height and educational attainment and tested for heterogeneity. These phenotypes were chosen because of previous evidence for shrinkage on these phenotypes and available data.


### Heterogeneity of shrinkage across variants within a phenotype

We used results of the within-sibship and population-based meta-analyses to estimate whether shrinkage estimates were consistent across all variants within a phenotype, using an estimate of heterogeneity. As above, we only evaluated heterogeneity for height and educational attainment because of previous evidence and available data. For each variant we estimated the Wald ratio of the shrinkage estimate



| s k = β P , k β W , k |
| --- |


The heterogeneity estimate was obtained as



| Q = ∑ k M w k 2 s k − S 2 |
| --- |




| w k = S 2 σ W , k 2 + S 2 σ S 2 |
| --- |



### Applying LDSC to within-sibship data

LDSC is a widely used method that can be applied to GWAS summary data to estimate heritability and genetic correlation 20 , 23 . The LDSC ratio, a function of the LDSC intercept unrelated to statistical power, is a measure of the proportion of association signal that is due to confounding. In this work, we apply LDSC to estimate SNP heritability and genetic correlation using the population and within-sibship GWAS data, so we investigated the LDSC intercept/ratio estimates from these data. Further detail is contained in the Supplementary Methods .

LDSC confounding estimates varied across the 25 phenotypes in the within-sibship model. Confounding estimates were modest for height (10%; 95% CI 6%, 14%) and BMI (9%; 2%, 16%), while the estimate for educational attainment was imprecise (35%; 12%, 57%). Across all phenotypes in the within-sibship data, the median confounding estimate was 21% (Q1–Q3: 10%, 28%), but stronger conclusions are limited by imprecise estimates (Supplementary Table 11 and Extended Data Fig. 8 ). The LDSC confounding estimates were higher using the population GWAS data (median 42%: Q1–Q3, 35%, 56%) than both the within-sibship model and previous studies (Supplementary Table 12 ). For example, the population model LDSC ratio estimates were higher for height (23%; 21%, 26%), BMI (22%; 19%, 25%) and educational attainment (41%; 37%, 45%).


#### Extended Data Fig. 8. LDSC estimates of confounding across 25 phenotypes using within-sibship data.


> **Figure/Table Caption:** BMI = body mass index, EverSmk = ever smoking, SBP = systolic blood pressure, WHR = waist-hip ratio, AFB = age at first birth, PA = physical activity, CPD = cigarettes per day, TG = triglycerides, CRP = C-reactive protein, eGFR = estimated glomerular filtration rate, FEV1 = forced expiratory volume, FEV1FVC = ratio of FEV1/forced vital capacity, HbA1c = Haemoglobin A1C. Extended Data Figure 8 shows LDSC ratio estimates and corresponding 95% confidence intervals 25 phenotypes using the within-sibship meta-analysis data. The LDSC ratio is a measure of the % of the polygenic signal attributable to confounding in a GWAS dataset. The number of individuals contributing to each phenotype ranged from n = 149,174 for height to n = 13,375 for age at menopause. Further information on the sample sizes of each phenotype are contained in Supplementary Table 2 .

The observed nonzero confounding in the within-sibship model was unexpected because of the intuition that the within-sibship GWAS models are unlikely to be confounded. The LDSC ratios in the population GWAS were also higher than previous studies. We followed up these findings by evaluating the effects of LD score mismatch and cryptic relatedness on the LDSC ratios.


### Evaluation of LD score mismatch

A large proportion of samples in the meta-analysis were from UK-based studies such as UK Biobank and Generation Scotland, for which the LD scores, generated using 1000 Genomes project (phase 3) European samples (CEU, TSC, FIN, GBR), have been shown to fit reasonably well 20 . However, a large number of samples were from Scandinavian populations (HUNT study, FinnTwin), where LD mismatch leading to elevated LDSC intercept/ratios has been previously discussed 20 . We investigated this possibility using empirical and simulated data.

We investigated variation in LDSC ratios across populations by comparing ratios for height across well-powered individual studies ( N > 5,000): UK Biobank, HUNT, the China Kadoorie Biobank (using default East Asian LD scores), Generation Scotland, DiscovEHR, Queensland Institute of Medical Research (QIMR) study and FinnTwin. We found some evidence of heterogeneity between studies: ratio estimates were higher in Scandinavian studies compared with UK-based studies (Extended Data Fig. 9 ). We also calculated within-sibship ratio estimates for BMI, SBP and educational attainment using UK Biobank summary data. UK Biobank estimates were largely consistent with zero confounding although confidence intervals were wide (Supplementary Table 13 ).


#### Extended Data Fig. 9. LDSC ratios from height GWAS.


> **Figure/Table Caption:** Extended Data Figure 9 shows LDSC ratio estimates and corresponding 95% confidence intervals for height GWAS from the summary data of 7 individual studies and the meta-analysis of European studies. The LDSC ratio is a measure of the % of the polygenic signal attributable to confounding in a GWAS dataset. The number of individuals in the meta-analysis estimate was n = 149,174 with the sample sizes for the displayed individual studies ranging from n = 40,068 in UK Biobank to 8,810 in the Finnish Twin Cohort. Further information on available height data in each phenotype are contained in Supplementary Table 1 .

We also performed simulations to evaluate potential mismatch between the Norwegian HUNT study and the default LD scores, which were generated using 1000 Genomes data, finding evidence of LD score mismatch between the 1000 Genomes LD scores and HUNT. The simulation setup and results are detailed in the Supplementary Methods .

The combined findings from the empirical and simulated analyses suggest that LD score mismatch with the 1000 Genomes LD scores in the Norwegian HUNT study and other studies likely contributed to inflated LDSC ratios in both population and within-sibship GWAS models.


### Cryptic relatedness

One source of inflation in GWAS associations is cryptic relatedness: nonindependence between close relatives in the study sample results which leads to inflated precision. In sibling GWAS models we clustered standard errors over sibships, but this clustering does not account for nonindependence between related sibships, for example, uncle/mother and two offspring. Inflated signal relating to cryptic relatedness may result in confounded signal, which is detected by the LD score intercept/ratio. In conventional population GWAS, either close relatives are removed or a mixed model is used to account for close relatives. We performed empirical and simulated analyses detailed in the Supplementary Methods to investigate the effect of cryptic relatedness on the population and within-sibship models.

The results suggest that the standard errors in the within-sibship model are not underestimated because of cryptic relatedness relating to common environmental effects shared between relatives. Thus, cryptic relatedness likely inflated LDSC ratios in the population models but not in the within-sibling data.


### [AUTHOR]-sibship SNP heritability estimates

LDSC was used to generate SNP heritability estimates for 25 phenotypes using the LDSC harmonized (see above) meta-analysis summary data. The summary data were harmonized using the LDSC munge_sumstats.py function, and we used the precomputed European LD scores from 1000 Genomes Phase 3.

LDSC requires a sample size parameter N to estimate SNP heritability. For this parameter, we used the effective sample size for each meta-analysis phenotype, equivalent to the number of independent observations. This was estimated as follows using GWAS standard errors, minor allele frequencies and the phenotype standard deviations (after adjusting for covariates).



| Effective N = 1 s.e. 2 s.d. _ Resid 2 2 × MAF × ( 1 − MAF ) |
| --- |


s.e., GWAS model standard error; MAF, MAF of the variant; s.d._Resid, standard deviation of the regression residual.

Effective sample size was estimated for each individual study GWAS and each model (for example, UK Biobank population GWAS of height). To reduce noise from low-frequency variants, we restricted to variants with MAF between 0.1 and 0.4 (from 1000 Genomes EUR). At the meta-analysis stage, the effective sample size for each variant was calculated as the sum of sample sizes of studies in which the variant was present. Simulations evaluating the use of effective sample sizes are detailed in the Supplementary Methods .

In empirical analyses, we decided to focus on the differences between the population model ( h Pop 2 ) and within-sibship model ( h WS 2 ) SNP heritability estimates. If we assume that biases affect the estimates equally then the difference between the two estimates will be unbiased. We estimated the difference between the heritability estimates ( h Diff 2 ) using a difference-of-two-means test 57 as below.



| h Diff 2 = h Pop 2 − h WS 2 |
| --- |




| s.e. h Diff 2 ~ s.e. ( h Pop 2 ) 2 + s.e. ( h WS 2 ) 2 − 2 Cov ( h Pop 2 , h WS 2 ) |
| --- |


To estimate Cov ( h Pop 2 , h WS 2 ) , we computed the cross-GWAS LDSC intercept between the population and within-sibship GWAS data (for the same phenotype) which is an estimate of Cor ( h Pop 2 , h WS 2 ) . The estimates of this term were ~0.40 across phenotypes. We then calculated the covariance term as follows:



| Cov ( h Pop 2 , h WS 2 ) = Cor ( h Pop 2 , h WS 2 ) × s.e. ( h Pop 2 ) × s.e. ( h WS 2 ) |
| --- |


We used the difference Z score (that is, h Diff 2 s.e. h Diff 2 ) to generate a P value for the difference between h Pop 2 and h WS 2 . In the text, we report differences reaching nominal significance (difference P < 0.05).

We calculated the expected effect of shrinkage on LDSC SNP heritability estimates. LDSC heritability estimates ( h 2 ) are derived from the formulation below 20 :



| χ 2 ~ N h 2 l j M + N a + 1 |
| --- |


where χ 2 is the square of the GWAS Z score, N is the sample size, M is number of variants such that h 2 M is the average heritability for each variant, l j is the LD score of variant j and a is the effect of confounding biases.

Uniform shrinkage across the genome would lead to GWAS Z scores being multiplied by a factor (1 − k ), where k is the shrinkage coefficient, and χ 2 statistics being multiplied by (1 − k ) 2 . As above, we have used effective sample size to account for differences in N between the population and within-sibship models. Therefore, assuming all other coefficients remain consistent, the expectation of h WS 2 can be written as a function of k and h Pop 2 .



| h Pop 2 = y |
| --- |




| h WS 2 = ( 1 − k ) 2 y |
| --- |


To evaluate the sensitivity of our results to assumptions of heritability models, we also estimated SNP heritability using SumHer 21 , which allows the use of different heritability models with regard to how local LD and allele frequencies affect the heritability contributions of individual SNPs. In SumHer analyses, we followed the same procedure as above for LDSC using effective sample sizes and estimating SNP heritability for all 25 phenotypes. We used the LDAK-Thin model with the precomputed tagging file over the BLD-LDAK model because of the limited power of our datasets (the BLD-LDAK model includes additional parameters so generates less precise estimates).


### [AUTHOR]-sibship r g with educational attainment

We used LDSC to estimate r g between educational attainment and other phenotypes using both population and within-sibship data. LDSC requires nonzero heritability to generate meaningful r g estimates, so we restricted analyses to the 22 phenotypes with SNP heritability point estimates greater than zero in both population and within-sibship models (that is, omitted physical activity and ratio of forced expiratory volume (FEV1)/forced vital capacity (FEV1FVC)). We estimated only pairwise genetic correlations between educational attainment and all other phenotypes because of previous evidence that educational attainment is influenced by demographic and indirect genetic effects and, given the limited statistical power, to reduce the multiple testing burden. Estimates failed to converge for genetic correlation analyses involving age at first birth and age at menopause, so these phenotypes were not analyzed here. We estimated the difference between the population ( r g,Pop ) and within-sibship ( r g,WS ) estimates ( r g,Diff ) using a difference-of-two-means test 57 .



| r g , Diff = r g , Pop − r g , WS |
| --- |


We used the jackknife to estimate the standard error of the difference, s.e. ( r g , Diff ) . After restricting to ~1.2 million Hapmap 3 variants present in the 1000 Genomes LD scores, we ordered variants by chromosome and base pair and separated variants into 100 blocks. We removed each block in turn and computed r g , Diff using LDSC 100 times. We then calculated s.e. ( r g , Diff ) across the 100 iterations as follows:



| s.e. ( r g , Diff ) = 99 100 ∑ 1 100 ( r g , Diff k − μ ) 2 |
| --- |




| μ = ∑ 1 100 r g , Diff , k 100 |
| --- |


r g , Diff , k is the r g estimate in the k th iteration and μ is the mean r g estimate across all 100 iterations.

We used the difference Z score (that is, r g , Diff s.e. r g , Diff ) to generate a P value for heterogeneity between r g , Pop and r g , WS . In the text, we report differences reaching nominal significance (heterogeneity P < 0.05).


### WS-MR: effects of height and BMI

We performed MR analyses using the within-sibship meta-analysis GWAS data to estimate the effect of two exposures (height and BMI) on 23 outcome phenotypes. For the exposure instruments, we used 803 and 418 independent genetic variants for height and BMI, respectively. These variants were identified by LD clumping in PLINK ( r 2 < 0.001, physical distance threshold = 10,000 kb, P < 5 × 10 −8 ) using the 1000 Genomes Phase 3 EUR reference panel 54 . We then performed an MR-IVW analysis using the within-sibship meta-analysis data to estimate the effect of the exposure on the outcome as



| β MR = ∑ β Exp * β Out ( σ Out ) 2 / ∑ ( β Exp ) 2 ( σ Out ) 2 |
| --- |


where β Exp is the association estimate from exposure GWAS, β Out is the association estimate from outcome GWAS and σ Out is the standard error from outcome GWAS.

We also performed MR analyses using the population meta-analysis GWAS data for comparison. We estimated differences between population MR and WS-MR estimates using the difference-of-two-means test 57 :



| β MR , Diff = β MR , Pop − β MR , WS |
| --- |


We used the jackknife to estimate the standard error of the difference, s.e.( β MR,Diff ). With n genetic instruments, we removed each variant from the analysis in turn and then computed β MR,Diff , storing the estimate from the n iterations. We then calculated s.e.( β MR,Diff ) as follows:



| s.e. ( β MR , Diff ) = n − 1 n ∑ 1 n ( β MR , Diff , k − μ ) 2 |
| --- |




| μ = ∑ 1 n β MR , Diff , k n |
| --- |


n is the number of genetic variants used as instruments, β MR, Diff, k is the β MR, Diff estimate in the k th iteration and μ is the mean β MR, Diff estimate across all n iterations.

We used the difference Z score (that is, β MR , Diff s.e. β MR , Diff ) to generate a P value for heterogeneity between β MR, Pop and β MR,WS . In the text, we report differences reaching nominal significance (heterogeneity P < 0.05).


### Polygenic adaptation

Polygenic adaptation was estimated using similar methods to a previous publication 28 . Precomputed SDS were downloaded for UK10K data from https://web.stanford.edu/group/pritchardlab/ . Genomic regions under strong recent selection ( MHC chr6: 25,892,529–33,436,144; lactase chr2: 134,608,646–138,608,646) were removed and SDS were normalized within each 1% allele frequency bin.

SDS were merged with GWAS meta-analysis data for 25 phenotypes. Variants with low effective sample sizes (<50% of maximum) were removed for each phenotype. SDS were transformed to tSDS such that the reference allele was the phenotype-increasing allele.

Spearman’s rank test was used to estimate the correlation between tSDS and the absolute value of GWAS Z scores from the population and within-sibship models. Standard errors were estimated using the jackknife. The genome was ordered by chromosome and base pair and divided into 100 blocks. Correlations were estimated 100 times with each k th block removed in turn. The standard error of the correlation estimate, s.e.(Cor), was calculated as follows:



| s.e. Cor = 99 100 ∑ 1 100 ( Cor k − μ ) 2 |
| --- |




| μ = ∑ 1 100 Cor k 100 |
| --- |


Cor k is Spearman’s rank correlation estimate in the k th iteration and μ is the mean correlation estimate across the 100 iterations.

Given previous concerns 26 , 27 , we performed several sensitivity analyses for the height analysis detailed in the Supplementary Methods .


### Reporting Summary

Further information on research design is available in the Nature Research Reporting Summary linked to this article.


## Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at [REDACTED_DOI].


## Supplementary information

Supplementary information—consortia, funding, cohort descriptions, phenotype definitions and supplementary methods.

Excel file with all supplementary tables in.


## Acknowledgements

L.J.H., T.T.M., Y.C., D.A.L., G.D.S., G.H. and N.M.D. work in a unit that receives support from the University of Bristol and the UK MRC (grant nos. MC_UU_00011/1 & 6). N.M.D. is supported by a Norwegian Research Council Grant (no. 295989). G.H. is supported by the Wellcome Trust and Royal Society (grant no. 208806/Z/17/Z). B.M.B., B.O.Å., H.R., A.F.H. and K.H. work in a research unit funded by Stiftelsen Kristian Gerhard Jebsen, the Liaison Committee for education, research and innovation in Central Norway and the Joint Research Committee between St. Olavs Hospital and the Faculty of Medicine and Health Sciences, NTNU. Funding information for other co-authors is contained in the Supplementary information . We thank H. Mostafavi and J. Pritchard for helpful suggestions and guidance relating to the polygenic adaptation analyses.


### Extended data



L.J.H., M.G.N., T.T.M., Y.C., J.B.P., J.F.W., J.L.H., S.L., M.C.S., D.A.L., N.G.M., A.H., K.H., C.J.W., B.O.Å., P.D.K., J.K., S.E.M., D.J.B., P.T., D.M.E., G.D.S., C.H., B.M.B., G.H. and N.M.D. were closely involved in conceptualizing and designing the study. J.K., K.P.H., E.M.T.D., S.M.K., H.C., J.F.W., E.J.C.D., R.P., J.A.S., P.A.P., S.L.R.K., S.L., J.L.H., M.C.S., K.C., N.M.D., S.E.M., N.G.M., B.M.B., R.G.W., I.Y.M., K.L., K.H., C.J.W., C.R.B., A.E.J., D.P., C.H. and A.C. were involved in data and funding acquisition. L.J.H. developed the GitHub GWAS pipeline with support from G.H. and N.M.D. and programming code from G.H. and P.T. (via SSGAC). C.H. kindly beta tested the GWAS pipeline and suggested improvements. Other analysts (listed below) also made major contributions to the GWAS pipeline. L.J.H., S.G., A.F.H., H.R., C.H., Y.C., G.C., R.A., P.A.L., T.P., M.D.V.Z., R.C., M.M., Y.W., S.L., L.K., S.M.R., L.F.B., C.A.R., M.N., J.V.B., A.G. and E.A.W. performed GWAS analyses in individual cohorts with the support and guidance of N.M.D., G.H., B.M.B., R.G.W., I.Y.M., K.L., S.O., A.E.J., S.E.M., J.K., M.G.N., M.B., J.B.P., S.H., J.L.H., J.F.W., J.A.S., P.A.P., S.L.R.K., K.C., M.C.K. and J.J.L. L.J.H. performed meta-analyses and all downstream analyses with the meta-analysis data. L.J.H. drafted the first version of the manuscript. M.G.N., T.T.M., B.O.Å., P.D.K., J.K., S.E.M., R.G.W., D.J.B., P.T., D.M.E., G.D.S., C.H., B.M.B., G.H. and N.M.D. played a key role in interpreting the results, planning additional analyses and revising the manuscript. All authors contributed to and critically reviewed the manuscript.


## Peer review


### Peer review information

Nature Genetics thanks David Cesarini and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Peer reviewer reports are available.


## Data availability

European meta-analysis summary statistics for both the within-sibship and population GWAS models are publicly available on OpenGWAS ( https://gwas.mrcieu.ac.uk/ ). The relevant GWAS IDs in OpenGWAS are ieu-b-4813 to ieu-b-4860 (for example, within-sibship GWAS estimates for height are in https://gwas.mrcieu.ac.uk/datasets/ieu-b-4813/ ). A description of the available summary data will be on the consortium website ( https://www.withinfamilyconsortium.com/home/ ). UK Biobank individual-level participant data are available via enquiry to [EMAIL_REDACTED]. Researchers associated with Norwegian research institutes can apply for the use of HUNT data and samples with approval by the Regional Committee for Medical and Health Research Ethics. Researchers from other countries may apply if collaborating with a Norwegian Principal Investigator. Information for data access can be found at https://www.ntnu.edu/hunt/data . Generation Scotland data access can be applied for via enquiry to [EMAIL_REDACTED]. Please see https://www.ed.ac.uk/generation-scotland/for-researchers/access . Researchers interested in China Kadoorie Biobank data access should contact [EMAIL_REDACTED]. Please see https://www.ckbiobank.org/site/Data+Access . Researchers interested in TEDS data can complete a data request form at https://www.teds.ac.uk/researchers/teds-data-access-policy . Researchers interested in TwinsUK data can fill in a proposal form at https://twinsuk.ac.uk/resources-for-researchers/access-our-data/ . Researchers interested in data from ORCADES and Viking1 can contact [EMAIL_REDACTED]. GENOA data are available via application to dbGaP https://ega-archive.org/studies/phs000379 . Researchers interested in Swedish Twin Registry data can find instructions at https://ki.se/en/research/swedish-twin-registry-for-researchers . Researchers interested in Danish Twin Registry data can contact [EMAIL_REDACTED].


## Code availability

Code for running GWAS analyses is available on GitHub ( [GITHUB_REPO_REDACTED] ) 58 . Code for downstream analyses is available ( [GITHUB_REPO_REDACTED] ) 59 .


## Competing interests

O.A.A. is a consultant to HealthLytix in a capacity unrelated to this work. All other authors declare no competing interests.


## Footnotes

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


Lists of authors and their affiliations appear at the end of the paper.


## Contributor Information

Laurence J. Howe, Email: [EMAIL_REDACTED]

Ben [AUTHOR], Email: [EMAIL_REDACTED].

Gibran [AUTHOR], Email: [EMAIL_REDACTED].

Neil M. [AUTHOR], Email: [EMAIL_REDACTED]

[AUTHOR] Science Genetic Association Consortium:

Hyeokmoon [AUTHOR] , Philipp D. [AUTHOR] , Daniel J. [AUTHOR] , and Patrick [AUTHOR]

[AUTHOR] Family Consortium:

Laurence J. Howe , Michel G. [AUTHOR] , Tim T. [AUTHOR] , Ailin F. [AUTHOR] , Humaira [AUTHOR] , Yoonsu Cho , Geetha [AUTHOR] , Rafael [AUTHOR] , Penelope A. Lind , Teemu [AUTHOR] , Matthijs D. van der Zee , Rosa [AUTHOR] , Massimo [AUTHOR] , Yunzhang Wang , Shuai Li , Lucija [AUTHOR] , Scott M. [AUTHOR] , Lawrence F. [AUTHOR] , Marianne [AUTHOR] , Alexandros [AUTHOR] , Emily A. [AUTHOR] , Chandra A. [AUTHOR] , Jared V. [AUTHOR] , Ole A. [AUTHOR] , Helga Ask , Dorret I. [AUTHOR] , Archie [AUTHOR] , Harry [AUTHOR] , Zhengming Chen , Paraskevi [AUTHOR] , Elizabeth [AUTHOR] , Christina C. Dahm , Deepika R. [AUTHOR] , Luke M. [AUTHOR] , Eco J. C. de Geus , Sudheer [AUTHOR] , Scott D. [AUTHOR] , K. Paige [AUTHOR] , W. David Hill , Amanda [AUTHOR] , Shona M. Kerr , Yongkang Kim , Antti [AUTHOR] , Deborah A. [AUTHOR] , Liming Li , Kuang Lin , Per [AUTHOR] , Patrik K. E. [AUTHOR] , Travis T. [AUTHOR] , Pekka [AUTHOR] , Melinda C. [AUTHOR] , Pål Rasmus [AUTHOR] , Nancy L. [AUTHOR] , David J. [AUTHOR] , Karri [AUTHOR] , Melissa C. [AUTHOR] , Camilla [AUTHOR] , Elliot M. [AUTHOR] , Margaret J. [AUTHOR] , John K. [AUTHOR] , Matthew C. [AUTHOR] , Michael C. [AUTHOR] , James J. Lee , Kaare [AUTHOR] , Sharon L. R. [AUTHOR] , Patricia A. [AUTHOR] , Jennifer A. [AUTHOR] , James F. [AUTHOR] , John L. [AUTHOR] , Sara Hägg , Tim D. [AUTHOR] , Jean-Baptiste [AUTHOR] , Robert [AUTHOR] , Alexandra [AUTHOR] , Meike [AUTHOR] , Nicholas G. [AUTHOR] , Sven [AUTHOR] , Anne E. [AUTHOR] , Iona Y. [AUTHOR] , Kristian [AUTHOR] , Øyvind [AUTHOR] , Cristen J. [AUTHOR] , Bjørn Olav [AUTHOR] , Jaakko [AUTHOR] , Sarah E. [AUTHOR] , Robin G. [AUTHOR] , David M. [AUTHOR] , George [AUTHOR] [AUTHOR] , Caroline [AUTHOR] , Ben [AUTHOR] , Gibran [AUTHOR] , and Neil M. [AUTHOR]


### Extended data

is available for this paper at [REDACTED_DOI].


### Supplementary information

The online version contains supplementary material available at [REDACTED_DOI].

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials

Supplementary information—consortia, funding, cohort descriptions, phenotype definitions and supplementary methods.

Excel file with all supplementary tables in.


### Data Availability Statement

European meta-analysis summary statistics for both the within-sibship and population GWAS models are publicly available on OpenGWAS ( https://gwas.mrcieu.ac.uk/ ). The relevant GWAS IDs in OpenGWAS are ieu-b-4813 to ieu-b-4860 (for example, within-sibship GWAS estimates for height are in https://gwas.mrcieu.ac.uk/datasets/ieu-b-4813/ ). A description of the available summary data will be on the consortium website ( https://www.withinfamilyconsortium.com/home/ ). UK Biobank individual-level participant data are available via enquiry to [EMAIL_REDACTED]. Researchers associated with Norwegian research institutes can apply for the use of HUNT data and samples with approval by the Regional Committee for Medical and Health Research Ethics. Researchers from other countries may apply if collaborating with a Norwegian Principal Investigator. Information for data access can be found at https://www.ntnu.edu/hunt/data . Generation Scotland data access can be applied for via enquiry to [EMAIL_REDACTED]. Please see https://www.ed.ac.uk/generation-scotland/for-researchers/access . Researchers interested in China Kadoorie Biobank data access should contact [EMAIL_REDACTED]. Please see https://www.ckbiobank.org/site/Data+Access . Researchers interested in TEDS data can complete a data request form at https://www.teds.ac.uk/researchers/teds-data-access-policy . Researchers interested in TwinsUK data can fill in a proposal form at https://twinsuk.ac.uk/resources-for-researchers/access-our-data/ . Researchers interested in data from ORCADES and Viking1 can contact [EMAIL_REDACTED]. GENOA data are available via application to dbGaP https://ega-archive.org/studies/phs000379 . Researchers interested in Swedish Twin Registry data can find instructions at https://ki.se/en/research/swedish-twin-registry-for-researchers . Researchers interested in Danish Twin Registry data can contact [EMAIL_REDACTED].

Code for running GWAS analyses is available on GitHub ( [GITHUB_REPO_REDACTED] ) 58 . Code for downstream analyses is available ( [GITHUB_REPO_REDACTED] ) 59 .
