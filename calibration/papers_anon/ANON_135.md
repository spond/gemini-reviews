# De-Identified Manuscript `ANON_135`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Introduction

Abdominal aortic aneurysm (AAA) is a catastrophic aortic disease characterized by focal expansion of the abdominal aorta [ 1 ], and contributes substantially to global morbidity and mortality burden due to its life-threatening complication - AAA rupture [ 2 , 3 ]. As AAA typically develops slowly without evident symptoms, approximately half of patients experience aneurysm rupture as their initial clinical manifestation. Left untreated, the mortality rate can reach nearly 100%, and even with surgical repair, it remains as high as 50%, which has not changed over the years despite advancements in medical technology [ 4 ].

Identifying individuals at higher risk of developing AAA and screening this population for asymptomatic AAA will lead to a timely management to prevent an aneurysm from growing and even rupturing. However, historical screening program based on conventional risk factors of AAA did not perform well. The National Health Service (NHS) Abdominal Aortic Aneurysm Screening Program (NAAASP) screened 1 million men in England aged 65 years for ultrasound only identified 3000 + with large AAAs who were referred for possible intervention [ 5 ]. A better screening strategy with higher identification rate of positive cases is therefore needed.

Chronic aortic inflammation has been recognized as a crucial histological feature of AAA involving the local infiltration of inflammatory cells, including monocytes, lymphocytes, and plasma cells, predominantly located in the outer part of the aorta [ 6 ]. These will eventually lead to the damage of aortic wall and the dysfunction of vascular smooth muscle cell [ 7 ]. However, whether chronic systemic inflammation impacts the onset, growth, and prognosis of AAA remains uncertain. Previous research has yielded inconsistent findings, with some studies showing a positive association between C-reactive protein (CRP) levels and the prognosis of AAA, while others have not [ 8 – 12 ], acknowledging the sample sizes of these studies were too small to yield robust evidence. Large population-based cohort studies are therefore needed to provide more definitive evidence.

In addition, how chronic systematic inflammation influencing the development and progression of AAA may vary among patient groups with different characteristics. As the heritability of AAA is estimated to be up to 70% [ 13 ], genome-wide association studies have been widely used to identify new susceptibility genes for AAA recently. The polygenetic risk score (PRS) of AAA would hopefully provide supplementary risk information beyond conventional risk factors. A previous study reported that individuals with a 1-SD increase in PRS carries a 26% increased risk of AAA [ 14 ]. Another study revealed that PRS-stratified screening could be more cost-effective than traditional screening approaches, and their modelling suggests inviting male current smokers with high PRS earlier than 65 and screening female smokers with high/intermediate PRS at 65 and 70 respectively, may improve cost-effectiveness [ 15 ]. Using population-based data of the UK Biobank, this study aimed to investigate the association between chronic systematic inflammation, measured by inflammatory markers in peripheral blood, and the risk of AAA development as well as its interactions with genetic predisposition and major AAA risk factors including age, sex, hypertension and smoking.


## Methods


### UK biobank and study participants

The UK Biobank prospective population-based cohort study has successfully enrolled over 500,000 participants from 22 centers across the UK between 2006 and 2010 [ 16 ]. Extensive biological and medical information were collected through questionnaires, physical measurements, verbal interviews, health records, blood sample assays, genotyping and, imaging. The UK Biobank is openly accessible to its approved applicants ( https://www.ukbiobank.ac.uk/ ).


### Outcomes measures

AAA cases were defined as individuals with International Classification of Disease (ICD)−10 diagnosis of AAA (I71.3- abdominal aortic aneurysm, ruptured; I71.4- abdominal aortic aneurysm, without mention of rupture). The follow-up for AAA event started from the recruitment until AAA diagnosis, death, or the Dec 31 st 2022 (the last follow-up visit), whichever occurred first. Exclusion criteria include: participants had any history of aortic aneurysm and dissection prior to baseline ( n = 584), participants without available data for blood tests at baseline visit ( n = 46,719), and participants had conditions at baseline that could impact the levels of systemic inflammatory markers and the AAA incidence ( n = 183,996), including malignant neoplasms, blood and blood-forming organ diseases, autoimmune diseases, chronic inflammatory conditions and connective tissue disease (Supplemental Table S1) [ 17 , 18 ].


### Measurement of systemic inflammatory markers

Nine markers considered to be useful for diagnosing and predicting the prognosis of inflammation-related diseases were included in this study [ 19 , 20 ]. Serum CRP and other blood cell markers including absolute lymphocytes, monocytes, neutrophils, and platelets counts were obtained from blood tests of UKB participants attending the initial assessment visit. Four additional novel indicators of systemic inflammation reflecting the balance of innate immunity and adaptive immunity were included and calculated based on peripheral blood cell counts. These include neutrophil-to-lymphocyte ratio (NLR), platelet-to-lymphocyte ratio (PLR), lymphocyte-to-monocyte ratio (LMR), and systemic immune-inflammation index (SII; neutrophils × platelets/lymphocytes). As the sample size of repeated blood measurements was small (4.06% of UKB participants who completed initial measurement received repeated blood measurements), and measurements performed later were closer in time to diagnosis of AAA and might therefore more likely be secondary to the disease, only the blood test data at the initial assessment visit were extracted. The descriptions of systemic inflammatory markers are presented in Supplemental Table S2. Prior to statistical analysis, systemic inflammatory markers were log 10-transformed due to skewed distributions and standardized to Z-scores to make biomarkers comparable between each other. Z score was calculated as (individual value – mean)/standard deviation (SD).


### Genetic data and polygenic risk score calculation

The imputed genetic data were derived from the UK Biobank, and details of the single nucleotide polymorphism (SNP) information regarding genotyping process, imputation, and stringent quality control have been described in previous literature [ 21 ]. We comprehensively took into account the AAA-related SNPs reported in two GWASs [ 22 , 23 ]. According to previous study, a total of 31 independent SNPs ( r 2 < 0·05 or 1000 kb apart, without linkage disequilibrium) were included. These SNPs were found to have a significant association with incident AAA in individuals of European ancestry, with a minor allele frequency >0·05 and P < 1 × 10 −5 [ 24 ]. Specific information about the SNPs is presented Supplemental Method. and we constructed polygenic risk score (PRS) based on the selected SNPs (details of PRS construction are described in Supplemental Method). Included participants were then categorized into low (Tertile 1), moderate (Tertile 2), and high (Tertile 3) genetic risk according to PRS.


### Covariates adjustment

Covariates were adjusted in the models in a stepwise manner (from model 1 to model 3). Model 1 only adjusted for age and sex. Given that socioeconomic status has been found to be associated with the levels of different inflammatory markers and cardiovascular diseases [ 25 – 27 ], model 2 additionally adjusted for socioeconomic (Townsend deprivation index [TDI] and education) and other known risk factors of AAA including smoking status, hypertension, ethnicity, and hypercholesterolemia. We further adjusted for the PRS in model 3.


### Statistical analysis

Baseline demographics were summarized for included participants with and without incident AAA and for excluded participants, presented as mean and SD for continuous variables and as number and percentage for categorical variables. Longitudinal associations between baseline levels of systemic inflammatory markers and incident AAA were examined with stepwise multivariable Cox proportional hazard regression models. Cumulative incidence of AAA over the follow-up was calculated using the cumulative incidence function of the Fine–Gray proportional sub-distribution hazards model. Restricted cubic splines with covariate adjustment (Model 3) were plotted to explore any non-linear relationship between CRP level and immunity cell counts and the risk of incident AAA. Three knots were placed at the 10th, 50th, and 90th percentiles according to Harell’s rules, and the median value of each inflammatory biomarker was chosen as a reference. The exposures were log 10-transformed to minimize the effect of outliers and to improve the interpretation of associational results referring to previous study [ 28 ].

To examine whether the association between systemic inflammatory markers and risk of AAA varied across individuals with different genetic predispositions, stratified analysis by the tertile of PRS of AAA was performed; p value for interaction was calculated by adding an interaction term in the Cox model. To identify other potential effect modifiers, additional subgroup analyses were conducted by major risk factors of AAA including age (< 65 versus ≥ 65), sex, smoking, and hypertension.

We examined the robustness of the results through several sensitivity analyses: (1) imputing missing values for all relevant exposures and covariates by linear interpolation, and repeating the analysis with the imputed dataset of included patients, (2) exclusion of extreme observations (> mean ± 3 SD) for all exposures and covariates, (3) using Fine-Gray competing risk model to control the influence of the competing risk of death.

Cox proportional hazard regressions was performed with SPSS (SPSS Statistics 23.0), and other statistical analyses were performed with R (version 4.2.2) and R packages (‘survival’, ‘rms’ and ‘cmprsk’ packages).


## Results


### Baseline characteristics

In this study, 271,068 participants aged 38–73 years (median: 55 years) were included. A flow chart of study design is shown in Fig. 1 . Baseline characteristics of included participants by AAA incidence are presented in Table 1 . Included participants with AAA were more likely to be male, white, current smokers, had college or university degree, and higher systolic blood pressure and lower cholesterol (all P < 0·05). In terms of the systemic inflammatory markers, patients with AAA have higher CRP, lymphocyte count, monocyte count, neutrophil count, NLR, and SII than those without AAA, and the platelet count in patients with AAA is lower than those without AAA (all P < 0·05). PLR and LMR did not differ between individuals with and without AAA.


#### Fig. 1.


> **Figure/Table Caption:** Flowchart of participant selection. AAA, Abdominal aortic aneurysm; PRS, Polygenic risk score


#### Table 1.

Baseline characteristics of included participants by AAA incidence



| Baseline characteristics | Participants without AAA ( N = 270440) | Participants with AAA ( N = 629) | P value |
| --- | --- | --- | --- |
| Age, years | 54·97 ± 8·08 | 62·99 ± 4·83 | <·001 |
| Age < 65 | 233,144 (86·21%) | 340 (54·05%) | <·001 |
| Age ≥ 65 | 37,295 (13·79%) | 289 (45·95%) |
| Sex |
| Male | 124,102 (45·9%) | 548 (87·1%) | <·001 |
| Female | 146,337 (54·1%) | 81 (12·9%) |
| Ethnicity |
| White | 253,416 (93·7%) | 617 (98·1%) | <·001 |
| Mixed | 1699 (0·6%) | 1 (0·2%) |
| Asian or Asian British | 5610 (2·1%) | 3 (0·5%) |
| Black or Black British | 4472 (1·7%) | 1 (0·2%) |
| Other ethnic groups | 5242 (1·9%) | 7 (1·1%) |
| Education |
| College or university degree | 33,528 (12·4%) | 54 (8·6%) | ·004 |
| Others | 236,911 (87·6%) | 575 (91·4%) |
| Townsend deprivation index | −1·39 ± 3·04 | −1·15 ± 3·10 | ·168 |
| Smoking status |
| Never | 156,124 (57·7%) | 130 (20·7%) | <·001 |
| Previous | 86,392 (31·9%) | 290 (46·1%) |
| Current | 26,786 (9·9%) | 206 (32·8%) |
| Missing | 1137 (0·4%) | 3 (0·5%) |
| SBP, mmHg | 138·59 ± 19·51 | 147·22 ± 21·16 | ·014 |
| DBP, mmHg | 82·22 ± 10·71 | 82·80 ± 11·03 | ·226 |
| Hypertension | 56,932 (21·05%) | 213 (33·86%) | <·001 |
| Total cholesterol, mmol/L | 5·72 ± 1·12 | 5·38 ± 1·29 | <·001 |
| Hypercholesterolemia | 183,396 (67·81%) | 339 (53·90%) | <·001 |
| C-reaction protein, mg/L | 2·24 ± 3·75 | 3·60 ± 5·46 | <·001 |
| Lymphocyte, 10 9 cells/L | 1·95 ± 0·64 | 2·06 ± 0·69 | <·001 |
| Monocyte, 10 9 cells/L | 0·47 ± 0·20 | 0·57 ± 0·20 | <·001 |
| Neutrophil, 10 9 cells/L | 4·13 ± 1·34 | 4·77 ± 1·74 | <·001 |
| Platelet, 10 9 cells/L | 252·36 ± 57·98 | 234·13 ± 52·58 | <·001 |
| NLR | 2·28 ± 1·05 | 2·55 ± 1·44 | <·001 |
| PLR | 140·62 ± 55·10 | 125·64 ± 51·59 | ·559 |
| SII | 578·01 ± 310·30 | 602·35 ± 437·13 | ·002 |
| LMR | 4·65 ± 3·10 | 4·02 ± 2·49 | ·096 |


Data presented as percentage for categorical variables and mean ± SD for continuous variables. P value is for comparison between participants without AAA and participants with AAA using chi-square test (for categorical variables) or two-tailed student’s t test (for continuous variables). Hypertension is defined as history of hypertension, regularly taking anti-hypertension medications, systolic blood pressure ≥ 140 mmHg, or diastolic blood pressure ≥ 90 mmHg, hypercholesterolemia is defined as total cholesterol ≥ 5·18 mmol/L. SI conversion factors: To convert cholesterol to mmol/L, multiply values by 0·0259

AAA Abdominal aortic aneurysm, SBP Systolic blood pressure, DBP Diastolic blood pressure, NLR Neutrophil-to-lymphocyte ratio, PLR Platelet-to-lymphocyte ratio, SII Systemic immune-inflammation index, LMR Lymphocyte-to-monocyte ratio, SD Standard deviation


### Systemic inflammatory markers and AAA risk

Over a median (interquartile range, IQR) follow-up of 13·89 (13·17 − 14·61) years, 629 incident AAA was recorded. In the analysis with a full covariate adjustment (Model 3), per SD increase in baseline CRP and both adoptive immunity marker (lymphocyte) and innate immunity markers (monocyte, neutrophil) were all associated with a significantly higher risk of incident AAA (CRP: 1·46 [1·35, 1·58], lymphocyte: 1·17 [1·07, 1·27], monocyte: 1·27 [1·16, 1·38], neutrophil: 1·27 [1·17, 1·39], all p < 0·001). Per SD increase in log-transformed platelet counts and PLR (platelet-to-lymphocyte ratio) was associated with a lower risk of incident AAA (platelet: 0·90, 0·83 − 0·97, p = 0·005; PLR: 0·82 [0·76, 0·89], p < 0·001). Results were generally consistent in Model 1 and Model 2 (Table 2 ).


#### Table 2.

Multivariate Cox regression analyses of systemic inflammatory markers associated with AAA incidence



|  | Model 1 a | Model 2 b | Model 3 c |
| --- | --- | --- | --- |
| HR(95%CI) | P value | HR(95%CI) | P value | HR(95%CI) | P value |
| CRP | 1·624 (1·505, 1·753) | <·001 | 1·461 (1·350, 1·582) | <·001 | 1·464 (1·352, 1·585) | <·001 |
| Lymphocyte | 1·318 (1·219, 1·426) | <·001 | 1·169 (1·075, 1·270) | <·001 | 1·166 (1·072, 1·268) | <·001 |
| Monocyte | 1·429 (1·315, 1·552) | <·001 | 1·272 (1·168, 1·386) | <·001 | 1·265 (1·161, 1·378) | <·001 |
| Neutrophil | 1·546 (1·419, 1·684) | <·001 | 1·272 (1·167, 1·388) | <·001 | 1·271 (1·165, 1·387) | <·001 |
| Platelet | 0·924 (0·854, 1·000) | ·050 | 0·898 (0·832, 0·970) | ·006 | 0·896 (0·830, 0·968) | ·005 |
| NLR | 1·115 (1·028, 1·210) | ·009 | 1·065 (0·981, 1·157) | ·135 | 1·067 (0·982, 1·160) | ·127 |
| PLR | 0·760 (0·706, 0·818) | <·001 | 0·821 (0·759, 0·887) | <·001 | 0·821 (0·758, 0·888) | <·001 |
| SII | 1·054 (0·971, 1·143) | ·207 | 0·996 (0·918, 1·081) | ·925 | 0·996 (0·917, 1·081) | ·919 |
| LMR | 0·918 (0·843, 1·001) | ·052 | 0·914 (0·839, 0·996) | ·040 | 0·916 (0·840, 0·998) | ·046 |


A total of 270,439 participants involved in this analysis. Exposures were log-transformed and standardized to Z scores such that the HR represents the predicted effect of per SD increment of log-transformed systemic inflammatory markers

HR Hazard ratio, CI Confidence interval, CRP C-reactive protein, NLR Neutrophil-to-lymphocyte ratio, PLR Platelet-to-lymphocyte ratio, SII Systemic immune-inflammation index, LMR Lymphocyte-to-monocyte ratio, SD Standard deviation

a Model 1 adjusted for age and sex

b Model 2 adjusted for age, sex, smoking status, hypertension, education, Townsend deprivation index, ethnicity and hypercholesterolemia

c Model 3 adjusted for age, sex, smoking status, hypertension, education, Townsend deprivation index, ethnicity, hypercholesterolemia, and polygenic risk score

Restricted cubic splines found a monotonic positive relationship between CRP and AAA incidence, and for lymphocyte and monocyte counts the risk began to rise when the value was above 75% percentile (Fig. 2 ) .


#### Fig. 2.


> **Figure/Table Caption:** Restricted cubic splines for the associations between systemic inflammatory markers and incident abdominal aortic aneurysm. Two dashed vertical lines indicate 25% and 75% values of each exposure, and the dashed horizontal line indicate HR = 1. Results were adjusted for age at baseline, sex, smoking status, hypertension, education, Townsend deprivation index, ethnicity, and hypercholesterolemia and polygenic risk score of abdominal aortic aneurysm. Exposures were log-transformed. HR, Hazard ratio; CI, Confidence interval; CRP, C-reactive protein


### Subgroup analysis

Per one SD increase in PRS was associated with a 32% higher risk of AAA [95% CI: 1·22, 1·43] (Supplemental Table S3). The cumulative incidence curves stratified by the tertile of PRS showed a similar result (Supplemental Figure S1). Subgroup analysis showed a significant positive association between CRP and risk of AAA in all PRS tertiles (HR per 1-SD increase in CRP ranges from 1·44 to 1·49) and no interaction between AAA and PRS (P for interaction = 0·85); Nor was there a significant interaction between other inflammatory biomarkers and PRS. Sex and smoking status significantly modified the associations of CRP and lymphocytes with AAA risk, with the strongest association seen in the current male smokers. Sex also interacts with LMR, while smoking interacts with neutrophil, platelet and SII. No interaction was found between CRP and age and between CRP and hypertension (Fig. 3 ).


#### Fig. 3.


> **Figure/Table Caption:** The associations between systemic inflammatory markers and incident AAA in subgroups of different genetic risk, age, sex, blood pressure and smoking status. Cox proportional hazards model was utilized, and adjusted for age, sex, smoking status, hypertension, education, Townsend deprivation index, ethnicity, hypercholesterolemia and polygenic risk score of abdominal aortic aneurysm (AAA). Exposures were log-transformed and standardized to Z score, and the HR represents the predicted effect of a one SD increment of log-transformed systemic inflammatory markers. Former and current smoking subgroups were combined when calculating P for interaction. HR, Hazard ratio; CI, Confidential interval; CRP, C-reactive protein; NLR, Neutrophil-to-lymphocyte ratio; PLR, Platelet-to-lymphocyte ratio; SII, Systemic immune-inflammation index; LMR, Lymphocyte-to-monocyte ratio; SD, Standard deviation


### CRP complements PRS and other risk factors in identifying individuals at higher AAA risk

There was a dose-dependent association between CRP + PRS and AAA risk. Compared to participants in the lowest CRP quartile and PRS tertile, those in the highest CRP quartile and PRS tertile had a 5·3-fold higher risk of AAA. Similar results were also observed in subgroup analyses by age, sex, hypertension, and smoking status (Fig. 4 ). Current smokers in the highest CRP quartile had a 16-fold higher risk of AAA than never smokers in the lowest CRP quartile; Males in the highest CRP quartile had a 20·9 fold higher risk of AAA than females in the lowest CRP quartile. Analysis using the lowest CRP quartile as the reference group within each sub-group yielded consistent results (Supplemental Table S4-S8).


#### Fig. 4.


> **Figure/Table Caption:** Associations between baseline levels of CRP and incident AAA by genetic predisposition, age, sex, blood pressure and smoking status. Hazard ratios and 95% confidence intervals were calculated using the Cox proportional hazards model adjusted for age, sex, smoking status, hypertension, education, Townsend deprivation index, ethnicity, and hypercholesterolemia. CRP was divided into quartiles (Quartile 1 to 4), and were log-transformed and standardized to Z scores such that the HR represents the predicted effect of per SD increment of log-transformed CRP. Cumulative incidence plot was drawn by applying the Fine-Gray competing risk model. AAA, abdominal aortic aneurysm; HR, Hazard ratio; CI, Confidential interval; CRP, C-reactive protein

To model the potential clinical utility of further risk stratification within a high-risk demographic, we performed a supplementary analysis according to previous study [ 29 ]. This analysis focused on men aged ≥ 65 years who were current smokers at baseline. Within this subgroup, the overall cumulative incidence of AAA over the follow-up period was 4.78%. When this group was further stratified, the incidence of AAA increased substantially. Among those who were also in the highest quartile of CRP, the incidence was 7.15%. Similarly, for those in the highest tertile of the PRS, the incidence was 6.32%. This corresponds to a 1.5-fold and 1.3-fold increase in the detection rate, respectively, compared to screening this high-risk demographic without considering these biomarkers. In the subgroup of the high-risk population with both high CRP and high PRS, the cumulative incidence rate was 10.05%, is 2.1 times that of the baseline high-risk group.


### Sensitivity analysis

The patterns of associations between different systemic inflammatory markers and the risk of incident AAA were consistent when missing values were imputed (Supplemental Table S9) or extreme observations were excluded (Supplemental Table S10). Besides, all systemic inflammatory markers were associated with incident AAA when analyzed using a multivariable Fine-Gray competing risk model to take into account competing death events (Supplemental Table S11).


## Discussion

In this large-scale, prospective, observational study of 271,068 participants from the UK biobank, we investigated the associations between baseline systemic inflammatory markers and risk of incident AAA. We found that higher levels of baseline serum CRP, peripheral lymphocyte counts, monocyte counts, and neutrophil counts were associated with a greater risk of subsequently identified AAA, while platelet counts, PLR and LMR were inversely associated with risk of incident AAA. Notably, sex and smoking status significantly modified the association between serum CRP and AAA incidence, with the strongest association seen in male current smokers. Participants with both high levels of major AAA risk factor and CRP had the highest risk of incident AAA. Moreover, CRP complements all major AAA risk factors in better identifying at-risk individuals.

Previous studies have suggested a potential link between peripheral blood inflammatory cell counts and AAA risk. During a median 3·8 years of follow-up, the CALIBER cohort study revealed a higher risk of incident AAA in participants with neutrophil counts between 6 and 7 10 9 /L compared to those with neutrophil counts between 2 and 3 × 10 9 /L (HR = 1·72) [ 30 ]. A screening study from Sweden also found that neutrophils and lymphocytes but not monocytes were associated with AAA development in men after adjustment for identified AAA risk factors or markers [ 31 ]. In the Atherosclerosis Risk in Communities (ARiC) study, higher neutrophil and monocyte counts were related to higher risk of AAA, independent of traditional risk factors such as smoking, obesity, and atherosclerosis [ 32 ].

While these studies contribute to our understanding of the relationship between inflammatory cells and AAA, they were limited by relatively small event numbers, short follow-up periods, potential selection bias, and lack of genetic data. Our study demonstrated a positive association between baseline counts of neutrophil, monocyte, lymphocyte and risk of incident AAA, independent of established AAA risk factors [ 33 ]. Subgroup analysis revealed the strongest association between CRP and AAA risk in-male current smokers, and the significant CRP-AAA association across all PRS tertile groups. Despite the strong association demonstrated in our study, the clinical implementation of CRP as a screening tool for AAA requires careful consideration. As a biochemical test, CRP is a highly sensitive but non-specific marker of inflammation. Its levels can be elevated by a multitude of conditions, including acute infection, trauma, and other chronic inflammatory states. The utility of CRP is not as a stand-alone diagnostic test, but as a risk-refining tool, as demonstrated in our analysis where CRP levels significantly stratified AAA risk within established high-risk groups. Our findings provide a rationale for future health-economic analyses to determine the cost-effectiveness of incorporating targeted CRP testing into existing AAA screening protocols.

CRP is a well-established biomarker of systematic inflammation and an independent risk factor for cardiovascular diseases [ 34 , 35 ]. However, the role of CRP in AAA pathogenesis remains uncertain. With a median follow-up of 22·5 years, the ARIC study found that higher CRP concentration was associated with increased risk of AAA, but the results should be interpreted with caution because of its small event number ( n = 66) [ 36 ]. Molacek and colleagues found a higher serum CRP level in AAA patients compared to healthy controls, but the discriminatory ability of CRP for AAA incidence was unsatisfactory (AUC = 0·601) [ 37 ]. Our study, leveraging a population-based prospective cohort of over 500,000 individuals followed for 13·9 years, found a significant positive association between baseline CRP and risk of incident AAA ( n = 629), even after adjusting for known AAA risk factors including genetic risk [ 33 ]. For each 1-SD increase in CRP, the risk of incident AAA increased by 46%. Our results lend to a support to CRP as a critical biomarker for AAA. Several single-center, small-size cohort studies have suggested association between CRP levels and AAA growth [ 38 , 39 ], rupture [ 40 , 41 ], and postoperative adverse events [ 41 , 42 ], which warranted further investigation.

The latest US [ 43 ] and European [ 44 ] guidelines recommend screening for AAA in all men aged ≥ 65 years old, particularly former or current smokers. Our study found that CRP substantially refined the risk of the population group who are recommended for screening. For example, in both male and older individuals, those with the highest CRP levels had a 3-fold higher risk of AAA compared to those with the lowest CRP levels. In current smokers, the risk was even higher, with individuals in the highest CRP quartile having a nearly 10-fold increased risk of AAA. These results have significant clinical implications on AAA risk refinement and provide valuable insights into the development of a more cost-effective screening program without missing out many positive cases. Our study also highlights the value of CRP as a biomarker for AAA risk, regardless of genetic predisposition as measured by the AAA PRS.

Our study has several methodological strengths. Owing to the rarity of AAA incidence in individuals aged under 60 years old [ 45 ], identifying potential risk factors requires a large cohort and a long follow-up period. The UK Biobank’s large sample size, extended follow-up, and detailed information on potential confounders were sufficient for identifying AAA risk factors. Moreover, the results drawn from the large-scale, prospective cohort studies avoided biases to some extent such as referral, selection, and recall bias. Nevertheless, there are also several limitations. Firstly, our analyses were restricted to blood cell counts and derived ratios, without further evaluation of inflammatory cytokines and subsets of immune cells. Secondly, participants from the UK Biobank were relatively young and healthy at recruitment and we have deliberately excluded participants with history of aortic aneurysm and those had conditions at baseline that could impact the levels of systemic inflammatory markers and the AAA incidence. This might have resulted in a very low incidence of AAA during the follow-up of our study. Thirdly, the UKB cohort primarily consists of individuals of European ancestry and white ethnicity, whether our findings can be generalized to other ethnic populations is unknown. The results should be verified in future studies involving diverse ethnic populations. Fourthly, the relatively short lifespan of blood cells means that cell counts only represent a snapshot of the inflammatory state at the time of blood draw, besides, although we have excluded known acute or chronic conditions that may lead to fluctuations in CRP levels, a one-time blood sample may be arbitrarily elevated due to other circumstance. We used immune cell counts reflecting the state of systemic inflammation over a period before disease onset with above limitations. While our study has excluded many conditions, it is also important to consider other potential confounders, such as congenital insufficiency of the aortic valve, which may be associated with AAA pathogenesis. Furthermore, specific medications, such as metformin, will also influence AAA development protectively or detrimentally.

In conclusion, our study found that higher baseline levels of serum CRP, and peripheral blood counts (lymphocytes, monocytes, and neutrophils) were associated with an increased risk of subsequently identified AAA, while platelet counts were inversely associated with AAA incidence risk. High CRP levels complement other AAA risk factors in better identifying individuals at risk.


## Supplementary Information


## Acknowledgements

We gratefully acknowledge the commitment and dedication of the participants of the UK Biobank. This study conforms to the principles outlined in the Declaration of Helsinki. All participants in UK Biobank provided their written consent. The application number of the resource under UK Biobank for this study is 88192. The original data in UK Biobank is openly accessible to its approved applicants ( https://www.ukbiobank.ac.uk/ ).


## Authors’ contributions

Concept and design: Wu, Qiu, Xu, Lu and Pu.Acquisition, analysis, or interpretation of data: Xu, Qiu, Lu, Qin, Ye, Wang, Zhou.Drafting of the manuscript: Pu, Zhou, Wu.Critical review of the manuscript for important intellectual content: All authors.Statistical analysis: Pu, Wu, Guo, Lei, Wei, Hu.Obtained funding: Lu, Qiu, Ye, Wang.Administrative, technical, or material support: Qiu, Qin, Ye, Wang.Supervision: Wu, Xu, Qiu, Lu, Zhou.


## Funding

This work was supported by these funding as follows: the National Natural Science Foundation of China (82300540; 82170509; 82370494; 82170411); the Fundamental Research Funds for the Central Universities (KLSB2023KF-04); Clinical Research Program of 9th People’s Hospital (JYLJ202010; JYLJ202204); Science and Technology Innovation Plan of Shanghai Science and Technology Commission (20Y11909600; 21S31904300; 21Y11909500); Shanghai Municipal Health Bureau (20224Y0170; 202240145); Original Exploration Project of Shanghai Ninth People’s Hospital (No.JYYC004); Shanghai Sailing Program (24YF2723600); China Postdoctoral Science Foundation (2025M772309); and Anhui Provincial Health Research Project (AHWJ2022a031). The funder had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.


## Data availability

The original data in UK Biobank is openly accessible to its approved applicants (https://www.ukbiobank.ac.uk/).


## Declarations


### Ethics approval and consent to participate

The application number of the resource under UK Biobank for this study is 88192. All participants in UK Biobank provided their written consent. This study conforms to the principles outlined in the Declaration of Helsinki. The study protocols were approved by the Medical Ethics Committee of Shanghai Ninth People’s Hospital Affiliated to Shanghai Jiao Tong University School of Medicine.


### Consent for publication


### Competing interests

The authors declare no competing interests.


## Footnotes

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.



## Contributor Information

Zhijue Xu, Email: [EMAIL_REDACTED].

Zhaoyu Wu, Email: [EMAIL_REDACTED].

Xinwu Lu, Email: [EMAIL_REDACTED].

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials


### Data Availability Statement

The original data in UK Biobank is openly accessible to its approved applicants (https://www.ukbiobank.ac.uk/).
