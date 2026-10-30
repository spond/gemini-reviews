# FEXP_ANON_147

## Abstract

This study investigates the phenolic compounds (PC), volatile compounds (VC), and fatty acids (FA) of extra virgin olive oil (EVOO) derived from the Turkish olive variety “Sarı Ulak”, along with ADMET, DFT, molecular docking, and gene network analyses of significant molecules identified within the EVOO. Chromatographic methods (GC-FID, HPLC) were employed to characterize FA, PC, and VC profiles, while quality parameters, antioxidant activities (TAC, ABTS, DPPH) were assessed via spectrophotometry. The analysis revealed a complex composition of 40 volatile compounds, with estragole, 7-hydroxyheptene-1, and 3-methoxycinnamaldehyde as the primary components. Hydroxytyrosol, tyrosol, oleuropein, apigenin, ferulic acid, and vanillic acid emerged as main phenolic constituents, with hydroxytyrosol and apigenin exhibiting high bioavailability. Molecular docking highlighted oleuropein and pinoresinol as compounds with strong binding affinities, though only hydroxytyrosol, apigenin, and pinoresinol fully met Lipinski and other drug-likeness criteria. DFT analysis showed that oleuropein and pinoresinol have notable dipole moments, reflecting polar and asymmetrical structures. KEGG enrichment analysis further linked key molecules like oleuropein and apigenin with pathways related to lipid metabolism and atherosclerosis, underscoring their potential bioactivity and relevance in health-related applications.


## Introduction

The olive tree ( Olea europaea L .), one of the earliest cultivated species, is predominantly found in Mediterranean countries, where Spain, Italy, Greece, and Turkey are among the leading producers. Extra virgin olive oil (EVOO), obtained from olive fruit by mechanical or physical processes it is considered the highest quality in olive oil classification due to its pleasant flavor and health benefits [ 1 – 3 ]. As it is derived directly from olives essentially pure olive juice-quality assessments of EVOO focus on components such as phenolic and pigment profiles, which contribute to its sensory attributes and pharmacological effects. Additionally, to be classified as EVOO, the oil must have a free acidity level no higher than 0.8% and must be free from sensory defects [ 1 – 3 ].

The positive health impacts of EVOO consumption, particularly in reducing cardiovascular and metabolic disease risk, are largely attributed to its fatty acid content and phenolic compounds [ 4 , 5 ]. Fatty acids, which make up ~ 97–99% of EVOO’s total weight, primarily include unsaturated fats like oleic acid, linoleic acid, and palmitoleic acid, along with around 14% saturated fats such as palmitic and stearic acids. The remaining fraction (1–3%) consists of bioactive compounds like phenols, phytosterols, tocopherols, and squalene [ 2 , 6 ]. Numerous studies have highlighted the antioxidant, antimicrobial, and anti-inflammatory properties of EVOO’s phenolic compounds, underscoring their significance in health-related research [ 7 ]. To date, at least 36 phenolic compounds have been identified in EVOO, with compositions varying from 0.02 to 600 mg kg −1 , influenced by factors like region, olive variety, genetic variations, environmental and climatic conditions, maturity at harvest, storage, and oil extraction methods [ 8 – 11 ]. Given the complex and variable composition of EVOO, advanced computational methods have become essential for accurately assessing and predicting the bioactivity of its diverse compounds.

Recent advancements in computational modeling, grounded in artificial intelligence (AI) and machine learning, have transformed research into chemical compound identification, target prediction, and toxicity assessment. Computational methods like virtual screening and molecular docking facilitate efficient drug discovery by reducing time and costs associated with experimental procedures. This shift allows researchers to screen for potential therapeutic agents, monitor drug efficacy, and explore drug repositioning strategies [ 12 – 14 ]. In EVOO studies, such approaches can provide insights into the bioactivity of particular compounds, allowing for more detailed analysis across varieties, geographical regions, and preparation conditions.

In this study, PC, VC, FA, antioxidant and antimicrobial analyzes of an EVOO obtained from a Turkish olive variety, as well as the evaluation of important molecules detected in EVOO with computer-based programs (ADMET, DFT, Molecular Docking and Gene network analysis) were performed. The olive oil evaluated in this study was first proven by laboratory findings to be EVOO. Then, it was supported by computer-based studies. This is an indication that the study is original. Previous studies on olive oil have predominantly been conducted on topics such as variety, growing conditions and authenticity. In this study, in addition to a comprehensive quality assessment of a characteristic EVOO of a common Turkish olive variety, the evaluation of its major phenolic compounds was also carried out using computer-based programs including ADMET, DFT, molecular docking and gene network analysis.


## Materials and methods


## Chemicals

The chemicals used were of analytical purity and the standards used (tyrosol, oleuropein, pinoresinol, caffeic acid, syringic acid, vanillic acid, p-coumaric acid, ferulic acid, gallic acid, luteolin, hydroxytyrosol, apigenin) were of high purity (purchased from Sigma-Alrich).


## Olive fruits

Olives of the Sarı Ulak variety were used in the EVOO production. The fruits of this olive were collected and purchased from a farmer's garden in Çakırlı Village. (Tarsus County, Türkiye). The geographical location of this garden is illustrated in Fig. 1 . The olives were harvested during the first week of November in the 2023 season and were classified as maturity level category 2, according to the International Olive Council (IOC, 2011) [ 15 ]. At this maturity stage, one side of the olive changes from yellow to pink or reddish. Approximately 100 kg of olives were harvested and transported to the olive oil mill facility for processing on the same day. Fig. 1 The location of the olive garden of Sarı Ulak variety used for the EVOO


> **Fig. 1:** The location of the olive garden of Sarı Ulak variety used for the EVOO


## Extraction of EVOO

EVOO was extracted using a boutique-scale olive oil mill (SLN-OLV200 Machine, Selni Makina, Istanbul, Turkey). This machine was designed to perform leaf-sorting, washing, crushing, malaxation, decantation and separation processes. In addition, its malaxator had a closed system that could hold the nitrogen gas pressed into it. Nitrogen gas can prevent quality defects by minimizing oxidation in the olive oil during the malaxation process. In the extraction of EVOO, malaxation process was at 26 ± 1 °C for 30 min. The EVOO taken from the separator was placed in 100 ml amber bottles and stored at 4 °C until analysis.


## Quality parameters analysis in EVOO

FFA, PV and extinction coefficients (K 270 and K 232 ) of the EVOO were measured according to the Turkish Official Methods (2014). FFA and PV were expressed as % oleic acid and meq O 2 kg −1 , respectively [ 3 , 16 ].


## Extraction of phenolic compounds (PC)

PCs in the EVOO were extracted according to the method of the International Olive Council (COI/T.20/DocNo29/ Rev.1, 2017) with a slight modifications. A 3 g of oil sample was weighed into a 12 mL tube. Then, 3 mL of methanol (80%), 1.5 mL of hexane and 0.5 mL of syringic acid (60 ppm) (internal standard (IS) were added to the tube. The mixture was vortexed for 30 s and centrifuged at 5000 rpm and 10 ºC for 5 min. The methanolic lower phase was transferred to another tube and the extraction was repeated two more times. After that, the lower phases were combined and washed twice with 3 mL hexane, and the hexane phase was removed from the top. The obtained phenolic extract was used in PC, TPC, TAC and ABTS analysis [ 17 ].


## Total phenolic content (TPC) and total antioxidant capacity (TAC) analysis

TPC of the sample was determined using the Folin-Ciocalteu method as described by Çapanoğlu et al. [ 18 ].

The results were calculated using a calibration curve created with solutions prepared at different concentrations of the gallic acid standard and expressed as mg gallic acid equivalent per 100 g sample. Determination of TAC of sample was performed using the DPPH radical scavenging capacity and carried out according to method of Osei et al. [ 19 ], with some modifications. The results were expressed as mg trolox equivalent (TE) per 100 g of sample.


## ABTS radical scavenging activity

ABTS Radical Scavenging Activity of the samples was determined according to the method used by Schlesier et al. [ 20 ], and expressed as mg trolox equivalents (TE) per 100 g sample.


## Determination of fatty acid (FA) composition by GC-FID

Approximately 100 mg of olive oil sample was shaken well by adding 10 mL of hexane to it. To obtain FAMEs, 0.5 mL of 2 M KOH dissolved in methanol was added to this mixture and then swirled for 20 s. The oil composition in the samples was analyzed using a gas chromatography flame ionization detector (GC-FID) system (Shimadzu QP2020, Shimadzu Corp., Japan) coupled with an Rtx-2330 capillary column (0.20 μm, 60 m × 0.25 mm, Restek, Bad Homburg, Germany). After 2 h of dark soaking, 1 μL of the solution was injected into the GC in split mode (1:100). The detector and injection port temperature was set at 250 °C and helium (at a flow rate of 1 mL/min) was used as the carrier gas. Peak designations and relative percentages of their fields were calculated using FAMEs' mixing standards [ 3 , 16 ].


## Determination of phenolic compounds by HPLC

PC in samples were analyzed using a Water Alliance e2695 HPLC system (Waters, Milford, MA, USA) consisting of a photodiode array detector (PDA) (Waters 2996, Milford, MA, USA) and an inertSustain C18 column (5 μm, 4.6 × 250 mm, GL Sciences, Tokyo, Japan). The phenolic extract was filtered through a 0.45 μm polyvinylidine fluoride (PVDF) syringe filter before injection into the HPLC system. The analysis conditions of HPLC were performed as described by Veneziani et al. with minor modifications. Results are expressed in mg kg −1 . [ 4 , 21 ].


## Determination of VC using SPME–GC–MS

VCs in samples were determined by solid-phase microextraction (SPME) followed by the use of a gas chromatography-mass detector (GC–MS) (Shimadzu QP2020 brand, Kyoto, Japan) system connected to an autosampler (AOC 5000 Plus). The method was modified as described by Genovese et al. and Korkmaz et al. [ 3 , 22 ].


## Sensory analysis of EVOO

A sensory panel of ten trained evaluators from the Central Laboratory of Artuklu University Mardin (Mardin, Türkiye) evaluated the samples in accordance with the Turkish Official Methods adapted to the IOC procedure. Positive characteristics (fruitiness, bitterness and burning) and defects (moldy, musty-smelling, wine-vinegar-like) were quantitatively determined by marking on the original profile sheet between 0 (no perception) and 10 (highest density) cm. The results were expressed as median values of the evaluators' perception scores [ 3 , 16 , 17 ].


## Determination of antimicrobial activity of EVOO

Escherichia coli ATCC 11229, Klebsiella aerogenes ATCC 13048, Pseudomonas aeruginosa ATCC 9027, Klebsiella pneumoniae ATCC 13883 were purchased from Microbiologics. Disk Diffusion method was applied to determine antimicrobial activity. (NCCLS 1997). Microorganisms taken from fresh culture were incubated in nutrient broth (NB) liquid medium at 37 °C until 0.5 Mc Farland (1.5 × 108 Kob/mL) turbidity occurred. Turbidity control was performed in a spectrophotometer at a wavelength of 625 nm with absorbances of 0.08–0.10. 100 μL of the cultured test microorganisms were taken and spread on nutrient agar solid medium. Then, 15 μL of each of the oils was impregnated on sterile discs placed in the transplanted petries. Inhibition zone diameters were measured for Escherichia coli , Klebsiella aerogenes, Klebsiella pneumoniae, Pseudomonas aeruginosa, bacteria after 24 h of incubation at 37 °C. Each test was performed in 3 repetitions at different times. Sulbactam/ampicillin (SAM) (20 μg) antibiotic discs were used as positive controls [ 23 , 24 ].


## Network-based pharmacology

Predicted targets of Hydroxytyrosol, oleuropein, pinoresinol and apigenin were obtained from a Swiss Target Prediction ( http://www.swisstargetprediction ). To identify the mutual targets of compounds we employed InteractiVenn online tool [ 25 ].


## Gene network analysis: gene enrichment analysis

We used ClusterProfiler, an ontology-based tool that offers three methods for gene classification and enrichment analyses: groupGO, richGO and richKEGG. ClusterProfiler provides a better understanding of the high-level functions of biological systems by comparing gene sets through biological term classification and enrichment analyses. This package presents a method called groupGO to classify genes according to a specific level of the GO ontology and performs enrichment tests for GO terms and Kyoto Encyclopedia of Genes and Genomes (KEEG) paths based on hypergeometric distribution. Q values are also calculated so as not to keep the false discovery rate (FDR) high. In addition, ClusterProfiler offers a comparison function called CompareCluster, which automatically calculates the enriched functional categories of each set of genes, and various visualization methods [ 26 , 27 ].


## Molecular modeling studies


## Ligand system

Hydroxytyrosol, oleuropein, pinoresinol and apigenin were retrieved from the PubChem ( https://pubchem.ncbi.nlm.nih.gov ) database in sdf format and converted to pdb format from the Open Babel GUI program (Table 1 ). Table 1 Major compounds found in EVOO and cardiovascular drugs for docking studies No. Molecule/drugs Formula Compound ID 1 Hydroxytyrosol C 8 H 10 O 3 82755 2 Oleuropein C 25 H 32 O 13 5281544 3 Pinoresinol C 20 H 22 O 6 73399 4 Apigenin C 15 H 10 O 5 5280443 Cardiovasculer (atherosclerosis/coronary artery diseases) drugs 5 Losartan C 22 H 23 ClN 6O 3961 6 Lisinopril C 21 H 31 N 3 O 5 5362119


### Table 1: Major compounds found in EVOO and cardiovascular drugs for docking studies

| No. | Molecule/drugs | Formula | Compound ID |
| 1 | Hydroxytyrosol | C 8 H 10 O 3 | 82755 |
| 2 | Oleuropein | C 25 H 32 O 13 | 5281544 |
| 3 | Pinoresinol | C 20 H 22 O 6 | 73399 |
| 4 | Apigenin | C 15 H 10 O 5 | 5280443 |
| Cardiovasculer (atherosclerosis/coronary artery diseases) drugs |
| 5 | Losartan | C 22 H 23 ClN 6O | 3961 |
| 6 | Lisinopril | C 21 H 31 N 3 O 5 | 5362119 |

## Protein system

A total of seven proteins that cause cardiovascular diseases were selected by literature review (Table 2 ). The crystal structures of these proteins are available in the Protein Data Bank ( www.rcsb.org ). All polar hydrogens were added using the Discovery Studio 2020 modeling package to reduce the tension of the crystal structures and make the proteins usable in the Autodock simulation. The resulting structure was minimized in a vacuum environment; During minimization, the hydrogens were allowed to move while the heavy atoms were kept stable in their crystal coordinates. Proteins and ligands were prepared with the Autodocktools graphical user interface program; Gasteiger charges were calculated, and nonpolar hydrogens were combined with carbon atoms. The pdbqt files created for macromolecules were saved [ 28 ]. Table 2 Targeted receptor proteins associated with Atherosclerosis along with structure No. Target proteins Disease PDB ID Structure 1 Angiotensin converting enzyme (Atherosclerosis/coronary artery diseases) 1O8A 2 Human angiotensin receptor (Atherosclerosis/coronary artery diseases) 4YAY


### Table 2: Targeted receptor proteins associated with Atherosclerosis along with structure

| No. | Target proteins | Disease | PDB ID | Structure |
| 1 | Angiotensin converting enzyme | (Atherosclerosis/coronary artery diseases) | 1O8A |  |
| 2 | Human angiotensin receptor | (Atherosclerosis/coronary artery diseases) | 4YAY |  |

## Molecular modeling

Data entry for modeling was created using the AutoDockTools (Autodock 4.2.6) program. In all models, a cube was formed consisting of squares with dimensions of 80 × 80 × 80 in the x, y, z directions. For energy calculations, an approach based on a distance of 0.375 Å (about a quarter of the length of the carbon–carbon covalent bond) and a dielectric constant was adopted. The simulations, which were carried out using the Lamarckian genetic algorithm, were carried out with a study time of 10 times. Randomly placed fragments were simulated with 50 breakpoints, a maximum energy of 2.5 × 10 6 , and a maximum occurrence of 2.7 × 10 4 . The mutation rate was set at 2% and the genetic crossover rate was set at 80%. By combining the results with a mean root square deviation (RMSD) of less than 0.5 Å, the structures with the best binding energy were determined as the final complex structures. Using the Autodock Vina 1.1.2 and Discovery Studio 2020 programs, the optical spectra in EVOO and ligand–protein interactions were investigated for active regional localization studies [ 29 , 30 ].


## ADME and ADMET

A new type of tool known as in silico ADME evaluation model has been developed to assist medical pharmacologists and chemists in pioneering discovery, development and optimization processes. SwissADME web server commonly used to predict the pharmacokinetics and drug-likeness properties of various substances ( http://www.swissadme.ch/ ) [ 31 ]. Toxicity and metabolism estimation analysis was calculated using the ADMETlab 2.0 website. https://admetmesh.scbdd.com/service/evaluation/cal . [ 32 ].


## Density functional theory analysis

Gaussian 09 software and GaussView 5.0 software were performed to carry out geometry optimization technique using DFT-based quantum chemistry simulations (B3LYP with a 6–311++ G(d,p) [ 33 ]. The ∆E value was calculated between LUMO and HOMO. The other calculated parameters were softness (s), the dipole moment (μ) hardness (η) and electronegativity (χ) [ 34 – 42 ]: 1 \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\Delta = E_{LUMO} - E_{HOMO} ,$$\end{document} Δ = E LUMO - E HOMO , 2 \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$A= -{E}_{LUMO},$$\end{document} A = - E LUMO , 3 \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$I= -{E}_{HOMO},$$\end{document} I = - E HOMO , 4 \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\eta = \frac{1}{2}(I - A),$$\end{document} η = 1 2 ( I - A ) , 5 \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$s = \frac{1}{\eta },$$\end{document} s = 1 η , 6 \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\chi = \frac{1}{2}(I + A).$$\end{document} χ = 1 2 ( I + A ) .

The obtained identifiers for quantum compounds were shown in Table 16 . It was discovered that this cholesterol had an energy gap of 3.187 eV, a E LUMO of − 0.607 eV and a E HOMO of − 3.794 eV.It's been proven that cholesterol has potent adsorption properties. Because of this, the cholesterol molecule is a good option for a chelating agent. The molecule's computed quantum values for hardness electronegativity, and softness were 2.200 eV, 0.628 eV −1 , and 1.594 eV, respectively. The E HOMO and E LUMO indicate the electron-giving and receiving abilities of molecules. As a result, a molecule's adsorption strength rises with a lower ∆E value and its stability increases with a bigger molecular energy gap. The strength of the dipole moment (1.9001 D), which can change the dielectric properties of the double electric layer, increases the probability of cholesterol sticking. Because of its large dipole moment, cholesterol functions as a ligand for biological processes. The most common use for it is to calculate the electronegativity ( χ ) of compounds that gain or lose electrons. Electron attraction gets easier when a molecule's electronegativity increases. Greater global hardness ( η ) was suggested to make charge transfer between molecules more difficult.


## Results and discussion

In this study, PC, VC, FA, TAC, ABTS analyzes of an EVOO obtained from a Turkish olive variety and ADMET, DFT, Molecular Docking and Gene network analysis of important molecules detected in EVOO were evaluated with computer-based programs. In addition, FFA, PV, K232 and K270 parameters were considered in the quality classification of EVOO. PV, K232, K270 are indicators for determining the level of oxidation in lipids, while FFA is considered a measure of enzymatic hydrolysis of lipids. Quality parameters are also affected by the degree of maturity of the olive, the extraction conditions used in oil production and the olive variety [ 3 , 43 , 44 ] The FFA, PV, K232 and K270 values of our study were 0.76 ± 0.02%, 17.61 ± 2.10 meq O 2 ·kg −1 , 1.24 ± 0.03, 0.176 ± 0.05, respectively. As shown in Table 3 , FFA, PV, K232 and K270 values were among the recommended values [ 43 ]. When the quality parameters of our study were examined, the recorded values were consistent with the findings of previous studies [ 45 , 46 ]. These parameters show that the oil meets quality standards and is high quality EVOO. High FFA values suggest that the oil has degraded or that the processing process has not attained a sufficient level of quality. Conversely, the FFA value of our study is low, suggesting that the oil is of high quality. A high peroxide value, K232 and K270 indicate that the oil has progressed in the oxidation process and its quality has decreased. If the FFA value is low, it can be interpreted that the oil is protected from enzymatic degradation, the PV value is within the recommended limits, the oxidation level of the oil is acceptable, and the K232 and K270 values are low, the oil is fresh and the oxidation level is low. Table 3 Legal quality parameters in the EVOO of Sarı Ulak Olives Parameter Mean ± SD FFA (% Oleic acid) 0.76 ± 0.02 PV (meq O 2 . kg −1 ) 17.61 ± 2.10 K232 1.24 ± 0.03 K270 0.176 ± 0.05 For EVOO; FFA (% oleic acid): Recommended ≤ 0,8; PV (meq O 2 kg −1 ); Recommended ≤ 20 K232: Recommended ≤ 2.50; K270: Recommended ≤ 0.22


### Table 3: Legal quality parameters in the EVOO of Sarı Ulak Olives

| Parameter | Mean ± SD |
| FFA (% Oleic acid) | 0.76 ± 0.02 |
| PV (meq O 2 . kg −1 ) | 17.61 ± 2.10 |
| K232 | 1.24 ± 0.03 |
| K270 | 0.176 ± 0.05 |
When the fatty acid findings of our study were examined, oleic acid (%71.85 ± 3.6), palmitic acid (%11.70 ± 1.9) Linoleic Acid (%9.00 ± 1.4), Stearic acid (%3.01 ± 0.8), Palmiteloic Acid (%0.73 ± 0.10), α-Linolenic acid (%0.58 ± 0.009), Palmiteloic Acid (%0.73 ± 0.10), Heptadecanoic acid (%0.152 ± 0.07), Cis-10-Heptadecanoic acid (%0.23 ± 0.08), Arachidic Acid (%0.45 ± 0.8), 11-Eicosenoic acid (%0.27 ± 0.06), Behenic Acid (%0.11 ± 0.05), Tricosanoic acid (%1.18 ± 0.1), Palmiteloic Acid (%0.731 ± 0.09), PUFAs (%9.58 ± 1.49), MUFAs (%73.81 ± 3.93) were recorded (Table 4 ). In the literature, EVOO major component content was Oleic acid (63.1–79.7%), Palmitic acid value (9.4–19.5%), Linoleic Acid (6.6–14.8%), Stearic acid (1.4–3.0%), Palmiteloic Acid (0.6–3.2%), α-Linolenic acid (0.46–0.69%), PUFAs (7.0–15.5%), MUFAs (65.2–80.8%). The values are examined, all of the results we obtained fall within the expected literature range, when the olive oil obtained from Sariulak olives is evaluated in general, it possesses practically all of the legal quality characteristics and fatty acid profile of EVOO [ 2 , 47 , 48 ]. Oleic Acid and MUFA levels indicate that olive oil has a healthy fatty acid profile and meets quality standards in addition; levels of saturated fatty acids such as Palmitic Acid, Stearic Acid indicate that olive oil has a balanced fatty acid profile and is within quality limitations. Along with EVOO's rich and complex chemical profile, which includes more than 200 compounds, it is widely appreciated for its high nutritional value and largely proven nutritional properties. In particular, the Oleic acid forms MUFAs are the primary constituents of EVOO [ 48 , 49 ]. Examining the main chemicals of EVOO in the present investigation reveals the results are largely consistent with previous research [ 44 ]. EVOO polyphenols have the ability to directly clean free radicals and break radical chains, as well as increase enzymatic endogenous antioxidant defense [ 50 ]. In this study, DPPH and ABTS radical scavenging activity values were converted to IC50. While the DPPH value was (IC50: 413.5 ± 217), the ABTS value was (IC50: 211.8 ± 16.2) (Table 5 ). The results suggest that EVOO has good free radical scavenging properties and high radical chain breaking capacity. The consumption of EVOO, which is the typical source of lipids in the cuisine of Mediterranean countries and especially one of the important representatives of the Mediterranean diet, is associated with a reduced risk of various chronic diseases such as diabetes, hypertension, obesity, cancer diseases and cardiovascular diseases (CVD) [ 51 – 53 ]. The burden of atherosclerotic cardiovascular illnesses, responsible for the majority of fatalities globally and have emerged as a major issue, must be reduced. It is specifically associated with the rise in atherosclerotic risk factors, which are linked to developing and advancement of cardiovascular disorders. Although risk factors were previously under control in many high-income countries, this disease, which is becoming an issue in low-income countries, is gradually losing ground in prevention even in high-income countries [ 54 , 55 ]. By 2030, the direct cost of CVD treatment in the U.S. is projected to reach one trillion U.S. dollars. However, a healthy life will significantly reduce the burden and complications of atherosclerosis [ 56 , 57 ]. Table 4 Fatty acid profile (%) of EVOO obtained from Sarı Ulak Olives Oleic acid (C18:1) 71.85 ± 3.6 Palmitic acid (C16:0) 11.70 ± 1.9 Linoleic acid (C18:2) 9.00 ± 1.4 Stearic acid (C18:0) 3.01 ± 0.8 Alpha-linolenic acid (C18:3) 0.58 ± 0.09 Palmiteloic acid (C16:1) 0.73 ± 0.10 Heptadecanoic acid (C17:0) 0.152 ± 0.07 Cis-10-heptadecanoic acid (C17:1) 0.23 ± 0.08 Arachidic acid (C20:0) 0.45 ± 0.8 11-eicosenoic acid (C20:1) 0.27 ± 0.06 Behenic acid (C22:0) 0.11 ± 0.05 Tricosanoic acid (C23:0) 1.18 ± 0.1 Palmiteloic acid (C16:1) 0.731 ± 0.09 SFAs 16.60 ± 3.72 PUFAs 9.58 ± 1.49 MUFAs 73.81 ± 3.93 MUFAs/PUFAs 7.70 ± 2.6 For EVOO: Palmitic acid:7.5 to 20.0; Palmitoleic acid: 0.3 to 3.5; Heptadecanoic: ≤ 0.3; Heptadecenoic acid: ≤ 0.3; Stearic acid: 0.5 to 5.0 ; Oleic acid: 55.0 to 83.0; Linoleic acid: 3.5 to 21. 0. Arachidic Acid: Recommended ≤ 0.6; Behenic Acid: Recommended ≤ 1.0; Linolenic acid: Recommended ≤ 1.0; Results are expressed as Mean ± SD (standard deviation) (n = 3) SFA saturated fatty acids, PUFA Polyunsaturated fatty acids, MUFAs Monounsaturated fatty acids Table 5 DPPH and ABTS activity of EVOO Mean ± SD DPPH (IC50) 413.5 ± 217 ABTS (IC50) 211.8 ± 16.2 Results are expressed as mean ± SD (standard deviation) (n = 3)


### Table 4: Fatty acid profile (%) of EVOO obtained from Sarı Ulak Olives

| Oleic acid (C18:1) | 71.85 ± 3.6 |
| Palmitic acid (C16:0) | 11.70 ± 1.9 |
| Linoleic acid (C18:2) | 9.00 ± 1.4 |
| Stearic acid (C18:0) | 3.01 ± 0.8 |
| Alpha-linolenic acid (C18:3) | 0.58 ± 0.09 |
| Palmiteloic acid (C16:1) | 0.73 ± 0.10 |
| Heptadecanoic acid (C17:0) | 0.152 ± 0.07 |
| Cis-10-heptadecanoic acid (C17:1) | 0.23 ± 0.08 |
| Arachidic acid (C20:0) | 0.45 ± 0.8 |
| 11-eicosenoic acid (C20:1) | 0.27 ± 0.06 |
| Behenic acid (C22:0) | 0.11 ± 0.05 |
| Tricosanoic acid (C23:0) | 1.18 ± 0.1 |
| Palmiteloic acid (C16:1) | 0.731 ± 0.09 |
| SFAs | 16.60 ± 3.72 |
| PUFAs | 9.58 ± 1.49 |
| MUFAs | 73.81 ± 3.93 |
| MUFAs/PUFAs | 7.70 ± 2.6 |

### Table 5: DPPH and ABTS activity of EVOO

|  | Mean ± SD |
| DPPH (IC50) | 413.5 ± 217 |
| ABTS (IC50) | 211.8 ± 16.2 |
Atherosclerosis begins with lipid deposits in the arterial intima, developing into a chronic inflammatory disease associated with myocardial infarction and stroke [ 54 , 58 ]. This process involves the buildup of LDL-cholesterol and the activation of endothelial cells, which promotes inflammation [ 59 ]. EVOO supports the reduction of atherosclerotic risk through its anti-inflammatory, antioxidant, and vasodilatory effects [ 60 ]. Extensive evidence highlights the cardiovascular benefits of EVOO, extending beyond cholesterol reduction to include a variety of mechanisms. Its high nutritional value is due to a complex profile of over 200 compounds, with key contributions from oleic acid and polyphenols that are instrumental in preventing cardiovascular diseases [ 49 , 61 ]. Notable phenolic components in EVOO include hydroxytyrosol, tyrosol, oleuropein, and a variety of phenolic acids, flavones, and lignans [ 62 ]. The examination of phenolic compounds demonstrated that, Hydroxytyrosol (2.33 ± 0.1 mg kg −1 ), Oleuropein (0.357 ± 0.01 mg kg −1 ), Pinoresinol (0.115 ± 0.05 mg kg −1 ), Apigenin (0.23 ± 0.08 mg kg −1 ), Tyrosol (0.106 ± 0.04 mg kg −1 ), Vanillic acid (0.059 ± 0.010 mg kg −1 ), p-Qumaric acid (0.045 ± 0.008 mg kg −1 ), t-Ferrulic acid (0.080 ± 0.009 mg kg −1 ), Caffeic acid (0.059 ± 0.007 mg kg −1 ), Total Phenolic Content (92.75 ± 5.9 mg GAE·kg −1 ) (Table 6 ). According to many studies, these effects in EVOO are largely due to the main secoiridoid derivatives such as oleuropein, oleocanthal, and oleacein. Additionally, simple phenols like hydroxytyrosol and tyrosol have been linked to a wide range of health-promoting effects, including antioxidant, anti-inflammatory, cardioprotective, neuroprotective, anticancer, antidiabetic, anti-obesity, antisteatotic, antimicrobial, etc. [ 63 – 65 ]. It is a monoterpene derivative of cyclopentane and consists of oleuropein, aglycon and glycoside, which has a bitter taste [ 66 ]. Oleuropein, a hydroxytyrosol ester containing an oleosidic skeleton and a carbohydrate group, has a beneficial effect on various aspects of cardiovascular disease through its vasodilator, anti-platelet aggregation, anti-inflammatory, anticancer, and antioxidant properties [ 67 , 68 ]. High amounts of tyrosol and hydroxytyrosol, the main phenolic compounds found in EVOOs, are found in the earliest harvest sample, while tyrosol and hydroxytyrosol concentrations decrease with increasing olive ripeness [ 69 ]. Hydroxytyrosol’s potential in preventing and reducing cardiovascular risk factors has shown that, especially at higher doses in both in vitro and in vivo studies, it positively influences lipid profiles, plaque formation, and inflammatory processes following treatment [ 70 ]. Tyrosol is protective against cardiovascular diseases, as Tyrosol is effective in maintaining cellular antioxidant defenses through intracellular accumulation despite its weak antioxidant activity, which is in favor of olive oil consumption [ 71 ]. Apigenin prevents cardiovascular diseases through anti-apoptotic and antioxidant mechanisms in cardiomyocytes and vascular endothelial cells [ 72 ]. Table 6 Phenolic compounds (mg kg −1 ) of EVOO obtained from Sarı Ulak Olives Phenolic compound Mean ± Std Hydroxytyrosol 2.33 ± 0.11 Oleuropein 0.357 ± 0.01 Pinoresinol 0.115 ± 0.05 Apigenin 0.23 ± 0.08 Tyrosol 0.106 ± 0.04 Vanillic acid 0.059 ± 0.010 p -Qumaric acid 0.045 ± 0.008 t -Ferrulic acid 0.080 ± 0.009 Caffeic acid 0.059 ± 0.007 Total phenolic content (mg GAE·kg −1 ) 92.75 ± 5.9


### Table 6: Phenolic compounds (mg kg −1 ) of EVOO obtained from Sarı Ulak Olives

| Phenolic compound | Mean ± Std |
| Hydroxytyrosol | 2.33 ± 0.11 |
| Oleuropein | 0.357 ± 0.01 |
| Pinoresinol | 0.115 ± 0.05 |
| Apigenin | 0.23 ± 0.08 |
| Tyrosol | 0.106 ± 0.04 |
| Vanillic acid | 0.059 ± 0.010 |
| p -Qumaric acid | 0.045 ± 0.008 |
| t -Ferrulic acid | 0.080 ± 0.009 |
| Caffeic acid | 0.059 ± 0.007 |
| Total phenolic content (mg GAE·kg −1 ) | 92.75 ± 5.9 |
VC profile of EVOOs is responsible for their odor and has a key role in their sensory quality [ 73 ]. VC responsible for the characteristic EVOO aroma are formed generally by enzymatic and chemical oxidation during processing [ 74 ]. The composition of (VC) in EVOO of Sarı ulak olive are given in Table 7 . A total of 40 volatile compounds were identified in the sample, including 6 terpenoids, 7 aldehydes, 7 alcohols, 5 esters, 2 ketones, 5 alkanes, 3 alkenes and 5 miscellaneous. Many of these compounds have also been reported from olive oil in several previous studies [ 3 , 74 ]. The both number and content of VC in olive oils depends mainly on the variety as well as growing, processing and storage conditions [ 75 ]. Compounds C6 (hexanal, 1-hexanol, 3-(Z)-hexenol, and 2-(E)-hexenol) and C5 (1-penten-3-ol, 2-(Z)-pentenol) which are responsible for the typical aroma of the oil, were also detected in the EVOO sample in this study. These molecules are generated from linoleic and α-linolenic acids via the lipoxygenase pathway and contribute to the pleasant odor of olive oil. Previous research has also identified these chemicals in EVOOs [ 76 , 77 ]. However, as an interesting finding, (E)−2-hexenal (almond, green), one of the compounds found in most olive oils in previous studies and responsible for the characteristic olive oil aroma, was not detected in EVOO from Sarı Ulak olive in this study. On the other hand, estragole (38.94%), 7-hydroxyheptene-1 (10.48%) and 3-methoxycinnamaldehyde (12.98%) were quantitatively identified as the major compounds in the sample. To our knowledge, estragole and 7-hydroxyheptene-1 have not been reported in any olive oil before. The abundant presence of these compounds can be attributed to the characteristics of the olive variety. Terpenoid compounds 1,8-cineole, δ-carene, (E)-phytol and farnesene, which contribute to the positive aroma of olive oil, were also found in the sample. These findings imply that the chemical components of this olive, and hence the characteristic aroma of olive oil, might change significantly depending on the olive variety, growing conditions, and processing procedures. Nevertheless, some compounds that cause aroma defects, such as ethanol (winey), 2-methylbutanol (fusty) and (E)−2-heptenal (rancid), were also found in the EVOO sample. Among tehese, the first two generated due to microbial activity, while the last one occurs based on lipid autoxidation [ 78 ]. Table 7 Relative concentration (% area) of volatile compounds in EVOO of Sarı Ulak Olives No. Compound a RI b Relative percentage (%) c Terpenoids 3.38 1 1,8-Cineole 1225 0.33 2 δ-Carene 1267 0.43 3 (E)−4,8-Dimethyl-1,3,7-nonatriene 1318 0.33 4 Farnesene 1754 0.54 5 (E)-Phytol 1972 1.21 6 Rosifoliol 2243 0.53 Aldehydes 22.13 7 Pentanal 1027 0.33 8 Hexanal 1115 7.24 9 (E)−2-Pentenal 1155 0.29 10 (E)−2-Heptenal 1338 0.34 11 Nonanal 1403 0.41 12 (E,E)−2,4-Heptadienal 1474 0.54 13 3-Methoxycinnamaldehyde 1790 12.98 Alcohols 6.80 14 Ethanol 989 0.71 15 1-Penten-3-ol 1181 0.67 16 2-Methylbutanol 1223 0.34 17 2-(Z)-pentenol 1329 0.37 18 1-Hexanol 1360 1.63 19 3-(Z)-Hexenol 1390 2.19 20 2-(E)-Hexenol 1411 0.88 Esters 3.81 21 Methyl acetate 907 0.34 22 Ethyl Acetate 949 0.63 23 Hexyl acetate 1289 0.49 24 (4E)−4-Hexenyl acetate 1333 1.74 25 Methyl cinnamate 2095 0.60 Ketones 1.69 26 3-Pentanone 1026 1.28 27 6-Methyl-5-Hepten-2-One 1351 0.41 Alkanes 3.15 28 2,4-Dimethylhexane 868 1.17 29 1-Methoxyhexane 1003 0.70 30 2,2,4,6,6-Pentamethylheptane 1009 0.28 31 Cyclohexane 1273 0.28 32 Hexatriacontane 2189 0.73 Alkenes 13.41 33 Z-1-Methoxy-3-hexene 1048 0.27 34 7-Hydroxyheptene-1 1238 10.48 35 1-Tetradecene 1255 2.65 Miscellaneous 45.63 36 3-Ethyl-1,5-octadiene 1050 0.60 37 Estragole 1684 38.94 38 1,5,9,9-Tetramethyl-1,4,7-cycloundecatriene 1784 0.61 39 Anethole 1842 1.88 40 Methyleugenol 2018 3.61 a Compounds were identified by comparing their mass spectra with those in MS libraries (NIST11 and Wiley9) b RI, Retention indices (Calculated on DB-HeavyWax capilary column) c %, The ratio of the peak area of each compound to the total area of all peaks in the chromatogram obtaind from GC–MS (results were calculated as the average of three replicates)


### Table 7: Relative concentration (% area) of volatile compounds in EVOO of Sarı Ulak Olives

| No. | Compound a | RI b | Relative percentage (%) c |
| Terpenoids |  |  | 3.38 |
| 1 | 1,8-Cineole | 1225 | 0.33 |
| 2 | δ-Carene | 1267 | 0.43 |
| 3 | (E)−4,8-Dimethyl-1,3,7-nonatriene | 1318 | 0.33 |
| 4 | Farnesene | 1754 | 0.54 |
| 5 | (E)-Phytol | 1972 | 1.21 |
| 6 | Rosifoliol | 2243 | 0.53 |
| Aldehydes |  |  | 22.13 |
| 7 | Pentanal | 1027 | 0.33 |
| 8 | Hexanal | 1115 | 7.24 |
| 9 | (E)−2-Pentenal | 1155 | 0.29 |
| 10 | (E)−2-Heptenal | 1338 | 0.34 |
| 11 | Nonanal | 1403 | 0.41 |
| 12 | (E,E)−2,4-Heptadienal | 1474 | 0.54 |
| 13 | 3-Methoxycinnamaldehyde | 1790 | 12.98 |
| Alcohols |  |  | 6.80 |
| 14 | Ethanol | 989 | 0.71 |
| 15 | 1-Penten-3-ol | 1181 | 0.67 |
| 16 | 2-Methylbutanol | 1223 | 0.34 |
| 17 | 2-(Z)-pentenol | 1329 | 0.37 |
| 18 | 1-Hexanol | 1360 | 1.63 |
| 19 | 3-(Z)-Hexenol | 1390 | 2.19 |
| 20 | 2-(E)-Hexenol | 1411 | 0.88 |
| Esters |  |  | 3.81 |
| 21 | Methyl acetate | 907 | 0.34 |
| 22 | Ethyl Acetate | 949 | 0.63 |
| 23 | Hexyl acetate | 1289 | 0.49 |
| 24 | (4E)−4-Hexenyl acetate | 1333 | 1.74 |
| 25 | Methyl cinnamate | 2095 | 0.60 |
| Ketones |  |  | 1.69 |
| 26 | 3-Pentanone | 1026 | 1.28 |
| 27 | 6-Methyl-5-Hepten-2-One | 1351 | 0.41 |
| Alkanes |  |  | 3.15 |
| 28 | 2,4-Dimethylhexane | 868 | 1.17 |
In order to provide the best possible information to the consumer thanks to sensory analyzes other than chemical and physical analysis, the oils are usually labeled as Dense/robust, medium or sensitive/light according to their properties. In the method used, fruitiness, bitterness and pungency (intensity/positive/positive) and Moldy, winey-vinegary (imperfect/negative) quantitative density are given a value between 0 (no perception) and 10 (highest intensity). (Median, Sturdy > 6; when the median of the middle feature is between 3 and 6; when the median of the feature is Precision < less than 3.0). [ 79 , 80 ]. In sensory analysis, EVOO needs to show a fruity note higher than 0 and, more importantly, a median of zero defects [ 81 ]. It was evaluated by a trained sensory panel/tasters consisting of ten evaluators from the Central Research Laboratory of Mardin Artuklu University (Mardin, Türkiye) in tasting sessions of four samples at approximately 15-min intervals, according to the Turkish Official Methods (2014), adapted from the IOC (2018) procedure. The obtained data was entered into the computer [ 3 , 16 , 80 ] When the sensory analysis results were examined, it had positive characteristics such as Fruitness (3.5 ± 0.49), Bitterness (3.8 ± 0.28), Pungency (3.25 ± 0.63). When the negative traits were examined, the quantitative intensity of Winey-vinegary, Fusty, Musty was 0 (Table 8 ). Examples of EVOO; It did not show antimicrobial effects in E .coli, K. pneumoniae, K. aerogenes bacteria . On P. aeruginosa , it produced an inhibition diameter of 8.0. Compared to 20 μg sulbactam/ampicillin antibiotic, 15μL of olive oil showed an inhibition effect of 69.57% (Table 9 ; Fig. 2 ). The fact that it does not show antimicrobial effects in bacteria such as E. coli, K. pneumoniae and K. aerogenes indicates that olive oil is ineffective against these bacteria, while this indicates that olive oil does not have an overall antimicrobial activity against all bacterial pathogens. On the contrary, it can be said that this olive oil provides a noticeable inhibition effect on P. aeruginosa , but its effect is limited. It can be interpreted that olive oil provides a similar effect on P. aeruginosa as antibiotics, but the effect may be less potent. Table 8 Sensory properties of EVOO obtained from Sarı Ulak Olives Scores of sensory attributes of EVOO obtained from Sarıulak olive Mean ± Std Fruitness 3.5 ± 0.49 Bitterness 3.8 ± 0.28 Pungency 3.25 ± 0.63 Winey-vinegary – Fusty – Musty – Table 9 Antimicrobial analysis results (inhibitions zone diamaters ± SD) E.coli K. pneumoniae P. aeruginosa K. aerogenes SAM 11.5 ± 0.7 EVOO – – 8.0 ± 0.0 – Fig. 2 Antimicrobial demonstration of EVOO obtained from Sarı Ulak Olives


### Table 8: Sensory properties of EVOO obtained from Sarı Ulak Olives

| Scores of sensory attributes of EVOO obtained from Sarıulak olive | Mean ± Std |
| Fruitness | 3.5 ± 0.49 |
| Bitterness | 3.8 ± 0.28 |
| Pungency | 3.25 ± 0.63 |
| Winey-vinegary | – |
| Fusty | – |
| Musty | – |

### Table 9: Antimicrobial analysis results (inhibitions zone diamaters ± SD)

|  | E.coli | K. pneumoniae | P. aeruginosa | K. aerogenes |
| SAM |  |  | 11.5 ± 0.7 |  |
| EVOO | – | – | 8.0 ± 0.0 | – |

> **Fig. 2:** Antimicrobial demonstration of EVOO obtained from Sarı Ulak Olives

Gene network analysis helps us understand cellular signal transduction and regulatory processes in a systematic way by identifying biological interactions between genes. It describes how a group of genes interact with each other to form a functional module, and how different gene modules are linked to each other [ 82 ]. Target gene predictions of bioactive important compounds in EVOO were extracted, and common gene associations of pinoresinol, apigenin, hydroxytyrosol, and oleuporein were found to be more frequent (Fig. 3 ). It implies that these compounds can affect similar biological pathways and exert a joint effect on these pathways. The frequent occurrence of co-gene associations may suggest that these compounds are involved in the same or similar cellular processes, for example, that they may exhibit joint effects on antioxidant defense, inflammation modulation, or cellular signaling pathways. With these common genes, a relationship was established between lipids and atherosclerosis in KEGG enrichment analysis. The Swiss Taregt prediction web tool was used to predict the target genes for each of EVOO's major molecules. The Venn diagram (Fig. 3 ) is depicted to analyze the genes shared for each of the major molecules of EVOO. CA3, TYR, CA14, CA9, ADORA1, ADORA2A, CA1, CA6, CA2, CA12, CA7, and PARP1 have been shown to frequently be shared between apigenin, hydroxytyrosol, and oleuropein. The KEGG enrichment analysis conducted with these 12 genes revealed the relationships between apigenin, hydroxytyrosol, and oleuropein—compounds targeted in our study—and lipids and atherosclerosis (Figs. 3 , 4 , 5 ). These data imply that the main compounds of EVOO, such as apigenin, hydroxytyrosol, and oleuropein, could potentially exert protective or regulatory effects on lipid metabolism and atherosclerosis through these genes. It also supports that these components may have beneficial effects on cardiovascular health, especially in processes such as lipid metabolism and regulation of atherosclerosis. Fig. 3 Venn diagram of the intersection between targets of each of Hydroxytyrosol, oleuropein, pinoresinol and apigenin target genes Fig. 4 Venn diagram of the intersection between targets of each of Hydroxytyrosol, oleuropein, pinoresinol and apigenin target genes list Fig. 5 KEGG enrichement analysis of Hydroxytyrosol, oleuropein, pinoresinol and apigenin


> **Fig. 3:** Venn diagram of the intersection between targets of each of Hydroxytyrosol, oleuropein, pinoresinol and apigenin target genes


> **Fig. 4:** Venn diagram of the intersection between targets of each of Hydroxytyrosol, oleuropein, pinoresinol and apigenin target genes list


> **Fig. 5:** KEGG enrichement analysis of Hydroxytyrosol, oleuropein, pinoresinol and apigenin

As a result of gene enrichment analysis, pinoresinol, apigenin, hydroxytyrosol and oleuporin were inserted into lipid and atherosclerosis-targeting protein structures (PDB ID: 1O8A and 4YAY) by molecular docking method. In the comparison of pinoresinol, apigenin, hydroxytyrosol and oleuporin compounds, lisinopril for 1O8A and losartan for 4YAY were used as the standard. When molecular docking for 1O8A was examined, apigenin (−8.5 kcal/mol) had a better binding score than pinoresinol and oleuropein lisinopril. Oleuropein showed good binding score in 1O8A protein structure. When molecular docking for YAY was examined, Hydroxytyrosol (− 5.9 kcal/mol), Oleuropein (− 7.8 kcal/mol), Apigenin (− 8.2 kcal/mol) had lower binding scores than Losartan. Pinoresinol (− 8.5 kcal/mol) showed a higher binding score than other molecules in the 4YAY protein structure and equal binding score with Losartan (Fig. 6 and Table 10 ). The hydrophobic and hydrogen bond interactions of apigenin, hydroxytyrosol, oleuropein, Pinoresinol and CVD inhibitors, which are important in drug targets, are given in Table 11 and Fig. 7 . Angiotensin converting enzyme (ACE, PDB ID:1O8A) is important component of renin–angiotensin–aldosterone system (RAAS), which converts angiotensin I to angiotensin II and is expressed in many different cell types [ 83 ]. Changes in ACE function have been associated with CVDs such as CAD, HF, and hypertension in previous studies [ 84 ]. Angiotensin II Type I Receptor (AT1R, PDB ID: 4YAY), which involved in cellular proliferation, apoptosis, fibrosis and inflammation is a member of the G protein-coupled receptor family that regulates RAAS signal transduction [ 85 – 87 ]. AT1R causes atherosclerosis through Angiotensin II-led inflammation in pathological conditions, and AT1R blockers are essential components of the treatment of coronary atherosclerosis [ 58 , 88 – 91 ]. Fig. 6 Molecular Docking patterns of Hydroxytyrosol, oleuropein, pinoresinol, apigenin, cardiovasculer inhibitors in target proteins structures Table 10 Docking score of Hydroxytyrosol, oleuropein, pinoresinol, apigenin, and cardiovascular inhibitors against their target protein receptors Molecule 1O8A 4YAY Hydroxytyrosol − 6.0 kcal/mol − 5.9 kcal/mol Oleuropein − 8.7 kcal/mol − 7.8 kcal/mol Pinoresinol − 8.3 kcal/mol − 8.5 kcal/mol Apigenin − 8.5 kcal/mol − 8.2 kcal/mol Inhibitors − 7.0 kcal/mol − 8.5 kcal/mol Lisinopril Losartan Docking score was expressed in kcal/mol Table 11 H-bond and hydrophobic interaction between high binding score compounds and receptor Target Protein Hydroxytyrosol H-bond Hydroxytyrosol Hydrofobic Oleuropein H-bond Oleuropein Hydrofobic Pinoresinol H-bond Pinoresinol hydrofobic 1O8A TYR62, PRO515, SER516 ASN85, ARG124, LEU139, LEU140 ASN66, ASN70, HIS353, ALA354, ALA356, ASP358, HIS387, TYR394, HIS410, HIS513 – HIS353, ALA354, SER422, ASP453, VAL379, VAL380, HIS383, MET450, TYR523 Apigenin H-bond Apigenin Hydrofobic Cardiovasculer Inhibitors H-bond Cardiovasculer Inhibitors Hydrofobic GLY404 LYS118, MET223, GLU403, PRO407, PHE570 ASN277, GLN281 HIS383, VAL379 Target Protein Hydroxytyrosol H-bond Hydroxytyrosol Hydrofobic Oleuropein H-bond Oleuropein Hydrofobic Pinoresinol H-bond Pinoresinol Hydrofobic 4YAY TYR62, ASN66, GLU143 ASN85 ALA21, TYR35, PRO285 ILE288 ASP281 TRP84, TYR92, VAL108, ILE288 Apigenin H-bond Apigenin Hydrofobic Cardiovasculer Inhibitors H-bond Cardiovasculer Inhibitors Hydrofobic – TRP84, VAL108, ALA181, MET284, ILE288 Fig. 7 Discovery Studio structure showing interactions between Hydroxytyrosol, oleuropein, pinoresinol, apigenin, cardiovasculer inhibitors and target proteins


> **Fig. 6:** Molecular Docking patterns of Hydroxytyrosol, oleuropein, pinoresinol, apigenin, cardiovasculer inhibitors in target proteins structures


### Table 10: Docking score of Hydroxytyrosol, oleuropein, pinoresinol, apigenin, and cardiovascular inhibitors against their target protein receptors

| Molecule | 1O8A | 4YAY |
| Hydroxytyrosol | − 6.0 kcal/mol | − 5.9 kcal/mol |
| Oleuropein | − 8.7 kcal/mol | − 7.8 kcal/mol |
| Pinoresinol | − 8.3 kcal/mol | − 8.5 kcal/mol |
| Apigenin | − 8.5 kcal/mol | − 8.2 kcal/mol |
| Inhibitors | − 7.0 kcal/mol | − 8.5 kcal/mol |
| Lisinopril | Losartan |

### Table 11: H-bond and hydrophobic interaction between high binding score compounds and receptor

| Target Protein | Hydroxytyrosol H-bond | Hydroxytyrosol Hydrofobic | Oleuropein H-bond | Oleuropein Hydrofobic | Pinoresinol H-bond | Pinoresinol hydrofobic |
| 1O8A | TYR62, PRO515, SER516 | ASN85, ARG124, LEU139, LEU140 | ASN66, ASN70, HIS353, ALA354, ALA356, ASP358, HIS387, TYR394, HIS410, HIS513 | – | HIS353, ALA354, SER422, ASP453, | VAL379, VAL380, HIS383, MET450, TYR523 |
| Apigenin H-bond | Apigenin Hydrofobic |  |  | Cardiovasculer Inhibitors H-bond | Cardiovasculer Inhibitors Hydrofobic |
| GLY404 | LYS118, MET223, GLU403, PRO407, PHE570 |  |  | ASN277, GLN281 | HIS383, VAL379 |
| Target Protein | Hydroxytyrosol H-bond | Hydroxytyrosol Hydrofobic | Oleuropein H-bond | Oleuropein Hydrofobic | Pinoresinol H-bond | Pinoresinol Hydrofobic |
| 4YAY | TYR62, ASN66, GLU143 | ASN85 | ALA21, TYR35, PRO285 | ILE288 | ASP281 | TRP84, TYR92, VAL108, ILE288 |
| Apigenin H-bond | Apigenin Hydrofobic |  |  | Cardiovasculer Inhibitors H-bond | Cardiovasculer Inhibitors Hydrofobic |
|  |  |  |  | – | TRP84, VAL108, ALA181, MET284, ILE288 |

> **Fig. 7:** Discovery Studio structure showing interactions between Hydroxytyrosol, oleuropein, pinoresinol, apigenin, cardiovasculer inhibitors and target proteins

Physicochemical properties and predictions about ADME are based on drug similarity rules. In our study, Oleuropein failed to pass the rule with three violations (MW > 500, NorO > 10, NHorOH > 5), Ghose (MW > 480, WLOGP < −0.4) with two violations, and Egan (TPSA > 131.6) with one violation. Hydroxytyrosol only had a violation of the Ghose rule (MW < 160). Hydroxytyrosol passed the full set of Lipinski, Veber, Egan. There were no violations of Apigenin and Pinoresinol. He completely passed all the rules. Hydroxytyrosol has an H-bond acceptor value of 3, and H-bond acceptors value is 3, while Rotatable bonds value is 2. Oleuropein has an H-bond donor value of 6, and H-bond acceptors value is 13, and Rotatable bonds value is 11. Apigen's H-bond acceptors value is 3, and H-bond acceptors value is 5, and Rotatable bonds value is 1. Pinoresinol H-bond donors have a value of 2, and H-bond acceptors value is 4, and Rotatable bonds value is 4. A radar map was created to evaluate and compare the molecules of Hydroxytyrosol, Apigenin, Oleuropein, Pinoresinol using six physicochemical properties such as size, lipophilicity, polarity, solubility, saturation and elasticity. The region shown in the diagram corresponds to the optimal range of values of each parameter. In the diagrams provided, Apigenin exhibited an optimal range (shown in pink area) for all criteria except Insatu (Saturation), while Oleuropein was outside the optimal range for Size, Polarity, and Flexibility. Hydroxytyrosol and Pinoresinol were within an optimal range for all criteria in the diagrams provided (Fig. 8 ). Hydroxytyrosol, Apigenin, Pinoresinol, Oleuropein showed Log Po/w (XLOGP3) values below 5; this suggests good permeability and absorption across the cell membrane. Furthermore, The solubility of a molecule is an important factor that plays a huge role in the absorption of the compound in the formulation process. Hydroxytyrosol, Apigenin, Pinoresinol exhibited 55% oral bioavailability. While this value was acceptable, Oleuropein exhibited a low value, i.e. 11% oral bioavailability (Table 12 ). In the light of these findings, it shows that Hydroxytyrosol, Apigenin and Pinoresinol are more advantageous in terms of pharmacokinetics and may be more suitable candidates in the drug development process. But Oleuropein's large size, low solubility, and bioavailability may make it pharmacologically disadvantageous. The lowest Synthetic accessibility value is Hydroxytyrosol, and the highest Synthetic accessibility value is the highest Oleuropein, the closer this value is to 1, the easier it can be synthesized, while the closer to 10, the more difficult it is to synthesize [ 31 ]. Log S (ESOL: Estimating Aqueous Solubility) is the in silico estimation of the aqueous solubility of molecules, including the effect of the topological polar surface area. The Log S scale value ranges from −10. (insoluble), −6 (poorly soluble), −4 (soluble), −2 (very soluble) and 0 (very soluble) [ 92 , 93 ]. The TPSA value is expected to be between 20 and 130 Å2. The only Oleuropein ((201.67 Å 2 ) molecule that did not fit this TPSA value range was [ 31 ]. Fig. 8 Radar map of Hydroxytyrosol ( A ), Oleuropein ( B ), Apigenin ( C ), Pinoresinol ( D ) molecules taken from Swissadme database (the pink area shows the optimal range for each property (lipophilicity: XLOGP3 between − 0.7 and + 5.0, Size: MW between 150 and 500 g/mol, polarity: TPSA between 20 and 130 Å2, solubility: log S not higher than 6, Saturation: fraction of carbons in the sp3 hybridization not less than 0.25, and Flexibility: no more than 9 rotatable bonds Table 12 Predictive models parameters Hydroxytyrosol Oleuropein Apigenin Pinoresinol Physicochemical properties Molecular Weight 154.16 g/mol 540.51 g/mol 270.24 g/mol 358.39 g/mol Formula C8H10O3 C25H32O13 C15H10O5 C20H22O6 Rotatable bonds 2 11 1 4 H-bond acceptors 3 13 5 6 H-bond donors 3 6 3 2 Molar Refractivity 41.42 127.28 73.99 94.90 Topological polar surface area (TPSA) 60.69 Å 2 201.67 Å 2 90.90 Å 2 77.38 Å 2 Lipophilicity Log Po/w (XLOGP3) − 0.72 − 0.45 3.02 2.28 Log P o/w (WLOGP) 0.63 − 0.63 2.58 2.54 Log P o/w (MLOGP) 0.60 − 1.34 0.52 1.17 Solubility Log S (ESOL) − 0.61 − 2.30 − 3.94 − 3.58 Solubility (water) 3.75e + 01 mg/ml; 2.43e−01 mol/l 2.72e + 00 mg/ml; 5.03e−03 mol/l 3.07e−02 mg/ml; 1.14e−04 mol/l 9.52e−02 mg/ml; 2.66e−04 mol/l Class Very soluble Soluble Soluble Soluble Druglikeness Lipinski (RO5) Yes; 0 violation No; 3 violations: MW > 500, NorO > 10, NHorOH > 5 Yes; 0 violation Yes; 0 violation Ghose No; 1 violation: MW < 160 No; 2 violations: MW > 480, WLOGP < −0.4 Yes Yes Veber Yes No; 2 violations: Rotors > 10, TPSA > 140 Yes Yes Egan Yes No; 1 violation: TPSA > 131.6 Yes Yes Bioavailability Score 0.55 0.11 0.55 0.55 Leadlikness Synthetic accessibility 1.08 6.22 2.96 3.99


> **Fig. 8:** Radar map of Hydroxytyrosol ( A ), Oleuropein ( B ), Apigenin ( C ), Pinoresinol ( D ) molecules taken from Swissadme database (the pink area shows the optimal range for each property (lipophilicity: XLOGP3 between − 0.7 and + 5.0, Size: MW between 150 and 500 g/mol, polarity: TPSA between 20 and 130 Å2, solubility: log S not higher than 6, Saturation: fraction of carbons in the sp3 hybridization not less than 0.25, and Flexibility: no more than 9 rotatable bonds


### Table 12: Predictive models parameters

|  | Hydroxytyrosol | Oleuropein | Apigenin | Pinoresinol |
| Physicochemical properties | Molecular Weight | 154.16 g/mol | 540.51 g/mol | 270.24 g/mol | 358.39 g/mol |
| Formula | C8H10O3 | C25H32O13 | C15H10O5 | C20H22O6 |
| Rotatable bonds | 2 | 11 | 1 | 4 |
| H-bond acceptors | 3 | 13 | 5 | 6 |
| H-bond donors | 3 | 6 | 3 | 2 |
| Molar Refractivity | 41.42 | 127.28 | 73.99 | 94.90 |
| Topological polar surface area (TPSA) | 60.69 Å 2 | 201.67 Å 2 | 90.90 Å 2 | 77.38 Å 2 |
| Lipophilicity | Log Po/w (XLOGP3) | − 0.72 | − 0.45 | 3.02 | 2.28 |
| Log P o/w (WLOGP) | 0.63 | − 0.63 | 2.58 | 2.54 |
| Log P o/w (MLOGP) | 0.60 | − 1.34 | 0.52 | 1.17 |
| Solubility | Log S (ESOL) | − 0.61 | − 2.30 | − 3.94 | − 3.58 |
| Solubility (water) | 3.75e + 01 mg/ml; 2.43e−01 mol/l | 2.72e + 00 mg/ml; 5.03e−03 mol/l | 3.07e−02 mg/ml; 1.14e−04 mol/l | 9.52e−02 mg/ml; 2.66e−04 mol/l |
| Class | Very soluble | Soluble | Soluble | Soluble |
| Druglikeness | Lipinski (RO5) | Yes; 0 violation | No; 3 violations: MW > 500, NorO > 10, NHorOH > 5 | Yes; 0 violation | Yes; 0 violation |
| Ghose | No; 1 violation: MW < 160 | No; 2 violations: MW > 480, WLOGP < −0.4 | Yes | Yes |
| Veber | Yes | No; 2 violations: Rotors > 10, TPSA > 140 | Yes | Yes |
| Egan | Yes | No; 1 violation: TPSA > 131.6 | Yes | Yes |
| Bioavailability Score | 0.55 | 0.11 | 0.55 | 0.55 |
| Leadlikness | Synthetic accessibility | 1.08 | 6.22 | 2.96 | 3.99 |
Inhibition and induction of CYPs are among the main mechanisms that cause pharmacokinetic drug-drug interactions, and CYP1A2, CYP2C19, CYP3A4, CYP2C9 and CYP2D6 are important CYPs preferred especially in silico assays [ 94 , 95 ]. Hydroxytyrosol and Oleuropein were not inhibitors for CYP1A2, CYP2C19, CYP2C9, CYP2D6 and CYPA4. Apigenin and Pinoresinol were inhibitors for CYP2D6, CYP3A4. Apigenin alone was inhibitory for CYP1A (Table 13 ). The fact that Apigenin and Pinoresinol inhibit the enzymes CYP2D6 and CYP3A4 indicates that these compounds could potentially interact with other drugs. In addition, the fact that Apigenin is an inhibitor of CYP1A requires careful use, especially with drugs that this enzyme metabolizes. Hydroxytyrosol is synthetically a more readily accessible compound, has good aqueous solubility, and has a low risk of pharmacokinetic interactions. On the contrary, Oleuropein is synthetically harder, has low aqueous solubility, and limited bioavailability. Apigenin and Pinoresinol should be carefully evaluated for potential drug-drug interactions as they can inhibit some CYP enzymes. These findings provide important insights into how Apigenin and Pinoresinol should be addressed in the pharmaceutical development process. Table 13 The interaction of hydroxytyrosol, oleuropein, apigenin, pinoresinol with cytochromes P450 isoforms predicted using SwissADME Pharmacokinetics parameters Hydroxytyrosol Oleuropein Apigenin Pinoresinol Pharmacokinetics GI absorption High Low High High BBB permeant No No No Yes P-gp substrate No Yes No Yes CYP1A2 inhibitor No No Yes No CYP2C9 inhibitor No No No No CYP2C19 inhibitor No No No No CYP3A4 inhibitor No No Yes Yes CYP2D6 inhibitor No No Yes Yes Log Kp (skin permeation) − 7.75 cm/s − 9.92 cm/s − 5.80 cm/s − 6.87 cm/s GI (HIA) human gastrointestinal absorption, BBB blood–brain barrier permeation, P-gp permeability glycoprotein, Log Kp the skin permeability coefficient


### Table 13: The interaction of hydroxytyrosol, oleuropein, apigenin, pinoresinol with cytochromes P450 isoforms predicted using SwissADME

| Pharmacokinetics parameters | Hydroxytyrosol | Oleuropein | Apigenin | Pinoresinol |
| Pharmacokinetics | GI absorption | High | Low | High | High |
| BBB permeant | No | No | No | Yes |
| P-gp substrate | No | Yes | No | Yes |
| CYP1A2 inhibitor | No | No | Yes | No |
| CYP2C9 inhibitor | No | No | No | No |
| CYP2C19 inhibitor | No | No | No | No |
| CYP3A4 inhibitor | No | No | Yes | Yes |
| CYP2D6 inhibitor | No | No | Yes | Yes |
|  | Log Kp (skin permeation) | − 7.75 cm/s | − 9.92 cm/s | − 5.80 cm/s | − 6.87 cm/s |
Since the study of ADME pharmacokinetics (absorption, distribution, metabolism, excretion) is an important factor in the development of drugs, it saves drug development time costs and supports experimental studies [ 96 ]. In our study, except for Oleuropein, Hydroxytyrosol, Apigenin, Pinoresinol were well absorbed because their gastrointestinal absorption (GI) was high. In addition, Pinoresinol appears to be able to cross the blood–brain barrier (Table 14 ). To evaluate the absorption property of Hydroxytyrosol, Oleuropein, Apigenin, Pinoresinol substrate or inhibitor (P-gpinh/P-gpsub), Caco-2-Permeability, human intestinal absorption (HIA) was estimated. 20% bioavailability (F20) and 30% bioavailability (F30) are as presented (Table 14 ). A positive value of F20 and F30 means that a compound is bioavailable up to 20% and 30% in the human body. The fact that the values are negative means that they cannot be used biologically. The F20 and F30 value of Hydroxytyrosol, Apigenin are positive. Oleuropein F20 is low negative, while F30 value is high positive. When looking at pinoresinol, both F20 and F30 values show high negative properties. Negative means a low oral bioavailability. Caco-2 cells are used to analyze how a molecule penetrates it Caco-2 permeability Hydroxytyrosol (− 4.43 cm/s), Oleuropein (− 5.8 cm/s), Apigenin (− 4.84 cm/s), Pinoresinol (− 4.79 cm/s). The increase of high negative Caco-2 mainly means that it has the potential to provide their permeability (Table 14 ). Hydroxytyrosol has a low negative value, indicating that this compound can pass through the intestine relatively well, while Oleuropein has a more negative value than other compounds, which can be interpreted as having lower permeability. Table 14 Absorption, distribution and excretion parameters of the Hydroxytyrosol, Oleuropein, Apigenin, Pinoresinol Molecule Absorption Distribution Excretion Caco-2 Pgp inh Pgp sub HIA F20 F30 PPB (%) BBB VD T1/2 TCL Hydroxytyrosol − 4.43 − − − − + + + + + + + + 35.53 − − 1.12 0.9 17.2 Oleuropein − 5.8 − − + + + + + − + + + 74.00 + 0.56 0.83 2.5 Apigenin − 4.84 − − + + − − + + + + + + 97.25 − − 0.51 0.85 7.02 Pinoresinol − 4.79 − − − − − − − − − − 94.77 – 1.05 0.43 7.89


### Table 14: Absorption, distribution and excretion parameters of the Hydroxytyrosol, Oleuropein, Apigenin, Pinoresinol

| Molecule | Absorption | Distribution | Excretion |
|  | Caco-2 | Pgp inh | Pgp sub | HIA | F20 | F30 | PPB (%) | BBB | VD | T1/2 | TCL |
| Hydroxytyrosol | − 4.43 | − − | − − | + + | + + + | + + + | 35.53 | − − | 1.12 | 0.9 | 17.2 |
| Oleuropein | − 5.8 | − − | + + | + + + | − | + + + | 74.00 | + | 0.56 | 0.83 | 2.5 |
| Apigenin | − 4.84 | − − | + + | − − | + + + | + + + | 97.25 | − − | 0.51 | 0.85 | 7.02 |
| Pinoresinol | − 4.79 | − − | − − | − − | − − | − − | 94.77 | – | 1.05 | 0.43 | 7.89 |
Hydroxytyrosol, Oleuropein, Apigenin and Pinoresinol HIA data were categorically represented as 0 and 1. HIA values are Hydroxytyrosol (+ +), Oleuropein (+ + +), Apigenin (− −) and Pinoresinol (− −), F20 values are Hydroxytyrosol (+ + +), Oleuropein (−), Apigenin (+ + +) and Pinoresinol (−−), F30 values are Hydroxytyrosol (+ + +), Oleuropein (+ + +), Apigenin (+ + +) and Pinoresinol (− −). When the HIA values are examined, it can be interpreted that Hydroxytyrosol and Oleuropein have a good absorption potential in the intestines, while Apigenin and Pinoresinol have a low absorption potential in the intestine. Hydroxytyrosol and Apigenin F20 and F30 values are positive when examined. This means that compounds can bioavailable in the human body at a rate of 20% and 30%, meaning that these compounds have a good bioavailability potential when taken orally. However, the Oleuropein F20 value is low negative, which indicates that the 20% bioavailability is quite low, while the high positive F30 value means that the potential to reach 30% bioavailability is high. This suggests that the bioavailability of Oleuropein may increase depending on dose or intake conditions. When we looked at pinoresinol, both F20 and F30 values were found to be highly negative, which means that pinoresinol will have very low bioavailability after oral ingestion and cannot be bioused in the body. PPB states that the effectiveness of a drug is related to how much it binds to proteins in the blood plasma. When the drug is less bound to proteins, it can pass or diffuse through cell membranes more effectively (Table 14 ) [ 97 ]. Since absorption and distribution affect each other, if the human body cannot easily absorb a drug, the distribution of the drug will also be poor [ 98 ]. The T1/2 half-life is defined as the time it takes for the plasma concentration of a drug to decrease by 50%. More than 30 min is considered a good half-life value. Hydroxytyrosol T1/2 value is 0.9, VD value is 1.12, Oleuropein T1/2 value is 0.83, VD value is 0.56, Apigenin T1/2 is 0.85, VD value is 0.510, Pinoresinol T1/2 value is 0.43, VD value is 1.052. A high VD value indicates that the drug is distributed more into tissue, while a low VD value indicates that the drug remains mostly in the plasma. In this case, we can say that Hydroxytyrosol and Pinoresinol have a wider distribution in the body. Since the whole is under 3.0 h, the drugs have a low T1/2, which indicates that the drug is removed from the human body at a reasonable rate. T1/2 depends on the rate constant (k), which is associated with VD and purge (CL). The CL values of Hydroxytyrosol, Oleuropein, Apigenin, Pinoresinol are 17.2, 2.5, 7.02, 7.89, respectively. The lowest is Oleuropein, while the highest is Hydroxytyrosol [ 99 , 100 ].

Below 5 mL/min/kg means that the renal clearance rate is low. These parameters are interconnected as the slower the CL, the longer the T1/2. Only Oleuropein shows this property [ 98 ]. Oleuropein has the lowest CL value, indicating that this drug will stay in the body longer and be cleared more slowly. We can say that hydroxytyrosol has the highest clearance rate and hence is eliminated from the body the fastest. However, Oleuropein's low CL value and relatively long T1/2 value suggest that this drug may stay in the body for a longer period of time and therefore exert longer-lasting effects. In particular, Oleuropein's low CL and relatively long T1/2 value may be clinically advantageous. Oleuropein, Pinoresinol, Apigenin, Hydroxytyrosol Toxicity and Metabolism Predictive Analyses were examined. The hERG encodes the pore-forming subunit of the rapidly activated delayed rectifier potassium channel, which is important for cardiac action potential repolarization. Dysfunction of these ion channels causes cardiac arrhythmias and sudden death. When the findings were examined, the hERG values of Hydroxytyrosol, Oleuropein, Apigenin, Pinoresinol were not significant (Table 15 ). [ 101 , 102 ]. Table 15 Toxicity parameters of the hydroxytyrosol, oleuropein, apigenin, pinoresinol Toxicity Environmental toxicity Toxicophore rules Molecule hERG H-HT AMES Tox SkinSen - DILI Carcinogencity IGC50 LC50FM LC50DM Acute toxicity rule Genotoxic carcinogenicity rule Hydroxytyrosol − − − − + + + − − – 3.03 3.29 4.26 0 Alert(s) 0 Alert(s) Oleuropein − − – + + − − + + + + + + 3.52 4.5 5.38 0 Alert(s) 1 Alert(s) Apigenin − − − − – + + + + + – 4.58 5.20 5.20 0 Alert(s) 0 Alert(s) Pinoresinol − − – – + – – 5.02 5.80 6.63 0 Alert(s) 0 Alert(s)


### Table 15: Toxicity parameters of the hydroxytyrosol, oleuropein, apigenin, pinoresinol

|  | Toxicity | Environmental toxicity | Toxicophore rules |
| Molecule | hERG | H-HT | AMES Tox | SkinSen - | DILI | Carcinogencity | IGC50 | LC50FM | LC50DM | Acute toxicity rule | Genotoxic carcinogenicity rule |
| Hydroxytyrosol | − − | − − | + | + + | − − | – | 3.03 | 3.29 | 4.26 | 0 Alert(s) | 0 Alert(s) |
| Oleuropein | − − | – | + + | − − | + + + | + + + | 3.52 | 4.5 | 5.38 | 0 Alert(s) | 1 Alert(s) |
| Apigenin | − − | − − | – | + + + | + + | – | 4.58 | 5.20 | 5.20 | 0 Alert(s) | 0 Alert(s) |
| Pinoresinol | − − | – | – | + | – | – | 5.02 | 5.80 | 6.63 | 0 Alert(s) | 0 Alert(s) |
Drug-induced liver injury (DILI) assessment is an important parameter to determine the potential toxic effect of a molecule on the liver. The higher the DILI value, the higher the potential for that molecule to cause damage to the liver. The high DILI value of apigenin means that this compound can exert more toxic effects on the liver. On the other hand, the low DILI value of Hydroxytyrosol indicates that this molecule has less toxic effects on the liver. Therefore, while Hydroxytyrosol may be a safer compound for the liver, the interpretation that its therapeutic use may offer a safer profile comes to mind [ 103 ] (Table 15 ). As a result of Carcinogencity and AMES toxicity, Oleuropein is the highest. The environmental toxicity profile bioconcentration factors are IGC50, LC50FM and LC50DM (Table 15 ) [ 104 ]. Only the Oleuropein Genotoxic Carcinogenicity Rule 1 provided alerts when the toxicophore rules were analyzed. Other than that, the other components were insignificant (Table 15 ).

In Fig. 9 the ESP maps of the compounds were also given. The notion of the electrostatic potential (ESP) is essential to density functional theory (DFT) calculations because it captures the complex electron–electron interactions and electron density distribution in a system. Theoretically, ESP contributes significantly to our understanding of electronic structure and molecular energetics as well as material characteristics. Positive regions were shown in blue or green on ESP maps produced from DFT calculations, whereas negative regions were shown in red or orange. The distribution of electron density in molecules or materials can be better seen with the use of these colors. Molecular orbital theory was used to investigate chemical stability and reactivity. Furthermore, the energy values of the HOMO and LUMO were used to calculate the quantum reactivity parameters. The negative areas indicate areas with relatively higher electron densities, indicating an environment rich in electrons or an abundance of electrons. These regions usually correspond to electron-rich functional groups, such as lone pairs of electrons or π-electron systems in organic compounds. Chemically, locations of potential electron donation or nucleophilic activity are connected to negative areas. The component of global electrophilicity shows how effectively electron acceptors can pick up additional electronic charge from the system [ 105 – 108 ]. Fig. 9 Compounds structures of ( a ) Apigenin, ( b ) Hydroxytyrosol, ( c ) Cholesterol, ( d ) Linoleic Acid, ( e ) Oleic Acid, ( f ) Pinoresinol, ( g ) Oleuropein and ( h ) Cholesterol-Oleic Acid (i: Mulliken charges; ii: HOMO and LUMO; iii: ESP)


> **Fig. 9:** Compounds structures of ( a ) Apigenin, ( b ) Hydroxytyrosol, ( c ) Cholesterol, ( d ) Linoleic Acid, ( e ) Oleic Acid, ( f ) Pinoresinol, ( g ) Oleuropein and ( h ) Cholesterol-Oleic Acid (i: Mulliken charges; ii: HOMO and LUMO; iii: ESP)

Positive zones on ESP maps, on the other hand, indicate lower electron densities and thus electron-deficient or electron-poor settings. These regions are usually found near electrophilic functional groups or atoms with much higher electronegativity than their adjacent atoms. Electrophilic behavior, in which molecules or atoms attempt to take electrons from other species, is typically associated with positive regions. In the ESP (Electrostatic Potential) analysis of the molecular structures provided, it has been observed that regions containing oxygen atoms exhibit negative charge [ 109 – 112 ]. This observation is consistent across the compounds (a) Apigenin, (b) Hydroxytyrosol, (d) Linoleic Acid, (e) Oleic Acid, (f) Pinoresinol, and (g) Oleuropein. In these molecules, oxygen atoms typically participate in electron-rich functional groups such as hydroxyl (-OH) or carbonyl (C=O) moieties. These oxygen-containing groups contribute to the overall negative electrostatic potential due to their ability to attract electrons. This characteristic is significant in understanding the chemical reactivity and intermolecular interactions of these compounds, particularly in contexts such as hydrogen bonding or interaction with positively charged species. Furthermore, the existence of negative ESP areas surrounding oxygen atoms may have an impact on the compounds' stability, solubility, or biological activity in different environments [ 113 – 115 ]. Cholesterol and Cholesterol-Oleic Acid may exhibit different reactivity characteristics due to their distinct molecular compositions and functional groups, suggesting potential variations in their electrostatic profiles and reactivity patterns.

Furthermore, Table 16 presented clear correlations between the dipole moments of the molecules and their corresponding chemical attributes, including spatial arrangement and electronic structure. The distribution of charge within a molecule is reflected by the dipole moment, which is a measure of polarity and is controlled by molecular geometry and the electronegativity of constituent atoms. In Table 16 , compounds with stronger dipole moments, such oleeuropein and pinoresinol, typically have more polar bonds or asymmetric chemical structures, which cause the positive and negative charges to be significantly separated along the molecular axis. This is in line with their chemical structures, where the unequal electron sharing caused by strongly electronegative atoms—like oxygen in pinoresinol and numerous oxygen atoms in oleuropein—contributes to prominent dipole moments. The molecules with smaller dipole moments, such as hydroxytyrosol and cholesterol, may exhibit more symmetric molecular structures or have less polar bonds, resulting in a reduced separation of charges and hence smaller dipole moments. This is evident in their molecular compositions, where the distribution of electronegative atoms and the overall symmetry of the molecule contribute to relatively lower dipole moments compared to more polar compounds. The relationship between dipole moment and molecular properties can also be inferred from the E HOMO and E LUMO , as well as the total energy changes upon compound formation. Higher dipole moments are often associated with molecules possessing larger energy gaps between E HOMO and E LUMO , indicative of stronger intramolecular charge transfer and greater polarity. Table 16 The calculated quantum parameters for oleic acid, linoleic acid, cholesterol, hydroxytyrosol, apigenin, pinoresinol, oleuropein and cholesterol-oleic acid, by DFT/B3LYP/6-311G (+ + d,p) method Molecule/compound E HOMO (eV) E LUMO (eV) ΔE (eV) χ (eV) η (eV) s (eV −1 ) Total energy (au) µ (Debye) Oleic acid − 6.02 − 1.73 4.28 3.88 2.14 0.46 − 856.9 3.86 Linoleic acid − 5.65 − 3.27 2.38 4.46 1.19 0.84 − 855.5 3.26 Cholesterol − 3.79 − 0.60 3.18 2.20 1.59 0.62 − 1013.7 1.90 Hydroxytyrosol − 6.62 − 7.91 − 1.28 7.26 − 0.64 − 1.55 − 536.6 1.40 Apigenin − 5.94 − 2.56 3.37 4.25 1.68 0.59 − 953.9 4.22 Pinoresinol − 5.78 − 0.85 4.93 3.31 2.46 0.40 − 1226.6 4.30 Oleuropein − 6.04 − 2.15 3.89 4.09 1.94 0.51 − 1949.2 6.10 Cholesterol_Oleic acid − 3.95 − 2.76 1.19 3.35 0.59 1.67 − 1794.2 2.88


### Table 16: The calculated quantum parameters for oleic acid, linoleic acid, cholesterol, hydroxytyrosol, apigenin, pinoresinol, oleuropein and cholesterol-oleic acid, by DFT/B3LYP/6-311G (+ + d,p) method

| Molecule/compound | E HOMO (eV) | E LUMO (eV) | ΔE (eV) | χ (eV) | η (eV) | s (eV −1 ) | Total energy (au) | µ (Debye) |
| Oleic acid | − 6.02 | − 1.73 | 4.28 | 3.88 | 2.14 | 0.46 | − 856.9 | 3.86 |
| Linoleic acid | − 5.65 | − 3.27 | 2.38 | 4.46 | 1.19 | 0.84 | − 855.5 | 3.26 |
| Cholesterol | − 3.79 | − 0.60 | 3.18 | 2.20 | 1.59 | 0.62 | − 1013.7 | 1.90 |
| Hydroxytyrosol | − 6.62 | − 7.91 | − 1.28 | 7.26 | − 0.64 | − 1.55 | − 536.6 | 1.40 |
| Apigenin | − 5.94 | − 2.56 | 3.37 | 4.25 | 1.68 | 0.59 | − 953.9 | 4.22 |
| Pinoresinol | − 5.78 | − 0.85 | 4.93 | 3.31 | 2.46 | 0.40 | − 1226.6 | 4.30 |
| Oleuropein | − 6.04 | − 2.15 | 3.89 | 4.09 | 1.94 | 0.51 | − 1949.2 | 6.10 |
| Cholesterol_Oleic acid | − 3.95 | − 2.76 | 1.19 | 3.35 | 0.59 | 1.67 | − 1794.2 | 2.88 |
The total energy changes upon the formation of compounds involving cholesterol and oleic acid can provide valuable insights into their stability and interactions. When considering the individual components, cholesterol and oleic acid, they possess distinct total energy values, reflecting their respective molecular structures and electronic configurations. However, upon combining these molecules to form cholesterol-oleic acid, there is a discernible alteration (diminishing) in the total energy, indicating the stable new molecular entities. This drop indicates a strengthening of the intermolecular interactions, most likely due to the creation of chemical bonds between the constituent molecules and favorable molecular conformations. Enlightening the energetics of molecular contacts and the production of molecules of biological significance, the overall energy changes provide information on the thermodynamic probability and stability of the reaction between oleic acid and cholesterol.


## Conclusions

In this study, both experimental and computational results provide complementary insights, aligning to reinforce the observed properties of key phenolic compounds in EVOO. The molecular docking analysis highlighted strong binding affinities of apigenin and pinoresinol to target proteins, corroborating their known pharmacological potential, particularly in cardiovascular health. The ADMET analysis aligns well with experimental observations on bioavailability; hydroxytyrosol and apigenin, both with higher bioavailability and absorption potential, match previously reported data on their effective absorption and therapeutic use. The DFT findings, including dipole moments and molecular structure support the pharmacokinetic advantages of hydroxytyrosol, apigenin, and pinoresinol, as these molecules exhibit suitable molecular sizes and stable interactions.

In the toxicity analysis, while the hERG values of all components were not found to be significant, it indicates that the risk of cardiac toxicity of these components is low. Apigenin may cause more damage to the liver with a high DILI value, while Hydroxytyrosol may be safer for the liver with a low DILI value.

Additionally, KEGG enrichment analysis of these compounds demonstrated correlations with lipid metabolism and atherosclerosis, consistent with experimental studies on EVOO’s health benefits.

Overall, the computational insights reinforce the experimental observations, providing a more comprehensive understanding of the therapeutic potential and safety of these compounds.


## Data availability

The datasets used and/or analysed during the current study are available from the corresponding author on reasonable request.