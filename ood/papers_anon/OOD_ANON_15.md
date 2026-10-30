# De-Identified Manuscript `OOD_ANON_15`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract


### Background

Childhood maltreatment (CM) is a major risk factor for the development of major depressive disorder (MDD). To gain more knowledge on how adverse childhood experiences influence the development of brain architecture, we studied functional connectivity (FC) alterations of neural networks of depressed patients with, or without the history of CM.


### Methods

Depressed patients with severe childhood maltreatment ( n = 18), MDD patients without maltreatment ( n = 19), and matched healthy controls ( n = 20) were examined with resting state functional MRI. History of maltreatment was assessed with the 28-item Childhood Trauma Questionnaire. Intra- and inter-network FC alterations were evaluated using FMRIB Software Library and CONN toolbox.


### Results

We found numerous intra- and inter-network FC alterations between the maltreated and the non-maltreated patients. Intra-network FC differences were found in the default mode, visual and auditory networks, and cerebellum. Network modelling revealed several inter-network FC alterations connecting the default mode network with the executive control, salience and cerebellar networks. Increased inter-network FC was found in maltreated patients between the sensory-motor and visual, cerebellar, default mode and salience networks.


### Limitations

Relatively small sample size, cross-sectional design, and retrospective self-report questionnaire to assess adverse childhood experiences.


### Conclusions

Our findings confirm that severely maltreated depressed patients display numerous alterations of intra- and inter-network FC strengths, not only in their fronto-limbic circuits, but also in sensory-motor, visual, auditory, and cerebellar networks. These functional alterations may explain that maltreated individuals typically display altered perception and are prone to develop functional neurological symptom disorder (conversion disorder) in adulthood.


## 1. Introduction

Major depressive disorder (MDD) is a common, severe mental illness with complex pathophysiology ( Otte et al., 2016 ). Childhood maltreatment (CM) is one of the most important risk factors for the development of MDD. Meta-analytic studies document that all forms of maltreatment can lead to the development of depression in adulthood ( Li et al., 2016 , Gardner et al., 2019 , Humphreys et al., 2020 ). CM is a severe ethical and health issue as 300 million 2–4 years old children globally, i.e., three in every four children, experience physical and/or psychological abuse ( WHO Report on Childhood Maltreatment, 2020 ). Depressed patients with a history of maltreatment are more likely to develop severe, early-onset, treatment-resistant depression with chronic disease trajectory ( Nanni et al., 2012 , Nelson et al., 2017 , Opel et al., 2019 ). Modern neuroimaging tools have been extensively utilized to understand the structural and functional alterations in the brains of depressed individuals ( Cattarinussi et al., 2021 , Yang et al., 2021 , Tse et al., 2023 ). Understanding the maltreatment-associated structural and functional brain differences may help us to develop preventive and therapeutic interventions for MDD ( Nemeroff, 2016 , Lippard and Nemeroff, 2020 , Samson et al., 2024 ).

The exact physiological mechanisms mediating the long-term consequences of CM are not yet completely understood. Numerous studies focused on the long-lasting neurobiological impact of CM and sought to understand the structural and functional brain alterations contributing to the increased vulnerability of maltreated individuals to develop a mental illness ( Paquola et al., 2016 , Teicher et al., 2016 , Teicher and Samson, 2016 , Heany et al., 2018 , Popovic et al., 2020 , Oltean et al., 2023 , Ireton et al., 2024 , Tomoda et al., 2024 ). A leading theory is that childhood trauma and maltreatment act as a severe, or chronic stressor, leading to altered brain development, which in turn results in disturbed emotional and cognitive functioning and increases the susceptibility to psychiatric disorders such as MDD ( Ohashi et al., 2019 , Lippard and Nemeroff, 2020 , Rakesh et al., 2021 , Rakesh et al., 2023 , Tomoda et al., 2024 ). Indeed, structural magnetic resonance imaging (MRI) studies of adults with a history of CM report on reduced grey matter volumes of the hippocampus, amygdala, medial prefrontal, anterior cingulate, orbitofrontal, and dorsolateral prefrontal cortices ( van Harmelen et al., 2010 , Dannlowski et al., 2012 , Lim et al., 2014 , Opel et al., 2014 , Paquola et al., 2017 ). Parallel to these findings, a recent, multimodal meta -analysis of neuroimaging studies reported on structural and functional abnormalities of similar brain areas in MDD patients, e.g., hippocampus, amygdala and subgenual cingulate cortex ( Gray et al., 2020 ). The more recent large scale, mega-analytic studies of the ENIGMA-MDD network found that in depressed patients CM is associated with thinner cortices in the banks of the superior temporal sulcus and the supramarginal gyrus together with the reduced surface area of the middle temporal lobe ( Tozzi et al., 2020 ), while another whole-brain coordinate-based meta -analysis reported regional cortical thinning in the right anterior cingulate/paracingulate gyri and left middle frontal gyrus ( Yang et al., 2023 ). In harmony with the structural changes, functional MRI (fMRI) studies reveal altered activation of fronto-temporal-limbic structures, including mainly the superior frontal gyrus, left middle temporal gyrus, hippocampus and amygdala in maltreated patients performing fMRI tasks using socio-affective cues ( Dannlowski et al., 2012 , Heany et al., 2018 ).

More recently, investigations of functional connectivity (FC) of large-scale brain networks came into focus and increasing efforts have been made to understand how abnormal brain development can lead to the emergence of psychopathology and mental disorders ( Xia et al., 2018 , Lees et al., 2021 , Zhu and Qiu, 2022 ). Resting state functional magnetic resonance imaging (rs-fMRI) has evolved to a fundamental research tool to study dysfunctional neural networks underlying psychiatric conditions ( Yang et al., 2020 , Bondi et al., 2023 ). Numerous studies found fronto-limbic FC alterations both in depressed patients ( Mulders et al., 2015 ) and in individuals with a history of CM ( Teicher et al., 2016 , Teicher and Samson, 2016 , Ireton et al., 2024 , Tomoda et al., 2024 ). Notably, a thorough examination of multivariate network-related associations found that the history of childhood trauma showed by far the strongest association among patient symptom and FC strengths ( Yu et al., 2019 ). This comparison included numerous dimensional clinical symptoms, i.e., anxiety, anhedonia, depressive mood, neuroticism, suicidal tendency, and personality traits ( Yu et al., 2019 ).

The first study to investigate FC patterns in MDD patients with or without CM analyzed their data using graph-theory approach and reported on both overlapping and segregated FC patterns in whole-brain networks ( Wang et al., 2014 ). They found that both MDD patient groups showed reduced FC strength in the bilateral ventral medial prefrontal and ventral anterior cingulate cortices whereas, MDD patients with a history of neglect displayed widespread reduction of FC strength within the prefrontal-limbic-thalamic-cerebellar circuitry compared to patients without neglect ( Wang et al., 2014 ). A subsequent comprehensive study found that sexual, physical, and emotional abuse, were all strongly associated with increased connectivity within the dorsal attention network and between the dorsal attention and fronto-parietal networks ( Yu et al., 2019 ). In recent years, there have been a surge of studies investigating the long-term consequences of CM in depressed patients using rs-fMRI with various analytical methods. Some used seed-based interregional, or seed-based whole-brain functional connectivity analysis ( Xu et al., 2019 , Chen et al., 2022 , Luo et al., 2022 , Luo et al., 2022 , Wang et al., 2022 , Wang et al., 2022 , Goltermann et al., 2023 , Liu et al., 2024 ), others employed spatial independent component analysis (ICA; Fadel et al., 2021 , Luo et al., 2022 ). All these studies describe numerous intra-network and inter-network alterations of FC as a consequence of childhood trauma or maltreatment, but there's a great deal of variability between the reported changes. Notably, a very recent large-scale study, involving 1325 participants, could not replicate most of the previous discoveries instead, they could find only one robust maltreatment-associated alteration, namely an increased connectivity between the amygdala and dorsolateral frontal areas ( Goltermann et al., 2023b ). Notably, there are also negative reports, documenting no association between adverse childhood experiences and brain activity/connectivity (e.g. Belleau et al., 2022 , Gruzman et al., 2024 ). More recent studies reported that FC alterations may correlate with the severity of the maltreatment and moderate the relationship between maltreatment and depression severity ( Yu et al., 2024 ). Another study found that the combined assessment of resting-state cerebral blood flow and FC abnormalities in MDD patients had the satisfactory classification ability to differentiate MDD patients with or without CM ( Liu et al., 2024 ), suggesting that these methods may function as potential neuroimaging biomarkers.

To address these inconsistencies, we set out to examine intra- and inter-network connectivity alterations in three groups of participants: 1) MDD patients who experienced severe to extreme maltreatment (MDD + CM group); 2) MDD patients who were exposed to moderate childhood maltreatment at most (MDD group) and 3) healthy, never-depressed controls (HC group). Individuals were carefully selected to match their age, gender, IQ, education level and depression severity in the experimental groups. We performed intra- and inter-network functional connectivity analysis using state-of-the-art evaluation softwares. FSL is a widely used program for intra-network analysis, while CONN is one of the most advanced tools for inter-network FC evaluation. Due to the noise in the rs-fMRI data, we applied a very thorough cleaning method to pre-process both the intra- and inter-network FC. Our hypothesis was that depressed patients with a history of severe CM will exhibit numerous altered intra- and inter-network architecture compared with non-maltreated MDD patients not only in their fronto-parietal circuits, but a more widespread alteration and that these alterations may correlate with the clinical symptoms.


## 2. Materials and methods


### 2.1. Subjects

MDD patients (N = 37) were recruited from the Affective Disorder Unit of the Department of Psychiatry and Psychotherapy, Clinical Centre, University of Pécs. Patients with severe maltreatment formed the MDD + CM group (N = 18), and individuals with a low incidence of CM formed the MDD group (N = 19). For detailed description on the psychological evaluation and on the assessment of CM of the recruited individuals see the Supplementary Material s and our earlier reports ( [AUTHOR] et al., 2019 , Nagy et al., 2021 ). In brief, the severity of depression was evaluated using the 21-item Hamilton Depression Rating Scale and the Beck Depression Inventory (BDI; Beck et al., 1961 ), whereas the severity of anxiety was examined with Beck Anxiety Inventory (BAI; Beck et al., 1988 ). General Intelligence Quotient (IQ) was measured with a four-subtest version of Hungarian adaptation of the Wechsler Adult Intelligence Scale-Revised ( Kaufman et al., 1991 , Wechsler, 1997 , Nagybányai Nagy and Rózsa, 2006 ).

All patients were tested with the 11-item general traumatic experiences subscale of the 27-item Early Trauma Inventory–Self Report questionnaire ( Bremner et al., 2007 ) to scan the exposure of causal traumatic life events during childhood. Subjects with experience of any random events (e.g., accident, natural disaster) in childhood were excluded from the study. Childhood maltreatment was specified as a chronic or/and repeated exposition to various type of neglect (physical, emotional) or/and abuse (physical, emotional, sexual) prior to the age of 18 years. The history of maltreatment was assessed retrospectively with the Hungarian Short Form version of self-reported 28-item Childhood Trauma Questionnaire-Short Form (CTQ; Bernstein et al., 2003 , Kenézlői et al., 2023 ).

We have validated the Hungarian version of the CTQ by testing it in large clinical and community samples. Details of these assessments (including exploratory and confirmatory factor analyses, differences between clinical and non-clinical populations, etc.) have been published before ( Csernela et al., 2021 , Kenézlői et al., 2023 ). The CTQ test measures the severity of five types of maltreatment before the age of 18 years: physical abuse (PA), emotional abuse (EA), physical neglect (PN), emotional neglect (EN), and sexual abuse (SA). Each subscale consists of 5 items, all of them are evaluated on 5-point Likert scales. In our hands, the internal consistency was excellent for the subscales: EA = 0.93, EN = 0.94, SA = 0.97, PA = 0.93, and good for the subscale PN = 0.77 ( Csernela et al., 2021 ). During the data analysis, CTQ raw scores were recoded into a two-level, binary variable by cut-off values on each subscale. Based on the literature, cut-off values (between low, moderate, and severe maltreatment) were defined based on a large normative sample consisting of 330 participants (university students and community sample). When CTQ scores in any maltreatment dimension were at least in the moderate range (or above that), then, exposure to high childhood maltreatment was assumed.

Participants of the present study were enrolled in the MDD + CM subgroup if they had CTQ scores higher than the cut-off value of the „low” range in any CTQ subscale. The exact cut-off values of the „low” range were the following in the different CTQ subscales: EA: >12; PA: >9; SA: >7; EN: >14; PN: >9. The different cut-off values for each subscale are summarized in Supplementary Table 1 .

To control for the subjectivity of the retrospective self-reports a senior author (MS), blinded to the results of the CM questionnaires, conducted a structured interview with all participants, focusing on childhood adversities. Afterwards, results of the interviews were compared with the scores of trauma scales by a psychologist blinded to the patient. Discrepancies were discussed with the participants and in case of unresolvable discrepancies, the participant was excluded from further analyses (N = 3).

All patients fulfilled the DSM-5 diagnostic criteria of MDD ( American Psychiatric Association, 2013 ), assessed by a trained psychiatrist (MS) using the Structured Clinical Interviews for DSM-5 disorders (SCID-5-CV and SCID-5-PD; First et al., 2015 , First et al., 2016 ). Inclusion criteria were: (1) age 18–50 years; (2) MDD diagnosis with a current major depressive episode (>8 points on the Hamilton Depression Rating Scale, 21-item version, Hamilton, 1967 ). Patients were enrolled in the non-maltreated MDD subgroup who had CTQ scores lower than the cut-off value of the „low” range in any CTQ subscale. The exact cut-off values of the „low” range were the following in the different CTQ subscales: EA: <12; PA: <9; SA: <7; EN: <14; PN: <9.

Non-excluding psychiatric disorders were in our study: anxiety disorders (panic disorder N = 3; generalized anxiety disorder N = 3; social phobia N = 2; specific phobias N = 4); cluster C personality disorders (dependent N = 2, avoidant N = 2); obsessive–compulsive disorder in the past 6 years, and never treated when symptomatic before (N = 1); lifetime sedatives, hypnotics, and anxiolytics use disorder (N = 2) in full remission for more than 2 years; mild and non-chronic alcohol use disorder (N = 2). The mean age of disease onset was 26.44 ± 9.71 years. The mean duration of illness was 6.61 ± 7.06 years (range 0.2–26 years). Thirty-six (97 %) patients with MDD were treated with antidepressant medication: SSRIs (N = 25); SNRIs (N = 3); NaSSAs (N = 7); agomelatine (N = 4); trazodone (N = 2); combined with mood stabilizer (N = 2); combined with low-dose atypical antipsychotics (N = 5).

The control group (N = 20) was matched in age, sex, IQ, and level of education to the entire MDD group. Control subjects had no lifetime or family history of mental disorders, and the Symptom-Checklist-90-R ( Derogatis, 1994 ) was applied to rule out subthreshold psychiatric symptoms.

We set the following exclusion criteria for participation: head injury, current substance use (i.e. abstinence for < 2 years), history of internal medical or neurological disorders, hearing or visual impairment, an IQ < 85, and any MR scanning issues (e.g. claustrophobia, or metal objects in the body). Moreover, no participants exposed to traumatic life events fulfilling the DSM-5 posttraumatic stress disorder (PTSD) criterion A were enrolled in this study.

The local Research Ethics Committee of the University of Pécs approved the study design and protocol (Ethical Approval Nr.: 2015/5626). All participants were Hungarian speaking Caucasians, living in the urban and suburban area of Pécs, and gave written informed consent.


### 2.2. Magnetic resonance imaging

Our data were collected with a 3 T Magnetom TIM Trio MRI scanner (Siemens AG, Erlangen, Germany) using a 12-channel head coil. Anatomical measurements were acquired using an isotropic T1-weighted 3D magnetization prepared rapid acquisition with gradient echo (MPRAGE) sequence with the following parameters: repetition time/inversion time/echo time (TR/TI/TE) = 2530/1100/3.37 ms; Flip angle = 7°; 176 sagittal slices with a thickness of 1 mm; Field of view (FOV) = 256 mm × 256 mm 2 ; matrix size = 256 × 256; receiver bandwidth = 200 Hz/pixel; number of averages = 1. For rs-fMRI measurements, a single shot echo planar imaging sequence was used with the following parameters: TR/TE = 3000/36 ms; acquisition time = 13:00 min; Flip angle = 83°; 44 axial slices; slice thickness = 3 mm; receiver bandwidth = 1242 Hz/pixel; FOV = 228 × 228 mm 2 ; matrix size = 76 × 76. During rs-fMRI, all participants fixated to a white cross presented at the centre of the screen on a black background via an MRI-compatible system (VisualSystem NordicNeuroLab AS, Bergen, Norway) specifically designed for fMRI studies.


### 2.3. Data processing

We combined the FMRIB Software Library and CONN Connectivity Toolbox to analyze our data. FSL Dual regression analysis is a widely used multivariate regression method for identifying between-group differences in FC of resting-state networks that reflect differences in shape and amplitude ( Nickerson et al., 2017 ). CONN is an approach to analyze the whole brain connectome ( Whitfield-Gabrieli and Nieto-Castanon, 2012 , Whitfield-Gabrieli and Ford, 2012 , Nieto-Castanon and Whitfield-Gabrieli, 2021 ), focusing on the overall multivariable pattern of functional connections between a given voxel and other parts of the brain ( Nieto-Castanon, 2022 ).


#### 2.3.1. Pre-processing for intra-network rs-fMRI data analysis

Detailed data pre-processing is described in the Supplementary Materials . Briefly FSL (version: 5.0.9; https://fsl.fmrib.ox.ac.uk/fsl/fslwiki )) Multivariate Exploratory Linear Decomposition into Independent Components Tool, (version: 3.14, https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/MELODIC ) was used to make motion correction, slice time correction, spatial smoothing, high-pass filtering, spatial registration, and variance normalization. Thereafter the data was cleaned by FMRIB’s ICA-based Xnoiseifier (version: 1.06.15; https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIX ).


#### 2.3.2. Intra-network rs-fMRI data analysis

After the clean-up method, a multi-session temporal concatenation ICA was run to get group-level spatial maps and timeseries, and then whole-brain general linear model (GLM) high level, non-time series statistical analyses were carried out. To detect differences between the examined groups, dual regression (version: 0.5 beta; https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/DualRegression ; Nickerson et al., 2017 ) analysis controlled for age and gender was applied on 27 independent components (out of 54) using permutation testing with 10.000 permutations. Threshold-free cluster enhancement (TFCE) was applied to correct for multiple comparisons. F-test was applied to see whether general between-group difference exists ( Donna et al., 2022 ). In case of any significance, further pairwise t-tests were applied to assign the directions of differences. During group comparison and network modelling significant differences in clusters larger than 10 voxels were considered acceptable.

Dual regression analysis was also applied to detect interaction effects of CTQ total score, BDI and BAI × group on rs-fMRI activation patterns. F-test was also applied to see whether any interaction effects were present. In case of significance, within group correlations were applied to determine the direction of the differences.


#### 2.3.3. Pre-processing for inter-network rs-fMRI data analysis

Seed-based voxel-wise (region of interest (ROI)-to-voxel) and ROI-to-ROI resting-state functional connectivity analyses were performed using the CONN Functional Connectivity Toolbox (RRID:SCR_009550 release 21a; https://web.conn-toolbox.org/ ; Whitfield-Gabrieli and Nieto-Castanon, 2012 , Whitfield-Gabrieli and Ford, 2012 ; Whitfield-Gabrieli and Nieto-Castanon, 2012 ). The CONN Toolbox was used to perform the following pre-processing steps: motion correction, slice time correction, and Artefact detection Tool −-based outlier detection ( https://www.nitrc.org/projects/artifact_detect/ ; Whitfield-Gabrieli et al., 2011 ). A simultaneous normalization to the Montreal Neurological Institute (MNI152) space data with a resampling voxel size of 2 × 2 × 2 mm 3 was also applied and spatial smoothing with an isotropic 6 mm FWHM Gaussian kernel was used during pre-processing. T1-weighted MPRAGE structural scans were normalized to MNI space and segmented into grey matter, white matter (WM) and cerebrospinal fluid (CSF).

A standard denoising pipeline according to Nieto-Castanon (2020) was used to regress out the effects of confounding variables from the time series data. Briefly, linear de-trending was applied to identify and remove the possible confounding effects separately for each voxel of each subject including the WM (first 5 PCA components) and CSF signals (first 5 PCA components), realignment parameters (12 parameters), and the scrubbing variables. To minimize the effect of head motion, physiological or other noise effects the band-pass filter was applied and set to 0.008–0.09 Hz.


#### 2.3.4. Inter-network rs-fMRI data analysis

To define ROIs for further ROI-to-voxel and ROI-to-ROI analysis a multivoxel pattern analysis (MVPA) was used on pre-processed and de-noised data ( Nieto-Castanon, 2022 ). As a next step, between-group differences were evaluated by using these ROIs as seeds, to evaluate differences in FC strengths of a specific seed and other brain voxels, and FC strengths between the seed and other ROIs specified by the MIST64 atlas. Gaussian Random Field theory was applied to assess cluster-based inferences between groups, with False Discovery Rate (FDR)-corrected cluster threshold of p < 0.05 and uncorrected voxel threshold of p < 0.001. In case of ROI-to-ROI analysis, connections were thresholded at uncorrected p < 0.05, while cluster threshold was set to ROI-level FDR-corrected p < 0.05, ROIs were sorted using hierarchical clustering. Age and gender were used as covariates in group-level ROI-to-voxel and ROI-to-ROI analyses.


### 2.4. Statistical analysis of clinical and demographic data

SPSS statistical software (v.26.0, IBM Corp.) was applied to analyze clinical and demographic data. Group comparisons of data with normal distribution were carried out with one-way ANOVA, chi-square test was applied to compare discrete variables and Fisher’s exact test were used for categorical variables. Data with irregular distributions were compared with Mann-Whitney- U test or Kruskall-Wallis-H test followed by Dunn Bonferroni post hoc test. The significance level was set at p < 0.05.


## 3. Results


### 3.1. Demographic data and clinical characteristics

The demographic data and exact scores of the three experimental groups at the various CTQ subscales are listed in Table 1 . No significant group differences were found for age, gender, years of education and IQ. The clinical characteristics of the maltreated and non-maltreated depressed patients were very similar ( Table 1 ), except that the CTQ scores of maltreated depressed patients were much higher compared to the non-maltreated and control groups on each subscale. Individuals of the MDD + CM group experienced severe childhood maltreatment as their total CTQ scores were 62.2 ± 13.4 (mean ± SD), while the CTQ scores of MDD and HC groups were similar ( Table 1 ). The most common maltreatment subtypes were the emotional neglect and emotional abuse as 61 % of the MDD + CM individuals experienced severe EN and 67 % of them were subjected to severe EA ( Supplementary Table 2 ).


#### Table 1.

Demographic, IQ, CTQ and clinical data.



|  | MDD + CM (N = 18) | MDD (N = 19) | HC (N = 20) | Between-group differences |
| --- | --- | --- | --- | --- |
| Age (years) a | 32.5 ± 8.39 | 33.68 ± 7.77 | 32.3 ± 7.83 | non-significant * |
| Number of females (%) | 12 (66.67 %) | 12 (63.16 %) | 13 (65.00 %) | non-significant ** |
| Years of education b | 12 (11.37–15.5) | 12 (12–17) | 15 (12–16.5) | non-significant § |
| IQ a | 109.9 ± 7.4 | 112.1 ± 5.7 | 114.8 ± 6.6 | non-significant # |
| CTQ sum b | 61 (53.75–71) | 33 (29–38) | 29 (27–33) | χ 2 = 34.161, p < 0.001 § ; post hoc : MDD vs HC, NS; MDD + CM vs HC, p < 0.001; MDD + CM vs MDD, p < 0.001 |
| CTQ physical neglect b | 10 (8–12.5) | 6 (5–7) | 5 (5–5) | χ 2 = 33.133, p < 0.001 § ; post hoc : MDD vs HC, NS; MDD + CM vs HC p < 0.001; MDD + CM vs MDD p < 0.001 |
| CTQ physical abuse b | 9 (7–12.25) | 5 (5–5) | 5 (5–5) | χ2 = 31.791, p < 0.001 § ; post hoc : MDD vs HC, NS; MDD + CM vs HC, p < 0.001; MDD + CM vs MDD, p < 0.001 |
| CTQ emotional neglect b | 18 (16–20) | 10 (7–13) | 8 (6–10.75) | F = 43.289, p < 0.001*; post hoc : MDD vs HC, NS; MDD + CM vs HC, p < 0.001; MDD + CM vs MDD, p < 0.001 |
| CTQ emotional abuse b | 18 (10.75–20) | 7 (5–9) | 6 (5.25–8) | χ2 = 28.027, p < 0.001 § ; post hoc : MDD vs HC, NS; MDD + CM vs HC, p < 0.001; MDD + CM vs MDD, p < 0.001 |
| CTQ sexual abuse b | 8 (5–9.25) | 5 (5–5) | 5 (5–5) | U = 107.00, p = 0.013† |
| Beck Depression Inventory b | 23.5 (17.75–28.25) | 22 (18–24) | 3 (2–6) | χ2 = 38.833, p < 0.001 § ; post hoc : MDD + CM vs HC, p < 0.001; MDD vs HC, p < 0.001; MDD + CM vs MDD, NS |
| Beck Anxiety Inventory b | 22 (16–30.5) | 18 (8–24) | 3 (1.25–10.75) | χ2 = 28.619, p < 0.001 § ; post hoc : MDD + CM vs HC, p < 0.001; MDD vs HC, p = 0.001; MDD + CM vs MDD, NS |
| Age at illness onset b | 20.5 (16–33.25) | 29 (18–34) | − | non-significant † |
| Length of illness (years) b | 2 (1–––3) | 2 (1–––2) | − | non-significant † |
| Number of MDD episodes b | 6.5 (0,3–12) | 5 (1–7) | − | non-significant † |


Notes: * One-way ANOVA with Dunn-Bonferroni post hoc test; ** Chi-square test; § Kruskal-Wallis H with Dunn-Bonferroni post hoc test; † Mann-Whitney U test (comparison of MDD + CM and MDD groups); # Fisher’s exact test; a mean ± SD; b median (interquartile range).

Abbreviations: MDD + CM: major depressive disorder with childhood maltreatment; MDD: major depressive disorder; HC: healthy control; CTQ: Childhood Trauma Questionnaire; IQ: intelligence quotient; NS: non-significant; vs : versus.


### 3.2. Intra-network FC differences: Between group comparisons

We detected significant between group differences in case of 3 components. We found significantly decreased FC in maltreated MDD subjects compared to the MDD group in the following brain structures: right occipital fusiform gyrus, right precuneus cortex, right supracalcarine cortex, right intracalcarine cortex, right lingual gyrus, left occipital pole, and left precentral gyrus ( Fig. 1 A). These areas were organized into 3 clusters as shown in Table 2 . Furthermore, we found significantly increased FC in the MDD + CM subjects compared to the MDD group in the following areas: left hippocampus, left amygdala, posterior part of the left middle temporal gyrus, right cerebellum crus I, right cerebellum VI, right cerebellum crus I, right cerebellum vermis crus II, right cerebellum vermis VI, right occipital fusiform gyrus, left cerebellum crus I, left planum polare, organised into 5 clusters ( Fig. 1 B and Table 2 ).


#### Fig. 1.


> **Figure/Table Caption:** Intra-network group differences of functional connectivity (FC) strengths between the MDD + CM and MDD groups controlled for age and gender. (A) Decreased FC in the MDD + CM group compared to the non-maltreated MDD subjects. Axial slices are presented in radiological convention for Montreal Neurological Institute space (MNI152) slice coordinates from Z = 30 mm to Z = 63 mm. (B) Increased FC in the MDD + CM group compared to the non-maltreated MDD patients. Axial slices are presented in radiological convention for MNI slice coordinates from Z = 29 mm to Z = 49 mm. Images were corrected for family-wise error and thresholded at p < 0.05. The color-bars show the p-values from the between-group comparison.


#### Table 2.

Intra-network resting-state FC differences between MDD + CM and MDD groups.



| Contrast | Number of voxels | Cluster | Area | p-value | x | y | z |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MDD + CM < MDD (decreased FC in maltreated patients) | 1505 | 1 | Right occipital fusiform gyrus visual network | 0.003 | 10 | −76 | −20 |
|  |  |  | Right precuneus cortex default mode network | 0.014 | 28 | −58 | 12 |
|  |  |  | Right supracalcariane cortex visual network | 0.014 | 28 | −60 | 16 |
|  |  |  | Right intracalcarine cortex visual network | 0.016 | 28 | −70 | 6 |
|  |  |  | Right lingual gyrus visual network | 0.016 | 14 | −78 | −6 |
|  |  | 2 | Left occipital pole visual network | 0.015 | −12 | −92 | 24 |
|  |  | 3 | Left precentral gyrus sensorimotor network | 0.038 | −36 | −18 | 34 |
|  |  |  |  |  |  |  |  |
| MDD + CM > MDD (higher FC in maltreated patients) | 528 | 1 | Left hippocampus default mode network | 0.016 | −24 | −18 | −20 |
|  |  |  | Left amygdala default mode network | 0.019 | –22 | −12 | −12 |
|  |  |  | Left middle temporal gyrus posterior part default mode network | 0.025 | −42 | −24 | −6 |
|  |  | 2 | Right cerebellum crus I cerebellar network | 0.016 | 12 | −74 | −28 |
|  |  |  | Right cerebellum VI cerebellar network | 0.023 | 10 | −70 | −26 |
|  |  |  | Left cerebellum crus I cerebellar network | 0.028 | −8 | −74 | −30 |
|  |  |  | Right cerebellum vermis crus II cerebellar network | 0.035 | 2 | −72 | −28 |
|  |  |  | Right cerebellum vermis VI cerebellar network | 0.049 | 2 | −78 | −26 |
|  |  | 3 | Right occipital fusiform gyrus visual network | 0.027 | 24 | −86 | −10 |
|  |  | 4 | Left cerebellum crus I. cerebellar network | 0.035 | −40 | −68 | −30 |
|  |  | 5 | Left planum polare auditory network | 0.035 | −56 | −4 | −2 |
|  |  |  |  |  |  |  |  |


Notes: x, y and z are the coordinates of local maximum in mm in the MNI152 standard space; number of voxels: sum of the voxels of all clusters within the contrast.

Abbreviations: MDD + CM: major depressive disorder with childhood maltreatment; MDD: major depressive disorder.

We also found differences in cerebellar areas, when we compared MDD subjects to the HC group ( Table 3 ). Here, there were significantly increased FC in the MDD group in the right posterior supramarginal gyrus, and in the right supracalcarine cortex, while decreased activity was found in the cerebellum right VI, in the right crus I and II, and in the vermis crus II.


#### Table 3.

Intra-network resting-state FC differences between the MDD and HC groups.



| Contrast | Number of voxels | Cluster | Area | p-value | x | y | z |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MDD > HC (higher FC in depressed patients) | 23 | 1 | Right posterior supramarginal gyrus sensorimotor network | 0.037 | 44 | −40 | 12 |
|  |  | 2 | Right supracalcariane cortex visual network | 0.012 | 8 | −78 | 16 |
|  |  |  |  |  |  |  |  |
| MDD < HC (decreased FC in depressed patients) | 159 | 1 | Right cerebellum VI cerebellar network | 0.007 | 10 | −70 | −18 |
|  |  |  | Right cerebellum crus I cerebellar network | 0.010 | 10 | −74 | −26 |
|  |  |  | Right cerebellum crus II cerebellar network | 0.014 | 14 | −74 | –32 |
|  |  |  | Right cerebellum vermis crus II cerebellar network | 0.021 | 4 | −74 | −30 |


Notes: x, y and z are the coordinates of local maximum in mm in the MNI152 standard space; number of voxels: sum of voxels of all clusters within the contrast.

Abbreviations: MDD: major depressive disorder; HC: healthy control.


#### 3.2.1. Intra-network FC differences: Interaction effects on FC strengths

Significant interaction effect was found between total CTQ scores of MDD + CM group versus HC subjects on FC strengths in the parietal, frontal and temporal lobes and in the limbic system. Further analysis showed a positive correlation between FC strengths and total CTQ scores in the right angular gyrus of the HC group (p = 0.002; Number of voxels: 12; MNI coordinates in mm: x = 42; y = -54; z = 50), but there was no significant correlation in MDD + CM subjects.

We also analyzed the interaction effects of anxiety and depression severity × group interaction on FC strengths, but these analyses yielded no positive outcome.


### 3.3. Inter-network FC differences


#### 3.3.1. Multivoxel-pattern analysis

Based on MVPA analysis, 8 areas were determined where we found between-group differences in FC strengths, and these were the left pre/postcentral gyrus, the right frontal pole, the right putamen, the cerebellum vermis X, the left posterior supramarginal gyrus, the cerebellum crus I., the precuneus cortex and the right superior lateral occipital cortex. All these 8 areas were used as seeds in the ROI-to-voxel and in the ROI-to-ROI analysis.


#### 3.3.2. Roi-to-voxel and ROI-to-ROI analysis

In ROI-to-voxel analysis, we found numerous inter-network between-group differences of FC strengths, except when using the cerebellum crus I as seed. The results are summarized in Table 4 . In the ROI-to-ROI analysis, we found increased FC strengths in the MDD + CM group compared to the MDD group in the neural networks from the pre/postcentral gyrus (sensorimotor network) to the anterior cingulate cortex (default mode network), to the bilateral superior parietal lobe (sensorimotor network) and to the left cerebellum VI (cerebellar network) with FDR-corrected p = 0.002488 (F (2,50) :12.00). In addition to that, the FC of the anterior cingulate cortex had stronger connectivity to the bilateral superior parietal lobe in maltreated patients compared to the MDD group (FDR-corrected p = 0.017899, F (2,50) : 8.26). These results are presented on Fig. 2 .

Inter-network resting-state FC differences between the groups in the ROI-to-voxel analysis.



| Seed | Contrast | x | y | z | Number of voxels | p-FDR | Areas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| left posterior supramarginal gyrus sensorimotor network | MDD + CM > MDD (higher FC in maltreated patients) | 24 | −58 | −4 | 228 | 0.000295 | right inferior lateral occipital cortex visual network |
|  | −44 | −66 | −14 | 205 | 0.000343 | left inferior lateral occipital cortex visual network |
|  |  | –32 | −82 | 14 | 132 | 0.004234 | left superior lateral occipital cortex visual network |
|  | MDD + CM < MDD (decreased FC in maltreated patients) | 56 | −44 | 42 | 115 | 0.006731 | right posterior supramarginal gyrus sensorimotor network |
|  |  |  |  |  |  |  |  |
| cerebellum vermis X. cerebellar network | MDD + CM < HC | −4 | −80 | 48 | 98 | 0.005522 | left precuneus cortex default mode network |
|  |  |  |  |  |  |  |  |
| right putamen basal ganglia resting state network | MDD < HC | –22 | −42 | 68 | 322 | 0.000001 | left superior parietal lobe sensorimotor network |
|  | 26 | −50 | 70 | 272 | 0.000002 | right superior parietal lobe sensorimotor network |
|  |  | 56 | −64 | 6 | 110 | 0.002724 | right inferior lateral occipital cortex visual network |
|  |  | −64 | −24 | 20 | 84 | 0.007318 | left anterior supramarginal gyrus sensorimotor network |
|  |  | −50 | −26 | 34 | 81 | 0.007318 | left postcentral gyrus sensorimotor network |
|  | MDD > HC | −52 | 24 | 16 | 94 | 0.005057 | left inferior frontal gyrus pars triangularis executive control network |
|  | MDD + CM > HC | 34 | −12 | 46 | 102 | 0.008290 | right precentral gyrus sensorimotor network |
|  | MDD + CM > MDD (higher FC in maltreated patients) | −64 | −24 | 20 | 573 | <0.00001 | left anterior supramarginal gyrus sensorimotor network |
|  |  | 60 | 8 | 2 | 410 | <0.00001 | right insular cortex salience network |
|  |  | 24 | −36 | 58 | 352 | <0.00001 | right postcentral gyrus sensorimotor network |
|  |  | –22 | −42 | 66 | 314 | <0.00001 | left superior parietal lobe executive control network |
|  |  | −48 | 2 | 0 | 259 | 0.000003 | left planum polare auditory network |
|  |  | 14 | −56 | −6 | 187 | 0.000050 | right lingual gyrus visual network |
|  |  | −6 | −2 | 40 | 178 | 0.000065 | left anterior cingulate cortex default mode network |
|  |  | −8 | −66 | −2 | 171 | 0.000079 | left lingual gyrus visual network |
|  |  | 66 | −12 | 14 | 129 | 0.000570 | right cingulate gyrus cingulo-opercular network |
|  |  | 56 | −62 | 40 | 108 | 0.001224 | right inferior occipital cortex visual network |
|  |  |  |  |  |  |  |  |
| right frontal pole executive control network | MDD + CM < HC | −38 | −62 | −30 | 180 | 0.001270 | left cerebellum crus I. cerebellar network |
| MDD + CM > MDD (higher FC in maltreated patients) | −10 | −54 | 38 | 197 | 0.000705 | left precuneus cortex default mode network |
|  | MDD + CM < MDD (decreased FC in maltreated patients) | −56 | −38 | 26 | 145 | 0.002668 | left parietal operculum cingulo-opercular network |
|  |  | −4 | 6 | 32 | 125 | 0.002906 | left anterior cingulate cortex default mode network |
|  |  | 60 | 14 | 4 | 125 | 0.002906 | right inferior frontal gyrus pars opercularis executive control network |
|  |  | −42 | 12 | −4 | 123 | 0.002906 | left insular cortex salience network |
|  |  | 68 | −42 | 32 | 108 | 0.004962 | right posterior supramarginal gyrus sensorimotor network |
|  |  |  |  |  |  |  |  |
| left pre/postcentral gyrus sensorimotor network | MDD + CM > HC | 12 | 14 | 36 | 145 | 0.002807 | right anterior cingulate cortex default mode network |
|  | −56 | −36 | 24 | 107 | 0.007414 | left parietal operculum cingulo-opercular network |
|  |  | −8 | 10 | 38 | 103 | 0.007414 | left paracingulate gyrus salience network |
|  | MDD + CM > MDD (higher FC in maltreated patients) | 0 | −66 | −16 | 683 | <0.00001 | left cerebellum VI. cerebellar network |
|  |  | 8 | 12 | 38 | 538 | <0.00001 | right anterior cingulate cortex default mode network |
|  |  | −2 | −86 | 0 | 356 | <0.00001 | left intracalcarine cortex visual network |
... (9 rows truncated) ...


Notes: x, y and z are coordinates in mm MNI152 standard space.

Abbreviations: MDD + CM: major depressive disorder with childhood maltreatment; MDD: major depressive disorder; HC: healthy control.


> **Figure/Table Caption:** Inter-network between-group differences in functional connectivity. (A) The connectogram with red line represents greater functional connectivity (FC) between the anterior cingulate cortex, the left pre/postcentral gyrus, the left cerebellum VI. and bilateral superior parietal lobe in maltreated patients compared to the non-maltreated MDD group. The color bar illustrates T-values. The circular sections show only those clusters of brain areas where functional connectivity was different between the groups. The highest p-value was observed in a cluster containing left pre/postcentral gyrus, anterior cingulate cortex and left cerebellum VI (FDR-corrected p = 0.002488). (B) Between-group differences are visualized anatomically in the brain using human Brainnetome Atlas of Fan ( Fan et al., 2016 ) in Montreal Neurological Institute space (MNI152). The coronal slices are from Z = 35.25 mm to Z = -64.75 mm. Red lines indicate significantly higher functional connectivity in MDD + CM subjects compared to MDD group between ROIs depicted with different colors. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)


## 4. Discussion

Here, we recruited depressed patients with or without the history of childhood maltreatment and investigated the intra-network and inter-network alterations with rs-fMRI. We focused primarily on differences between the maltreated and non-maltreated depressed patients, and we report here the results of the analysis in a way, that the non-maltreated MDD group served as the baseline for the comparisons. We found that maltreated patients had decreased FC in several right hemispheric areas of their visual network and in the right precuneus cortex, as part of the default mode network (DMN), compared to non-maltreated depressed patients. Furthermore, maltreated patients had increased FC in their left hippocampus and left amygdala, as part of the DMN, and increased FC in several cerebellar structures especially in the right hemisphere of the cerebellum and several left hemispheric areas of the auditory network compared with non-maltreated depressed patients.

Network modelling revealed numerous intra-network alterations, many of these involved the same neural circuits as the inter-network alterations. Once again, focusing primarily on differences between the maltreated and non-maltreated patients, we found the following changes: 1) increased FC strengths between the i) sensorimotor − default mode networks, ii) sensorimotor − salience networks, iii) sensorimotor − cerebellar networks, iv) sensorimotor − visual networks, v) executive control − default mode networks, and vi) from the basal ganglia resting state network to all other major networks; 2) we found decreased FC strengths between the i) executive control − default mode networks, ii) executive control − cingulo-opercular networks, iii) executive control − salience networks, iv) visual − sensorimotor networks, and v) between the default mode and salience networks. In all these comparisons, the non-maltreated depressed group served as the baseline.

A major strength of our study is that we report here on both intra-network and inter-network FC alterations. Furthermore, the maltreated patients of our study experienced severe childhood maltreatment as their total CTQ scores were > 60, while comparable studies include subjects with total CTQ scores ranging between 40–50, occasionally up to 55 (see e.g. He et al., 2022 , Wu et al., 2021 , Zhang et al., 2021 , Dong et al., 2022 , Luo et al., 2022 , Luo et al., 2022 , Wang et al., 2022 , Wang et al., 2022 , Rong et al., 2023 , Gruzman et al., 2024 , Liu et al., 2024 ). The severity of the maltreatments may explain why we found such widespread disturbances of neural circuits. However, in our present study, we found no association between FC strengths and severity of maltreatment, or between FC strengths and clinical symptoms.

In our maltreated subjects, emotional abuse and neglect were the two most common maltreatment subtypes. We did not focus on the specific effect of different maltreatment types, mainly because our sample size did not allow the forming of different subgroups (based on the various trauma subtypes) and because abuse and neglect (both emotional and physical) often co-occur. Only a few studies addressed the effect of different types of maltreatment on functional connectivity, e.g., a very recent report found significant association between childhood threat (abuse) and functional connectivity of key reward regions (nucleus accumbens and amygdala), while deprivation (neglect) had no specific influence on functional connectivity ( Liuzzi et al., 2024 ).

While the sample size of our case-control study was relatively low, in order to compensate for this limitation, we selected the subjects very carefully to match their age, gender, IQ, education level and depression severity. Furthermore, we performed a thorough psychological assessment of the recruited individuals, we collected blood samples to investigate potential laboratory biomarkers and carried out various MRI measurements. Several observations from this cohort have already been reported before: 1) we documented that the maltreated patients had higher serum triglyceride and lower HDL-cholesterol concentrations compared to non-maltreated MDD patients and that the severity of childhood adversity was a stronger predictor of serum lipid profiles than depression severity ( Péterfalvi et al., 2019 ); 2) maltreated individuals had impaired theory of mind abilities when they were examined with the Reading the Mind in the Eyes Test (RMET, [AUTHOR] et al., 2019 ) and 3) exposure to early-life emotional abuse and neglect had a negative impact on the performance in the emotional valences of RMET and multiple early-life adversities had a dose-dependent association with mental state decoding deficits ( [AUTHOR] et al., 2019 ). 4) When we studied these patients with a facial emotion recognition fMRI task then, we found that the maltreated patients had impaired accuracy to recognize facial emotions, especially sadness, and that they displayed altered functioning of key reward-related fronto-striatal circuits ( Nagy et al., 2021 ). We also have preliminary data on altered diffusion tensor imaging parameters of this cohort, data that we plan to publish later.


### 4.1. The long-term impact of adverse childhood experiences on brain architecture and function

A rapidly growing number of studies report that CM can alter trajectories of brain development and result in alterations in brain structure, function, connectivity, and network architecture of neural circuits critical for socio-cognitive functions, and by that, embed latent vulnerability to psychopathologies ( Lim et al., 2020 , Kraaijenvanger et al., 2020 , Pollok et al., 2022 , Li et al., 2023 , Oltean et al., 2023 , Yang et al., 2023 , Ireton et al., 2024 , Tomoda et al., 2024 ). Such developmental brain alterations contribute to the abnormal emotional regulation, reward processing, threat detection and response, interhemispheric integration, and sensory processing which are often present in maltreated individuals ( Samson et al., 2024 ). Most neuroimaging studies investigating the long-term impact of early life stress report on structural and functional alterations of brain areas involved in socio-affective functioning and stress regulation, whereas here we document that severely maltreated depressed patients display numerous alterations of intra- and inter-networks FC strengths, not only in their fronto-limbic circuits, but also in their sensory-motor, visual, auditory, and cerebellar networks. Notably, recent meta -analytic studies document that childhood adversities are associated with reduced gray matter volumes also in the cerebellum and sensory-motor areas ( Li et al., 2023 , Yang et al., 2023 ). Altogether, these findings may explain that individuals with a history of child abuse have deficits in perception of auditory and visual signals ( Pechtel and Pizzagalli, 2011 ), and in adulthood they may develop functional neurological (conversion) disorder ( Diez et al., 2021 ), a disabling condition, whereby the subjects exhibit sensorimotor symptoms incompatible with other neurological disorders ( Espay et al., 2018 ).


### 4.2. Intra-network FC alterations of the default mode network, visual network and cerebellum of depressed patients with a history of childhood maltreatment

In our present study, maltreated individuals had several alterations of FCs within the DMN, namely, we found increased FC in the left amygdala and hippocampus, and decreased FC in their right precuneus cortex compared to non-maltreated patients. The DMN plays a key role in internally oriented cognitive processes, including self-reflection, planning future events, or recalling the past, but it also has a decisive role in social interactions ( Yeshurun et al., 2021 ) and depressive rumination ( Hamilton et al., 2015 , Zhou et al., 2020 ). Not surprisingly, a great body of evidence implicate the involvement of the DMN in the pathophysiology of depressive disorders ( Greicius et al., 2007 , Sheline et al., 2009 , Whitfield-Gabrieli and Ford, 2012 , Whitfield-Gabrieli and Nieto-Castanon, 2012 , Guo et al., 2013 , Guo et al., 2014 , Yan et al., 2019 ). However, the findings of altered FC in the DMN of depressed patients are contradictory. Some studies document increased FC ( Greicius et al., 2007 ), while others report on both increased and decreased FC at the same time ( Zhu et al., 2012 , Guo et al., 2014 , Yan et al., 2019 ), similarly to our present findings. A likely explanation for these inconsistences is the fact that two spatially independent subnetworks are separated within the DMN: the anterior and posterior subnetworks ( Li et al., 2013 ), and these may react differently to stress. For example, Zhu and co-workers described an increased FC in the anterior regions and decreased FC in the posterior regions of first-episode, drug-naïve MDD patients ( Zhu et al., 2012 ). More recent investigations of MDD patients document abnormal − mainly increased −, resting state FC for all hippocampal subfields ( Hao et al., 2020 ), while another study found higher connectivity between the hippocampus and the anterior cingulate cortex ( Krug et al., 2022 ). In our case, the history of CM resulted increased FC in the amygdala and hippocampus, brain areas associated with the anterior subnetwork, and decreased FC in the precuneus cortex involved in the posterior subnetwork of the DMN. These findings suggest that childhood maltreatment may cause or augment the intra-network alterations of FCs in the DMN.

Plenty of neuroimaging studies document altered morphology, activity and connectivity of the hippocampus and amygdala as a long-term consequence of childhood maltreatment ( Woon and Hedges, 2008 , Opel et al., 2014 , Jedd et al., 2015 , Teicher et al., 2016 , Teicher and Samson, 2016 , McCrory et al., 2017 , Chen et al., 2024 , Nie et al., 2024 ). Specifically, in abused adolescents with symptoms of PTSD, which was related to childhood sexual abuse, increased FC was detected between the hippocampus and the middle temporal gyrus and lateral occipital cortex ( van Hoof et al., 2019 ). Aberrant FC of amygdala subregions has been reported in MDD patients with a history of childhood maltreatment ( Jedd et al., 2015 , Luo et al., 2022 , Luo et al., 2022 , Goltermann et al., 2023 ). A more recent study reported that abuse rather than neglect correlated with abnormal network functions in subregions of the right amygdala, and that FC alterations of the right amygdala also correlated with clinical features of the MDD patients, such as disease onset and treatment outcome ( Chen et al., 2024 ). Another study documented that extensive experiences of threat in childhood were associated with increased left amygdala connectivity with the precuneus ( Liuzzi et al., 2024 ).

Regarding the clinical findings related to the precuneus cortex, a recent mega-analytic comparison of data from a large multi-site cohort reported that individuals experiencing both childhood neglect and abuse had a lower cortical thickness in their precuneus cortex compared to individuals not exposed to CM ( Tozzi et al., 2020 ). Whereas another study investigating differences in network architecture between maltreated and non-maltreated individuals found that the precuneus cortex showed enhanced centrality within the network ( Teicher et al., 2014 ). More recently, increased dynamic FC between the left superior ventro-anterior thalamus and left precuneus has been reported ( Yu et al., 2024 ).

In the maltreated patients, we found decreased FC within several structures that are part of the visual network, and increased FC within the cerebellum, especially in the right cerebellum, and increased FC in several areas of the auditory network compared to non-maltreated depressed patients. These areas are responsible for brain functions which are not easily related to childhood maltreatment, but interestingly, a recent report also found decreased inter-network connectivity between the medial visual network and the auditory network, lateral visual network, sensorimotor and the anterior default mode network as well as between the occipital pole visual network and dorsal attention network in depressed patients with a history of child abuse ( Luo et al., 2022b ). The same study reported decreased inter-network connectivity between the auditory network and posterior default mode network and medial visual network ( Luo et al., 2022b ). These findings are in accordance with the concept that children who experience parental verbal abuse and witness domestic violence have altered development of their auditory and visual pathways which process and convey such aversive experiences ( Teicher and Samson, 2016 , Teicher et al., 2016 ).

We found increased intra-network FC in several cerebellar subareas. The cerebellum has traditionally been viewed as a brain area primarily involved in motor behavior, but more recent neuroanatomical data demonstrate that the posterior cerebellum, and especially the vermis, has bidirectional connections with fronto-cortical and limbic regions, which regulate cognitive, executive and emotional functions ( Middleton and Strick, 1997 , Middleton and Strick, 2001 ). Recent structural and functional neuroimaging studies highlight the fact that the cerebellum plays a significant role in the pathophysiology of psychiatric disorders ( Hoppenbrouwers et al., 2008 ). Accordingly, a meta -analytic study reported hypoactive cerebellum in depressed patients ( Fitzgerald et al., 2008 ), while another found reduced functional activity of the cerebellar vermis in individuals with a history of childhood maltreatment ( Teicher et al., 2003 ).

Overall, our present data support the notion that the long-term functional consequences of childhood maltreatment affect not only the well-known fronto-limbic circuits, but also other, less documented structures such as the auditory and visual networks, or the cerebellum.


### 4.3. Inter-network FC alterations of depressed patients with a history of childhood maltreatment

Analysis of inter-network differences of maltreated depressed patients compared with non-maltreated patients revealed that most of the networks that had intra-network FC alterations, had inter-network FC alterations as well. For example, the DMN had altered FC with the executive control and salience networks. Numerous studies reported on altered connectivity of the DMN in maltreated patients ( Rakesh et al., 2021 , Luo et al., 2022 , Wang et al., 2022 , Zhang et al., 2022 , Ireton et al., 2024 ). Interestingly, we found mixed, i.e., increased as well as reduced FC strengths between the executive control and default mode networks. Whereas the salience network had reduced FC with both the executive control and default mode networks, similarly with the findings described in non-clinical adults with moderate or severe childhood trauma ( Zhao et al., 2021 ). These three networks are tightly linked to each other and according to the unifying triple network model proposed by Menon, deficits in the engagement and disengagement of these three core neurocognitive networks play a significant role in numerous neuro-psychiatric disorders ( Menon, 2011 ). The executive control and default mode networks are regarded as opposing networks, as they participate in opposite functions, the executive control network is a task-dependent network that supports cognitively demanding tasks and involved in monitoring the external environment whereas, the DMN is responsible for internal awareness and self-referential processing. As recent theories suggest the interaction between these two networks are perturbed as a developmental consequence of childhood trauma and such disrupted interplay between these two networks underlie the cognitive deficits and clinical symptoms seen in many psychiatric disorders ( Allen et al., 2019 ).

We observed that several areas in the sensorimotor network had increased FC strengths with various other networks. This finding is in harmony with recent findings reporting increased inter-network connectivity of the sensorimotor network with other networks ( Luo et al., 2022b ). Another study documented that emotional abuse and neglect were strongly associated with increased network connectivity between the dorsal attention and sensorimotor networks ( Yu et al., 2019 ). We also found decreased FC between the visual and sensorimotor network and similar finding has been reported by Luo et al. (2022b) . A recent prospective study documented that girls exposed to mothers with depressive symptoms showed a slower development of FC between the language and sensorimotor networks ( Zhang et al., 2021 ). Furthermore, CM is associated with widespread white matter microstructural abnormalities of neural pathways linking fronto-limbic and occipital visual cortices ( Lim et al., 2020 ). These findings are in agreement with the concept that maltreatment alters the trajectories of brain development and influence the network connectivity of sensory systems ( Masten et al., 2008 , Teicher et al., 2016 , Teicher and Samson, 2016 ) and that maltreated individuals often display cognitive impairments ( Kavanaugh et al., 2017 , [AUTHOR] et al., 2019 , Su et al., 2019 ).

We found stronger connectivity between the anterior cingulate cortex and the bilateral superior parietal lobe in maltreated patients compared to the MDD group. A comparable finding to this result is recent meta -analytical evidence revealing negative associations between CTQ scores and brain activation to socio-affective cues in the left superior parietal lobule ( Heany et al., 2018 ).

The cerebellar network displayed altered FC with the sensorimotor (increased FC) and with the executive control (decreased FC) networks. Comparable finding has been reported by a recent longitudinal study demonstrating an altered development of cerebellar − sensorimotor connections in maltreated children ( Zhang et al., 2021 ). As discussed earlier current knowledge highlight the role of cerebellar networks in the pathophysiology of psychiatric disorders ( Hoppenbrouwers et al., 2008 ). A recent functional MRI study reported that maltreated women with depression had significantly greater stress-related connectivity between the cerebellum and medial prefrontal cortex ( Dong et al., 2022 ). Complementing these functional data structural studies reveal that childhood adversities are associated with gray matter volume alterations of various fronto-limbic structures, as well as sensory-motor and cerebellar areas ( Li et al., 2023 , Yang et al., 2023 ).

In summary, we found numerous differences in functional brain architecture between the maltreated and non-maltreated depressed patients and these findings are supported by growing body of recent evidences (e.g. Xu et al., 2019 , Yu et al., 2019 , He et al., 2022 , Wu et al., 2021 , Zhang et al., 2021 , Dong et al., 2022 , Luo et al., 2022 , Luo et al., 2022 , Luo et al., 2022 , Luo et al., 2022 , Wang et al., 2022 , Wang et al., 2022 , Fan et al., 2023 , Goltermann et al., 2023 , Rong et al., 2023 , Gruzman et al., 2024 , Liu et al., 2024 ). Clinical evidence demonstrates that depressed patients with a history of maltreatment are more likely to develop a more severe, early-onset, treatment-resistant depression with chronic disease trajectory ( Nanni et al., 2012 , Nelson et al., 2017 , Opel et al., 2019 ). Together these data support the concept that maltreated individuals form a distinct subgroup among depressed patients with a more malignant clinical course and should be treated differently ( Nemeroff, 2016 , Lippard and Nemeroff, 2020 , Tomoda et al., 2024 ).


### 4.4. Limitations

This study, as any investigations, has limitations that should be kept in mind when interpreting the results. Major limitations were the relatively low sample size and the cross-sectional study design. Another limiting factor was the use of a retrospective self-report questionnaire to assess their adverse childhood experiences. This may be a confounding factor as previous studies demonstrate that the congruence between retrospective and prospective assessment of CM can be poor or modest ( Reuben et al., 2016 , Baldwin et al., 2019 ). In contrast to that, a more recent finding suggests that such retrospective self-reports are in fact highly reliable ( Goltermann et al., 2023a ). To control for the subjectivity of the retrospective self-reports a senior author conducted a structured interview with all participants, focusing on childhood adversities, to reveal any inconsistencies. Possible influencing effect of current depressive symptoms on the subjective evaluation of past experiences was also considered. However, we found no correlation between depression severity and total CTQ scores, or depression severity compared with scores of any CTQ subscales.

Another limitation was that we did not include a healthy control group with childhood maltreatment. Our control subjects were also meticulously screened for any clinical symptoms. Originally, we wanted to include a control group with CM, but during the recruitment period, we could identify only 4 individuals without any psychopathology, but reporting at least a moderate level of childhood maltreatment. As we could not increase the subject number of this group, therefore, these individuals were not involved in this study.

Finally, we could not control the effect of antidepressant medication. The majority of our clinical MDD sample (97 %) was medicated and took antidepressants from various classes. Therefore, it was not possible to form homogeneous medication groups for further analysis.


### 4.5. Conclusions

Our present data provide further convincing evidence that childhood maltreatment not only alters the development of the fronto-limbic circuitry which regulates emotions, but also disrupts functional connectivity of major sensorimotor and cerebellar networks. These alterations may explain the fact that maltreated individuals perceive external and internal cues differently, and that their reactions are also often abnormal. Our findings are in harmony with recent ideas emphasizing that childhood trauma may disrupt the functioning of three core neurocognitive networks, the default mode, executive control, and salience networks, and that perturbed interactions between these networks represent a potential underlying mechanism for the cognitive deficits and clinical symptoms seen in many psychiatric disorders. Our data also demonstrate that maltreated depressed patients have more severe disturbances in their brain architecture, as a consequence of early life trauma, and that such individuals represent a distinct sub-group among MDD patients.


## Funding

This research was founded by the Hungarian Brain Research Program 3 (NAP-3), and by the TKP2021-EGA-16 project. Project TKP2021-EGA-16 has been implemented with the support provided from the National Research, Development and Innovation Fund of Hungary, financed under the TKP2021-EGA funding scheme.” S.A.N. was supported by the János Bolyai Research Scholarship of the Hungarian Academy of Sciences.


## CRediT authorship contribution statement

Mónika [AUTHOR]: Writing – original draft, Visualization, Formal analysis, Data curation. Szilvia [AUTHOR] Nagy: Writing – review & editing, Writing – original draft, Visualization, Supervision, Resources, Project administration, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. Gergely Orsi: Writing – review & editing, Supervision, Methodology, Formal analysis. Gábor [AUTHOR]: Writing – review & editing, Supervision, Methodology, Formal analysis. Maria [AUTHOR]: Writing – review & editing, Supervision, Resources, Investigation, Formal analysis, Data curation, Conceptualization. Boldizsár Czéh: Conceptualization, Funding acquisition, Project administration, Supervision, Writing - Original Draft, Writing - Review & Editing.


## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.


## Acknowledgments

We are grateful to Nándor Németh, Eszter Csernela, Flóra Elza Lakner for performing the psychological evaluation of the subjects involved in this study.


## Footnotes

Supplementary data to this article can be found online at https://doi.org/[REDACTED_DOI] .


## Appendix A. Supplementary data

The following are the Supplementary data to this article:


## Data availability

Data will be made available on request.

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials


### Data Availability Statement

Data will be made available on request.
