# FEXP_ANON_138

## Abstract

Major depressive disorder (MDD) is closely associated with suicide, which often begins with suicidal ideation (SI). However, the underlying neural mechanisms remain unclear.

We included 73 MDD patients with SI (MDD-SI), 44 MDD patients without SI (MDD-NSI) and 78 healthy controls (HCs), then compared the amplitude of low-frequency fluctuations (ALFF), functional connectivity (FC), and effective connectivity (EC) differences across groups and analyzed their relationship with SI severity. FC and EC analyses used brain regions with ALFF differences between MDD-SI and MDD-NSI as seed points. ALFF findings were validated using the REST-meta-MDD consortium dataset (N = 1 596, 24 sites). Additionally, we explored the trend of changes in abnormal activity and connectivity of SI and suicidal behavior (SB) in MDD-SI.

Compared to MDD-NSI, MDD-SI showed increased ALFF in the right anterior cingulate cortex (ACC), validated by the REST-meta-MDD consortium dataset. MDD-SI also exhibited reduced FC between the right ACC and the left inferior frontal gyrus and decreased EC from the right ACC to the right fusiform gyrus, which were negatively correlated with the Hamilton Depression Rating Scale (HAMD)-suicidality item scores. Increased EC was observed in MDD-SI from the right ACC to the right cerebellar tonsil and from the left inferior parietal lobule (IPL) to the right ACC, following a progressive increase pattern (HC < MDD-NSI < MDD-SI without SB < MDD-SI with SB).

Increased activity and aberrant connectivity of the ACC may be associated with SI in MDD patients and potentially serve as biomarkers for suicide risk.


## Introduction

Major depressive disorder (MDD) is defined by persistent low mood, loss of interest in activities, and associated psychological and physical symptoms lasting for at least two weeks (Simon, Moise, & Mohr, 2024 ). MDD is one of the leading contributors to the global burden of disease, responsible for 49.4 million disability-adjusted life years worldwide in 2020 (Santomauro et al., 2021 ). Studies have shown that MDD is strongly associated with suicide (Angst et al. 1999 ), with the suicide risk among MDD patients being 20 times higher than that of the general population (Otte et al., 2016 ). Annually, 7% of male and 4% of female MDD patients die by suicide (Nordentoft, Mortensen, & Pedersen, 2011 ). Suicide typically begins with suicidal ideation (SI), which involves thinking about, considering, or planning suicide (Klonsky, May, & Saffer, 2016 ). The lifetime prevalence of SI among individuals with MDD in China is 53.1% (Dong et al., 2018 ). Research suggests that compared to MDD patients without SI (MDD-NSI), those with SI (MDD-SI) tend to exhibit more severe symptoms, greater psychiatric comorbidities, poorer cognitive function, and lower quality of life (Borentain, Nash, Dayal, & DiBernardo, 2020 ). Therefore, identifying the neural mechanisms that differentiate MDD-SI and MDD-NSI is crucial for the early identification and intervention of suicide risk, as well as for the treatment of MDD.

Resting-state functional magnetic resonance imaging (rs-fMRI) effectively identifies abnormal brain regional activity in mental disorders, offering valuable insights (Liu et al., 2022 ). Among rs-fMRI indices, the amplitude of low-frequency fluctuations (ALFFs) provides a reliable measure of regional spontaneous activity (Zuo et al., 2010 ). Previous studies have reported distinct ALFF abnormalities in MDD -SI. For example, Lan et al. found that compared to MDD-NSI, MDD-SI exhibited enhanced ALFF in the right hippocampus, bilateral thalami, and caudate nuclei (Lan et al., 2019 ). Extending beyond static measures, dynamic ALFF studies further suggest reduced temporal variability in the dorsal anterior cingulate cortex (ACC) and left hippocampus in MDD-SI, and these alterations may predict the severity of SI (Li et al., 2019 ).

Beyond regional activity, functional connectivity (FC) has been widely used to investigate interregional coordination (Horien, Shen, Scheinost, & Constable, 2019 ). Du and his colleagues demonstrated reduced FC between the ACC and the right middle temporal gyrus and the orbitomedial prefrontal cortex in MDD-SI compared to MDD-NSI (Du et al., 2017 ). At the network level, studies have demonstrated that both adult and adolescent patients with MDD and SI exhibit reduced connectivity among large-scale brain networks, particularly the default mode network, salience network, and frontoparietal network, which are critically involved in executive function (Cao et al., 2020 ; Ordaz et al., 2018 ; Yang et al., 2021 ).

Effective connectivity (EC) approaches, such as the Granger causality model (GCM), quantify the directionality of interactions between brain regions (Jiao et al., 2011 ; Mastrovito, Hanson, & Hanson, 2018 ). Compared to FC, EC provides a more mechanistic account of abnormal information transfer. Nevertheless, EC studies specifically targeting MDD-SI remain limited.

To the best of our knowledge, no study has applied ALFF-based FC and EC analyses to differentiate MDD-SI from MDD-NSI. While FC captures abnormal functional interactions between brain regions, it does not specify which regions exhibit primary activity disturbances. In contrast, ALFF directly detects local abnormal activity patterns, providing suitable seed regions for connectivity analyses (Chen et al., 2023 ; He et al., 2024 ; Zhang et al., 2021 ). Building on this rationale, our study identified ALFF alterations in MDD-SI and subsequently employed ALFF-based FC and EC analyses to investigate both functional integration and the directionality of interactions among these regions, thereby offering a deeper understanding of the mechanisms underlying brain network dysfunction associated with SI.

We hypothesized that MDD-SI patients would exhibit altered activity in key hub regions previously implicated in SI and that abnormalities in FC and EC originating from these regions would characterize the neural basis of SI and potentially relate to its clinical severity.


## Methods


## Participants

The participants were recruited from the Xiangya Second Hospital, Central South University. The Ethics Committee of the Second Xiangya Hospital of Central South University approved this study. All participants were right-handed native Chinese speakers. Written informed consent was obtained from each participant. All research procedures were conducted in strict accordance with the Declaration of Helsinki. A total of 127 patients with MDD and 88 healthy controls (HCs) were included, with the MDD group further subdivided into MDD-SI (n = 83) and MDD-NSI (n = 44).

Diagnosis of MDD was confirmed by a licensed psychiatrist using the Diagnostic and Statistical Manual of Mental Disorders, Fourth Edition (DSM-IV)–based Structured Clinical Interview for DSM-IV Patient Edition (SCID-P), with a cutoff score of ≥17 on the 17-item Hamilton Depression Rating Scale (HAMD) (Hamilton, 1967 ). Gender- and age-matched HCs (n = 88) were recruited from the community and screened using the DSM-IV non-patient version of the Structured Clinical Interview (SCID/NP). The exclusion criteria for MDD and HCs are detailed in Supplementary Material S1 .


## Clinical assessment

Diagnosis and assessment were performed by a clinical psychiatrist on the day of the MRI scan. Symptom severity was evaluated using HAMD, the Hamilton Anxiety Rating Scale (HAMA) (Hamilton, 1959 ), and the Brief Psychiatric Rating Scale (BPRS) (Faustman & Overall, 1962 ). SI was assessed using the Beck Scale for Suicide Ideation-Chinese Version (BSI-CV) (Beck, Kovacs, & Weissman, 1979 ). In this scale, items 4 and 5 are used to evaluate the participant’s current active and passive suicidal thoughts (Marzuk, Hartwell, Leon, & Portera, 2005 ). A score greater than 1 on either item 4 or 5 indicates the presence of SI, and the participant is required to complete the remaining 14 items. If both items 4 and 5 score 0, indicating no SI, the participant may skip the remaining items. The BSI-CV score is calculated as the sum of scores across 19 items for the recent one week (Yang et al., 2022 ).


## ALFF calculation

The details of fMRI data imaging acquisition parameters and preprocessing are described in Supplemental Material S2 . The calculation of ALFF was also performed using the DPABI_V8.2 toolbox (Yan, Wang, Zuo, & Zang, 2016 ). After data preprocessing, the time series of each voxel was transformed into the frequency domain using a fast Fourier transform to obtain the power spectrum. The square root of the power spectrum was calculated at each frequency, and the mean square root within the frequency range of 0.01–0.08 Hz was determined as the ALFF value for each voxel. For group comparisons, the individual-level ALFF value of each voxel was normalized into Z-scores by subtracting the whole-brain mean ALFF value and then dividing by the standard deviation.


## FC calculation

The calculation of FC was also performed using the DPABI_V8.2 toolbox (Yan et al., 2016 ). Brain regions with significant ALFF differences between the MDD-SI and MDD-NSI groups were defined as seed regions for FC analysis. FC was defined as the Pearson correlation coefficient between the mean time series of voxels within the seed regions and those of all other voxels in the whole brain. Subsequently, the FC correlation coefficients between the seed regions and all other voxels in the brain were converted into z-values using Fisher’s r-to-z transformation to facilitate group comparisons.


## EC calculation using the Granger Causality Model

GCM is employed to investigate the directional causal relationships between seed regions and all other voxels across the entire brain using RESTplus V1.30 ( http://www.restfmri.net/forum/restplus ) (Jia et al., 2019 ). It includes two analyses: one from region X to region Y and the other from region Y to region X. A positive coefficient from region X to region Y indicates that the activity in region X exerts a causal influence on the activity in region Y in the same direction, whereas a negative coefficient indicates a causal influence in the opposite direction. The same reasoning applies to the relationship from region Y to region X (Zang et al., 2012 ). In this study, the time series of seed regions was designated as time series X, while the time series of all other voxels in the whole brain was designated as time series Y. Subsequently, two Granger causality maps were generated based on the influence measures for each subject. Finally, Fisher’s r-to-z transformation was applied to improve the normality of data distributions for further group comparisons.


## Validation analysis

To ensure reproducibility, we validated ALFF findings using the REST-meta-MDD consortium dataset ( http://rfmri.org/REST-meta-MDD ) (Chen et al., 2022 ; Yan et al., 2019 ). This dataset includes rs-fMRI data from 24 research sites, comprising 538 MDD patients (mean age: 33.33 ± 11.41 years, 64.13% females) and 1 058 HCs (mean age: 36.45 ± 15.82 years, 58.60% females). The MDD cohort was divided into 396 MDD-SI patients (mean age: 33.26 ± 11.21 years, 67.17% female) and 142 MDD-NSI patients (mean age: 33.54 ± 11.99 years, 55.63% female) based on the HAMD-suicidality item (item 3). Scores greater than 0 were classified as the SI group, and a score of 0 was classified as the NSI group (Kong et al., 2023 ). Ethical approval was obtained from the local research ethics committees at all sites. We extracted the abnormal ALFF values of each subject and conducted an analysis of variance (ANOVA) using SPSS software version 27 to assess the differences between groups. Post hoc comparisons were performed using the Bonferroni method to correct for multiple comparisons with the statistical significance at p Bon < 0.05.


## Exploratory analysis

To examine whether the brain regions that showed significant group differences between MDD-SI and MDD-NSI also exhibit progressive changes along a continuum of suicide severity, extending to individuals with suicidal behavior (SB). We further categorized the MDD-SI group into two subgroups: one with SB, defined by HAMD-suicidality item scores = 4, and one without SB, defined by HAMD-suicidality item scores <4 (Kong et al., 2023 ). Meanwhile, we extracted the corresponding values from detected brain regions to explore their variation along the gradient of suicide severity.


## Statistical analysis

We used SPSS statistical software version 27 for the analysis of demographic and clinical data. One-way ANOVAs, two-sample t-tests, and chi-square (χ 2 ) tests were performed to evaluate the demographic and clinical differences between groups. A p -value of <0.05 was considered to indicate statistical significance for the above comparisons.

To determine group-level differences in ALFF, FC, and EC, we used Statistical Parametric Mapping 12 (SPM12; https://www.fil.ion.ucl.ac.uk/spm/ ) to perform a one-way analysis of covariance (ANCOVA) across three groups, with age, gender, education level, and head motion parameters as covariates. Significant voxels from the ANCOVA were then used as a mask for post hoc t-tests between any two groups. The voxel-wise threshold for statistical significance was set at a false discovery rate–corrected p -value ( p FDR ) < 0.05, with a cluster size >5 voxels. Finally, we extracted the ALFF, FC, and EC values from the voxels showing significant differences between MDD-NSI and MDD-SI and performed Spearman’s rank correlation analysis to examine the relationship between these values and the HAMD-suicidality item (item 3) scores across all patients.


## Results


## Demographic and clinical characteristics

The demographic and clinical characteristics of the three groups are shown in Table 1 . No significant differences were found in sex, age, and education level. No significant differences were observed in illness duration, total HAMD score (excluding the suicidality item), HAMA score, and BPRS score between the MDD-NSI and MDD-SI groups. However, the MDD-SI group had a significantly higher score on the HAMD-suicidality item compared to the MDD-NSI group ( t = 8.18), indicating that the clinical symptoms in these two groups were comparable, except for suicidality. Table 1. Demographic and clinical characteristics of three groups Characteristic MDD-SI (n = 78) MDD-NSI (n = 44) HCs (n = 73) χ 2 /F/t p Gender (male/female) 25/53 15/29 29/44 1.01 0.603 Age (years) 24.81 ± 6.97 27.86 ± 10.24 24.96 ± 4.95 2.92 0.056 Education (years) 14.80 ± 2.35 13.46 ± 2.84 14.53 ± 4.02 2.63 0.075 Number of episodes 1.99 ± 1.80 2.02 ± 2.89 N/A −0.09 0.466 Illness duration (months) 28.39 ± 33.87 26.27 ± 28.32 N/A 0.35 0.727 On medication(yes/no) 42/36 19/25 N/A 1.28 0.258 FLU equivalent doses (mg/d) 17.21 ± 18.48 14.70 ± 19.85 N/A 0.70 0.242 CPZ equivalent doses (mg/d) 16.60 ± 66.68 30.38 ± 107.95 N/A −0.87 0.193 Treatment duration (months) 5.12 ± 15.43 4.68 ± 17.43 N/A 0.14 0.443 HAMD-suicidality 2.50 ± 0.95 1.00 ± 1.01 N/A 8.18 <0.001 HAMD-except suicidality 20.29 ± 4.22 20.20 ± 3.75 N/A 0.12 0.906 HAMD-total score 22.79 ± 4.42 21.20 ± 3.91 N/A 1.99 0.049 HAMA 18.41 ± 6.90 19.00 ± 7.40 N/A −0.44 0.659 BPRS 37.46 ± 7.84 35.95 ± 6.83 N/A 1.07 0.288 BSI-CV 34.37 ± 5.93 N/A N/A N/A N/A Note : MDD-SI, major depressive disorder patients with suicidal ideation; MDD-NSI, major depressive disorder patients without suicidal ideation; HCs, healthy controls; FLU, Fluoxetine; CPZ, Chlorpromazine; HAMD, 17-item Hamilton Depression Scale; HAMA, Hamilton Anxiety Rating Scale; BPRS, Brief Psychiatric Rating Scale; BSI-CV, Beck Scale for Suicide Ideation-Chinese Version; N/A, not available. HAMD-suicidality refers to the score of the suicidality item (item 3) of HAMD; HAMD-except suicidality refers to the total score of HAMD excluding item 3.


### Table 1.: Demographic and clinical characteristics of three groups

| Characteristic | MDD-SI (n = 78) | MDD-NSI (n = 44) | HCs (n = 73) | χ 2 /F/t | p |
| Gender (male/female) | 25/53 | 15/29 | 29/44 | 1.01 | 0.603 |
| Age (years) | 24.81 ± 6.97 | 27.86 ± 10.24 | 24.96 ± 4.95 | 2.92 | 0.056 |
| Education (years) | 14.80 ± 2.35 | 13.46 ± 2.84 | 14.53 ± 4.02 | 2.63 | 0.075 |
| Number of episodes | 1.99 ± 1.80 | 2.02 ± 2.89 | N/A | −0.09 | 0.466 |
| Illness duration (months) | 28.39 ± 33.87 | 26.27 ± 28.32 | N/A | 0.35 | 0.727 |
| On medication(yes/no) | 42/36 | 19/25 | N/A | 1.28 | 0.258 |
| FLU equivalent doses (mg/d) | 17.21 ± 18.48 | 14.70 ± 19.85 | N/A | 0.70 | 0.242 |
| CPZ equivalent doses (mg/d) | 16.60 ± 66.68 | 30.38 ± 107.95 | N/A | −0.87 | 0.193 |
| Treatment duration (months) | 5.12 ± 15.43 | 4.68 ± 17.43 | N/A | 0.14 | 0.443 |
| HAMD-suicidality | 2.50 ± 0.95 | 1.00 ± 1.01 | N/A | 8.18 | <0.001 |
| HAMD-except suicidality | 20.29 ± 4.22 | 20.20 ± 3.75 | N/A | 0.12 | 0.906 |
| HAMD-total score | 22.79 ± 4.42 | 21.20 ± 3.91 | N/A | 1.99 | 0.049 |
| HAMA | 18.41 ± 6.90 | 19.00 ± 7.40 | N/A | −0.44 | 0.659 |
| BPRS | 37.46 ± 7.84 | 35.95 ± 6.83 | N/A | 1.07 | 0.288 |
| BSI-CV | 34.37 ± 5.93 | N/A | N/A | N/A | N/A |

## Group differences in ALFF

Significant differences in ALFF among the three groups were observed in the following brain regions: right precentral gyrus (PreCG; F = 15.44), bilateral postcentral gyrus (PoCG; right: F = 15.41; left: F = 11.38), bilateral ACC (right: F = 12.09; left: F = 10.46), right superior frontal gyrus (SFG; F = 10.86), left ventral lateral nucleus of thalamus ( F = 10.23), right superior parietal gyrus (SPG; F = 10.18), left inferior temporal gyrus (ITG; F = 8.89), medial frontal gyrus (MeFG; F = 8.74), left cerebellar pyramis ( F = 7.96), and vermis ( F = 7.92). More details are shown in Table 2 and Supplementary Figure S1 . Table 2. Brain regions showing significant differences among the three groups Brain regions One-way ANOVA Post hoc analysis MNI Cluster size F p FDR η 2 Comparison t p FDR Cohen’s d X Y Z ALFF R PreCG 51 −9 39 30 15.44 <0.001 0.14 MDD-SI < HCs −4.58 0.001 0.75 MDD-NSI < HCs −5.11 <0.001 0.98 R PoCG 51 −12 33 30 15.41 <0.001 0.14 MDD-SI < HCs −4.23 0.001 0.69 MDD-NSI < HCs −5.25 <0.001 1.01 R ACC 9 21 −12 36 12.09 <0.001 0.11 MDD-SI > MDD-NSI* 3.71 0.024 0.71 MDD-SI > HCs 4.76 <0.001 0.78 L PoCG −57 −6 30 45 11.38 <0.001 0.11 MDD-SI < HCs −4.25 0.001 0.70 MDD-NSI < HCs −4.06 <0.001 0.78 R SFG 21 54 6 11 10.86 <0.001 0.10 MDD-SI > HCs 4.66 <0.001 0.76 L ACC −9 24 −12 46 10.46 <0.001 0.10 MDD-SI > HCs 4.56 <0.001 0.75 MDD-NSI > HCs 3.67 0.003 0.71 L VLN −12 −15 6 5 10.23 <0.001 0.10 MDD-SI < HCs −3.01 0.004 0.58 MDD-NSI < HCs −4.34 <0.001 0.84 R SPG 21 −69 66 8 10.18 <0.001 0.10 MDD-SI > HCs 2.78 0.009 0.46 MDD-NSI > HCs 4.50 0.001 0.87 L ITG −39 −12 −36 20 8.89 0.001 0.08 MDD-SI > HCs 4.09 <0.001 0.67 MDD-NSI > HCs 3.84 0.002 0.77 MeFG 0 −18 60 36 8.74 0.001 0.08 MDD-SI < HCs −4.02 0.001 0.66 MDD-NSI < HCs −3.69 <0.001 0.71 L pyramis −30 −78 −42 6 7.96 0.001 0.08 MDD-NSI > HCs 3.98 0.002 0.77 Vermis 0 −30 −12 6 7.92 0.001 0.08 MDD-SI < HCs −3.83 0.001 0.63 MDD-NSI < HCs −3.05 0.003 0.59 FC L IFG −54 39 −3 8 9.92 0.001 0.09 MDD-SI < MDD-NSI* −4.42 <0.001 0.84 MDD-SI < HCs −3.08 0.007 0.50 EC From R ACC to the whole brain R cerebellar tonsil 15 −33 −45 8 7.88 0.002 0.08 MDD-SI > MDD-NSI* 3.38 0.002 0.64 MDD-SI > HCs 3.75 0.001 0.61 R fusiform gyrus 51 −33 −30 5 7.71 0.002 0.07 MDD-SI < MDD-NSI* −3.85 <0.001 0.73 From the whole brain to R ACC R VLN 15 −15 6 11 10.71 0.001 0.10 MDD-SI > HCs 4.49 <0.001 0.74 MDD-NSI > HCs 3.38 0.009 0.65 L IPL −45 −45 48 32 9.84 0.001 0.09 MDD-SI > MDD-NSI* 3.08 0.012 0.59 MDD-SI > HCs 4.37 <0.001 0.72 R MFG 45 15 54 7 9.31 0.001 0.09 MDD-SI > HCs 3.78 <0.001 0.62 MDD-NSI > HCs 3.37 0.009 0.65 L VPM −9 −18 3 6 8.77 0.001 0.08 MDD-SI > HCs 4.15 <0.001 0.68 Note : MDD-SI, major depressive disorder patients with suicidal ideation; MDD-NSI, major depressive disorder patients without suicidal ideation; HCs, healthy controls; MNI, Montreal Neurological Institute; FDR, false discovery rate correction; ALFF, amplitude of low-frequency fluctuation; FC, functional connectivity; EC, effective connectivity; R, right; L, left; PreCG, precentral gyrus; PoCG, postcentral gyrus; ACC, anterior cingulate cortex; SFG, superior frontal gyrus; VLN, ventral lateral nucleus of thalamus; SPG, superior parietal gyrus; ITG, inferior temporal gyrus; MeFG, medial frontal gyrus; IFG, inferior frontal gyrus; IPL, inferior parietal lobule; MFG, middle frontal gyrus; VPM, ventral posteromedial nucleus of thalamus.


### Table 2.: Brain regions showing significant differences among the three groups

| Brain regions | One-way ANOVA |  | Post hoc analysis |
| MNI | Cluster size | F | p FDR | η 2 | Comparison | t | p FDR | Cohen’s d |
| X | Y | Z |
| ALFF |  |  |  |  |  |  |  |  |  |  |  |
| R PreCG | 51 | −9 | 39 | 30 | 15.44 | <0.001 | 0.14 | MDD-SI < HCs | −4.58 | 0.001 | 0.75 |
| MDD-NSI < HCs | −5.11 | <0.001 | 0.98 |
| R PoCG | 51 | −12 | 33 | 30 | 15.41 | <0.001 | 0.14 | MDD-SI < HCs | −4.23 | 0.001 | 0.69 |
| MDD-NSI < HCs | −5.25 | <0.001 | 1.01 |
| R ACC | 9 | 21 | −12 | 36 | 12.09 | <0.001 | 0.11 | MDD-SI > MDD-NSI* | 3.71 | 0.024 | 0.71 |
| MDD-SI > HCs | 4.76 | <0.001 | 0.78 |
| L PoCG | −57 | −6 | 30 | 45 | 11.38 | <0.001 | 0.11 | MDD-SI < HCs | −4.25 | 0.001 | 0.70 |
| MDD-NSI < HCs | −4.06 | <0.001 | 0.78 |
| R SFG | 21 | 54 | 6 | 11 | 10.86 | <0.001 | 0.10 | MDD-SI > HCs | 4.66 | <0.001 | 0.76 |
| L ACC | −9 | 24 | −12 | 46 | 10.46 | <0.001 | 0.10 | MDD-SI > HCs | 4.56 | <0.001 | 0.75 |
| MDD-NSI > HCs | 3.67 | 0.003 | 0.71 |
| L VLN | −12 | −15 | 6 | 5 | 10.23 | <0.001 | 0.10 | MDD-SI < HCs | −3.01 | 0.004 | 0.58 |
| MDD-NSI < HCs | −4.34 | <0.001 | 0.84 |
| R SPG | 21 | −69 | 66 | 8 | 10.18 | <0.001 | 0.10 | MDD-SI > HCs | 2.78 | 0.009 | 0.46 |
| MDD-NSI > HCs | 4.50 | 0.001 | 0.87 |
| L ITG | −39 | −12 | −36 | 20 | 8.89 | 0.001 | 0.08 | MDD-SI > HCs | 4.09 | <0.001 | 0.67 |
| MDD-NSI > HCs | 3.84 | 0.002 | 0.77 |
| MeFG | 0 | −18 | 60 | 36 | 8.74 | 0.001 | 0.08 | MDD-SI < HCs | −4.02 | 0.001 | 0.66 |
| MDD-NSI < HCs | −3.69 | <0.001 | 0.71 |
| L pyramis | −30 | −78 | −42 | 6 | 7.96 | 0.001 | 0.08 | MDD-NSI > HCs | 3.98 | 0.002 | 0.77 |
| Vermis | 0 | −30 | −12 | 6 | 7.92 | 0.001 | 0.08 | MDD-SI < HCs | −3.83 | 0.001 | 0.63 |
| MDD-NSI < HCs | −3.05 | 0.003 | 0.59 |
| FC |  |  |  |  |  |  |  |  |  |  |  |
| L IFG | −54 | 39 | −3 | 8 | 9.92 | 0.001 | 0.09 | MDD-SI < MDD-NSI* | −4.42 | <0.001 | 0.84 |
| MDD-SI < HCs | −3.08 | 0.007 | 0.50 |
| EC |  |  |  |  |  |  |  |  |  |  |  |
| From R ACC to the whole brain |  |  |  |  |  |  |  |
| R cerebellar tonsil | 15 | −33 | −45 | 8 | 7.88 | 0.002 | 0.08 | MDD-SI > MDD-NSI* | 3.38 | 0.002 | 0.64 |
| MDD-SI > HCs | 3.75 | 0.001 | 0.61 |
| R fusiform gyrus | 51 | −33 | −30 | 5 | 7.71 | 0.002 | 0.07 | MDD-SI < MDD-NSI* | −3.85 | <0.001 | 0.73 |
| From the whole brain to R ACC |  |  |  |  |  |  |  |
Post hoc analyses revealed that, compared to MDD-NSI, MDD-SI exhibited increased ALFF in the right ACC ( t = 3.71; Table 2 and Figure 1a ). Figure 1. Brain regions exhibiting significant differences in ALFF between MDD-SI and MDD-NSI. (a) Results from the original dataset. * p < 0.05, FDR corrected. (b) Results from the validation analysis using the REST-meta-MDD consortium dataset. Post hoc comparisons were performed using the Bonferroni method, with * denoting p < 0.05 and *** denoting p < 0.001. Note : MDD-SI, major depressive disorder patients with suicidal ideation; MDD-NSI, major depressive disorder patients without suicidal ideation; HCs, healthy controls; R, right; ACC, anterior cingulate cortex; ALFF, amplitude of low-frequency fluctuation.


> **Figure 1.:** Brain regions exhibiting significant differences in ALFF between MDD-SI and MDD-NSI. (a) Results from the original dataset. * p < 0.05, FDR corrected. (b) Results from the validation analysis using the REST-meta-MDD consortium dataset. Post hoc comparisons were performed using the Bonferroni method, with * denoting p < 0.05 and *** denoting p < 0.001. Note : MDD-SI, major depressive disorder patients with suicidal ideation; MDD-NSI, major depressive disorder patients without suicidal ideation; HCs, healthy controls; R, right; ACC, anterior cingulate cortex; ALFF, amplitude of low-frequency fluctuation.

Compared to HCs, MDD-SI exhibit increased ALFF in the bilateral ACC (right: t = 4.76; left: t = 4.56), right SFG ( t = 4.66), right SPG ( t = 2.78), left ITG ( t = 4.09), and decreased ALFF in the right PreCG ( t = −4.58), bilateral PoCG (right: t = −4.23; left: t = −4.25), left ventral lateral nucleus of thalamus ( t = −3.01), MeFG ( t = −4.02), and vermis ( t = −3.83). MDD-NSI, compared to HCs, exhibit increased ALFF in the left ACC ( t = 3.67), right SPG ( t = 4.50), left ITG ( t = 3.84), left pyramis ( t = 3.98), and decreased ALFF in the right PreCG ( t = −5.11), bilateral PoCG (right: t = −5.25; left: t = −4.06), left ventral lateral nucleus of thalamus ( t = −4.34), MeFG ( t = −3.69), and vermis ( t = −3.05).


## Group differences in FC

We selected the right ACC as the seed region for further FC analysis. Our results showed that three groups showed significant differences in the left inferior frontal gyrus (IFG; F = 9.92; Table 2 and Supplementary Figure S2A ). MDD-SI exhibited reduced FC between the right ACC and the left IFG compared with MDD-NSI and HCs (MDD-NSI: t = −4.42; Table 2 and Figure 2a ; HCs: t = −3.08), while no significant differences were observed between the MDD-NSI and HCs. Figure 2. Brain regions showing significant connectivity pattern differences between MDD-SI and MDD-NSI. (a) FC results between the right ACC and the whole brain. (b) EC from the right ACC to the whole brain. (c) EC from the whole brain to the right ACC. D: 3D brain network visualization of connectivity pattern differences, with cool colors representing decreased connectivity and warm colors indicating increased connectivity. Node size corresponds to the t-value. *** p < 0.001, ** p < 0.01, * p < 0.05, FDR corrected. Note : MDD-SI, major depressive disorder with suicidal ideation; MDD-NSI, major depressive disorder without suicidal ideation; R, right; L, left; ACC, anterior cingulate cortex; IFG, inferior frontal gyrus; IPL, inferior parietal lobule; FC, functional connectivity; EC, effective connectivity.


> **Figure 2.:** Brain regions showing significant connectivity pattern differences between MDD-SI and MDD-NSI. (a) FC results between the right ACC and the whole brain. (b) EC from the right ACC to the whole brain. (c) EC from the whole brain to the right ACC. D: 3D brain network visualization of connectivity pattern differences, with cool colors representing decreased connectivity and warm colors indicating increased connectivity. Node size corresponds to the t-value. *** p < 0.001, ** p < 0.01, * p < 0.05, FDR corrected. Note : MDD-SI, major depressive disorder with suicidal ideation; MDD-NSI, major depressive disorder without suicidal ideation; R, right; L, left; ACC, anterior cingulate cortex; IFG, inferior frontal gyrus; IPL, inferior parietal lobule; FC, functional connectivity; EC, effective connectivity.


## Group difference in EC


## EC from the right ACC to the whole brain

We used the right ACC as seed region for the subsequent EC analysis. The results showed significant differences among the three groups in the right cerebellar tonsil ( F = 7.88) and right fusiform gyrus ( F = 7.71). More details are shown in Table 2 and Supplementary Figure S2B .

Post hoc analysis revealed that, compared to MDD-NSI and HCs, MDD-SI exhibited increased EC from the right ACC to the right cerebellar tonsil (NSI: t = 3.38; HCs: t = 3.38). Meanwhile, MDD-SI exhibited decreased EC from the right ACC to the right fusiform gyrus ( t = −3.85; Table 2 and Figure 2b ), compared to MDD-NSI. However, no group differences were found between MDD-NSI and HCs.


## EC from the whole brain to the right ACC

The three groups showed significant differences in the right ventral lateral nucleus of thalamus ( F = 10.71), left inferior parietal lobule (IPL; F = 9.84), right middle frontal gyrus (MFG; F = 9.31), and left ventral posteromedial nucleus of thalamus ( F = 8.77). More details are shown in Table 2 and Supplementary Figure S2C .

Post hoc analysis revealed that, compared to MDD-NSI, MDD-SI exhibited increased EC from the left IPL to the right ACC ( t = 3.08; Table 2 and Figure 2c ).

Compared to HCs, MDD-SI showed increased EC from the right ventral lateral nucleus of thalamus ( t = 4.49), left IPL ( t = 4.37), right MFG ( t = 3.78), and left ventral posteromedial nucleus of thalamus ( t = 4.15) to the right ACC. Compared to HCs, MDD-NSI exhibited increased EC from the right ventral lateral nucleus of thalamus ( t = 3.38) and right MFG ( t = 3.37) to the right ACC.


## Validation analysis

Based on the REST-meta-MDD consortium dataset, we also observed significant differences in ALFF values at the right ACC among the three groups ( F = 9.13). Post hoc analysis revealed that the ALFF values at the right ACC in the MDD-SI were significantly higher than those in the MDD-NSI and HCs (MDD-NSI: t = 2.77 and p Bon = 0.017; HCs: t = 4.14 and p Bon < 0.001), while no significant difference was found between the MDD-NSI and HC groups ( Supplementary Table S1 and Figure 1b ).


## Correlation analysis

Among all brain regions showing differences between MDD-SI and MDD-NSI ( Figure 2d ), we found that decreased FC between the left IFG and the right ACC and decreased EC from the right ACC to the right fusiform gyrus were negatively correlated with the HAMD-suicidality item scores (left IFG: r = −0.26 and p FDR = 0.011; Figure 3a ; right fusiform gyrus: r = −0.28 and p FDR = 0.011; Figure 3b ). The results of other correlation analyses are presented in Supplementary Table S2 . Moreover, no significant associations were found between chlorpromazine (CPZ)/fluphenazine (FLU) equivalents, treatment duration, number of depressive episodes, or illness duration and abnormalities in ALFF, FC, or EC ( Supplementary Table S3 ). Figure 3. The results of the correlation and exploratory analyses. (a) Decreased FC between the left IFG and the right ACC was negatively correlated with the HAMD-suicidality item scores. (b) Decreased EC from the right ACC to the right fusiform gyrus was negatively correlated with the HAMD-suicidality item scores. (c) Progressive increase pattern (HC < MDD-NSI < MDD-SI without SB < MDD-SI with SB) in the EC from the right ACC to the right cerebellar tonsil, and the EC from the left IPL to the right ACC. These represent exploratory trends only and were not subjected to statistical testing due to the limited sample size. Note: MDD-SI, major depressive disorder patients with suicidal ideation; MDD-NSI, major depressive disorder patients without suicidal ideation; SB, suicidal behavior; HC, healthy controls; R, right; L, left; ACC, anterior cingulate cortex; IFG, inferior frontal gyrus; IPL, inferior parietal lobule; FC, functional connectivity; EC, effective connectivity.


> **Figure 3.:** The results of the correlation and exploratory analyses. (a) Decreased FC between the left IFG and the right ACC was negatively correlated with the HAMD-suicidality item scores. (b) Decreased EC from the right ACC to the right fusiform gyrus was negatively correlated with the HAMD-suicidality item scores. (c) Progressive increase pattern (HC < MDD-NSI < MDD-SI without SB < MDD-SI with SB) in the EC from the right ACC to the right cerebellar tonsil, and the EC from the left IPL to the right ACC. These represent exploratory trends only and were not subjected to statistical testing due to the limited sample size. Note: MDD-SI, major depressive disorder patients with suicidal ideation; MDD-NSI, major depressive disorder patients without suicidal ideation; SB, suicidal behavior; HC, healthy controls; R, right; L, left; ACC, anterior cingulate cortex; IFG, inferior frontal gyrus; IPL, inferior parietal lobule; FC, functional connectivity; EC, effective connectivity.


## Exploratory analysis

We observed a progressive increase pattern (HC < MDD-NSI < MDD-SI without SB < MDD-SI with SB; Supplementary Table S4 and Figure 3c ) in the EC from the right ACC to the right cerebellar tonsil and the EC from the left IPL to the right ACC. This is an exploratory trend and was not statistically tested.


## Discussion

Our findings demonstrate that compared to MDD-NSI, (a) MDD-SI showed increased ALFF in the right ACC, validated by the REST-meta-MDD consortium dataset; (b) MDD-SI also exhibited reduced FC between the right ACC and the left IFG and decreased EC from the right ACC to the right fusiform gyrus, which were both negatively correlated with the HAMD-suicidality item scores; and (c) increased EC was observed in MDD-SI from the right ACC to the right cerebellar tonsil and from the left IPL to the right ACC, following a progressive increase pattern (HC < MDD-NSI < MDD-SI without SB < MDD-SI with SB). Sensitivity analyses excluding underage participants yielded results consistent with the primary analyses, ruling out potential confounding effects of developmental factors ( Supplementary Table S5 ).

Our study revealed that both MDD-SI and MDD-NSI showed shared ALFF alterations in the SPG, cerebellum, thalamus, and other regions. These findings are consistent with previous structural network evidence showing disrupted efficiency in these regions in MDD (Chen et al., 2017 ), which are involved in cognitive control and emotion regulation (Chen et al., 2018 ; Rudolph et al., 2023 ; Zhou et al., 2021 ).

Crucially, only the right ACC showed significantly increased ALFF in MDD-SI compared to MDD-NSI, which was further validated by the REST-meta-MDD consortium dataset. These results highlight the central role of the right ACC in SI within MDD, while the other abnormalities may reflect more general depression-related pathophysiology. The ACC is a part of the brain’s limbic system and plays a crucial role in emotional regulation (Bush, Luu, & Posner, 2000 ) and the pathophysiology of MDD (Bora, Fornito, Pantelis, & Yücel, 2012 ). Emotional dysregulation is closely associated with SI (Rogante et al., 2024 ). Therefore, one possible explanation is that the hyperactivation of the ACC in MDD-SI may lead to changes in brain plasticity as compensatory mechanisms (Fears et al., 2015 ) to regulate emotional states (Sublette, Oquendo, & Mann, 2006 ) and mitigate the failures in frontal ‘top-down’ modulation (Strakowski et al., 2012 ). Our findings are consistent with a structural MRI study, which reported that MDD-SI exhibited greater gray matter volume (GMV) in the bilateral ACC compared to MDD-NSI (Yi et al., 2025 ). However, the ACC volume in MDD overall has been found to be reduced relative to HCs (Jiang et al., 2024 ). Additionally, MDD-SI exhibited a decrease in dynamic ALFF in the ACC, suggesting disrupted activity of ACC from a dynamic perspective in MDD-SI (Li et al., 2019 ). Our results extend these prior findings by providing additional evidence for the involvement of the ACC in the pathophysiology of SI in MDD.

Our results of FC and EC based on the right ACC further revealed abnormal connectivity of the right ACC related to SI. Compared to MDD-NSI, MDD-SI showed reduced FC between the right ACC and the left IFG, which were significantly associated with higher suicidal symptom severity. The IFG is critical for impulsivity inhibition and the cognitive process (Bari & Robbins, 2013 ). Previous studies have reported that damage to the left IFG is associated with impaired inhibitory control (Picton et al., 2007 ). Notably, impaired impulse control is significantly associated with SI in individuals with depression (Kim et al., 2023 ). An electroencephalography study found that MDD-SI showed hypoactivity within ACC and IFG compared to depressed controls (Benschop et al., 2019 ). Our results of the reduced FC between the ACC and IFG may indicate a decoupling of frontal and subcortical regions, manifesting as an imbalance between top-down cognitive control and bottom-up emotion generation processes (Pizzagalli, 2011 ), and this may lead to the emergence of SI.

Decreased EC from the right ACC to the right fusiform gyrus was also observed in MDD-SI, which was negatively correlated with the HAMD-suicidality item scores. Consistently, structural MRI studies have revealed reduced GMV in the fusiform gyrus in MDD-SI compared to MDD-NSI (Deng et al., 2025 ). The fusiform gyrus is a critical region for facial expression recognition and is closely associated with processing socially emotional cues (Haxby, Hoffman, & Gobbini, 2002 ). Given this, we hypothesize that the reduced EC from the ACC to the fusiform gyrus may impair the processing of social emotional cues and lead to the misinterpretation of others’ emotional states, potentially exacerbating feelings of loneliness and reinforcing SI (Marzetti, McDaid, & O’Connor, 2022 ; Olié et al., 2015 ).

The ALFF of the right ACC, along with decreased FC between the right ACC and left IFG and decreased EC from the right ACC to the right fusiform gyrus, distinguished MDD-SI from MDD-NSI. Importantly, the ALFF of the right ACC was not significantly correlated with HAMD-suicidality scores, whereas the two ALFF-based connectivity measures were correlated. These findings suggest that ALFF may primarily serve as a group-level state marker, while specific connectivity abnormalities may better reflect the severity of SI.

We also found that MDD-SI exhibited increased EC from the right ACC to the right cerebellar tonsil and from the left IPL to the right ACC compared to MDD-NSI. Exploratory analysis further revealed the progressive increase in these ECs may track the elevated suicide risk, indicated by graded increases across clinical subgroups: HC < MDD-NSI < MDD-SI without SB < MDD-SI with SB. The cerebellum not only plays a key role in motor coordination but also participates in higher-order functions, including cognition and emotional regulation (Allen, Buxton, Wong, & Courchesne, 1997 ; Gao et al., 1996 ; Konarski, McIntyre, Grupp, & Kennedy, 2005 ; Middleton & Strick, 1994 ). MDD-SI individuals often exhibit more severe sleep disturbances, anxiety symptoms, and depressive symptoms compared to MDD-NSI (Fan et al., 2024 ). Research suggests that dysfunction in the ACC-cerebellum circuit may not only predispose individuals to depression but also reflect the severity of the condition (Chen et al., 2025 ). Our result of increased EC from the right ACC to the right cerebellar tonsil in MDD-SI complements previous research and highlights a direction-specific dysconnectivity associated with suicide risk in MDD.

The IPL plays a crucial role in the top-down regulation of attention and emotion (Wang et al., 2024 ) and is also closely associated with rumination (Chen & Yan, 2021 ). The enhanced EC from the IPL to the ACC may make individuals more prone to being drawn to negative emotions and impair attentional disengagement from them (Koster, De Lissnyder, Derakshan, & De Raedt, 2011 ), ultimately increasing the risk of suicide (Law & Tucker, 2018 ). Previous studies have reported reduced FC between the left amygdala and the left IPL in MDD-SI compared to MDD-NSI (Li et al., 2022 ). In our exploratory analysis, we observed that the enhanced EC from the IPL to the ACC in MDD-SI followed a progressive increase across groups with escalating suicidal severity. This emerging pattern suggests that aberrant IPL connectivity – particularly with regions involved in emotional and cognitive control – may serve as a potential biomarker of suicidal vulnerability. It is noteworthy that the progressive patterns identified in the exploratory analysis should be interpreted only as trend-level findings, as statistical testing was not performed due to the very small sample size of the subgroup.

In our study, some differences were observed between the FC and EC results. FC is generally inferred based on the correlation between neuronal activity measurements, reflecting the synchrony or association between different brain regions (Chao-Gan & Yu-Feng, 2010 ). In contrast, EC is estimated using interaction or coupling models to infer potential causal relationships between brain regions (Seth, Barrett, & Barnett, 2015 ). Differences in correlation between two regions do not necessarily indicate changes in their coupling. Additionally, variations in measurement and modeling approaches between the two methods may contribute to the observed differences in connectivity results (Friston, 2011 ). Future research could explore ways to better integrate FC and EC to facilitate a more comprehensive understanding of brain networks.

Our findings suggest that abnormal activation of the ACC, along with disrupted functional and EC based on the ACC, may play a significant role in triggering excessive negative emotions and blunting positive internal states. These abnormal psychological states may further stimulate the emergence of SI. Functional abnormalities in these brain regions (such as the ACC, IFG, fusiform gyrus, cerebellar tonsil, and IPL) may serve as potential targets for future neuromodulation treatments.


## Limitations

It is important to acknowledge several limitations in this study. First, we validated the ALFF findings through the REST-meta-MDD consortium dataset. However, the available large-sample data were confined to ALFF measurements. The lack of raw time-series data prevented the direct replication of the FC and EC findings in an independent cohort. Therefore, the findings of FC and EC need to be validated through large-sample datasets in the future. Second, due to the small sample size of the MDD-SI with the SB group, the exploratory analysis did not conduct a statistical analysis but only briefly explored the trends of EC changes. Therefore, future studies may consider adopting a larger sample of MDD-SI with SB or a longitudinal study design, to further confirm the dysfunction of ACC underlying the transition from SI to SB. Third, the HAMD-suicidality item in the REST-meta-MDD dataset is insufficient for quantitatively assessing SI severity, and HAMD-based grouping in our dataset failed to replicate the main FC and EC findings, although ALFF results were consistent ( Supplementary Table S6 ). Future studies should utilize datasets with structured SI measures for validation. Furthermore, the EC analysis in this study was based on the GCM, which reflects statistical predictability in time series rather than true neurobiological causation. Future studies employing interventional methods, such as transcranial magnetic stimulation, are warranted to validate these directional connectivity patterns.


## Conclusions

In conclusion, this study reveals unique brain activity and connectivity patterns of the ACC associated with SI in MDD. These are characterized by hyperactivity of ACC, hyperconnectivity from IPL to ACC and from ACC to cerebellar tonsil, and hypoconnectivity between ACC and IFG and from ACC to fusiform gyrus. Our findings not only advance the neuropathological understanding of suicide risk but also identify ACC-centered circuits as promising targets for clinical interventions.


## Supporting information

Zhang et al. supplementary material