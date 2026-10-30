# De-Identified Manuscript `OOD_ANON_33`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract


### Objective

This study seeks to analyze the coordinated patterns of spontaneous neural activity and instantaneous electrical activity in the brain using dual-dimensional indicators of brain functional connectivity and microstates, aiming to identify potential biomarkers for early screening and precise classification.


### Methods

A case-control study design was utilized, with 195 older adults suffering from cognitive impairment (with a roughly equal distribution of mild and moderate cases) serving as the case group, and 65 healthy older adults matched as the control group. Participants were required to complete a demographic questionnaire, the Montreal Cognitive Assessment Scale, the short form of the International Physical Activity Questionnaire, and the Pittsburgh Sleep Quality Index, after which 5 min of eyes-closed resting EEG signals were recorded.


### Results

Significant differences were observed in the average strength and density of brain functional connectivity within the δ and θ frequency bands among older adults with different cognitive levels, indicating that higher average strength and density corresponded to more severe cognitive impairment ( P < 0.05). Older adults with varying cognitive levels showed significant differences in both static features (Duration, Coverage, Occurrence) and dynamic features (transition probabilities) of microstates A, B, C, and D ( P < 0.05). In terms of static features, stronger temporal characteristics of microstates B and D were associated with greater severity of cognitive impairment, while microstate A demonstrated the most pronounced temporal characteristics during the mild cognitive impairment stage ( P < 0.05). In dynamic features, healthy older adults primarily exhibited bidirectional balanced transitions between A/C↔C/A and B/D↔D/B, while those with mild cognitive impairment displayed transitional characteristics in the paths A→B/D and C→D. In contrast, older adults with moderate to severe cognitive impairment showed significantly enhanced directed transitions from microstates B/D to A/C ( P < 0.05).


### Conclusion

Older adults with mild cognitive impairment demonstrated increased abnormal and redundant brain functional connectivity, inefficiency in microstate C, and compensatory mechanisms in low-frequency connectivity in brain functions as well as microstates A, B, and D. Older adults with moderate to severe cognitive impairment displayed sustained compensatory mechanisms in brain functional connectivity and microstates, characterized by dominant abnormal and redundant connections, along with pathological hypersynchrony in microstates B and D, which persisted until rigidity set in.


### Supplementary Information

The online version contains supplementary material available at [REDACTED_DOI].

Keywords: Cognitive impairment, Older adults, EEG, Brain functional connectivity, Microstates, Biomarkers


## Introduction

With the acceleration of global population aging, cognitive impairment has emerged as a major challenge to public health [ 1 ]. According to the World Health Organization, around 55 million people globally are affected by dementia, with 60%−70% of these cases attributed to Alzheimer’s disease. It is projected that the number of affected individuals will rise to 139 million by 2050 [ 2 ]. The primary symptoms of cognitive impairment encompass progressive memory loss, executive function deficits, language decline, visuospatial orientation challenges, and a gradual reliance on assistance for daily activities [ 3 ]. Cognitive impairment follows a progressive trajectory: Mild Cognitive Impairment (MCI) is considered an early stage, with about 10%−15% of patients progressing to dementia, which highlights a crucial window for early detection and intervention [ 4 ]. Older adults with moderate cognitive impairment show a marked reduction in their ability to live independently, necessitating assistance with daily tasks [ 5 ]. Severe cognitive impairment, exemplified by dementia, manifests as a total loss of memory, language skills, and executive functions [ 6 ]. Consequently, the accurate classification of cognitive impairment has emerged as an urgent problem that requires immediate attention.

At present, the screening of cognitive impairment mainly utilizes neuropsychological scales (such as the Montreal Cognitive Assessment [ 7 ]), structural magnetic resonance imaging (to detect hippocampal atrophy [ 8 ]), and cerebrospinal fluid analysis (including Aβ42, t-tau, and p-tau [ 9 ]). Classification predominantly relies on amyloid and tau PET imaging [ 10 ]. Compared to the invasiveness of cerebrospinal fluid sampling (lumbar puncture) and the delayed response of structural magnetic resonance imaging (where hippocampal volume changes lag behind pathology by approximately 5–10 years) [ 11 ], electroencephalography (EEG) presents several advantages, including non-invasiveness, low cost, portable equipment (ideal for community screening), and high temporal resolution [ 12 ]. EEG demonstrates a high sensitivity to subtle variations in brain function, a fact supported by many studies [ 12 – 14 ]. Additionally, past studies have often concentrated on single frequency band power, lacking in multidimensional feature analysis. The examination of brain functional connectivity and microstates offers a novel perspective for observing subtle changes in brain functionality. EEG offers crucial technical support for the screening and classification of cognitive impairment.

Resting-state EEG functional connectivity involves analyzing electroencephalogram (EEG) signals from subjects in a resting state (without specific tasks) to evaluate the synchrony or coordination of neural activity across different brain regions, thereby uncovering the functional integration patterns of brain networks [ 15 ]. The essence of this approach is to quantify the efficiency of information transfer between brain regions. Commonly utilized metrics include phase lock value (PLV), coherence, phase lag index (PLI), and weighted phase lag index (WPLI), which reflect the functional coupling characteristics of neural networks across various frequency bands (such as δ, θ, α, β, and γ waves) [ 16 ]. Recent research by Chowtapalle utilizing pairwise phase consistency (PPC) revealed differences in brain functional connectivity across specific frequency bands between patients with Alzheimer’s disease and those with mild cognitive impairment (MCI), indicating decreased connectivity in the θ band among Alzheimer’s disease (AD) patients and increased connectivity in the γ band among MCI patients. Nevertheless, it is crucial to recognize that pairwise phase consistency (PPC) primarily focuses on phase information, neglecting variations in amplitude. Furthermore, PPC’s assessment of connectivity may lack accuracy for non-periodic signals, potentially leading to an incomplete evaluation of functional connectivity in some scenarios [ 17 ]. In response to this, we utilized four brain functional connectivity indicators: PLV (which is highly sensitive to short-term phase activity but vulnerable to volume conduction effects [ 18 ]), coherence (which integrates both phase and amplitude information but is also influenced by volume conduction [ 19 ]), PLI (which circumvents volume conduction issues but shows reduced sensitivity to weak connectivity [ 20 ]), and WPLI (which addresses volume conduction problems while being more sensitive to weak connectivity, albeit with higher data quality requirements [ 21 ]). We employed these indicators to investigate the strength, density, and potential influencing factors of brain functional connectivity among older adults with different cognitive levels.

Resting-state microstates refer to stable global field potential spatial patterns that exist briefly within electroencephalogram (EEG) signals. They reflect the spontaneous and transient functional coordination of brain neural networks during resting states [ 22 ]. The common metrics used to evaluate microstates include their types (typically labeled as A, B, C, and D), along with duration, coverage, occurrence, and transition probability [ 23 ]. Microstate A reflects the language network (Broca/Wernicke areas) and semantic processing, while microstate B is associated with the dorsal attention network (DAN) and visuospatial processing. Microstate C is closely linked to the default mode network (DMN), and microstate D represents the frontoparietal control network [ 24 ]. Nonetheless, significant controversy exists regarding the microstate characteristics of older adults with varying cognitive levels. According to Yibing’s research, patients with Alzheimer’s disease demonstrated longer durations of microstates C and D, alongside a decrease in coverage for microstate B [ 25 ]. Conversely, Martin’s study revealed that individuals with mild cognitive impairment (MCI) with Lewy bodies displayed higher coverage across microstates A, B, C, and D, especially noting shorter average durations and higher coverage in microstate B [ 26 ]. In this context, we aim to assess the temporal characteristics of microstates among older adults with varying cognitive levels and investigate the potential influencing factors.

A review of prior studies reveals that EEG is highly sensitive to subtle changes in brain function [ 12 – 14 ]. However, the brain functional connectivity characteristics of older adults with different cognitive levels have not been fully explored. Further, there remains ongoing debate regarding microstate features, and whether external manifestations (e.g., cognitive decline) are influenced by shared factors with internal changes (such as brain functional connectivity and microstates) remains uncertain [ 27 – 29 ]. In response, we adopted a case-control study design, incorporating dual-dimensional indicators—brain functional connectivity and microstates—to dissect the cooperative patterns of spontaneous neural activity and transient electrical activity in the brain. Our study seeks to identify biomarkers for early detection and precise classification, while examining influencing factors across three dimensions: demographic characteristics, modifiable behaviors and lifestyles, and physical and mental health conditions. The ultimate aim is to deliver cost-effective, widely acceptable, and community-screening-friendly diagnostic tools that are both accurate and clinically effective.


## Methods


### Participants

Sample size estimation was conducted using G-power 3.1.9.7 software, applying F tests and ANOVA: Fixed effects, omnibus, one-way. A medium effect size of 0.5 was chosen [ 30 ], with an alpha level of 0.05 and a statistical power of 0.8, yielding a total sample size of 159 participants, with at least 53 participants in each group.

This research will take place from December 2023 to April 2025 in multiple centers, including the Health Service Center in Guangfulin Street, Changfujiayuan Community, Qiangwei Jiuli Community, and Luqian Community in Jinshan District, Shanghai. A total of 195 older adults with cognitive impairment will be included, featuring an approximate 1:1 ratio between those with mild cognitive impairment and those with moderate to severe cognitive impairment, as determined through health assessments. The control group will include 65 cognitively healthy older adults, randomly selected from those undergoing health check-ups at the same hospital or community. This selection will follow a 1:3 ratio (cognitively healthy to cognitively impaired) based on differences in cognitive function. This study adheres to the Helsinki Declaration and has been approved by the Ethics Committee of Shanghai University of Sport (Ethics Number: No. 102772020RT060). All participants voluntarily participated in the experiment and signed the informed consent form. (The exclusion criteria and the information on participant grouping can be found in Appendix 1 of the supplementary materials.)


### Test protocol

All testing was scheduled to take place daily between 13:30 and 16:30, requiring each participant to visit the laboratory twice, with each session lasting about one hour. In the first laboratory visit, participants received an explanation of the testing procedures, completed basic information forms, and underwent cognitive assessments. The second visit occurred the next day, when participants filled out questionnaires and had their EEG signals recorded.Participants were instructed to refrain from vigorous exercise for 24 h before testing and to avoid consuming caffeinated or alcoholic beverages. (See Fig. 1 )


#### Fig. 1.


> **Figure/Table Caption:** Technical roadmap


### Quality assurance

In this study, both the testers, participants, and outcome assessors were blinded to the participants’ group assignments, thereby implementing a triple-blind design. The testing process involved one principal investigator and two assistant researchers responsible for data collection, operation, and monitoring, with all testing personnel unaware of the individual circumstances of the participants. Participants were also kept unaware of their group assignments and other related information. Throughout the study, participants were informed of the testing procedures and EEG collection precautions. Ultimately, all data analysis was performed by a researcher who had no involvement in either the intervention or data collection.


### Questionnaire assessment

Basic Information Questionnaire

The basic information collected from participants includes demographic data (age, gender, occupation, residence, marital status, education level), lifestyle factors (smoking habits, alcohol consumption, dietary habits), and health status (fall history, vision status, hearing status, and body mass index).

Montreal Cognitive Assessment (MoCA)

MoCA is an internationally recognized cognitive screening tool that facilitates the quick assessment of cognitive impairment and early signs of cognitive decline, making it widely applicable for evaluating cognitive function in older adults. Created by neurologist Ziad Nasreddine in 1996 [ 31 ], MoCA evaluates multiple cognitive domains, such as visual-spatial/executive function, naming, memory, attention, language fluency, abstract reasoning, delayed recall, and orientation. To account for the effect of educational background, additional points are awarded based on years of education: 2 points for ≤ 6 years, 1 point for 6–12 years, and no points for more than 12 years. The maximum score for MoCA is 30, with scores of 26–30 indicating cognitive health, 20–25 indicating mild cognitive impairment, and scores of 19 or lower indicating severe cognitive impairment; higher scores correlate with better cognitive function [ 7 ]. In this study, the Chinese version of MoCA was employed, demonstrating a Cronbach’s α of 0.810 and a test-retest reliability of 0.898, indicating its high sensitivity and specificity [ 32 ].

International Physical Activity Questionnaire-Short (IPAQ-S)

The International Physical Activity Questionnaire - Short Form (IPAQ-S) is a widely utilized instrument to evaluate physical activity levels, demonstrating strong reliability and validity with a Cronbach’s α of 0.90 [ 33 ]. This study employed the IPAQ-S, comprising 7 questions that address walking, moderate-intensity physical activity, and vigorous-intensity physical activity. Total energy expenditure was determined using the metabolic equivalent of task (MET) values assigned to each category of physical activity: walking (3.3 METs), moderate-intensity activity (4.0 METs), and vigorous-intensity activity (8.0 METs). The formula for calculation is as follows:

Pittsburgh Sleep Quality Index (PSQI)

The Pittsburgh Sleep Quality Index (PSQI) is a globally utilized tool for assessing sleep quality. Developed by the University of Pittsburgh, it measures an individual’s sleep quality and related problems within the past month. The PSQI includes 19 self-rated items and 5 observer-rated items, of which 18 self-rated items contribute to the scoring. These items cover seven dimensions: sleep quality, sleep latency, sleep duration, sleep efficiency, sleep disturbances, use of sleep medication, and daytime dysfunction. The PSQI has a maximum score of 21, where 0 to 6 points indicate normal sleep quality, and ≥ 7 points suggest sleep disturbances. Higher scores correspond to worse sleep quality. The PSQI demonstrates solid psychometric properties, with a Cronbach’s α of 0.790, indicating good reliability, validity, as well as high sensitivity and specificity [ 34 ].


### EEG signal acquisition and preprocessing

EEG data were collected with a 24-channel electroencephalogram (EEG) device (NCERP-190012) from Shanghai Nuochen Electric Co., Ltd. The selected electrodes included Fp1 (left frontal pole), Fp2 (right frontal pole), F3 (left frontal mid), F4 (right frontal mid), C3 (left central), C4 (right central), P3 (left parietal), P4 (right parietal), O1 (left occipital), O2 (right occipital), F7 (left lateral frontal), F8 (right lateral frontal), T3 (left temporal mid), T4 (right temporal mid), T5 (left temporal posterior), and T6 (right temporal posterior) as regions of interest (ROIs), referencing previous research [ 35 – 37 ]. The ground electrode was placed at the midline frontal (GND), and the reference electrodes were positioned on both mastoids (A1 and A2). The device is equipped with a preamplifier, set to a sampling rate of 500 Hz, while the impedance between the electrodes and the skin is kept below 5 kΩ. The testing environment was a soundproof, well-ventilated indoor setting with suitable lighting, ensuring there was no electromagnetic interference. Participants were seated, and the testing staff instructed them to close their eyes, remain relaxed, quiet, and alert, while avoiding swallowing or teeth grinding. Considering the objectives and subjects of this study, and informed by previous research [ 35 – 37 ], EEG signals were recorded for a duration of 5 min. EEG signals were then recorded for 5 min once a stable state was achieved.

Data preprocessing was performed using the EEGLAB toolbox in MATLAB 2023a. EEGLAB is an open-source toolbox that operates within MATLAB and includes various MATLAB functions. The specific preprocessing steps are as follows: (1) Import continuous EEG data; (2) Localize electrodes; (3) Remove unnecessary electrodes; (4) Downsample the data to 256 Hz; (5) Apply a high-pass filter at 0.1 Hz and a low-pass filter at 30 Hz; (6) Average reference the electrodes; (7) Check the waveform for bad electrodes and interpolate them if necessary; (8) Segment the continuous EEG data into 2-second epochs; (9) Use Independent Component Analysis (ICA) to correct for eye movements, blinking, electromyography, electrocardiography, or any non-physiological artifacts; (10) Identify the characteristics of principal components and remove interfering components; (11) Reject electrodes with amplitude values exceeding ± 100 µV; (12) Manually remove significant drift segments; (13) Save the processed continuous EEG data. (The operational definition of this study in terms of electroencephalogram is presented in Appendix 2 of the supplementary materials.)


### Brain functional connectivity analysis

This study utilized MATLAB scripts for brain functional connectivity analysis and conducted graph theory analysis using the BrainNet Viewer package [ 38 ]. To enhance the comprehensiveness of the brain functional connectivity analysis, we utilized four metrics: Phase Locking Value (PLV), Phase Lag Index (PLI), Weighted Phase Lag Index (WPLI), and Coherence. These metrics were used to construct brain functional connectivity and assess the cognitive levels of different groups of older adults through two dimensions: connectivity strength and density. To address the limitations of relying solely on a single metric and to enhance robustness and sensitivity, a positive result was defined as the simultaneous significant differences observed in all four metrics—PLV, PLI, WPLI, and COH. (The methodological details regarding brain functional connectivity can be found in Appendix 3 of the supplementary materials.)


### Microstate analysis



|  | 1 |
| --- | --- |


This study performed microstate analysis using the MS 1.0 toolbox in MATLAB. The specific steps are outlined below: (1) Compute the Global Field Power ( GFP ) across all electrode channels, resulting in the GFP curve. It is commonly accepted that the data at the GFP peak demonstrates a higher signal-to-noise ratio. The calculation formula for GFP is presented in (5), where K denotes the number of electrodes, Vi(t) indicates the measured voltage of a specific electrode at time t, and Vmean(t) represents the average instantaneous potential of all electrodes at that time point; (2) Clustering. The EEG topographies at the GFP peaks were categorized using the Atomize and Agglomerate Hierarchical Clustering (AAHC) algorithm, ultimately resulting in the EEG microstate topography, known as the topography template; (3) Back-fitting. Each topography at each time point was categorized according to the most similar topography template, yielding a microstate temporal sequence; (4) Microstate Temporal Features and Global Explained Variance. (The methodological details regarding the micro-state approach can be found in Appendix 3 of the supplementary materials.)


### Statistical analysis

This study employed SPSS 29.0 for data computation and statistical analysis, MATLAB 2023b to calculate brain functional connectivity metrics and microstate parameters, and Origin 2024, R Studio, and BrainNet Viewer for effective data visualization. The Shapiro-Wilk test was used to assess data normality. For measurements that adhered to a normal distribution, data were expressed as mean ± standard deviation (M ± SD). For non-normally distributed data, non-parametric tests were applied. For categorical variables, differences among the three groups of older adults were analyzed using the Chi-square test. For continuous variables, including demographic data, influencing factors, brain functional connectivity, and microstate parameters, one-way ANOVA and ANCOVA were utilized to assess group differences. Multivariate logistic regression and partial correlation analysis were conducted to identify factors influencing cognitive function in older adults. Pearson’s correlation test was applied to investigate the determinants of brain functional connectivity and microstates. The significance threshold was set at α = 0.05, with P < 0.05, P < 0.01, and P < 0.001 denoting statistical significance. All statistical analyses adhered to two-tailed testing.

To mitigate the issue of multiple comparisons, Bonferroni correction was employed to control the family-wise error rate. For brain functional connectivity analysis involving six frequency bands, the corrected significance threshold was α = 0.05/6 ≈ 0.0083. For microstate analysis, which encompasses four microstate types and eight feature parameters (resulting in 32 comparisons), the corrected threshold was α = 0.05/32 ≈ 0.0016. Considering the sample size and degrees of freedom in this study, the critical F-value for brain functional connectivity was determined to be 4.900 (numerator df = 2, denominator df = 257), while for microstate parameters, it was 6.599 (numerator df = 2, denominator df = 257). Values exceeding the respective critical F-values were regarded as significant post-correction.


## Results


### Basic information of participants and their influencing factors

This study included 260 older adults, consisting of 95 individuals with moderate to severe cognitive impairment, 100 with mild cognitive impairment, and 65 who were cognitively healthy. The three groups of older adults did not exhibit significant differences in terms of gender, residence, marital status, smoking habits, drinking habits, dietary conditions, falls in the past year, hearing decline, vision decline, and BMI ( P > 0.05). However, there were significant differences in age, occupation, education level, Pittsburgh Sleep Quality Index, and physical activity levels ( P < 0.05). (Detailed demographic information can be found in Fig. 2 A and Appendix 4 of the supplementary materials.)


#### Fig. 2.


> **Figure/Table Caption:** Differences in Brain Functional Connectivity and Microstates Among Older Adults with Different Cognitive Levels and Their Potential Influencing Factors. A Differences in cognitive function, age, education level, Pittsburgh Sleep Quality Index, and physical activity among older adults with differing cognitive levels; B Differences in phase locking value (PLV), coherence, phase lag index (PLI), and weighted phase lag index (WPLI) in the δ frequency band among older adults with varying cognitive levels (the matrix in the upper right corner illustrates the brain functional connectivity strength between selected regions of interest (ROIs), while the lower left corner depicts the connectivity density of these ROIs); C Differences in the four brain functional connectivity metrics in the θ frequency band among older adults with varying cognitive levels; D Correlation matrix and network connectivity diagram (the upper right corner presents the correlation matrix among eight brain functional connectivity metrics, while the lower left corner illustrates the network connectivity diagram conducting Pearson correlations between age, education level, PSQI, physical activity, and the eight brain functional connectivity metrics); E Topological maps of microstates A, B, C, and D for older adults with differing cognitive levels; F Diagrams illustrating differences in duration, coverage, and occurrence for microstates A, B, C, and D among older adults with varying cognitive levels; G Pairwise difference diagrams depicting microstate transition probabilities among older adults with varying cognitive levels (for instance, in comparison to the mild cognitive impairment group, the moderate to severe cognitive impairment group exhibited a greater likelihood of transitioning between microstates BA, BC, BD, DA, DB, and DC, while showing a lesser tendency for transitions between microstates AB, AC, AD, CA, CB, and CD); H Correlation matrix and network connectivity diagram (the upper right corner presents the correlation matrix among 24 microstate parameters, while the lower left corner depicts the network connectivity diagram conducting Pearson correlations between age, education level, PSQI, physical activity, and the 24 microstate parameters)

To further explore the factors influencing cognitive function in older adults with varying cognitive levels, we constructed a multivariate logistic regression model with three groups of older adults as the dependent variables, and age, occupation, education level, Pittsburgh Sleep Quality Index, and physical activity as the independent variables. The model’s −2 log likelihood value was 438.212 ( p < 0.001), and the chi-square value for goodness-of-fit was 456.228 ( p = 0.756), indicating that the model is effective and exhibits good fit. In order to explore the specific relationships between cognitive function and age, Pittsburgh Sleep Quality Index (PSQI), education level, and physical activity level, we performed a partial correlation analysis. The findings showed that the partial correlation coefficients between MoCA and age, PSQI, education level, and IPAQ were − 0.213 ( P < 0.001), 0.271 ( P < 0.001), −0.156 ( P = 0.012), and 0.388 ( P < 0.001), respectively. The results suggest that age and the Pittsburgh Sleep Quality Index are risk factors for cognitive function in the older adults, while education level and physical activity are protective factors. The outcomes of the multivariate logistic regression and partial correlation analysis indicate that age and PSQI are risk factors for cognitive function in older adults, whereas education level and physical activity are identified as protective factors. (For detailed results of the multivariate logistic regression, please refer to Appendix 5 in the supplementary materials.)


### Brain functional connectivity characteristics in older adults with varying cognitive levels


#### Differences in brain functional connectivity strength across various frequency bands

To explore the variations in brain functional connectivity strength across different frequency bands among older adults with differing cognitive levels, we calculated the average brain functional connectivity strength (PLV, COH, PLI, WPLI) for six frequency bands: δ, θ, α1, α2, β1, and β2 across the three groups. Subsequently, we performed ANCOVA (with age, education, PSQI, and IPAQ as covariates) to assess the intergroup differences. The ANCOVA results revealed significant differences in average brain functional connectivity strength (PLV, COH, PLI, WPLI) among the three groups in the δ and θ frequency bands (F-values: 6.929, 6.274, 6.262, 5.752, 6.926, 5.384, 7.343, and 7.807, with P-values: 0.001, 0.002, 0.002, 0.004, 0.001, 0.005, < 0.001, and < 0.001, and Partial Eta-Squared values: 0.052, 0.047, 0.047, 0.043, 0.052, 0.041, 0.055, and 0.058). In contrast, there were no significant differences in average brain functional connectivity strength (PLV, COH, PLI, WPLI) in the α1, α2, β1, and β2 frequency bands (F-values were all less than 4.900, and P-values were all above the corrected threshold of 0.0083). It is noteworthy that the results for the α1 and α2 frequency bands did not fulfill the correction criteria, despite P-values being below 0.05 before correction. We discovered significant differences in average brain functional connectivity strength among older adults with varying cognitive levels in the δ and θ frequency bands, indicating that higher connectivity strength is associated with more severe cognitive impairment. This indicates that older adults with cognitive impairment may have abnormal connectivity in lower frequency bands, leading to an unusually high average brain functional connectivity strength. (For detailed information on the differences in brain functional connectivity strength, please refer to Fig. 2 B and C, and Appendix 6 in the supplementary materials.)


#### Differences in brain functional connectivity density across the δ and θ frequency bands

To explore the differences in brain functional connectivity density among older adults with varying cognitive levels across different frequency bands, we performed a graph-theoretic analysis of brain functional connectivity density in the δ and θ frequency bands, where significant differences in average connectivity strength were identified. We selected the average brain functional connectivity strength of all older adults in the δ and θ frequency bands as a reference to compare the connectivity density of the three groups at the same level of brain functional connectivity strength. Analysis of brain connectivity graphs and correlation matrix heatmaps revealed that a deeper level of cognitive impairment correlated with increased brain functional connectivity density. This indicates that older adults with cognitive impairment may have redundant connections in lower frequency bands, resulting in an elevated brain functional connectivity density. (For detailed information on the differences in brain functional connectivity density, please refer to Fig. 2 B and C.)


#### Correlation between brain functional connectivity and influential factors on cognitive function in older adults

To explore whether factors impacting cognitive function—such as age, education level, Pittsburgh Sleep Quality Index (PSQI), and physical activity (as external manifestations)—are also associated with brain functional connectivity (as internal changes) in older adults with cognitive impairment, we performed a correlation analysis between these factors and the brain functional connectivity metrics that exhibited significant differences. Figure 2 D illustrates that there were significant correlations between age, education level, physical activity, and brain functional connectivity metrics (with all P-values being less than 0.05). In contrast, no significant correlations were observed between PSQI and the brain functional connectivity metrics (with all P-values exceeding 0.05). This indicates that age, education level, and physical activity might be significant factors influencing the observed differences in brain functional connectivity in the θ and δ frequency bands among older adults. (For detailed correlation coefficients and significance levels, please refer to Figs. 2 D and 3 , and Appendix 7 in the supplementary materials.)


> **Figure/Table Caption:** Mechanism diagram


### Microstate characteristics in older adults with varying cognitive levels


#### Clustering results

We performed electroencephalographic (EEG) microstate analyses on the resting-state EEG data of older adults with varying cognitive levels, obtaining four distinct microstate topographies, as illustrated in Fig. 2 E.


#### Differences in static microstate features

To explore the differences in static microstate features among older adults with differing cognitive levels, we calculated the duration, coverage, and occurrence of microstates A, B, C, and D for the three groups. Subsequently, we conducted ANCOVA (with age, education, PSQI, and IPAQ as covariates) to assess the group differences. The ANCOVA results revealed significant differences in duration, coverage, and occurrence of microstates A, B, C, and D among older adults with differing cognitive levels (F-values were 695.786, 951.307, 733.074, 1091.157, 782.276, 948.391, 825.959, 1072.705, 23.534, 45.979, 22.620, and 12.908, all with P-values < 0.001). We found that stronger temporal characteristics of microstates B and D correlated with more severe cognitive impairment, whereas microstate A displayed the strongest temporal characteristics at the mild cognitive impairment stage. The preservation of microstate C may be linked to the maintenance of normal cognitive function. This implies that the duration, coverage, and occurrence of microstates A, B, C, and D may act as potential biomarkers for differentiating levels of cognitive impairment, offering opportunities for the prevention, assessment, early intervention, and personalized treatment approaches for cognitive disorders. (For differences in static microstate features, please refer to Fig. 2 F and Appendix 8 in the supplementary materials.)


#### Differences in dynamic microstate features

To explore the differences in dynamic microstate features (transition probabilities) among older adults with differing cognitive levels, we calculated the transition probabilities for microstates A, B, C, and D in the three groups and conducted ANCOVA (using age, education, PSQI, and IPAQ as covariates) to examine the differences among the groups. The ANCOVA results revealed significant differences in transition probabilities among the three groups (F-values were 328.560, 156.142, 174.053, 241.182, 223.090, 110.339, 287.265, 269.557, 258.980, 147.746, 994.741, and 204.629, all with P < 0.001). We found that the moderate to severe cognitive impairment group exhibited significantly enhanced directional transitions from microstates B/D to A/C, whereas the mild cognitive impairment group displayed transitional characteristics in the A→B/D and C→D pathways. The healthy group predominantly demonstrated bidirectional balanced transitions between A/C↔C/A and B/D↔D/B. These findings offer potential objective electrophysiological indicators for the classification, screening, efficacy monitoring, and progression prediction of cognitive impairments. (For differences in dynamic microstate features, please refer to Fig. 2 G and Appendix 8 in the supplementary materials.)


#### Correlation between microstates in older adults and influencing factors of cognitive function

To investigate whether age, education level, Pittsburgh Sleep Quality Index, and physical activity (external factors) that influence cognitive function are also associated with microstates in older adults with cognitive impairment (internal changes), we performed correlation analyses between these factors and the microstate parameters that exhibited significant differences. As illustrated in Fig. 2 G, age, education level, and physical activity were significantly correlated with the microstate parameters (all P-values < 0.05), whereas the Pittsburgh Sleep Quality Index showed no correlation with the microstate parameters (all P-values > 0.05). This indicates that age, education level, Pittsburgh Sleep Quality Index, and physical activity may be influencing factors contributing to the differences in microstate parameters among older adults. (For specific correlation coefficients and significance, please refer to Figs. 2 H and 3 , and Appendix 9 in the supplementary materials.)


## Discussion

The findings of this study reveal significant differences in cognitive function, age, education level, Pittsburgh Sleep Quality Index, and physical activity among older adults with varying cognitive levels. Specifically, age and Pittsburgh Sleep Quality Index are identified as risk factors for cognitive function, whereas education level and physical activity are protective factors, aligning with previous research [ 39 – 42 ]. As older adults age, experience higher Pittsburgh Sleep Quality Index scores, lower education levels, and decreased physical activity, the severity of cognitive impairment tends to increase. It is crucial to recognize that cognitive decline is an external behavioral manifestation of individuals, while brain functional connectivity and microstates represent coordinated patterns of spontaneous neural activity and instantaneous electrical activity [ 43 , 44 ]. The interactions among external manifestations (cognitive decline), internal changes (brain functional connectivity and microstates), and influencing factors (age, education level, Pittsburgh Sleep Quality Index, and physical activity) need to be explored further.

This study revealed significant differences in the average intensity and density of brain functional connectivity in the δ and θ frequency bands among older adults with varying cognitive levels. Notably, higher connectivity intensity and density were associated with greater severity of cognitive impairment. Age, education level, and physical activity may play a role in influencing the differences in brain functional connectivity intensity and density observed among older adults. This suggests that older adults with cognitive impairment may exhibit abnormal or inefficient connectivity in the lower frequency bands, leading to abnormally high brain functional connectivity intensity and density. This abnormal phenomenon is likely the result of a combination of neural network inefficiency, compensatory mechanisms [ 45 , 46 ], and pathological synchronization [ 47 ]. In older adults with mild cognitive impairment, certain functional connections in the brain start to become inefficient. To compensate for the damage and meet the demands of increased cognitive resource allocation, the brain may enhance functional connectivity within the δ and θ frequency bands [ 45 , 46 ]. This compensatory mechanism could account for the higher levels of brain functional connectivity intensity and density observed in older adults with mild cognitive impairment compared to their healthy counterparts. As cognitive impairment worsens, the efficiency of brain functional networks further declines, and the neural networks within the brain become significantly disrupted, resulting in increased energy consumption due to excessive synchronous activity [ 48 ]. To compensate for this damage, brain functional connectivity in the low-frequency δ and θ bands exhibits pathological hypersynchronization, which eventually becomes rigid [ 47 ]. This may explain why older adults with moderate to severe cognitive impairment show higher brain functional connectivity intensity and density compared to those with mild cognitive impairment or healthy older adults. Furthermore, it is worth noting that the δ frequency band is strongly associated with deep sleep and repair processes, while the θ frequency band is closely linked to memory encoding and retrieval, spatial navigation, and emotional regulation [ 49 ]. These findings offer valuable insights into understanding and developing targeted interventions for brain functional connectivity in older adults with cognitive impairment, which should be further investigated in future research.

This study also revealed significant differences in both static features (Duration, Coverage, Occurrence) and dynamic characteristics (transition probabilities) of microstates A, B, C, and D among older adults with varying cognitive levels. Age, education level, Pittsburgh Sleep Quality Index, and physical activity may influence these differences in microstate parameters. Regarding static features, enhanced temporal characteristics of microstate B (linked to the dorsal attention network and visuospatial processing) and microstate D (associated with the frontoparietal control network) correlated with more severe cognitive impairment. Microstate A (connected to the language network and semantic processing) showed the strongest temporal features during the mild cognitive impairment stage, whereas the preservation of microstate C (aligned with the default mode network) was strongly associated with maintaining normal cognitive function. In terms of dynamic features, older adults with moderate to severe cognitive impairment displayed markedly increased directional transitions from microstate B/D to A/C. Those with mild cognitive impairment exhibited transitional patterns along the pathways from A to B/D and C to D, whereas healthy older adults predominantly demonstrated balanced bidirectional transitions between A/C ↔ C/A and B/D ↔ D/B. This abnormal phenomenon is likely the combined result of neural network inefficiency [ 48 ], compensatory mechanisms [ 45 , 46 ], and pathological hypersynchronization [ 47 ]. Among older adults with mild cognitive impairment, inefficiency in microstate C (associated with the default mode network) activates compensatory mechanisms in microstate A (language network), microstate B (dorsal attention network), and microstate D (frontoparietal control network) [ 50 – 52 ]. For older adults with moderate to severe cognitive impairment, compensatory mechanisms in microstates persist, but pathological hypersynchronization increasingly dominates microstate B (dorsal attention network) and microstate D (frontoparietal control network), ultimately leading to rigidity in transition patterns between networks [ 47 ]. Importantly, the brain sources of microstate A are located in the bilateral temporal and parietal regions, microstate B involves the occipital lobe and frontal visual cortex, microstate C encompasses the posterior cingulate cortex and insula, and microstate D is situated in the frontoparietal region. These findings offer valuable insights into understanding and developing precise interventions for microstates in older adults with cognitive impairment, which should be further explored in future research.

In conclusion, this study examined the coordinated patterns of spontaneous neural activity and instantaneous electrical activity in the brain by utilizing dual-dimensional indicators of brain functional connectivity and microstates. It investigated potential biomarkers for early screening and precise classification, offering clinical tools that are widely acceptable, cost-effective, suitable for community screening, and accurate for diagnosis. Our findings indicate significant differences in brain functional connectivity and microstate characteristics among older adults with different cognitive levels. These differences are not only closely associated with external factors such as age, education level, Pittsburgh Sleep Quality Index, and physical activity but also reflect the complex changes in spontaneous neural activity occurring in the brains of older adults as they progress through cognitive impairment. The observed imbalances, compensatory mechanisms, and rigidity in brain functional connectivity and microstates among older adults with cognitive impairment further support the notion of brain plasticity to a certain degree. Lastly, the specific pathways through which age, education level, Pittsburgh Sleep Quality Index, and physical activity (influencing factors) alter brain functional connectivity and microstates (internal changes), ultimately resulting in cognitive decline (external manifestations), still need further exploration. Future research should emphasize examining the degree to which these influencing factors can regulate the relationship between cognitive decline and brain function.


## Conclusion

There are significant differences in brain functional connectivity and microstate characteristics among older adults with varying cognitive levels. These differences are not only closely associated with external factors like age, education level, Pittsburgh Sleep Quality Index, and physical activity, but also reflect the complex changes in spontaneous neural activity that occur in the brains of older adults during the progression of cognitive impairment. Older adults with mild cognitive impairment show an increase in abnormal and redundant brain functional connections, where microstate C becomes inefficient, and compensatory mechanisms are observed in low-frequency brain functional connectivity and microstates A, B, and D. For older adults with moderate to severe cognitive impairment, compensatory mechanisms in brain functional connectivity and microstates are sustained, characterized by dominant abnormal and redundant connections, along with pathological hypersynchronization in microstates B and D, which leads to rigidity.


## Limitations and future perspectives

Given the limitations of the cross-sectional study design, we cannot establish causal conclusions; the current findings only allow for reasonable inferences about the outcomes. There remains a lack of strong longitudinal monitoring to assess the progression of cognitive impairment. Future research should aim to validate the inferences made in this study through cohort studies and other methodologies.

The assessments of physical activity and sleep quality index in this study were based on questionnaires, which may introduce subjectivity. Future research should consider using objective measurement tools (such as accelerometers). The screening and classification of participants were mainly conducted using the MoCA scale; future studies could integrate structural MRI, cerebrospinal fluid analysis, PET imaging, and other methods for more comprehensive screening and classification.

Considering the power of the sample size and the objectives of the study, this research did not separate older adults with moderate and severe cognitive impairment into distinct groups. Future research could increase the sample size to further investigate the neurophysiological characteristics of older adults across different levels of cognitive impairment.

Due to equipment limitations, this study employed a 24-channel EEG for analyzing brain functional connectivity and microstates. Future research could utilize high-density EEG (such as 32 or 64 channels) to further validate the findings of this study [ 53 ].


## Supplementary Information


## Acknowledgements

We are grateful to our research participants for their time and commitment.



FD, SJ, XW conceptualized the project. FD drafted the manuscript. FD, SJ, XX, SL, ZG, QL, XW, CW, XW, and CL developed the methodology. FD, XX, SJ, and XW analyzed the data. FD, XW, SJ, SL, CW reviewed and edited the manuscript. XW supervised the project. All authors discussed the results, contributed to the final version, and approved the final manuscript.


## Funding

National Social Science Fund Project: Research on the Dose-Effect Relationship and Application Strategies of Physical Exercise in Delaying Cognitive Decline in Older Adults (Project Number: 22BTY076); Shanghai Key Laboratory of Human Performance Development and Guarantee (Project Number: 11DZ2261100).


## Data availability

Data are available from corresponding authors.


## Declarations


### Ethics approval and consent to participate

This research complies with the Declaration of Helsinki and has been approved by the Ethics Committee of Shanghai University of Sport (Ethics ID: No. 102772020RT060). All participants voluntarily agreed to partake in the study and signed informed consent forms.


### Consent for publication


### Competing interests

The authors declare no competing interests.


## Footnotes

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials


### Data Availability Statement

Data are available from corresponding authors.
