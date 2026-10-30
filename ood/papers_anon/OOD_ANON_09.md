# De-Identified Manuscript `OOD_ANON_09`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract


### Background

Sleep disorders are common among adolescents with depression, yet lack reliable neuroimaging diagnostic techniques. This study aimed to predict sleep disorders in depressed adolescents using brain network features, including betweenness centrality (BC) and functional connectivity (FC).


### Methods

117 adolescents diagnosed with depression underwent resting-state fMRI. Whole-brain FC (reflecting inter-regional relationships) and BC (quantifying a node’s importance for network information flow) were analyzed. Differences in FC and BC between depressed adolescents with sleep disorders and depressed adolescents without sleep disorders were compared using two-sample t -tests in a discovery dataset ( n = 86). A support vector machine (SVM) classifier was trained to differentiate these groups. Validation employed leave-one-out cross-validation (LOOCV) internally and an independent dataset ( n = 31).


### Results

Depressed adolescents with sleep disorders showed elevated BC in the right middle temporal gyrus (MTG.R) and decreased BC in the left median cingulate and paracingulate gyri (DCG.L) and left caudate nucleus (CAU.L), indicating altered information flow hubs. Alterations in FC were observed across several regions, with the most pronounced changes occurring between the left middle occipital gyrus and MTG.R (MOG.L-MTG.R). The SVM model, using combined whole-brain BC and FC features, achieved 81.40% accuracy during LOOCV and identified discriminative features. Predictive performance was validated externally, yielding 74.19% accuracy.


### Conclusions

Significant functional brain network alterations occur in depressed adolescents with sleep disorders. Integrating brain network analysis(BC and FC analysis) with machine learning techniques offers a promising approach to identifying neuroimaging markers for diagnosing sleep disorders in depressed adolescents.


### Supplementary Information

The online version contains supplementary material available at [REDACTED_DOI].

Keywords: Adolescent, Depression, Functional connectivity, Betweenness centrality, Support vector machine


## Introduction

Adolescence, a neurodevelopmental stage marked by accelerated physical and cognitive maturation, paradoxically coincides with elevated risk for depression and sleep disorders [ 1 ]. Depression is a chronic and debilitating mood disorder marked by anhedonia and significant impairments in daily functioning [ 2 , 3 ]. The incidence of depression has increased among children and adolescents in recent years, with its escalating prevalence and associated suicide rates, presenting a major global mental health challenge [ 4 ].

Sleep disorders are highly prevalent in adolescent depression, affecting approximately 83.1% of affected individuals, with characteristic manifestations including sleep initiation/maintenance difficulties, poor sleep quality, and circadian rhythm disruptions [ 5 ]. Notably, sleep-impaired depressed adolescents demonstrate distinct clinical profiles, typically presenting with more severe depressive symptoms and heightened suicide risk [ 1 , 6 , 7 ]. Currently, the diagnosis of sleep disorders in adolescent depressed patients predominantly depends on subjective self-reports, which frequently differ significantly from objective sleep assessments [ 8 , 9 ]. While polysomnography remains the gold standard for sleep architecture assessment, its clinical utility is limited by procedural complexity—a particular challenge in China’s high-volume adolescent outpatient settings [ 1 , 10 ]. This underscores the pressing need for developing an accurate, efficient, and scalable objective measure to improve early detection and clinical management of sleep disorders in this vulnerable population [ 7 , 11 ].

In recent years, resting-state functional MRI (rs-fMRI) has become a valuable tool for exploring the neural mechanisms underlying both sleep disorders and depression, thereby enhancing our understanding of their neurobiological relationship [ 12 ]. Given the inherent complexity of brain organization, contemporary research predominantly conceptualizes the brain as an interconnected resting-state network system. The construction of functional connectivity (FC) networks through temporal Pearson correlation analysis of interregional blood oxygen level-dependent (BOLD) signals has become a well-established methodology in MDD research [ 13 , 14 ]. Previous studies have reported altered FC in patients with depression and sleep disorders [ 14 – 17 ]. A recent meta-analysis revealed that both increased and decreased FC within the default mode network (DMN), along with enhanced FC between the DMN and the frontoparietal network, as well as aberrant FC between the ventral and dorsal attention networks, may constitute the neurobiological basis of depression [ 17 ]. These alterations manifest as heightened self-referential processing, enhanced executive control, and impaired sensorimotor integration [ 17 ]. These resting-state networks, particularly the DMN, are also closely associated with sleep disorders [ 18 ]. Furthermore, a study utilizing data from the Human Connectome Project involving mixed samples of healthy controls and individuals with psychiatric conditions demonstrated that FC among the hippocampus, amygdala, temporal cortex, and precuneus mediates the relationship between depressive symptoms and impaired sleep quality [ 19 ]. These findings suggest that abnormal FC patterns may constitute the neuropathological basis of comorbid depression and sleep disorders in adolescents, potentially serving as neuroimaging biomarkers for identifying sleep disorders in youth with depression.

However, traditional FC analyses have primarily focused on pairwise regional comparisons while overlooking the integrative properties of whole-brain network organization [ 20 ]. This limitation has prompted the widespread adoption of graph theory approaches in neuroimaging research, which reveal the fundamental topological architecture of human functional networks and demonstrate particular sensitivity to psychiatric disease progression [ 20 – 22 ]. Betweenness centrality (BC), a key topological attribute, quantifies a node’s role as a network mediator by summing its occurrence on all shortest paths between node pairs, normalized by the total number of such paths. Nodes with high BC are typically regarded as critical network hubs in functional brain networks. These “hub” nodes play pivotal roles in whole-brain information integrations [ 23 ]. Compared to other network topological attributes, BC has been widely used in adolescent research due to its high stability across age groups [ 24 ]. While BC applications in sleep research remain limited, Lu et al.‘s seminal work identified a positive correlation between right putamen BC and sleep disturbance severity, highlighting this hub’s mechanistic importance [ 25 ]. Building on these findings, our study innovatively combines FC and BC analyses to investigate the neural substrates of sleep disorders in adolescent depression.

Previous studies on FC and network topological properties in depression and sleep disorders primarily focused on brain region differences between case and control groups. However, these studies provide limited clinical implications for diagnosis and treatment. Machine learning (ML), a powerful data analysis tool, has proven valuable in diagnosing and predicting the prognosis of mental illnesses by uncovering complex relationships between neuroimaging data and psychiatric symptoms [ 26 ]. Notably, the Support Vector Machine (SVM) model, widely used in medical applications, excels in classification accuracy and its capacity to manage high-dimensional data [ 27 ]. For example, in a study on adolescent depression, Hong et al. employed regional volumes and cortical thickness as features, using an SVM model to predict suicide risk with an accuracy of 78.59% [ 28 ]. Gong et al. conducted a relatively rare study utilizing FC as a feature to predict sleep disorders, achieving an accuracy of 76.92% with an SVM model [ 29 ]. Current ML studies based on resting-state brain networks have demonstrated promising results in depression and sleep disorder populations [ 29 , 30 ]. However, these investigations have been largely limited to examining single network features (e.g., using either FC or topological attributes alone). Notably, Wang et al.‘s recent study [ 31 ] achieved superior performance in schizophrenia classification by developing an SVM model that integrated both FC and topological attributes, significantly outperforming previous diagnostic models relying on single network features. These findings strongly suggest that multi-feature fusion of resting-state network features can substantially enhance the classification performance of ML models in psychiatric disorders.

To the best of our knowledge, no study has simultaneously incorporated both network topology attributes and FC as features in a machine learning model to predict sleep disorders in adolescent patients with depression. Therefore, this study extracted whole-brain network topology features and FC from rs-fMRI data of 86 adolescent patients with depression, constructing an SVM classification model to predict the presence of sleep disorders. The model’s performance was then externally validated using an independent dataset of 31 patients. Here, we propose the following hypotheses: (1) Adolescents with depression and comorbid sleep disorders will exhibit significant differences in both BC and FC compared to those without sleep disturbances, suggesting that these altered network features may represent the neurobiological basis of sleep disorders in depressed youth; (2) The SVM model integrating both BC and FC features will demonstrate superior classification accuracy in distinguishing between these adolescent depression subgroups compared to models using either feature type alone; (3) The most discriminative features contributing to SVM classification performance will overlap with the between-group differences identified in hypothesis (1), potentially serving as key neuroimaging biomarkers for sleep disorders in adolescent depression.


## Materials and methods


### Participants

A total of 117 adolescents with depression were recruited from the inpatient population of the Department of Children and Adolescents at Fourth People’s Hospital in Hefei. The inclusion criteria were as follows: (1) participants aged 12 to 18 years; (2) right-handed individuals; (3) individuals meeting the ICD-10 criteria for a depressive episode or recurrent depressive disorder, as independently confirmed by two experienced psychiatrists. Exclusion criteria included: (1) a documented history of drug or alcohol abuse; (2) a diagnosis of other psychiatric disorders, such as bipolar disorder or schizophrenia; (3) documented history of traumatic brain injury or major medical conditions (e.g., cardiovascular diseases); (4) the presence of metal implants, which would preclude MRI examination; and (5) refusal of MRI examination by participants or their legal guardians.

Of the total participants, 86 were recruited between June 2022 and June 2024 and assigned to the discovery dataset for model training and validation. The remaining 31 participants, recruited between June 2024 and October 2024, were assigned to the independent validation dataset for model testing (Fig. 1 ).


#### Fig. 1.


> **Figure/Table Caption:** Workflow chart for patient recruitment and quality control

The study was approved by the Ethics Committee of Fourth People’s Hospital in Hefei (HFSY-IRB-YJ-LWTG-XL (2024-077-001)) and conducted in accordance with the Declaration of Helsinki. Written informed consent was obtained from each participant and their guardian.


### Measures

The 24-item Hamilton Depression Rating Scale (HAMD) was used to assess depressive symptoms in adolescents diagnosed with depression, where higher scores indicate greater severity of symptoms [ 32 ]. The HAMD has demonstrated robust reliability and validity within the Chinese population [ 33 ].

Sleep quality in adolescents with depression was evaluated using the Chinese adaptation of the Pittsburgh Sleep Quality Index (PSQI), which assesses seven domains: overall sleep quality, sleep onset latency, total sleep duration, sleep efficiency, sleep disturbances, use of sleep medications, and daytime functioning. Each domain is scored from 0 to 3, with a maximum possible score of 21, where higher scores reflect poorer sleep quality [ 34 ]. In this study, adolescents with PSQI scores ≥ 11 were classified as having depression with sleep disorders [ 35 ].

In the discovery dataset, 44 participants were assigned to the adolescent depression with sleep disorder group, while 42 participants were assigned to the adolescent depression without sleep disorder group (Fig. 1 ).


### MRI data acquisition

All resting-state MRI data were acquired on a 3.0-Tesla General Electric Discovery MR750w scanner. Earplugs were provided to reduce noise exposure. Participants were instructed to remain still, relaxed, and awake during the scan. High-resolution 3D T1-weighted structural images were obtained using a brain volume (BRAVO) sequence with the following parameters: repetition time (TR) = 8.5 ms; echo time (TE) = 3.2 ms; inversion time (TI) = 450 ms; flip angle (FA) = 12°; field of view (FOV) = 256 mm × 256 mm; matrix = 256 × 256; slice thickness = 1 mm, no gap; 188 sagittal slices; acquisition time = 296 s. Resting-state BOLD images were acquired using a gradient-echo single-echo planar imaging (GRE-SS-EPI) sequence with these parameters: TR = 2000 ms; TE = 3.2 ms; FA = 90°; FOV = 220 mm × 220 mm; matrix = 64 × 64; slice thickness = 3 mm, slice gap = 1 mm; 35 interleaved axial slices; 185 volumes; acquisition time = 370 s. Post-scan quality control included a review of all brain MRI images to assess imaging quality and identify incidental brain abnormalities.


### MRI data preprocessing and analysis

Resting-state fMRI data were preprocessed using Statistical Parametric Mapping software (SPM12, http://www.fil.ion.ucl.ac.uk/spm ) and Data Processing & Analysis for Brain Imaging (DPABI, http://rfmri.org/ dpabi) [ 36 ]. The first 10 volumes of each participant were discarded to allow the signal to reach equilibrium and enable adaptation to scanning noise. The remaining volumes were corrected for slice acquisition time delay. Realignment was then applied to correct for motion between time points. Head motion parameters were computed by estimating translational and rotational movement in each direction for each volume. All participants’ data met the motion threshold criteria, with translational and rotational motion parameters < 3 mm or 3°. Additionally, frame-wise displacement (FD), which indexes volume-to-volume changes in head position, was calculated. Several nuisance covariates, including linear drift, estimated motion parameters based on the Friston-24 model, volumes with FD > 0.5 mm, global signal, white matter signal, and cerebrospinal fluid signal, were regressed out. During normalization, individual structural images were first co-registered with the mean functional images. The transformed structural images were then segmented and normalized to MNI space using a high-order nonlinear warping algorithm, specifically the diffeomorphic anatomical registration through exponentiated Lie algebra (DARTEL) technique [ 37 ]. Each filtered functional volume was subsequently spatially normalized to MNI space using the deformation parameters from the earlier step and resampled to 3-mm isotropic voxels. Finally, the datasets were bandpass filtered within a frequency range of 0.01–0.1 Hz and linearly detrended.


### FC and network topological attribute analysis

The FC analysis employed a data-driven, whole-brain approach to construct the network. Ninety brain regions from the Automated Anatomical Labelling atlas (AAL) atlas were designated as regions of interest (ROIs), and Pearson correlation analysis was conducted between ROIs for each patient to compute FC and generate correlation coefficients between the preprocessed fMRI time series of each ROI and all other ROIs, resulting in a 90 × 89 network connectivity matrix for each patient [ 38 , 39 ]. Fisher’s Z -transformation was applied to the connectivity matrices to normalize the data for subsequent analysis.

Based on the FC matrices, we computed the topological attributes using the GRETNA toolbox [ 40 ]. Specifically, BC quantifies the fraction of all shortest paths passing through a given node, reflecting its influence on information flow control within the network. To ensure meaningful network connections and validate small-world properties, we employed a sparsity threshold ( S ) approach [ 41 ]. Sparsity ( S ) is defined as the ratio of the number of existing edges to the maximum possible edges in the network [ 42 ]. Using this approach, individual brain networks (constructed from correlation matrices of 90 regions) were binarized into adjacency matrices, retaining only significant connections, where an edge was preserved if its absolute correlation coefficient exceeded a subject-specific threshold [ 42 ]. This method standardizes network structure across individuals by enforcing identical node counts and edge densities, thereby mitigating confounding effects from inter-subject differences in overall correlation strength and focusing the analysis on relative network organization differences. The sparsity threshold range was selected such that all individual networks satisfied the criterion of small-worldness (σ > 1.1) [ 42 , 43 ]. Ultimately, the sparsity threshold was systematically varied from 6 to 34% in increments of 1%. For each resulting thresholded network, the BC of each node was computed. Subsequently, for each node, we calculated the Area Under the Curve (AUC) of its BC values across the entire sparsity range (6%−34%) [ 42 ]. This AUC metric, derived by integrating the nodal BC values over the threshold spectrum, provides a comprehensive scalar characterization of the brain network’s topological organization and was employed in all subsequent analyses [ 41 , 42 , 44 , 45 ].


### Statistical analysis

Demographic and scale data for all patients were analyzed using SPSS version 23.0. Chi-square tests assessed differences in gender ratios between the adolescent depression with sleep disorder group and the group without sleep disorder, while two-sample t -tests were used to compare age, education, illness duration, HAMD scores, and PSQI scores, with a significance threshold set at p < 0.05.

FC and BC between the two groups were analyzed using two-sample t -tests with the GRETNA toolbox. Covariates, including sex, age, disease duration, head movement, and HAMD score, were incorporated after a collinearity test. Bonferroni correction was applied for multiple comparisons, with a p -value < 0.05 considered statistically significant. Pearson’s correlation analysis explored the relationship between altered FC and BC, and PSQI scores, with a significance threshold of p < 0.05. Bonferroni correction was applied to the results of Pearson correlation analyses. For the 12 statistical tests performed, comprising correlations between regional BC values from 3 brain areas and PSQI total scores, and between 9 FC connections and PSQI total scores, the original significance threshold (α = 0.05) was adjusted to 0.0042. Results were considered statistically significant only if the corrected p -value was less than 0.0042.


### Support vector machine-based machine learning analysis

In this study, SVM model construction and validation were performed on fMRI data using the LIBSVM package ( https://www.csie.ntu.edu.tw/~cjlin/libsvm ) in MATLAB (R2022b). To prevent information leakage, whole-brain FC and BC values were selected as feature variables for the classification model, rather than the FC and BC values that differed between the two groups.

Given the limited sample size, leave-one-out cross-validation (LOOCV) was implemented to partition the dataset into training and test sets and to evaluate the classifier’s ability to discriminate between groups. During the LOOCV procedure, the training dataset was partitioned into 86 subsets. In each iteration, 85 subsets constituted the training set, while the remaining single subset served as the test set. Data within the training set were normalized in each iteration, and the same normalization parameters were applied to the corresponding test set. Furthermore, a feature selection step using the F -score metric was performed exclusively on the training data during each LOOCV fold [ 46 , 47 ]. The F -score, a simple and effective measure for evaluating feature importance widely cited in feature selection (calculation details provided in Supplementary Information), was employed [ 46 , 47 ]. For each training fold, the top 100 features exhibiting the highest F -scores were selected to train the SVM model [ 46 , 47 ]. Model training incorporated a grid search approach to identify the optimal regularization parameter (C). A Linear kernel SVM was chosen to minimize the risk of overfitting. The trained model was then evaluated on the independent test set. This entire LOOCV process was repeated 86 times, ensuring each subject served as the test set exactly once. The overall SVM classification accuracy was calculated as the mean accuracy across all LOOCV iterations. Receiver Operating Characteristic (ROC) curves and the AUC were subsequently generated to further assess model performance [ 48 ]. Additionally, the statistical significance of the classification accuracy was evaluated using permutation testing (1000 repetitions). Specifically, group labels (sleep disorder vs. non-sleep disorder) were randomly permuted, and the entire LOOCV procedure (including normalization, F -score feature selection, model training with grid search, and testing) was repeated 1000 times. The accuracies obtained from these 1000 permuted-label iterations were compiled to form a null distribution. The accuracy derived from the true labels was then compared against this null distribution to verify that the performance of the constructed SVM model was statistically significant and not attributable to chance.

Furthermore, the external validity of the SVM classification model was assessed using an independent validation dataset. Since LOOCV led to the selection of different features across each iteration, consensus features were identified as those that appeared in the SVM model across all 86 LOOCV iterations [ 49 , 50 ]. These consensus features, along with the most frequent parameter C = 16, were used to retrain the model on the discovery dataset of 86 patients and subsequently validated on the independent dataset consisting of 31 patients. To assess the stability of our findings, we performed 1,000 permutation tests. These tests involved training models on the discovery dataset with permuted class labels and subsequently evaluating their accuracy on the independent validation dataset.

To further evaluate the stability of the SVM classification model across samples with varying depression severity, we conducted a subgroup analysis. The independent validation cohort was stratified into two subgroups based on HAMD scores: a lower-severity depression group (HAMD score ≤ 35) ( n = 12) and a higher-severity depression group (HAMD score > 35) ( n = 29). External validation analysis was then repeated using our established SVM classification model and its characterizing features within each subgroup.


## Results


### Demographic and clinical characteristics

The demographic and clinical characteristics of all patients in the discovery dataset are summarized in Table 1 . No significant differences were observed in gender, age, education level, head motion, or disease duration between adolescent depression patients with sleep disorders and those without ( p > 0.05). However, significant differences were found in the HAMD score ( t = 2.692, p = 0.009) and PSQI scores ( t = 10.648, p < 0.001) between the two groups. In the independent validation dataset, the two groups demonstrated significant differences exclusively in PSQI scores ( t = 2.641, p = 0.013), with no statistically discernible variations observed in other demographic or clinical parameters ( p > 0.05) (refer to Table 2 ).


#### Table 1.

Demographic and clinical characteristics of adolescent depressed patients with or without sleep disorders in the discovery dataset



| Characteristics (mean ± SD) | With sleep disorder ( n = 44) | Without sleep disorder ( n = 42) | Statistical value | p -value |
| --- | --- | --- | --- | --- |
| Gender (M/F) a | 11/33 | 13/29 | 0.378 | 0.538 |
| Age (years) b | 14.80 ± 1.62 | 15.31 ± 1.85 | 1.370 | 0.174 |
| Education (years) b | 9.00 ± 1.59 | 9.33 ± 1.73 | 0.931 | 0.354 |
| Disease duration (months) b | 13.01 ± 15.21 | 9.19 ± 11.77 | 1.298 | 0.198 |
| HAMD b | 33.66 ± 7.31 | 29.00 ± 8.70 | 2.692 | 0.009 * |
| PSQI b | 14.73 ± 2.57 | 7.76 ± 3.45 | 10.648 | < 0.001 * |
| Head motion (mean FD_Jenkinson) b | 0.08 ± 0.04 | 0.07 ± 0.04 | 0.112 | 0.911 |


HAMD Hamilton Depression Scale, PSQI Pittsburgh Sleep Quality Index


#### Table 2.

Demographic and clinical characteristics of depressed adolescents with and without sleep disorder in the independent validation dataset



| Characteristics (mean ± SD) | With sleep disorder ( n = 21) | Without sleep disorder ( n = 10) | Statistical value | p -value |
| --- | --- | --- | --- | --- |
| Gender (M/F) a | 15/6 | 5/5 | 1.359 | 0.662 |
| Age (years) b | 15.48 ± 1.44 | 15.20 ± 1.99 | 0.442 | 0.370 |
| Education (years) b | 9.57 ± 1.36 | 9.50 ± 1.84 | 0.122 | 0.904 |
| Disease duration (months) b | 23.10 ± 13.12 | 25.00 ± 22.38 | 0.300 | 0.767 |
| HAMD b | 38.81 ± 7.03 | 34.50 ± 9.56 | 0.220 | 0.166 |
| PSQI b | 13.24 ± 3.56 | 9.20 ± 4.78 | 2.641 | 0.013 * |
| Head motion (mean FD_Jenkinson) b | 0.09 ± 0.06 | 0.07 ± 0.02 | 1.073 | 0.292 |


HAMD Hamilton Depression Scale, PSQI Pittsburgh Sleep Quality Index


### Network analysis between patients with and without sleep disorder

Significant differences in BC were observed across three brain regions between adolescent depression patients with and without sleep disorders (Table 3 ; Fig. 2 A top panel). BC was significantly higher in the right Middle Temporal Gyrus (MTG.R) in patients with sleep disorders compared to those without ( t = 4.435, p < 0.001, Bonferroni-corrected). Conversely, BC was significantly lower in the left Median Cingulate and Paracingulate Gyri (DCG.L) ( t = 3.750, p < 0.001, Bonferroni-corrected) and left Caudate Nucleus (CAU.L) ( t = 4.804, p < 0.001, Bonferroni-corrected) in patients with sleep disorders.


#### Table 3.

Significant BC differences between adolescent depressed patients with or without sleep disorders



| Brain region | t-value | p -value |
| --- | --- | --- |
| With sleep disorder > Without sleep disorder |
| MTG.R | 4.435 | < 0.001 |
| With sleep disorder < Without sleep disorder |
| DCG.L | 3.750 | < 0.001 |
| CAU.L | 4.804 | < 0.001 |


BC Betweenness centrality, MTG Middle temporal gyrus, DCG Median cingulate and paracingulate gyri, CAU Caudate nucleus


#### Fig. 2.


> **Figure/Table Caption:** Network analysis and correlation with PSQI scores in adolescent depressed patients with sleep disorders. A Top: Brain regions exhibiting significant BC differences between depressed adolescents with versus without sleep disorders. Bottom: Brain regions showing significant FC alterations between groups. Red represents an increase in BC or FC in the sleep disorder group, and blue represents a decrease in BC or FC in the sleep disorder group. B Correlation of BC values of CAU.L and MTG.R with PSQI scores. C Correlation of FC values of ORBsup.L-ANG.L and LING.L-MTG.R with PSQI scores. All FC values are Fisher’s Z -transformed. FC = functional connectivity, BC = betweenness centrality, PSQI = Pittsburgh sleep quality index, MTG = middle temporal gyrus, CAU = caudate nucleus, ORBsup = superior frontal gyrus, orbital part, ANG = angular gyrus, LING = lingual gyrus


### FC analysis between patients with and without sleep disorder

In FC analyses, patients with sleep disorders exhibited enhanced connectivity in 8 FC edges, including the left superior orbital frontal gyrus to the left angular gyrus (ORBsup.L - ANG.L) ( t = 4.702, p < 0.001, Bonferroni-corrected), the left lingual gyrus to the right middle temporal gyrus (LING.L - MTG.R) ( t = 5.040, p < 0.001, Bonferroni-corrected), the right LING to MTG.R (LING.R - MTG.R) ( t = 4.826, p < 0.001, Bonferroni-corrected), the left calcarine fissure and surrounding cortex to the MTG.R (CAL.L-MTG.R) ( t = 5.109, p < 0.001, Bonferroni-corrected), the right CAL to the MTG.R (CAL.R-MTG.R) ( t = 5.241, p < 0.001, Bonferroni-corrected), the left middle occipital gyrus to the MTG.R (MOG.L -MTG.R) ( t = 5.266, p < 0.001, Bonferroni-corrected), the right inferior occipital gyrus to the MTG.R (IOG.R - MTG.R) ( t = 4.900, p < 0.001, Bonferroni-corrected), and the right CAL to the temporal pole middle temporal gyrus (CAL.R- TPOmid.R) ( t = 4.913, p < 0.001, Bonferroni-corrected), while showing decreased connectivity in the left olfactory cortex to the left caudate nucleus (OLF.L - CAU.L) ( t = 4.781, p < 0.001, Bonferroni-corrected) compared to patients without sleep disorders (Fig. 2 A bottom panel, Table 4 ).


#### Table 4.

FC differences between adolescent depressed patients with or without sleep disorders



| Seed region | Target region | t-value | p -value |
| --- | --- | --- | --- |
| With sleep disorder > Without sleep disorder |
| ORBsup.L | ANG.L | 4.702 | < 0.001 |
| LING.L | MTG.R | 5.040 | < 0.001 |
| LING.R | MTG.R | 4.826 | < 0.001 |
| CAL.L | MTG.R | 5.109 | < 0.001 |
| CAL.R | MTG.R | 5.241 | < 0.001 |
| MOG.L | MTG.R | 5.266 | < 0.001 |
| IOG.R | MTG.R | 4.900 | < 0.001 |
| CAL.R | TPOmid.R | 4.913 | < 0.001 |
| With sleep disorder < Without sleep disorder |
| OLF.L | CAU.L | 4.781 | < 0.001 |


FC Functional connectivity, ORBsup Superior frontal gyrus, orbital part, ANG Angular gyrus, CAL Calcarine fissure and surrounding cortex, MTG Middle temporal gyrus, LING Lingual gyrus, MOG Middle occipital gyrus, IOG Inferior occipital gyrus, TPOmid Temporal pole: middle temporal gyrus, OLF Olfactory cortex, CAU Caudate nucleus


### Correlation analysis

Pearson correlation analyses were conducted to investigate the relationship between BC values and PSQI scores in the aforementioned brain regions, as well as between the values of the 9 connections and PSQI scores. The results revealed significant correlations between BC values in the CAU.L, DCG. L and MTG.R regions and PSQI scores ( p < 0.0042, Bonferroni-corrected) (Fig. 2 B, Supplementary Table 1). Additionally, all 9 connections that showed significant differences between the two groups were significantly correlated with PSQI scores, with the two connections demonstrating the strongest correlation presented in Fig. 2 C ( p < 0.0042, Bonferroni-corrected) (Supplementary Table 2).


### Support vector machine classification results

In this study, an SVM classification model was constructed using whole-brain FC and BC features. The classification results are presented in Fig. 3 ; Table 5 . The model achieved an overall accuracy of 81.40%, specificity of 78.57%, sensitivity of 84.09%, and AUC of 89.34% ( p < 0.001, nonparametric permutation test) (Supplementary Fig. 1 A). The performance of this combined model was significantly superior to SVM models built with FC features or BC features alone (Fig. 3 A). A total of 62 features were selected during the 86-fold LOOCV, which were identified as consensus features. These included two BC features (CAU.L and MTG.R) and 60 FC features, which were considered the primary contributors to the model (Fig. 4 , Supplementary Table 3, Supplementary Table 4).


#### Fig. 3.


> **Figure/Table Caption:** ROC curves of SVM classification models. A The ROC curves of SVM classification models in the discovery dataset. B The ROC curves of SVM classification models in the independent validation dataset ROC = receiver operating characteristic, SVM = support vector machine, AUC = area under the receiver operating characteristic curve


#### Table 5.

Classification results of SVM models



|  | Features | Accuracy (%) | Sensitivity (%) | Specificity (%) |
| --- | --- | --- | --- | --- |
| Discovery dataset | BC + FC | 81.40 | 84.09 | 78.57 |
| BC | 77.91 | 79.55 | 78.57 |
| FC | 76.74 | 79.55 | 83.33 |
| Independent validation dataset | BC + FC | 74.19 | 66.67 | 80.00 |
| BC | 64.52 | 42.86 | 80.00 |
| FC | 64.52 | 80.95 | 50.00 |


SVM Support vector machine, BC Betweenness centrality, FC F unctional connectivity


#### Fig. 4.


> **Figure/Table Caption:** Consensus features and their weights contributing to all SVM classification models in 86-fold LOOCVs. A The consensus features in FC features. The numbers corresponding to the coordinates represent the region numbers of the AAL90 atlas. Red indicates positive weight values, while blue represents negative weight values. B The consensus features in BC features. The region numbers of AAL are presented in Supplementary Table 5. FC= functional connectivity, BC = betweenness centrality, LOOCV = leave-one-out cross-validation. MTG = middle temporal gyrus, CAU = caudate nucleus, AAL = Automated Anatomical Labelling atlas.


### External validity of the SVM classification model

The SVM model developed from the discovery dataset was further validated in an independent dataset to differentiate between adolescent depression patients with and without sleep disorders. In the validation analysis, the model achieved an accuracy of 74.19%, sensitivity of 66.67%, specificity of 80.00%, and AUC of 69.05% ( p = 0.006, nonparametric permutation test) (Fig. 3 B, Supplementary Fig. 1B, Table 5 ). These results demonstrate that the SVM model exhibits satisfactory generalization performance.

The SVM model demonstrated consistently robust performance in subgroup analyses of the independent validation dataset. Specifically, the SVM model achieved accuracies of 75.00% in the lower-severity subgroup and 73.68% in the higher-severity subgroup, closely aligning with the overall accuracy of 74.19% observed in the full independent dataset (Supplementary Fig. 2). These results indicate that the SVM classification model and its underlying feature set effectively capture sleep disorder-related variability, independent of depression severity.


## Discussion

This cross-sectional study compared BC and FC in two groups of adolescent patients with depression, one with sleep disorders and the other without. Differences in BC and FC across brain regions were identified, and the correlation between these differential regions and sleep quality was explored. Whole-brain BC and FC were then utilized as features to construct SVM classification models for predicting the presence of sleep disorders in adolescent depression patients. The results revealed a combined identification accuracy of 81.40%, with specificity of 78.57%, sensitivity of 84.09%, and AUC of 89.34%. In the independent validation dataset, accuracy was 74.19%, sensitivity was 66.67%, specificity was 80.00%, and AUC was 69.05%. These findings suggest that BC and FC features may serve as potential neurological markers for classifying sleep disorders in adolescents with depression.

In our investigation of between-group BC differences, we identified significant BC abnormalities in the MTG.R, DCG.L, and CAU.L among adolescents with depression when comparing those with and without comorbid sleep disorders. These key brain regions are critically involved in language processing, emotion regulation, and higher cognitive functions [ 51 – 53 ]. The DCG, a key component of the cingulate cortex, represents one of the few brain regions, besides the suprachiasmatic nucleus, that exhibits cyclic expression of clock genes [ 54 ]. Prior evidence [ 54 , 55 ] demonstrated that clock gene expression modulates neural responses in the cingulate cortex during cognitive tasks. In addition, depressed carriers of the CLOCK 3111 C allele exhibit significantly higher rates of sleep disorders compared to depressed non-carriers [ 54 , 55 ]. These findings suggest a significant association between this region and circadian regulation. Adolescence represents a critical period of sleep architecture reorganization, characterized by increased light sleep proportion, reduced total sleep duration, and a pronounced circadian timing delay compared to other stages [ 1 ]. Notably, the developmental trajectory of adolescent sleep is characterized by a marked reduction in slow-wave activity during sleep. This physiological change may reflect synaptic pruning, a crucial neurodevelopmental process involving the selective elimination of neuronal connections [ 56 – 58 ]. This age-related decline in synaptic activity may underlie both diminished sleep requirements and delayed sleep phase patterns observed in adolescents, suggesting mechanistic connections between physiological changes and circadian rhythm disturbances during pubertal maturation [ 59 ]. The impact of delayed circadian rhythms on depression in adolescents has been extensively investigated. Emerging evidence suggests that disrupted sleep patterns in depressed adolescents may be associated with delayed and diminished melatonin secretion, potentially contributing to both sleep disorders and mood dysregulation [ 60 , 61 ]. Furthermore, delayed circadian timing or other sleep disorders may create prolonged nocturnal ruminative states in adolescents with depression, potentially exacerbating depressive symptoms [ 59 , 62 , 63 ]. Given their shared psychophysiological underpinnings, circadian rhythm disruptions during adolescent development may play a pivotal role in the bidirectional relationship between sleep disorders and depression [ 59 ]. The observed BC abnormalities in the DCG region in our study may represent neuroimaging manifestations of this process. These findings highlight the need for future investigations into DCG’s role in mediating circadian rhythms, depression, and sleep disorders, suggesting this region may serve as a critical neural hub for therapeutic interventions targeting both conditions.

In our FC analysis, we identified 9 significantly altered FC edges (including ORBsup.L-ANG.L and LING.L-MTG.R) between depressed adolescents with and without sleep disorders. Notably, most of these aberrant FC edges involved the MTG as a central node. The MTG serves as a crucial region for emotion recognition and empathy, constituting an essential component of the temporal cortex [ 53 ]. In a large-scale cross-sectional fMRI study utilizing the Human Connectome Project, Cheng et al. identified significant correlations between FC of the temporal cortex with other brain regions and both sleep disturbance and depressive symptom scores [ 19 ]. These findings suggest that aberrant FC patterns involving the temporal cortex may represent a shared neurobiological substrate underlying depression and sleep disorders. A recent simultaneous electroencephalography-fMRI study [ 64 ] revealed that increased MTG activity during N2 sleep may contribute to reduced sleep duration, potentially through its role in ongoing information processing. In our adolescent depression cohort with sleep disorders, the observed stronger FC centered on the MTG may reflect abnormally enhanced information processing during sleep. This neural hyperactivity could force sleep spindles to prioritize information integration at the expense of sleep maintenance, ultimately contributing to the pathogenesis of sleep disorders in this population [ 52 , 64 ]. These findings demonstrate a significant association between the MTG and sleep disorders. Given that prior research has established reduced gray matter volume in the MTG as a characteristic feature of depression, further investigation specifically targeting the MTG’s role in both depression and sleep disorders shows considerable potential.

In this study, an SVM classification model was developed to identify adolescent depression with sleep disorders. The model demonstrated notable performance, achieving an accuracy of 81.40% for the discovery dataset and 74.19% for the independent validation dataset. Previous studies have also focused on ML models for classifying sleep disorder patients. For instance, Zhang et al. [ 65 ] used the subregion cingulate gyrus FC network as a feature for SVM classification, reporting an accuracy of 84.21%, specificity of 84.62%, sensitivity of 71.43%, and AUC of 90%. Similarly, Dai et al. [ 66 ] suggested that inter-hemispheric communication could serve as a neural marker for sleep disorders, utilizing voxel-mirrored homotopic connectivity as a feature in their SVM model, yielding a sensitivity of 81.3%, specificity of 87.50%, and AUC of 88.70%. These classification accuracies are comparable to our findings. However, prior research typically relied on brain regions showing significant differences between sleep disorder and non-sleep disorder groups as features for model construction [ 65 , 66 ]. This approach carries a risk of information leakage, potentially leading to overfitting and inflated accuracy. In contrast, our study incorporated whole-brain BC and FC in the model and used LOOCV to partition the discovery dataset into training and validation sets, ensuring feature screening occurred exclusively within the training sets to mitigate the risk of information leakage. Notably, in the SVM model developed in this study, the integrated model combining both BC and FC features demonstrated superior performance compared to models using either BC or FC features alone, with consistent improvements observed across both discovery and validation datasets. This finding aligns with Wang et al.‘s results [ 31 ], demonstrating that SVM models integrating both FC and topological attributes exhibit superior classification performance for psychiatric disorders. The enhanced performance likely stems from the model’s ability to more comprehensively characterize brain network features by simultaneously capturing FC patterns and topological properties of individual brain regions.

To enhance the interpretability of our SVM classification model, we operationally defined features consistently selected during all LOOCV iterations as consensus features, considering them to be major contributors to the model’s discriminative performance. These comprised 2 BC features (CAU.L and MTG.R) and 60 FC features. These features overlapped with those identified in our BC and FC analyses comparing groups with and without sleep disorders, suggesting their significance for diagnosing sleep disorders. These consensus features are primarily localized in key regions, including the cingulate cortex, MTG, caudate nucleus, and middle frontal gyrus, all of which constitute critical components of the DMN [ 67 , 68 ]. The DMN is implicated in self-referential thought and emotional control, with evidence suggesting its critical involvement in impaired affective processing observed in depression [ 69 , 70 ]. Leerssen et al. demonstrated that sleep disorder patients exhibit significantly increased FC between core DMN regions (hippocampus-middle frontal gyrus), with this enhancement being positively correlated with clinical measures of sleep disturbance severity [ 71 ]. Consequently, DMN impairment may represent the neural substrate underlying emotional dysregulation and altered self-referential processing in sleep disorder patients, which is closely associated with their depressive symptoms [ 54 ]. Emerging evidence suggests that DMN dysfunction may be linked to rumination, a maladaptive emotional processing pattern that potentially exacerbates depressive symptomatology [ 72 , 73 ]. Given that both depression and sleep disorders are considered network-level disorders, our successful classification of depressed adolescents with/without sleep disorders using consensus features of DMN highlights the DMN’s central role. These findings suggest that the DMN plays a pivotal role in both depression and sleep disorders, making the investigation of its network features a promising avenue for developing diagnostic models targeting these comorbid conditions.

In summary, our study employed multiple closely interrelated and complementary analyses, including group difference evaluation and classification analysis, to investigate adolescent depression with sleep disorder. The BC of the CAU.L and MTG.R, along with all 9 edges demonstrating significant group differences (including ORBsup.L- ANG.L, and the LING.L - MTG.R), were consistently implicated in both the group comparisons and the SVM model analyses as significantly associated with sleep disturbances. The relationship between these brain regions and sleep disorders has been extensively discussed within this paper. Notably, among the 62 consensus features identified, 51 edges, including those connecting the Rolandic operculum to supplementary motor area (SMA) and the inferior temporal gyrus to the SMA, were not validated in the group difference analysis. While this discrepancy may partly stem from the stringent Bonferroni correction applied in the group comparison, it also suggests several points. Firstly, it likely reflects the distinct emphases of different analytical approaches. The case-control design used for group comparisons treats each group as an “average individual” to identify the most prominent pathological markers, highlighting features with the largest between-group differences [ 74 ]. This method, valued for its statistical rigor, is widely accepted in neuroimaging studies of depression [ 75 , 76 ]. However, recent research indicates that such group-comparison approaches may obscure substantial biological heterogeneity [ 77 ]. Conversely, the machine learning model aims to identify complex and subtle brain features to construct an optimal diagnostic model [ 26 ]. The consensus features we identified represent feature combinations with the greatest potential for individualized diagnostic utility [ 49 , 50 ]. By integrating these two complementary methodologies, we identified overlapping network features, validated both by case-control analysis and present within the SVM’s consensus features, as potential biomarkers for sleep disturbances in adolescent MDD patients. The remaining consensus features serve as complementary features enhancing the performance of our SVM model, potentially capturing more nuanced patterns related to sleep dysregulation.

This study has several Limitations. First, the diversity of treatment options for adolescent depression, with varying types and dosages of medication across patients, made it difficult to include medication regimen as a covariate. Future studies should consider selecting samples that are either medication-free or consist of subjects undergoing the same treatment regimen. Second, the higher prevalence of sleep disorders among adolescents with depression led to an imbalance in the number of subjects in the two groups within the independent validation set, potentially affecting the efficacy of the classification model. Future research should prioritize the use of more balanced datasets for model training and validation. Additionally, due to the absence of objective sleep assessment measures such as polysomnography in our study, sleep disturbances were determined solely based on PSQI scores. This approach may have influenced the study outcomes. Future investigations should incorporate objective sleep metrics to enhance the scientific rigor of research. Furthermore, this study employed the AAL atlas to extract FC and BC for analysis. Although the AAL atlas has been widely used in previous similar research, its reliance on anatomical rather than functional parcellation, combined with its relatively coarse resolution of only 90 regions, may limit the regional specificity and reproducibility of the findings. Therefore, future studies should consider utilizing finer-grained, functionally defined atlases, such as the Schaefer or Glasser parcellations, for more precise analyses [ 78 , 79 ].


## Conclusion

Network topological attributes and FC are crucial for evaluating brain networks. This study provides evidence of alterations in BC and FC in adolescents with depression, both with and without sleep disorders. Our findings also demonstrate that the SVM classification model, built using BC and FC features, exhibits strong performance in identifying adolescent depression patients with co-occurring sleep disorders. These results suggest that BC and FC could serve as reliable neuroimaging markers for diagnosing sleep disorders.


## Supplementary Information


## Acknowledgements

We extend our heartfelt gratitude to all participants involved in this study. We thank Bullet Edits Limited for the linguistic editing and proofreading of the manuscript.


## Authors’ contributions

S.H. and X.Z. performed data analysis and wrote the original draft. D.Y., J.H., S.Z., and L.X. participated in data collection. M.W., D.L., J.X., and M.Z. contributed to patient evaluations. Y.L. and D.Z. provided essential research instruments. L.Z. conceived and designed the study, and acquired funding. S.H. and X.Z. share first authorship.


## Funding

This study was supported by National Clinical Key Specialty Construction Project of China, Anhui Province Medical and Health Key Specialty Construction Project, the Open Fund Project of the Anhui Province Key Laboratory of Philosophy and Social Sciences for Adolescent Mental Health and Crisis Intelligent Intervention (SYS2023C07), and Anhui Province Environmental Toxicology and Pollution Control Technology Key Laboratory Project (2025SZ0007).


## Data availability

The datasets used in this study are available from the corresponding authors, Li Zhu or Daomin Zhu, upon reasonable request.


## Declarations


### Ethics approval and consent to participate

The study was approved by the Ethics Committee of Fourth People’s Hospital in Hefei (HFSY-IRB-YJ-LWTG-XL (2024-077-001)). All procedures followed the ethical standards of the 1964 Helsinki Declaration and its later amendments. Written informed consent was obtained from all participants and their legal guardians.


### Consent for publication


### Competing interests

The authors declare no competing interests.


## Footnotes

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Songhao Hu and Xingyue Zuo are share first authorship.


## Contributor Information

Daomin Zhu, Email: [EMAIL_REDACTED].

Li Zhu, Email: [EMAIL_REDACTED].

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials


### Data Availability Statement

The datasets used in this study are available from the corresponding authors, Li Zhu or Daomin Zhu, upon reasonable request.
