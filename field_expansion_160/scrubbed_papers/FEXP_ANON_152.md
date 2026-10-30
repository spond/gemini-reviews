# FEXP_ANON_152

## Abstract

Alzheimer's disease (AD) leads to gradual memory loss including other compromised cognitive abilities. Acetylcholinesterase (AChE), an important biochemical enzyme from the cholinesterase (ChE) family, is recognized as primary pharmacological target for treating AD. Currently marketed drugs for AD treatment are primarily AChE inhibitors and coumarin derivatives comprising a wide variety of pharmacological activities have proved their efficacy towards AChE inhibition. Ensaculin (KA-672 HCl), a compound that belong to the coumarin family, is a clinical trial candidate for AD treatment. Therefore, a ligand library was prepared with 60 reported coumarin derivatives for field-based 3D-QSAR and pharmacophore modelling. The field-based 3D-QSAR model obtained at partial least square (PLS) factor 7, was the best validated model that predicted activity closer to original activity for each ligand introduced. The contour maps demonstrated spatial distribution of favourable and unfavorable steric, hydrophobic, electrostatic and H-bond donor and acceptor contours around coumarin nucleus. The best pharmacophore model, ADHRR_1 exhibited five essential pharmacophoric features of four different traits for optimum AChE inhibition. Virtual screening through ADHRR_1 accompanied with molecular docking and MM/GBSA identified 10 HITs from a 4,00,000 coumarin derivatives from PubChem database. HITs comprised docking scores ranging from −12.096 kcal/mol to −8.271 kcal/mol and compared with the reference drug Donepezil (-8.271 kcal/mol). ADME properties analysis led into detecting two leads (HIT 1 and HIT 2) among these 10 HITs. Molecular Dynamics Simulation indicated thermodynamic stability of the complex of lead compounds with AChE protein. Finally, thorough survey of the experimental results from 3D-QSAR modelling, pharmacophore modelling and molecular docking interactions led us to develop the lead formula I for future advancements in treating AD through AChE inhibitors.

Keywords: Alzheimer's disease, Coumarin, Acetylcholine esterase, Pharmacophore, 3D-QSAR


## Introduction

Neurodegenerative AD is abstracted as a process that progresses from normal cognitive function to mild cognitive impairment (MCI) through degeneration of brain-cholinergic neurons followed by dementia due to interrupted ACh-mediated neurotransmission ( Bartus et al., 1982 ). It is anticipated that 139 million people would suffer from dementia and 50–60% of these individuals will develop AD by 2050 ( Moreira et al., 2022 ). Neurodegeneration, declining brain functions, apathy, anxiety, depression and memory loss are key signs of AD. Aggression, hallucinations, and delusions grow more frequently as illness worsens ( Lyketsos et al., 2011 ). AChE, an important biochemical enzyme from cholinesterase family, is recognized as primary pharmacological target for treating AD ( Arslan et al., 2020 ; Cavdar et al., 2019 ; Poslu et al., 2023 ). AChE regulates neuronal signal transmission by controlling ChE in CNS (central nervous system). AChE protein comprises unique structure consisting of a gorge region linked catalytic active site (CAS) and a peripheral anionic site (PAS) ( Eckroat et al., 2020 ). AChE enzyme catalyzes acetylcholine (ACh) to hydrolyze into acetate and choline, thereby stopping synaptic neuronal transmission ( Moreira et al., 2022 ), while AChE inhibitors seize esterase activity and prevent disease progression ( Fig. 1 ). The presynaptic reduction of acetylcholine (ACh) in AD is mostly due to cholinergic neuron loss in specific regions like cortex and hippocampus of brain ( Asadipour et al., 2013 ). Randomized clinical studies of AChE inhibitors in patients with AD have been demonstrated to block neurodegenerative effects in cortex, hippocampus, and basal forebrain ( Moss, 2020 ).


> **Fig. 1:** Mechanism of action of AChE inhibition in AD.

Coumarin derivatives demonstrated a diverse array of pharmacological activities, encompassing anti-microbial, hepato-protective, anti-inflammatory, anti-allergic, anti-HIV, anti-oxidant, anti-diabetic, antinociceptive, antidepressant, anti-asthmatic, anti-cancer and anti-AD properties ( George et al., 2022 ). In context of AD, the coumarin-piperazine-benzopyran hybrid molecule, Ensaculin (KA-672 HCl), has exhibited AChE inhibition during clinical trials ( Anand et al., 2012 ). Pharmacophore mapping and field-based 3D-QSAR are widely utilized tools to accelerate the drug development process ( Kapetanovic, 2008 ). As per IUPAC, pharmacophore modelling ensures electronic and steric attributes required for achieving optimal supramolecular interactions with target protein to exert a biological response ( Wermuth et al., 1998 ). A pharmacophore model represents a collection of molecules and their spatial arrangement by abstracting the essential chemical properties crucial for bio-activity ( Schaller et al., 2020 ). To explore the required structural conformation and interactions of bioactive ligands within receptor proteins, molecular docking techniques are employed ( Yadav et al., 2020 ). MM/GBSA, MD Simulations and H-bond analysis are the reliable methods to evaluate thermodynamic stability of lead-protein complexes while ADMET study could confirm drug-likeness of the HITs through pharmacokinetic and toxicity profiling ( Das et al., 2023 ).


## Materials and method


## Computer and software information

The research work including protein preparation, ligand preparation, field-based 3D-QSAR, ADME calculation and pharmacophore modelling was carried out using Maestro 12.9 software of Schrodinger LLC (NY-USA). Pharmacophore modelling and virtual screening database preparation were carried out using the PHASE module. The virtual screening workflow (VSW) was used for virtual screening ( Venkatesan et al., 2018 ). For molecular modelling and docking research, a HP Proliant ML 150-Gen 9 with an Intel Xeon v4 E5-2620 v4 @2.10 GHz, 32 logical processors, 16 cores, 64 GB RAM, and Ubuntu 20.04.2 LTS operating system (OS). Schrodinger LLC (NY-USA) and ChemDraw Professional softwares were employed for drawing compounds for ligand library.


## Protein preparation

Protein preparation in computational biology is the transformation of macromolecular structures into more suitable form for molecular docking. It is important to carry out procedures, such as optimization, H-bond (Hydrogen bond) addition, removal of atomic clashes and water molecules from protein crystal structures prior to docking. 3D crystal structure of human AChE protein (4M0E) in complex with dihydrotanshinone I was obtained from Protein Data Bank ( https://www.rcsb.org/ ). 4M0E comprised good values for standardizing parameters including Resolution = 2.00 Å, Free R-value = 0.196 and Observed R-value = 0.162 ( Jana et al., 2023 ). Maestro's protein preparation wizard (Schrodinger, LLC, New York, NY, USA) was utilized to prepare protein. This tool cleaned up the protein, corrected bond orders and charges, added missing hydrogens and took out the water molecules. Finally, OPLS4 force field reduced and optimized the protein structure.


## Ligand preparation

Total 60 molecules comprising good AChE inhibitory activity (IC 50 range: 0.059–83.76 μM) were collected from literature survey ( Table S1 ) for preparing ligand library for 3D-QSAR and pharmacophore modelling ( Asadipour et al., 2013 ; Mishra et al., 2024 ). The Epik tool of LigPrep module of Maestro 12.9 was utilized for ligand preparation and only one conformer per ligand with least energy state were generated using force field, OPLS4. Which was followed by pH neutralization and desalting ( Das et al., 2023 ; Madhavi Sastry et al., 2013 ). IC 50 values in micromolar concentration were added into dataset and converted into pIC 50 using the following formula ( Kuchana et al., 2022 ):


## Field-based 3D-QSAR modeling

Field-based algorithm was utilized to generate 3D-QSAR models from prepared library of 60 ligands. Models were generated through random distribution of ligands into test set (30%) and training set (70%). Partial Least Square (PLS) factors were utilized to linearly fit 5 Gaussian parameters (Steric, Electrostatic, Hydrophobic, H-bond acceptor and H-bond donor). Linear regression statistics used these 5 parameters at highest number of PLS factors. Analysis of scores for cross-regression coefficient (Q 2 ), standard deviation (SD), regression coefficient (R 2 ), root-mean-squared error (RMSE), R 2 cross validation (R 2 CV) and Pearson-r led us the best QSAR model. The best obtained model was examined through visual representation of 5 distinct coloured contour maps to demonstrate desired spatial arrangements of functional moieties.


## Pharmacophore modelling

Pharmacophore modelling was conducted employing Phase modulev4.6 in Maestro 12.9 of Schrödinger ( Das et al., 2023 ). All 60 prepared coumarin derivatives were incorporated to “Develop Pharmacophore Hypothesis” panel of PHASE tool of Maestro. Pharmacophore hypothesis models were generated considering six pharmacophoric features including H-bond acceptor (A), H-bond donor (D), aromatic ring (R), hydrophobic (H) positively charged group (P) and negatively charged group (N). Best hypothesis model was sorted out through study of survival score, fitness score and molecular alignment with pharmacophore models. The best performing model was secured assigning active with pIC 50 ≥ 6.5 and inactive with pIC 50 ≤ 4.5. All pharmacophore hypotheses were validated through enrichment calculation through screening of active molecules reported in literatures against 1000 decoys (Avg. M.W. = 400 kDa) obtained from Schrödinger database ( http://www.schrodinger.com/glidedecoyset ) and enrichment calculation was carried out. Enrichment factor (EF) was used to describe number of known inhibitors recovered during screening ( Devi et al., 2015 ). Standard enrichment calculation parameters including EF 1% (enrichment in the top 1% of the decoys), Phase Hypo Score, and BEDROC160.9 score was analyzed to validate the best pharmacophore model.


## Dataset preparation and virtual screening

400,000 exclusive structural records of coumarin derivatives in the PubChem database ( https://pubchem.ncbi.nlm.nih.gov ) were used in this investigation. LigPrep and Epik tools of maestro were used to create a database that expanded each molecule's tautomeric conformations and protonation states at pH 7. Electrostatic interactions were screened by dielectric solvation technique based on distance. Structures with high energy were excluded by fixing relative energy-difference maximum at 10.0 kcal/mol. Indexing of the database was done through Phase and pharmacophoric sites were constructed for screening ( Saxena et al., 2018 ). The most validated and trustworthy pharmacophore model was used to perform virtual screening in a hierarchal approach via Phase database screening as well as High Throughput Virtual Screening (HTVS).


## Molecular docking

The molecular docking study of screened molecules was conducted using Maestro 12.5 software. Grid-based Ligand Docking with Energetics (GLIDE) tool explored protein-ligand interaction energies (kcal/mol) and calculated flexibility of the ligands. Ligands under consideration had been docked via Standard Precession (SP) and Extra Precession (XP) molecular docking. The key metrics including hydrophobic, pi-pi stacking and H-bonding interactions were analyzed to identify HIT molecules.


## ADME calculations

Bioavailability prediction is one of the vital stages in drug discovery and development, since it prevents many medications from succeeding in preliminary phases of clinical trials because of their poor pharmacokinetic features ( Storelli et al., 2022 ). The ADME properties including Absorption, Distribution, Metabolism, and Excretion of 10 identified HITs were evaluated through QikProp tool of Maestro 12.9 for determination of pharmacokinetic properties like hydrophobicity, water solubility, human oral absorption, blood brain barrier permeability and gastrointestinal permeability ( Turner et al., 2007 ).


## Binding free energy calculation

Free binding energies for all HITs were determined to hypothesize thermodynamic stability of the ligands within target protein by Prime MMGBSA technique. Binding energy of docked complexes were minimized and binding free energy was estimated considering water as solvent via OPLS force field ( Suryadevara et al., 2016 ). Free energy of binding (G Binding ) was calculated using Equation (1) .

Where, ΔE = E Complex – (E Protein + E Ligand ); ΔGSolv = ΔGSolv Complex – (ΔGSolv Protein + ΔGSolv Lig );

[Terms: Solv = solvation energy; SA = surface area associated energy; E = energy minimized states of the protein-ligand complex]


## Molecular Dynamics stimulation

MD simulation study was performed for 100ns for the most efficacious compounds HIT 1 and HIT 2 for analysis of protein-ligand binding interactions through GROMACS 2021.6 software ( Saini et al., 2023 ). Complex topology of TIP3P model was generated using CHARMM36-Mar2019 force field. A solvate water box was used with minimum 1.5 nm distance from protein surface. Counter ions like Na + and Cl − were added for neutralizing the protein-ligand complexes. The complex systems undergone energy minimization through steepest descent algorithm, NVT equilibration (500 ps at 310K) using Nose-Hoover thermostat with Coupling constant of 0.1 ps and NPT equilibration (500 ps at 1 bar pressure) with the use of Parrinello-Rahman algorithm ( Evans et al., 1985 ; Parrinello et al., 1981 ). Production run of 100 ns was conducted and time step of 2 fs was fixed. LINear Constraint Solver (LINCS) algorithm calculated bond length constrains ( Hess et al., 1997 ). In addition, Particle mesh Ewald (PME) strategy with grid spacing of 0.16 nm, cut-off radius of 1.2 nm and van der Waals cut-off distance of 1 nm were employed. The MD trajectory was evaluated through GROMACS analysing parameters such as Root Mean Square Deviation (RMSD), Root Mean Square Fluctuation (RMSF) and Radius of Gyration (rGy) ( Kumar et al., 2022 ).


## Results and discussion


## Field-based 3D-QSAR modelling

The 3D-QSAR models generation based on Gaussian field is a modified version of CoMFA and CoMSIA in computer aided drug designing. Gaussian field-based 3D-QSAR was responsible for predicting AChE inhibitory activity and providing three-dimensional information about essential spatial features of precisely aligned 60 coumarin ligands from ligand library ( Fig. 2 ).


> **Fig. 2:** Aligned ligands for QSAR modelling.

PLS linear regression analysis was utilized to generate QSAR models and best model was achieved at PLS factor 7 with a SD of 0.2754, R^2 of 0.9644, R^2 CV of 0.1945, R^2 Scramble of 0.8208, Stability of 0.25, F value of 104.6, P value of 6.86E-18, RMSE of 0.87, Q^2 of 0.595 and Pearson-r of 0.854. pIC 50 values of ligands were dependent variable against 5 independent Gaussian parameters for the chosen 3D-QSAR model ( Table 1 ). Values of SD and RMSE closer to 0 indicated negligible error probability at PLS7. R 2 value nearer to 1 reflected excellent correlation between predicted activity and original activity for training set while Q 2 showed good correlation within test set. Low value of probability of errors (P) and high value for variance ratio (F) signified great predictivity of the selected model. External validation of the best model was confirmed by Pearson-r value exhibiting correlation between observed activity and predicted activity within test set. Pearson-r value close to +1 established strong positive linear correlation ( Marondedze et al., 2020 ).


### Table 1: Field-based 3D-QSAR modelling parameters.

| PLS Factors | SD | R^2 | R^2 CV | R^2 Scramble | Stability | F | P | RMSE | Q^2 | Pearson-r |
| 1 | 1.0614 | 0.3544 | 0.077 | 0.3319 | 0.916 | 18.1 | 0.000162 | 1.14 | 0.3085 | 0.6008 |
| 2 | 0.6996 | 0.728 | 0.0323 | 0.4992 | 0.408 | 42.8 | 9.00E-10 | 1.02 | 0.4493 | 0.6985 |
| 3 | 0.6001 | 0.8061 | 0.1582 | 0.5823 | 0.438 | 43 | 3.72E-11 | 0.89 | 0.5776 | 0.8026 |
| 4 | 0.5148 | 0.8619 | 0.1649 | 0.6536 | 0.399 | 46.8 | 1.77E-12 | 0.8 | 0.6573 | 0.8579 |
| 5 | 0.4504 | 0.8978 | 0.1417 | 0.716 | 0.32 | 51 | 1.75E-13 | 0.75 | 0.6979 | 0.8963 |
| 6 | 0.3792 | 0.9301 | 0.1289 | 0.778 | 0.267 | 62.1 | 7.00E-15 | 0.8 | 0.6602 | 0.9024 |
| 7 | 0.2754 | 0.9644 | 0.1945 | 0.8208 | 0.25 | 104.6 | 6.86E-18 | 0.87 | 0.595 | 0.854 |
For further validation of selected 3D-QSAR model, two scatter plots were produced for exhibiting graphical representation of predicted activity vs experimental activity for training and test sets. Scatter plots denoted all the molecules in both data sets lies close to the linear regression line confirming reliability of the model at PLS 7 ( Fig. 3 ).


> **Fig. 3:** Scatter plot of experimental activity versus predicted activity at PLS factor 7 - (a) Training set (b) Test set.


## Contour map analysis

The PHASE module of Maestro facilitated five distinct contour plots visualization and demonstrated percentage Gaussian field contributions for steric (38.1%), electrostatic (10.3%), hydrophobic (27.8%), H-Bond Donor (6.9%) and H-Bond acceptor (16.9%) contours. The different coloured contours estimated desired spatial characteristics around aligned coumarin scaffold to exert AChE inhibitory activity to treat AD while red coloured regions indicated unfavorable contours for each Gaussian field ( Fig. 4 ). Green coloured contours representing steric contributions suggested bulky substitutions are preferred at C-3, C-6 and C-8 positions of coumarin scaffold for better activity. Blue electrostatic contours indicated favourable electropositive regions over C-4, C-5, C-6 and C-7 on the coumarin plane and nearby regions of C-3 while red coloured sites near C-3, C-6 and C-8 outside coumarin plane favoured electronegative attachments. The favourable spot for H-Bond donor groups was found at C-4 presented in magenta and double bonded oxygen at C-2 and its nearby yellow-green coloured positions indicated beneficial as H-Bond acceptor region. Cyan coloured favourable hydrophobic contours were found to be distributed throughout the plot outside coumarin plane and mainly preferred at C-3, C-6 and C-8 positions while those are not desired at C-7. The numbering system of coumarin represented in Fig. 11 was utilized for explaining the contour maps (see Fig. 12 ).


> **Fig. 4:** Contour maps - A. Steric; B. Electrostatic; C. Hydrophobic; D. H-bond acceptor; E. H-bond donor.


> **Fig. 11:** Molecular dynamics stimulation trajectory.


> **Fig. 12:** Lead formula I.


## Pharmacophore modelling

The pharmacophore modelling benefits from ligand-based as well as structure-based screening techniques to quickly screen millions of chemical entities and considered as a trustworthy lead hopping method that can extract a wider range of actives than conventional structure-based pharmacophore method ( Jana et al., 2019 ). Coumarin based AChE inhibitors have shown significant promise against AD ( Onder et al., 2022 ). In the current study, sixty distinct compounds with coumarin Scaffold, were chosen from literatures within the range of pIC 50 values of 4.5–6.5. Total ten hypotheses were produced assigning actives with pIC 50 values ≥ 6.5 and inactive molecule pIC 50 values ≤ 4.5 within ligand library and pharmacophore models with distinct pharmacophoric fingerprints (ADHRR, AHHRR, AHRRR, AARRR, DHRR and HRRR) were generated ( Table 2 ).


### Table 2: Generated pharmacophore models with scoring parameters.

| Sr. No. | Models | Survival Score | Vector Score | Volume Score | BEDROC Score | Site Score |
| 1 | AARRR_1 | 5.136 | 0.905 | 0.741 | 0.608 | 0.730 |
| 2 | ADHRR_4 | 5.180 | 0.989 | 0.654 | 0.602 | 0.822 |
| 3 | ADHRR_1 | 5.464 | 0.999 | 0.848 | 0.575 | 0.886 |
| 4 | ADHRR_3 | 5.258 | 0.967 | 0.750 | 0.576 | 0.773 |
| 5 | DHRR_1 | 5.059 | 0.992 | 0.797 | 0.582 | 0.822 |
| 6 | AHRRR_1 | 5.532 | 0.938 | 0.832 | 0.560 | 0.848 |
| 7 | ADHRR_5 | 5.121 | 1.000 | 0.697 | 0.571 | 0.695 |
| 8 | AHHRR_1 | 5.159 | 0.937 | 0.632 | 0.571 | 0.705 |
| 9 | AHRRR_2 | 5.270 | 0.883 | 0.719 | 0.560 | 0.767 |
| 10 | HRRR_1 | 5.217 | 0.947 | 0.838 | 0.560 | 0.899 |
All models were analyzed for their ligand fitness scores and ability to distinguish between active and inactive and best pharmacophore model was obtained as ADHRR_1 comprised of one H-bond acceptor (A), one H-bond donor (D), one hydrophobic (H), and two aromatic rings (R) ( Fig. 5 ). The best model was chosen based on survival score (5.464), vector score (0.999), volume score (0.848), BEDROC score (0.575) and site score (0.886) for virtual screening of coumarin derivatives from PubChem database ( Table 2 ).


> **Fig. 5:** A. spatial arrangement of pharmacophoric features, B. Distance measured between pharmacophoric features, C. Alignment of actives D. Alignment of inactives for pharmacophore model ADHRR_1.


## Pharmacophore model validation

Best obtained pharmacophore model was verified through enrichment calculations before database screening in order to evaluate quality of model to differentiate between inactive and active. The best model, ADHRR_1, showed high EF1% value (11.92) whereas BEDROC160.9, Phase Hypo Score scores were 11.92, 0.64 and 0.90, respectively ( Table 3 ) that confirmed high probability of identifying good hits through this model during virtual screening. Out of 65 active compounds, ADHRR_1 managed to rank 65 out of 65 actives with no excluded volume and exhibiting 3 out of 4 pharmacophoric matches.


### Table 3: Enrichment results of the pharmacophore models.

| Models | EF1% | BEDROC160.9 Scores | Phase Hypo Scores | Total Actives | Ranked Actives | Matches | Excluded Volumes |
| AARRR_1 | 2.98 | 0.19 | 0.92 | 65 | 65 | 3 of 4 | No |
| ADHRR_4 | 8.94 | 0.58 | 0.91 | 65 | 64 | 3 of 4 | No |
| ADHRR_1 | 11.92 | 0.64 | 0.90 | 65 | 65 | 3 of 4 | No |
| ADHRR_3 | 4.47 | 0.29 | 0.89 | 65 | 65 | 3 of 4 | No |
| DHRR_1 | 7.45 | 0.41 | 0.89 | 65 | 52 | 3 of 4 | No |
| AHRRR_1 | 4.47 | 0.34 | 0.89 | 65 | 62 | 3 of 4 | No |
| ADHRR_5 | 13.41 | 0.86 | 0.88 | 65 | 65 | 3 of 4 | No |
| AHHRR_1 | 4.47 | 0.21 | 0.88 | 65 | 65 | 3 of 4 | No |
| AHRRR_2 | 2.98 | 0.15 | 0.88 | 65 | 64 | 3 of 4 | No |
| HRRR_1 | 5.96 | 0.44 | 0.87 | 65 | 49 | 3 of 4 | No |
In pharmacophore models, a good sensitivity versus specificity performance was established by using receiver operating characteristic (ROC) curve. The distinguishing ability of chosen model for identifying true positives and false positives was determined by ROC plot and percentage screen plot ( Florkowski, 2008 ) ( Fig. 6 ).


> **Fig. 6:** A. ROC plot; B. Percentage of screen plot for ADHRR_1 pharmacophore model.


## Virtual screening

Virtual screening has become a crucial tool in search of innovative drug-like molecules. Large variety of comparable and dissimilar methodological approaches are accessible in databases used for lead compound screening ( Reddy et al., 2007 ). Present study employs PubChem database for assessing chemical structures as it provides thorough chemical data that is beneficial for drug discovery ( Kim, 2016 ). A library of 4,00,000 molecules downloaded from PubChem database were prepared in order to perform virtual screening. PubChem database was screened through PHASE tool in maestro using selected pharmacophore model, ADHRR_1 to yield 2,49,086 molecules with desired pharmacophoric traits including H-bond donor and acceptor, hydrophobic system and aromatic ring system. All 2,49,086 molecules were taken for High Throughput Virtual Screening (HTVS) to filter out 1,97,527 compounds for performing SP molecular docking and ranked according to docking scores. Top 1% (1975) of the ranked ligands of glide SP docking were chosen for XP molecular docking based on their fitness score (>2.3). XP docking scores brought out 245 compounds with molecular docking score greater or equal to donepezil (−8.271 kcal/mol) and were considered for MM/GBSA for free energy of binding. Virtual screening steps have been depicted in Fig. 7 .


> **Fig. 7:** Virtual Screening workflow.


## Molecular docking

Molecular docking stands as a valuable computational tool in the realms of drug design, lead optimization, and virtual screening, facilitating the discovery of novel bioactive molecules through the analysis of protein-ligand binding interactions ( Guedes et al., 2014 ). This approach provides detailed insights into molecular recognition, proving instrumental in the fields of drug discovery and medicinal chemistry ( Jakhar et al., 2020 ). Glide dock SP and XP were performed to rank and sort out coumarin derivatives having dock scores (range: −8.271 to −13.01 kcal/mol) higher than or equals to Donepezil (−8.271 kcal/mol). HIT molecules exerted several interactions ( Table S2 ) with amino acid residues of AChE including pi-pi interactions with TRP 286 and TRP 284, hydrophobic interactions with TYR 41, PHE 338, TYR 337, ILE 451, PHE 297, TYR 72 and formed H-bonds with SER 203, PHE 295, ARG 296, TYR 124, HIP447, SER 203 and GLU202. Detailed 2D and 3D binding interactions of HIT1, possessing highest docking score and reference compound donepezil have been depicted in Fig. 8 . Furthermore, Fig. 9 showed binding poses of all identified HIT molecules following MM/GBSA, within AChE protein cavity.


> **Fig. 8:** Protein-ligand 2D and 3D interactions of best HIT 1 and Donepezil with 4M0E.


> **Fig. 9:** All HITs docked within donezepil binding pocket of 4M0E.


## MM/GBSA calculations

Binding free energy of for small molecules to biological macromolecules was determined through molecular mechanics energies in combination with generalized born surface area continuum solvation (MM/GBSA) methods ( Genheden et al., 2015 ). All 245 molecules refined through XP docking, were exposed to MM/GBSA for assessing thermodynamic compatibility within the protein cavity of 4M0E through calculating free energies of binding ( Table S3 ). Relative binding affinity, total binding energy and energies of van der Waals (VdW) interactions towards AChE binding were determined by MM-GBSA technique ( Durrant et al., 2011 ). All 245 molecules had binding energies within a diverse range from −72.26 to −28.96 kcal/mol while score of reference drug, donepezil elicited as −35.56 kcal/mol ( Table 4 ). A thorough analysis of thermodynamic stability results of MM/GBSA study and binding affinity data from molecular docking led into identification of 10 HIT molecules namely - HIT1, HIT2, HIT3, HIT4, HIT5, HIT6, HIT7, HIT8, HIT9 and HIT10 having PubChem IDs of 134139986, 134155007, 156011162, 156013172, 26795926, 19185913, 134152051, 100794119, 122280404, 2984957 ( Fig. 10 ). MMGBSA dG Bind scores of all HITs were identified within the range of −70.94 to −55.33 kcal/mol while their docking scores lies between −12.096 kcal/mol and 8.271 kcal/mol.


### Table 4: MM/GBSA results of HITs.

| HITs | MMGBSA dG Bind | MMGBSA dG Bind Coulomb | MMGBSA dG Bind Covalent | MMGBSA dG Bind Solv GB | MMGBSA dG Bind vdW | Prime MMGBSA ligand efficiency |
| 134139986 | −60.19 | −20.34 | −0.41 | 56.63 | −49.42 | −1.77 |
| 134155007 | −60.16 | −18.18 | 2.37 | 45.86 | −48.53 | −2.149 |
| 156011162 | −68.7 | −31.92 | 8.49 | 57.99 | −56.13 | −1.963 |
| 156013172 | −69.63 | −33.16 | 6.52 | 55.07 | −51.55 | −2.11 |
| 26795926 | −56.24 | −18.95 | 3.62 | 49.85 | −47.09 | −2.25 |
| 19185913 | −70.94 | −7.64 | 16.94 | 45.15 | −69.09 | −2.086 |
| 134152051 | −60.66 | −25.21 | 0.43 | 55.81 | −46.88 | −1.784 |
| 100794119 | −58.52 | −20.28 | 3.38 | 53 | −49.04 | −2.544 |
| 122280404 | −65.67 | −23.46 | 0.77 | 47.88 | −52.06 | −2.526 |
| 2984957 | −55.33 | −28 | 2.43 | 48.72 | −44.25 | −2.305 |
| Donepezil | −35.56 | −11.11 | −0.75 | 57.56 | −37.61 | −1.27 |

> **Fig. 10:** Structure of HIT molecules.


## ADMET

ADMET property of all 10 HITs were estimated for determining the pharmacokinetic characteristics using QikProp module of Schrödinger 10.7 as QikProp provides a range for contrasting a specific molecule characteristics of almost 95 percent of recognized medications and examined parameters according to “Lipinski's rule of five” ( CAL, 2004 ; Lipinski et al., 1997 ). All identified HITs showed drug-like ADMET characteristics and showed favourable toxicological profile ( Table 5 ) ( Verma et al., 2018 ). All HITs having molecular weight within 307.348 Da and 482.440 Da, exhibited significantly high percentage of Human Oral Absorption (HOA) while HIT1, HIT2, HIT5 and HIT8 were highlighted with 100% HOA. Hydrogen bond acceptors (HBA) ranged from 4 to 8. The analogues' high HBA count provided significant contribution towards improved affinity and interactions for AChE. Caco cell permeability (QPPCaco) of the top HITs is within an acceptable range (>70), estimated efficient absorption and dispersion of HITs. Finally, analysis all pharmacokinetic parameters including Polar surface area, H-bond acceptor and donor, water solubility, lipophilicity and permeability through blood brain barrier (BBB), two (HIT1 and HIT2) of the 10 HITs were identified as leads and considered for MD simulations study to analyze stability of protein-ligand complexes.


### Table 5: ADME profiling of HITs.

| HITs (Recommended range) | mol MW (130.0–725.0) | PSA (above 100) | DonorHB (0.0–6.0) | Accept HB (2.0–20.0) | QPlogPo/w (−2.0 to 6.5) | QPlogS (<5.0) | QPlogHERG (above −5.0) | QPlogBB (−3.0 to 1.2) | QPPMDCK (Great: >500 nm/s) | % HOA (>80% = high; <25% = poor) |
| HIT1 | 472.927 | 95.537 | 1.000 | 4.750 | 6.109 | −8.156 | −7.753 | −1.182 | 591.095 | 100.00 |
| HIT2 | 376.411 | 97.119 | 1.000 | 4.750 | 4.297 | −6.265 | −6.755 | −1.293 | 230.009 | 100.0 |
| HIT3 | 482.440 | 134.634 | 1.000 | 8.000 | 4.124 | −7.074 | −7.311 | −2.173 | 122.145 | 87.148 |
| HIT4 | 452.506 | 134.446 | 1.000 | 8.000 | 3.595 | −6.235 | −6.202 | −2.173 | 49.641 | 85.152 |
| HIT5 | 341.338 | 83.590 | 0.000 | 4.750 | 3.797 | −5.165 | −6.238 | −0.795 | 741.259 | 100.00 |
| HIT6 | 455.509 | 102.102 | 0.000 | 6.500 | 5.206 | −7.277 | −7.246 | −1.304 | 263.286 | 93.631 |
| HIT7 | 456.472 | 96.343 | 1.000 | 4.750 | 5.571 | −7.252 | −7.276 | −1.175 | 440.832 | 95.996 |
| HIT8 | 307.348 | 74.501 | 0.000 | 4.000 | 3.834 | −5.196 | −6.394 | −0.790 | 460.209 | 100.000 |
| HIT9 | 351.361 | 118.754 | 0.000 | 6.000 | 2.782 | −4.787 | −6.041 | −1.427 | 116.310 | 85.518 |
| HIT 10 | 327.339 | 98.534 | 0.000 | 6.750 | 2.222 | −3.380 | −5.922 | −1.135 | 259.930 | 89.021 |

## Molecular Dynamics

Molecular dynamics (MD) simulation was performed on two obtained leads for 100 ns using GROMACS 2021.6 to explore thermodynamic compatibility of protein-ligand complexes. Root Mean Square Deviation (RMSD) plot was found within 0.2–0.28 nm range while average RMSD obtained 0.24 nm throughout the trajectory ( Fig. 11 A). Gyration radius (rGy) evaluated compactness of protein around ligand and found between 2.30 and 2.33 nm which signified high complex stability with negligible variation during trajectory of ∼3 nm ( Fig. 11 B). The RMSF studied indicated dynamic protein residues around ligand and values depicted within a range of 0.06–0.4 nm indicated no significant fluctuations internally ( Fig. 11 C). Higher oscillations were observed in residues of various regions such as 78–85, 270–275, and 490–495 along with terminal residues of 4M0E protein, which might be due to presence of loops in that region and free end at terminal regions. RMSF value for HIT1 and HIT2 was found to vary between 0.06-0.37 nm and 0.02–0.15 nm, respectively, signified that atoms of small ligands were oscillating during amino acid interactions present inside catalytic binding pocket of AChE ( Fig. 11 D). Furthermore, H-bond profiling and hydrogen bond occupancy were assessed for both leads and was observed to be 100% ( Fig. 11 E) indicating 2–4 and 1–3 hydrogen bond interactions, respectively for HIT1 and HIT2. Finally, hydrogen bond distance distribution was recorded and was found that all H-bonds formed within the applied cut-off value of 0.35 nm for both the complexes confirmed significant role of H-bonding for stabilization of protein-ligand complexes ( Fig. 11 F). Overall analysis of the trajectory confirmed that both complexes were well stabilized thermodynamically throughout 100ns within the 4M0E protein.


## Development of lead formula

A combination of multi-stage in silico analysis of derivatives containing small molecule explored many vital pharmacophoric as well as spatial features around coumarin scaffold to exert good AChE binding for AD. Gaussian field-based 3D-QSAR model exposed key spatial arrangements of substitutions with distinct physicochemical characteristics for betterment of AChE inhibitory activity. The contour plot analysis suggested that bulky steric and hydrophobic groups are preferred at C-3, C-6 and C-8 positions; electropositive groups are favourable at C-4, C-5, C-6, C-7 and nearby regions of C-3; while H-Bond donors are desired at C-4 and double bonded oxygen at C-2 is a vital H-Bond acceptor for AChE protein binding. The best obtained pharmacophore model, ADHRR_1 reflected essentiality of H-Bond donors, H-Bond acceptors, aromatic ring and hydrophobic systems in its pharmacophoric fingerprints at precise distance from each other in three-dimensional space. Thorough analysis of pharmacophore model dependent virtual screening, GLIDE docking and MM/GBSA yielded 10 HITs with high dock scores and free energies of AChE binding. Structural exploration of protein-ligand binding interactions suggested that coumarin scaffold is important for AChE binding through pi-pi interactions with TRP 286 via ring A and with TRP 286 and TYR 34 via ring B whereas oxygen of carbonyl group formed H-bond with PHE 295. Finally, pharmacokinetic parametric analysis led into identification of two best capable leads – HIT1 and HIT2. Furthermore, the amide linkage present at C-3 position was found responsible for H-bonding interactions with TYR 124 to achieve stable conformation within donepezil binding pocket. R1 attached to amide linked chain could be substituted with phenyl, indole, 3H-cyclopentapyridazine or imidazole for optimum potentials. At C-7 position, R2 substitutions are preferable as phenol, chloro-substituted phenol, difluoro phenol, ethyl cyclopropane for better fitting into the binding pocket. Based on these analytical results a lead formula I was developed to provide a coumarin-core framework for generating novel leads as AChE inhibitor against AD.


## Conclusion

The current study involved development of optimal 3D-QSAR model at PLS factor 7 with predictiveness for AChE inhibition and demonstrated desired location of pharmacophoric groups which was further corroborated by the best-validated pharmacophore model, ADHRR_1, featuring four distinct traits. Utilizing the pharmacophore model virtual screening was carried out to concentrate the 400000-molecule containing PubChem database. Glide dock SP and XP sorted out 245 molecules having better binding affinity compare to reference drug donepezil. Extensive investigation of docking scores and MM/GBSA free binding energies led to find out thermodynamically stable 10 HITs having docking scores between −8.271 kcal/mol and −12.096 kcal/mol. Results of ADME analysis for 10 HITs indicated that HIT1 and HIT2 as lead molecules having docking scores of −12.096 kcal/mol and −11.666 kcal/mol along with MMGBSA dG Bind scores of −60.19 kcal/mol and −60.16 kcal/mol, respectively and consisted of 100% HOA. Furthermore, MD simulations certified that both lead-complexes were thermodynamically stable throughout the 100ns trajectory. Finally, a lead formula I was developed from the outcomes of 3D-QSAR, pharmacophore modelling and molecular docking interactions to provide insight of crucial structural and binding properties for developing novel AChE inhibitors for future advancements in treating AD.


## CRediT authorship contribution statement

Bikram Saha: Field-based 3D-QSAR and Pharmacophore Model-based Virtual Screening. Agnidipta Das: Molecular Docking, Manuscript Preparation. Kailash Jangid: Molecular Dynamic. Amit Kumar: MM/GBSA, ADME. Vinod Kumar: MD and editing. Vikas Jaitak: Idea generation, Writing – review & editing, and overall, Supervision.


## Supplementary data

The following is the Supplementary data to this article.


## Data availability

Data will be made available on request.


## Associated Data


## Supplementary Materials


## Data Availability Statement

Data will be made available on request.