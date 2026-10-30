# De-Identified Manuscript `OOD_ANON_06`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Accumulating evidence has revealed deviations in neural network connectivity among individuals with suicidal ideation (SI). We sought to explore the neural network dynamics of suicide attempt (SA) survivors. We recruited 31 SA survivors, 33 individuals with SI, and 33 normal people controls (NP). To investigate brain network dynamics, we collected 64-channel resting-state EEG recordings and conducted microstate analysis on all participants. Compared to the NP group, both SA survivors and SI group displayed greater coverage and occurrence of microstates A and B. Notably, relative to the SI group, a marked elevation in the occurrence of microstates D and E and a significant increased coverage of microstate E, were observed in the SA group. The SA group exhibited significantly shorter durations of microstates C, D, and E, along with reduced occurrence and coverage of microstate C, compared to the SI group. The SA group exhibited significantly greater transition probabilities from microstate E to any other microstate compared to the SI group. Furthermore, higher suicide risk scores significantly correlated increased occurrence of microstate D, occurrence of microstate E, and coverage of microstate E. A key limitation is the cross-sectional design, which restricts the capacity to establish whether microstate dynamics can serve as predictors of future suicidal behavior. The present results imply that the microstate dynamics of SA survivors are distinct from those of individuals with SI. These results indicate that microstate dynamics could potentially act as neurobiomarkers for distinguishing suicidal behavior and SI.

Keywords: Suicide attempt survivors, EEG microstate, Large-scale brain network


## Introduction

Suicide is a critical global public health concern. According to WHO reports, suicide causes 1 in 100 deaths globally (9/100,000), with China’s rate at 6.7/100,000 (WHO, 2021 ). China has experienced a significant reduction in national suicide mortality during the last twenty years, contrasting with concerning increases among urban adolescent populations (Hu et al. 2024 ). Consequently, identifying risk factors for suicide at an early stage is crucial for predicting and preventing suicidal behavior. Nevertheless, progress has been hampered by limitations in existing diagnostic tools. Current clinical assessments rely primarily on patient self-reports and scale-based screenings which are characterized by high subjectivity and low specificity. Consequently, the risk stratification (i.e., high- vs. low-risk) derived from them has limited power in predicting an individual’s long-term suicide risk, making it difficult to achieve accurate identification before the behavior occurs (Woodford et al. 2017 ). Meanwhile, the pathophysiological mechanisms underlying suicidal behavior remain poorly understood. Although neurobiological factors such as prefrontal cortex dysfunction and impaired emotion-regulation circuitry have been associated with suicide risk (Lippard et al., 2014 ), these findings largely represent nonspecific associations. Such limitations impede accurate prediction and effective prevention efforts.

Extensive investigation across clinical, psychological, and social domains has yet to yield measurable improvements in suicide risk prediction over the past half-century (Franklin et al. 2017 ; May and Klonsky 2016 ). This persistent limitation suggests critical deficiencies in existing theoretical frameworks of suicide risk assessment. Investigating determinants that mediate the transition from suicidal ideation to enacted behavior represents a fundamental research priority in suicide prevention research. Empirical studies demonstrate that most individuals experiencing suicide ideas do not subsequently engage in suicide attempts (Klonsky et al. 2016 ).

Neurocognitive features are posited to provide critical insights into the mechanisms underlying the transition from suicidal ideation to action. This is because neurocognitive abilities, such as executive function, cognitive control, and future planning, constitute the very machinery that governs the translation of internal state into goal-directed behavior (Bredemeier and Miller 2015 ). In the context of suicide, specific impairments in these domains may directly facilitate this critical shift. For instance: maladaptive decision-making (e.g., heightened impulsivity) may predispose individuals to choose a drastic, immediate solution (a suicidal act) over alternative courses of action, driven by an overvaluation of immediate negative reinforcement (escape from pain) and a devaluation of long-term consequences (Dombrovski et al., 2017 ).Deficits in emotion regulation may compromise the ability to modulate intense negative affect (such as perceived burdensomeness, thwarted belongingness, hopelessness or feeling of defeat, pessimism, self-inefficacy, and self-blame), thereby increasing the likelihood that such emotional states culminate in suicidal behavior as a maladaptive coping strategy (Colmenero-Navarrete et al. 2022 ; Guyonne et al. 2024 ). Therefore, elucidating these neurocognitive characteristics can help explore the transition from suicidal ideation to behavior.

Empirical evidence has delineated a range of neurocognitive deficits associated with suicidal behavior. For instance, suicide attempt survivors exhibit significantly poorer performance in attention control and working memory compared to non-attempters with depression, with particularly pronounced executive dysfunction observed among those who used violent means (Keilp et al. 2012 , 2014 ). Furthermore, impairments in executive function, affective shifting task, planning, and risk decision-making have been consistently reported in this population (Silva et al. 2018 ; Westheide et al. 2008 ; Ho et al. 2018 ; Moraes, 2013 ; Baek et al. 2017 ; Jollant et al. 2011 ). While these findings robustly associate cognitive deficits with suicidal acts, they primarily rely on traditional neuropsychological tasks that measure behavioral outcomes over extended periods (seconds to minutes). As such, they fail to capture the rapid, dynamic brain state transitions underlying critical cognitive operations, leaving it unclear whether suicidal behavior stems from a specific, transient neurocognitive state or a general, persistent deficit. Consequently, the field lacks a temporally precise model to explain how impaired cognitive processes moment-by-moment facilitate the transition from suicidal ideation to action.

To address this gap, the present study turns to EEG microstate analysis—a method uniquely suited to capturing the millisecond-scale dynamics of large-scale neural networks. Resting-state networks, which integrate distributed neuronal assemblies into functional units, are fundamental to supporting complex cognition (Bressler 1995 ; Bressler and Tognoli 2006 ). EEG microstates offer a window into these systems by quantifying transient, quasi-stable scalp potential topographies that typically persist for 80–120 milliseconds, serving as electrophysiological markers of rapid network reconfigurations (Khanna et al. 2015 ). A key advantage of microstate analysis over other neuroimaging techniques such as fMRI is its superior temporal resolution, which is essential for characterizing the spontaneous brain dynamics that underlie resting-state cognition (Khanna et al. 2015 ; Michel and Koenig 2018 ). Moreover, canonical microstate patterns have been reliably linked to specific resting-state networks and are recognized as clinically meaningful indicators of brain disorders and cognitive dysfunction (Britz et al. 2010 ; Michel and Koenig 2018 ).

Despite this potential, microstate studies in suicidal populations remain limited. Emerging evidence suggests that individuals with suicidal ideation exhibit distinct alterations—such as reduced occurrence and coverage of microstate B alongside increased metrics in microstate A—relative to non-SI controls (He et al. 2024 ). Similarly, while examining adolescent groups, those with pure major depressive disorder demonstrated elevated microstate A metrics, both occurrence and duration, compared to both healthy adolescents and non-suicidal self-injury engaged depressed teens (J.-h. Hu et al. 2023a , b ). However, no study to date has used microstate analysis to directly compare suicide attempt survivors with those experiencing SI only.

To gain deeper insights into brain neurocognitive characteristics in the context of suicidal behavior, we employed EEG microstates to explore the activity patterns of large-scale neural systems of SA survivors. We hypothesize that the suicide may involve disruptions in the dynamic equilibrium of large-scale brain networks and abnormal activation of specific neural states, which could involve: (1) heightened engagement of perceptual networks, as suggested by potential enhancements in auditory and visual processing (reflected in microstates A and B), possibly leading to amplified sensitivity to negative stimuli and increased emotional load (He et al. 2024 ); (2) increased persistence of self-referential processing, potentially associated with sustained activity in the anterior default mode network (microstate C), which may contribute to repetitive negative thinking patterns underlying suicidal ideation (Greicius et al., 2007 ; (Chase et al. 2015 ; Zhang et al. 2024 ); and (3) altered interplay between attention and salience networks, where increased dynamics between the dorsal attention network (microstate D) and the salience network (microstate E) could facilitate heightened vigilance to threat and a propensity for impulsive responses (Dombrovski et al., 2017 ; Ho et al. 2021 ).The rapid reconfiguration and stable-state imbalance of these networks over time—manifested as alterations in the duration, occurrence, and coverage of specific microstates—may collectively constitute the dynamic neural basis for the transition from suicidal ideation to suicidal action, making individuals more likely to cross cognitive control boundaries and enact suicidal behaviors at critical moments.


## Methods


### Participants

Volunteers between the ages of 18 and 35 invited to volunteer through advertisements in medical institutions and the community. Psychiatric diagnoses were established through structured clinical interviews adhering to the diagnostic criteria specified in the diagnostic and statistical manual of mental disorders (DSM). The study employed the following exclusion criteria: dependence on psychoactive substances or nonpsychoactive substances; a history of brain diseases, head injuries, abnormal EEGs, or MRI evidence of structural brain anomalies; the presence of hallucinations, delusions, significant agitation, psychomotor retardation, or anxiety symptoms; and engagement in non-suicidal self-injury. Eligible participants were either free from concomitant medication or had completed a washout period of at least five drug half-lives prior to enrollment. Participants were stratified into three groups according to self-reported evaluations on the Suicidal Behaviors Questionnaire–Revised (SBQ-R; Osman et al. 2001 ) and clinical assessments by psychosomatic physicians: SA survivors, individuals with SI, and normal controls.

Participants were stratified into three distinct groups according to self-reported measures using the SBQ-R and diagnoses by psychosomatic physicians: SA survivors, individuals with SI, and normal controls. The sample size of this study was determined based on practical considerations and the sample sizes commonly reported in the existing EEG microstate literature. Our final cohort of 97 participants is comparable to or larger than those most previous studies (Schiller et al. 2024 ), thereby supporting its adequacy for the current investigation. The experimental groups were well-matched on demographic variables, showing equivalent gender ratios and age ranges. The general features of the study cohorts are summarized in Table 1 .


#### Table 1.

Demographic data for the three groups



|  | SA ( n 1 = 31) | SI ( n 2 = 33) | NP ( n 3 = 33) | F/χ 2 | p |
| --- | --- | --- | --- | --- | --- |
| Mean/ N | SD/% | Mean/ N | SD/% | Mean/ N | SD/% |
| Age | 25.45 | 5.41 | 25.97 | 5.93 | 23.84 | 4.99 | 1.35 | 0.26 |
| Gender |  |  |  |  |  |  | 1.02 | 0.60 |
| Male | 18 | 58.06 | 15 | 45.45 | 17 | 51.52 |  |  |
| Female | 13 | 41.94 | 18 | 54.56 | 16 | 48.48 |  |  |
| Marriage |  |  |  |  |  |  | 2.35 | 0.50 |
| Unmarried | 22 | 70.97 | 19 | 21.21 | 24 | 6.06 |  |  |
| First marriage | 8 | 25.81 | 12 | 66.67 | 9 | 81.82 |  |  |
| Others | 1 | 3.23 | 2 | 12.12 | / | 12.12 |  |  |
| Education |  |  |  |  |  |  | 5.23 | 0.27 |
| Middle school | 6 | 19.35 | 7 | 21.21 | 2 | 6.06 |  |  |
| Undergraduate | 24 | 77.42 | 22 | 66.67 | 27 | 81.82 |  |  |
| Graduate | 1 | 3.25 | 4 | 12.12 | 4 | 12.12 |  |  |
| Mental disorder diagnosis |  |  |  |  |  |  | 12.84 4.05 Δ | 0.05 0.26 Δ |
| None | 19 | 61.29 | 17 | 51.52 | 27 | 81.82 |  |  |
| Depression | 12 | 38.71 | 12 | 36.36 | 6 | 18.18 |  |  |
| Anxiety disorder | / | / | 2 | 6.06 | / | / |  |  |
| Bipolar disorder | / | / | 2 | 6.06 | / | / |  |  |


Δ Only the SA group and the SI group were compared.

This study was approved by the Ethical Committee of Xijing Hospital (Approval No. KY20212203-F-1) and was formally registered with the Chinese Clinical Trials Registry (Registration No. ChiCTR2200061682). Each participant gave written informed consent and was compensated with 50 RMB after completing the experimental task.


### Psychological Assessment


#### Suicidal Behaviors Questionnaire–Revised (SBQ-R)

The SBQ-R (Osman et al. 2001 ) was utilized to evaluate suicide risk in this study. The SBQ-R questionnaire comprises four items, with composite scores calculated by summing responses across all scale items, yielding a continuous risk scale ranging from 3 to 18 points. A score of 7 has been verified as a threshold for distinguishing between low-risk and high-risk individuals in clinical and nonclinical samples. A score ≥ 7 indicates the risk of suicide, with higher scores on the scale corresponding to a greater risk of suicidal behaviors. This scale has demonstrated good reliability (0.75), validity (0.76) and internal consistency (0.83) (Dixon-Gordon et al. 2022 ; Osman et al. 2001 ).


#### Beck Depression Inventory II (BDI-II)

The BDI-II was used to evaluate the depressive status of the participants (Beck 1961 ). The BDI-II comprises 21 item sets, each containing four statements. Respondents select the statement that best reflects their condition over the past two weeks. Higher scores indicate more severe depression. This tool has been shown to exhibit good reliability (0.92) (Storch et al. 2004 ).


### EEG Data Acquisition

Participants remained seated in a relaxed position throughout the experiment, which was conducted in a standardized EEG recording environment with controlled lighting and noise levels. Participants completed a 3-minute visual fixation task, maintaining gaze on a centrally presented cross stimulus against a black background while remaining alert with eyes open. Continuous electrophysiological recordings were acquired from 64 scalp sites using a Neuroscan Quik-Cap, with standardized 10–20 system electrode placement ensuring consistent spatial sampling across participants. M1 and M2 were used as reference electrodes, with data recorded in DC mode at a frequency of 1000 Hz. Data collection commenced only after all electrode-scalp contact impedances were verified to be below 5 kΩ, in accordance with standard electrophysiological recording protocols.


### EEG Data Preprocessing and Analysis

For preprocessing, we utilized the MATLAB 2022b and EEGLAB (version 2023.0) toolboxes. First, we removed unused channels (HEO, VEO and TRIGGER). EEG data were processed with a 1–40 Hz bandpass filter prior to analysis. Third, artifact-contaminated epochs were manually identified and excluded, while channels exhibiting persistent artifacts were interpolated. Following this, independent component analysis (ICA) was subsequently performed to isolate and remove artifactual components corresponding to ocular (blinks and saccades) and myogenic activity. Once these steps were finalized, the data were ready for microstate analysis.

Microstates were derived using the standardized steps (Poulsen et al. 2018 ). First, a group-level template was constructed by aggregating 1,000 global field power (GFP) peaks randomly selected from each participant’s EEG recording. Second, the template was classified into representative microstates using a k-means clustering algorithm. Third, considering the stability of the data, five typical microstates were selected (Kleinert et al. 2023 ). Fourth, the EEG data of each participant was backfitted based on the template microstates, and microstate labels lasting less than 30ms were temporally smoothed. Finally, quantitative microstate parameters, including mean duration, occurrence, temporal coverage, and inter-state transition probabilities, were computed for each participant. The final analytical sample comprised 97 participants distributed across three groups: suicide attempt survivors (SA, n = 31), individuals with suicidal ideation (SI, n = 33), and normal people controls (NP, n = 33).


### Statistical Analyses

All quantitative analyses were conducted using IBM SPSS Statistics (version 19.0). Intergroup differences in demographic characteristics, clinical measures, and microstate dynamics (duration, occurrence, coverage, and transition probabilities) were assessed using one-way analysis of variance (ANOVA). For all ANOVAs, post-hoc pairwise comparisons were performed using the Bonferroni correction to control for Type I error. The threshold for statistical significance was set at p < 0.05. Effect sizes for post-hoc tests were reported using Cohen’s d, with values of 0.2, 0.5, and 0.8 interpreted as small, medium, and large effects, respectively. Correlation analysis was used to explore the relationships between suicide risk, depression levels, and microstate dynamics.


## Results

As illustrated in Fig. 1 , five characteristic microstate topographies were identified, matching established patterns reported in prior research (Kleinert et al. 2023 ; Michel and Koenig 2018 ; Férat et al. 2022 ). All participant groups exhibited equivalent global explained variance (GEV) percentages (Group SA: 0.71; Group SI: 0.72; Group NP: 0.70), indicating consistent microstate segmentation quality.


### Fig. 1.


> **Figure/Table Caption:** The five electroencephalographic microstates in the three groups. SA: suicide attempt survivors, SI: individuals with suicidal ideation, NP: normal controls


### Microstate Duration, Occurrence, and Coverage

One-way ANOVAs with Bonferroni post hoc tests revealed distinct patterns in microstate dynamics across the three groups (SI, SA, and NP), as summarized in Table 2 ; Fig. 2 . Overall, the SI group was characterized by prolonged durations of microstates C, D, E and greater occurrence of microstate C compared to the SA group, with particularly strong effects for microstate D (Cohen’s d = 1.48). In contrast, the SA group showed higher occurrence rates of microstates D and E, along with greater coverage of microstate E, suggesting a more active and sustained involvement of these states. Meanwhile, the NP group consistently exhibited reduced occurrence and coverage of microstates A and B relative to both the SA and SI groups, pointing to a possible attenuation of these microstates in this population. These patterns highlight distinct neural dynamics among the groups, with SI showing prolonged state duration, SA exhibiting higher occurrence and coverage of specific states, and NP displaying a general reduction in microstates A and B.


#### Table 2.

Comparison of the EEG microstate dynamics among the three groups



|  | SA Mean (SEM) | SI Mean (SEM) | NP Mean (SEM) | F value | P value | Post hoc comparisons |
| --- | --- | --- | --- | --- | --- | --- |
| Duration |  |  |  |  |  |  |
| A | 58.89(1.17) | 59.73(1.51) | 67.38(4.42) | 2.75 | 0.07 |  |
| B | 60.42(1.51) | 57.66(1.28) | 56.81(1.22) | 1.97 | 0.15 |  |
| C | 60.62(1.92) | 68.67(2.63) | 61.40(2.09) | 3.94 | 0.02 | SI> SA/NP |
| D | 61.56(1.69) | 155.52(15.35) | 126.65(11.72) | 17.44 | <0.01 | SI> NP> SA |
| E | 55.85(0.99) | 74.27(5.72) | 57.79(1.28) | 8.41 | <0.01 | SI> SA/NP |
| Occurrence |  |  |  |  |  |  |
| A | 2.37(0.11) | 2.32(0.10) | 0.94(0.12) | 56.54 | <0.01 | SA/SI> NP |
| B | 2.57(0.11) | 2.56(0.14) | 2.25(0.09) | 2.43 | 0.09 | SA/SI> NP |
| C | 2.44(0.09) | 2.89(0.14) | 2.72(0.12) | 3.60 | 0.03 | SI/NP> SA |
| D | 2.71(0.10) | 0.84(0.11) | 0.92(0.18) | 60.50 | <0.01 | SA> SI/NP |
| E | 2.46(0.10) | 0.81(0.10) | 2.42(0.09) | 94.38 | <0.01 | SA/NP> SI |
| Coverage |  |  |  |  |  |  |
| A | 13.88(0.62) | 13.79(0.63) | 7.44(1.02) | 22.31 | <0.01 | SA/SI> NP |
| B | 15.68(0.91) | 14.88(0.95) | 12.62(0.47) | 3.92 | 0.02 | SA/SI> NP |
| C | 14.98(0.92) | 20.25(1.52) | 16.84(1.11) | 4.78 | 0.01 | SI> SA/NP |
| D | 16.80(0.90) | 16.47(2.64) | 13.21(2.34) | 0.86 | 0.42 |  |
| E | 13.67(0.56) | 7.43(1.17) | 13.79(0.50) | 20.24 | <0.01 | SA/NP> SI |


SEM: Std. Error of the mean.


#### Fig. 2.


> **Figure/Table Caption:** Group differences in microstate temporal dynamics: duration, occurrence, and coverage. ( A ) Microstate duration dynamics across three groups (SA, SI, and NP). ( B ) Microstate occurrence across three groups (SA, SI, and NP). ( C ) Microstate coverage across three groups (SA, SI, and NP). * p < 0.05. ** p < 0.01. n.s. Not significant


### Microstate Transition Probabilities

Transition probabilities between microstates for all three groups are presented in Table 3 . In most instances, the SA group exhibited significantly higher transition probabilities than the SI group, particularly for transitions from microstates A, B, and C to microstates D and E. In contrast, the SI group showed significantly greater transition probabilities than the SA group when shifting from microstates A, B, and C to microstates B, C, and A. Moreover, the SA group had a significantly higher probability of transitioning from microstate E to any other microstate compared to the SI group.


#### Table 3.

Comparison of the transition probabilities among the three groups



|  | SA Mean (SEM) | SI Mean (SEM) | NP Mean (SEM) | F value | P value | Post hoc comparisons |
| --- | --- | --- | --- | --- | --- | --- |
| A to B | 2.55(0.11) | 3.12(0.17) | 1.02(0.14) | 60.43 | <0.01 | SI> SA> NP |
| A to C | 2.53(0.13) | 4.14(0.25) | 1.01(0.13) | 74.85 | <0.01 | SI> SA> NP |
| A to D | 2.81(0.14) | 1.47(0.25) | 1.03(0.20) | 20.21 | <0.01 | SA> SI/NP |
| A to E | 3.07(0.17) | 1.06(0.16) | 1.39(0.19) | 36.15 | <0.01 | SA> SI/NP |
| B to A | 2.55(0.11) | 3.12(0.17) | 1.02(0.14) | 60.43 | <0.01 | SI> SA> NP |
| B to C | 2.53(0.13) | 4.14(0.25) | 1.01(0.13) | 74.85 | <0.01 | SI> SA> NP |
| B to D | 2.81(0.14) | 1.47(0.25) | 1.03(0.20) | 20.21 | <0.01 | SA> SI/NP |
| B to E | 3.06(0.17) | 1.06(0.16) | 1.39(0.19) | 36.15 | <0.01 | SA> SI/NP |
| C to A | 2.57(0.13) | 2.98(0.16) | 1.09(0.14) | 48.76 | <0.01 | SI> SA> NP |
| C to B | 3.00(0.25) | 5.21(0.48) | 3.19(0.18) | 13.61 | <0.01 | SI> SA/NP |
| C to D | 3.68(0.26) | 0.85(0.17) | 1.01(0.18) | 59.48 | <0.01 | SA> SI/NP |
| C to E | 3.21(0.24) | 0.79(0.10) | 2.88(0.15) | 61.68 | <0.01 | SA/NP> SI |
| D to A | 2.50(0.11) | 4.06(0.27) | 0.97(0.12) | 70.27 | <0.01 | SI> SA> NP |
| D to B | 2.96(0.28) | 5.19(0.47) | 3.21(0.18) | 13.34 | <0.01 | SI> SA/NP |
| D to C | 3.18(0.22) | 1.43(0.49) | 1.20(0.32) | 8.52 | <0.01 | SA> SI/NP |
| D to E | 2.35(0.09) | 1.04(0.13) | 3.49(0.18) | 77.42 | <0.01 | NP> SA> SI |
| E to A | 2.91(0.15) | 1.63(0.28) | 0.98(0.18) | 20.46 | <0.01 | SA> SI> NP |
| E to B | 3.78(0.27) | 0.84(0.21) | 1.04(0.20) | 52.38 | <0.01 | SA> SI/NP |
| E to C | 3.17(0.21) | 1.48(0.46) | 1.13(0.31) | 9.65 | <0.01 | SA> SI/NP |
| E to D | 2.98(0.15) | 0.93(0.19) | 0.94(0.19) | 43.21 | <0.01 | SA> SI/NP |


SEM: Std. Error of the mean.


### Regression Analysis between Microstate Dynamics and Clinical Measures

As detailed in Table 4 , significant differences in suicide risk and depression levels were observed across the three groups (F = 27.28, p < 0.01; F = 35.65, p < 0.01). Crucially, depression severity did not differ significantly between the SA and SI groups ( p = 0.37), allowing for a focused investigation into the association between microstate dynamics and suicide risk across the suicide risk spectrum (only SA and SI groups combined).


#### Table 4.

Comparison of the behavior results among the three groups



|  | SA | SI | NP | F | p |
| --- | --- | --- | --- | --- | --- |
| Suicide risk | 13.45 ± 4.40 | 9.00 ± 3.36 | 5.97 ± 4.40 | 27.28 | < 0.01 |
| Depression level | 24.90 ± 12.18 | 20.61 ± 9.91 | 5.12 ± 7.19 | 35.65 | < 0.01 |


Bivariate correlations were computed between of the parameters of these three microstate dynamics and individual suicide risk scores among the SA and SI groups. As illustrated in Fig. 3 , significant negative correlations emerged between suicide risk and temporal characteristics of microstates C, D, and E. Notably, our analysis revealed statistically significant inverse associations between individuals’ suicide risk scores and the duration of microstate D ( p < 0.01 F ( x )= −0.02 x + 13.62, adjusted R 2 = 14.4%), as well as microstate E duration ( p < 0.05 F ( x )= −0.05 x + 14.54, adjusted R 2 = 7.3%). However, positive correlations were identified between suicide risk scores and the occurrence of microstate D ( p < 0.01 F ( x ) = 1.64 x + 8.29, adjusted R 2 = 15.7%), microstate E occurrence ( p < 0.01 F ( x ) = 2.22 x + 7.59, adjusted R 2 = 23.6%), and microstate E coverage ( p < 0.05 F ( x ) = 0.22 x + 8.84, adjusted R 2 = 7.8%).


#### Fig. 3.


> **Figure/Table Caption:** Correlation between microstate dynamics and suicide risk scores (suicide attempt survivors and suicidal ideation only, n = 64). Scatterplots showing the associations between ( A ) suicide risk score and microstate D mean duration, ( B ) suicide risk score and microstate E mean duration, ( C ) suicide risk score and microstate D mean occurrence, ( D ) suicide risk score and microstate E mean occurrence, ( E ) suicide risk score and microstate E mean coverage. All the univariate regressions are significant


## Discussion

Microstate analysis was implemented to investigate potential disparities in large-scale neural network dynamics across three groups. Our results revealed a significant elevation in both the occurrence and coverage of microstates A and B among SA and SI groups relative to the NP group. Moreover, the occurrence of microstates D and E, as well as the coverage of microstate E, were significantly higher in the SA group relative to the SI group. Comparative analyses revealed that relative to the SI group, the SA group demonstrated significantly abbreviated durations of microstates C, D, and E, coupled with diminished occurrence and coverage specifically for microstate C. Notably, the SA group demonstrated significantly higher transition probabilities compared to the SI group, particularly for shifts from microstates A, B, and C to microstates D and E. In contrast, the SI group showed notably higher transition probabilities compared to the SA group when transiting from microstates A, B, and C to microstates B, C, and A. Additionally, the SA group exhibited significantly higher transition probabilities from microstate E to other microstates relative to the SI group. Furthermore, suicide risk scores demonstrated significant inverse correlations with the durations of both microstates D and E. However, suicide risk scores exhibited significant positive correlations with microstate D occurrence, microstate E occurrence, and microstate E coverage. The present results demonstrate the potential utility of resting-state EEG microstate patterns as objective neural markers for suicide risk assessment.

Our analysis revealed significantly increased occurrence rates of microstate A in both SA and SI groups relative to NP group. Microstate A has been neuroanatomically linked to activation in bilateral superior and middle temporal gyri, core components of the auditory processing network (Michel and Koenig 2018 ). Prior research has demonstrated a significant association between increased microstate A occurrence and depressive symptom severity (Damborská et al. 2019 ). Recent research demonstrated significantly elevated occurrence and coverage of microstate A in major depressive disorder(MDD) patients with suicidal ideation relative to those with major depressive disorder but without SI or healthy individuals (He et al. 2024 ). This finding aligns with established evidence demonstrating higher rates of suicidal ideation among patients experiencing auditory hallucinations, implying a potential causal relationship between hallucinatory experiences and elevated suicide risk (Yin et al. 2023 ). Complementary research has demonstrated increased prevalence of suicidal ideation among children and adolescents with hallucination experiences (Duffy et al. 2019 ). Despite the absence of reported auditory hallucinations in our SA and SI groups, the increased prevalence of microstate A implies that subtle auditory network dysregulation could function as an alternative neural correlate of suicide risk.

The analysis revealed significantly increased occurrence and coverage of microstate B in the SA and SI groups relative to the NP group. Microstate B has been consistently linked to neural activity in the bilateral occipital cortex, a core region of the visual processing network (Britz et al. 2010 ; Custo et al. 2017 ). Previous research has documented alterations in visual processing among depressed patients with varying intensities of suicidal thoughts(Xie et al. 2018 ). Another study demonstrated significantly elevated occurrence and coverage of microstate B in depressed individuals Zhao et al. 2022 ). Recent findings suggest that suicidal ideation in MDD patients may be associated with unique visual processing deficits not present in MDD patients without SI (He et al. 2024 ). Microstate B has been implicated in visual network activity supporting both self-reflection and autobiographical memory functions (Tarailis et al. 2023 ). Evidence suggests that autobiographical memory disturbances, present across depressed patients and healthy controls, may predispose MDD patients to suicidal ideation (Jiang et al. 2020 ). Neural activation patterns during emotional autobiographical memory retrieval differed significantly between depressed patients with SI and those without SI (Zheng et al., 2023 ). A previous study revealed elevated microstate B occurrence and coverage in depressed patients with SI relative to depressed patients without SI (He et al. 2024 ). The above results provide insight into the greater occurrence and coverage of microstate B in the SA group and SI group in our research.

Our analysis revealed that microstate C demonstrated prolonged duration, increased occurrence, and expanded coverage in the SI group relative to the SA group. Microstate C has been neuroanatomically mapped to anterior default mode network regions, which mediate self-referential cognitive processes (Michel and Koenig 2018 ). Recent neuroimaging research identified that suicide rest-state neural alterations form a distributed network encompassing key default mode regions, particularly involving the orbitofrontal cortex and medial cingulate cortex (Zhang et al. 2024 ).Another study also demonstrated a significant positive association between subjective life satisfaction ratings and gray matter volume in multiple core regions of the default network (Kong et al. 2015 ).A resting-state brain imaging study revealed that spontaneous brain activity in the left dorsolateral prefrontal cortex and bilateral orbitofrontal cortex in the anterior region of the default network was directly proportional to the overall happiness score of the individual (Yang et al. 2011 ).Although the happiness index of SA survivors was not directly measured in this study, it was inferred from the parameters of microstate C that the decrease in their potential happiness may be an important factor affecting their suicidal behavior.

Our study revealed that the SA group exhibited more extensive microstate D coverage compared to the SI group. Microstate D has been consistently associated with activation in the dorsal attention network, which mediates fundamental attentional functions such as reflexive focusing, attention switching, and reorientation that occur with higher frequency during rest than during concentrated task performance (Michel and Koenig 2018 ). One study revealed greater microstate D frequency in adults with attention-deficit/hyperactivity disorder than in control subjects (Férat et al., 2022 ). Research has demonstrated that increased microstate D predominance correlates with transient stimulus unresponsiveness characteristic of early drowsiness onset (Comsa et al. 2018 ). A growing corpus of evidence over the past two decades has established that decision-making deficits are among the most prevalent trait-like characteristics in individuals with a history of SAs (Dombrovski and Hallquist 2017 ; Jollant et al. 2011 ) based on their behavioral performance in decision-making paradigms, particularly the Iowa Gambling Task. However, clues about gain and loss in the IGT are not apparent, thus requiring the subjects to use various cognitive processing strategies to complete the risk decision-making task (Dougherty et al., 2004 ). Our findings provide important insights into why individuals in the SA group perform poorly on such decision-making tasks.

Our results revealed significantly greater occurrence and coverage of microstate E in SA group compared to SI group, accompanied by enhanced transition probabilities from microstate E to any other microstate in the SA group. Microstate E is tied to both interoceptive processing and emotional information integration, primarily through its association with the salience network (Tarailis et al. 2023 ; Nazare, et al., 2024 ). Neurocognitive research has established microstate E as a neural correlate of interoceptive awareness and affective processing, demonstrating heightened prevalence during cognitively demanding tasks and negatively-valenced affective states, such as post-stress conditions (Tarailis et al. 2023 ; Hu et al. 2023b ). The salience network shows distinct functional abnormalities in individuals with suicidal ideation and non-suicidal self-injury, which may contribute to their observed attentional biases toward threatening stimuli and pervasive hypervigilance (Ho et al. 2021 ). Our study revealed the same change among individuals with SI compared with normal controls, which aligns with the results of a prior study (Ho et al. 2021 ). Interestingly, the greater occurrence and coverage of microstate E among the SA survivors in our study suggested that they might differ from patients with depressive disorder patients. Patients with depressive disorder often experience SI, and their most significant clinical manifestation is anhedonia (Chase et al. 2015 ). People who attempt suicide may be more sensitive to external stimuli, making them more impulsive when faced with the option of taking suicidal actions to deal with their pain. However, further research is necessary to validate this interpretation.

Additionally, regression analyses revealed significant positive correlations between suicide risk severity scores and microstate coverage for both microstate D and microstate E among individuals with SI and suicide attempt survivors.

Taken together, the alterations in microstates reveal a neural model associated with suicide risk, characterized by dysfunctional dynamic interactions across multiple large-scale brain networks. Specifically, individuals at suicide risk (SA and SI groups) exhibited generalized enhancement in the auditory (microstate A) and visual (microstate B) networks, which may reflect abnormal sensitization to perceptual information from both internal and external environments. Meanwhile, the prolonged duration and increased activation of the anterior default mode network (microstate C) in the SI group suggest that excessive self-referential processing may play a central role in the formation and maintenance of suicidal ideation. In contrast, the SA group demonstrated higher activity and greater transition propensity in the dorsal attention network (microstate D) and the salience network (microstate E), which may constitute the neural basis for the transition from passive ideation to active behavior: a brain state highly vigilant to threats or internal signals (microstate E), coupled with altered attentional control and decision-making functions (microstate D), is more likely to facilitate impulsive or planned suicidal acts. Therefore, suicidal behavior may not stem from isolated abnormalities in a single brain network, but rather from a systemic imbalance in the dynamic equilibrium among multiple large-scale networks—an imbalance pattern that may objectively mark the critical transition from ideation to action.


## Limitations

Several factors may constrain the generalizability of these findings. First, the design of this cross-sectional study limits the direct effect of microstate dynamics on the occurrence of suicidal ideation and suicidal behavior, and this topic needs to be further examined in longitudinal research. Second, although differences in microstates between the SA and SI groups have been found at the population level, the feasibility of using these large-scale dynamics to identify or predict individual suicide risk at the individual level remains to be clarified. Finally, this study excluded the impact of depression on the results of the study by controlling for differences in depressive disorder diagnoses between the SA and SI groups. However, depression, which is a known suicide risk factor, is worthy of further exploration in subsequent studies.


## Conclusion

In this study, we found different microstate dynamic patterns among SA survivors, individuals with SI, and normal controls. Compared with those of normal controls, the differences between SA survivors and individuals with SI involved mainly microstates A and B, which are associated with perceptual information processing. The difference between SA survivors and individuals with SI mainly involves microstates C, D and E, which are related to interoceptive and cognitive abilities. These results offer fresh perspectives on the neural mechanisms underlying suicide and indicate that microstate dynamics could potentially act as neurobiomarkers for differentiating suicidal behavior from suicidal ideation.



Qin Liu, Jiaxi Peng and Danmin Miao designed the study and developed the methodology. Qin Liu, Quxing Wu and Zhao Song performed data collection and preprocessing. Peng Fang and Qinliu conducted statistical analyses and microstate classification. Qin Liu wrote the original draft. All authors reviewed, edited, and approved the final manuscript.


## Funding

This work was supported by the Rapid Response Project from the Air Force Medical University (Grant No. 2023KXKT062) and Shaanxi Provincial Natural Science Basic Research Program (2024JC-YBQN-0209).


## Data Availability

No public datasets were generated or analysed during the current study.


## Declarations


### Competing Interests

The authors declare no competing interests.


## Footnotes

Co-first Authors: Qin Liu and Xingqu Wu

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


## Contributor Information

Jiaxi Peng, Email: [EMAIL_REDACTED].

Danmin Miao, Email: [EMAIL_REDACTED].

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Data Availability Statement

No public datasets were generated or analysed during the current study.
