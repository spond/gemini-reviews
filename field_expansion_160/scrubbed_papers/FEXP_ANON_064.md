# FEXP_ANON_064

## Abstract

Arthropathy was related to macronutrients in an increasing number of studies nowadays. However, the causal effect of macronutrients and micronutrients on them remains unknown. The macronutrient and micronutrient summary statistics from the greatest genome-wide meta-analysis produced by the DietGen and other cohorts and genome-wide association studies statistics of arthropathy from FinnGen were used in this two-sample bidirectional Mendelian randomization investigation. The causal relationship between macronutrients and arthropathy was investigated using inverse variance weighting (IVW), Mendelian randomization (MR)-Egger regression, weighted median, weighted model, and simple mode. IVW estimates suggested that carbohydrates, Iron, Vitamin A, and gamma-tocopherol had casual associations with arthropathy. As for gonarthrosis, the IVW estimate of the carbohydrate (OR: 2.11, 95% CI: 1.20–3.73, P IVW = 9.70E−3); as for adhesive capsulitis of shoulder, the IVW estimate of Iron (OR: 1.29, 95% CI: 1.16–1.43, P IVW = 2.80E−6); as for rheumatoid arthritis, the IVW estimate of Iron (OR: 1.17, 95% CI: 1.06–1.30, P IVW = 3.00E−3); as for Coxarthrosis, the IVW estimate of Vitamin A (OR: 0.95, 95% CI: 0.94–0.97, P IVW = 2.70E−8); as for adhesive capsulitis of shoulder, the IVW estimate of gamma-tocopherol (OR: 0.36, 95% CI: 0.29–0.44, P IVW = 3.50E−21); in the reserve MR analysis, as for carbohydrate, the IVW estimate of juvenile arthritis (OR: 0.99, 95% CI: 0.99–1.00, P IVW = 4.50E−3); as for protein, the IVW estimate of juvenile arthtitis (OR: 1.01, 95% CI: 1.00–1.01, P IVW = 2.40E−3). As risk factors, this MR investigation discovered that in macronutrients, carbohydrates were causally linked to gonarthrosis and juvenile arthritis. Protein was related to juvenile arthritis. Iron was obviously associated with adhesive capsulitis of the shoulder and rheumatoid arthritis. Vitamin A was related to Coxarthrosis. Gamma-tocopherol related to adhesive capsulitis of the shoulder and gout. To fully understand how they affect arthropathy, more research is required.


## 1. Introduction

Arthropathy is a common health problem worldwide. According to recent estimates, >300 million people worldwide are affected by osteoarthritis (OA) alone, which is the most common type of arthropathy. [ 1 ] Arthropathy refers to a group of disorders that affect the joint, including inflammatory joint diseases (e.g., gout, rheumatoid arthritis) and noninflammatory joint diseases (e.g., OA). including as well as other conditions (e.g., genetic predisposition, injury, infection, and autoimmune dysfunction) that cause joint pain, inflammation, and limited mobility. [ 2 ] The clinical manifestations and development of arthropathy are closely related to diet. A randomized controlled trial showed that dietary interventions in obese patients with OA could relieve and improve pain. [ 3 ] However, targeted dietary regulation and potential drug development for patients with different subtypes of arthritis require an in-depth understanding of the association between nutrients and arthropathy. However, the network of relationships between multiple nutrients (including macronutrients and micronutrients) and multiple subtypes of arthropathy is still lacking.

Diets with high carbohydrates, such as sugars and refined grains, may contribute to the development of joint diseases. Simple carbohydrates can cause inflammation in the body, contributing to joint pain and stiffness. [ 4 ] At the same time, obesity caused by a high-carbohydrate diet can increase the stress joint load and increase the risk of gonarthrosis . [ 5 ] Complex carbohydrates, on the other hand, provide critical nutrients and fiber that support joint health. Several studies have indicated a correlation between sugar intake and the risk of developing arthropathy. For instance, the administration of bromopyruvic acid, which inhibits glycolysis in vivo, was found to significantly reduce the severity of arthritis in a mouse model. [ 6 ]

Iron homeostasis is significantly important for cartilage tissue. Excess iron might promote the production of reactive oxygen species, and damage cartilage tissue, leading to the occurrence of OA. [ 7 ] A mouse model of iron overload demonstrated that biochanin A regulates iron level and NRF2/Systemzx-/GPZ axis to prevent iron overload associated OA. [ 8 ] Another research found JNK-JUN-NCOA4 axis contributed to chondrocyte ferroptosis and aggravates OA via ferritinophagy. [ 9 ] Too much vitamin A can lead to inflammation of bone cells. Experiments with bone marrow macrophages in mice have shown that excessive vitamin A or retinoid could increase the number of periosteal osteoclasts and decrease the number of endodermal osteoclasts, which could decrease bone mass and increase the risk of OA. [ 10 ] Alpha and gamma-tocopherol had the potential of anti-arthritis as extracts of Alternanthera bettzickiana . [ 11 ] One study has linked gamma-tocopherol to vitamin deficiency. [ 12 ] This association between nutrients hints at the need to build a nutrient-disease network.

Mendelian randomization (MR) is a statistical technique that uses genetic variants as instrumental variables (IV) to estimate the causal effect of exposure on an outcome. [ 12 ]

Currently, the causal relationship between nutrients and joint disease remains uncertain, particularly when nutrients are categorized into macronutrients and micronutrients and analyzed through MR. Therefore, we conducted an MR analysis that validated previous findings and established a network of meaningful causal correlations between nutrients and arthropathies. The results will offer a global perspective for dietary adjustments and drug development for joint patients.


## 2. Materials and methods


## 2.1. Data sources

The largest dietary intake genome-wide association studies (GWAS) of relative diet-composition phenotypes including carbohydrate, fat, protein, and sugar were performed in European-ancestry individuals, including 268,922 for relative intake of fat, carbohydrate, and protein and 235,391 for relative sugar intake. [ 13 ] In this study, >235,000 people had their genotyping from over 14 population cohorts including Lifelines, The Rotterdam Study I/II/III, Avon Longitudinal Study of Parents and Children, Fenland, Framingham Heart Study, Health and Retirement Study, GARNET, HIPFX, Women’s Health Initiative memory Study+, the international consortia European Prospective Investigation into Cancer and Nutrition-InterAct and DietGen. The study was divided into 2 categories: macronutrients and micronutrients. 4 categories of macronutrients were examined in this study: fat, carbohydrate, protein, and sugar. Meanwhile, ten categories of macronutrients were examined in this study: folate, iron, magnesium, vitamin A, vitamin D, vitamin B6, vitamin B12, vitamin C, alpha-tocopherol, gamma-tocopherol. As a result, all of them were used for analysis in the current study. Aggregated GWAS of arthropathies was performed, analyzing summary data from GWAS meta-analysis available in FinnGen. [ 14 ] Detailed in Table S1, Supplemental Digital Content, https://links.lww.com/MD/O626 , our study included 121,176 cases and 221,323 controls of European ancestry.


## 2.2. Instrumental variable

To choose IVs, this study used the following selection criteria. (1) The reference panel used in this study to determine the linkage disequilibrium of the single nucleotide polymorphism (SNPs) was the European sample data from the 1000 Genomes Project. (2) If SNPs linked with each macronutrient met the locus-wide significance level ( P < 5 × 10 −8 ), they would be chosen as possible IVs; If SNPs linked with each micronutrient met the locus-wide significance level ( P < 5 × 10 −6 ), they would be chosen as possible IVs. Additionally, the SNPs with the lowest P -value were selected from among those with R 2 = 0.001 (using a clumping window size of 10,000 kb). (3) Try to infer positive strand alleles, using allele frequencies for palindromes (default, conservative). Our approach involved assuming that all alleles were coded on the forward strand and disregarding any attempts to flip alleles. Additionally, we excluded any palindromic SNPs for which the direction could not be determined. (4) Horizontal pleiotropy is an important factor that deviates from the exclusion restriction assumption in MR studies. It occurs when a genetic variant affects other traits that independently influence the outcome, unrelated to the hypothesized exposure. In this study, methods such as MR-Egger and MR-the pleiotropic residual sum and outlier test (MR-PRESSO) were developed to address the influence of horizontal pleiotropy. The MR-PRESSO global test was used to detect horizontal pleiotropy, while the MR-PRESSO outlier test was used to calculate the pleiotropic and significant P -value for each SNP to exclude the influence of horizontal pleiotropy.


## 2.3. Statistical analysis

In this study, several MR techniques were employed, such as the weighted model, inverse variance weighting (IVW), simple mode, MR-Egger regression, and weighted median, to investigate the causal association between nutrients and arthropathies. We conducted sensitivity analyses to identify potential pleiotropy bias.

The IVW technique, which combines Wald ratios in the fixed-effect meta-analysis, assigns weights to each ratio based on the inverse variance of the SNP-outcome correlation. Fixed effect meta-analysis assumes that differences in estimates from different studies are solely due to sampling variation. This means that if there is no horizontal pleiotropy in the context of MR, using the IVW technique with legitimate IVs would produce the most accurate results for causal estimates, which enables us to quantify the overall impact of nutrients on arthropathies. [ 15 ]

To assess the potential for horizontal pleiotropy, the MR-Egger regression was also performed. Pleiotropy can render any SNP invalid as long as it conforms to the instrument strength independent of direct effect assumption. When an MR-Egger regression’s intercept is not null, pleiotropy can be inferred. [ 16 ] Additionally, the MR-Egger regression’s outcome agrees with IVW. [ 17 ]

In addition, the MR-PRESSO test was used to investigate pleiotropy. This test is designed to identify and account for horizontal pleiotropy, as well as assess any significant differences in causal effects before and after outlier removal. [ 18 ]

A reverse MR analysis on the nutrients was conducted, which was found to have a causal relationship with arthropathies in the forward MR analysis. We aim to investigate whether there is a causal relationship between nutrients and arthropathies. We applied the P -value threshold ( P < 5 × 10 −8 ) in this step and the consistent methods with those of forward MR.

We calculated the F-statistic for each effective SNP using the algorithm to determine the strength of the IVs [ 19 ] :

It was assumed that a weak instrumental bias was not present if the F-statistic value was >10.

All analyses were carried out using packages from the Two samples MR (version 0.5.6), and MR-PRESSO (version 1.0) in R version 4.2.1. (R Foundation for Statistical Computing, Vienna, Austria).


## 3. Result


## 3.1. Selection of IVs

All IVs used for forward and reverse MR analysis after screening are shown in Table S2, Supplemental Digital Content, https://links.lww.com/MD/O627 and Table S7, Supplemental Digital Content, https://links.lww.com/MD/O658 . First off, at the suggestive significance threshold P < 5.0 × 10 –8 , we respectively found 515, 264, 265, and 317 SNPs linked to macronutrients at the carbohydrate, fat, protein, and sugar levels. A total of 27 IVs were identified as being linked with arthropathies following clumping and harmonization, as shown in Table S2, Supplemental Digital Content, https://links.lww.com/MD/O627 . Among 10 IVs in carbohydrates, there were 10 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis and gonarthrosis, respectively. Among 5 IVs in fat, there were 5 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, respectively. Among 6 IVs in protein, there were 6 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, respectively. Among 9 IVs in sugar, there were 9 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, respectively.

Under the significance threshold P < 5.0 × 10 –6 , we found 96, 128, 208, 96, 192, 208, 240, 80, 160, and 112 SNPs associated with micronutrient levels of folate, iron, magnesium, vitamin A, vitamin B6, vitamin B12, vitamin D, alpha-tocopherol, vitamin C, and gamma-tocopherol. A total of 95 IVs were identified as being linked with arthropathies following clumping and harmonization, as shown in Table S2, Supplemental Digital Content, https://links.lww.com/MD/O627 . Among 6 IVs in folate, there were 6 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis. Among 8 IVs in Iron, there were 8 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, Among 13 IVs in Magnesium, there were 13 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, Among 6 IVs in vitamin A, there were 6 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, Among 12 IVs in vitamin B6 there were 12 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, Among 13 IVs in vitamin B12, there were 13 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, Among 15 IVs in vitamin D, there were 15 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, Among 5 IVs in Alpha-tocopherol, there were 5 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, Among 10 IVs in vitamin C, there were 10 SNPs for adhes Among 7 IVs in Gamma-tocopherol, there were 7 SNPs for adhesive capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis, capsulitis of shoulder, arthropathies, coxarthrosis, and gonarthrosis.

At each macronutrient and micronutrient, the horizontal pleiotropy effect has been shown in Table S3, Supplemental Digital Content, https://links.lww.com/MD/O628 . By removing SNPs identified through the MR-PRESSO outlier test and the MR-Egger regression, we ensured that the remaining IVs did not exhibit any indications of horizontal pleiotropy (both MR-PRESSO Global test P > .05 and MR-Egger regression P > .05).


## 3.2. Associations of nutrients and arthropathy

The workflow of the MR analyses conducted is succinctly depicted in Figures 1 and 2 . In order to improve the significance of the results, when studying the causal relationship between nutrients and joint disease, we adjusted the P value of IVW (multiplicative random effects model) by category on the basis of < .05, p'< P/4 = .0125 in macronutrients and p"< p/10 = .005 in micronutrients, and obtained a more significant causal relationship result.


> **Figure 1.:** The working flow chart of this Bidirectional Two-sample Mendelian Randomization Study to explore the causal relationship between macronutrient and arthritis.


> **Figure 2.:** The working flow chart of this Bidirectional Two-sample Mendelian Randomization Study to explore the causal relationship between micronutrients and arthritis.

As shown in Figure 3 , as for gonarthrosis, the IVW estimate of the carbohydrate (OR: 2.11, 95% CI: 1.20–3.73, P IVW = 9.70E−3); as for adhesive capsulitis of shoulder, the IVW estimate of Iron (OR: 1.29, 95% CI: 1.16–1.43, P IVW = 2.80E−6); as for rheumatoid arthritis, the IVW estimate of Iron (OR: 1.17, 95% CI: 1.06–1.30, P IVW = 3.00E−3); as for Coxarthrosis, the IVW estimate of Vitamin A (OR: 0.95, 95% CI: 0.94–0.97, P IVW = 2.70E−8); as for adhesive capsulitis of shoulder, the IVW estimate of gamma-tocopherol (OR: 0.36, 95% CI: 0.29–0.44, P IVW = 3.50E−21).


> **Figure 3.:** The forest plot showing MR results, which explores the causal effect of nutrients and arthritis.

As shown in Table S4, Supplemental Digital Content, https://links.lww.com/MD/O654 https://links.lww.com/MD/O655 , 5 MR approaches are used to investigate the causal relationship between each pair of nutrients and arthropathies during the discovery stage. In at least one MR approach, it was discovered that 1 macronutrient and 3 micronutrients were connected to arthropathies, as shown in Table 1 . The results of the IVW test and MR-egger showed no significant heterogeneity in these IVs. Besides, the MR Egger intercept and MR-PRESSO global test were utilized to test for horizontal pleiotropy, and all P -values were >.05, indicating no significant directional horizontal pleiotropy, as shown in Table 2 and Table S3, Supplemental Digital Content, https://links.lww.com/MD/O628 . The complete results of sensitivity analysis are shown in Table S6a, Supplemental Digital Content, https://links.lww.com/MD/O657 .


### Table 1: Full positive results of MR estimate for the association between nutrients and joint diseases.

| Nutrients (exposure) | Joint diseases (outcome) | MR method | No. SNP | F | OR (95% CI) | P -value |
| Carbohydrate | Gonarthrosis | IVW (MRE) | 10 | 31.95 | 2.11 (1.20–3.73) | 9.70E−03 |
| MR Egger | 10 |  | 13.32 (0.41–434) | .18 |
| Weighted median | 10 |  | 2.48 (1.49–4.12) | 4.40E−04 |
| Simple mode | 10 |  | 3.48 (1.35–9.01) | 3.00E−02 |
| Weighted mode | 10 |  | 3.26 (1.00–10.67) | .08 |
| Iron | Adhesive capsulitis of shoulder | IVW (MRE) | 8 | 20.88 | 1.29 (1.16–1.43) | 2.80E−06 |
| MR Egger | 8 |  | 1.49 (0.89–2.50) | .18 |
| Weighted median | 8 |  | 1.17 (0.89–1.53) | .26 |
| Simple mode | 8 |  | 1.23 (0.81–1.87) | .36 |
| Weighted mode | 8 |  | 1.17 (0.86–1.60) | .35 |
| Iron | Rheumatoid arthritis | IVW (MRE) | 8 | 20.88 | 1.17 (1.06–1.30) | 3.00E−03 |
| MR Egger | 8 |  | 1.23 (0.87–1.76) | .29 |
| Weighted median | 8 |  | 1.18 (0.98–1.42) | .08 |
| Simple mode | 8 |  | 1.24 (0.93–1.64) | .18 |
| Weighted mode | 8 |  | 1.20 (0.98–1.47) | .12 |
| Retinol (Vitamin A) levels | Coxarthrosis | IVW (MRE) | 6 | 21.1 | 0.95 (0.94–0.97) | 2.70E−08 |
| MR Egger | 6 |  | 0.93 (0.78–1.10) | .42 |
| Weighted median | 6 |  | 0.95 (0.89–1.02) | .17 |
| Simple mode | 6 |  | 0.94 (0.85–1.04) | .31 |
| Weighted mode | 6 |  | 0.95 (0.86–1.05) | .38 |
| Gamma-tocopherol levels | Adhesive capsulitis of shoulder | IVW (MRE) | 7 | 21.35 | 0.36 (0.29–0.44) | 3.50E−21 |
| MR Egger | 7 |  | 0.50 (0.03–9.19) | .66 |
| Weighted median | 7 |  | 0.35 (0.16–0.78) | 1.10E−02 |
| Simple mode | 7 |  | 0.30 (0.11–0.85) | .06 |
| Weighted mode | 7 |  | 0.33 (0.11–1.02) | .1 |

### Table 2: Sensitivity analyses for association between nutrients and joint diseases.

| Nutrients (exposure) | Joint diseases (outcome) | No. SNP | Pleiotropy | Heterogeneity |
| MR-PRESSO Global P -value | MR-egger P -value | IVW test P -value | MR-egger P -value |
| Carbohydrate | Gonarthrosis | 10 | .9284 | .324940513 | 5.13E−05 | .00013532 |
| Iron | Adhesive capsulitis of shoulder | 8 | .9537 | .561917783 | .97517187 | .97115181 |
| Iron | Rheumatoid arthritis | 8 | .8615 | .766758909 | .82717783 | .74675676 |
| Retinol (Vitamin A) levels | Coxarthrosis | 6 | .9967 | .742601781 | .99506811 | .99073403 |
| Gamma-tocopherol levels | Adhesive capsulitis of shoulder | 7 | .9956 | .823047799 | .99493654 | .98691165 |

## 3.3. Influence of arthropathy on nutrients

As shown in Figure 4 , as for carbohydrate, the IVW estimate of juvenile arthritis (OR: 0.99, 95% CI: 0.99–1.00, P IVW = 4.50E−3); as for protein, the IVW estimate of juvenile arthritis (OR: 1.01, 95% CI: 1.00–1.01, P IVW = 2.40E−3). The results estimated by other supplementary MR methods were shown in Table 3 . The complete results of MR estimates for the causal association between joint diseases and nutrients are shown in Table S9, Supplemental Digital Content, https://links.lww.com/MD/O660 . Furthermore, the conducted sensitivity analysis (Table 4 and Table S8, Supplemental Digital Content, https://links.lww.com/MD/O659 ) suggested that any potential horizontal pleiotropy was improbable to distort the established causal relationship between the aforementioned factors. The complete results of sensitivity analysis are shown in Table S6b, Supplemental Digital Content, https://links.lww.com/MD/O657 .


### Table 3: Full positive results of MR estimate for the association between joint diseases and nutrients.

| Joint diseases (exposure) | Nutrients (outcome) | MR method | No. SNP | F | OR (95% CI) | P -value |
| Juvenile arthritis | Carbohydrate | IVW (MRE) | 23 | 33.48 | 0.99 (0.99–1.00) | 4.50E−03 |
| MR Egger | 23 |  | 1.00 (0.98–1.01) | .66 |
| Weighted median | 23 |  | 0.99 (0.98–1.00) | .09 |
| Simple mode | 23 |  | 1.00 (0.98–1.01) | .73 |
| Weighted mode | 23 |  | 0.99 (0.98–1.01) | .35 |
| Juvenile arthritis | Protein | IVW (MRE) | 23 | 33.48 | 1.01 (1.00–1.01) | 2.40E−03 |
| MR Egger | 23 |  | 1.01 (0.99–1.02) | .35 |
| Weighted median | 23 |  | 1.01 (1.00–1.02) | .07 |
| Simple mode | 23 |  | 1.01 (0.99–1.02) | .23 |
| Weighted mode | 23 |  | 1.01 (0.99–1.02) | .26 |

### Table 4: Sensitivity analyses for association between joint diseases and nutrients.

| Joint diseases (exposure) | Nutrients (outcome) | No. SNP | Pleiotropy | Heterogeneity |
| MR-PRESSO Global P -value | MR-egger P -value | IVW test P -value | MR-egger P -value |
| Juvenile arthritis | Carbohydrate | 23 | .625 | .487058806 | .60948686 | .58023894 |
| Juvenile arthritis | Protein | 23 | .8005 | .90132498 | .79179627 | .74350015 |

> **Figure 4.:** The forest plot showing reserve MR results, which explores the causal effect of nutrients and arthritis. MR = Mendelian randomization.


## 3.4. Sensitivity analyses

All the MR methods produced consistent estimates of the causal effect direction, indicating a stronger likelihood of a genuine association. To identify any potential outlier variants that may affect exposure but not the outcome, we generated a scatter plot of the relevant statistics for the causal association. [ 20 ]

We found significant heterogeneity tested by both the IVW test and the MR-egger test in all results. Thus, a random effect model was employed in MR analysis. The IVs’ F-statistics ranged from 30.32 to 121.77, and as all of them are bigger than 10, the bias of weak IVs is eliminated. In addition, the findings of the MR-Egger regression intercept analysis indicated that there was no directional horizontal pleiotropy.


## 3.5. Reverse MR analysis

As shown in Table S5, Supplemental Digital Content, https://links.lww.com/MD/O656 , no positive causality was found in the associations identified by the reverse MR analysis.


## 4. Discussion

In the current study, We used the largest GWAS meta-analysis of the macronutrients performed by DietGen and other cohorts, and GWAS meta-analysis for arthropathies to assessed the possible causation between the nutrients and arthropathies, which was able to identify carbohydrates, sugar, iron, vitamin A, and gamma-tocopherol that were causally associated with arthropathies.

As shown in Figure 5 , nutritional interventions provide some health benefits in arthropathies through mechanisms such as weight loss, reduced inflammation, and antioxidant capacity. [ 21 ] However, due to limited data and mixed results, high-quality evidence, including MR and clinical trials, is needed to determine the efficacy of nutritional supplements in preventing or managing arthropathies. [ 22 ] Various nutrient compositions have different effects on arthropathies. Both glucosamine sulfate and chondroitin sulfate are components of the extracellular matrix of cartilage cells. [ 23 ] When OA, joint degeneration, or cartilage wear occurs, supplementation of glucosamine sulfate and chondroitin sulfate is required, which can provide necessary nutrition to damaged cartilage and aid in repair. [ 24 ] However, consumption of fructose and the prevalence of hyperuricemia are associated with an increased risk of gout. [ 25 ] In addition, an animal study demonstrated that the carbohydrate makeup of the rodents’ low-fat control diet might also increase the risk of developing OA. [ 26 ] Modifying the sucrose and fiber content in the diet affected the pathology of OA in rodents; additionally, the high-sucrose diet heightened indications of joint inflammation, whereas the high-fiber diet induced modifications in cartilage genes and cellular stress-response pathways. [ 26 ] Thus, Griffin study was in accordance with the results that carbohydrates were the risk factor for arthropathies. Nevertheless, further research is of significance to prove this conclusion through epidemiological trials. We did not find any causal experiments linking macronutrients and adhesive capsulitis of the shoulder, possibly due to a limited number of cases, resulting in poor statistical power. [ 16 ]


> **Figure 5.:** (A) Iron aggravated OA through the JNK/JUN/NCOA4 axis; (B) BCA (biochanin A) regulated arthritis caused by iron overload; (C) glucose sulfate made inflammatory level lower but sucrose made it higher. Figure created with BioRender( https://biorender.com ).

Iron deficiency caused by Iron overload or iron instability can lead to joint disease. Consistent with Susanna Larsson findings, we believed that iron deficiency was associated with the development of rheumatoid arthritis. [ 27 ] Iron deficiency can lead to iron deficiency anemia, which is a risk factor for rheumatoid arthritis. [ 28 ] Excess iron induces degradation of the chondrocyte matrix and decreases the level of aggregates, resulting in cartilage destruction. [ 29 ] Hfe-knockout mouse models showed cartilage degeneration and increased subchondral bone volume under iron overload. [ 30 ] However, iron deficiency anemia and OA could be co-manifested in some groups, which were especially outstanding in the elderly group. The regulatory mechanism is not clear, which may be related to local iron accumulation and systemic anemia.

Multitude of studies have shown that selenium deficiency is associated with impaired cartilage metabolism and joint abnormalities. [ 31 ] Sun rat experiments showed that the lack of selenium would lead to the downregulation of Col2a1 expression and the increase of Mmp-3 expression, which would lead to abnormal cartilage metabolism. [ 32 ] A population-based cross-sectional study showed that the lower the plasma level, the higher the prevalence of OA and in a dose–response relationship. [ 33 ]

Magnesium deficiency has also been shown to be associated with the severity of OA. The results of a statistical study by Coskun showed that a reduction in serum Mg was associated with more severe OA, but not with inflammatory biomarkers. [ 34 ]

Vitamin A is linked to bone and joint health. Vitamin A can enhance the differentiation of osteoblasts and inhibit the absorption of osteoclasts in order to increase bone density and bone strength and prevent OA caused by mechanical stress. [ 35 ] However, studies have shown that excessive vitamin A intake increases the risk of total fractures and hip fractures. [ 36 ] This might lead to the neutralization of the risk of arthritis at different sites. [ 37 ] More detailed subregional studies of the association of vitamin A with OA are needed. gamma-tocopherol has been shown that it could be used clinically in the form of extracts as anti-inflammatory and anti-rheumatoid drugs. [ 38 ] However, alpha-tocopherol and γ-tocopherol were often present in extracts and were thought to have similar effects, but our study has not found a relationship between alpha-tocopherol and arthritis. Experiments in mice have shown that after dietary supplementation of quantitative α and γ tocopherol, the content of α-tocopherol in the blood of mice was almost unchanged while the content of γ-tocopherol was significantly increased. [ 39 ] The significance of the relationship with arthritis may be related to this.

There are discrepancies between gonarthrosis and coxarthrosis with respect to anatomical and biomechanical factors, epigenetics, pathophysiology, prognosis, pain, and nonsurgical treatment recommendations and management. [ 40 ] For example, individuals with coxarthrosis may be less inclined to participate in non-pharmacological treatments as compared to those with gonarthrosis. [ 41 ] Obesity caused by fat is often unrecognized as a strong risk factor for symptomatic or radiographic progression of hip OA, which showed that macronutrients might not take an effective part in coxarthrosis development. [ 40 ]

However, some nutrients that have been associated with arthropathy in past studies were found to be negative. Protein has been confirmed to help release the pain of gonarthrosis, [ 25 ] on the other hand, it is essential for building and repairing tissues, producing enzymes and hormones, and supporting immune function, which indicates the necessity of subgroup analyses of protein according to the origin of protein. For example, the incidence of hyperuricemia is not significantly associated with the total intake of protein, but is significantly positively correlated with the consumption of red meat, shellfish, and seafood protein, and significantly negatively correlated with the intake of legume protein. [ 42 , 43 ] Research on the protein-arthropathy relationship holds true in the research on the fat-arthropathy relationship as well. For instance, daily supplementation of sesame oil in OA rat models could alleviate early joint pain by inhibiting nuclear factor erythroid 2-related factor 2-related muscle oxidative stress, [ 44 ] while there was a correlation between the consumption of saturated fat and an increased risk of developing OA. [ 45 ] Antioxidants and cholesterol-lowering drugs might slow the progression of joint damage caused by fatty acids found in foods such as palm oil and butter. [ 46 ] The heterogeneity of arthropathy hinders the construction of networks. In addition, the regulatory relationship between nutrients is also a potential factor influencing the results.

This study has several advantages. According to body parts, subgroup analyses were conducted for arthropathies because raw data were employed in the analysis. To ascertain the relationship between the nutrients and arthropathies, MR analysis was selected. The most comprehensive GWAS meta-analysis was used, assuring the reliability of the tools used in the MR study. The present study introduced MR-PRESSO and MR-Egger as novel methods to account for the impact of horizontal pleiotropy. [ 47 ] Additionally, we assessed the F-statistics for each effective SNP to evaluate the strength of IVs. This study does have several limitations: first, the heterogeneity of results was significant in our study, although we used a random effect model; second, nutrients are called for dividing into more detailed compositions, and arthropathies also needed to be sub-grouped into detail; lastly, the number of cases in adhesive capsulitis of shoulder was relatively small, which needs to further expand the sample size.


## 5. Conclusion

This MR investigation discovered that carbohydrate, sugar, iron, vitamin A, and gamma-tocopherol were risk factors for arthropathy, therein carbohydrates were related to gonarthrosis and juvenile arthritis, protein was related to juvenile arthritis. Iron and gamma-tocopherol were related to adhesive capsulitis of the shoulder. It will guide clinical applications in arthropathy therapy by administering diet habits.

The consortium’s release of macronutrient phenotypes of the GWAS summary statistics was appreciated by the authors. The authors also wish to thank the authors of the GWAS summary statistics for arthropathies from FinnGen.

Data curation: Wantong Xu.

Formal analysis: Wantong Xu.

Funding acquisition: Xia Chen.

Investigation: Xia Chen.

Methodology: Wantong Xu, Rui Xia, Xia Chen.

Software: Wantong Xu, Dan Peng.

Validation: Wantong Xu, Dan Peng.

Visualization: Dan Peng.

Writing – original draft: Rui Xia.

Writing – review & editing: Rui Xia, Xia Chen.