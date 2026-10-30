# De-Identified Manuscript `ANON_119`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Purpose: Accurate survival prediction is essential for optimizing the treatment planning in patients with castration-resistant prostate cancer (CRPC). However, the traditional statistical models often underperform due to limited variable inclusion and an inability to account for complex, multidimensional data interactions. Methods: We retrospectively collected 46 clinical, laboratory, and pathological variables from 801 patients with CRPC, covering the disease course from the initial disease diagnosis to CRPC progression. Multiple machine learning (ML) models, including random survival forests (RSFs), XGBoost, LightGBM, and logistic regression, were developed to predict cancer-specific mortality (CSM), overall mortality (OM), and 2- and 3-year survival status. The dataset was split into training and test cohorts (80:20), with 10-fold cross-validation. The performance was assessed using the C-index for regression models and the AUC, accuracy, precision, recall, and F1-score for classification models. Model interpretability was assessed using SHapley Additive exPlanations (SHAP). Results: Over a median follow-up of 24 months, 70.6% of patients experienced CSM. RSFs achieved the highest C-index in the test set for both CSM (0.772) and OM (0.771). For classification tasks, RSFs demonstrated a superior performance in predicting 2-year survival, while XGBoost yielded the highest F1-score for 3-year survival. The SHAP analysis identified time to first-line CRPC treatment and hemoglobin and alkaline phosphatase levels as key predictors of survival outcomes. Conclusion: The RSF and XGBoost ML models demonstrated a superior performance over that of traditional statistical methods in predicting survival in CRPC. These models offer accurate and interpretable prognostic tools that may inform personalized treatment strategies. External validation and the integration of emerging therapies are warranted for broader clinical applicability.

Keywords: machine learning, prediction algorithms, prostatic neoplasms, castration-resistant, survival


## 1. Introduction

Advanced prostate cancer (PCa) can initially be managed effectively through androgen deprivation therapy (ADT); however, the majority of patients eventually develop castrate resistance [ 1 ]. The introduction of multiple lines of systemic therapies, including novel androgen receptor pathway inhibitors, taxane-based chemotherapies, radiopharmaceuticals, and poly (ADP-ribose) polymerase inhibitors, has led to improvements in the overall survival of patients with castration-resistant PCa (CRPC) [ 2 , 3 , 4 ]. Nonetheless, the prognosis remains poor and heterogeneous across different patient subgroups.

With the expansion of the treatment choices for CRPC, there is a growing need for accurate survival predictions to optimize the treatment sequencing. However, the traditional statistical methods fail to take into account the nonlinear and multidimensional associations between biological factors in CRPC and the multitude of sequenced therapies during each landscape of the disease. Studies have explored prognostic models regarding OS predictions for patients with CRPC [ 5 ]. However, the predictive performance reported has been modest, ranging between 0.62 and 0.79, presumably due to the limited sample sizes and restricted clinicopathological variables included in the analyses and the reliance on traditional statistical methods that assessed the outcomes based on arbitrarily defined risk groups. Indeed, the performance of survival prediction models could potentially be improved by including larger patient cohorts and a broader range of input variables, as well as by incorporating machine learning (ML) techniques [ 5 ].

ML has recently gained popularity in survival predictions due to its capacity to process complex and high-dimensional datasets, enabling highly accurate predictive modeling. Compared to the traditional statistical approaches, such as Cox proportional hazards models or Kaplan–Meier analysis, ML methods have demonstrated superior predictive accuracy, particularly in scenarios involving numerous variables. Studies across various cancer types have reported that ML models can achieve predictive accuracies ranging from approximately 70% to 90% and root mean square errors below 20 in regression-based survival analyses [ 6 , 7 ]. Despite these promising outcomes, ML techniques have not yet been extensively applied to datasets specific to patients with CRPC. Given the heterogeneity and therapeutic complexity of CRPC, the utilization of ML may potentially provide more individualized and precise survival estimates.

This study aimed to develop and compare multiple ML models for predicting the survival time before cancer-specific mortality (CSM) and overall mortality (OM) and the 2-year and 3-year survival status after a CRPC diagnosis by utilizing a comprehensive set of demographical and clinicopathological variables. We sought to identify the most accurate and reliable ML model for guiding clinical decision-making.


## 2. Materials and Methods


### 2.1. Data Collection

Clinical, laboratory, and pathological data comprising 46 variables at the time of the initial PCa diagnosis and at the time of progression to CRPC were retrospectively collected from 801 consecutive patients diagnosed with CRPC at two institutions from January 2005 to February 2022. CRPC was defined according to the Prostate Cancer Working Group 2 criteria. Patients were excluded if their clinical data were incomplete, if their treatment deviated from the standard recommendations, or if cause of death or survival status could not be identified.

Data on CRPC treatments were collected, including the type of therapeutic agent (abiraterone acetate, enzalutamide, cabazitaxel, docetaxel, and olaparib) and the durations of the first, second, and third lines of treatment until disease progression. The sequence of administered agents was determined at the physician’s discretion and according to patient preference. The treatment regimens included intravenous docetaxel (75 mg/m 2 ) and cabazitaxel (20 mg/m 2 ) administered every three weeks in combination with oral prednisone (5–10 mg); enzalutamide (160 mg); abiraterone (1000 mg) combined with prednisolone (5–10 mg); and olaparib (300–600 mg). Each line of treatment was maintained until disease progression, the development of unacceptable toxicity, or patient refusal.

Survival status and cause of death were determined using data from the National Cancer Registry Database or institutional medical records. Deaths were attributed to CRPC if there was documented progression of metastatic CRPC or if death resulted from treatment-related complications.


### 2.2. The Study Endpoints

The primary endpoint of this study was to develop ML models predicting CSM, OM, and 2-year and 3-year survival status following the diagnosis of CRPC. The secondary study endpoint was to evaluate the discriminative performance and calibration of the developed models.


### 2.3. Statistical Analyses


#### 2.3.1. Data Processing

To prepare the dataset, key variables were derived, including the time interval (months) between the CRPC diagnosis and either death or the last follow-up; %PSA changes from the initial PCa diagnosis to the initiation of ADT; durations and %PSA changes between PCa diagnosis and ADT initiation; risk group stratification based on the LATTITUDE (high-risk) and CHAARTED (high-volume) criteria; and neutrophil-to-lymphocyte ratio. To classify the survival outcomes, 2-year survival status and 3-year survival status after a CRPC diagnosis were encoded as binary variables.

Missing data were addressed using imputation methods based on the type of variable. For numeric variables, missing values were imputed using multiple iterative imputations with Bayesian ridge regression and mean-based strategies. For categorical variables, imputation was performed using the most frequent category. Cases with missing outcome data were excluded from the analysis. The final dataset was randomized into training and validation sets using an 80:20 split for cross-validation.


#### 2.3.2. Model Development

Survival periods and binary survival status were predicted using both regression and classification approaches. In the regression models, the target variable was survival time in months after CRPC diagnosis. In the classification models, binary outcomes represented the 2-year and 3-year survival status.

Regression models were developed using a Cox proportional hazard analysis, random survival forests (RSFs), and extreme gradient boosting (XGBoost). The classification models were developed using logistic regression, Light Gradient-Boosting Machine (LightGBM), XGBoost, and random forest algorithms. The best-performing model in each category was selected as the final predictive model.

Supplementary Tables S1 and S2 provide details on the regression and classification models applied, including the corresponding hyperparameters and search ranges used during model tuning. We employed 10-fold cross-validation and optimized the model hyperparameters using grid search, with all model development conducted using the Optuna optimization framework in Python (version 3.12.7).


#### 2.3.3. Model Performance Interpretation

Regression models, which generate survival time predictions, were evaluated using Harrell’s concordance index (C-index) to assess their discriminative performance. For the classification models, which produced the categorical survival status predictions, their performance was evaluated using accuracy, the area under the receiver operating characteristic curve (AUC), mean precision, mean recall, and F1-score.

To enhance interpretability, the final models were analyzed using the SHapley Additive exPlanations (SHAP) framework. SHAP quantifies the contribution of each input variable to the model predictions, enabling an understanding of the feature importance behind individual predictions.


### 2.4. Ethical Considerations

This study was approved by the Institutional Ethics Committee of Yonsei University Health System (approval number: 3-2016-0190) following a review of the study protocol. All procedures were conducted in accordance with the ethical standards of the Declaration of Helsinki (1946) and its most recent revision in 2008.


## 3. Results


### 3.1. Patient Characteristics

The baseline demographic and clinicopathological characteristics of the patients at the time of the initial PCa diagnosis and at progression to CRPC are presented in Table 1 . Over a median follow-up period of 24.0 months (interquartile range: 12.0–43.0 months), 566 cancer-specific deaths (70.6%) and 588 overall deaths (73.4%) were observed. The type and distribution of systemic agents administered according to the treatment lines are provided in Supplementary Table S3 .


#### Table 1.

Clinical, laboratory, and pathological characteristics.



| Number | 801 |
| --- | --- |
| At initial PCa diagnosis |  |
| Body mass index (kg/m 2 ) | 24.0 (21.6–25.7) |
| PSA (ng/mL) | 65.6 (18.2–280.9) |
| PSA density (ng/mL/cc) | 1.58 (0.47–6.21) |
| Gleason score |  |
| ≤7 | 131 (16.4%) |
| ≥8 | 670 (83.6%) |
| Extent of metastasis |  |
| Bone | 439 (54.7%) |
| Lymph node | 283 (35.3%) |
| Lung | 43 (5.4%) |
| Liver | 13 (1.6%) |
| NCCN risk category |  |
| Intermediate | 36 (4.5%) |
| High | 765 (95.5%) |
| Clinical T stage |  |
| ≤T2 | 115 (14.4%) |
| ≥T3 | 686 (85.6%) |
| Clinical N1 stage |  |
| N0 | 395 (49.3%) |
| N1 | 406 (50.7%) |
| Clinical M1 stage |  |
| M0 | 356 (44.4%) |
| M1 | 445 (55.6%) |
| Type of definitive treatment |  |
| Radical prostatectomy | 96 (12.0%) |
| Radiation therapy with or without ADT | 243 (30.3%) |
| ADT alone | 462 (57.7%) |
| PSA level at ADT initiation | 46.6 (10.0–255.5) |
| Duration from ADT administration to CRPC (months) | 0.0 (0.0–3.0) |
| At CRPC progression |  |
| Age (years) | 70.0 (65.0–76.0) |
| Presence of SPM | 68 (8.5%) |
| Presence of SPM before CRPC progression | 50 (6.2%) |
| Comorbidity |  |
| Hypertension | 332 (41.4%) |
| Diabetes mellitus | 162 (20.2%) |
| Pulmonary tuberculosis history | 29 (3.6%) |
| Liver cirrhosis | 5 (0.6%) |
... (35 rows truncated) ...


Data are given as numbers (%) and medians (interquartile range). ADT = androgen deprivation therapy; CCI = Charlson Comorbidity Index; CRPC = castration-resistant prostate cancer; ECOG = Eastern Cooperative Oncology Group; NCCN = National Comprehensive Cancer Network; PCa = prostate cancer; PSA = prostate-specific antigen; SPM = second primary malignancy; WBC = white blood cell.

The 2-year and 3-year cancer-specific survival rates were 18.7% and 13.5%, respectively, while the 2-year and 3-year overall survival rates were 17.7% and 13.0% ( Table 2 ). These survival outcomes were observed to be consistent with previously published real-world data on the prognosis of CRPC [ 8 ]. Kaplan–Meier curves for the cancer-specific and overall survival were generated, with time defined as the interval from a CRPC diagnosis to death or the last follow-up ( Figure 1 ).


#### Table 2.

Summary of 2-year and 3-year survival in patients with CRPC.



|  | Cancer-Specific Survival (%) | Overall Survival (%) |
| --- | --- | --- |
| 2-year | 18.7% | 17.7% |
| 3-year | 13.5% | 13.0% |



#### Figure 1.


> **Figure/Table Caption:** Kaplan–Meier curves for cancer-specific survival and overall survival.

Comparisons between groups were performed using Welch’s t -test for continuous variables and the chi-square test for categorical variables. All tests were two-sided, and p -values were reported accordingly.


### 3.2. Comparison of Model Performance

Table 3 presents the models’ performance on the test dataset comprising 160 patients. Among the models evaluated, RSFs demonstrated a strong performance for both CSM and OM predictions. In the validation cohort, XGBoost with internal imputation achieved the highest C-index for both outcomes: 0.771 for CSM (95% CI 0.706–0.836) and 0.773 for OM (95% CI 0.708–0.838). RSFs ranked second in the validation set, with C-index values of 0.764 for CSM (95% CI 0.698–0.830) and 0.771 for OM (95% CI 0.706–0.836).


#### Table 3.

Performance of regression models.



|  | Cox | RSF | XGB | XGB (With Its Own Imputation) |
| --- | --- | --- | --- | --- |
| Valid score | CSM | 0.685 | 0.764 | 0.761 | 0.771 |
| 95% CI | 0.656–0.714 | 0.698–0.830 | 0.695–0.827 | 0.706–0.836 |
| OM | 0.6934 | 0.771 | 0.770 | 0.773 |
| 95% CI | 0.665–0.722 | 0.706–0.836 | 0.705–0.835 | 0.708–0.838 |
| Test score | CSM | 0.6210 | 0.772 | 0.770 | 0.753 |
| 95% CI | 0.590–0.652 | 0.707–0.837 | 0.705–0.835 | 0.686–0.820 |
| OM | 0.6130 | 0.771 | 0.756 | 0.765 |
| 95% CI | 0.584–0.642 | 0.706–0.836 | 0.689–0.823 | 0.699–0.831 |


CI = confidence interval; CSM = cancer-specific mortality; OM = overall mortality; RSF = random survival forest; XGB = extreme gradient boosting.

However, in the test set, RSFs outperformed all of the other models, achieving the highest C-index for both CSM (0.772, 95% CI 0.707–0.837) and OM (0.771, 95% CI 0.706–0.836). XGB ranked third, with C-indices of 0.753 (95% CI 0.686–0.820) for CSM and 0.765 (95% CI 0.699–0.831) for OM, respectively. This indicated a tendency toward overfitting, as the test score was lower than the validation score. From a model generalizability perspective, RSFs appeared to offer a more robust and reliable performance across datasets.

For 2-year survival predictions, the RSF model achieved the best overall performance as follows: accuracy: 0.750; AUC: 0.820; recall: 0.787; mean precision: 0.744; F1-score: 0.764 ( Table 4 ). This was followed by XGBoost and LightGBM. For 3-year survival predictions, RSFs again showed the highest accuracy (0.751), AUC (0.822), and mean precision (0.690). However, XGBoost showed the best recall (0.493) and F1-score (0.545), metrics that are particularly important for evaluating performance in imbalanced classification tasks. Given the balanced nature of the F1-score in terms of both precision and recall, XGBoost was considered more generalizable for long-term survival predictions. In both the 2-year and 3-year predictions, all models outperformed the traditional methods, such as logistic regression and Cox proportional hazard modeling, highlighting the potential of ML approaches for more accurate survival classification in CRPC patients.


#### Table 4.

Performance of classification models.



|  | Model | Accuracy | AUC | Recall | Precision | F1-Score |
| --- | --- | --- | --- | --- | --- | --- |
| 2-year survival | Logistic Regression | 0.6356 | 0.7271 | 0.6818 | 0.6353 | 0.6528 |
| LightGBM | 0.7107 | 0.8074 | 0.7442 | 0.7078 | 0.7236 |
| XGB | 0.7198 | 0.8138 | 0.7586 | 0.7151 | 0.7350 |
| Random Forest | 0.7504 | 0.8196 | 0.7868 | 0.7443 | 0.7640 |
| 3-year survival | Logistic Regression | 0.7183 | 0.7069 | 0.3105 | 0.5958 | 0.3993 |
| LightGBM | 0.7432 | 0.8017 | 0.4817 | 0.6275 | 0.5375 |
| XGB | 0.7485 | 0.7861 | 0.4925 | 0.6246 | 0.5452 |
| Random Forest | 0.7506 | 0.8224 | 0.3905 | 0.6903 | 0.4818 |


LightGBM = Light Gradient-Boosting Machine; XGB = extreme gradient boosting.


### 3.3. Attribute Weights

The SHAP summary plots ( Figure 2 and Figure 3 ) illustrate the overall impact and distribution of the individual risk variables, ranked in descending order of importance. In the CSM model ( Figure 2 ), the most influential feature was the time interval from a CRPC diagnosis to the initiation of first-line therapy. Other top-ranked predictors included baseline hemoglobin and alkaline phosphatase (ALP) levels at CRPC diagnosis and the duration from an initial PCa diagnosis to ADT initiation. Notably, these same variables were also identified as the most influential features in the corresponding OM model ( Figure 3 ), indicating their consistent prognostic relevance across different survival endpoints.


#### Figure 2.


> **Figure/Table Caption:** SHAP summary plot for XGB regression model based on CSM.


#### Figure 3.


> **Figure/Table Caption:** SHAP summary plot for XGB regression model based on OM.


## 4. Discussion

The quality of the data preparation plays a critical role in the performance of ML algorithms, especially in CRPC survival predictions, where the outcomes are influenced by a complex interplay between clinical and biological factors. The key strength of our study is the use of the largest and most comprehensive CRPC dataset to date, incorporating 46 clinical, laboratory, and pathological variables, spanning the full disease landscape, from an initial PCa diagnosis to death. To our knowledge, this is the first study to apply a multi-model ML-based approach to survival prediction specifically in patients with CRPC, representing a significant step forward in precise prognostication.

While numerous studies have explored survival prediction in PCa, they have largely focused on localized disease, often utilizing deep learning models trained on large and relatively homogeneous patient populations [ 9 ]. In contrast, our study uniquely targeted a CRPC population, which is typically smaller in its sample size and more heterogeneous in its clinical features. For instance, Dai et al. reported a C-index of up to 0.85 using deep learning models for localized PCa cohorts, benefiting from more uniform disease characteristics and a greater data volume [ 10 ]. Despite working with a more complex dataset, our ML models achieved a robust predictive performance, with C-indices up to 0.77. These results indicate the potential of ML in demonstrating a robust predictive performance in a substantially more complex clinical setting. These findings highlight the potential of ML in CRPC and suggest that future applications of deep learning, customized to the intricacies of advanced disease, may improve the prognostic accuracy further.

By incorporating a broad range of input variables and comparing multiple ML algorithms, we demonstrated that survival predictions for CRPC can be significantly improved over those of the traditional statistical methods. Our top-performing models achieved C-indices of 0.772 for CSM and 0.771 for OM in the test set, substantially higher than the C-index of 0.67 reported by Moreira et al., who utilized Cox proportional hazard models to predict the OM in a smaller dataset of 205 patients and 14 variables [ 11 ]. These findings highlight the importance of both dataset comprehensiveness and algorithmic calculations in achieving a superior predictive performance.

Saito et al. reported ML-based survival prediction models for PCa patients treated with ADT, achieving a C-index of 0.74 using an RSF. Although their survival tree model achieved a higher C-index of 0.85 in metastatic PCa patients, it lacked generalizability to non-metastatic cases [ 12 ]. In contrast, our study included a broader CRPC population and evaluated multiple ML algorithms, including RSFs, XGBoost, LightGBM, and logistic regression, allowing for a more comprehensive comparison. Although the C-indices of our model were relatively lower than those reported, our models demonstrated a superior overall performance for both metastatic and non-metastatic CRPC patients, supporting more generalized applicability in real-world clinical practice.

In our analysis, XGBoost demonstrated a higher performance in the validation set; however, it showed a relative decline in the test set, indicating a tendency toward overfitting. This reflects a limitation of XGBoost, which may capture noise or idiosyncrasies in the training set rather than generalizable prognostic patterns. Overfitting not only diminishes the predictive stability but may also restrict the clinical utility when models are applied to external populations. To mitigate this issue, we applied several strategies, including hyperparameter optimization using grid search within a 10-fold cross-validation framework; the application of regularization parameters (e.g., L1 and L2) embedded within algorithms such as XGBoost and LightGBM; and an evaluation of the model’s generalizability through a performance assessment on an independent test set. Additional approaches, such as stricter regularization, early stopping to prevent over-training, or dimensionality reduction by prioritizing features with stronger prognostic value, could be considered in future studies to reduce the risk of overfitting further. To balance accuracy with generalizability, RSFs and LightGBM were combined with XGBoost as a hybrid approach. Ultimately, the most critical step would be external validation on independent cohorts, which would confirm the robustness and support the generalizability of the models.

A key advantage of our approach is the integration of SHAP, which improved the interpretability of our ML models by quantifying the individual contribution of each input variable. Among the top-ranked predictors for both CSM and OM were the time interval from CRPC diagnosis to the initiation of first-line systemic therapy and baseline hemoglobin and ALP levels at the time of CRPC diagnosis. Notably, traditional prognostic indicators such as age, Gleason grade, and baseline PSA contributed minimally to the models, indicating a shift in prognostic relevance toward more dynamic, treatment-related, and biochemical variables in the advanced-disease setting.

These findings are consistent with the existing clinical literature. Prior studies have identified anemia and elevated or rapidly increasing ALP levels as strong, independent predictors of a poor prognosis in mCRPC, particularly in large cohorts treated with docetaxel or cabazitaxel [ 13 , 14 ]. Imaging-based investigations have also emphasized the prognostic significance of ALP kinetics [ 15 ]. In contrast, conventional variables such as Gleason grade and PSA appeared to lose prognostic relevance after progression to the castration-resistant state. This aligns with recent meta-analyses and PSMA–PET-based studies, which similarly reported a limited or no survival impact of Gleason grade in the mCRPC setting [ 16 , 17 ]. Taken together, these data support a paradigm shift in which survival prediction models in advanced PCa may benefit from prioritizing systemic and bone turnover markers, such as Hb and ALP, over the traditional histopathologic or laboratory prognosticators.

Several limitations must be acknowledged. First, the absence of an external validation cohort limits the generalizability of our results. Second, our dataset spans an 18-year period (2005–2022) during which substantial advancements in the systemic therapies for CRPC occurred. During this period, novel agents such as androgen-receptor-axis targeted therapies (e.g., abiraterone, enzalutamide), cabazitaxel, and various combination or sequential strategies were gradually introduced. These therapeutic shifts may have significantly influenced the survival outcomes and consequently affected the predictive performance of our models. Era-based sensitivity analyses to account for temporal heterogeneity were considered; however, the irregular timing of therapeutic changes and resultant heterogeneity within subgroups limited the feasibility and statistical reliability of such analyses. Finally, recently approved agents not represented in our cohort, including darolutamide, pembrolizumab, and rucaparib, may impact survival outcomes further. Incorporating these therapies into future studies, along with external validation using contemporary cohorts, will be essential to enhance the predictive accuracy, clinical relevance, and generalizability of our models.


## 5. Conclusions

Using a large, comprehensive dataset and multiple ML algorithms, we demonstrated that XGBoost and RSFs can substantially outperform the traditional statistical methods in predicting the CSM and OM in patients with CRPC. Importantly, the application of SHAP improved the model interpretability by identifying clinically meaningful prognostic factors, which may support individualized treatment planning. Future studies should focus on model refinement, the incorporation of emerging therapeutic agents, and external validation to ensure broad clinical applicability and translation into real-world practice.


## Supplementary Materials

The following supporting information can be downloaded at https://www.mdpi.com/article/[REDACTED_DOI]/s1 . Table S1: Hyperparameter settings and ranges for regression models; Table S2: Hyperparameter settings and ranges for classification models; Table S3: Distribution of systemic agents administered according to treatment lines.



Conceptualization: J.H.L. and K.C.K. Data curation and formal analysis: J.J. Funding acquisition: K.C.K. Investigation and methodology: J.H.L., Y.J.A. and J.J. Project administration and supervision: K.C.K. Visualization: J.J. Writing—original draft: J.H.L. Writing—review and editing: K.S.L., J.S.L., S.H.L., W.S.H. and B.H.C. All authors have read and agreed to the published version of the manuscript.


## Institutional Review Board Statement

This study was approved by the Institutional Ethics Committee of Yonsei University Health System (approval number: 3-2016-0190)(approval date: 17 February 2017) following a review of the study protocol. All procedures were conducted in accordance with the ethical standards of the Declara-tion of Helsinki (1946) and its most recent revision in 2008.


## Informed Consent Statement

Informed consent was not required for the purposes of this study, as it was based upon retrospective anonymous patient data and did not involve patient intervention or the use of human tissue samples.


## Conflicts of Interest

Author Jaeyun [AUTHOR] is affiliated with SKTelecom. The company had no role in the design, execution, interpretation, or writing of this study. All other authors declare no conflicts of interest.


## Funding Statement

This study was supported by a research grant from the Korea Health Industry Development Institute (HC19C016401).


## Footnotes

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials
