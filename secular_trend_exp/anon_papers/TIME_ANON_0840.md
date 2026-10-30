# Anonymous Manuscript ID: TIME_ANON_0840

*(All identifying metadata, author names, journal titles, DOIs, and publication/citation calendar years have been scrubbed for temporally blinded review.)*

## Abstract

Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) is distinctly infective and there is an ongoing effort to find a cure for this pandemic. Flavonoids exist in many diets as well as in traditional medicine, and their modern subset, indole-chalcones, are effective in fighting various diseases. Hence, these flavonoids and structurally similar indole chalcones derivatives were studied in silico for their pharmacokinetic properties including absorption, distribution, metabolism, excretion, toxicity (ADMET) and anti-SARS-CoV-2 properties against their proteins, namely, RNA dependent RNA polymerase (rdrp), main protease (M pro ) and Spike (S) protein via homology modelling and docking. Interactions were studied with respect to biology and function of SARS-CoV-2 proteins for activity. Functional/structural roles of amino acid residues of SARS-CoV-2 proteins and, the effect of flavonoid and indole chalcone interactions which may cause disease suppression are discussed. The results reveal that out of 23 natural flavonoids and 25 synthetic indole chalcones, 30 compounds are capable of M pro deactivation as well as potentially lowering the efficiency of M pro function. Cyanidin may inhibit RNA polymerase function and, Quercetin is found to block interaction sites on the viral spike. These results suggest flavonoids and their modern pharmaceutical cousins, indole chalcones are capable of fighting SARS-CoV-2. The in vitro anti-SARS-CoV-2 activity of these 30 compounds needs to be studied further for complete understanding and confirmation of their inhibitory potential.

Keywords: Flavonoids, Indole chalcones, SARS-CoV-2, In silico , COVID-19, Phytochemicals


## Introduction

Coronavirus, the 21st-century pandemic highlights the role of viruses in emerging infectious diseases. It caused a vital onset of lethal pneumonia, initiated by the severe acute respiratory syndrome coronavirus (SARS-CoV) epidemic in [YEAR] ( Rahman et al., [YEAR] ). The SARS-CoV-2 afflicted 213 countries around the world with more than 18 million infections and more than 0.7 million deaths worldwide as on August 5, [YEAR]. The current global plight of COVID-19 is pandemic and the virus continues to sweep the world with no known cure. Coronaviruses are spherical positive RNA viruses in the Coronaviridae family with the largest genome amidst all RNA viruses ( Weiss and Leibowitz, [YEAR] ; Wu et al., 2020a ). The CoV genomes have non-structural proteins (nsps), replicase (RNA dependent RNA polymerase or rdrp) at 5′ end, open reading frames and structural proteins at 3′ end. The replication gene has two polyproteins (pp1ab and pp1a) for replication and transcription which are converted into 16 nsps by main protease (M pro ) ( Jin et al., 2020b ). These nsps produce subgenomic RNA encoding the structural proteins: spike (S), envelope (E), membrane (M) and nucleocapsid (N) proteins ( Wu et al., 2020a ). The N protein complexes with RNA forming the helical capsid in the viral envelope with other structural proteins embedded inside. The spike proteins projecting from the viral surface carries two domains (S1 and S2) and the receptor-binding domain (RBD) in S1 binds with angiotensin-converting enzyme 2 (ACE2) in host cells to mediate the integration of host and viral cells for viral entry ( Ashour et al., [YEAR] ; Cui et al., [YEAR] ). This initiates replication and once inside the host cell, rdrp produces viral mRNA or messenger RNA from template RNA which undergoes translation forming non-structural and structural proteins. The process is error-laden as rdrp lack proofreading functions, increasing the mutation rate within the virus ( Venkataraman et al., [YEAR] ).

The present-day SARS-CoV-2 has 89% nucleotide similarity and 80% identity with SARS-CoV ( Wu et al., 2020b ). When correlated with Middle East respiratory syndrome coronavirus (MERS-CoV) and SARS-CoV, current SARS-CoV-2 shows 96% sequence identity with a bat CoV, RaTG13, indicating a common ancestral origin ( Guo et al., [YEAR] ; Zhou et al., [YEAR] ). Despite endeavours to develop a cure after MERS and SARS coronaviruses, vaccines or drugs are still lacking. The antivirals used currently reduce transmission and give symptomatic relief. Current approaches toward anti-corona agents include repurposing of drugs, screening of promising molecules using an extant database or developing a novel vaccine using genomic information of CoVs ( Wu et al., 2020a ). The main drug targets for CoV include the M pro , rdrp and spike proteins. An in-silico approach of screening existing database to find a variety of compounds inhibiting coronavirus against these targets can save time by filtering out candidates worthy of in vitro analysis.

One such set of compounds are flavonoids given in Table 1 ubiquitous in vegetables, fruits, herbs and in traditional medicines ( He et al., [YEAR] ; Li et al., [YEAR] ; Xu et al., [YEAR] ). Flavonoids exhibit antiviral ( Dai et al., [YEAR] ), antibacterial ( Yixi et al., [YEAR] ), antimicrobial ( Cushnie and Lamb, [YEAR] ), anticancer ( Chahar et al., [YEAR] ), antidiabetic ( AL-Ishaq et al., [YEAR] ), anti-inflammatory ( He et al., [YEAR] ) and antifungal ( Weidenbörner et al., [YEAR] ) properties. Recent reports show quercetin based antiviral drug Gene-Eden-VIR/Novirin inhibiting the protease of SARS-CoV-2 ( Polansky and Lori, [YEAR] ). Chalcones in flavonoids subset inhibit tobacco mosaic virus ( Tang et al., [YEAR] ), HIV ( Wu et al., [YEAR] ), herpes ( Hassan et al., [YEAR] ) and dengue virus ( Kiat et al., [YEAR] ) along with antioxidant ( Biradar et al., [YEAR] ), antimicrobial ( Burmaoglu et al., [YEAR] ), antimycobacterial ( Chiaradia et al., [YEAR] ) and antileishmanial ( de Mello et al., [YEAR] ) properties. The alkylated chalcones extracted from Angelica keiskei inhibit SARS-CoV protease ( Park et al., [YEAR] ).


### Table 1: Biological activities of natural flavonoids.

| Name | Compound CID | Bioactivity | Reference |
| Luteolin | 5280445 | Inhibition of Japanese encephalitis virus | Fan et al. ([YEAR]) |
| Apigenin | 5280443 | Inhibition of Foot-and-mouth disease virus (FMDV) and Enterovirus-71 infection | ( Qian et al., [YEAR] ; Zhang et al., [YEAR] ) |
| Tangeritin | 68077 | Inhibition of respiratory syncytial virus (RSV) | Xu et al. ([YEAR]) |
| Kaempferol | 5280863 | Inhibition of influenza virus | Dong et al. ([YEAR]) |
| Quercetin | 5280343 | Inhibition of dengue and influenza virus | ( Wu et al., [YEAR] ; Zandi et al., [YEAR] ) |
| Myricetin | 5281672 | Inhibition of tobacco mosaic virus and anti-HIV activity | ( Semwal et al., [YEAR] ; Tang et al., [YEAR] ) |
| Fisetin | 5281614 | Inhibition of enterovirus-A71 | ( Lalani and Poh, [YEAR] ; Lin et al., [YEAR] ) |
| Hesperitin | 72281 | Inhibition of influenza virus | Dong et al. ([YEAR]) |
| Naringenin | 932 | Inhibition of dengue virus | ( Frabasile et al., [YEAR] ; Salehi et al., [YEAR] ) |
| Eriodictyol | 440735 | Anti-diabetic, anti-inflammatory and anti-osteoclastogenic agent | ( Wang et al., [YEAR] ; Zhang et al., [YEAR] ) |
| Liquiritin | 503737 | Anti-inflammatory, antiviral and anti-microbial | ( Chirumbolo, [YEAR] ; Yu et al., [YEAR] ) |
| Genistein | 5280961 | Inhibition of African swine flu virus and herpes virus | ( Andres et al., [YEAR] ; Arabyan et al., [YEAR] ; LeCher et al., [YEAR] ) |
| Daidzein | 5281708 | Inhibition of herpes virus | Argenta et al. ([YEAR]) |
| Calophyllolide | 5281392 | Anti-HIV activity | Liu et al. ([YEAR]) |
| Cyanidin | 128861 | Anti-HIV activity | ( [REDACTED_AUTHOR] and Kolandaivel, [YEAR] ; Kaur et al., [YEAR] ) |
| Delphinidin | 68245 | Inhibition of flavivirus, zika virus and dengue virus | Vázquez-Calvo et al. ([YEAR]) |
| Malvidin | 159287 | Anti-HIV and anti-RSV | Mohammadi Pour et al. ([YEAR]) |
| Pelargonidin | 440832 | Anti-HIV and anti-RSV | Mohammadi Pour et al. ([YEAR]) |
| Peonidin | 441773 | Anti-HIV and anti-RSV | Mohammadi Pour et al. ([YEAR]) |
| Phloridzin | 6072 | Antiviral, anticancer and cardioprotective agents | Gupte and Buolamwini ([YEAR]) |
| Arbutin | 440936 | Anti-inflammatory and antioxidant agent | Migas and Krauze-Baranowska ([YEAR]) |
| Phloretin | 4788 | Inhibition of zika virus | Lin et al. ([YEAR]) |
| Chalconaringenin | 5280960 | Immunomodulation, anti-inflammatory, antiviral, anticancer, and antimicrobial properties | Lee et al. ([YEAR]) |
In this study, we have taken 23 natural flavonoids and 25 anti-tubercularly active synthetic indole chalcones ( [REDACTED_AUTHOR] et al., [YEAR] ) and studied in silico for their potential anti-SARS-CoV-2 activity along with their physicochemical and absorption, distribution, metabolism, excretion, toxicity (ADMET) properties.


## Materials and methods

The molinspiration ([YEAR]) and pkCSM ( Pires et al., [YEAR] ) servers were used to analyse the pharmacokinetic properties of flavonoids. The crystal structures of proteins were acquired from the RCSB Protein Data Bank (PDB) based on resolution and R factors specifically 6M71, 6YB7, and 6LZG. Homology modelling of selected proteins of SARS-CoV-2 was performed using online server SWISS-MODEL ( Schwede et al., [YEAR] ). The quality of the protein structures was appraised by the Ramachandran plot ( Lovell et al., [YEAR] ) using PROCHECK ( Laskowski et al., [YEAR] ) webserver. The proteins were made ready using AutoDock Tools v.1.5.6. to remove unwanted co-crystallized molecules, to add charges (Gaussian, Gasteiger), and to incorporate polar hydrogens. Their energy minimized ligand data was developed on PerkinElmer Chem3D v15.0. Blind docking was achieved using AutoDock Vina v.1.1.2 ( Trott and Olson, [YEAR] ) and PyRx-Python Prescription v0.8 ( Dallakyan and Olson, [YEAR] ) to assist. Binding affinity for poses with RMSD lower than 2 Å was noted in kcal/mol. Post-docking analysis of protein-ligand interactions was conducted on BIOVIA Discovery Studio Visualizer v.19.1.0. ([YEAR]). The synthesis and characterization of indole chalcones were published already by us and the synthetic procedure is available in the literature ( [REDACTED_AUTHOR] et al., [YEAR] ).


## Results


## Pharmacokinetic investigation of flavonoids

Pharmacokinetic properties are an elemental segment of drug development to identify the biological properties of drug candidates. Lipinski's rule of five ( Lipinski et al., [YEAR] ) and Veber's rules ( Veber et al., [YEAR] ) were used to check the drug-likeness. Flavonoids given in Table 1 were analysed for their physicochemical properties and the results are epitomized in Table 2 . The ADMET characteristics of the flavonoids were studied to understand their pharmacokinetic profile and the results are given in Table 3 .


### Table 2: Physicochemical properties of flavonoids under study.

| Name | Lipinski's Rule of 5 | Veber's Rule |
| Log P | Mole. Wt. | Hydrogen donor | Hydrogen acceptor | No. of violations | Total polar surface area (Å 2 ) | No. of rotatable bonds |
| Luteolin | 1.97 | 286.24 | 4 | 6 | 0 | 111.12 | 1 |
| Apigenin | 2.46 | 270.24 | 3 | 5 | 0 | 90.89 | 1 |
| Tangeritin | 3.78 | 372.37 | 0 | 7 | 0 | 76.38 | 6 |
| Kaempferol | 2.17 | 286.24 | 4 | 6 | 0 | 111.12 | 1 |
| Quercetin | 1.68 | 302.24 | 5 | 7 | 0 | 131.35 | 1 |
| Myricetin | 1.39 | 318.24 | 6 | 8 | 1 | 151.58 | 1 |
| Fisetin | 1.97 | 286.24 | 4 | 6 | 0 | 111.12 | 1 |
| Hesperitin | 1.99 | 316.26 | 4 | 7 | 0 | 120.36 | 2 |
| Naringenin | 2.46 | 270.24 | 3 | 5 | 0 | 90.89 | 1 |
| Eriodictyol | 1.97 | 286.24 | 4 | 6 | 0 | 111.12 | 1 |
| Liquiritin | 0.41 | 418.40 | 5 | 9 | 0 | 145.91 | 4 |
| Genistein | 2.27 | 270.24 | 3 | 5 | 0 | 90.89 | 1 |
| Daidzein | 2.56 | 254.24 | 2 | 4 | 0 | 70.67 | 1 |
| Calophyllolide | 6.63 | 414.50 | 0 | 4 | 1 | 48.68 | 4 |
| Cyanidin | −0.75 | 287.25 | 5 | 6 | 0 | 112.31 | 1 |
| Delphinidin | −1.04 | 303.25 | 6 | 7 | 1 | 132.54 | 1 |
| Malvidin | −0.42 | 331.30 | 4 | 7 | 0 | 110.55 | 3 |
| Pelargonidin | −0.26 | 271.25 | 4 | 5 | 0 | 92.08 | 1 |
| Peonidin | −0.44 | 301.27 | 4 | 6 | 0 | 101.32 | 2 |
| Phloridzin | 0.40 | 436.41 | 7 | 10 | 1 | 177.13 | 7 |
| Arbutin | −1.36 | 288.25 | 6 | 8 | 1 | 139.84 | 3 |
| Phloretin | 2.66 | 274.27 | 4 | 5 | 0 | 97.98 | 4 |
| Chalconaringenin | 2.69 | 272.26 | 4 | 5 | 0 | 97.98 | 3 |

### Table 3: ADMET properties of flavonoids.

| Name | Absorption | Distribution | Metabolism | Excretion | Toxicity |
| Solubility Log S (log mol/L) | Caco-2 perm. (log Papp in 10 −6 cm/s) | Intestinal. absorption. (% Abs) | VDss (log L/kg) | Fraction. Unbound (Fu) | BBB perm. (log BB) | CNS perm. (log PS) |  | Total clearance (log ml/min/kg) | Hepato toxicity | Ames toxicity |  |
| Luteolin | −3.019 | 0.649 | 78.93 | 0.065 | 0.11 | −1.185 | −2.42 | CYP1A2, CYP3A4 inhibitor | 0.62 | No | No |  |
| Apigenin | −2.77 | 1.034 | 90.842 | 0.007 | 0.198 | −0.908 | −2.168 | CYP1A2, CYP2C19, CYP2C9 inhibitor | 0.661 | No | No |  |
| Tangeritin | −4.379 | 1.429 | 99.904 | −0.326 | 0.088 | −0.942 | −2.958 | CYP3A4 substrate, CYP1A2, CYP2C19, CYP2C9 inhibitor | 0.862 | No | No |  |
| Kaempferol | −3.191 | 0.879 | 82.139 | 0.234 | 0.125 | −1.189 | −2.36 | CYP1A2, CYP2C9 inhibitor | 0.649 | No | Yes |  |
| Quercetin | −3.262 | 0.737 | 69.799 | 0.361 | 0.067 | −1.453 | −3.403 | CYP1A2 inhibitor | 0.608 | No | No |  |
| Myricetin | −3.03 | 0.357 | 55.482 | 0.333 | 0.097 | −1.797 | −3.727 | CYP1A2 inhibitor | 0.598 | No | No |  |
| Fisetin | −3.155 | 0.777 | 80.112 | 0.2 | 0.094 | −1.175 | −2.382 | CYP1A2, CYP2C9, CYP3A4 inhibitor | 0.573 | No | No |  |
| Hesperitin | −3.34 | 1.145 | 74.297 | 0.448 | 0.087 | −1.369 | −3.314 | CYP1A2, CYP2C9 inhibitor, | 0.698 | No | Yes |  |
| Naringenin | −2.77 | 1.034 | 90.842 | 0.007 | 0.198 | −0.908 | −2.168 | CYP1A2, CYP2C19, CYP2C9 inhibitor | 0.661 | No | No |  |
| Eriodictyol | −3.019 | 0.649 | 78.93 | 0.065 | 0.11 | −1.185 | −2.42 | CYP1A2, CYP3A4 inhibitor | 0.62 | No | No |  |
| Liquiritin | −3.681 | −0.164 | 45.76 | −0.431 | 0.198 | −1.419 | −4.001 | No | 0.482 | No | Yes |  |
| Genistein | −2.945 | 0.942 | 91.714 | −0.029 | 0.154 | −0.9 | −2.187 | CYP1A2, CYP2C19, CYP2C9 inhibitor | 0.297 | No | No |  |
| Daidzein | −3.531 | 0.949 | 93.327 | −0.136 | 0.221 | −0.177 | −1.971 | CYP1A2, CYP2C19, CYP2C9, CYP2D6 inhibitor | 0.203 | No | Yes |  |
| Calophyllolide | −6.575 | 0.989 | 97.623 | 0.53 | 0.115 | −0.398 | −1.44 | CYP3A4 substrate, CYP1A2, CYP2C19, CYP2C9 inhibitor | 0.868 | No | No |  |
| Cyanidin | −3.192 | 0.799 | 78.013 | 0.304 | 0.05 | −1.395 | −2.354 | CYP1A2 inhibitor | 0.787 | No | No |  |
| Delphinidin | −3.003 | 0.707 | 65.867 | 0.227 | 0.073 | −1.747 | −3.545 | CYP1A2 inhibitor | 0.802 | No | No |  |
| Malvidin | −3.654 | 1.042 | 74.828 | 0.343 | 0.048 | −1.429 | −3.244 | CYP1A2, CYP2C9 inhibitor | 0.927 | No | No |  |
| Pelargonidin | −3.148 | 0.957 | 88.181 | 0.284 | 0.111 | −1.124 | −2.096 | CYP1A2, CYP2C19, CYP2C9, CYP3A4 inhibitor | 0.803 | No | No |  |
| Peonidin | −3.398 | 0.996 | 82.489 | 0.342 | 0.066 | −1.307 | −2.264 | CYP1A2, CYP2C19, CYP3A4 inhibitor | 0.857 | No | No |  |
| Phloridzin | −3.507 | 0.051 | 41.007 | 0.167 | 0.156 | −1.751 | −4.315 | No | 0.801 | No | Yes |  |
| Arbutin | −2.189 | 0.27 | 41.21 | −0.184 | 0.425 | −1.416 | −4.745 | No | 0.722 | No | No |  |
| Phloretin | −2.885 | 0.349 | 70.9 | −0.361 | 0.208 | −1.261 | −2.734 | CYP1A2, CYP2C9, CYP3A4 inhibitor | 0.263 | No | No |  |
| Chalconaringenin | −2.874 | 0.407 | 71.479 | −0.408 | 0.202 | −1.242 | −2.618 | CYP1A2, CYP2C9, CYP3A4 inhibitor | 0.163 | No | No |  |

## Homology of SARS-CoV-2 proteins

The SARS-CoV-2 proteins, namely RNA dependent RNA polymerase (PDB: 6M71 ), M pro (PDB: 6YB7 ) and Spike protein (PDB: 6LZG ) showed 96.348%, 96.078% and 72.778% sequence identity with rdrp NSP12 (PDB: 6NUR ), main protease (PDB: 2Z9J ) and spike protein (PDB: 2AJF ) respectively with SARS-CoV. The data indicated that 98.9% (M pro , PDB: 6YB7 ), 99.4% (spike protein, PDB: 6LZG ) and 99.9% (rdrp, PDB: 6M71 ) residues are in Ramachandran favoured regions. The Ramachandran plots for each protein are given in supplementary data.


## Protein-ligand docking studies

Analysis of protein-ligand docking revealed the following: Cyanidin binds at ASP761 catalytic residue on rdrp. Compounds C25, Daidzein, Eriodictyol, Fisetin, Genistein, Kaempferol, Myricetin, Quercetin, Arbutin, Chalconaringenin, Phloretin and Liquiritin interact on the spike proteins’ key RBD. Out of 48 compounds, 45 compounds from the library interact with M pro at important residues. The comprehensive list of drugs, their binding affinity and amino acid interactions can be found in the supplementary material in Fig. S1 and Table S2 respectively. The important results are discussed in detail in the subsequent sections.


## Discussion


## Pharmacokinetic investigation of flavonoids

Out of 23 natural flavonoids listed in Fig. 1 , nineteen flavonoids are showing no violation of the Lipinski's and Veber's rules and hence display druglike molecular (DLM) nature. The Log P values of 22 flavonoids are within the range of −1.36 to 3.78, while Calophyllolide shows one violation with a higher Log P value of 6.63. Molecular weight and number of H-acceptors of all flavonoids are within the accepted values of less than 500 and 10 respectively. Myricetin, Delphinidin, Phloridzin and Arbutin show violation in the number of H-bond donors. However, all the flavonoids are following the criteria of Veber's rules with total polar surface area (TPSA) values and the count of rotatable bonds within range for oral availability. The indole chalcones given in Fig. 2 are also obeying the aforementioned rules and show excellent DLM properties ( [REDACTED_AUTHOR] et al., [YEAR] ).


> **Fig. 1:** Natural flavonoids used in the current study.


> **Fig. 2:** Synthetic indole chalcones used in the current study.

The parameters for evaluating the drug absorption was solubility and Caco-2 permeability as listed in Table 3 . The solubility ranges from −6 to −2 indicating the moderate to the high solubility of flavonoids. The high water solubility can be due to 2–6 hydroxy groups present in each compound capable of forming bonds with water molecules. The human colonic adenocarcinoma cell line Caco-2 permeability of 10 compounds are high while myricetin, liquiritin, phloridzin, arbutin, phloretin, and chalconaringenin show poor permeation. The gastrointestinal absorption of the flavonoids is high except for phloridzin, arbutin and liquiritin which only show 40% absorption rate. The low absorption rate of compounds is a direct effect of its molecular size. However, an exception is Calophyllolide showing intestinal absorption of 97% despite its high molecular weight. The distribution of drug candidates considers the volume of distribution (VDss), blood-brain barrier (BBB) permeability, fraction unbound and central nervous system (CNS) permeability. The Log VDss values of less than 0.45 indicate the higher distribution of these drugs in plasma than in the tissues, except for Calophyllolide showing Log VDss vslue of <0.53. The fraction bound indicates the efficacy with which the compounds can diffuse. The compounds are not BBB permeant as none of the flavonoids has Log BBB >0.3. In the case of CNS penetration, 15 flavonoids have Log P values from −3 to −2 range, indicating moderate to high permeability. The ability to penetrate CNS is significant as there are reports of coronavirus targeting the CNS, owing to the presence of angiotensin-converting enzyme 2 receptors in neurons and glial cells ( Baig et al., [YEAR] ). The metabolism and total clearance of the flavonoids were analysed. The flavonoids showed no hepatotoxicity, while 5 compounds showed Ames toxicity and hence may be mutagenic. In a collective sense, the ADMET profile of the flavonoids is satisfactory and hence suitable for in silico studies with SARS-CoV-2 proteins.


## Homology of SARS-CoV-2 proteins and protein-ligand docking studies

Homology modelling revealed that the M pro , rdrp and Spike proteins of SARS-CoV-2 are remarkably similar to SARS-CoV in sequence, and their quality based on the Ramachandran plots was adequate for docking study. The anti-coronavirus drug design strategy can be classified based on different pathways of action. These can be the inhibition of proteins like M pro or enzymes which are required for viral RNA replication and synthesis (rdrp) or, the inhibition of structural proteins like spike protein for adhering to host cells by inhibiting the spike – angiotensin-converting enzyme 2 domain. Interactions between the docked ligands and proteins predict possible modes of action or lack thereof. The compounds with lower binding energy can have a higher affinity towards target proteins. The following sections cover significant docking results and analysis.


## RNA dependent RNA polymerase (rdrp)

The replication mechanism of SARS-CoV-2 is chiefly led by rdrp, a complex of nsp12, nsp8 and nsp7 ( Jacome et al., [YEAR] ; Tan et al., [YEAR] ). The structure resembles a partially curled right hand grip and can be assorted into three regions namely the palm, the thumb and the fingers ( Gao et al., [YEAR] ). This rdrp protein (PDB: 6M71 ) is largely carried over from SARS-CoV and provides certain targets of opportunity ( Elfiky, [YEAR] ; Gao et al., [YEAR] ; Yin et al., [YEAR] ) for the selected flavonoids. The key catalytic residue sequence of Ser759, Asp760, and Asp761 on the palm region is the binding site of RNA; assisted in part by Asp618 which is the divalent cation binding residue, these are essential to the replication ( Elfiky, [YEAR] ; Gao et al., [YEAR] ; Yin et al., [YEAR] ). Residues, Lys545 and Arg555 stabilize the incoming orientation of RNA while Lys500 and Ser501 mobilize to accommodate its approach ( Yin et al., [YEAR] ). In addition to these residues, 29–50 on β-hairpin of nsp12 are held responsible for rdrp structural stabilization by interacting with other domains of nsp12 ( Yin et al., [YEAR] ).

Post docking analysis shows that library members C4, C8, C12, C16, C17, C20, C22, C23, Calophyllolide, Genistein, Quercetin, Tangeritin, Arbutin and Liquiritin interact with β-hairpin residues (29–50). Unfortunately, literature to predict the outcome of these particular β-hairpin interactions in terms of rdrp function or stability is insufficient at present. However, it was encouraging to note that Cyanidin shows H-bonding with Asp761 (as shown in Fig. 3 ) at the RNA binding site with a binding affinity of −7.7 kcal/mol, suggesting that it may hinder the replication mechanism ( Yin et al., [YEAR] ).


> **Fig. 3:** Binding mode of Cyanidin to rdrp.


## Main protease (M pro )

Viral RNA is translated into various polyproteins by the action of the main protease (M pro ) in SARS-CoV-2 (PDB: 6YB7 ) ( Anand et al., [YEAR] ; Zhang et al., 2020b ). The human equivalent for this particular protease is absent, thus, this is a safe target for anti-SARS-CoV-2 agents. The M pro , in active form is a dimer of identical protomers ( Neuman et al., [YEAR] ; Yang et al., [YEAR] ; Zhang et al., 2020b ). Each protomer has 3 domains with the region between I and II being the main site of catalysis between residues, Cys145 and His41, while, the cleft between domains II and III is reserved for protomer dimerization ( Shi and Song, [YEAR] ; Zhang et al., 2020b ). The main catalytic site is shaped by the dimerization process which involves the residues between domains II and III ( Jin et al., 2020a ; Wei et al., [YEAR] ; Yang et al., [YEAR] ). Residues Met6, ARG4, Glu290, and Arg298 are responsible for this monomer-dimer behavior ( Wei et al., [YEAR] ; Zhang et al., 2020b ). Removal/mutation of these amino acids has shown the loss of M pro activation and reversion to protomer form ( Shi et al., [YEAR] ; Yang et al., [YEAR] ). Catalytic efficiency is regulated by residues 284–286 ( Zhang et al., 2020b ), special emphasis on Ala285 ( Shi and Song, [YEAR] ) which is credited with making M pro in SARS-CoV-2 several times more effective than its predecessor, SARS-CoV ( Wei et al., [YEAR] ). Mutation at Glu288 and Asp289 was also held responsible for disruption of M pro and certain other amino acids such as Lys5 interact with one or more of the aforementioned in a support capacity ( Shi et al., [YEAR] ). Post docking analysis was astounding as with the exceptions of Arbutin and Calophyllolide almost all the candidates show some form of desirable interaction. Forty compounds at protease regulatory sites and 30 at critical junctures are responsible for activation/shaping of the catalytic site, with 22 compounds common to both categories as shown in Fig. 4 .


> **Fig. 4:** Sites of compound interaction on M pro .

The key sites included are Glu288, Asp289, Glu290, and Lys5 whereas Ala285 and Leu286 are the regulatory sites of interaction. Except for C16 from indole chalcones and 7 flavonoids (Calophyllolide, Daidzein, Luteolin, Peonidin, Tangeritin, Arbutin and Phloridzin), all compounds interact with Leu286. The chalcones, C3 and C12 also interacted with Ala285. Overall, the flavonoids are more favourable with a maximum of three key residue interactions, whereas the indole chalcones are limited to a maximum of two. The best candidates were C23 indole-chalcone with a binding affinity of −10.4 kcal/mol interacting at Glu288, Asp289 and, the flavonoid Quercetin with an additional Glu290 interaction at −9.2 kcal/mol as given in Fig. 5 .


> **Fig. 5:** Binding mode of Mpro with (a) C23 in 3D (b) C23 in 2D with amino acid interactions (c) Quercetin in 3D (d) Quercetin in 2D with amino acid interactions.


## Spike (S) protein

An appealing SARS-CoV-2 target is a spike (S) protein, which attacks the human angiotensin converting enzyme 2 receptors ( South et al., [YEAR] ; Wang et al., [YEAR] , [YEAR] ; Zhang et al., 2020a ). Recent studies show us the spike protein is split into subunits S1 and S2 by the host proteases; S1 is made up of two domains one C-terminal (CTD) and an N-terminal (NTD) ( Wang et al., [YEAR] ). The CTD is used by SARS-CoV-2 to bind to, and, it is further divided into external and core subdomains ( Wang et al., [YEAR] ). This CTD external subdomain is made up of two β-strands attached to a flexible loop and, is primarily responsible for receptor recognition and binding ( Wang et al., [YEAR] ). Some of the residues that the external subdomain of SARS-CoV-2 S1 CTD uses to bind to the receptor include, Tyr453, Gly496, Gln498, Asn501, Gly502, Tyr503, and Tyr505 ( Wang et al., [YEAR] ).

These residues are pertinent as seen from the post-docking analysis of compounds. The compounds, C25, Daidzein, Eriodictyol, Fisetin, Genistein, Kaempferol, Myricetin, Quercetin, Arbutin, Chalconaringenin, Phloretin and Liquiritin, evidently all have one or more interactions with these residues. C17 and Luteolin have some minor interaction with residues Asn450 and Arg457 which are adjacent to key sites Tyr449 and Phe456 respectively ( Wang et al., [YEAR] ). Quercetin proved superior as it was most tightly bound with a −7.8 kcal/mol binding affinity at Gly496, Asn501, Tyr505 and Tyr453 residues as shown in Fig. 6 . These compounds, by occupying specific residues may show some effect in thwarting the spike protein's ability to bind and, warrant further study ( in vitro) of flavonoids as competitive inhibitors of the spike protein.


> **Fig. 6:** Binding mode of spike protein and Quercetin in (a) 3D (b) 2D with amino acid interactions.


## Structure-activity relationships (SARs)

The SARs of the compounds is derived from the interactions at M pro activation/dimerization site as given in Fig. 4 . This was possible for flavonoid compounds and M pro , as their large number of interactions provided ample data to interpret. The molecular weight, rotatable bonds and TPSA values of different categories of flavonoids may be similar and hence activity can be related to hydrogen bond donors and acceptors. The number and position of hydroxyl groups especially at 3, 3’ and 7 positions ( Anusuya and Gromiha, [YEAR] ) are significant in explaining the SARs of flavonoids and are marked in Fig. 7 .


> **Fig. 7:** The general structure of flavonoids.

The study includes flavonoids from seven subcategories. The flavones luteolin, apigenin, tangeritin are showing 3, 2, and 1 each respectively with the binding energy of −8.9 kcal/mol for both luteolin and apigenin. The lower binding energy and higher interactions (3 interactions) of apigenin and luteolin can be assigned to the existence of a hydroxy group at the 7th position of the basic flavonoid structure. The four bulky methoxy groups in tangeritin, however, reduces its interaction to only one protein and also contributes to the higher binding energy of −7.7 kcal/mol. The flavonols category had quercetin, myricetin, kaempferol and fisetin. Here, quercetin and myricetin show interactions with Glu288, Asp289 and Glu290 because of five hydroxyl groups with three –OH groups at 3, 3′ and 7 positions. Kaempferol has four hydroxyl groups with only 2 interactions with Glu288 and Asp289, owing to the absence of –OH at 3’ position. However, fisetin with four hydroxyl groups interacts with only one amino acid and has the highest binding energy of −8.7 kcal/mol. Flavones lack an additional –OH group at 3rd position, structurally discriminating them from flavonols and making them less active which is evident from the higher binding energies for same amino acid interactions.

In the case of flavanones, namely, hesperitin, naringenin, eriodictyol and liquiritin, even with the presence of 7 –OH groups, eriodictyol is not interacting with any key residues. The three key interactions of hesperitin can be attributed to the four free hydroxyl groups with three hydroxyl groups in 3, 3’ and 7 positions. The number of hydroxyl groups in naringenin is limited to three, with only two in favourable positions and thereby decreasing the number of amino acid interactions to two. However, the presence of beta-D-glucopyranosyl residue at 2nd position and the presence of only one hydroxyl group reduces the interactions of liquiritin to one interaction with Asp289. The result of interaction with isoflavanones was surprising, as daidzein shows interactions with three key amino acids, Glu288, Asp289 and Glu290; while genistein only interacts with Asp289, even though both have only one favourable hydroxyl group at the 7th position. The anthocyanins are structurally similar to flavonols, with the notable absence of C <svg xmlns="http://www.w3.org/[YEAR]/svg" version="1.0" width="20.666667pt" height="16.000000pt" viewBox="0 0 20.666667 16.000000" preserveAspectRatio="xMidYMid meet"><metadata> Created by potrace 1.16, written by Peter Selinger [YEAR]-[YEAR] </metadata><g transform="translate(1.000000,15.000000) scale(0.019444,-0.019444)" fill="currentColor" stroke="none"><path d="M0 440 l0 -40 480 0 480 0 0 40 0 40 -480 0 -480 0 0 -40z M0 280 l0 -40 480 0 480 0 0 40 0 40 -480 0 -480 0 0 -40z"/></g></svg> O in 4th position. Extending the same criteria to anthocyanins, cyanidin and peonidin show three interactions each, and, pelargonidin shows only one amino acid interaction. The lower binding energy of cyanidin (−8.7 kcal/mol) may be due to the presence of five free hydroxyl groups while peonidin (−8.4 kcal/mol) has four free hydroxyl and one methoxy groups.Moving on to chalcones, phloridzin with three hydroxyl groups and one glucoside ring showed three key interactions, followed by chalconaringenin with two key interactions. The indole chalcones were mainly limited to two key interactions. Out of 7 indole chalcones interacting with Glu288 and Asp289, five were heterocyclic compounds. The compound C9, with 3-NH 2 groups capable of H-bonding, also interacted with the aforementioned amino acids. Three indole chalcones, C3, C6 and C16 only interacted with Asp289. The reason for the lower interaction of indole chalcones when compared to flavonoids can be due to the absence of free hydroxyl groups. In a nutshell, the presence of hydroxy groups is favoring the interactions with key residues, while the position and number of hydrogen bonds are important in analyzing the inhibitory potential. The flavonoids and indole chalcones can be plausible agents against SARS-CoV-2 inhibition and the in vitro studies should be implemented to understand their anti- SARS-CoV-2 properties.


## Conclusion

Natural flavonoids and synthetic indole-chalcones were tested in silico for their pharmacokinetic properties and were validated as having druglike nature. This library was considered for tackling the modern-day issue of SARS-CoV-2 and further tested against homology modelled M pro , rdrp and S proteins. Analysis of protein-ligand docking revealed the following: Cyanidin may suppress rdrp by binding at Asp761 catalytic residue, halting the viral replication process. Compounds C25, Daidzein, Eriodictyol, Fisetin, Genistein, Kaempferol, Myricetin, Quercetin, Arbutin, Chalconaringenin, Phloretin and Liquiritin interact on the spike proteins’ key RBD and may inhibit spread to receptors limiting viral spread. The most encouraging result was that of M pro with a staggering 30 compounds capable of disrupting activation/dimerization of the protease. A whopping 40 compounds could lower the efficiency of M pro by action at regulatory residues. The indole-chalcones and flavonoids displayed the capability to suppress SARS-CoV-2 proteins and justify their further in vitro in vivo studies. Quercetin is an established anti-viral agent for dengue and influenza. It displayed strong interactions on SARS-CoV-2 proteins such as M pro at Glu290 and Asp289, as well as on receptor binding domain of the viral spike based on the computational analysis. These results echo the works on Quercetin by other researchers. Hence, Quercetin is an exceptional candidate for further in vitro/in vivo studies.


## Associated Data

