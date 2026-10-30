# FEXP_ANON_063

## Abstract

Oxidative stress is one of the leading causes of aging and aging-related diseases. However, there is no conclusive evidence on whether dietary antioxidants can decelerate epigenetic age in human. A two-sample Mendelian randomization (MR) analysis was conducted to explore the causal associations between dietary antioxidants intake and epigenetic age. Summary-level data about 4 dietary antioxidants (vitamin A, vitamin C, vitamin E and carotene) and 4 epigenetic age measures (HannumAge, Intrinsic epigenetic age acceleration [IEAA], GrimAge and PhenoAge) were respectively got from FinnGen Project Database and a meta-analysis of 28 genome-wide association studies (GWAS) involving 34,710 European participants. Inverse variance weighted (IVW) was used as the main method to evaluate causal estimates complemented by other 4 methods (Weighted median, MR-Egger, Weighted mode and Simple mode). Genetically predicted dietary vitamin C was associated with decreased HannumAge (IVW: beta = -1.1988, P = .0014; weighted median: beta = −1.3342, P = .0112). IVW method found that dietary vitamin C was marginally associated with decreased GrimAge (beta = −0.768, P = .0504), other 4 methods did not find significant association between dietary vitamin C and GrimAge, but the effect direction was similar to that by IVW. There was no significant association of dietary vitamin C with IEAA and PhenoAge. MR analyses found no significant effects of vitamin A, vitamin E and carotene on 4 epigenetic age measures. In total, the study suggested that dietary vitamin C may potentially decrease epigenetic age measured by HannumAge. Further studies are needed to assess the effect of dietary antioxidants on aging and aging-related diseases, and explore related mechanisms.

Keywords: biological age, dietary antioxidants, epigenetic age, Mendelian randomization study, vitamin C


## 1. Introduction

Aging is a time-dependent biological process characterized by progressive damage of cells and gradual decline in tissue and organ functions. [ 1 ] Aging is the major risk factor for the development of age-related diseases, including cardiovascular diseases, neurodegenerative disorders, and cancer. [ 2 ] These age-related diseases are the most prevalent all over the world and the leading causes of death. [ 3 ] It was reported that the age-standardized mortality rate per 100,000 population in 2021 around the world was 108.7 for ischemic heart disease, 87·4 for stroke, 25.2 for Alzheimer and other dementias, and 23·5 for lung cancer. [ 4 ] The progression of chronological age is consistent among all individuals, while significant inter-individual variability exists in biological age. [ 5 ] Compared with chronological age, biological age is a more accurate measure of health status, fully indicating the aging pace of an individual. [ 6 ] Effort to elucidate the underlying mechanism of the variability in biological age may shed light on the drivers of aging, and find the potential therapeutic targets for aging-related diseases. [ 7 ]

DNA methylation status has been found being closely associated with aging and lifespan. [ 8 ] Epigenetic age measures or epigenetic clocks have been developed as biomarkers of biological age based on the methylation feature of genetic variants associated with chronological age or age-related mortality. [ 9 ] Epigenetic age measures comprise a diverse set of models, including Hannum epigenetic age (HannumAge), Horvath epigenetic age (HorvathAge), PhenoAge and GrimAge. HannumAge is consisted of 71 age-related markers that were established using methylation data at particular cytosine-phosphate-guanine (CpG) sites from whole blood samples of 656 adults. [ 10 ] HorvathAge, the first multi-tissue epigenetic clock, was developed based on 193 positively age-related CpGs and 160 negatively age-related CpGs. [ 11 ] Intrinsic epigenetic age acceleration (IEAA) is developed from HorvathAge by regressing out blood cell estimates. [ 12 ] HannumAge and HorvathAge (including IEAA) are the first generation of epigenetic age measures, and present good performance in predicting chronological age. [ 10 , 11 ] PhenoAge and GrimAge are the second generation of epigenetic clocks. PhenoAge was developed using data from the Third National Health and Nutritional Survey, and 10 clinical characteristics have been taken into account. [ 13 ] The GrimAge comprises 7 plasma protein markers that were constructed using DNA methylation data and takes smoking variant among others as a risk factor. [ 14 ] PhenoAge and GrimAge present good performance in predicting age-related diseases and mortality. [ 13 , 14 ] The epigenetic age measures show better ability of predicting biological age than chronological age and other aging biomarkers such as telomere length. [ 12 ]

Epigenetic age acceleration (EAA) defines that the biological age of an individual measured by epigenetic clocks exceeds the chronological age. The populations with EAA experience increased risk of diseases and all-cause death. [ 14 – 18 ] Studies have found that EAA is associated with increased risks of cardiovascular diseases, including aortic valve stenosis, [ 19 ] incident atrial fibrillation [ 20 ] and heart failure. [ 21 ] A number of studies have also found the potential of epigenetic age for cancer risk prediction on the background of aging. [ 9 ] EAA is correlated with the development of lung cancer and cancer-related fatal event. [ 22 ] Zheng et al found that EAA showed a dose–response relationship with cancer risk. [ 23 ] Besides, EAA detected before chemoimmunotherapy in chronic lymphocytic leukemia patients shows significant association with the time of tumor relapse. [ 24 ] In total, aging-related diseases are the main disease burden worldwide, and slowing the progression of aging such as EAA is of great importance.

Oxidative stress can impair the structure and function of cells, tissues and organs, and be regarded as one of the leading causes of aging and aging-related diseases. [ 1 ] Anti-oxidative stress is considered a potential strategy to slow aging. [ 1 ] For example, a randomized clinical trial found that treatment with N-acetylcysteine and glycine reduces oxidative stress and several aging hallmarks, including mitochondrial dysfunction, insulin resistance, genomic damage and endothelial function dysfunction, in older participants. [ 25 ] However, the sample size is small, and supplementing N-acetylcysteine and glycine had no significant effect on the expression of protection of telomeres protein 1, a protein regulating telomere stability used as a hallmark of biological aging. [ 25 ] In addition to medicines, diet or dietary supplements also present modulating effects on oxidative stress levels. [ 1 ] Pre-clinical studies found that some dietary antioxidants, including vitamin C, vitamin E and carotene, show effects in improving aging in mouse models of aging. [ 26 – 28 ] For example, in a mouse model of aging, vitamin C treatment inhibits the progression of EAA. [ 26 ] Li et al found that vitamin C improves the features of aging in a premature aging model of human mesenchymal stem cells, including decreasing reactive oxygen species levels. [ 29 ] Basic experiments and small sample clinical trials indicated that dietary antioxidants may delay epigenetic age. However, the related results may be impacted by small sample size, reverse causality and unadjusted confounding factors. So far, there is no conclusive evidence on whether dietary antioxidants can improve epigenetic age in human.

Mendelian randomization (MR) study adopts genetic variants, randomly allocated during meiosis similar to intervention allocation in randomized controlled trials, as instrumental variables (IVs) to determine the causal effect of an exposure on an outcome. [ 30 ] Therefore the results by MR method are more robust to reverse causality and confounding factors than that by traditional observational methods. [ 30 ] In this study, a MR analysis was conducted to elucidate the causal effects of dietary antioxidants on epigenetic age.


## 2. Materials and methods


## 2.1. Study design and data source

A two-sample MR analysis was conducted to explore the causal associations between dietary antioxidants intake and epigenetic age. Vitamin A (retinol), vitamin C, vitamin E and carotene are common dietary antioxidants. Summary-level data of these 4 dietary antioxidants were got from FinnGen Project Database ( https://r11.finngen.fi/ ). The datasets about vitamin C, vitamin E and carotene include 64,979 European participants and 9851,867 single nucleotide polymorphisms (SNPs). The data about vitamin A involves 62,991 European participants and 9851,867 SNPs. The related details are shown in Table S1 (Supplemental Digital Content, https://links.lww.com/MD/Q486 ). Summary-level data about 4 epigenetic age measures, including HannumAge, IEAA, GrimAge and PhenoAge, was got from a meta-analysis of 28 genome-wide association studies (GWAS) involving 34,710 European participants. [ 31 ] The proportion of female participants was 57.3%. The meta-analysis identified 137 aging-related genomic loci. The details about these GWAS are shown in Table S2 (Supplemental Digital Content, https://links.lww.com/MD/Q486 ). A flow diagram shows the design of the present MR study (Fig. 1 ). The summary-level data of epigenetic age and dietary antioxidants were from different databases, which significantly decreased the possibility of sample overlap. This study was based on publicly available databases. Related studies and data had been approved by their relevant ethical review board and participants.


> **Figure 1.:** The flow diagram shows the design and process of this two-sample Mendelian randomization (MR) study. GWAS = genome-wide association study, IEAA = intrinsic epigenetic age acceleration, IVW = inverse variance weighted, MAF = Minor allele frequency, MR = Mendelian Randomization, MR-PRESSO = Mendelian randomization pleiotropy residual sum and outlier, SNP = single nucleotide polymorphism.


## 2.2. MR assumptions and instrumental variable extraction

In MR study, genetic variants (usually SNPs) associated with exposure phenotypes were extracted as IVs. IVs used in MR analysis must adhere to 3 key assumptions. [ 32 , 33 ] Firstly, genetic IVs should be closely related to the exposure phenotype. Secondly, genetic IVs should not be associated with confounding factors. Thirdly, the effect of genetic IVs on outcomes should be exclusively via influencing the exposure phenotype. The following processes were conducted to extract IVs from the summary data of exposure. To meet the first assumption, SNPs with genetic genome-wide significance in summary data of dietary antioxidants were extracted. Because of the limited number of SNPs for dietary antioxidants, the cutoff of significance was loosened to 5 × 10 −6 . To eliminate linkage disequilibrium, the clumping conditions were set as r 2 < 0.001 and kb > 10,000. F -statistics was calculated to assess the strength of IVs. The following formula was used: F -statistic=β 2 / SE 2 (β = effect size, SE = standard error). [ 34 ] SNPs with F -statistic ≥ 10 are regarded as strong genetic instruments to influence phenotype, and used as the IVs of exposure phenotype in MR analysis. [ 35 ] The SNPs with F-statistic < 10 are weak genetic instruments, and were excluded in MR analysis. To meet the second and third assumptions of MR analysis, SNPs related to confounding factors and outcomes were excluded through searching for the traits related to each SNP ( https://snipa.org/snipa3/ ). Palindromic SNPs with a MAF > 0.42 and ambiguous SNPs were also excluded. [ 36 ] Besides, the Steiger filtering was conducted to verify the directionality of each SNP used as IV. The Steiger filtering is a method to exclude SNPs explaining more variations in the outcome than in the exposure. [ 37 ]


## 2.3. The causal effects of dietary antioxidants on epigenetic age

We adopted random-effects inverse variance weighted (IVW) method as the main MR method when there was no obvious horizontal pleiotropy. IVW method presents the best power to detect effect size in the condition of all SNPs being valid IVs. [ 38 ] The horizontal pleiotropy was detected using MR-Egger intercept test. [ 39 ] MR-Egger method can assess causal effect estimates when there is significant horizontal pleiotropy, but usually demands a large sample size. When significant horizontal pleiotropy was found, the MR-Egger method was used as the main method in place of IVW to detect effect size. [ 40 ] Three other methods were used to complement the MR results by IVW or MR-Egger, including Weighted median, [ 41 ] Weighted mode [ 42 ] and Simple mode. The effect estimate detected by Weighted median method is robust if over half of SNPs are valid IVs. [ 41 ] The Weighted mode method detects the effect estimate based on the collection of the vast majority of SNPs with similar individual effect. [ 42 ] The causal associations of dietary antioxidants with epigenetic age were further confirmed by sensitivity analyses. Steiger test for directionality was performed to confirm the validity of directionality of causal effect estimate in MR analysis. [ 37 ] In sensitivity analyses, Mendelian randomization pleiotropy residual sum and outlier (MR-PRESSO) test was used to identify outlier SNPs and detect pleiotropy. [ 39 ] Leave-one-out analyses were implemented to estimate the role of a single SNP in the overall effect size detected. [ 43 ] Cochran Q statistic was conducted to detect the heterogeneity in the SNPs of exposure. [ 44 ]


## 2.4. Statistical analyses

R software 4.3.0 with the “TwoSampleMR” package was utilized to conduct statistical analyses and data visualization. [ 45 ] Differences with a two-sided P value < 0.05 were considered statistically significant.


## 3. Results


## 3.1. The extraction of IVs

We got 9 SNPs for vitamin A with 1 SNP (rs909570) not found in the outcome data, 11 SNPs for vitamin C with 1 SNP (rs61868302) not found in the outcome data, 12 SNPs for vitamin E, and 16 SNPs for carotene with 1 SNP (rs116995905) not found in the outcome data. The SNPs not found in the outcome data were deleted. There were 8 SNPs for vitamin A, 10 SNPs for vitamin C, 12 SNPs for vitamin E, and 15 SNPs for carotene in final MR analyses (Table S3, Supplemental Digital Content, https://links.lww.com/MD/Q486 ). All SNPs used as genetic instruments had a F-statistic value more than 10 and passed Steiger filtering test. The details about the genetic instruments for 4 dietary antioxidants are summarized in Tables S4–S7 (Supplemental Digital Content, https://links.lww.com/MD/Q486 ).


## 3.2. The effect of genetically predicted dietary vitamin C on epigenetic age

IVW method found that genetically predicted dietary vitamin C was associated with decreased HannumAge (beta = −1.1988, 95%CI (−1.9355, −0.462), P = .0014), and Weighted median got similar result (beta = −1.3342, 95%CI (−2.3654, −0.3031), P = .0112) (Fig. 2 A and Table S8, Supplemental Digital Content, https://links.lww.com/MD/Q486 ). The effect estimates assessed by MR-Egger, Weighted mode and Simple mode were in the same direction as that by IVW and Weighted median, but not significant. IVW method found that genetically predicted dietary vitamin C was marginally associated with decreased GrimAge (Beta = −0.768, 95%CI (−1.5373, 0.0013), P = .0504), other 4 methods did not find significant association between dietary vitamin C and GrimAge, but the effect direction was similar to that by IVW (Fig. 2 B). There were no significant association of genetically predicted dietary vitamin C with IEAA and PhenoAge (Fig. 2 C and D). The scatter plots about the causal associations of dietary vitamin C with epigenetic age measures detected by 5 MR methods are shown in Figure 3 . The causal effects of vitamin C on HannumAge and GrimAge detected by 5 MR methods were in the same direction (Fig. 3 A and B). Leave-one-out analysis showed the contribution of each SNP to the total effect size of the causal association (Fig. 4 ). There was no individual SNP with a disproportionate impact on the causal estimate between vitamin C and HannumAge (Fig. 4 A), while some SNPs presented a disproportionate impact on the causal estimate between vitamin C and GrimAge (Fig. 4 B). Steiger test for directionality was used to evaluate the reliability of causal inference. As shown in Table 1 , the causal associations detected in MR analyses were confirmed to be valid. As for the causal effect of genetically predicted dietary vitamin C on HannumAge and GrimAge, Cochran Q test found no significant heterogeneity, and MR-PRESSO and MR-Egger intercept analyses found no outliers and horizontal pleiotropy (Table 1 ). Therefore, the results were robust based on MR analyses and sensitivity analyses.


> **Figure 2.:** The causal effects of genetically predicted vitamin C on epigenetic age. (A–D) Forest map about the causal effects of genetically predicted vitamin C on 4 epigenetic age measures, including HannumAge (A), GrimAge (B), intrinsic epigenetic age acceleration (IEAA) (C) and PhenoAge (D). IVW = inverse variance weighted.


> **Figure 3.:** Scatter plot about the causal effects of genetically predicted dietary vitamin C on 4 epigenetic age measures, including HannumAge (A), GrimAge (B), IEAA (C) and PhenoAge (D). IEAA = intrinsic epigenetic age acceleration, IVW = inverse variance weighted, MR = Mendelian randomization, SNP = single nucleotide polymorphism.


> **Figure 4.:** Leave-one-out analyses based on the causal associations between dietary vitamin C and epigenetic age measures. HannumAge (A), GrimAge (B), IEAA (C) and PhenoAge (D). IEAA = intrinsic epigenetic age acceleration, MR = Mendelian randomization.


### Table 1: The pleiotropy, heterogeneity and directionality of Mendelian randomization analyses.

| Exposure | Outcome | MR-Egger intercept P value | MR-PRESSO global test P value | Cochran Q P value | Causal direction | Steiger test P value |
| Vitamin C | GrimAge | .3902 | .4183 | .3928 | True | 2.17E−09 |
| Vitamin C | HannumAge | .7554 | .5893 | .5463 | True | 3.39E−08 |
| Vitamin C | IEAA | .4872 | .2797 | .2697 | True | 1.66E−09 |
| Vitamin C | PhenoAge | .8058 | .3657 | .3346 | True | 4.25E−10 |
| Vitamin A | GrimAge | .777 | .6433 | .6209 | True | 4.01E−10 |
| Vitamin A | HannumAge | .6154 | .2267 | .2137 | True | 2.13E−08 |
| Vitamin A | IEAA | .3339 | .1973 | .1809 | True | 2.72E−08 |
| Vitamin A | PhenoAge | .3928 | .0523 | .0425 | True | 4.43E−07 |
| Vitamin E | GrimAge | .6856 | .9193 | .913 | True | 7.70E−15 |
| Vitamin E | HannumAge | .7505 | .1063 | .1004 | True | 6.33E−11 |
| Vitamin E | IEAA | .2027 | .072 | .0622 | True | 4.81E−10 |
| Vitamin E | PhenoAge | .9533 | .6093 | .5867 | True | 1.09E−13 |
| Carotene | GrimAge | .368 | .16 | .1595 | True | 2.37E−13 |
| Carotene | HannumAge | .6018 | .942 | .943 | True | 2.03E−18 |
| Carotene | IEAA | .0272 | .8223 | .8333 | True | 3.28E−17 |
| Carotene | PhenoAge | .324 | .4543 | .4318 | True | 7.01E−15 |

## 3.3. The effect of genetically predicted dietary vitamin A, vitamin E and carotene on epigenetic age

MR analyses found no significant effects of genetically predicted dietary vitamin A, vitamin E and carotene on 4 epigenetic age measures (Table S8, Supplemental Digital Content, https://links.lww.com/MD/Q486 ).


## 4. Discussion

Epigenetic age is an important biological age marker, and EAA involves in the development of aging-related diseases. Previous basic experiments and observational studies have indicated the potential role of dietary antioxidants in modulating aging, including EAA. However, there is no conclusive evidence on whether dietary antioxidants can improve epigenetic age in human. To the best of our knowledge, this is the first MR study to detect the causal relationship between dietary antioxidants and epigenetic age. We found that genetically predicted dietary vitamin C was associated with decreased epigenetic age of HannumAge, and marginally related with decreased GrimAge. There was no significant association of dietary vitamin C with IEAA and PhenoAge. MR analyses found no significant effects of vitamin A, vitamin E and carotene on 4 epigenetic age measures.

Vitamin C is a classic dietary antioxidant. A previous study found that vitamin C levels in plasma and tissue decreased, while cardiac lipid peroxidation increased in an aging model of rat. [ 46 ] Vitamin C treatment slows the aging of human pluripotent stem cell-derived cardiomyocytes. [ 47 ] In a mouse model of aging, vitamin C shows inhibiting effect on EAA. [ 26 ] These basic experiments indicate a protective effect of vitamin C on the progression of aging or EAA, but its effect on human epigenetic age is undefined. A previous observational study found that dietary vitamin C was related with reduced HannumAge, [ 48 ] which is supported by the present MR study. We found that genetically predicted dietary vitamin C was associated with decreased epigenetic age of HannumAge. Our findings add evidence to the inhibiting effect of vitamin C on HannumAge. Endothelial function is an important phenotype of vascular aging. A meta-analysis found that supplement with vitamin C improves endothelial function in adults, especially in the old participants. [ 49 ] As for the possible mechanisms, vitamins C has been shown to decrease oxidative stress through lowing IL-6 and hs-CRP levels, and neutralizing free radicals. [ 50 ] In addition to improving oxidative stress-induced cellular injury, the anti-aging effects of vitamin C also include inhibiting telomere shortening and chromatin damage. [ 51 ]

We found that genetically predicted dietary vitamin C was marginally associated with decreased GrimAge. The result is partly supported by a previous MR study finding that dried fruit intake reduces accelerated GrimAge. [ 52 ] Dried fruit is one of the important sources of vitamin C intake. However, dried fruit also contains other vitamins and nutrients, which may also play a role in regulating epigenetic age. Our MR study specifically focused on the causal associations of dietary antioxidants with epigenetic age. In the present study, genetically predicted dietary vitamin C showed no significant effect on PhenoAge and IEAA. It is partly supported by an observational study by Bordoni et al. [ 48 ]

There are inconsistencies about the associations of vitamin C with 4 epigenetic age measures. However, the inconsistencies across different epigenetic clocks do not necessarily deny our results. Because these epigenetic clocks were trained on different set of CpGs associated with different tissues, risk factors, clinical features or outcomes. [ 53 ] These epigenetic clocks reflect distinctive characteristics and mechanism of biological aging, [ 54 ] which may explain the inconsistencies in our results.

Vitamin A (retinol) is also a classic dietary antioxidant. Observational studies have found contradictory results about the association of vitamin A with epigenetic age. Grootswagers et al found that high intake of vitamin A was related with PhenoAge acceleration in postmenopausal women. [ 55 ] Ma et al found that intake of vitamin A was negatively associated with PhenoAge in 4692 participants over age 20. [ 56 ] However, the present MR study found no significant association of dietary vitamin A with 4 measures of epigenetic age. The inconsistency could be attributed to the limitations of traditional observational study, such as sample representativeness, residual confounding and reverse causation. The level of MR analyses-based evidence is superior to that based on observational study. The lack of consensus indicates the necessity of further exploration in this field.

Vitamin E is another classic dietary antioxidant. So far, there is no observational study assessing the relationship between vitamin E and epigenetic age. There are some studies explore the association of vitamin E with other aging markers. Observational studies found that lower vitamin E intake was associated with shorter leukocyte telomere length in patients with cardiovascular diseases. [ 57 ] Basic experiments found that vitamin E might ameliorate aging-related diseases and gene expression in aging mice. [ 27 , 58 ] These observational and pre-clinical studies indicate a possible role vitamin E in the progression of aging, but its effect on human epigenetic age is undefined. This is the first MR study to explore the causal association between vitamin E and epigenetic clocks. Our MR study did not find significant association of dietary vitamin E with 4 epigenetic age measures. Further studies are needed to explore the effect of vitamin E on epigenetic age.

Carotene is also a kind of dietary antioxidant. There are few studies about the associations of carotene with epigenetic age. A prospective cohort study found that decreased serum beta-carotene was a risk factor for elevated all-cause mortality in older men independent of inflammation and other risk factors. [ 59 ] A basic experiment demonstrated that β-carotene could ameliorate the aging of mesenchymal stem cells induced by H 2 O 2 , and inhibiting the aging process of tissues and organs in aged mice. [ 28 ] An observational study by Chen et al found that individuals with high supplement of carotene presented decreased PhenoAge. [ 60 ] Another observational study found that high dietary intake of beta-carotene was related with decelerated PhenoAge in postmenopausal women. [ 55 ] However, our MR study found no significant association of dietary carotene with 4 measures of epigenetic age. The lack of consensus calls for further exploration on the role of carotene in epigenetic age.

The present study shows light on developing a vitamin C-based therapeutic strategy in aging-related diseases. Recently, studies propose that biological aging may be modifiable via modulating aging-related epigenomic changes, providing a prospective avenue for preventing aging-related disorders. [ 61 , 62 ] A nonrandomized intervention trial by Fahy et al shows that biological aging detected by epigenetic age measures can be reversed using a combination therapy of metformin, dehydroepiandrosterone and human growth hormone. [ 63 ] Besides, clinical studies have found that caloric restriction, a healthy diet and physical exercise can alleviate the pace of aging in human. [ 6 ] Our study adds new evidence to the anti-aging strategy from the aspect of dietary antioxidants.

There are some advantages in our study. This is the first MR study to evaluate the causal relationships between the dietary antioxidants and epigenetic age, offering causal evidence robust to confounding factors and reverse causality due to the use of IVs (genetic variants). The evidence obtained is superior to that in observational studies. In addition, sensitivity analyses based on different methods were implemented to verify the robustness of our results. However, there are also some disadvantages in our study. Firstly, the summary data of exposures and outcomes was from GWAS conducted in European population, which limits the generalizability of the findings to other populations. Furthermore, the sample size of GWAS studies about epigenetic age is relatively small, the effect estimate may be underpowered for definitive conclusions. Therefore, the association between dietary antioxidants and epigenetic age is still needed to be further explored using GWAS with big sample size.


## 5. Conclusion

In this study, we used MR analyses for the first time to evaluate the causal associations between dietary antioxidants and epigenetic age, and found that genetically predicted dietary vitamin C was associated with decreased epigenetic age measured by HannumAge, indicating the potential of delaying the progression of aging through dietary vitamin C intake. Besides, dietary vitamin C was marginally associated with decreased GrimAge. However, dietary vitamin A, vitamin E and carotene were not causally related to epigenetic age. From a public health perspective, this study provides important genetic evidence about the causality between dietary vitamin C and epigenetic age, which shows light on developing a vitamin C-based therapeutic strategy in EAA-related diseases. Nevertheless, epigenetic clocks, as novel biomarkers of biological age developed in recent years, have become a popular research field, there are also a number of challenges. Besides, there is no consensus about the effect of different dietary antioxidants on epigenetic aging markers. Therefore, further studies, such as randomized controlled trials or MR study with big sample size, are needed to assess the effect of dietary antioxidants on aging and aging-related diseases, and explore related mechanisms.

The authors thank all the participants and investigators of the FinnGen study for the GWAS summary statistics provided by FinnGen. The authors wish to acknowledge the participants and investigators contributing to the summary statistics data for epigenetic age.

Conceptualization: Gaofeng Zeng, Yang Liu.

Data curation: Chunlan Huang, Jingsong Chen, Bo Wang.

Formal analysis: Chunlan Huang, Jingsong Chen, Shao Ouyang, Qilin Ou.

Funding acquisition: Chunlan Huang, Gaofeng Zeng, Kebin Zhan.

Investigation: Chunlan Huang, Qilin Ou, Bo Wang.

Methodology: Chunlan Huang, Kebin Zhan, Shao Ouyang, Yang Liu.

Project administration: Bo Wang, Yang Liu.

Resources: Jingsong Chen.

Software: Jingsong Chen.

Supervision: Gaofeng Zeng, Kebin Zhan, Yang Liu.

Validation: Chunlan Huang, Gaofeng Zeng, Kebin Zhan, Jingsong Chen, Shao Ouyang, Qilin Ou, Bo Wang, Yang Liu.

Visualization: Qilin Ou.

Writing – original draft: Chunlan Huang, Yang Liu.

Writing – review & editing: Gaofeng Zeng, Kebin Zhan, Shao Ouyang, Yang Liu.

Abbreviations: EAA epigenetic age acceleration GWAS genome-wide association study IEAA intrinsic epigenetic age acceleration IV instrumental variable IVW inverse variance weighted MAF minor allele frequency MR Mendelian randomization MR-PRESSO Mendelian randomization pleiotropy residual sum and outlier SE standard error SNP single nucleotide polymorphism

epigenetic age acceleration

genome-wide association study

intrinsic epigenetic age acceleration

instrumental variable

inverse variance weighted

minor allele frequency

Mendelian randomization

Mendelian randomization pleiotropy residual sum and outlier

single nucleotide polymorphism

We acknowledge the support from the Scientific Research Project of Hunan Provincial Health Commission (grant B202303078230 to CH), Natural Science Foundation of Hunan Province (grant 2023JJ60048 to GZ), University of South China Clinical Research 4310 Program (grant 20224310NHYCG08 to KZ) and Clinical Research Center For Prevention and Treatment of Cognitive Impairment In Hunan Province (grant 2023SK4050 to KZ).

This study was based on publicly available database. Related studies and data had been approved by their relevant ethical review board and participants.

The authors have no conflicts of interest to disclose.

The datasets generated during and/or analyzed during the current study are publicly available.

Supplemental Digital Content is available for this article.

How to cite this article: Huang C, Zeng G, Zhan K, Chen J, Ouyang S, Ou Q, Wang B, Liu Y. Causal effects of dietary antioxidants on epigenetic age: A two-sample Mendelian randomization study. Medicine 2025;104:44(e45519).


## Contributor Information

Chunlan Huang, Email: [EMAIL_REDACTED].

Gaofeng Zeng, Email: [EMAIL_REDACTED].

Kebin Zhan, Email: [EMAIL_REDACTED].

Jingsong Chen, Email: [EMAIL_REDACTED].

Shao Ouyang, Email: [EMAIL_REDACTED].

Qilin Ou, Email: [EMAIL_REDACTED].

Bo Wang, Email: [EMAIL_REDACTED].


## Associated Data


## Supplementary Materials