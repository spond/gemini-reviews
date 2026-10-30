# De-Identified Manuscript `OOD_ANON_48`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract


### Background

At present, the clinical diagnosis of obsessive-compulsive disorder (OCD) is primarily based on interviews with patients by experienced psychiatrists, which is inherently limited by its subjectivity. Therefore, there is a pressing clinical need to identify objective biomarkers of OCD. Although the combination of EEG and data-driven method based on machine learning offers promise for identifying objective neurophysiological biomarkers, current researches either rely on only small sample sizes, lack interpretability, use only one single dataset which cannot validate model generalizability, or utilize only one type of EEG feature which cannot evaluate the relative utility of different features as potential biomarkers of OCD under a unified data-driven framework.


### Method

This study employed two independent datasets (Dataset 1: OCD = 35, healthy controls = 37; Dataset 2: OCD = 21, healthy controls = 21). Eight EEG features were extracted and were sent to six machine learning (ML) classifiers to classify OCD from healthy controls. After optimizing the hyperparameters and the most relevant feature set on Dataset 1, each ML model was retrained on Dataset 1 and then were tested on an independent external test set (Dataset 2) to assess their generalizability. Feature contributions were interpreted using SHapley Additive Explanations (SHAP) analysis.


### Result

Among the eight EEG feature sets, the phase-locking value (PLV) features achieved the highest classification performance across all machine learning models. The LightGBM classifier outperformed others ML classifiers, reaching an accuracy of 86.6% on Dataset 1 and 83.3% on Dataset 2 (independent external test). The data-driven method based on machine learning selected the most important 16 PLV features and SHAP-based feature importance analysis identified alpha band PLV (F4-P3), delta band PLV (P3-O1, F3-O1), and theta band PLV (C3-T4) as the most influential contributors to model predictions.


### Conclusion

This study developed an explainable machine learning framework based on PLV functional connectivity feature to enable accurate and generalizable OCD classification. These results highlight the potential of PLV especially long-range PLV connectivity between frontal and parietal/occipital lobe as a reliable EEG biomarker for objective and clinically applicable OCD diagnosis.


### Supplementary Information

The online version contains supplementary material available at [REDACTED_DOI].

Keywords: Obsessive compulsive disorder, EEG biomarker, Explainable machine learning, SHAP


## Introduction

Obsessive-compulsive disorder (OCD) is a serious and chronic mental disorder that affects approximately 2–3% of the global population [ 1 – 3 ]. Clinically, OCD is principally characterized by recurrent, intrusive obsessive thoughts and repetitive compulsive behaviors that patients often recognize as irrational, yet experience a marked loss of voluntary control over these symptoms [ 4 – 6 ]. Currently, the clinical diagnosis of OCD is primarily based on interviews with patients by experienced psychiatrists, but this method is inherently limited by its subjectivity and susceptibility to diagnostic ambiguity [ 7 , 8 ]. Therefore, identifying objective biomarkers of OCD could provide complementary information to current clinical assessments and contribute to a better understanding of the disorder.

At present, electroencephalography (EEG) as a non-invasive imaging technique has been widely applied for detecting neurophysiological abnormality of OCD. A growing body of quantitative EEG studies have revealed the following EEG alterations in OCD patients, including increased theta-band power [ 9 ], reduced beta-band activity [ 10 ], significant changes in frontal cortical oscillatory dynamics [ 11 ], disrupted connectivity between anterior cingulate cortex and frontal regions [ 12 ] and frontal alpha asymmetry [ 13 ]. However, the above-mentioned abnormal EEG measures in OCD were identified by using traditional group-level statistics and are not suitable as potential biomarkers for classifying OCD at the individual level.

To overcome the limitations associated with traditional EEG analysis approaches, machine learning (ML) has emerged as a promising data-driven solution for uncovering subtle and multidimensional neural patterns in psychiatric disorders such as OCD. By enabling data-driven classification and feature selection, ML methods can effectively capture complex brain dynamics that may be overlooked by univariate statistical techniques. In recent years, several studies have explored the application of ML to EEG-based OCD classification, yielding encouraging results [ 14 ]. For example, Aydin et al. utilized support vector machine (SVM) to classify OCD patients using EEG-derived complexity and hemispheric asymmetry features, achieving an accuracy of 85% in a small sample of 10 patients [ 15 ]. Similarly, Tan et al. employed SVM to distinguish OCD patients based on Global Field Synchronization (GFS) in the theta band, reporting 78.05% accuracy in a cohort of 15 OCD patients [ 16 ]. In another study, Altuğlu et al. applied a Random Forest classifier to Approximate Entropy (ApEn) features in the beta band, successfully differentiating treatment-responsive and treatment-resistant OCD patients with 89.66% accuracy in a sample of 57 individuals [ 17 ]. While these findings support the potential of identifying EEG biomarkers and EEG-based OCD diagnosis by using ML, current research still suffers from notable limitations. Most previous studies rely on small sample sizes and only one single dataset, which cannot verify the model generalizability. In addition, the majority of ML models function as black boxes, offering limited transparency and interpretability, which remains a major barrier to provide clinicians with sufficient information to identify which features are more important for classifying OCD. Crucially, existing studies often utilize only one type of EEG feature (e.g., power or entropy), without evaluating the relative utility of different feature domains as potential biomarkers of OCD under a unified data-driven framework.

In summary, this study tried to apply a systematic and interpretable ML classification strategy to explore potential EEG biomarkers of OCD, addressing several key limitations in prior research. Eight EEG measures including coherence, phase locking value (PLV), power spectral density (PSD), Kolmogorov complexity (KC), Approximate Entropy (ApEn), Fuzzy Entropy (FuzzyEn), Sample entropy (SampEn), and Lempel-Ziv Complexity (LZC) were extracted and comparatively evaluated within a standardized interpretable ML pipeline. To ensure generalizability and minimize overfitting, two independent datasets were utilized for training and testing respectively with consistent preprocessing protocols. Classification performance was assessed across six machine learning algorithms, enabling a robust comparative analysis. Furthermore, the integration of SHapley Additive exPlanations (SHAP) enhanced model transparency and interpretability by identifying feature contributions. By combining multi-domain EEG features, cross-model benchmarking, and explainable ML techniques, this study offers a reproducible and clinically meaningful computational framework for EEG-based OCD diagnosis.


## Materials and methods


### Participants

The participants in this study were sourced from two distinct cohorts. The Dataset 1 was from a publicly available database [ 18 ] which included 35 patients diagnosed with OCD and 37 matched healthy controls. For the Dataset 2, 21 OCD patients and 21 matched healthy controls were recruited from the Second Affiliated Hospital of Xinxiang Medical University (Fig. 1 ). Demographic information is presented in Tables 1 and 2 .


#### Fig. 1.


> **Figure/Table Caption:** Flow chart of materials and methods in this study


#### Table 1.

Demographic information of the dataset 1



|  | Age(years) Mean ± std | Sex Male/Female | YBOCS |
| --- | --- | --- | --- |
| Patients | 31.43 ± 9.66 | 20/ 15 | 27.89 ± 6.64 |
| Healthy controls | 29.13 ± 11.37 | 14/ 23 | — |



#### Table 2.

Demographic information of the dataset 2



|  | Age(years) Mean ± std | Sex Male/Female | YBOCS |
| --- | --- | --- | --- |
| Patients | 25.95 ± 11.89 | 10/ 11 | 33.76 ± 8.90 |
| Healthy controls | 22.67 ± 2.27 | 10/ 11 | — |


All OCD patients underwent comprehensive behavioral and neuropsychiatric evaluations. Participants were excluded if they exhibited significant suicide risk, a history of neurological disorders, seizures, serious somatic illness, or a history of substance dependence or personality disorders. Only patients with a Yale-Browne score (Y-BOCS) of 16 or higher were included in the study. Ethical approval for the Dataset 2 was obtained from the Ethics Committee of the Second Affiliated Hospital of Xinxiang Medical University, and written informed consent was obtained from all participants.


### EEG data acquisition

For the Dataset 1, 26-channel EEG data were obtained using a Compumedics Quickcap equipped with sintered Ag/AgCl electrodes, according to the 10–10 international electrode system. The EEG data were sampled at 500 Hz and collected during two minutes of eye-open (EO) and two minutes of eye-closed (EC) conditions. The electrode impedance was maintained below 10 kΩ throughout the recording. In this study, only EEG data during EC condition was used for subsequent analysis.

For the Dataset 2, 64-channel resting-state EEG data were recorded using the Neuroscan SynAmps2 system (Australia) according to the 10–20 international electrode system. During EEG data recording, participants were asked to sit comfortably with their eyes closed for approximately 10 min. The EEG was sampled at 1000 Hz, and electrode impedance was also kept below 10 kΩ.


### EEG data preprocessing

The EEG data from both Dataset 1 and Dataset 2 were preprocessed using the EEGLAB toolbox [ 19 ] and MATLAB 2013b software (The MathWorks Inc. Natick, MA, USA) with a consistent pipeline. Initially, 19 EEG channels (Fp1, Fp2, F7, F3, Fz, F4, F8, T3, C3, Cz, C4, T4, P7, P3, Pz, P4, P8, O1, O2) were extracted from each subject of Dataset 1 and Dataset 2 at the same electrode locations. The EEG data were then bandpass filtered between 1 and 30 Hz using a zero-phase finite impulse response (FIR) filter. Next, the EEG data were down-sampled to 250 Hz and independent component analysis (ICA) was employed to identify and remove artifacts including such as electrooculography (EOG), electromyography (EMG), electrocardiography (ECG) [ 20 ]. In addition, the continuous EEG data were segmented into non-overlapping 2-second segment, and any segments containing remaining artifacts were discarded following visual inspection. Finally, all EEG data were re-referenced to a common average reference, and 30 segments (60 s) were selected from each subject for subsequent analysis.


### Multi-dimensional EEG feature computation

To comprehensively investigate the atypical brain activity in individuals with OCD and to identify the most sensitive EEG-based biomarkers, this study employed a multi-dimensional feature extraction strategy. In this study, eight commonly used resting-state EEG measures including coherence, phase locking value (PLV), power spectral density (PSD), Kolmogorov complexity (KC), Approximate Entropy (ApEn), Fuzzy Entropy (FuzzyEn), Sample entropy (SampEn), and Lempel-Ziv Complexity (LZC) were computed.

Coherence can quantify both phase alignment and amplitude correlation between signals from spatially distinct cortical regions within defined spectral bands. By capturing interregional synchronization of oscillatory activity, coherence provides a reliable index for assessing functional connectivity across distributed brain areas [ 21 ]. PLV offers a more temporally precise measure of phase synchronization, evaluating the stability of phase differences between EEG signals over time [ 22 ]. PSD is a foundational tool in resting-state EEG studies, allowing for quantification of the power distribution of EEG signals at different frequencies [ 23 ]. In addition, KC [ 24 ], ApEn [ 25 ], FuzzyEn [ 26 ], SampEn [ 27 ], and LZC [ 28 ] were used to qualify the irregularity, pattern unpredictability or complexity in EEG signals.


### Machine learning classification

In this study, a multi-stage machine learning classification framework was developed to enable accurate identification of patients with obsessive-compulsive disorder (OCD). Initially, raw EEG features were standardized using z-score normalization to ensure consistency across the dataset. The Dataset 1 is the training set, and the most relevant feature set and hyperparameter for each ML model were optimized by using Dataset 1. Feature selection was performed using a random forest model in combination with Recursive Feature Elimination with Cross-Validation (RFECV), a method that effectively identifies the most relevant features for model training. In addition, hyperparameter optimization was conducted using the Optuna framework (50 iterations) across six machine learning algorithms (Table 3 ) to determine optimal parameter configurations. The 10-fold cross-validation was used to train and validate each ML model on the Dataset 1. After optimizing the hyperparameters and the most relevant feature set, each ML model was retrained on Dataset 1. Subsequently, the retrained models were tested on an independent external test set (Dataset 2) to assess their generalizability.


#### Table 3.

Machine learning models used in this study



| Model | Description |
| --- | --- |
| Random Forest (RF) | RF employs bootstrap aggregating with randomized feature subspaces to construct decorrelated decision trees, a design particularly suited for high-dimensional EEG biomarker analysis [ 30 ]. |
| K-Nearest Neighbors (KNN) | KNN operates through Euclidean distance-weighted voting among localized EEG epochs, capturing transient neurophysiological states that may evade global pattern classifiers [ 31 ]. |
| Support Vector Machine (SVM) | SVM with radial basis function (RBF) kernel projects nonlinear EEG feature interactions into higher-dimensional separable space [ 32 ]. |
| XGBoost | XGBoost iteratively constructs gradient-enhanced trees with L2 regularization, a mechanism that hierarchically prioritizes clinically interpretable EEG-clinical feature interactions [ 33 ]. |
| LightGBM | LightGBM accelerates gradient boosting through histogram-based approximation and exclusive feature bundling (EFB), enabling efficient processing of long-term EEG time series [ 34 ]. |
| CatBoost | CatBoost implements ordered boosting with oblivious trees to prevent target leakage when integrating categorical clinical metadata [ 35 ]. |


ML model performance was assessed using accuracy (ACC), area under the receiver operating characteristic (AUC), sensitivity (SEN), specificity (SPE), and F1-score. To enhance interpretability, SHapley Additive Explanations (SHAP) were applied post hoc to quantify feature contributions to model predictions, providing individualized and clinically meaningful insights [ 29 ]. All analyses were conducted in Python (v3.8.18) using the scikit-learn library (v1.3.2).


### Statistical analysis

Statistical analyses were conducted using SPSS 19.0. Continuous data are expressed as mean ± standard deviation (SD). The Shapiro-Wilk test assessed normality of data distribution. Wilcoxon rank-sum test with false discovery rate (FDR) correction were used to compared the difference of the importance features derived from SHAP analysis between OCD patients and healthy controls. Spearman correlation analysis was used to evaluate whether there is correlation between the importance features derived from SHAP analysis and Y-BOCS score.


## Result


### ML classification results

For Dataset 1, we found that the PLV feature achieved the best classification performance across all models after optimizing the hyperparameters and the most relevant feature set. Specifically, when using the most important 16 PLV features (Table 6 ; Fig. 2 ) and the LightGBM model we can obtain the best classification performance (ACC = 86.6%, SEN = 85.6%, SPE = 87.5%, F1 score = 0.866, AUC = 0.809) (Fig. 3 ; Table 4 ). Classification results for other models and other EEG features on Dataset 1 are presented in the Supplementary Material.


#### Table 6.

Statistical comparison of PLV connectivity obtained from SHAP analysis between OCD and heathy controls in dataset 1



| Brain connectivity | Strength (mean ± std) | P | Z | P fdr |
| --- | --- | --- | --- | --- |
| HC | OCD |
| PLV-alpha(F4-P3) | 0.44 ± 0.05 | 0.41 ± 0.05 | 0.022 | 5.470 | 0.0711 |
| PLV-delta(P3-O1) | 0.69 ± 0.02 | 0.68 ± 0.02 | 0.164 | 1.975 | 0.2518 |
| PLV-delta(F3-O1) | 0.70 ± 0.03 | 0.70 ± 0.02 | 0.783 | 0.077 | 0.7829 |
| PLV-theta(C3-T4) | 0.47 ± 0.02 | 0.51 ± 0.04 | < 0.001 | 25.508 | 0.0001 |
| PLV-alpha(P8-O1) | 0.64 ± 0.09 | 0.67 ± 0.08 | 0.173 | 1.894 | 0.2518 |
| PLV-alpha(F4-PZ) | 0.48 ± 0.05 | 0.43 ± 0.05 | < 0.001 | 18.702 | 0.0004 |
| PLV-delta(F3-F8) | 0.67 ± 0.02 | 0.67 ± 0.01 | 0.459 | 0.553 | 0.6126 |
| PLV-alpha(F3-PZ) | 0.57 ± 0.07 | 0.54 ± 0.07 | 0.064 | 3.531 | 0.1472 |
| PLV-theta(P7-O1) | 0.59 ± 0.06 | 0.60 ± 0.06 | 0.698 | 0.152 | 0.7444 |
| PLV-beta(FP1-P3) | 0.31 ± 0.05 | 0.29 ± 0.03 | 0.052 | 3.920 | 0.1377 |
| PLV-alpha(PZ-P8) | 0.62 ± 0.09 | 0.56 ± 0.09 | 0.018 | 5.922 | 0.0700 |
| PLV-theta(FZ-P7) | 0.56 ± 0.05 | 0.58 ± 0.06 | 0.101 | 2.765 | 0.1793 |
| PLV-theta(F8-O2) | 0.62 ± 0.06 | 0.67 ± 0.06 | < 0.001 | 13.340 | 0.0027 |
| PLV-theta(F3-PZ) | 0.62 ± 0.05 | 0.61 ± 0.06 | 0.539 | 0.382 | 0.6630 |
| PLV-theta(C3-C4) | 0.45 ± 0.02 | 0.46 ± 0.03 | 0.080 | 3.148 | 0.1608 |
| PLV-theta(F4-P8) | 0.60 ± 0.06 | 0.60 ± 0.05 | 0.638 | 0.224 | 0.7289 |



#### Fig. 2.


> **Figure/Table Caption:** PLV connectivity alterations with significant differences across frequency bands in the Dataset 1: ( a ) delta, ( b ) theta, ( c ) alpha, and ( d ) beta. The red lines indicate that the mean value of patients with OCD is greater than that of the healthy control group. Conversely, green lines represent OCD patients with mean values that are lower than those observed in the healthy control group, and black line represents no difference between the two groups


#### Fig. 3.


> **Figure/Table Caption:** ROC of six machine learning models (RF, KNN, SVM, XGBoost, LightGBM, and CatBoost models) evaluated on Dataset 1


#### Table 4.

Machine learning classification metrics for dataset 1



| ML model | ACC | AUC | F1 score | SEN | SPE | Precision | Recall | Confusion Matrix | Time (s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SVM | 0.866 | 0.788 | 0.866 | 0.857 | 0.875 | 0.861 | 0.861 | [[31,5], [5,31]] | 0.54 |
| KNN | 0.807 | 0.806 | 0.798 | 0.714 | 0.875 | 0.867 | 0.722 | [[26,10], [4,32]] | 0.45 |
| LightGBM | 0.866 | 0.809 | 0.866 | 0.856 | 0.875 | 0.861 | 0.861 | [[31 , 5] , [5 , 31]] | 0.24 |
| RF | 0.802 | 0.783 | 0.798 | 0.714 | 0.875 | 0.867 | 0.722 | [[26,10], [4,32]] | 0.28 |
| XGBoost | 0.866 | 0.783 | 0.866 | 0.857 | 0.875 | 0.861 | 0.861 | [[31,5], [5,31]] | 0.56 |
| CAtboost | 0.733 | 0.759 | 0.733 | 0.714 | 0.750 | 0.813 | 0.722 | [[26,10], [6,30]] | 0.27 |


In order to evaluate the model generalizability, each model was retrained on Dataset 1 using its optimized hyperparameters and the most relevant feature set, and then was tested on an independent external dataset (Dataset 2). As shown in Fig. 4 ; Table 5 , the LightGBM model with the most important 16 PLV features (Table 6 ; Fig. 2 ) also achieved the best classification performance compared to other models. Specifically, we achieved an ACC of 83.3%, AUC of 0.839, SEN of 90.4%, and SPE of 76.1%. These findings underscore the robustness and generalizability of the model, particularly highlighting the effectiveness of the PLV feature set in both training and test datasets.


#### Fig. 4.


> **Figure/Table Caption:** ROC of six machine learning models (RF, KNN, SVM, XGBoost, LightGBM, and CatBoost models) evaluated on an external dataset (Dataset 2)


#### Table 5.

Machine learning classification metrics for dataset 2



| ML model | ACC | AUC | F1 score | SEN | SPE | Precision | Recall | Confusion Matrix | Time (s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SVM | 0.738 | 0.829 | 0.791 | 0.952 | 0.723 | 0.696 | 0.941 | [[16,1], [7,18]] | 0.58 |
| KNN | 0.714 | 0.851 | 0.697 | 0.952 | 0.776 | 0.556 | 0.909 | [[10,1], [8,23]] | 0.45 |
| LightGBM | 0.833 | 0.839 | 0.832 | 0.904 | 0.761 | 0.792 | 0.905 | [[19 , 2] , [5 , 16]] | 0.22 |
| RF | 0.761 | 0.888 | 0.756 | 0.914 | 0.619 | 0.704 | 0.905 | [[19,2], [8,13]] | 0.21 |
| XGBoost | 0.761 | 0.895 | 0.756 | 0.904 | 0.719 | 0.682 | 0.882 | [[15,2], [7,18]] | 0.56 |
| CatBoost | 0.709 | 0.879 | 0.807 | 0.904 | 0.714 | 0.72 | 0.9 | [[18,2], [7,15]] | 0.27 |



### SHAP analysis results

The above results shown that the best classification performance for OCD was obtained when using PLV feature and LightGBM model. To elucidate the contribution of PLV functional connectivity features in distinguishing OCD patients from healthy controls, we employed SHAP analysis to interpret the impact of each input feature on the model’s output.

The SHAP bar plot (Fig. 5 ) displays the mean absolute SHAP values, ranking the importance of individual features. The most influential features include alpha-band PLV (F4-P3), delta-band PLV (P3-O1, F3-O1), and theta-band PLV (C3-T4), indicating they have a significant influence on the model’s predictions, playing a key role in distinguishing OCD from healthy controls. These findings suggest that disruptions in alpha, delta, and theta frequency bands are especially relevant in OCD-related neural dysregulation. In contrast, features such as PLV-theta (F4–T6) and PLV-theta (F8–O2) contribute less to the model’s output, as indicated by their lower SHAP values.


#### Fig. 5.


> **Figure/Table Caption:** SHAP analysis of PLV functional connectivity features in OCD classification. Mean Absolute SHAP Values: Ranked feature importance based on SHAP values, identifying PLV-alpha (F4-P3), PLV-delta (P3-O1), and PLV-delta (F3-O1) as key discriminative features

Figure 6 presents the SHAP summary plot, showing both the magnitude and direction of each feature’s influence on the prediction. Notably, higher values (in red) of PLV-alpha (F4–P3) and PLV-delta (P3–O1) are predominantly associated with positive SHAP values, indicating a stronger likelihood of OCD classification. Conversely, lower values (in blue) tend to align with negative SHAP values, signifying reduced probability of OCD classification.


#### Fig. 6.


> **Figure/Table Caption:** SHAP analysis of PLV functional connectivity features in OCD classification. SHAP Summary Plot: Feature-wise SHAP value distribution, illustrating the impact of connectivity patterns on model predictions. Alterations in theta, alpha, and delta band connectivity are strongly associated with OCD classification


### Statistical comparison of PLV connectivity

We conducted a statistical comparison of the 16 PLV functional connectivity features that were identified as the most important contributors to the model’s predictions through SHAP analysis. The results (Table 6 ) indicate that OCD patients exhibited significantly higher phase synchronization in the theta band between right frontal and occipital regions (F8-O2) and between the central and temporal regions (C3-T4) compared to healthy controls. Additionally, OCD patients demonstrated significantly lower phase synchronization in the alpha band, particularly between the right frontal and parietal regions (F4-PZ).These findings suggest that increased theta band connectivity and reduced alpha band synchronization might be associated with functional dysregulation in OCD.Although differences were observed in the alpha frequency band for F4-P3 ( P = 0.022, P fdr = 0.0711) and PZ-P8 ( P = 0.018, P fdr = 0.070), these did not reach statistical significance after FDR correction.


### Correlations of important features and Y-BOCS

Spearman correlation analysis was conducted to examine the relationship between Y-BOCS score and the 16 most important PLV features. The results indicated that no significant correlation was found between any of the important features and the Y-BOCS score.


## Discussion

In this study, we demonstrated that PLV features, analyzed using a LightGBM classifier, show potential to distinguish between OCD patients and healthy controls. Among the eight EEG feature sets evaluated, PLV achieved the highest classification performance, with an accuracy of 86.6% on Dataset 1 and 83.3% on an independent external validation dataset (Dataset 2), highlighting the model’s robustness and generalizability across datasets. SHAP analysis identified the most influential features driving the model’s predictions, including alpha band PLV (F4-P3), delta band PLV (P3-O1, F3-O1), and theta band PLV (C3-T4). These features played a crucial role in distinguishing OCD patients from healthy controls, with increased delta-band synchronization and reduced theta-band and alpha-band synchronization observed in OCD patients. This data-driven approach highlights potential biomarkers for OCD, providing preliminary evidence that may contribute to a better understanding of the neural connectivity abnormalities associated with the disorder.


### Long-range PLV connectivity between frontal and parietal/occipital lobe as potential biomarkers of OCD patients

In this study, SHAP analysis identified 16 PLV-based functional connectivity features that significantly contributed to the model’s predictions, of which 7 were related to frontal-parietal connectivity. Notably, alpha-band PLV (F4-PZ) exhibited a statistically significant difference between OCD and healthy controls even after FDR correction, and alpha-band PLV (F4-P3) also showed significant difference although it did not pass FDR correction. These results highlight the potential involvement of the frontal-parietal network in the pathophysiology of OCD, suggesting that alterations in this network may serve as a key neurophysiological marker for the disorder. Previous research has consistently demonstrated disruptions in the frontal-parietal network in OCD patients, with studies employing both resting-state functional connectivity and effective connectivity revealing significant alterations in these brain regionsds [ 36 , 37 ]. In addition, neuroimaging studies utilizing functional magnetic resonance imaging (fMRI) and EEG have further corroborated the role of the frontal-parietal network in OCD, highlighting the network’s critical involvement in cognitive and emotional dysregulation observed in the disorder [ 38 , 39 ]. Together, these findings support the hypothesis that disruptions in the frontal-parietal network are integral to the neurobiological underpinnings of OCD and may provide valuable insights for its diagnosis and treatment.

Among the 16 functional connectivity features identified through SHAP analysis, two were specifically related to frontal-occipital connectivity: delta-band PLV (F3-O1) and theta-band PLV (F8-O2). Notably, theta-band PLV (F8-O2) demonstrated a statistically significant difference between OCD patients and healthy controls even after FDR correction, indicating a disruption in connectivity within this frontal-occipital network. These results highlight the potential involvement of frontal-occipital connectivity in the neurobiological mechanisms of OCD, suggesting its contribution to the cognitive and emotional dysregulation observed in the disorder. The observed alterations in frontal-occipital connectivity are in line with previous studies employing both EEG and fMRI. Deng et al. found reduced interhemispheric connectivity between the occipital gyrus and frontal regions in OCD patients, further supporting the role of this network in the pathophysiology of OCD [ 40 ]. Likewise, Yu et al. reported significant changes in the functional connectivity between the occipital gyrus and frontal regions in OCD patients, with these alterations correlating with the severity of clinical symptoms [ 41 ]. Additionally, a study by Xue et al. employing graph theory found frequency-dependent functional connectivity alterations between the occipital and frontal regions in OCD, emphasizing the role of frontal-occipital connectivity in the disorder [ 42 ]. These findings collectively underscore the importance of frontal-occipital functional connectivity as a key factor in the pathophysiology of OCD, suggesting that dysfunction in this network may serve as an important biomarker for diagnosis and therapeutic strategies.

Furthermore, SHAP analysis also revealed a significant theta band connectivity between the central cortex (C3) and the temporal lobe (T4). The C3 (central cortex), part of the sensorimotor cortex, is involved in motor control and sensory integration [ 43 ], while the T4 (temporal lobe) plays a crucial role in auditory processing, memory, and emotion regulation [ 44 ]. The enhanced theta band connectivity suggests overactivation or dysregulation of the sensorimotor network, which may contribute to the repetitive behaviors and hyperactivity observed in OCD. These findings align with literature on theta band activity in OCD, where studies have shown that theta abnormalities in sensorimotor regions correlate with impaired sensory processing and cognitive control. Researches by Perera et al. [ 45 ] and Koh et al. [ 46 ] emphasized how theta band connectivity between sensorimotor and temporal regions disrupts sensory-motor integration, contributing to symptoms like repetitive behaviors and intrusive thoughts. These findings support the idea that sensorimotor dysregulation could be a core mechanism underlying OCD symptoms and suggest that theta band connectivity may serve as a biomarker for OCD, as well as a target for neurostimulation therapies aimed at normalizing functional connectivity.

Although some features such as alpha-band PLV (P8-O1) and delta-band PLV (F3-F8) did not show statistically significant differences between OCD and healthy controls, this does not entirely rule out their potential role in distinguishing these two groups. These features may be relevant for specific subtypes or stages of OCD, or they could enhance classification accuracy when combined with other biomarkers. Furthermore, individual variability and the heterogeneity of OCD may reduce the predictive effectiveness of these features in the overall sample. Therefore, future research should explore the role of these features in classifying OCD and healthy controls, potentially employing more refined stratification or personalized analytical methods. Additionally, improving data collection, analytical techniques, and increasing sample sizes may help uncover the clinical significance of these features, providing more reliable biomarkers for distinguishing between OCD and healthy controls.


### Comparison with classification performance in previous studies

Compared to previous studies, our results demonstrate a more robust and interpretable approach to OCD classification. As summarized in Table 7 , earlier works primarily employed support vector machines (SVM) or other classifiers trained and tested on the same dataset, which may limit generalizability. For example, Aydin et al. [ 15 ] and Aydin & Tan [ 47 ] both achieved 85% accuracy using SVM with EEG features related to hemispheric dependence and frequency bands. O. Tan et al. [ 16 ] reported a notably higher accuracy of 94.75% using Global Field Synchronization (GFS) features in the delta band. Altuğlu et al. [ 17 ] utilized Approximate Entropy (ApEn) features in the beta band with a Random Forest classifier, reaching 89.66% accuracy, while Ma et al. [ 48 ] applied EEG microstate analysis combined with entropy-based features and machine learning, achieving a accuracy of 85%.


#### Table 7.

Comparison of the classification accuracy of OCD and HC with other previous studies



| References | Number of subjects | Feature Sets | Classifier | The most discriminative features | Best classification accuracy | Independent Test Set |
| --- | --- | --- | --- | --- | --- | --- |
| Aydin et al. 2015 [ 15 ] | 10 OCD patients and 10 HC | the complexity and hemispheric dependence features of the EEG | SVM | the complexity and hemispheric dependence features of the EEG | 85% | No |
| O. Tan, Özçoban, and Aydın 2016 [ 16 ] | 15 OCD patient and 15 HC | Global Field Synchronization, GFS | SVM | GFS features in the delta band. | 94.75% | No |
| Altuğlu et al. 2020 [ 17 ] | 29 treatment-resistant and 28 treatment-responsive OCD patients | ApEn | RF | ApEn features based on the beta frequency band | 89.66% | No |
| Aydin, S., Tan, O., 2017 [ 47 ] | 10 OCD patients, 10 HC | Frequency Band Features (Delta, Theta, Alpha, Beta) | SVM | Frontal-occipital, frontal-parietal, occipital features | 85% | No |
| Ma, MH., Lu, BX., Zhang, Y., 2025 [ 48 ] | 48 OCD patients, 52 HC | EEG Microstate Analysis | Machine Learning | Microstate transitions (B to C), sample entropy, Lempel-Ziv complexity | 85% | No |
| Present study | Dataset1: 35OCD,37 HC Dataset2:21OCD, 21HC | Synchronicity, spectral characteristics, nonlinear complexity | LightGBM | PLV | 86.6% (Dataset 1), 83.3% (Dataset 2) | Yes |


Although some prior studies reported high classification accuracy, they often lacked independent validation and model interpretability. In contrast, our study incorporated both an external test dataset and SHAP-based feature attribution analysis, which not only ensured more reliable performance estimates but also provided valuable insights into the model’s decision-making process. These methodological improvements contribute to advancing OCD-related neurobiological understanding and support the clinical potential of explainable machine learning in psychiatric diagnosis.


### Limitations and future directions

While the findings of this study are promising, there are still several limitations to consider for future research. First, although two independent datasets were utilized to evaluate generalizability, the sample size in each dataset is moderate. In addition, because the patient group consisted of pharmacologically treated individuals while controls were medication-naïve, potential drug effects on EEG activity cannot be fully excluded, which may confound the interpretation of findings as core neurophysiological features of OCD. Second, future research should incorporate larger, multi-site cohorts to enhance external validity and better capture clinical heterogeneity. Lastly, although SHAP was employed to enhance model interpretability, it remains a model-specific approach and does not inherently capture underlying neurobiological causality. Beyond diagnostic applications, future studies should also address clinically meaningful aspects such as predicting treatment response, stratifying symptom severity, and identifying comorbid conditions, which would further enhance translational value. Future work should also explore more biologically grounded interpretability frameworks to bridge the gap between algorithmic decision-making and clinical neuroscience.


## Conclusion

This study presents an interpretable EEG-based machine learning framework for OCD classification. PLV-based functional connectivity features, combined with the LightGBM model, achieved superior accuracy and generalizability across datasets. SHAP analysis further enhanced interpretability by highlighting potentially clinically relevant biomarkers. These findings support the potential of PLV as a robust EEG biomarkerfor OCD and underscore the value of integrating explainable machine learning into neuropsychiatric diagnostics.


## Supplementary Information

Below is the link to the electronic supplementary material.


## Acknowledgements

We gratefully acknowledge Xiangying Ran from the School of Medical Engineering, Xinxiang Medical University, and Dr. Yongfeng Yang from the Physiotherapy Center at the Second Affiliated Hospital of Xinxiang Medical University for their valuable support for this research. We also acknowledge the use of the publicly available dataset Two Decades Brainclinics Research Archive for Insights in Neurophysiology (TDBRAIN) in this study.





## Funding

This work was supported by the National Natural Science Foundation of China (Nos. 82201709, 82302298, and 82572359), This work was supported by the National Natural Science Foundation of China (No. 82201709 and 82302298), the Science and Technology Research Project of Henan Province (No. 242102310055, 232102310009, 242102310005, 242102521012), the Open Project Program of Henan Collaborative Innovation Center of Prevention and Treatment of Mental Disorder (No. XTkf07, XTkf01, XTgh02, XTgh01), the Open Project Program of the First Affiliated Hospital of Xinxiang Medical University (No.XZZX2022009), the Innovative Research Team (in Science and Technology) in University of Henan Province (No. 24IRTSTHN042), Major science and technology projects of Henan Province (No. 221100310500), the Open Program of Henan Key Laboratory of Biological Psychiatry (No. ZDSYS2022008), the Science and Technology Research Program Project of Xinxiang City (No. GG2021013), the Open Program of Henan Clinical Research Center for Mental Disorders (No. 2021-zxkfkt-007), and the Henan Province medical science and technology research plan joint construction project (No. LHGJ20230539).


## Data availability

The datasets generated and/or analysed during the current study are not publicly available due to participant privacy and ethical restrictions, but are available from the corresponding author on reasonable request.


## Declarations


### Ethics approval and consent to participate

All procedures performed in studies involving human participants were in accordance with the ethical standards of the institutional and/or national research committee and with the 1964 Helsinki declaration and its later amendments or comparable ethical standards. Written informed consent was obtained from all participants or their legal guardians/next of kin, as documented in the original study.


### Consent for publication


### Competing interests

The authors declare no competing interests.


## Footnotes

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.



## Contributor Information

Zongya Zhao, Email: [EMAIL_REDACTED].

Zhaohui Zhang, Email: [EMAIL_REDACTED].

Zihao Xu, Email: [EMAIL_REDACTED].

Yi Yu, Email: [EMAIL_REDACTED].

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials


### Data Availability Statement

The datasets generated and/or analysed during the current study are not publicly available due to participant privacy and ethical restrictions, but are available from the corresponding author on reasonable request.
