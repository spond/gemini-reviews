# FEXP_ANON_130

## Abstract

To separate the resting-state network of patients with dental pain using independent component analysis (ICA) and analyze abnormal changes in functional connectivity within as well as between the networks.

Twenty-three patients with dental pain and 30 healthy controls participated in this study. We extracted the resting-state functional network components of both using ICA. Functional connectivity differences within 14 resting-state brain networks were analyzed at the voxel level. Directional interactions between networks were analyzed using Granger causality analysis. Subsequently, functional connectivity values and causal coefficients were assessed for correlations with clinical parameters.

Compared to healthy controls, we found enhanced functional connectivity in the left superior temporal gyrus of anterior protrusion network and the right Rolandic operculum of auditory network in patients with dental pain (p<0.01 and cluster-level p<0.05, Gaussian random field corrected). In contrast, functional connectivity of the right precuneus in the precuneus network was reduced, and were significantly as well as negatively correlated to those of the Visual Analogue Scale (r=−4.93, p=0.017), Hamilton Anxiety Scale (r=−0.46, p=0.027), and Hamilton Depression Scale (r=−0.563, p<0.01), using the Spearman correlation analysis. Regarding the causal relationship between resting-state brain networks, we found increased connectivity from the language network to the precuneus in patients with dental pain (p<0.05, false discovery rate corrected). However, the increase in causal coefficients from the verbal network to the precuneus network was independent of clinical parameters.

Patients with toothache exhibited abnormal functional changes in cognitive-emotion-related brain networks, such as the salience, auditory, and precuneus networks, thereby offering a new imaging basis for understanding central neural mechanisms in dental pain patients.


## Introduction

Toothache (TA) is a common form of neuropathic orofacial pain defined as, pain caused by a lesion or disease affecting one or more teeth and/or adjacent and supporting structures including pulp, periodontal tissues, and gums. 1 Odontogenic pain is mainly caused by pulpal infection, periodontal disease, and pericoronitis, mostly affecting the dentin-pulp complex. 2 Dental pain neurotransmission reaches the nociceptors through Aδ and C fibers, then passes through the trigeminal ganglion, trigeminal thalamic tract, sphenopalatine tract, reticular thalamic tract, and finally to the somatosensory cortex and periaqueductal gray matter. 3 Additionally, chronic recurrent pain can cause several mental health problems (such as anxiety, depression, sleep disorders, etc.), which can have detrimental effect on work and life, making it a serious public-health issue in today’s time. 4

Early neuroimaging studies focused on task-state functional magnetic resonance imaging (fMRI) of dental pain, including pulpal electrical stimulation, 5 alveolar ridge stimulation, 6 and stressful periodontal stimulation, 7 which revealed the widespread activation of core pain networks, including the primary somatosensory, insular, and anterior cingulate cortex, as well as the intrinsic central neural mechanisms of sensory experience, and cognitive and affective factors contributing to dental pain initiation. In contrast to the task-state, the hemodynamic characteristics of some voxel-based blood oxygen level-dependent signals in the resting-state reflect the underlying metabolic information changes in patients with TA at a deeper level. For example, patients with TA have significantly higher low-frequency amplitude values in brain regions such as the left posterior central gyrus, right paracentral lobule, and right lingual gyrus than healthy controls. 8 In a study of the dynamics of local indicators in the resting-state of patients with TA, it was found that the brain regions that showed functional abnormalities, such as the left superior temporal and middle frontal gyri, were mostly related to cognition and mood. 9 Previous studies have recognized that the pain experience is a complex perception that interacts with multiple dimensions of sensation, emotion, and cognition. 10 Functional network integration in the brain is not the isolated operation of a particular brain region, but receives projections from widely distributed sensory regions and interacts with multiple regions to achieve confluence of information, with a high degree of local modularity and hierarchical connectivity, so that abnormalities in local regions are do not fully explain functional changes at the level of the entire neural network.

Studies of large-scale brain networks are more conducive to observing brain-wide functional connectivity changes in TA patients. Moreover, there is no systematic fMRI study of intra- and inter-functional integration within different resting-state functional networks in TA patients. Furthermore, any damage to the relevant networks may affect effective cognition and emotional experience. Based on the aforementioned rationale, in this study, we aimed to extract resting-state networks (RSNs) using the independent component analysis (ICA) method to explore the functional connectivity (FC) changes in TA patients, both intra- and inter-networks, as well as the directionality of the flow of abnormal information inter-networks. Thereby exploring the functional changes in the brain due to TA, and to assess the relationship of these functional changes with the clinical parameters.


## Materials and Methods


## Participants

Twenty-five patients with TA, diagnosed by experienced dentists (ie, those with at least 5–10 years of clinical practice, professional medical knowledge and skills, a good reputation in the field, and the ability to handle complex cases and emergencies), were recruited from the Department of Dentistry at the First Affiliated Hospital of Nanchang University. Thirty matched subjects (by age, gender, and education) served as healthy controls (HC). All participants reported themselves as being right-handed and standardized according the Edinburgh Handedness Inventory. This study was approved by the Biomedical Ethics Committee of First Affiliated Hospital of Nanchang University, China (No.2020-9-57). All the subjects and their families were informed of the purpose, procedure, precautions, and possible risks of the study and signed an informed consent form.

The inclusion criteria for the TA group were as follows: 1) patients diagnosed with odontogenic pain (pericoronitis and pulpitis) in the acute phase (duration <7 days); 2) no associated painful diseases such as those of the oral and maxillofacial region, temporomandibular joint disorders, traumatic injuries, or tumors; 3) no abnormal signal changes in the brain on routine MRI examination; and 4) no contraindications to MRI scanning (such as metal implants, epilepsy, claustrophobia, etc.).

The exclusion criteria for the TA group were as follows: 1) co-existing headache, temporomandibular joint disorder, trigeminal neuralgia, fibromyalgia, back pain, or other non-odontogenic pain of any kind; 2) other physical or mental illnesses (such as schizophrenia, paranoid psychosis, and bipolar disorder); and 3) contraindications to MRI scanning.


## Clinical and Cognitive Psychological Assessments

Prior to the MRI scan, the investigators collected clinical information from the subjects, including their gender, age, duration and location of TA, past medical history, and Hamilton Anxiety Scale (HAMA) and Hamilton Depression Scale (HAMD) scores. The Visual Analogue Scale (VAS) was used to assess pain, wherein higher scores indicate more intense pain.


## Resting-State Functional Magnetic Resonance Imaging (fMRI) Data Acquisition

All participants underwent MRI using a 3.0T magnetic resonance system (Siemens, Erlangen, Germany) scanner with 8-channel phased array magnetic head coils at our hospital. The subjects were informed about the precautions to be taken and their cooperation was ascertained preoperatively. During the scans, the subjects were placed supine on the examination bed. First, the head was immobilized with foam, and the subjects were given noise canceling headphones to limit head movements from noise effects. All subjects were awake with their eyes closed. Prior to resting-state fMRI scans, all subjects underwent routine T1-weighted and T2-weighted (T1W and T2W) imaging to exclude structural brain lesions that could affect brain function and microstructure. MRI scans included T1 structural images and resting-state functional images. T1 structural images were scanned with echo time (TE) = 2.26 ms, repetition time (TR) = 1900 ms, flip angle = 9°, acquisition matrix = 256×256 mm, field of view = 250×250 mm, thickness = 1.0 mm, gap = 0.5 mm, voxel = 1.0 × 1.0×1.0 mm. Resting-state fMRI scan parameters were: TE = 30 ms, TR = 2000 ms, flip angle = 90°, acquisition matrix = 64×64 mm, field of view = 220×220 mm, thickness = 4.0 mm, gap = 1.2 mm, and voxel = 3.0×3.0 × 4.0 mm.

At the end of the scan, the image quality was checked; if the image did not meet the prerequisites, the results of the scan were discarded, or the scan repeated with the subject’s permission.


## Data Preprocessing

Scanned completed data were analyzed using MRIcro software ( http://www.MRIcro.com ) to analyze the acquired information and exclude incomplete data. SPM12 ( http://www.fil.ion.ucl.ac.uk/spm ) and the DPABI software package ( http://rfmri.org/DPABI ) were run in MATLAB R2018b to analyze the resting-state fMRI, and the structural images were preprocessed. Essentially the steps included: 1) Initial DICOM data of the subjects were converted to nii format; 2) The first 10 time points of the images were removed; 3) Temporal layer correction; 4) Head motion correction; 5) Spatial normalization, aligning BOLD fMRI with high-resolution T1W structural images, the DARTEL algorithm was used to segment the T1 structural images into gray matter, white matter, and cerebrospinal fluid, followed by nonlinear transformation of the gray matter maps to Montreal Neurological Institute space, and the fMRIs were further aligned to the MNI spatial templates and resampled to voxel size of 3×3×3 mm; 6) the images were spatially smoothed using a Gaussian kernel of 8 mm full-width at half-maximum. In addition, subjects with head movement in the cardinal direction (x, y, z) > 3 mm and maximum rotation (x, y, z) > 3° were excluded, whereby two patients with TA were excluded.


## Group Independent Component Analysis (ICA) and Resting-State Network (RSN) Identification

First, we performed a group spatial ICA on the preprocessed data of patients with TA and HC using the Group ICA of the fMRI Toolbox (GIFT, [GITHUB_REPO_REDACTED] ). We chose a relatively high model-order ICA (IC = 75) because first, previous studies have demonstrated that such models yield refined components 11 and highly stable ICA decomposition. 12 Second, to ensure the reliability and stability of the ICs, the Infomax algorithm with ICASSO was executed 100 times. 13 Finally, subject-specific spatial maps and time courses were back-constructed using group ICA, and the results were converted to a z-score for display. Based on the GUI display window in the GIFT toolbox displaying all components, ICs associated with the cerebrospinal fluid-, motor-, or vascular-evoked pseudo-activation were discarded. We identified 14 RSNs using a template-matching algorithm based on the maximum spatial correlation value. Functional templates were provided by Shirer et al. 14


## Analysis of Intra-Network Functional Connectivity (FC)

MATLAB SPM12 software was used to perform one-sample t -tests for the RSNs in the TA and HC groups to obtain templates at the group level, and the concurrent sets were then taken as the total mask for each network. Differences in the FC values between the two groups for each network within the corresponding total mask were examined using two-sample t -tests (GRF-corrected, voxel p<0.01, cluster p<0.05). In this step, head motion parameters, age, and sex were regarded as covariates of no interest to avoid their impact on the findings.


## Granger Causality Analysis (GCA)

Granger causality analysis was performed using the Functional Network Connectivity Toolbox ( https://trendscenter.org/software/ ). According to the given interval and order selection criteria, the optimal order of the autoregressive model was selected, which was not constant and varied within the interval for every mutual relationship. We preferred the Schwarz-Bayesian criterion to determine the optimal order of the autoregressive model and calculated the smallest mean-squared prediction error of the fitted autoregressive model. In this study, GCA was compared between patients with TA and HC. The statistical significance level was set at a p-value <0.05, with false discovery rate (FDR) correction.


## Statistical Analysis

General clinical data of the two groups were statistically tested using the statistical analysis software SPSS version 25, and data that did not follow a normal distribution were reported as medians and quartiles using the Mann–Whitney U -test. The independent sample t -test was used to analyze the measurement data, which are presented as the mean ± standard deviation ( \documentclass[12pt]{minimal} \usepackage{wasysym} \usepackage[substack]{amsmath} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage[mathscr]{eucal} \usepackage{mathrsfs} \DeclareFontFamily{T1}{linotext}{} \DeclareFontShape{T1}{linotext}{m}{n} {linotext }{} \DeclareSymbolFont{linotext}{T1}{linotext}{m}{n} \DeclareSymbolFontAlphabet{\mathLINOTEXT}{linotext} \begin{document} $\overline x\pm {{\rm s}}$\end{document} ). The chi-square test was used to detect differences in the data between the two groups. Abnormal Granger causality coefficients and FC differences within the RSN were correlated with VAS, HAMA, and HAMD scores, controlling for age and sex. A relationship was considered significant if the p-value was <0.05.


## Results


## Demographic and Clinical Data of TA and HC Groups

Table 1 shows the demographic data and clinical scale scores, including VAS, HAMA and HAMD scores, of all subjects. There was no statistically significant difference in age and gender between the two groups. The scores were significantly higher in TA patients than in HC (p<0.001) ( Table 1 ). Table 1 Demographic and Clinical Data of TA and HC Groups TA HC t P Age (year, mean±SD) 26.96±3.72 28.33±4.07 1.60 0.21 Gender (male/female) 8/15 10/20 0.01* 0.91 Leigh hand (right/Left) 23/0 30/0 N/A N/A Duration of pain (days) 3.0(1.0) N/A N/A N/A VAS (0–10) 6.0(2.0) N/A N/A N/A HAMA 8.00(3.00) 2.00(2.00) −6.24** <0.001 HAMD 11.00(3.00) 2.00(1.25) −6.26** <0.001 Notes : *Represents the chi-square test χ 2 -value;**Represents the Mann–Whitney U -test Z-value; p <0.05, statistical significance. Abbreviations : TA, toothache; HC, healthy control; VAS, Visual Analogue Scale; HAMA, Hamilton Anxiety Scale; HAMD, Hamilton Depression Scale.


### Table 1: Demographic and Clinical Data of TA and HC Groups

|  | TA | HC | t | P |
| Age (year, mean±SD) | 26.96±3.72 | 28.33±4.07 | 1.60 | 0.21 |
| Gender (male/female) | 8/15 | 10/20 | 0.01* | 0.91 |
| Leigh hand (right/Left) | 23/0 | 30/0 | N/A | N/A |
| Duration of pain (days) | 3.0(1.0) | N/A | N/A | N/A |
| VAS (0–10) | 6.0(2.0) | N/A | N/A | N/A |
| HAMA | 8.00(3.00) | 2.00(2.00) | −6.24** | <0.001 |
| HAMD | 11.00(3.00) | 2.00(1.25) | −6.26** | <0.001 |

## Spatial Distribution and Correlation Coefficients of RSNs

Analysis of the fMRI data revealed 14 spatial maps of potentially relevant RSNs, including the posterior salience network (IC, 55; correlation coefficient: 0.510), anterior salience network (IC, 59; correlation coefficient: 0.331), basal ganglia network (IC, 44; correlation coefficient: 0.148), primary visual network (IC, 25; correlation coefficient: 0.334), and visuospatial network (IC, 63; correlation coefficient: 0. 459), higher visual network (IC, 20; correlation coefficients: 0.609), language network (IC, 47; correlation coefficients: 0.271), sensorimotor network (IC, 6; correlation coefficients: 0.339), auditory network (IC, 11; correlation coefficients: 0.456), left executive control network (IC, 37; correlation coefficients: 0.294), right executive control network (IC, 32; correlation coefficients: 0.379), dorsal default mode network (IC, 39; correlation coefficients: 0.533), precuneus network (IC, 24; correlation coefficients: 0.303), and ventral default mode network (IC, 35; correlation coefficients: 0.477); Figure 1 shows a map of the corresponding spatial distribution of these 14 networks. Figure 1 Spatial distribution of brain networks corresponding to the 14 independent components in Group ICA.


> **Figure 1:** Spatial distribution of brain networks corresponding to the 14 independent components in Group ICA.


## FC Analysis

Compared to HC, we found that FC in the left superior temporal gyrus of the anterior salience network and the right Rolandic operculum of the auditory network was increased. FC in the right precuneus of the precuneus network decreased (two-tailed voxel level p<0.01, cluster level p<0.05, GRF-corrected) ( Table 2 ; Figure 2 ). Table 2 Brain Regions with Significant Differences in FC Within the Network of RSNs Network Anatomical Location Cluster Size MNI Coordinates of Peak T value X Y Z aSN Temporal_Sup_L 37 −54 −6 0 3.91 Auditory Rolandic_Oper_R 75 36 −27 18 4.01 Precuneus Precuneus_R 73 9 −42 42 −4.33 Notes : Temporal_Sup_L, left superior temporal gyrus; Rolandic_Oper_R, right Rolandic operculum; and Precuneus_R, right precuneus. Abbreviation : aSN, anterior salience network. Figure 2 Brain regions with inter-network FC differences mainly located in the aSN, the auditory network, and the precuneus network. Notes : Warm colors in the TA group represent increased FC, and cool colors represent decreased FC.


### Table 2: Brain Regions with Significant Differences in FC Within the Network of RSNs

| Network | Anatomical Location | Cluster Size | MNI Coordinates of Peak | T value |
| X | Y | Z |
| aSN | Temporal_Sup_L | 37 | −54 | −6 | 0 | 3.91 |
| Auditory | Rolandic_Oper_R | 75 | 36 | −27 | 18 | 4.01 |
| Precuneus | Precuneus_R | 73 | 9 | −42 | 42 | −4.33 |

> **Figure 2:** Brain regions with inter-network FC differences mainly located in the aSN, the auditory network, and the precuneus network.


## Causal Relationships of RSNs

We also used GCA to investigate the causal relationships of the 14 RSNs between TA and HCs. Patients with TA had significantly increased connectivity from the language network to the precuneus network (p<0.05, FDR-corrected) ( Figure 3 ). Additional results are shown in Supplementary Figure 1 . Figure 3 Differences between the GCA groups of TA patients and HC patients. The arrow direction represents the direction of information flow. Note : The color bar represents the spectrum (0–0.25 Hz) of blood oxygenation levels which are dependent on the brain. The lighter the color, the lower the spectral frequency, and the darker the color, the higher the spectral frequency.


> **Figure 3:** Differences between the GCA groups of TA patients and HC patients. The arrow direction represents the direction of information flow.


## Analysis of Correlations

Compared with HC, reduced FC values in the right precuneus within the precuneus network were significantly and negatively correlated with VAS (r=−4.93, p=0.017), HAMA (r=−0.46, p=0.027), and HAMD (r=−0.563, p<0.01) (Spearman correlation analysis) ( Figure 4a–c ). However, the FC values of the different brain regions within the network of the other RSNs were not significantly correlated with the scores of the clinically relevant scales. In TA patients, the increase in the causal coefficient from language network to precuneus network was not significantly correlated with clinical parameters such as VAS, HAMA, and HAMD. Figure 4 Scatter plot of correlation between functional correctional values in the precuneus and clinical scores. Subgraphs ( a – c ) show the correlation between VAS, HAMA and HAMD and precuneus, respectively.


> **Figure 4:** Scatter plot of correlation between functional correctional values in the precuneus and clinical scores. Subgraphs ( a – c ) show the correlation between VAS, HAMA and HAMD and precuneus, respectively.


## Discussion

We applied group ICA and GCA to reveal the relationships within and between brain networks in TA patients and HC. Our findings revealed three intra-network FC abnormalities in patients with TA, including the anterior salience network, auditory, and precuneus networks. While analyzing FC between networks, we also found an abnormal increase in information cycling from the language network to the precuneus in patients with TA. This approach may provide a useful complement to the understanding of the potential compensatory mechanisms of neuropathic pain in patients with TA.

In the present study, we found that in patients with TA, abnormal FC was present within the precuneus network, particularly involving the right precuneus, which had reduced FC and was negatively correlated with clinical variables (VAS, HAMA, and HAMD). The precuneus network comprises the precuneus, middle cingulate cortex, posterior inferior parietal lobule, and dorsal angular gyri. The right precuneus is a critical node in the precuneus network. 15 The precuneus is part of a group of areas related to the neurological characteristics of pain, 16 and impairment of consciousness is often associated with its deficits. 17 Yang et al 18 found that the right precuneus showed both structural and functional changes in patients with chronic cervical spine pain, as reflected by reduced gray matter volume and reduced FC in the bilateral medial prefrontal cortex. Both were negatively correlated with VAS scores, which is highly consistent with some of the results of the present study. Studies have shown that changes in precuneus functional connectivity are strongly associated with reduced sleep quality in individuals with depression. Disruption of the connectivity in this area can lead to diminished consciousness, cognitive impairment, 19 depression. 20 , 21 In this study, decreased FC values in the right precuneus were negatively correlated with VAS scores, indicating that higher pain levels were associated with more pronounced changes in the right precuneus. Reduced FC of the right precuneus was also negatively correlated with HAMA and HAMD scores, suggesting that negative emotions in patients with TA may be associated with changes in this region.

Compared with HC, patients with TA showed functional connectivity changes in the auditory network, mainly in the right Rolandic operculum. Anatomically, the Rolandic operculum 22 is located in the precentral and postcentral gyri on either side of the central sulcus of Rolando. It has been shown to have complex connectivity patterns that play an important role in sensory-auditory integration, particularly in speech production. 23 For example, Xu et al 24 found that the FC of the right insula with the central sulcus was reduced in patients with sensorineural deafness. Several studies have confirmed the relationship between the Rolandic operculum and emotions. In a study by Sutoko et al 25 , it was found that, among patients with post-stroke depression, the worse the condition (level of depression), the greater the degree of lesioning of the right Rolandic operculum. Moreover, the mean diffusivity of the Rolandic operculum was positively correlated with indices of empathizing-cooperativeness. 26 An fMRI study based on cerebellar-cerebellar FC showed reduced FC between the right Rolandic operculum and the cerebellar vermis in older women with symptoms of depression. 27 This thereby confirms that changes in the Rolandic operculum are closely related to sensorineural and emotional disturbances. In the present study, increased FC in the right Rolandic operculum, in conjunction with the above literature, cannot be ruled out as an early change in the tendency toward affective disorders in patients with TA.

In addition, the left superior temporal gyrus within the anterior salience network of patients showed abnormal functional changes, as demonstrated by an increase in FC. It is a task-positive network that can recognize relevant stimuli and guide behavioral responses and is associated with attentional and internal perceptual processes. 28 Many previous studies have shown that pain can cause abnormal alterations in the functioning of cognitive emotion-related networks; for example, Van Ettinger-Veenstra et al 29 found that the connectivity of the salience network increased in patients with chronic widespread pain and was associated with increased pain sensitivity. The superior temporal gyrus is often considered the auditory-perceptual and emotion-regulatory portion of the human brain, 30 which is critical for individual stress experiences, cognitive processes, and adaptive behaviors, and is more strongly active on the left side. 31 Lan et al 32 in a seed-based FC analysis found reduced FC in the left superior temporal gyrus in patients with chronic pelvic pain syndrome. A systematic review of migraine studies revealed that patients have increased gray matter volume in the superior temporal gyrus bilaterally. 33 This finding is partially consistent with the results of the present study. The elevated FC of the left superior temporal gyrus in the present study can be interpreted as a compensatory increase in central nociceptive conduction in patients with TA; however, we did not find a significant correlation between FC and clinical scales (eg, VAS), which may be an overestimation of its compensatory effect. The structure of the superior temporal gyrus may also undergo alterations when acute pain develops into chronic pain.

Of the 14 RSNs causal relationships, only a significant increase in information flow from the language to the precuneus network was found in patients with TA compared to HC. The language network includes the posterior insula, which is part of the “pain neuromatrix” ascending processing system and is involved in important cognitive tasks such as language comprehension. 34 Giorgio et al 34 found a higher long-range FC between the cerebellar and auditory language comprehension networks in patients with cluster headache patients. Zhang et al 35 found abnormal patterns of causal interactions in the language networks of patients with intractable hallucinations, suggesting that insufficient or disrupted connectivity within the language network may be crucial to their pathology. Interestingly, information flow from the language network to the precuneus was not observed in the HC group. In contrast, the increased directional connectivity from the language to the precuneus network in patients with TA may be related to the unbalanced dynamic interactions within the precuneus network, and to a certain extent, it reflects damage to the precuneus network, which may be a potential mechanism for impaired speech and auditory function in TA patients.


## Limitation

Although this study revealed functional changes in cognitive emotion-related networks in patients with TA, several limitations exist. First, the anxiety and depression scores of patients with TA in this study were higher than those of HC, but they did not meet the criteria for the diagnosis of anxiety and depression. Moreover, since the two emotions overlapped each other it was difficult for us to fully explain the relationship between pain, anxiety, depression, and brain network changes; therefore, we were very cautious while discussing the results. In the future, we will expand the sample size to further explore the neural mechanisms underlying the accompanying relationships between emotional symptoms. Second, the patients included in this study mostly had acute pericoronitis or acute exacerbation of chronic pulpitis. However, the effect of different types of dental pain on central pain remains unclear. In future studies, we will contemplate subdividing the types of TA and observe the changes in the diencephalic function for each type of TA. Third, although the results of Allen et al’s study support that 75 components are the most stable, we attempted to divide the components into 31 and 100 components which matched less closely to the template. Using the basal-ganglia network as an example, the highest correlation values of 75, 31, and 100 components were 0.148, 0.020, and 0.064, respectively. The temporal and spatial resolutions of MRI may be a significant factor, which is also one of the limitations of this study.


## Conclusion

In summary, in the absence of clinical cognitive deficits, pain perception in patients with TA interferes with the brain networks associated with cognitive functioning, which could help reveal the underlying neuropathological mechanisms. The present study also found that the brain regions exhibiting abnormal functional changes in patients with TA were associated with anxiety and depression. This finding provides valuable insights for subsequent studies associated with emotional problems in patients experiencing pain.


## Data Sharing Statement

The data are available from the corresponding author upon reasonable request made by email.