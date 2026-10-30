# De-Identified Manuscript `ANON_107`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract


### Background

No previous studies have explored metabolites associated with both genetic predispositions to type 2 diabetes (T2DM) and T2DM onset. Therefore, we aimed to explore metabolic profiles using genetic risk to identify pathways for tailored T2DM prevention strategies.


### Methods

This prospective community-based cohort study in Japan included a total of 12,461 participants aged ≥ 20 years. Genetic predictors were genome-wide and pathway-based polygenic risk scores (PRSs). We quantified 43 metabolites using nuclear magnetic resonance spectroscopy. T2DM was defined as a non-fasting glucose level of ≥ 200 mg/dL, glycated hemoglobin level ≥ 6.5%, or self-reported T2DM treatment. A modified Poisson regression model was used to examine the associations of PRSs and metabolites with T2DM incidence. Linear associations were tested using the restricted cubic spline, and mediation analysis was conducted to assess the mediating effect of metabolites on the association between PRSs and T2DM incidence.


### Results

During the 4.3-year median follow-up period, 354 T2DM cases were identified. A higher PRS was associated with incident T2DM (relative risk [RR] 2.09, 95% confidence interval [CI], 1.68–2.60, P < 0.001, 1-standard deviation [SD] increment). The nitrogen compound transport pathway PRS was associated with incident T2DM (RR 1.32, 95% CI 1.03–1.70, P < 0.001, 1-SD increment). Fourteen metabolites like glucose, 2-ketoisocaproic acid, glutamic acid, leucine, 2-aminobutyric acid, 2-hydroxybutyric acid, valine, 3-methyl-2-oxobutyric acid, alanine, 3-hydroxybutyric acid, 3-methyl-2-oxiovaleric acid, formic acid, arginine, and tyrosine were positively associated with the risk of T2DM. Only glycine was inversely associated with the risk of T2DM. Among 43 metabolites, 14 metabolites were positively associated with PRS ( P for linear trend < 0.05). 3-hydroxyisobutyric-acid, 2-Aminobutyric acid, 2-ketoisocaproic acid, 2-hydroxybutyric acid, leucine, glycine, and glucose mediated the association between PRS and incident T2DM.


### Conclusions

Several metabolites were found to mediate the association between PRS and incident T2DM. These findings may contribute to a better understanding of the metabolic pathways involved in genetic susceptibility to T2DM.


### Supplementary Information

The online version contains supplementary material available at [REDACTED_DOI].

Keywords: Type 2 diabetes, Genetic, Metabolomics, Personalized prevention


## Article Highlights

Why did we undertake this study?

We aimed to identify plasma metabolites associated with type 2 diabetes (T2DM) incidence and genetic risk scores (PRS) using a large-scale genomic and cohort approach.

What is the specific question(s) we wanted to answer?

How do PRS and associated metabolites contribute to T2DM incidence, independent of lifestyle factors?

Higher PRS significantly increased T2DM incidence, with metabolites, such as glucose, alanine, and valine, partially mediating this relationship, accounting for 1–7% of the effect. These findings highlight the interplay between genetic predisposition and metabolomic profiles in T2DM risk.

What are the implications of our findings?

PRSs were associated with T2DM incidence, and seven metabolites were found to partially mediate this association. These findings may help elucidate the metabolic pathways underlying genetic susceptibility to T2DM.


### Supplementary Information

The online version contains supplementary material available at [REDACTED_DOI].


## Background

Globally, diabetes has reached epidemic proportions, with 529 million people currently affected. This number is projected to increase to over 1.31 billion by 2050, according to the Global Burden of Disease, Injuries, and Risk Factors Study [ 1 ]. Therefore, preventing diabetes to reduce premature death, complications, and disability is crucial for public health.

Type 2 diabetes (T2DM) results from a combination of genetic predisposition and unhealthy lifestyle [ 2 – 4 ]. Substantial evidence has demonstrated that various lifestyle factors, including obesity, smoking, and physical inactivity, are drivers of T2DM incidence [ 5 – 9 ]. In terms of genetic predisposition, recent large-scale genome-wide association studies (GWASs) have identified many T2DM-related single nucleotide polymorphisms (SNPs) [ 10 – 12 ]. Using SNPs detected in GWASs, the polygenic risk score (PRS) was developed, which predicts new-onset T2DM [ 3 , 4 , 13 – 15 ]. Furthermore, previous studies have shown that PRS was positively associated with T2DM risk incidence, regardless of modifiable lifestyle factors [ 3 , 4 ]. This finding suggests that individuals with high genetic risk may require frequent screening; however, the underlying preventive strategies remain unclear.

Metabolomics, the systematic study of small molecules, offers a powerful approach to identifying metabolic disturbances linked to pathological conditions [ 16 ]. As the downstream product of gene expression, transcripts, protein transporters, and enzyme reactions, metabolites regulate biological processes and play key roles in disease pathogenesis [ 16 ]. Thus, examining the associations between metabolites and T2DM incidence, as well as differences in metabolome based on an individual’s genetic risk, could provide valuable insights. This approach may elucidate disease pathogenesis mechanisms, identify the biomarkers for risk prediction, and guide targeted interventions tailored to an individual’s genetic risk [ 17 , 18 ].

A recent systematic review and meta-analysis identified several amino acids, aromatic amino acids, and carbohydrates as potential contributors to T2DM incidence and its pathology [ 19 ]. However, this meta-analysis revealed considerable heterogeneity across studies. In addition, all but one of the 44 studies included in the analysis involved a small number of participants, ranging from a few hundred to < 5000, with over half conducted in European populations. Thus, this underscores the need for high-quality evidence on metabolites and T2DM incidence from large populations in non-European populations. Moreover, to the best of our knowledge, no studies have explored metabolites associated with both genetic predisposition to T2DM and T2DM onset. Elucidating the association between the genetic risk and metabolites linked to T2DM incidence may provide critical insights for developing prevention strategies for genetically at-risk participants.

To address this knowledge gap, this study aimed to identify plasma metabolites associated with T2DM incidence and examine plasma metabolites linked to genetic risk using the biobank of the Tohoku Medical Megabank community-based cohort study (TMM CommCohort Study), employing a large-scale genomic and cohort approach [ 20 , 21 ].


## Methods


### Ethics statements

The study protocol conformed to the ethical guidelines of the 1975 Declaration of Helsinki and was approved by the Ethics Committee of [AUTHOR], Tohoku University (approval number: 2022-4-047; approval date: June 30, 2022). Written informed consent was obtained from all participants.


### TMM CommCohort study participants

To identify plasma metabolites associated with T2DM incidence and examine plasma metabolites linked to genetic risk, we conducted a prospective cohort study using data from the TMM CommCohort Study [ 20 , 21 ]. The source population for this study comprised men and women aged ≥ 20 years living in the Miyagi prefectures in northeastern Japan. Over 60,000 participants were recruited via three approaches: a type 1 survey (n = 40,433 participants), which was conducted at specific municipal health check-up sites; a type 1 additional survey (n = 664 participants), which was conducted on dates different from those of the health check-up sites; and a type 2 survey (n = 13,855), which was conducted at the assessment center. All participants were recruited between May 2013 and March 2016.

Respondents from the baseline survey were invited to participate in a repeat assessment center-based survey during the second period (follow-up survey) from June 2017 to March 2021. This follow-up survey collected basic information similar to that in the baseline survey [ 22 ].

First, to develop pathway-specific PRS and select PRS associated with the development of T2DM, we used data of the type 2 survey participants (n = 13,855). We excluded participants who withdrew from the study by November 16, 2021 (n = 204), had type 1 diabetes (n = 31), lacked genetic information genotyped via the Affymetrix Axiom Japonica Array (v2) (n = 3,783), lacked information on glucose (n = 16), and had ≥ 6 standard deviations (SDs) from the mean of each genetic principal component (n = 20). Finally, we constructed PRSs and determined hyperparameters using data from 9,801 participants.

Second, to test the association between the PRS and risk of developing T2DM, we initially included participants from the type 1 survey (n = 40,433). We excluded participants who withdrew from the study by November 16, 2021 (n = 770), had a history of cardiovascular disease (n = 1806), had type 1 (n = 126) or T2DM at the baseline survey (n = 3020), lacked genetic information genotyped via the Affymetrix Axiom Japonica Array (v2) (n = 6438), or lacked metabolomics data (n = 497). We subsequently excluded participants with data ≥ 6 SDs from the mean of each genetic principal component (n = 53) and those who did not join the follow-up survey, thus having missing information on glucose and hemoglobin A1c (HbA1c) during the follow-up survey (n = 15,262). Finally, data from 12,461 participants were analyzed.


### Type 2 diabetes

Non-fasting blood glucose and HbA1c levels were measured using the hexokinase and latex agglutination turbidimetry methods, respectively. T2DM was defined as a non-fasting glucose level of ≥ 200 mg/dl, HbA1c ≥ 6.5%, and/or self-reported treatment for T2DM.


### PRS

We used a multi-ancestry GWAS for T2DM by Suzuki et al. [ 12 ], which is based on an independent dataset and does not include participants from the TMM CommCohort Study (Additional File 1 ). Thus, the PRS constructed in our analysis is based on external summary statistics, and there is no overlap between the discovery and target datasets. For quality control, ambiguous SNPs (A/T and G/C) and SNPs that do not present in both GWAS summary statistics and genotype data were excluded [ 12 ]. We calculated the genome-wide PRS using PRSice-2 v2.3.5 and pathway-specific PRS using the PRSet software (included in PRSice-2) on genotype data [ 23 ]. According to a previous study, PRSice-2 uses the standard clumping + thresholding approach to calculate the PRS (with the window size set to 250 Kb on either side of the index SNP and r2 set to 0.1). To calculate PRSs that account for potential confounding factors, we adjusted for age, sex, and the first 10 principal components to account for confounding effects of ancestry.

PRSet performed regio-aware (coordinate set based) SNP clumping (1 Mb to either side of the index SNP) to generate PRSs that corresponded to sets of genes (pathways) and account for linkage disequilibrium across the genes via clumping. A total of 9,270 pathways were defined using 6 publicly available databases (Biocarta, Pathway Interaction Database, Reactome, Mouse Genome Database, Kyoto Encyclopedia of Genes and Genomes, and Genome Ontology). For Mouse Genome Database pathways, we used the human-mouse homolog list provided by the Mouse Genome Database to convert the mouse gene names to their human counterparts and restricted our analyses to pathways with ontology levels > 4 to avoid inclusion of pathways that are extremely specific [ 23 ]. We also removed pathways with < 10 genes to exclude overly specific pathways that would have insufficient power for enrichment testing and pathways with > 2000 genes to exclude broad pathways of limited biological specificity. The major histocompatibility complex region (chr6:25–34 Mb) was removed. We extended the gene coordinates 35 Kb upstream and 10 Kb downstream of each gene to include potential regulatory elements so that SNPs were part of pathways within these window boundaries but not outside. Pathways with competitive P -values < 0.05 were considered as significantly enriched. For more details on the PRSet pipeline, see the study by Choi et al. [ 24 ] All PRSs were standardized to have a mean of 0 and SD of 1.

Because there are so many PRSs, we first constructed each PRS among type 2 participants and determined the optimal P-value threshold. Using Lasso regression analysis, we selected eight pathway-specific PRSs that were significantly associated with T2DM among type 2 survey participants. Then, these selected PRSs were validated among type 1 survey participants.


### Metabolomics

All blood samples were stored at 4 °C at the study site. Most samples were transported within 8 h and frozen at − 80 °C in accordance with the established protocol [ 25 ]. They were then cryopreserved until metabolomic analysis. The detailed procedures for the examination and blood sampling have been previously described [ 26 ]. Forty-three metabolites, including 8 essential and 19 non-essential amino acids, 6 ketone bodies, 6 glycolytic metabolites, and 3 other metabolites, were obtained from blood samples (Additional File 2 ). Nuclear magnetic resonance spectroscopy (NMR) was used to quantify those metabolites [ 27 , 28 ]. The details of the NMR metabolome analysis have been described elsewhere [ 26 , 29 ]. Further information on the metabolites in this cohort is provided elsewhere (jMorp; https://jmorp.megabank.tohoku.ac.jp/ ).


### Other variables

Information on demographic characteristics, smoking status, drinking status, physical activity, treatment for T2DM, history of cardiovascular disease, and diet was collected through a self-reported questionnaire. Education status was classified into four categories: below high school, vocational school or junior college or technical college, university or graduate school, and unknown. Smoking status was classified into three categories: never smokers (those who smoked < 100 cigarettes in their lifetime and were not current smokers), ex-smokers (those who smoked ≥ 100 cigarettes in their lifetime and were not current smokers), and current smokers (those who smoked ≥ 100 cigarettes in their lifetime and were current smokers) [ 30 ]. Drinking status was classified into the following three categories: never drinkers (those who consumed little or no alcohol or were constitutionally incapable of alcohol consumption), ex-drinkers (those who had stopped drinking alcohol), and current drinkers. Dietary information was obtained using a self-reported food frequency questionnaire (FFQ). Through the FFQ, we evaluated the frequency and amount of 130 food items and beverages consumed. Total energy was calculated using the Standard Tables of Food Composition in Japan (Fifth Revised and Enlarged Edition 2005) [ 31 ]. To calculate the minutes of moderate-intensity and vigorous-intensity physical activities per week, participants provided information on hours spent on various activities per day over the past years [ 32 ]. We assigned time values (0, 30, 120, 240, 360, 480, 600, and 660 min) corresponding to the following categories: none, < 1, 1–3, 3–5, 5–7, 7–9, 9–11, and ≥ 11 h, respectively. Information was collected on the frequency (times per week) and duration (minutes per time) of normal walking, brisk walking, moderate-intensity exercises, and high-intensity exercises during leisure time. The frequency was classified as < 1 time per month, 1–3 times per month, 1–2 times per week, 3–4 times per week, 6–8 times per week, and almost every day [ 32 – 34 ]. Duration was classified into the following categories: < 30 min, 30–59 min, 1–2 h, 2–3 h, 3–4 h, and ≥ 4 h. In addition, “walking,” “normal walking,” “brisk walking,” and “moderate-intensity exercise” were classified as moderate physical activity, whereas “strenuous work” and “hard-intensity exercise” were classified as vigorous physical activity [ 32 – 34 ]. The average times of moderate and vigorous physical activities during leisure time were determined by multiplying the frequency by the duration. Subsequently, the minutes of moderate-intensity and vigorous physical activities per week were calculated by adding the duration of walking and the average moderate physical activity time, or the duration of strenuous work and the average time of vigorous physical activity during leisure time, respectively. Regular physical activity was defined as at least 150 min of moderate-intensity physical activity per week or 75 min of vigorous-intensity physical activity per week.

Serum gamma-glutamyl transferase levels were measured using an enzymatic method. Body mass index (BMI) was calculated as weight (kg) divided by the square of height (m). Obesity was defined as BMI ≥ 25.0 kg/m 2 based on the Western Pacific Region of World Health Organization criteria for the Japanese [ 35 ].


### Statistical analysis

To address missing information, we applied random forest imputation using the missForest R package. The characteristics of the participants are described according to genetic risk. Data are presented as means [SD] or median (interquartile range) and number (percentage) for continuous and categorical variables, respectively. Continuous variables were compared between genetic risk groups using the t-test or Kruskal–Wallis test, and categorical variables were compared using the chi-square test.

First, we examined the association between the genetic risk and the risk of developing T2DM using a Poisson regression model with robust variance correction to estimate the relative risk (RR) of T2DM incidence. Second, we examined the association between circulating metabolites and the risk of developing T2DM using the same regression model with robust variance correction. RRs and 95% confidence intervals (95% CIs) are reported per each 1-SD increase. Third, we conducted restricted cubic spline analyses with three knots in the adjusted logistic regression models to examine the association between circulating metabolites and the standardized PRS (per 1-SD increase), which was used as the outcome variable. The linearity of the associations was assessed using each metabolite as a continuous variable. Finally, a mediation analysis was applied to estimate the natural direct effect, natural indirect effect, and proportion-mediated effect via each metabolite on the association between the PRS and T2DM incidence. In this analysis, we used a PRS 1-SD increase as the exposure and each metabolite as a continuous mediator. In all analyses, adjustment was made for age, sex, education status, the top 10 genetic principal components (to adjust for population structure), total energy intake, BMI, smoking status, alcohol consumption, and physical activity [ 4 , 23 ].

We used the Benjamini–Hochberg approach to calculate the false discovery rate at 0.05 to account for multiple testing. Statistical analyses were performed using R software (version 4.1.2; R Foundation for Statistical Computing, Vienna, Austria).


## Results


### Participants’ characteristics

The baseline characteristics of the participants by genetic risks are presented in Table 1 . Among the 12,461 participants (4128 men and 8333 women), the median follow-up time was 4.3 years, and 354 incidences of T2DM occurred. In total, 1294 (10.7%), 6428 (51.6%), 2947 (23.7%), and 5742 (55.8) participants were current smokers, current drinkers, obese, and engaging in regular physical activity, respectively. The mean glucose and HbA1c levels at the baseline survey were 88.5 (12.4) mg/dL and 5.5 (0.3) %, respectively. Both glucose and HbA1c levels at the baseline survey tended to be higher in participants with higher genetic risk than their counterparts. However, smoking status, drinking status, and engagement in regular physical activity did not differ significantly among the genetic risk groups.


#### Table 1.

Characteristics of the study participants



|  | Overall | Low PRS | PRS 1-SD increase | P for difference | Missing rate |
| --- | --- | --- | --- | --- | --- |
| Number | 12 461 | 10 471 | 1990 |  |  |
| Age, y | 59.9 (11.1) | 60.0 (11.0) | 58.9 (11.6) | < 0.001 | 0.0 |
| Women, % | 8333 (66.9) | 6962 (66.5) | 1371 (68.9) | 0.039 | 0.0 |
| Glucose, mg/dL | 88.5 (12.4) | 88.2 (12.3) | 89.8 (12.7) | < 0.001 | 0.1 |
| HbA1c, % | 5.5 (0.3) | 5.5 (0.3) | 5.6 (0.3) | < 0.001 | 0.0 |
| BMI kg/m 2 | 22.9 (3.3) | 22.9 (3.3) | 23.0 (3.3) | 0.446 | 0.0 |
| Total energy intake, kcal/day | 2003.7 (272.4) | 2005.0 (270.3) | 1997.2 (283.4) | 0.245 | 2.3 |
| Smoking status, % |  |  |  | 0.271 | 3.4 |
| Never smoker | 7896 (65.6) | 6629 (65.5) | 1267 (66.1) |  |  |
| Ex-smoker | 2852 (23.8) | 2421 (23.9) | 431 (22.5) |  |  |
| Current smoker | 1294 (10.7) | 1074 (10.6) | 220 (11.5) |  |  |
| Drinking status, % |  |  |  | 0.370 | 2.5 |
| Never drinker | 5466 (45.0) | 4573 (44.8) | 893 (46.1) |  |  |
| Ex-drinker | 260 (2.1) | 218 (2.1) | 42 (2.2) |  |  |
| Current drinker | 6428 (51.6) | 5426 (51.8) | 1002 (50.4) |  |  |
| Family history, % | 1343 (11.4) | 1051 (10.6) | 292 (15.5) | < 0.001 | 5.1 |
| Obesity, % | 2947 (23.7) | 2477 (23.7) | 470 (23.6) | 0.984 | 0.0 |
| Regular physical activity, % | 5742 (55.8) | 4816 (55.8) | 926 (55.9) | 0.998 | 17.4 |
| Education status, % |  |  |  | 0.842 | 2.6 |
| Below high school | 7684 (63.3) | 6466 (63.4) | 1218 (62.9) |  |  |
| Vocational school or junior college or technical college | 2985 (24.6) | 2503 (24.6) | 482 (24.9) |  |  |
| University or graduate school | 1379 (11.4) | 1158 (11.4) | 221 (11.4) |  |  |
| Unknown | 83 (0.7) | 67 (0.7) | 16 (0.8) |  |  |
| Succinic acid | 8.2 (1.7) | 8.2 (1.7) | 8.3 (1.8) | 0.032 | 0.0 |
| Acetone | 6.0 (5.2) | 6.0 (5.2) | 6.0 (5.2) | 0.698 | 0.0 |
| 3-Hydroxyisobutyric acid | 11.5 (3.4) | 11.4 (3.4) | 11.6 (3.5) | 0.015 | 0.0 |
| Formic acid | 11.3 (3.3) | 11.3 (3.3) | 11.2 (3.2) | 0.766 | 0.1 |
| 2-Aminobutyric acid | 16.8 (3.2) | 16.8 (3.2) | 17.0 (3.2) | 0.004 | 0.0 |
| 3-Methyl-2-oxovaleric acid | 19.4 (4.4) | 19.4 (4.4) | 19.6 (4.5) | 0.034 | 0.0 |
| Methionine | 27.1 (4.1) | 27.1 (4.1) | 27.3 (4.0) | 0.018 | 0.0 |
| 2-Ketoisocaproic acid | 25.9 (6.1) | 25.8 (6.0) | 26.2 (6.3) | 0.007 | 0.0 |
| Creatine | 38.8 (13.8) | 38.6 (13.8) | 39.7 (13.9) | 0.003 | 0.0 |
| 2-Hydroxybutyric acid | 36.9 (13.0) | 36.7 (12.8) | 37.9 (14.0) | < 0.001 | 0.0 |
| Acetic acid | 35.3 (10.2) | 35.2 (10.2) | 35.4 (10.5) | 0.601 | 0.2 |
| Tryptophan | 51.8 (9.4) | 51.8 (9.4) | 51.8 (9.3) | 0.847 | 0.0 |
| Carnitine | 37.5 (7.7) | 37.6 (7.7) | 37.3 (7.8) | 0.217 | 0.1 |
| Cysteine | 58.2 (11.1) | 58.2 (11.1) | 58.6 (11.3) | 0.147 | 0.0 |
| Glutamic acid | 52.4 (14.9) | 52.3 (14.9) | 52.7 (14.8) | 0.236 | 0.0 |
| Creatinine | 58.6 (12.3) | 58.6 (12.3) | 58.3 (12.2) | 0.226 | 0.0 |
... (27 rows truncated) ...


BMI body mass index, METs metabolic equivalents, PRS polygenic risk score, HbA1c hemoglobin A1c

Obesity: defined as a BMI > 25.0 kg/m 2 based on the Western Pacific Region of World Health Organization criteria for Japanese individuals

Regular physical activity: defined as meeting the American Heart Association recommendations of at least 150 min of moderate activity per week or 75 min of vigorous activity per week (or an equivalent combination)

Baseline characteristics of participants who were included in the analysis and those who were excluded are presented in Additional File 3 to assess potential selection bias. Participants included in the analysis tended to be older and have lower BMI. They were also less likely to be obese, or current smokers.


### Association of the PRS with T2DM incidence

Eight PRSs were selected because they were significantly associated with T2DM among type 2 participants. Among type 1 survey participants, PRS was associated with a higher risk of developing T2DM (1-SD increment RR 2.09, 95% CI 1.68–2.60). A 1-SD increment in the nitrogen compound transport PRS was positively associated with the risk of developing T2DM (RR 1.32, 95% CI 1.03–1.70). However, the other six pathway-specific PRSs were not associated with the risk of developing T2DM (Additional File 4).


### Association of circulating metabolites with T2DM incidence

Figure 1 presents the circulating metabolites associated with T2DM incidence. Among the 43 circulating metabolites, 14 metabolites including glucose, 2-ketoisocaproic acid, glutamic acid, leucine, 2-aminobutyric acid, 2-hydroxybutyric acid, valine, 3-methyl-2-oxobutyric acid, alanine, 3-hydroxybutyric acid, 3-methyl-2-oxiovaleric acid, formic acid, arginine, and tyrosine were positively associated with the risk of developing T2DM. For example, each 1-SD increase in the glucose level was associated with a 3.67-fold higher risk of T2DM (RR 3.67, 95% CI 2.96–4.54), and 2-ketoisocaproic acid was associated with a 1.70-fold higher risk of T2DM (RR 1.70, 95% CI 1.32–2.17). In contrast, glycine was inversely associated with T2DM risk (RR 0.51, 95% CI 0.32–0.81).


#### Fig. 1.


> **Figure/Table Caption:** Association between circulating metabolites and diabetes incidence. CI confidence interval, RR relative risk. Bold indicates statistical significance. The RR and 95% CI were calculated using the Poisson regression model with robust variance correction. The model was adjusted for age, sex, total energy intake, education status, the top 10 genetic principal components (to adjust for population structure), total energy intake, BMI, smoking status, alcohol consumption, and physical activity


### Association of PRSs and circulating metabolites

Figure 2 shows the restricted cubic splines between the PRS and adjusted odds ratio of circulating metabolites. PRS was linearly and positively associated with 14 metabolites including succinic acid, 3-hydroxyisobutyric acid, 2-aminobutyric acid, 3-methyl-2-oxovaleric acid, methionine, 2-ketoisocaproic acid, creatine, 2-hydroxybutyric acid, cysteine, arginine, ornithine, tyrosine, histidine, leucine, lysine, valine, glutamine, glucose, and 3-methyl-2-oxobutyric acid. Among these, glucose, 2-ketoisocaproic acid, glutamic acid, leucine, 2-aminobutyric acid, 2-hydroxybutyric acid, 3-methyl-2-oxiovaleric acid, arginine, and tyrosine were also positively associated with incident T2DM. The nitrogen compound transport PRS was not statistically associated with all circulation metabolites (Additional File 5).


#### Fig. 2.


> **Figure/Table Caption:** Dose-response associations between PRS and circulating metabolites, fitted using restricted cubic splines. CI confidence interval, OR odds ratio. The OR and 95% CI were calculated using the logistic regression model. The model was adjusted for age, sex, total energy intake, education status, the top 10 genetic principal components (to adjust for population structure), total energy intake, BMI, smoking status, alcohol consumption, and physical activity


### Mediation analysis of circulating metabolites for the association between the PRS and the risk of T2DM

A mediation analysis revealed that the association between the PRS and the risk of developing T2DM was partially mediated by seven metabolites (3-hydroxyisobutyric-acid, 2-aminobutyric acid, 2-ketoisocaproic acid, leucine, glycine, glucose, and 3-methyl-2-oxobutyric acid) (Table 2 ). A 1-SD increase in the PRS increased the RR of T2DM incidence, with the association mediated by metabolites being 1.0–7.0%. For the nitrogen compound transport PRS, no metabolites showed a statistically significant natural direct effect (Table 3 ).


#### Table 2.

Mediation effects of metabolites on the association between the PRS and T2DM incidence



| Metabolite | Natural direct effect | Natural indirect Effect | Proportion mediated |
| --- | --- | --- | --- |
| Succinic acid | 2.07 (1.69–2.50) | 1.01 (0.99–1.02) | − 1.0 (− 0.4–1.0) |
| Acetone | 2.01 (1.59–2.55) | 1.00 (0.99–1.01) | 0.0 (− 3.0–2.0) |
| 3-Hydroxyisobutyric acid | 2.02 (1.58–2.42) | 1.01 (1.00–1.02) | 2.0 (0.0–5.0) |
| Formic acid | 2.04 (1.59–2.46) | 1.00 (0.99–1.01) | 0.0 (− 1.0–2.0) |
| 2-Aminobutyric acid | 2.02 (1.55–2.49) | 1.01 (1.00–1.02) | 2.0 (0.0–5.0) |
| 3-Methyl-2oxovaleric acid | 2.03 (1.63–2.45) | 1.01 (1.00–1.02) | 0.0 (− 1.0–2.0) |
| Methionine | 2.05 (1.67–2.54) | 1.00 (0.99–1.01) | 0.0 (− 2.0–1.0) |
| 2-Ketoisocaproic acid | 2.00 (1.58–2.55) | 1.01 (1.00–1.02) | 3.0 (1.0–6.0) |
| Creatine | 2.04 (1.68–2.53) | 1.00 (0.99–1.01) | 0.0 (− 2.0–2.0) |
| 2-Hydroxybutyric acid | 2.00 (1.63–2.43) | 1.01 (0.99–1.02) | 3.0 (0.0–6.0) |
| Acetic acid | 2.04 (1.59–2.54) | 1.00 (0.99–1.00) | 0.0 (− 4.0–2.0) |
| Tryptophan | 2.05 (1.64–2.57) | 1.00 (0.99–1.00) | 0.0 (− 2.0–1.0) |
| Carnitine | 2.06 (1.66–2.61) | 1.00 (0.99–1.01) | − 1.0 (− 3.0–1.0) |
| Cysteine | 2.05 (1.63–2.58) | 1.01 (0.99–1.01) | − 2.0 (− 6.0–1.0) |
| Glutamic acid | 2.07 (1.56–2.54) | 1.01 (0.99–1.02) | 0.0 (− 1.0–2.0) |
| Creatinine | 2.04 (1.54–2.50) | 1.00 (0.99–1.00) | 0.0 (− 1.0–2.0) |
| Asparagine | 2.04 (1.63–2.44) | 1.00 (0.99–1.00) | 0.0 (− 2.0–1.0) |
| Isoleucine | 2.04 (1.68–2.52) | 1.00 (0.99–1.01) | 0.0 (− 2.0–2.0) |
| Phenylalanine | 2.05 (1.57–2.56) | 1.00 (0.99–1.01) | 0.0 (− 2.0–1.0) |
| Arginine | 2.03 (1.53–2.53) | 1.01 (1.00–1.02) | 1.0 (− 2.0–4.0) |
| Ornithine | 2.04 (1.61–2.48) | 1.01 (0.99–1.01) | 0.0 (− 2.0–2.0) |
| Tyrosine | 2.05 (1.66–2.57) | 1.00 (0.99–1.01) | 0.0 (− 2.0–1.0) |
| Pyruvic acid | 2.06 (1.62–2.56) | 1.00 (0.99–1.01) | − 1.0 (− 4.0–0.0) |
| Glycerol | 2.04 (1.62–2.57) | 1.00 (0.99–1.01) | 0.0 (− 1.0–.0) |
| Histidine | 2.03 (1.58–2.49) | 1.00 (0.99–1.01) | 1.0 (− 2.0–3.0) |
| 3-Hyudroxybutyric acid | 2.04 (1.62–2.56) | 1.00 (0.99–1.00) | 0.0 (− 2.0–1.0) |
| Leucine | 2.01 (1.59–2.47) | 1.01 (1.00–1.02) | 2.0 (0.0–5.0) |
| Serine | 2.05 (1.57–2.59) | 1.00 (0.99–1.00) | 0.0 (− 4.0–1.0) |
| Lysine | 2.07 (1.56–2.62) | 1.01 (1.00–1.02) | − 1.0 (− 5.0–1.0) |
| Threonine | 2.04 (1.62–2.53) | 1.00 (0.99–1.00) | 0.0 (− 3.0–1.0) |
| Proline | 2.04 (1.64–2.50) | 1.00 (0.99–1.00) | 0.0 (− 1.0–1.0) |
| Valine | 2.02 (1.56–2.58) | 1.01 (0.99–1.01) | 1.0 (0.0–4.0) |
| Glycine | 2.02 (1.62–2.56) | 1.01 (1.00–1.03) | 2.7 (0.0–6.8) |
| Alanine | 2.04 (1.61–2.47) | 1.00 (0.99–1.01) | 0.0 (− 1.0–2.0) |
| Glutamine | 2.05 (1.61–2.56) | 1.00 (0.99–1.01) | − 1.0 (− 3.0–1.0) |
| Lactic acid | 2.04 (1.63–2.60) | 1.00 (0.99–1.01) | 0.0 (− 1.0–2.0) |
| Glucose | 1.99 (1.52–2.47) | 1.06 (1.04–1.09) | 7.0 (3.0–15.0) |
| 3-Methyl-2-oxobutyric acid | 2.04 (1.57–2.46) | 1.01 (1.00–1.02) | 1.0 (0.0–4.0) |
| Betaine | 2.04 (1.63–2.53) | 1.00 (0.99–1.00) | 0.0 (− 1.0–1.0) |
... (4 rows truncated) ...


PRS polygenic risk score, T2DM type 2 diabetes

Natural direct effect shows the effect of the PRS not explained by the mediator

Natural indirect effect shows the effect of the PRS through the mediator


#### Table 3.

Effects of metabolites on the association between nitrogen compound transport pathway PRS and T2DM incidence



| Metabolite | Natural direct effect | Natural Indirect Effect | Proportion mediated |
| --- | --- | --- | --- |
| Succinic acid | 1.36 (1.08–1.64) | 1.00 (0.99–1.01) | 0.0 (− 0.4–5.0) |
| Acetone | 1.35 (1.01–1.74) | 1.00 (0.99–1.00) | 0.0 (− 4.0–3.0) |
| 3-Hydroxyisobutyric acid | 1.35 (1.03–1.68) | 1.00 (0.99–1.00) | − 2.0 (− 8.0–4.0) |
| Formic acid | 1.33 (1.05–1.67) | 1.00 (0.99–1.00) | − 2.0 (− 12.0–5.0) |
| 2-Aminobutyric acid | 1.36 (1.06–1.74) | 1.00 (0.99–1.00) | − 2.0 (− 11.0–2.0) |
| 3-Methyl-2-oxovaleric acid | 1.32 (1.00–1.62) | 1.00 (0.99–1.01) | 2.0 (− 6.9–31.0) |
| Methionine | 1.34 (1.03–1.70) | 1.00 (0.99–1.01) | 1.0 (− 2.0–5.0) |
| 2-Ketoisocaproic acid | 1.31 (0.99–1.67) | 1.00 (0.99–1.01) | 2.0 (− 5.0–20.0) |
| Creatine | 1.36 (1.07–1.75) | 1.00 (0.99–1.01) | 0.0 (− 6.0–3.0) |
| 2-Hydroxybutyric acid | 1.36 (1.05–1.73) | 1.00 (0.99–1.01) | 0.0 (− 4.0–4.0) |
| Acetic acid | 1.37 (1.09–1.73) | 1.00 (0.99–1.00) | − 1.0 (− 0.9–3.0) |
| Tryptophan | 1.35 (1.02–1.75) | 1.00 (0.99–1.00) | − 1.0 (− 9.0–6.0) |
| Carnitine | 1.37 (1.05–1.78) | 1.00 (0.99–1.00) | 0.0 (− 5.0–4.0) |
| Cysteine | 1.35 (1.03–1.68) | 1.00 (0.99–1.00) | 0.0 (− 5.0–2.0) |
| Glutamic acid | 1.35 (1.02–1.72) | 1.00 (0.99–1.01) | 1.0 (− 5.0–8.0) |
| Creatinine | 1.36 (1.05–1.73) | 1.00 (0.99–1.00) | 0.0 (− 2.0–3.0) |
| Asparagine | 1.35 (1.00–1.74) | 1.00 (0.99–1.01) | 2.0 (− 2.0–15.5) |
| Isoleucine | 1.35 (1.02–1.69) | 1.00 (0.99–1.00) | 0.0 (− 6.0–5.0) |
| Phenylalanine | 1.36 (1.08–1.72) | 1.00 (0.99–1.00) | 0.0 (− 5.0–4.0) |
| Arginine | 1.34 (1.03–1.71) | 1.00 (0.99–1.01) | 1.0 (− 2.0–11.0) |
| Ornithine | 1.35 (1.06–1.64) | 1.00 (0.99–1.01) | 1.0 (− 3.0–5.0) |
| Tyrosine | 1.37 (1.03–1.72) | 1.00 (0.99–1.00) | 0.0 (− 3.0–5.0) |
| Pyruvic acid | 1.36 (1.05–1.69) | 1.00 (0.99–1.00) | 1.0 (− 3.0–13.0) |
| Glycerol | 1.33 (1.00–1.76) | 1.00 (0.99–1.00) | 1.0 (− 3.0–13.0) |
| Histidine | 1.35 (0.97–1.71) | 1.00 (0.99–1.00) | 0.0 (− 3.0–4.0) |
| 3-Hyudroxybutyric acid | 1.35 (1.06–1.77) | 1.00 (0.99–1.01) | 0.0 (− 3.0–4.0) |
| Leucine | 1.34 (1.02–1.73) | 1.00 (0.99–1.01) | 0.0 (− 11.0–8.0) |
| Serine | 1.36 (1.02–1.74) | 1.00 (0.99–1.01) | 0.0 (− 2.0–60) |
| Lysine | 1.34 (1.03–1.73) | 1.00 (0.99–1.01) | 2.0 (− 6.0–14.0) |
| Threonine | 1.37 (0.99–1.75) | 1.00 (0.99–1.01) | − 2.0 (− 14.0–4.0) |
| Proline | 1.35 (0.99–1.75) | 1.00 (0.99–1.00) | 0.0 (− 4.0–3.0) |
| Valine | 1.36 (1.01–1.75) | 1.00 (0.99–1.00) | − 2.0 (− 10.0–5.0) |
| Glycine | 1.38 (1.08–1.84) | 1.02 (0.99–1.03) | 5.6 (− 7.0–20.0) |
| Alanine | 1.33 (1.01–1.69) | 1.00 (0.99–1.01) | 2.0 (− 8.0–11.0) |
| Glutamine | 1.36 (1.05–1.68) | 1.00 (0.99–1.00) | 1.0 (− 3.0–6.0) |
| Lactic acid | 1.36 (1.04–1.70) | 1.00 (0.99–1.00) | − 1.0 (− 6.03.0) |
| Glucose | 1.24 (0.95–1.53) | 1.02 (0.99–1.03) | 10.0 (− 76.0–55.0) |
| 3-Methyl-2-oxobutyric acid | 1.32 (1.01–1.70) | 1.00 (0.99–1.01) | 2.0 (− 4.0–17.0) |
| Betaine | 1.35 (1.06–1.67) | 1.00 (0.99–1.01) | 0.0 (− 3.0–8.0) |
... (4 rows truncated) ...


PRS polygenic risk score, T2DM type 2 diabetes

Natural direct effect shows the effect of the PRS not explained by the mediator

Natural indirect effect shows the effect of the PRS through the mediator


## Discussion

This large, community-based Japanese cohort study showed that PRS and the nitrogen compound transport PRS were associated with a higher risk of developing T2DM. Among 43 metabolites, 14 metabolites were positively associated with T2DM incidence, whereas only glycine was inversely associated with T2DM incidence. 3-Hydroxyisobutyric-acid, 2-aminobutyric acid, 2-ketoisocaproic acid, leucine, glycine, glucose, and 3-methyl-2-oxobutyric acid mediated the association between the PRS and T2DM incidence.

Our findings indicate that the PRS was associated with T2DM incidence, regardless of lifestyle factors. Many previous studies have proved that the PRS is associated with T2DM incidence, regardless of whether individuals have healthy lifestyles [ 3 , 4 , 36 , 37 ]. Our finding was consistent with those previous studies. Additionally, our study showed that the nitrogen compound transport PRS was associated with T2DM incidence. Several biological mechanisms may support this observation, including reduced efficiency of branched-chain amino acid transport contributing to insulin resistance [ 38 ] and impaired glutamate metabolism compromising β-cell function [ 39 ]. Further studies are needed to replicate this association and better understand the mechanisms.

The result of this large-scale prospective cohort study conducted in Japan was consistent with previous findings on the strong positive association between metabolites, such as 3-hydroxybutyric acid, 2-aminobutyric acid, glutamic acid, tyrosine, leucine, valine, and glucose, with T2DM risk [ 19 ]. The association of leucine and valine with the T2DM risk was confirmed in previous studies and Mendelian randomization analysis [ 40 , 41 ], and this was consistent with our findings. Furthermore, higher levels of glycine were inversely associated with T2DM risk, which is consistent with findings of previous studies including a large-scale prospective cohort study from Europe [ 42 ]. Several biological mechanisms may underlie this association, including impaired branched-chain amino acid catabolism contributing to insulin resistance [ 37 ], disturbances in glutamate metabolism affecting β-cell function [ 38 ], genetically driven alterations in central amino acid transport that influence feeding behavior [ 43 ], and elevated ketone bodies or oxidative stress markers reflecting metabolic dysregulation [ 44 ]. Although the present study was exploratory, it is important to note that most previous studies were conducted in European populations [ 19 ] and few large cohorts had > 10 000 participants [ 42 , 45 ]. Hence, our findings may offer valuable insights into the pathways involved in T2DM pathophysiology and may contribute to the identification of novel biomarkers for early T2DM risk detection before overt symptoms.

The underlying mechanisms for the association between the PRS and T2DM incidence remain unclear. Many studies have indicated that participants with a higher PRS have an increased risk of T2DM incidence, even among those with healthy lifestyles [ 3 , 4 , 36 , 37 ]. However, an effective prevention strategy for those at high genetic risk is still lacking. As the cost of genetic analysis continues to decrease and individuals may soon have easy access to their genetic information, it is crucial to explore prevention strategies for populations at high genetic risk. Metabolites offer a promising opportunity to understand the “black box” of disease mechanisms. Thus, integrating metabolites into genetic epidemiology could provide a deeper understanding of gene-environment interactions and facilitate the discovery of novel biomarkers for the early prevention and detection of T2DM. In this study, we explored circulating metabolites associated with both the T2DM incidence and genetic risk, which may explain the association between the genetic risk and T2DM incidence. We identified 14 metabolites that were associated with the T2DM incidence and genetic risk. Moreover, seven of these metabolites partially mediated the association between the PRS and incident T2DM. Although the current study was exploratory, it is difficult to determine the exact role of each metabolite in the inheritance pathways and diabetogenesis. However, our findings suggest that differences in metabolites associated with the T2DM incidence and genetic risk could provide insightful information for elucidating the mechanisms linking the PRS and T2DM incidence. This may help identify potential biomarkers for new drug development.

To our best knowledge, this is the first study to examine whether metabolites mediated the associations of the genetic risk with incident T2DM. Most importantly, this study revealed differences in metabolite levels by genetic risk among participants without T2DM at baseline, which may represent useful biomarkers for preventing T2DM tailored to an individual’s genetic risk. Additionally, the use of NMR spectroscopy enabled absolute quantification of circulating metabolites [ 46 ]. This allowed for direct comparison of metabolite levels across individuals, thereby improving the interpretability and reproducibility of our finding in a population-based setting.

The study has some limitations. First, this study had a lower T2DM incidence rate than previous studies. One of the reasons why we analyzed participants who took part in both the baseline and follow-up surveys was to avoid healthy volunteer bias. Second, our study included only Japanese participants. Given that allele frequencies and dietary habits vary by ancestry, our findings may not be applicable to populations of different ancestral backgrounds [ 47 , 48 ]. Third, the currently known and quantifiable metabolome consists of > 100 000 metabolites [ 49 ]; however, we did not examine all metabolites, so additional relevant metabolites may have been overlooked. Fourth, we used PRSs, which included more than 60 000 SNPs; however, it explained only a small proportion of T2DM heritability. Additional T2DM-associated variants identified by whole exome and whole genome sequencing studies will help to improve the genetic risk performance and enhance our understanding of T2DM pathogenesis. Finally, although this study had a larger sample size than previous studies, the number of incidents T2DM cases were not substantial because the follow-up time was shorter than that in previous studies. This may have limited the statistical power. Thus, well-established long-term follow-up studies may be required in the future.


## Conclusions

This study demonstrated that PRSs are associated with T2DM incidence, independent of lifestyle factors. We identified 14 metabolites that were associated with T2DM incidence. Seven of these metabolites partially mediated the relationship between the genetic risk and T2DM incidence. These findings contribute to a better understanding of the metabolic pathways underlying the genetic susceptibility to T2DMs. Further research is needed to clarify the biological mechanisms linking the polygenic risk to T2DM development.


## Supplementary Information


## Acknowledgements

The authors thank the members of the Tohoku Medical Megabank Organization, including the Genome Medical Research Coordinators, and the office and administrative personnel for their assistance. A complete list of the members is available at https://www.megabank.tohoku.ac.jp/english/a240901/ .

Use of artificial intelligence and machine learning: This study did not use generative artificial intelligence.


## Abbreviations

Genome-wide association studies

Single nucleotide polymorphisms

Tohoku Medical Megabank community-based cohort study

Nuclear magnetic resonance spectroscopy

Food frequency questionnaire

95% Confidence intervals



Authors contributions: Conceptualization, M.T., S.K., K.K., A.H.; Data curation, M.T., K.N., I.C., T.N., S.K., K.K., I.K., E.H., A.N., H.O., S.O., S.N., K.K., G.T.; Formal analysis, M.T., K.N., I.C., S.K., I.M., E.H., H.O., K.K., G.T.; Funding acquisition, M.T., A.H.; Investigation, All authors; Methodology, M.T., S.K., K.K., I.M., A.H.; Project administration, A.H.; Resources; N.N., T.N., S.K., K.K., I.M., E.H., A.N., S.O., S.N., K.K., G.T., A.H., M.Y.; Software, M.T., K.N., I.C., T.N., H.O., S.O., S.N., K.K., G.T.; Supervision, A.H., M.Y.; Validation, M.T.; Visualization, All authors; Writing draft, M.T.; Review & editing. All authors have read and agreed to the published version of the manuscript. M.T. is the guarantor of this work and, as such, had full access to all the data in the study and takes responsibility for the integrity of the data and the accuracy of the data analysis.


## Funding

This study was supported by grants from the Japanese Society for the Promotion of Science [JSPS; Grant-in-Aid for Science Research (B), Number: 24K02699; JSPS KAKENHI Grant Number JP24K23673]; and the Tohoku Medical Megabank Project of the Ministry of Education, Culture, Sports, Science, and Technology and the Japan Agency for Medical Research and Development [AMED; JP22tm0124005]. This study used a supercomputer system provided by the Tohoku Medical Megabank Project, founded by AMED [Grant Number: JP21tm0424601]. The funders had no role in the design and conduct of the study; the collection, management, analysis, and interpretation of the data; or the preparation, review, and approval of the manuscript; or the decision to submit the manuscript for publication.


## Availability of data and materials

Availability of data and materials: Masato [AUTHOR] has full access to all data and code in the study and takes responsibility for the integrity of the data and the accuracy of the data analyses. Any additional information required to reanalyze the data reported in this paper is available after contacting: [EMAIL_REDACTED].


## Declarations


### Ethics approval and consent to participate

The study protocol conformed to the ethical guidelines of the 1975 Declaration of Helsinki and was approved by the Ethics Committee of [AUTHOR], Tohoku University (approval number: 2022-4-047; approval date: June 30, 2022). Written informed consent was obtained from all participants.


### Consent for publication


### Competing interests

The authors declare no competing interests.


## Footnotes

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials


### Data Availability Statement

Availability of data and materials: Masato [AUTHOR] has full access to all data and code in the study and takes responsibility for the integrity of the data and the accuracy of the data analyses. Any additional information required to reanalyze the data reported in this paper is available after contacting: [EMAIL_REDACTED].
