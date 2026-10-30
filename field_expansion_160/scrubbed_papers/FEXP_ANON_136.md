# FEXP_ANON_136

## Abstract

Cognitive networks impairments are common in neuropsychiatric disorders like Attention Deficit Hyperactivity Disorder (ADHD), bipolar disorder (BD), and schizophrenia (SZ). While previous research has focused on specific brain regions, the role of the procedural memory as a type of long-term memory to examine cognitive networks impairments in these disorders remains unclear. This study investigates alterations in resting-state functional connectivity (rs-FC) within the procedural memory network to explore brain function associated with cognitive networks in patients with these disorders.

This study analyzed resting-state functional magnetic resonance imaging (rs-fMRI) data from 40 individuals with ADHD, 49 with BD, 50 with SZ, and 50 healthy controls (HCs). A procedural memory network was defined based on the selection of 34 regions of interest (ROIs) associated with the network in the Harvard-Oxford Cortical Structural Atlas (default atlas). Multivariate region of interest to region of interest connectivity (mRRC) was used to analyze the rs-FC between the defined network regions. Significant differences in rs-FC between patients and HCs were identified ( P < 0.001).

ADHD patients showed increased Cereb45 l - Cereb3 r rs-FC ( p = 0.000067) and decreased Cereb1 l - Cereb6 l rs-FC ( p = 0.00092). BD patients exhibited increased rs-FC between multiple regions, including Claustrum r - Caudate r ( p = 0.00058), subthalamic nucleus r - Pallidum l ( p = 0.00060), substantia nigra l - Cereb2 l ( p = 0.00082), Cereb10 r - SMA r ( p = 0.00086), and Cereb9 r - SMA l ( p = 0.00093) as well as decreased rs-FC in subthalamic nucleus r - Cereb6 l ( p = 0.00013) and Cereb9 r - Cereb9 l ( p = 0.00033). SZ patients indicated increased Caudate r– putamen l rs-FC ( p = 0.00057) and decreased rs-FC in subthalamic nucleus r – Cereb6 l ( p = 0.000063), and Cereb1 r – subthalamic nucleus r ( p = 0.00063).

This study found significant alterations in rs-FC within the procedural memory network in patients with ADHD, BD, and SZ compared to HCs. These findings suggest that disrupted rs-FC within this network may related to cognitive networks impairments observed in these disorders.

Not applicable.


## Introduction

Neurological and mental disorders afflict nearly a billion people worldwide, underscoring their significant global health burden [ 1 ]. ADHD [ 2 ], BD [ 3 ], and SZ [ 4 ] affecting 5%, 2.5%, and 0.5% of the population respectively, collectively impact closer to 8% of the population. These disorders are characterized by cognitive dysfunction and impaired motor control [ 5 , 6 ]. A common deficit in these disorders is impaired long-term memory, impacting cognitive and mental functions [ 7 – 9 ]. Long-term memory is typically divided into implicit and explicit memory [ 10 ]. Implicit memory operates below conscious awareness, storing and retrieving information without intention. Brain regions like the cerebellum, subcortical motor areas, and basal ganglia are crucial for this type of memory, facilitating the acquisition and consolidation of skills, behaviors, and habits [ 11 ]. Unlike implicit memory, explicit memory requires conscious effort for storage, retrieval, and sharing [ 12 ]. The cerebral cortex, particularly the neocortex, is the neural basis for explicit memory [ 13 ]. Accessing explicit memories requires intentional effort and conscious focus [ 14 ]. Given the challenges neuropsychiatric patients, especially ADHD, BD, and SZ, face with task cooperation [ 15 ], investigating implicit memory during rest may offer insights into their cognitive networks impairments [ 13 ]. Procedural memory, a subconscious form of long-term memory for motor skills and habits, is interconnected with various cognitive networks [ 16 ]. Procedural memory allows tasks to be recalled and executed effortlessly, without conscious deliberation [ 17 ]. The cerebellum, supplementary motor area (SMA), and basal ganglia form the procedural memory network [ 18 ]. These regions are functionally connected, meaning that their neural activities are statistically dependent on each other [ 19 ]. Because these areas are active in the resting state, the intrinsic patterns of activity and neural connections that occur spontaneously in the brain demonstrate a special type of functional connectivity: rs-FC [ 20 ]. Given the functional connectivity within the procedural memory network and its resting-state activity, exploring rs-FC patterns can provide valuable insights into the neural mechanisms underlying its organization [ 21 ]. Neuroimaging is crucial for studying brain functional connections, the patterns of interaction between different brain regions [ 22 ]. fMRI is a prominent neuroimaging method due to its high spatial resolution, non-invasive nature, and strong signal-to-noise ratio [ 23 ]. rs-fMRI is a specialized fMRI technique that measures brain activity at rest, focusing on the spontaneous fluctuations of the BOLD signal [ 24 ]. BOLD signals exhibit high temporal coherence between functionally related brain regions [ 25 ]. Various methods can be used to analyze functional connections between brain regions based on these fluctuations. Some of these methods include seed-based connectivity, MRRC, network measures, dynamic connectivity, graph theory and etc [ 26 ]. MRRC method analyzes the connectivity patterns between multiple regions of interest (ROIs) simultaneously, considering the relationships between multiple ROIs [ 27 , 28 ]. MRRC approach offers several advantages over other connectivity methods: (1) unlike seed-based connectivity, which focuses on the connectivity of a single seed region [ 29 ], mRRC allows for the simultaneous examination of the interrelationships between multiple ROIs. This provides a more holistic understanding of the network’s dynamics [ 30 ]. (2) While network measures can provide global properties of the network, mRRC focuses on the specific interactions between individual ROIs [ 27 ]. This allows for a more detailed investigation of the network’s structure and function. (3) While dynamic connectivity explores how connectivity patterns change over time, mRRC can capture the static or relatively stable patterns within the network [ 31 ]. This is particularly useful for understanding the underlying architecture of the procedural memory network, as this network relies on consistent and stable communication patterns between brain regions [ 32 , 33 ]. (4) Graph theory provides a framework for analyzing networks as graphs, but it often focuses on global properties rather than specific ROI-to-ROI interactions [ 34 ]. According to the mentioned advantages, mRRC method was chosen for this study due to its ability to comprehensively analyze the interactions between multiple ROIs within the procedural memory network. Studies investigating brain function associated with cognitive networks by examining alterations in rs-FC within procedural memory network in neuropsychiatric patients such as those with ADHD, BD, and SZ, using rs-fMRI imaging have not been reported. In this study, we investigate whether rs-FC within the procedural memory network differs between patients with ADHD, BD, and SZ compared to healthy controls, and whether these rs-FC alterations are associated with cognitive networks impairments in the studied patient groups. Using rs-fMRI and the mRRC method, we identified, characterized, and investigated the association between alterations in rs-FC within the procedural memory network and cognitive networks impairments in patients with ADHD, BD, and SZ.


## Materials and methods


## Participants

This study leveraged the UCLA Consortium for Neuropsychiatric Phenomics (CNP) dataset [ 35 ]. Demographic details of the 189 participants (104 male, 85 female) are provided in Table 1 . The dataset included individuals aged 21–50 years (mean: 33.72, median: 31.0). Participants were selected based on the following criteria: right-handedness, absence of metal implants, non-pregnancy, lack of MRI fear, and no history of head trauma or loss of consciousness. All participants underwent 314-second fMRI scans [ 35 ].

Table 1 Demographic characteristics of the UCLA CNP database Groups ADHD ( n = 40) BD ( n = 49) SZ ( n = 50) HCs ( n = 50) Age (M ± SD) Male 32.90 ± 10.60 35.89 ± 9.22 35.61 ± 8.91 31.96 ± 8.78 Female 33.27 ± 11.16 34.48 ± 8.93 39.17 ± 8.59 30.50 ± 8.69 Gender (%) Male 7.7 10.3 14 25 Female 8.1 7.7 4.4 22.8


### Table 1: Demographic characteristics of the UCLA CNP database

| Groups | ADHD ( n = 40) | BD ( n = 49) | SZ ( n = 50) | HCs ( n = 50) |
| Age (M ± SD) | Male | 32.90 ± 10.60 | 35.89 ± 9.22 | 35.61 ± 8.91 | 31.96 ± 8.78 |
| Female | 33.27 ± 11.16 | 34.48 ± 8.93 | 39.17 ± 8.59 | 30.50 ± 8.69 |
| Gender (%) | Male | 7.7 | 10.3 | 14 | 25 |
| Female | 8.1 | 7.7 | 4.4 | 22.8 |

## Image acquisition

This study utilized rs-fMRI data from a publicly available resource: the UCLA CNP dataset on OpenNeuro (10.18112/openneuro.ds000030.v1.0.0) [ 35 ]. The CNP database employed a 3 Tesla (3T) Siemens Trio scanner to acquire both fMRI and structural MRI (sMRI) images from participants. The fMRI images were acquired using a T2-weighted echo planar imaging (EPI) sequence with the following parameters: images slice thickness = 4 mm, 34 slices, TR = 2s, TE = 30ms, FOV = 192 mm, flip angle = 90°, matrix size = 64 × 64. Additionally, T1-weighted high-resolution anatomical scans (MPRAGE) were obtained with the following parameters: images slice thickness = 1 mm, 176 slices, TR = 1.9s, TE = 2.26ms, FOV = 250 mm, matrix size = 256 × 256.


## Image preprocessing

As discussed in recent literature, global signal regression (GSR) can introduce spurious correlations and distort functional connectivity patterns, particularly in resting-state fMRI studies [ 40 – 44 ]. To avoid these potential pitfalls, we opted not to apply global signal regression in our analysis. To preprocess both sMRI and fMRI data, we employed the CONN v21.a functional connectivity toolbox [ 30 ], built upon SPM12. For sMRI preprocessing, the following steps were executed: (1) the image center was translated to the origin coordinates (0,0,0) to establish a consistent reference point. (2) Unified segmentation and MNI (Montreal Neurological Institute) normalization were applied using a comprehensive model that integrates segmentation, registration, and normalization into a single process [ 36 ]. The fMRI data underwent a rigorous preprocessing pipeline to ensure data quality and reliability. Key steps included: (1) Motion Correction: Head motion was corrected using realignment and unwarp techniques. The image center was translated to the origin coordinates (0,0,0) to establish a consistent frame of reference. (2) Temporal Correction: Slice-time correction was applied to account for temporal variations. (3) Outlier Detection: Artifact Detection Toolbox (ART)-based outlier scan detection and scrubbing methods were used to identify and remove volumes with excessive head motion, ensuring data integrity [ 37 ]. Specifically, we utilized the ART to pinpoint outlier volumes within our functional data. This identification was based on measures such as framewise displacement (FD) and other motion parameters, as calculated by Statistical Parametric Mapping (SPM) [ 38 ]. (4) Spatial Normalization: To ensure accurate spatial alignment between anatomical and functional data, T1-weighted and Echo-Planar Imaging (EPI) images were co-registered prior to normalization. The co-registered images were then normalized to the MNI space to facilitate inter-subject comparisons [ 39 ]. (5) Nuisance Regression: To account for noise variables, nuisance regression was performed using the 6 realignment parameters, their derivatives, scrubbing vectors, and the first 5 principal components derived from white matter (WM) and cerebrospinal fluid (CSF) time series using CompCor [ 30 ]. (6) Temporal Filtering: Temporal band-pass filtering (0.008–0.09 Hz) and linear detrending were applied to reduce noise and drift, enhancing the quality of the fMRI data [ 36 ].


## Procedural memory network

Procedural memory, a fundamental component of the memory system, facilitates the automatic execution and retrieval of motor and cognitive skills necessary for various tasks. Operating primarily at a subconscious level, it seamlessly guides activities. When required, procedural memories are automatically retrieved and applied in executing complex procedures involving motor and cognitive functions [ 45 ]. The procedural memory network is comprised of key anatomical brain structures: the basal ganglia, cerebellum, and SMA. These regions, interconnected through neural pathways, collectively facilitate the automatic execution and retrieval of motor and cognitive skills [ 18 ]. The basal ganglia play a pivotal role in selecting and initiating motor actions, as well as learning and refining motor and cognitive skills through practice [ 46 ]. The cerebellum contributes to motor coordination, precision, and timing, aiding in fine-tuning movements and error correction during skill acquisition [ 47 ]. Moreover, the SMA is responsible for planning and coordinating complex movements, particularly sequences or well-learned motor patterns. It plays a crucial role in initiating and executing motor programs [ 48 ]. In this study, we defined a procedural memory network comprising 34 ROIs using the CONN toolbox. These ROIs were distributed across the basal ganglia (12), cerebellum (lobules I-X; 20), and SMA (2) [ 18 ] (A complete reference ring view of all ROIs is provided in Fig. 1 , with their corresponding MNI coordinates listed in Table 2 ). The ROIs were defined using MNI coordinates from the default atlas in the CONN toolbox [ 30 ] and the study by Song X, et al. [ 49 ]. This network was established to examine the functional connectivity between ROIs within the procedural memory network in individuals with ADHD, BD, and SZ.

Fig. 1 ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network regions. ( d ) A reference ring view of all ROIs associated with brain’s procedural memory network


> **Fig. 1:** ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network regions. ( d ) A reference ring view of all ROIs associated with brain’s procedural memory network

Table 2 MNI coordinates of the 34 ROIs relevant to procedural memory network ROI MNI coordinate Abbreviation Left caudate nucleus (-13, 9, 10) Caudate l Right caudate nucleus (13, 10, 10) Caudate r Left Claustrum (-33, -20, 12) Claustrum l Right Claustrum (33, -19, 10) Claustrum r Left Substantia Nigra (-12, -15, -18) Substantia nigra l Right Substantia Nigra (13, -17, -16) Substantia nigra r Left Subthalamic nucleus (-18, -18, -8) Subthalamic nucleus l Right Subthalamic nucleus (12, -18, -7) Subthalamic nucleus r Left Supplementary motor area (-5, -3, 56) SMA l Right Supplementary motor area (6, -3, 58) SMA r Left Putamen (-25, 0, 0) Putamen l Right Putamen (25, 2, 0) Putamen r Left Pallidum (-19, -5, -1) Pallidum l Right Pallidum (20, -4, -1) Pallidum r Left cerebellar lobule I (-36, -66, -30) Cereb1 l Right cerebellar lobule I (38, -67, -30) Cereb1 r Left cerebellar lobule II (-29, -73, -38) Cereb2 l Right cerebellar lobule II (32, -69, -40) Cereb2 r Left cerebellar lobule III (-9, -37, -19) Cereb3 l Right cerebellar lobule III (12, -35, -19) Cereb3 r Left cerebellar lobules IV&V (-14, -44, -17) Cereb45 l Right cerebellar lobules IV&V (16, -44, -19) Cereb45 r Left cerebellar lobule VI (-23, -58, -24) Cereb6 l Right cerebellar lobule VI (24, -58, -25) Cereb6 r Left cerebellar lobule VII (-32, -60, -45) Cereb7 l Right cerebellar lobule VII (33, -63, -48) Cereb7 r Left cerebellar lobule VIII (-26, -55, -48) Cereb8 l Right cerebellar lobule VIII (25, -56, -49) Cereb8 r Left cerebellar lobule IX (-11, -49, -46) Cereb9 l Right cerebellar lobule IX (9, -49, -46) Cereb9 r Left cerebellar lobule X (-23, -34, -42) Cereb10 l Right cerebellar lobule X (26, -34, -41) Cereb10 r


### Table 2: MNI coordinates of the 34 ROIs relevant to procedural memory network

| ROI | MNI coordinate | Abbreviation |
| Left caudate nucleus | (-13, 9, 10) | Caudate l |
| Right caudate nucleus | (13, 10, 10) | Caudate r |
| Left Claustrum | (-33, -20, 12) | Claustrum l |
| Right Claustrum | (33, -19, 10) | Claustrum r |
| Left Substantia Nigra | (-12, -15, -18) | Substantia nigra l |
| Right Substantia Nigra | (13, -17, -16) | Substantia nigra r |
| Left Subthalamic nucleus | (-18, -18, -8) | Subthalamic nucleus l |
| Right Subthalamic nucleus | (12, -18, -7) | Subthalamic nucleus r |
| Left Supplementary motor area | (-5, -3, 56) | SMA l |
| Right Supplementary motor area | (6, -3, 58) | SMA r |
| Left Putamen | (-25, 0, 0) | Putamen l |
| Right Putamen | (25, 2, 0) | Putamen r |
| Left Pallidum | (-19, -5, -1) | Pallidum l |
| Right Pallidum | (20, -4, -1) | Pallidum r |
| Left cerebellar lobule I | (-36, -66, -30) | Cereb1 l |
| Right cerebellar lobule I | (38, -67, -30) | Cereb1 r |
| Left cerebellar lobule II | (-29, -73, -38) | Cereb2 l |
| Right cerebellar lobule II | (32, -69, -40) | Cereb2 r |
| Left cerebellar lobule III | (-9, -37, -19) | Cereb3 l |
| Right cerebellar lobule III | (12, -35, -19) | Cereb3 r |
| Left cerebellar lobules IV&V | (-14, -44, -17) | Cereb45 l |
| Right cerebellar lobules IV&V | (16, -44, -19) | Cereb45 r |
| Left cerebellar lobule VI | (-23, -58, -24) | Cereb6 l |
| Right cerebellar lobule VI | (24, -58, -25) | Cereb6 r |
| Left cerebellar lobule VII | (-32, -60, -45) | Cereb7 l |
| Right cerebellar lobule VII | (33, -63, -48) | Cereb7 r |
| Left cerebellar lobule VIII | (-26, -55, -48) | Cereb8 l |
| Right cerebellar lobule VIII | (25, -56, -49) | Cereb8 r |
| Left cerebellar lobule IX | (-11, -49, -46) | Cereb9 l |
| Right cerebellar lobule IX | (9, -49, -46) | Cereb9 r |
| Left cerebellar lobule X | (-23, -34, -42) | Cereb10 l |
| Right cerebellar lobule X | (26, -34, -41) | Cereb10 r |

## Rs-FC analysis

The human brain is a complex network of interconnected regions, both functionally and structurally. Effective functional communication between these regions is crucial for complex cognitive processes, as it enables the seamless integration of information across different brain areas. Studying functional connectivity in the human brain is essential for gaining deeper insights into its fundamental organization [ 50 ]. rs-FC examines the statistical dependencies between spatially distributed neuronal units while the brain is at rest, revealing the intrinsic functional organization of the brain [ 51 ]. We employed the mRRC method within the CONN toolbox to conduct correlation analyses and estimate functional connectivity in the procedural memory network. Pre-defined ROIs associated with the procedural memory network (Table 2 ) were used to calculate correlations between brain regions within this network. The mRRC approach enabled us to spatially map correlation patterns in the brain during rest, identifying abnormal functional connections among studied neuropsychiatric disorders.


## Statistical analysis

To analyze the data, we utilized the CONN v21.a toolbox [ 30 ] within MATLAB R2019b software. Prior to analysis, we verified the normality of the data distribution. The data were concentrated around the mean, indicating a normal distribution [ 52 ]. Independent t-tests were conducted to examine significant differences in rs-FC within the procedural memory network between neuropsychiatric patients (ADHD, BD, and SZ) and HCs. To address the multiple comparisons problem, we applied False Discovery Rate (FDR) correction to control the proportion of false positive findings. Significant differences were identified at a threshold of p < 0.001 (p-value). To assess the magnitude of these significant differences, we calculated the effect size (η²) [ 53 ]. η² (eta-squared) is a measure of effect size that quantifies the proportion of variance in the dependent variable (rs-FC) that is explained by the independent variable (group: ADHD, BD, SZ, or HCs). For instance, η²=0.4 means that 40% of the variance in rs-FC can be attributed to group differences. Among the 992 functional connections between 34 ROIs of the procedural memory network in the studied patients, only those connections exhibiting significant differences compared to HCs were shown and reported in the results section.


## Results

Results indicated significant differences in specific rs-FC patterns within the procedural memory network between individuals with ADHD, BD, SZ, and HCs. To ensure that age differences did not confound our results, we compared the mean age of the four study groups using a one-way ANOVA. There were no significant differences in average age between groups ( p > 0.05).

The following sections provide a detailed analysis of the significant rs-FC differences ( p < 0.001) observed between patient groups and HCs, with accompanying figures to illustrate the findings.


## Rs-FC analysis in ADHD vs. HCs

Individuals with ADHD exhibited significantly elevated rs-FC between the Cereb3 r and Cereb45 l ( p = 0.000067) compared to HCs. Conversely, they demonstrated significantly decreased rs-FC between the Cereb1 l and the Cereb6 l ( p = 0.00091). Table 3 provided a detailed statistical analysis, including the significance level (p-value), the strength of rs-FC differences (t-test), and the effect size (η²) to offer a comprehensive understanding of these findings. The table categorizes results into instances where ADHD patients exhibited heightened (ADHD > HCs) or diminished (ADHD < HCs) rs-FC compared to HCs. Figures 2 and 3 visually depict the regions within the procedural memory network of ADHD patients that exhibited significantly elevated and reduced rs-FC between them, respectively, compared to HCs.

Table 3 Significant differences in rs-FC within the procedural memory network of ADHD patients compared to HCs. ( p < 0.001) Sign Connectivity Statistic (T test) p -value η² ADHD > HCs Cereb45 l – Cereb3 r 4.00 0.000067 0.53 ADHD < HCs Cereb1 l – Cereb6 l -3.13 0.00091 0.49


### Table 3: Significant differences in rs-FC within the procedural memory network of ADHD patients compared to HCs. ( p < 0.001)

| Sign | Connectivity | Statistic (T test) | p -value | η² |
| ADHD > HCs | Cereb45 l – Cereb3 r | 4.00 | 0.000067 | 0.53 |
| ADHD < HCs | Cereb1 l – Cereb6 l | -3.13 | 0.00091 | 0.49 |
Fig. 2 ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with increased rs-FC in ADHD patients compared to HCs. ( d ) Ring view of regions with increased rs-FC in ADHD patients compared to HCs. (ADHD > HCs)


> **Fig. 2:** ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with increased rs-FC in ADHD patients compared to HCs. ( d ) Ring view of regions with increased rs-FC in ADHD patients compared to HCs. (ADHD > HCs)

Fig. 3 ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with decreased rs-FC in ADHD patients compared to HCs. ( d ) Ring view of regions with decreased rs-FC in ADHD patients compared to HCs (ADHD < HCs)


> **Fig. 3:** ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with decreased rs-FC in ADHD patients compared to HCs. ( d ) Ring view of regions with decreased rs-FC in ADHD patients compared to HCs (ADHD < HCs)


## rs-FC analysis in BD vs. HCs

BD patients illustrated significantly increased rs-FC between the Claustrum r and Caudate r ( p = 0.000584), subthalamic nucleus r and Pallidum l ( p = 0.000604), substantia nigra l and Cereb2 l ( p = 0.000818), Cereb10 r and SMA r ( p = 0.000862), Cereb9 r and SMA l ( p = 0.000933) compared to HCs. Whilst, they displayed significantly reduced rs-FC between the subthalamic nucleus r and the Cereb6 l ( p = 0.000126), Cereb9 r and Cereb9 l ( p = 0.000329) compared to HCs. Table 4 presented a detailed statistical analysis of these differences. The table outlines the significance level (p-value), the strength of rs-FC differences (t-test), and the effect size (η²) to offer a comprehensive understanding of these findings. The table categorizes results into cases where BD patients exhibited higher (BD > HCs) or lower (BD < HCs) rs-FC compared to HCs. Figures 4 and 5 visually showed the regions within the procedural memory network of BD patients that exhibited significantly increased and reduced rs-FC between them, respectively, compared to HCs.

Table 4 Significant differences in rs-FC within the procedural memory network of BD patients compared to HCs. ( p < 0.001) Sign Connectivity Statistic (T test) p -value η² BD > HCs Claustrum r – Caudate r 3.35 0.00058 0.28 subthalamic nucleus r – Pallidum l 3.34 0.00060 0.21 substantia nigra l – Cereb2 l 3.24 0.00082 0.16 Cereb10 r – SMA r 3.22 0.00086 0.12 Cereb9 r – SMA l 3.20 0.00093 0.14 BD < HCs subthalamic nucleus r – Cereb6 l -3.80 0.00013 0.52 Cereb9 r – Cereb9 l -3.52 0.00033 0.32


### Table 4: Significant differences in rs-FC within the procedural memory network of BD patients compared to HCs. ( p < 0.001)

| Sign | Connectivity | Statistic (T test) | p -value | η² |
| BD > HCs | Claustrum r – Caudate r | 3.35 | 0.00058 | 0.28 |
| subthalamic nucleus r – Pallidum l | 3.34 | 0.00060 | 0.21 |
| substantia nigra l – Cereb2 l | 3.24 | 0.00082 | 0.16 |
| Cereb10 r – SMA r | 3.22 | 0.00086 | 0.12 |
| Cereb9 r – SMA l | 3.20 | 0.00093 | 0.14 |
| BD < HCs | subthalamic nucleus r – Cereb6 l | -3.80 | 0.00013 | 0.52 |
| Cereb9 r – Cereb9 l | -3.52 | 0.00033 | 0.32 |
Fig. 4 ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with increased rs-FC in BD patients compared to HCs. ( d ) Ring view of regions with increased rs-FC in BD patients compared to HCs. (BD > HCs)


> **Fig. 4:** ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with increased rs-FC in BD patients compared to HCs. ( d ) Ring view of regions with increased rs-FC in BD patients compared to HCs. (BD > HCs)

Fig. 5 ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with decreased rs-FC in BD patients compared to HCs. ( d ) Ring view of regions with decreased rs-FC in BD patients compared to HCs (BD < HCs)


> **Fig. 5:** ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with decreased rs-FC in BD patients compared to HCs. ( d ) Ring view of regions with decreased rs-FC in BD patients compared to HCs (BD < HCs)


## rs-FC analysis in SZ vs. HCs

SZ patients illustrated significantly increased rs-FC between the Caudate r and putamen l ( p = 0.000567). Whiles, they demonstrated significantly reduced rs-FC between the subthalamic nucleus r and the Cereb6 l ( p = 0.000063), Cereb1 r and subthalamic nucleus r ( p = 0.000628) compared to HCs. Table 5 presented a detailed statistical analysis of these differences. The table outlines the significance level (p-value), the strength of rs-FC differences (t-test), and the effect size (η²) to offer a comprehensive understanding of these findings. The table categorizes results into cases where SZ patients exhibited higher (SZ > HCs) or lower (SZ < HCs) rs-FC compared to HCs. Figures 6 and 7 visually indicated the regions within the procedural memory network of SZ patients that exhibited significantly increased and reduced rs-FC between them, respectively, compared to HCs.

Table 5 Significant differences in rs-FC within the procedural memory network of SZ patients compared to HCs ( p < 0.001) Sign Connectivity Statistic (T test) p -value η² SZ > HCs Caudate r– putamen l 3.35 0.00057 0.25 SZ < HCs subthalamic nucleus r – Cereb6 l -3.99 0.000063 0.51 Cereb1 r – subthalamic nucleus r -3.32 0.00063 0.0.19


### Table 5: Significant differences in rs-FC within the procedural memory network of SZ patients compared to HCs ( p < 0.001)

| Sign | Connectivity | Statistic (T test) | p -value | η² |
| SZ > HCs | Caudate r– putamen l | 3.35 | 0.00057 | 0.25 |
| SZ < HCs | subthalamic nucleus r – Cereb6 l | -3.99 | 0.000063 | 0.51 |
| Cereb1 r – subthalamic nucleus r | -3.32 | 0.00063 | 0.0.19 |
Fig. 6 ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with increased rs-FC in SZ patients compared to HCs. ( d ) Ring view of regions with increased rs-FC in SZ patients compared to HCs. (SZ > HCs)


> **Fig. 6:** ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with increased rs-FC in SZ patients compared to HCs. ( d ) Ring view of regions with increased rs-FC in SZ patients compared to HCs. (SZ > HCs)

Fig. 7 ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with decreased rs-FC in SZ patients compared to HCs. ( d ) Ring view of regions with decreased rs-FC in SZ patients compared to HCs (SZ < HCs)


> **Fig. 7:** ( a , b , and c ) 3D views of coronal, sagittal, and axial planes of the brain’s procedural memory network with decreased rs-FC in SZ patients compared to HCs. ( d ) Ring view of regions with decreased rs-FC in SZ patients compared to HCs (SZ < HCs)


## Discussion

To examine the brain function associated with cognitive networks in patients with ADHD, BD, and SZ, we identified distinct patterns of altered rs-FC within procedural memory network in each patient group using rs-fMRI and mRRC method, independent of any specific task. Given the roles of the brain’s procedural memory network regions, disruptions in their functional connectivity, such as increased or decreased connectivity, were associated with cognitive and behavioral impairments in ADHD, BD, and SZ [ 54 ]. In the following, we will elucidate the role of each ROI within the procedural memory network in cognitive networks. Subsequently, we will delve into rs-FC alterations between these ROIs and their potential implications for cognition in individuals with ADHD, BD, and SZ (Section ADHD , BD , and SZ ). The cerebellum, traditionally associated with motor control, is increasingly recognized for its pivotal role in various cognitive networks, including working memory and executive function, particularly in the visual-spatial domain [ 55 ]. The SMA, a part of the premotor cortex, plays a critical role in planning and executing complex movements, as well as in cognitive networks such as working memory and decision-making [ 56 , 57 ]. The Subthalamic nucleus and pallidum are key components of the basal ganglia, a group of brain structures involved in motor control, reward processing, and learning [ 58 ]. The Subthalamic nucleus is thought to play a role in inhibiting unwanted movements [ 59 ], while the pallidum is involved in regulating motor output [ 60 ]. The caudate and putamen are both components of the striatum [ 61 ], a key brain region involved in motor control, reward processing, and learning [ 62 ]. The caudate is thought to play a role in planning and initiating movements [ 63 ], while the putamen is involved in executing movements and regulating motor output [ 64 ]. The substantia nigra plays a multifaceted role in cognitive networks, regulating reward, motivation, movement, learning, and executive functions through its production of dopamine [ 65 ].


## ADHD

Patients with ADHD demonstrated decreased functional connectivity between Cereb1l and Cereb6l regions. This finding suggests potential disruptions in information transfer between these regions, which are implicated in cognitive processes [ 66 ]. These disruptions could contribute to the observed cognitive networks deficits in ADHD patients, such as impaired motor-cognitive integration, attentional problems, and executive function difficulties, particularly in visual-spatial tasks [ 67 ]. The rs-FC analysis performed in the ADHD sample closely aligned with previously published rs-FC analyses conducted by Jiang K and colleagues [ 68 ]. Furthermore, our analysis indicated increased functional connectivity between regions Cereb3 r and Cereb45 l, potentially reflecting hyperactive communication within the procedural memory network [ 69 ]. This aberrant connectivity pattern may contribute to the cognitive networks impairments experienced by ADHD patients, potentially leading to difficulties in task switching, attention, and working memory [ 49 , 50 ]. This finding is consistent with previous research indicating increased functional connectivity between cerebellar regions, which has been associated with cognitive network deficits, including working memory, in ADHD [ 70 – 72 ].


## BD

This study’s findings, examining rs-FC between the claustrum and caudate in BD patients, suggest potential mechanisms underlying several BD symptoms. The claustrum’s role in attention and emotion regulation [ 73 ] might be impaired due to its hyperconnectivity with the caudate, a brain region implicated in reward processing [ 74 ]. These findings align with the “default mode network” (DMN) hypothesis of BD, which suggests that individuals with BD exhibit aberrant activity in the DMN [ 75 ], a network of brain regions involved in introspection and self-referential thought [ 76 ]. Niccolò Zovetti et al.‘s study [ 77 ] demonstrated that BD is linked to alterations in the frontal and posterior DMN structures, primarily in the prefrontal, posterior, and inferior cingulate cortices. Given that the claustrum and caudate are both situated within the frontal region of the DMN, the findings of this study corroborate the potential involvement of these structures in BD. Moreover, the findings of this study, which examined rs-FC between the subthalamic nucleus and pallidum in BD patients, provide further support for the “reward circuit” hypothesis of BD. Increased rs-FC between these regions may contribute to several symptoms associated with the cognitive networks impairments, including motor disturbances [ 78 ]. These results are consistent with previous research [ 79 ] suggesting that disruptions in the basal ganglia, a key component of the reward circuit, can lead to cognitive network deficits in neuropsychiatric conditions. The hyperconnectivity observed in BD patients could potentially disrupt the balance of excitatory and inhibitory signals within the reward circuit, leading to difficulties in regulating emotions, motivation, and behavior [ 80 , 81 ]. Furthermore, the increased rs-FC between the cerebellum and SMA in BD patients could potentially contribute to several symptoms associated with the disorder. For example, the cerebellum’s involvement in emotion regulation and social cognition [ 82 , 83 ] might be affected by its hyper connectivity with the SMA, which is implicated in planning and executing movements [ 84 ]. These findings align with the “motor network” hypothesis of BD [ 85 ], which suggests that abnormalities in brain regions involved in motor control contribute to the development and maintenance of the disorder. Arshaq Saleem et al.‘s study [ 86 ] found that increased functional connectivity between sensory-motor areas is correlated with the intensity of both motor control and emotional experiences. This suggests that heightened connectivity in these regions may be a specific marker of mood state or a general indicator of disease severity. Also, the decreased rs-FC between the Subthalamic nucleus and cerebellum in BD patients could potentially contribute to several symptoms associated with the disorder. For example, the subthalamic nucleus, implicated in motor control and reward processing [ 78 ] might be affected by its reduced connectivity with the cerebellum, a region involved in motor coordination and cognitive network. This could lead to difficulties in regulating movements and emotional responses, which are common features of BD [ 82 , 83 ]. These findings align with the “motor network” and “reward circuit” hypotheses of BD, which suggest that abnormalities in brain regions involved in motor control and reward processing contribute to the development and maintenance of the disorder. Our findings of decreased rs-FC between the subthalamic nucleus and cerebellum in BD patients are consistent with previous research by Tao Wu et al., [ 87 ] which implicated disruptions in the motor network and reduced connectivity between these brain regions in Parkinson’s disease. These results suggest that similar mechanisms may underlie motor coordination and cognitive network deficits in both conditions. In addition, Interhemispheric communication within the cerebellum is essential for coordinating movements and maintaining balance [ 88 ]. The decreased rs-FC between the cerebellar hemispheres in BD patients might contribute to cognitive networks impairments associated with the disorder, including motor coordination difficulties and balance issues [ 89 ]. These findings align with the “motor network” hypothesis of BD, which suggests that abnormalities in brain regions involved in motor control contribute to the development and maintenance of the disorder. Our findings of decreased rs-FC between the cerebellar hemispheres in BD patients are consistent with previous research by Ying Wang et al., [ 90 ] which identified interhemispheric coordination deficits in individuals with BD. These results suggest that impaired communication between the two cerebellar hemispheres may contribute to the motor coordination, balance, and cognitive difficulties often observed in BD patients. This aligns with the “motor network” hypothesis, which posits that abnormalities in brain regions involved in motor control play a role in the development and maintenance of BD.


## SZ

Increased rs-FC between the caudate and putamen in SZ patients may contribute to hyperconnectivity within the striatum, potentially leading to difficulties in controlling motor behavior, such as motor tics or abnormal movements [ 91 ]. Moreover, given the striatum’s role in reward processing [ 92 ], altered rs-FC in this region could contribute to motivational deficits and anhedonia, which are common symptoms of SZ [ 93 ]. In a study by Mingjun Duan et al., [ 94 ] functional connectivity changes within the basal ganglia network of individuals with SZ were examined. They found that increased functional connections within this network were associated with symptoms such as impaired motor processing, cognitive network deficits, motivational difficulties, and emotional control issues. These findings align with our results. On the other hand, decreased rs-FC between the subthalamic nucleus and cerebellum in patients with SZ could contribute to symptoms such as impaired motor control, difficulties with reward processing, and cognitive network deficits [ 95 ]. These disruptions might lead to challenges in regulating movements and emotional responses, which are common characteristics of SZ [ 96 ]. Our findings of decreased rs-FC between the subthalamic nucleus and cerebellum in patients with SZ align with previous research by Hugo C. Baggio et al., [ 95 ] who demonstrated that deficits in motor, cognitive, and emotional networks in Parkinson’s and multiple system atrophy patients arise from impaired connectivity between these brain regions. This suggests that disruptions in the subthalamic nucleus-cerebellum circuit may underlie similar symptoms in SZ, such as impaired motor control, difficulties with reward processing, and cognitive network deficits.


## Limitations

While this study provides valuable insights into the neural correlates of ADHD, BD, and SZ, it is essential to acknowledge its limitations. The sample size, while sufficient for detecting significant group differences, may limit the generalizability of the findings to larger populations. Additionally, the focus on three specific disorders may not fully capture the heterogeneity of psychiatric conditions. Furthermore, despite a relatively balanced gender distribution in the overall sample, due to limited access to subjects, the gender distribution within each study subgroup was not completely balanced. This gender imbalance could potentially affect brain function and accurate comparisons between groups, as sex differences in brain structure and function are well-documented. Future research should address these limitations by: Enrolling larger and more diverse samples: This will increase statistical power and improve generalizability. Exploring a wider range of psychiatric disorders: This will provide a more comprehensive understanding of neural abnormalities across different conditions. Ensuring balanced gender distribution within subgroups: This will minimize the potential impact of sex differences on the findings. Employing advanced analysis techniques: Such as dynamic causal modeling [ 97 ] and asymmetrical functional connectivity [ 98 ], can provide more nuanced insights into brain network dynamics. By addressing these limitations, future studies can further advance our understanding of the neural mechanisms underlying psychiatric disorders and inform the development of more effective treatments.


## Conclusions

This study highlights the importance of the procedural memory network in cognitive networks and provides evidence for its involvement in the pathophysiology of ADHD, BD, and SZ. By examining rs-FC within the procedural memory network, we identified distinct patterns of altered connectivity in each patient group. These findings suggest that disruptions in the functional communication between key brain regions within this network play a significant role in the cognitive and behavioral networks deficits observed in these disorders. Future research can build upon these findings to develop targeted interventions aimed at improving cognitive networks in these disorders.


## Data availability

The data is publicly available, which means that anyone can access and use it. 10.18112/openneuro.ds000030.v1.0.0.