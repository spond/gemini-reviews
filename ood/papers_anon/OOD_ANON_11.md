# De-Identified Manuscript `OOD_ANON_11`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

This study investigated how resting-state functional connectivity (rsFC) of the subgenual anterior cingulate cortex (sgACC) predicts antidepressant response in patients with major depressive disorder (MDD). Eighty-seven medication-free MDD patients underwent baseline resting-state functional MRI scans. After 12 weeks of escitalopram treatment, patients were classified into remission depression (RD, n = 42) and nonremission depression (NRD, n = 45) groups. We conducted two analyses: a voxel-wise rsFC analysis using sgACC as a seed to identify group differences, and a prediction model based on the sgACC rsFC map to predict treatment efficacy. Haufe transformation was used to interpret the predictive rsFC features. The RD group showed significantly higher rsFC between the sgACC and regions in the fronto-parietal network (FPN), including the bilateral dorsolateral prefrontal cortex (DLPFC) and bilateral inferior parietal lobule (IPL), compared to the NRD group. These sgACC rsFC measures correlated positively with symptom improvement. Baseline sgACC rsFC also significantly predicted treatment response after 12 weeks, with a mean accuracy of 72.64% ( p < 0.001), mean area under the curve of 0.74 ( p < 0.001), mean specificity of 0.82, and mean sensitivity of 0.70 in 10-fold cross-validation. The predictive voxels were mainly within the FPN. The rsFC between the sgACC and FPN is a valuable predictor of antidepressant response in MDD patients. These findings enhance our understanding of the neurobiological mechanisms underlying treatment response and could help inform personalized treatment strategies for MDD.

Subject terms: Depression, Predictive markers


## Introduction

Major depressive disorder (MDD) is currently the second leading cause of disability worldwide [ 1 ], resulting in debilitating symptoms and significant socioeconomic costs. The first-line treatment for MDD is typically antidepressant medication, particularly selective serotonin reuptake inhibitors (SSRIs) [ 2 ]. However, the efficacy of pharmacotherapy for MDD varies between individuals [ 3 ], with ~40–50% of patients not responding to treatment in clinical practice [ 4 ]. Given the urgency to address this issue, efforts have been made to identify treatment-related biomarkers that can better predict the outcome of antidepressant treatment. A meta-analysis of antidepressant response biomarkers has shown that imaging biomarkers have the strongest predictive performance compared to other approaches [ 5 ].

Functional magnetic resonance imaging (fMRI) is a commonly used noninvasive brain imaging technique that can reveal brain abnormalities in MDD [ 6 ]. Recent studies have highlighted the importance of certain brain structures, such as the subgenual anterior cingulate cortex (sgACC), in the pathophysiology of depression and the mechanism of antidepressant treatment. The sgACC, specifically the Brodmann area 25 (BA25), is a key component of the limbic and paralimbic system, which regulates emotional responsiveness and monitors rewarding or punishing outcomes [ 7 ]. Previous research has found impairments in synaptic plasticity in the anterior cingulate cortex of individuals with MDD [ 8 ]. Additionally, hyperactivity of the sgACC has been consistently observed in depression, and its activity tends to decrease after successful treatment [ 9 ]. Resting-state functional connectivity (rsFC) between the sgACC and the prefrontal cortex has been widely studied in the context of repetitive transcranial magnetic stimulation (rTMS) treatment. For instance, responders to rTMS have been found to exhibit a negative rsFC between the dorsolateral prefrontal cortex (DLPFC) and sgACC prior to treatment [ 10 ]. Furthermore, studies have shown that rsFC between an individual’s rTMS cortical target and the sgACC can predict antidepressant response [ 11 – 13 ]. Empirical research has also demonstrated that the DLPFC site with the strongest anticorrelation to the sgACC is the most effective target for optimizing clinical response [ 14 , 15 ]. All of these studies support the notion that rsFC of the sgACC is a significant indicator of treatment outcomes for rTMS. However, the association between rsFC of the sgACC and treatment outcomes of first-line pharmacotherapy remains understudied.

Only a limited number of studies have focused on the association between the functional network of the sgACC and the response to antidepressant pharmacotherapy. For instance, Iseger et al. [ 16 ] observed a decrease in EEG-based connectivity between the sgACC and prefrontal cortex in male responders after eight weeks of pharmacotherapy treatment [ 16 ]. Wang et al. [ 17 ] also found that MEG-based connectivity between the DLPFC and sgACC was associated with a more favorable antidepressant outcome in a real-world study [ 17 ]. These two studies utilized EEG and MEG techniques, which have limited spatial resolutions. Additionally, the patients included in these studies received different medication strategies. In a study using fMRI, Dunlop et al. [ 18 ] discovered that the rsFC of the sgACC was differentially associated with treatment outcomes for cognitive behavior therapy and antidepressant medication [ 18 ]. More recently, a study on late-life depression found that the response to escitalopram is related to functional connectivity in various intrinsic brain networks, including the connection between the sgACC and prefrontal cortex [ 19 ]. All of these studies highlight the association between sgACC connectivity and improvement in response to antidepressant medications. However, no studies have investigated whether pre-treatment rsFC of the sgACC, as measured with fMRI, can independently predict the outcome of antidepressant treatment.

Therefore, the aim of the present prospective longitudinal study is to examine the predictive role of sgACC rsFC in antidepressant response among patients with MDD. Notably, established guidelines recommend escitalopram as a first-line antidepressant for MDD [ 20 ]. Its rapid onset of therapeutic effects distinguishes it from other antidepressants, allowing for a quicker improvement in symptoms [ 21 ]. Moreover, as a SSRI that specifically targets the serotonin (5-HT) pathway, escitalopram aligns well with the neurochemical profile of key limbic regions such as the sgACC [ 22 ]. Furthermore, it is widely recognized that the acute treatment phase of depression typically lasts around 12 weeks. The therapeutic effect during this period is crucial for promoting the recovery of patients’ subsequent social functions and enhancing their quality of life. Therefore, we exclusively used escitalopram as the treatment medication and investigated the predictive role of brain functions on the acute treatment effect of antidepressant medication in our study. We hypothesized that the rsFC of sgACC would be correlated with the treatment response in MDD, and that the baseline rsFC of sgACC might serve as a predictor for the clinical efficacy of the 12 weeks of escitalopram therapy.


## Methods


### Studies

This study was approved by the ethics committee of Beijing Anding Hospital, Capital Medical University, with reference number 2017–24. All methods were performed in accordance with the relevant guidelines and regulations. Prior to analysis, the study design and methods were preregistered at the Chinese Clinical Trial Registry (ChiCTR), under the trial name “Appropriate technology study of MDD diagnosis and treatment based on objective indicators and measurement” with the registration number ChiCTROOC-17012566. All subjects provided written informed consent before participating in the study. The primary objective of this trial was to identify clinical, neuroimaging, neurobiological, and behavioral factors that could influence outcomes to antidepressant medication.


### Patients and treatment

Patients with MDD (n = 110) were recruited and screened from Beijing Anding Hospital, Capital Medical University by psychiatrists from July 2018 to June 2021. These patients were outpatients, aged between 18 and 65 years, with either a first-episode or recurrent MDD. They were either drug-naive or had taken no more than 7 days of antidepressant medication in the 14 days prior to the study. Diagnosis was based on the Mini International Neuropsychiatric Interview (M.I.N.I.) 5.0.0 [ 23 ], a short structured clinical interview following DSM-IV guidelines. Baseline assessment included the 17-item Hamilton Depression Rating Scale (HAMD-17), and only patients with a score ≥ 14 were included in the study. Patients with preexisting or concurrent co-morbid primary diagnoses meeting the DSM-IV criteria for any Axis I disorder other than MDD were excluded. Exclusion criteria also included acute suicidal or homicidal behavior, family history of major psychiatric or neurological illness in first-degree relatives, history of trauma resulting in loss of consciousness, major neurological or physical disorders that could affect mental state, as well as current pregnancy or breastfeeding.

Patients with MDD received treatment with escitalopram for a period of 12 weeks. According to clinical practice guidelines, the dosage of escitalopram was increased from 5 mg/day to 10–20 mg/day within 7 days, and further adjustments between 10–20 mg/day were made by psychiatrists during the 12-week study period [ 24 ]. Patients experiencing insomnia symptoms were permitted to receive additional medications as needed, but no other medications were allowed during the study. Some patients (n = 13) did not complete the full 12-week treatment due to loss of follow-up. Ultimately, a total of 97 patients with MDD underwent MRI scans at pre-treatment and completed the 12-week escitalopram treatment.


### Treatment outcomes

The HAMD-17 was assessed at baseline and after 12 weeks of treatment to measure the primary clinical outcome of remission. Remission was defined as a HAMD-17 score ≤ 7 after 12 weeks. Patients were then divided into subgroups based on whether they achieved remission depression (RD) and nonremission depression (NRD) after 12 weeks. The percent improvement in HAMD-17 was calculated using the formula: (baseline score—week12 score)/baseline score*100.


### Image acquisition

Resting-state fMRI data were acquired using a Siemens Prisma 3.0 Tesla whole-body scanner located at Beijing Anding Hospital, Capital Medical University. Participants were instructed to lie still inside the scanner with their eyes closed, remain awake, and avoid focusing on any specific thoughts. A total of 200 volumes of fMRI images were acquired using an echo-planar imaging sequence with the following parameters: repetition time (TR) = 2000 ms, echo time (TE) = 30 ms, field of view (FOV) = 200 mm × 200 mm, matrix = 64 × 64, flip angle = 90°, number of slices = 33, slice thickness = 3.5 mm, slice spacing = 0.7 mm. Additionally, a sagittal T1-weighted structural scan (TR = 2530 ms, TE = 1.85 ms, matrix = 256 × 256, FOV = 256 mm × 256 mm, slice thickness = 1 mm, flip angle = 9°) was obtained and co-registered with the fMRI data.


### Data preprocessing

Resting-state fMRI data preprocessing was performed using SPM12 (version: 7487; http://www.fil.ion.ucl.ac.uk/spm ) and the Data Processing Assistant for Resting-State fMRI (DPARSFA 4.4, http://www.rfmri.org/DPARSF ) [ 25 ]. The preprocessing steps included deleting the first five-time volumes, correcting for slice timing, correcting for motion, regressing nuisance covariates (which included 24 head motion parameters, the first five principal components of signals from white matter and cerebrospinal fluid, polynomial trend, and head motion scrubbing regressors), normalizing functional images using T1 images, resampling to a resolution of 2 × 2 × 2 mm 3 , smoothing with a 4 mm kernel, and applying band-pass filtering between 0.01 and 0.1 Hz. The mean framewise displacement (FD), which considers measures of voxel-wise differences in motion in its derivation [ 26 ], was used as a measure of micro-head motion for each subject [ 27 ]. Participants with mean FD larger than 3 interquartile ranges from the sample median or less than 100 “good” volumes of data (“good” volume defined as FD threshold ≤ 0.2 mm) were excluded from further analysis. As a result, 10 patients with MDD were excluded based on the head motion control criteria, leaving a total of 87 patients with MDD for subsequent analysis.


### rsFC analysis

We employed a seed-based region of interest approach to calculate rsFC between the sgACC and other brain regions. Existing literature often emphasizes the significance of the right hemisphere when examining sgACC activity in relation to antidepressant efficacy. For example, Fox et al. [ 11 ] reviewed prior research and observed that treatment frequently resulted in decreased activity in the right sgACC [ 11 ]. Studies on TMS targets for depression have also linked treatment efficacy to intrinsic functional connectivity of the right sgACC [ 11 , 12 ]. Similarly, studies using EEG/MEG have focused on the right sgACC seed, indicating its relevance to antidepressant response [ 16 , 17 ]. Hence, our primary focus was on the right sgACC. The MNI coordinate of the right sgACC (5, 25, −10), which was derived from previous studies [ 7 , 28 ], was represented by a sphere with a radius of 4 mm. Additionally, as an exploratory measure, we also examined the rsFC of the left sgACC (−5, 25, −10) using the same methodology. The seed-based rsFC analysis of the sgACC was performed by averaging the time series of all voxels within the seed region to obtain the mean time series of the seed region. Pearson’s correlation coefficients were then computed between the mean time series of each seed region and the time series of each voxel in the entire brain. To improve their normality for group-level analyses, the correlation coefficients were converted into z-values using Fisher’s r -to- z transformation.


### The efficacy prediction model

To determine if baseline voxel-wise rsFC of the sgACC can effectively predict the response to escitalopram treatment after 12 weeks, we constructed a logistic regression model with an L2 penalty term. The prediction model was implemented using the scikit-learn package in Python 3.10.6. The rsFC data, particularly voxel-wise connectivity strength, contains a large number of features. This high dimensionality of the data can lead to the “dimensionality curse” [ 29 ], which may negatively impact the performance of the model. The dimensionality curse occurs when the number of observations is much smaller than the number of features, resulting in decreased accuracy in capturing the association between features and the target variable. This imbalance can also lead to model instability, making it difficult to accurately assess the association between rsFC features and treatment efficacy. To address these challenges, it is necessary to reduce the dimensionality of the data whereas retaining relevant information. In our study, Principal Component Analysis (PCA), a well-established technique in previous studies [ 30 – 32 ], was used to decrease the dimensionality of the rsFC data. PCA helps to eliminate redundant information whereas preserving important details. Model performance was evaluated using 10-fold cross-validation, and the optimal model parameters were determined based on the average prediction accuracy. In each fold, the training data underwent PCA dimensionality reduction, and the resulting linear transformation was applied to the test data before inputting it into the logistic regression model for prediction. The prediction performance was characterized by receiver operating characteristic (ROC) curves. Additionally, the area under the curve (AUC), sensitivity, and specificity were calculated to comprehensively assess the model performance.


### Model interpretation

After obtaining a reliable prediction model, the model was interpreted to identify the predictive rsFC features. For this purpose, the Haufe transformation was employed to determine the importance of features in the efficacy prediction [ 33 ]. In the Haufe transformation, the covariance between the voxel rsFC and the model outcome is calculated to indicate the contribution of each voxel signal to the prediction result. The Haufe transformation effectively reduces the potential impact of noise signals on model interpretation, particularly in the context of fMRI signals [ 34 ]. In this study, the top 1% voxels with the highest Haufe scores were identified as predictive features that significantly contribute to the model prediction. Subsequently, the K-means algorithm was applied to the predictive voxels (whereas non-predictive voxels were set to 0) to explore potential clustering of the predictive rsFC. Mean squared errors were calculated for different cluster numbers, and the elbow method was employed to determine the optimal cluster number. The analysis script was implemented using Python 3.10.6, with the K-means clustering algorithm implemented with reference to the scikit-learn package.


### Statistical analyses

The demographic and clinical characteristics of the participants were analyzed using SPSS 22.0. Student’s t -test was utilized to compare age, illness duration, number of episodes, HAMD-17 score, and percentage improvement of HAMD-17 between the RD and NRD groups. The Chi-square test was used to analyze sex, education level, and type of episode.

Regarding the rsFC analysis, the z -values were initially subjected to two-sample t -tests to identify brain regions exhibiting significant differences in connectivity with each seed region between the RD group and NRD group. Sex, education level, age, and mean FD were included as covariates. The statistical threshold was set at voxel-wise p < 0.001, in conjunction with a cluster-wise FWE p < 0.05, to correct for multiple comparisons. Subsequently, Pearson correlation analysis was conducted within the MDD group to explore the association between the strength of the baseline rsFC of the sgACC, which showed group differences, and the percentage improvement of HAMD-17 score, reflecting treatment efficacy. Finally, the statistical effect of the prediction model was evaluated using a permutation test. The permutation was performed 1000 times, and the statistical effect p was calculated as the ratio of the empirical performance compared to the permuted result. The level of statistical significance was set at p < 0.05 for all tests.


## Results


### Demographic and clinical characteristics

Table 1 presents the demographic and clinical characteristics of patients in the RD and NRD groups. The results indicate that there were no significant differences between the groups in terms of age, sex, education status, illness duration, type of episode, number of episodes, and baseline HAMD-17 score ( ps ≥ 0.05). However, there were significant differences between the RD and NRD groups in terms of HAMD-17 score at 12 weeks and the percent improvement of HAMD-17 ( ps < 0.001).


#### Table 1.

Demographic and clinical characteristics of patients in the RD and NRD groups.



| Characteristics | RD (n = 42) | NRD (n = 45) | t/χ 2 | p |
| --- | --- | --- | --- | --- |
| Age(years) | 27.14 ± 5.84 | 27.00 ± 6.86 | 0.10 | 0.917 |
| Sex(male/female) | 16/26 | 12/33 | 1.30 | 0.254 |
| Education status |  |  | 1.49 | 0.475 |
| High school/college | 8 | 7 |  |  |
| Undergraduate | 26 | 33 |  |  |
| Postgraduate or above | 8 | 5 |  |  |
| Illness duration(months) | 27.45 ± 33.72 | 45.67 ± 67.78 | −1.60 | 0.114 |
| Type of episode(first-episode/recurrent) | 25/17 | 31/14 | 0.83 | 0.381 |
| Number of episodes | 1.67 ± 1.12 | 1.80 ± 1.84 | −0.41 | 0.687 |
| HAMD-17(baseline) | 19.86 ± 3.71 | 21.53 ± 4.13 | −1.99 | 0.050 |
| HAMD-17(week12) | 4.38 ± 2.10 | 13.40 ± 4.47 | −12.18 | <0.001 |
| HAMD-17(percent improvement) | 77.09 ± 11.49 | 35.97 ± 24.19 | 10.23 | <0.001 |


RD remission depression, NRD nonremission depression, HAMD-17 17-item Hamilton Depression Rating Scale.


### rsFC analysis between RD and NRD

Upon comparing the rsFC patterns between the two groups, we observed that the RD group exhibited increased rsFC between the right sgACC and the bilateral DLPFC as well as the bilateral inferior parietal lobule (IPL) ( p < 0.05, FWE-corrected), in comparison to the NRD group (Fig. 1 and Table 2 ). There were no significant differences in the rsFC of the left sgACC between the RD and NRD groups; therefore, further analysis was not conducted for the left sgACC.


#### Fig. 1. Results of rsFC analysis between RD and NRD.


> **Figure/Table Caption:** Brain regions (left panel) and bar graphs (right panel) showing significant differences for the rsFC of the right sgACC between patients in the RD and NRD groups. RD remission depression, NRD nonremission depression, DLPFC dorsolateral prefrontal cortex, IPL inferior parietal lobule.


#### Table 2.

Clusters differentiating RD and NRD.



| Region | Peak MNI Coordinates (x, y, z) | Cluster Size (2-mm voxels) | T | p |
| --- | --- | --- | --- | --- |
| Left DLPFC | −34 34 14 | 199 | 4.13 | 0.007 |
| Right DLPFC | 40 34 14 | 285 | 4.31 | 0.001 |
| Left IPL | −44 −46 46 | 459 | 4.64 | <0.001 |
| Right IPL | 50 −38 42 | 578 | 4.92 | <0.001 |


RD remission depression, NRD nonremission depression, MNI Montreal Neurological Institute, DLPFC dorsolateral prefrontal cortex, IPL inferior parietal lobule.


### Correlations between rsFC and percent improvement of HAMD-17

Pearson correlation analyses revealed positive correlations between rsFC of the sgACC and the left DLPFC ( r = 0.321, p = 0.002), the right DLPFC ( r = 0.376, p < 0.001), the left IPL ( r = 0.453, p < 0.001), and the right IPL ( r = 0.428, p < 0.001) with the percent improvement of HAMD-17 in patients with MDD. These results are displayed in Fig. 2 .


#### Fig. 2. Results of Pearson correlation analyses.


> **Figure/Table Caption:** Scatter plots showing positive correlations between the percent improvement of HAMD-17 scores and rsFC of the sgACC with the bilateral DLPFC and the bilateral IPL separately. HAMD-17 17-item Hamilton Depression Rating Scale, DLPFC dorsolateral prefrontal cortex, IPL inferior parietal lobule.


### The predictive model based on baseline rsFC

A logistic regression model with L2 penalty terms was used to predict the treatment outcomes of patients with MDD. The 10-fold cross-validation demonstrated that baseline rsFC could significantly predict the treatment effect of escitalopram, with an average accuracy of 72.64% ( p < 0.001). Figure 3 shows that the average AUC value for treatment outcome prediction was 0.74 ( p < 0.001), with a standard deviation of 0.21. The mean sensitivity value for the cross-validation was 0.70 and the mean specificity value was 0.82. The ROC curve displayed that the baseline rsFC could effectively predict the efficacy of escitalopram for MDD treatment through a linear model in the majority of the cross-validation folds.


#### Fig. 3. Result of the efficacy prediction model analysis.


> **Figure/Table Caption:** Mean ROC curves over 10 folds for predicting the escitalopram treatment outcomes. ROC receiver operating characteristic.


### The predictive features in the prediction model

The predictive features in the prediction model were selected based on the top 1% of voxels with the highest Haufe scores. To examine the clustering patterns of these predictive features, the K-means algorithm was utilized. According to the elbow method, the optimal number of clusters was determined to be 3. Thus, the whole-brain rsFC voxels were divided into three K-means clusters: cluster 0 (144705 unpredictive voxels), cluster 1 (1005 voxels), and cluster 2 (362 voxels). Interestingly, a high percentage of voxels, specifically 832 out of 1005 (overlap rate of 82.78%), in cluster 1 were overlapped with the voxels found to differentiate the RD and NRD groups. Conversely, cluster 2 seemed to contain the remaining sporadic predictive voxels. As depicted in Fig. 4 , there was a strong overlap between the predictive voxels identified in the logistic regression model and the regions identified in the rsFC analysis of group differences. The majority of predictive voxels were located in the fronto-parietal network (FPN) according to the study of Yeo et al. [ 35 ]


#### Fig. 4. The association between predictive features and ROIs differentiating RD and NRD groups.


> **Figure/Table Caption:** A The surface mapping visualization presents the K-means clusters 1 and 2 based on the predictive features. B The surface mapping visualization shows the 4 ROIs identified in the between-group comparation analysis of the sgACC rsFC. C The surface mapping visualization presents the K-means clusters, the ROIs obtained from the between-group comparation analysis of the sgACC rsFC, and the FPN brain network from Yeo et al. [ 35 ]. D The Venn diagram illustrates a substantial overlap between the predictive voxels (n = 832) in K-means cluster 1 and the ROIs obtained from the between-group comparation analysis of the sgACC rsFC. E The bar plot describes that the distribution of the cluster voxels across different functional networks and the majority of identified important voxels clearly locate in the FPN. RD remission depression, NRD nonremission depression, ROI region of interest, FPN fronto-parietal network.


## Discussion

The current study focused on the baseline rsFC of the sgACC and its role in predicting the efficacy of escitalopram treatment after 12 weeks. Utilizing an L2 regularized logistic regression model, we observed a significant prediction (mean accuracy of 72.64%, p < 0.001, mean AUC of 0.74, p < 0.001, mean specificity of 0.82 and mean sensitivity of 0.70 in 10-fold cross-validation) in a relatively young MDD sample with a mean age of 27. Importantly, the predictive voxels in the model exhibited substantial overlap with the FPN regions identified in the between-group comparison of sgACC rsFC, namely, bilateral DLPFC and IPL (82.78% overlap rate). Patients with higher rsFC in these regions were more likely to experience improvement with escitalopram treatment, whereas lower rsFC (or negative connectivity) suggested that escitalopram might not be the optimal choice. These findings suggest that sgACC-FPN rsFC has the potential to serve as a predictor of escitalopram treatment efficacy after 12 weeks.

Our study revealed that individuals in the RD group showed higher rsFC between the sgACC, DLPFC, and IPL compared to those in the NRD group. These regions, namely the DLPFC and IPL, are part of the FPN, which plays a crucial role in top-down regulation of attention and emotion. The FPN is essential for effectively coordinating our behavior in a quick, accurate, and flexible manner [ 36 ]. Previous research has suggested that the FPN is implicated in the pathophysiology of depression [ 37 ]. In a meta-analysis of rsFC studies, Kaiser et al. [ 37 ] investigated network dysfunction in MDD and found that MDD is characterized by reduced connectivity within the FPN and altered connectivity between the cognitive processing within the FPN and those regions supporting salience or emotion processing [ 37 ]. Additionally, several studies have highlighted the association between the function of the FPN and clinical response to antidepressant treatment. In their study involving elderly depressed patients, Alexopoulos et al. [ 38 ] discovered that lower rsFC within the FPN predicted a lower remission rate and persistence of depressive symptoms after treatment with escitalopram [ 38 ]. Chin Fatt et al. [ 39 ] observed that the prediction of response to sertraline involved higher rsFC between the FPN and the default mode network, as well as higher rsFC within the default mode network [ 39 ]. Another recent study reported that antidepressant response in late-life depression is associated with connectivity in the FPN, default mode network, and limbic networks [ 19 ]. With regard to the specific regional connectivity of the sgACC, a previous study demonstrated that alpha band sgACC-DLPFC EEG connectivity decreased after antidepressant treatment [ 16 ]. Wang et al. [ 17 ] found that the alpha band MEG connectivity between the DLPFC and sgACC at baseline was associated with the final efficacy of antidepressant medication, indicating that higher connectivity was associated with a more favorable prognosis [ 17 ]. Our current findings align with these previous studies on antidepressant treatment response in individuals with MDD and further suggest that rsFC of the sgACC during fMRI can independently predict the outcome of antidepressant treatment. Specifically, hyperconnectivity between the sgACC and the DLPFC and IPL within the FPN is more likely to lead to improvement with escitalopram treatment.

Interestingly, our findings seem mutually complementary with previous rTMS studies that have found negative functional connectivity between the prefrontal stimulation site and the sgACC to be associated with better treatment outcomes. For example, one study found that patients who responded well to high frequency rTMS treatment had stronger negative connectivity between the sgACC and the frontal gyrus at the start of treatment. This negative correlation was reversed after successful treatment [ 40 ]. Another study found that DLPFC stimulation sites with better clinical efficacy were more negatively correlated with the sgACC [ 11 ]. Retrospective studies have also shown that patients who were treated closer to personalized functional connectivity-guided targets had significantly better clinical response to rTMS [ 41 , 42 ]. Recent prospective randomized clinical trials have further confirmed the antidepressant effect of rTMS based on fMRI-guided targeting, where the region of the left DLPFC that was most anticorrelated with the sgACC in each individual was stimulated [ 14 , 15 ]. However, it is important to note that these results cannot be directly compared to results of antidepressant medication studies, as different intervention methods were used. The neurobiological mechanisms underlying the efficacy of antidepressant drugs and neuromodulation treatments are significantly different. Based on our findings and previous rTMS studies, we speculate that the functional connectivity between the sgACC and fronto-parietal regions is correlated with individual differences in treatment outcomes and can guide different treatment strategies. Specifically, it appears that higher rsFC of the sgACC at baseline is more likely to lead to improvement with antidepressants, whereas lower rsFC (i.e., stronger negative correlation) of the sgACC at baseline is more likely to lead to improvement with rTMS in the DLPFC sites. However, these speculations need to be validated in future large-scale clinical studies. Through further exploration, we hope that researchers can develop better personalized treatment strategies for patients with MDD based on the functional topography of the sgACC.


### Limitations

There are several limitations that should be acknowledged in the current work. Firstly, whereas the current study achieved a high level of discriminative power, it is important to verify whether the prediction model can maintain its performance on a larger dataset or across multiple sites. Further investigation is needed to assess the generalizability of the findings. Secondly, the findings were obtained from patients with MDD who were treated solely with escitalopram. This raises questions about the specificity of the identified rsFC markers to this particular medication. It is unclear whether these markers are exclusive to escitalopram treatment or if they can be used as generic predictors of outcomes that could be seen with alternative interventions such as placebo, psychotherapy, or other depressive treatments. Patients receiving different treatments may exhibit different or similar results, highlighting the need for further exploration into the predictive value of sgACC rsFC across different treatment modalities for symptom improvement. Thirdly, the assessment of anxiety symptoms and prior treatments was not included in this study. Future studies should explore and verify whether anxiety symptoms and prior treatments could influence the findings. Additionally, as part of our study design, outpatient participants self-reported their medication status, lacking robust objective adherence monitoring mechanisms. This limitation highlights the challenge of fully guaranteeing adherence levels among participants. Stringent criteria were applied in this study to exclude individuals intolerant or unresponsive to escitalopram, as well as those deviating from monotherapy guidelines or experiencing severe adverse effects during treatment. These screening measures likely contribute to the higher remission rate observed in this study compared to conventional clinical observations. Lastly, it is worth considering that a combination of multiple indicators, including clinical, electrophysiological, neurocognitive, and neuroimaging measures, may enhance the sensitivity and robustness of predicting the effectiveness of antidepressant treatment [ 43 ]. Future studies can incorporate a broader range of measures to gain a more comprehensive understanding of individual response to treatment.

In conclusion, this study is the first to investigate the predictive role of sgACC rsFC in the treatment response of escitalopram among patients with MDD. Our findings indicate that a higher rsFC between the sgACC and the regions within the FPN, specifically the bilateral DLPFC and bilateral IPL, is associated with clinical improvement after 12 weeks of escitalopram treatment. Importantly, using machine learning techniques, we have shown that the baseline rsFC can effectively predict the effectiveness of escitalopram in treating depression, with a significant contribution from the rsFC between the sgACC and the FPN regions. These findings provide insights into the neurobiological mechanisms underlying antidepressant response and suggest that the rsFC between the sgACC and FPN could potentially serve as a neurobiological marker to predict the efficacy of escitalopram treatment in MDD. This offers valuable insights for guiding precise and personalized treatment approaches.



YW, YZ and GW conceived and designed the study. YW, JZ, XC, RL, ZZ, YF, LF and JL collected the data. YW and CW analyzed the data. YW and CW drafted the manuscript. YW, GW and YZ revised the draft.


## Funding

This research was supported by STI2030-Major Projects (2021ZD0200600), National Natural Science Foundation of China (82101597, 82071531), and Beijing Hospitals Authority Youth Programme (QML20231901).


## Data availability

Data is available on request from the corresponding author.


## Competing interests

The authors declare no competing interest.


## Footnotes

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.



## Contributor Information

Yuan Zhou, Email: [EMAIL_REDACTED].

Gang Wang, Email: [EMAIL_REDACTED].

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Data Availability Statement

Data is available on request from the corresponding author.
