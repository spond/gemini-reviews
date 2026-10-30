# De-Identified Manuscript: SP_ANON_033

> **Blinding Note:** All title, author, affiliation, journal, and identifier metadata have been scrubbed for unbiased methodological review.

## Abstract & Main Text

## Jun Yong Choi


## Sergei L [AUTHOR]


## Christy M Anderson


## Douglas D Richman


## Davey M Smith

Correspondence: J. Y. Choi, MD, PhD, Department of Internal Medicine, Yonsei University College of Medicine, 50 Yonsei-ro, Seodaemun-gu, Seoul 120–752, South Korea ( [EMAIL_REDACTED] ).

Corresponding author.

Received 2017 Jan 3; Accepted 2017 Apr 10; Issue date 2017 May 15.

To know how HIV variants are selected for transmission from a source partner and how they evolve in the recipient, we re-analyzed data from 58 transmission pairs, and identified several virologic factors for understanding into the biology of HIV transmission.

Keywords: HIV, transmitted virus, viral evolution, env .


## Abstract


## Background.

Investigations into which human immunodeficiency virus type 1 (HIV-1) sequence features may be selected for transmission during sexual exposure have been hampered by the small number of characterized transmission pairs in individual studies.


## Methods.

To boost statistical power to detect differences in glycosylation, length, and electrical charge in the HIV-1 V1–V4 coding region, we reanalyzed all available 2485 env sequences derived from 114 subjects representing 58 transmission pairs from previous studies using mixed-effects linear regression and an approach to approximate the unobserved transmitted virus.


## Results.

The recipient partner had a shorter V1–V4 region and fewer potential N-linked glycosylation sites (PNGS) than sequences from the source partner. We also detected a trend toward more PNGS and lower isoelectric points in transmitted sequences with source partner and the evolutionary tendency to shorten V1–V4 sequences, reduce the number of PNGS, and lower isoelectric points in the recipient following transmission.


## Conclusions.

By using all available well-characterized env sequences from transmission pairs via sexual exposure, we were able to identify several important virologic factors that may be important in the development of biomedical preventive interventions.

Human immunodeficiency virus type 1 (HIV-1) increases the number and varies the position of carbohydrates on its envelope glycoprotein to shield itself against antibody responses [ 1 , 2 ]. Insertions, deletions, and mutations within the variable loops of the HIV envelope protein can mediate escape from neutralization by monoclonal and polyclonal antibodies in sera, and alter co-receptor usage and infection efficiency to various target cell types [ 1 , 3–7 ].

The HIV-1 Env glycoprotein likely contributes significantly to the ability of a strain to establish infection in a new host following sexual exposure [ 8–10 ]; however, which envelope properties correlate with sexual transmission remains unclear. A previous report on 8 source-recipient heterosexual pairs infected with HIV-1 subtype C or G suggested that the selective bottleneck during transmission may favor envelope proteins with shorter V1–V4 regions, fewer glycans, and a greater susceptibility to neutralization by source partner autologous antibodies [ 9 ]. In another study involving heterosexual transmission of subtype A or D HIV-1, viral variants transmitted from the source partner had significantly shorter V1–V4 regions and less overall V3 charge but no significant difference in potential N-linked glycosylation site (PNGS) number [ 8 ]. Another report on HIV-1 subtype B transmission between 18 pairs of men who have sex with men (MSM) suggested that transmitted Env variants had shorter variable loops and fewer PNGS [ 11 ]. Some of these similarities may be evidence of a transmission bottleneck, although a transmission study of 14 MSM infected with subtype B HIV-1 found relatively few changes in neutralization sensitivity, glycosylation patterns, or genotypic modifications in envelope [ 12 ]. These studies have considered the transmitted strain to be the consensus sequence of the sampled viral population in the recipient [ 13 ]. However, this may be confounded by viral evolution in the recipient during replication unrestrained by host immune responses and most likely driven by target cell tropism and amplification during primary infection [ 14 , 15 ]. Additionally, analyses that do not correct for the effect of repeated correlated measurements, which are inherent in the analysis of clonal viral populations, may have also confounded the analysis of the transmitted variant because of unequal sampling across transmission pairs.

To improve the ability to detect differences in glycosylation, V1–V4 length variation, and electrical charge in the HIV-1 V1–V4 coding region of env across transmission pairs with varying risk exposures and HIV subtype infections, we reanalyzed all available env sequences with associated demographic and risk data from 114 subjects representing 58 transmission pairs.


## MATERIALS AND METHODS


## Selection of Articles and Data Collected

All published articles that reported HIV transmission pairs with sexual risk factors using search terms HIV , sexual , transmission , and pairs in PubMed as of October 2015 were searched. Studies that performed sequence analysis of the V1–V4 coding region of HIV-1 env were selected. Papers using population-based sequencing were also excluded. All of the relevant published sequences with accompanying subject identification were downloaded (GenBank accession numbers EU852934-EU853141 , AY423908-AY424198 , U50780-U50815 , DQ853426-DQ853435 , DQ853455-DQ853464 , FJ185853 - FJ187678 , and HQ162499-HQ162648 ). To identify factors associated with number of N-linked glycosylation sites, amino acid length, and isoelectric points of V1–V4, we also collected epidemiological and clinical data, including age, sex, mode of sexual transmission (MSM or heterosexual), source or recipient partner, HIV-1 subtype, and source of virus (blood plasma, blood cells, seminal plasma, or seminal cells). All available env sequences in the Los Alamos National Laboratory (LANL) HIV database ( http://www.hiv.lanl.gov , accessed 5 September 2016) that were annotated by sex of host, infecting subtype, and reported risk group were also examined.


## Sequence Alignment and Phylogenetic Analysis

Nucleotide sequences for each transmission pair were analyzed using a custom bioinformatics pipeline written, unless stated otherwise, as scripts for the [SOFTWARE] software package [ 16 ]. Each sequence was translated to amino acids and aligned to the HXB2 gp120 protein sequence using an HIV-1–specific protein scoring alignment matrix, namely, the 25% between host matrix [ 17 ]. Individual sequence features (V1–V4, C1–C4) were determined by extracting subsequences matching the corresponding coordinate ranges in HXB2, as defined in the LANL database. We reconstructed phylogenetic trees for source and recipient sequences with the neighbor-joining (NJ) method [ 18 ] under the Tamura-Nei distances [ 19 ] and bootstrapped them using 100 replicates. Each set of sequences was screened for evidence of intrahost recombination using GARD [ 20 ]. Next, we fitted the MG94xREV codon substitution model with a global dN/dS ratio to determine mean pairwise sequence divergence and mean selective forces within each host [ 21 ]. To represent each viral population with a single strain and obtain “intrapair” measurements of divergence, we computationally inferred center-of-tree (COT) sequences using the MG94xREV model fit, following the procedure previously described [ 22 ]. Finally, we aligned the inferred COT sequences using the Needleman-Wunsch dynamic programming algorithm with the HIV-1 protein scoring matrix, and merged the recipient and source multiple sequence alignments using the COT pairwise alignment as a guide. This alignment procedure conservatively biases source and recipient sequences against clustering together in the joint phylogenetic tree purely due to progressive alignment artifacts. We inferred the NJ tree (with 100 bootstrap replicates) for the joint pair alignment, and fitted the MG94xREV model where each branch in the tree is endowed with its own dN/dS ratio (the free-ratio model) [ 23 ] to estimate branch lengths and selective pressures, which are expected to vary from branch to branch [ 12 ]. We also estimated selective pressures by evolutionary fingerprinting each source and recipient sequence alignment [ 24 ]. The site-specific ratio of nonsynonymous to synonymous substitution rates (dN/dS) were used to identify the fingerprinting.

We evaluated correlations between the length, number of PNGS, and the isoelectric point of proteins sequences for all available and equilibrated sequence datasets. The equilibrated dataset means the subsample where each individual was represented by 6 clones, as the smallest number of sequence observations was 6 within one individual. We computed these descriptive statistics for the entire V1–V4 of HIV-1 env and for each of the individual coding regions (V1V2, C2, V3, C3, and V4). The number of PNGS was defined as the number of nonoverlapping occurrences of the N[not P][S or T][not P] motif in the sequence. We estimated the isoelectric point for each sequence using a nonlinear numerical optimization technique in [SOFTWARE] to solve the approximation based on the Henderson-Hasselbalch equation [ 25 ]. For this calculation, we did not include the charges on carboxyl or amino-termini of the polypeptide, since we were estimating isoelectric points for parts of longer polypeptides.


## Analysis of Sequence Difference Between Unobserved Transmitted and Other Viruses

We identified the single source and recipient sequences that were closest to each other phylogenetically. To better evaluate the virus that was transmitted from the source vs virus in the recipient that evolved following transmission, we evaluated the recipient and source viruses that were closest to each other (ie, “closest source” and “closest recipient”) vs the remaining sequences (ie, “other source” and “other recipient”). We hypothesized that (1) the single recipient and source viral variants that were closest to each other would more closely reflect transmitted virus; (2) the “closest source” vs “other source” sequences would more closely reflect the transmission bottleneck; and (3) the “closest recipient” vs “other recipient” sequences would more closely reflect evolution in the recipient.


## Statistical Analysis

To address the correlation of measurements within subjects and within transmission pairs, linear mixed-effects regression models were used to investigate the correlates of PNGS, length of V1–V4, and isoelectric points. Because subject is nested within transmission pair and each subject has >1 sequence, we captured these hierarchical dependencies by treating both transmission-pair identification and subject as random effects. Additionally, because 3 subjects belonged to >1 transmission pair, crossed random effects were used in the models. The following variables were treated as fixed effects: indication whether sequence came from recipient or source of transmission, transmission risk (MSM or heterosexual transmission pair), HIV-1 subtype, tissue origin, viral tropism, source of the data, average pairwise distance within subject, and distance to closest source sequence. To better evaluate the virus that was transmitted from the source vs the virus in the recipient that evolved following transmission, stratified linear mixed-effects regression models were also developed for recipients and for sources. Manual backward elimination was used to build all multivariate models, and variables were initially included in the multivariate models when P < .10 at the univariate level. Models were compared using Akaike information criteria and likelihood ratio tests. For analyses using the equilibrated dataset, independent Mann-Whitney (2 samples) or Kruskal-Wallis (>2 samples) tests were used to test for the difference of the number of PNGS, amino acid length, or isoelectric points of V1–V4 between various groups. All analyses were performed using the R package (version 2.9.0) [ 26 ].


## RESULTS


## Collected Sequences and Phylogenetic Linkage of Transmission Pairs

Nine studies met our eligibility criteria [ 8 , 9 , 11 , 12 , 21 , 27–30 ], and 6 [ 8 , 9 , 11 , 12 , 29 , 30 ] provided complete V1–V4 sequences, spanning reference (HXB2) coordinates 6615–7478 ( Table 1 ). Sequence data were collected from 58 transmission pairs (54 pairs and 2 triplets), comprised of 114 subjects. There were 2 examples of 1 source partner transmitting to 2 recipients. The number of sequences obtained from each individual in a partner pair varied greatly (Supplementary Table 1), ranging from 6 to 59 per individual.

Sources for This Analysis

| Year | No. of Subjects | Mode of Transmission | HIV-1 Subtypes | Title | Reference |
| 2005 | 12 | MSM | B | Characterization of human immunodeficiency virus type 1 (HIV-1) envelope variation and neutralizing antibody responses during transmissionof HIV-1 subtype B | [12] |
| 2009 | 26 | Heterosexual | A, D | Selection of HIV variants with signature genotypic characteristics during heterosexual transmission | [8] |
| 2004 | 16 | Heterosexual | C, G | Envelope-constrained neutralization-sensitive HIV-1 after heterosexual transmission | [9] |
| 1996 | 2 | MSM | B | Genetic characterization of human immunodeficiency virus type 1 in blood and genital secretions: evidence for viral compartmentalization and selection during sexual transmission | [29] |
| 2008 | 18 | MSM, heterosexual | B | Env length and N-linked glycosylation following transmission of human immunodeficiency virus type 1 subtype B viruses | [11] |
| 2009 | 40 | Heterosexual | A, C | Inflammatory genital infections mitigate a severe genetic bottleneck in heterosexual transmission of subtype A and C HIV-1 | [30] |
Abbreviations: HIV-1, human immunodeficiency virus type 1; MSM, men who have sex with men.

In 35 transmission pairs, source and recipient viral populations were reciprocally monophyletic with ≥70% phylogenetic bootstrap support [ 31 ]. In 20 pairs, the populations were intermixed in the joint phylogenetic tree, while in the remaining 3 cases (transmission pairs 18, 27, and 45), there appeared to be productive oligoclonal infections (Supplementary Figure 1).

The median pairwise genetic distance of the viral population in source samples was significantly greater than that in recipient samples ( P < .001, Mann-Whitney test). Evolutionary fingerprinting of the viral populations revealed molecular evidence of diversifying positive selection ( P ≤ .05) in 30 sources, but only in 7 recipients. These findings are consistent with the sampling of the recipients earlier in the course of infection than the sources.


## Mixed-Effects Regression Results for Sequence Features of PNGS, Length, and Isoelectric Point of V1–V4 Region

Because all sequences from a single host are correlated due to shared viral ancestry and sequences within transmission pairs may share similarities, biases are likely introduced to the analyses. To address the biases, we analyzed the dataset with the full set of sequence and then on a subset, where each partner contributed 6 (the minimum number of clones/host) randomly selected clones to the equilibrated dataset (n = 688) (Supplementary Table 2). As the smallest number of sequence observations was 6 within one individual, this resulted in a considerable loss of power; therefore, we performed a mixed-effects linear regression analysis to address the biases more.

At the univariate level ( Table 2 ), sequences from the recipient partner were more likely to have a significantly shorter V1–V4 region ( P = .001) and marginally fewer PNGS ( P = .053) than sequences from the source partner. Sequences belonging to MSM were more likely to have more PNGS ( P < .001) and longer V1–V4 ( P = .013) than those belonging to heterosexuals. HIV-1 subtype was significantly associated with PNGS ( P = .020) and length of V1–V4 ( P = .031). Sequences with subtype B had the largest number of PNGS (21.8), and subtypes A (20.7; P = .020) and C (20.3; P < .001) had significantly fewer. Excluding the 1 transmission pair that had an unknown subtype, sequences with subtype B had the longest V1–V4 (288), and sequences with subtypes C (282; P = .01), D (282; P = .022), and G (272; P = .027) had significantly shorter V1–V4. Sequences originating with seminal plasma had fewer number of PNGS ( P = .013) and lower isoelectric point ( P = .016) than those originating with blood plasma or peripheral blood mononuclear cells (PBMCs), and sequences with R5 phenotypes were more likely than those with X4 phenotypes to have shorter V1–V4 ( P = .014) and a lower isoelectric point ( P < .001). Further, analysis demonstrated that PNGS and V1–V4 length were significantly associated with the source of the data (ie, publication).

Fixed Effects Associated With Number of N-Linked Glycosylation Sites, Amino Acid Length, and Isoelectric Point in V1–V4 of Sequences of Transmitted Pairs in Univariate Linear Mixed-Effects Regression

|  | PNGS | Length of V1–V4 | Isoelectric Points |
| Variable | Marginal Mean (95% CI) | β | P Value | Marginal Mean (95% CI) | β | P Value | Marginal Mean (95% CI) | β | P Value |
| Partner transmission status |
| Recipient | 20.7 (20.3–21.1) | –.44 | .0525 | 283 (281–285) | –2.24 | .0013 | 8.0 (7.9–8.1) | –.04 | .3348 |
| Source | 21.2 (20.8–21.6) |  |  | 285 (283–287) |  |  | 8.1 (8.0–8.2) |  |  |
| Transmission risk |
| MSM (n = 16 pairs) | 21.8 (21.2–22.4) | 1.22 | .0008 | 288 (285–291) | 5.14 | .0133 | 8.1 (7.9–8.2) | .00 | .9924 |
| Heterosexual (n = 42 pairs) | 20.6 (20.2–21.0) |  |  | 283 (281–285) |  |  | 8.1 (8.0–8.2) |  |  |
| HIV-1 subtypes |
| A (n = 12 pairs) | 20.7 (20.0–21.4) | –1.10 | .0198 | 286 (282–289) | –2.37 | .0314 | 8.0 (7.8–8.2) | –.07 | .2004 |
| C (n = 17 pairs) | 20.3 (19.7–20.9) | –1.53 |  | 282 (278–285) | –6.15 |  | 8.1 (8.0–8.3) | .05 |  |
| D (n = 10 pairs) | 20.9 (20.1–21.7) | –.93 |  | 282 (277–286) | –6.34 |  | 8.0 (7.8–8.2) | –.03 |  |
| G a (n = 1 pair) | 20.6 (18.1–23.1) | –1.23 |  | 272 (259–286) | –15.8 |  | 8.2 (7.6–8.8) | .13 |  |
| Unknown b (n = 1 pair) | 20.9 (18.5–23.3) | –.93 |  | 289 (275–302) | .75 |  | 7.3 (6.7–7.9) | –.79 |  |
| B (n = 17 pairs) | 21.8 (21.2–22.4) |  |  | 288 (285–291) |  |  | 8.1 (7.9–8.2) |  |  |
| Tissue origin—seminal plasma |
| Blood plasma or PBMC (n = 2475 sequences) | 21.0 (20.6–21.3) | 1.41 | .0130 | 284 (282–286) | 3.64 | .0823 | 8.1 (8.0–8.1) | .32 | .0155 |
| Seminal plasma (n = 10 sequences) | 19.5 (18.4–20.7) |  |  | 281 (276–285) |  |  | 7.7 (7.5–8.0) |  |  |
| Viral tropism |
| R5 (n = 2257 sequences) | 20.9 (20.6–21.3) | –.10 | .5635 | 284 (282–286) | –1.61 | .0140 | 8.0 (7.9–8.1) | –.22 | <.0001 |
| X4 (n = 228 sequences) | 21.0 (20.6–21.5) |  |  | 286 (283–288) |  |  | 8.2 (8.1–8.3) |  |  |
| Source article |
| Liu et al [11] (n = 7 pairs) | 22.1 (21.2–23.0) | .49 | .0101 | 289 (284–294) | 1.65 | .0250 | 8.1 (7.9–8.4) | .09 | .9296 |
| Sagar et al [8] (n = 13 pairs) | 21.0 (20.3–21.7) | –.58 |  | 282 (279–286) | –5.24 |  | 8.0 (7.8–8.2) | –.06 |  |
| Derdeyn et al [9] (n = 8 pairs) | 20.2 (19.4–21.1) | –1.37 |  | 278 (274–283) | –9.26 |  | 8.1 (7.9–8.3) | .05 |  |
| Zhu et al [29] (n = 1 pair) | 21.8 (19.4–24.2) | .19 |  | 282 (268–296) | –5.59 |  | 7.9 (7.2–8.6) | –.14 |  |
| Haaland et al [30] (n = 20 pairs) | 20.4 (19.9–21.0) | –1.16 |  | 285 (282–288) | –2.75 |  | 8.1 (7.9–8.2) | .03 |  |
| Frost et al [12] (n = 9 pairs) | 21.6 (20.8–22.4) |  |  | 288 (283–292) |  |  | 8.0 (7.8–8.3) |  |  |
| APD of within host sequences |  | .01 | .7936 |  | .39 | .0191 |  | .01 | .4643 |
β = regression coefficient from linear mixed-effects model.

Abbreviations: APD, average pairwise distance; HIV-1, human immunodeficiency virus type 1; MSM, men who have sex with men; PBMC, peripheral blood mononuclear cell; PNGS, potential N-linked glycosylation sites.

a Suptype G exists as a recombinant of subtype A and CRF_02AG.

b Unknown subtype represents complex recombinant consisting of HIV-1 subtypes A1, F2, B, and D.

The results from multivariate modeling ( Table 3 ) showed a significant interaction between the subject-level characteristics of MSM/heterosexuals and source/recipient ( P = .0023). Specifically, there was no significant difference between the number of PNGS on sequences from recipients vs sources when they came from heterosexuals ( P = .899); however, the number of PNGS was significantly greater on sequences coming from sources who were MSM compared with sequences from recipients who were MSM ( P < .001). Furthermore, the association of greater numbers of PNGS for sequences originating with seminal plasma was marginally significant in the multivariate model ( P = .060). The univariate associations of MSM/heterosexual and recipient/source on PNGS persisted in multivariate modeling showing that sequences from MSM were more likely to have longer V1–V4 ( P = .012), while those from recipients were more likely to have shorter V1–V4 ( P = .001). When the association of MSM and recipient were considered simultaneously on PNGS, the effects of HIV-1 subtype, viral tropism, and the source of the data no longer had a significant association on the number of PNGS. The univariate association of tropism and tissue origin on the isoelectric point also persisted in the multivariate model. Namely, sequences with R5 genotypes were more likely to have a lower isoelectric point than those with X4 ( P < .001), and sequences from seminal plasma were more likely to have lower isoelectric point ( P = .026) than those from blood plasma or PBMCs ( Table 3 ).

Fixed Effects Associated With Number of N-Linked Glycosylation Sites, Amino Acid Length, and Isoelectric Point in V1–V4 by Multivariate Linear Mixed-Effects Regression Analysis

| Model | β | Standard Error | P Value |
| PNGS |
| MSM vs heterosexual | 2.01 | 0.25 | .0016 |
| Recipient vs source | –.03 | 0.45 | .0012 |
| Interaction: MSM–recipient | –1.53 | 0.48 | .0023 |
| Blood plasma/PBMCs vs seminal plasma | 1.23 | 0.75 | .0598 |
| V1–V4 length |
| MSM vs heterosexual | 5.12 | 2.04 | .0123 |
| Recipient vs source | –2.25 | 0.69 | .0012 |
| Isoelectric point |
| R5 vs X4 tropsim | –.22 | 0.04 | <.0001 |
| Blood plasma/PBMCs vs seminal plasma | .30 | 0.13 | .0257 |
β = regression coefficient from linear mixed-effects model.

Abbreviations: MSM, men who have sex with men; PBMC, peripheral blood mononuclear cell; PNGS, potential N-linked glycosylation sites.

To better evaluate the virus that was transmitted from the source vs the virus in the recipient that evolved following transmission, we performed a stratified analysis, developing separate mixed-effects models for recipients and for sources. Among recipients ( Table 4 ), larger genetic distances from the closest source partner sequence (ie, source partner sequence that is phylogenetically closest to the recipient partner sequences) to the recipient sequence were associated with fewer PNGS ( P < .001), while controlling for the average pairwise distance of the corresponding source ( P = .181) and the interaction between the 2 ( P < .001). The genetic distance between the closest source partner sequence and the recipient was not significantly associated with the length of the V1–V4 region ( P = .758) or the isoelectric point ( P = .315). Among recipients ( Table 4 ) nor sources (Supplementary Table 3), the average pairwise distance within subject was not significantly associated with the length of the V1–V4 region nor the isoelectric point.

Among Recipient Partners, Fixed Effects Associated With Number of N-Linked Glycosylation Sites, Amino Acid Length, and Isoelectric Point in V1–V4 in Univariate and Multivariate Linear Mixed-Effects Regression Analysis

| Variable | PNGS | Length of V1–V4 | Isoelectric Points |
| Univariate | Multivariate | Univariate | Multivariate | Univariate | Multivariate |
| β | P Value | β | P Value | β | P Value | β | P Value | β | P Value | β | P Value |
| Transmission risk |
| MSM | .48 | .2683 |  |  | 4.68 | .0458 | 5.00 | .0358 | .06 | .6003 |  |  |
| Heterosexual |  |  |  |  |  |  |  |  |  |  |  |  |
| HIV-1 subtypes |
| A | 1.83 | .3259 |  |  | 16.46 |  |  |  | –.19 | .0326 | .43 | .0661 |
| B | 2.13 |  |  |  | 17.56 |  |  |  | –.03 |  | –.01 |  |
| C | 1.20 |  |  |  | 11.24 |  |  |  | –.04 |  | –.04 |  |
| D | 2.06 |  |  |  | 11.61 |  |  |  | –.06 |  | –.09 |  |
| Unknown a | .81 |  |  |  | 16.96 |  |  |  | –1.31 |  | –1.31 |  |
| G b |  |  |  |  |  |  |  |  |  |  |  |  |
| Tissue origin |
| Blood plasma | –.02 | .6157 |  |  | –.03 |  |  |  | .00 | .9793 |  |  |
| PBMC |  |  |  |  |  |  |  |  |  |  |  |  |
| Viral tropism |
| R5 | .15 | .3587 |  |  | 1.30 | .0231 | 1.35 | .0183 | –.43 | <.0001 | –.09 | <.0001 |
| X4 |  |  |  |  |  |  |  |  |  |  |  |  |
| Source article |
| Liu [11] | –.25 | .2338 |  |  | .89 | .0117 |  |  | .12 | .8946 |  |  |
| Sagar [8] | –.17 |  |  |  | –5.22 |  |  |  | –.10 |  |  |  |
| Derdeyn [9] | –1.60 |  |  |  | –11.40 |  |  |  | –.08 |  |  |  |
| Zhu [29] | –.70 |  |  |  | –3.39 |  |  |  | –.17 |  |  |  |
| Haaland [30] | –.71 |  |  |  | –1.64 |  |  |  | –.01 |  |  |  |
| Frost [12] |  |  |  |  |  |  |  |  |  |  |  |  |
| Distance to closest source | –.19 | <.0001 | –.58 | <.0001 | .03 | .7581 |  |  | .01 | .3145 |  |  |
| APD of source sequences | –.08 | .3148 | –.13 | .1805 | .21 | .6415 |  |  | .02 | .8086 |  |  |
| Interaction between distance to closest source and APD of source sequences |  |  | .06 | .0009 |  |  |  |  |  |  |  |  |
| Interaction between subtype and tropism |
| A, R5 |  |  |  |  |  |  |  |  |  |  | –.73 | <.0001 |
| B, R5 |  |  |  |  |  |  |  |  |  |  | .15 | .6655 |
β = regression coefficient from linear mixed-effects model.

Abbreviations: APD, average pairwise distance; HIV-1, human immunodeficiency virus type 1; MSM, men who have sex with men; PBMC, peripheral blood mononuclear cell; PNGS, potential N-linked glycosylation sites.

a Unknown subtype represents complex recombinant consisting of HIV-1 subtypes A1, F2, B, and D.

b Suptype “G” exists as a recombinant of subtype A and CRF_02AG.


## Evaluating the Unobserved Transmitted Virus via Statistical Methods

In univariate analysis, when closest source sequences were compared to the rest of the source sequences, the closest source sequences had more glycosylation sites (21.35 vs 20.75; P = .012) and lower mean isoelectric point than other source sequences (7.94 vs 8.09; P = .002), but amino acid length in V1–V4 did not differ (284.90 vs 285.28; P = .708) ( Table 5 ). The closest recipient sequences had more glycosylation sites (20.79 vs 20.49; P = .001), longer V1–V4 (285.03 vs 283.69, P = .01), and higher isoelectric points (8.10 vs 7.97; P = .0001) than other recipient sequences.

Univariate Comparison of Number of N-Linked Glycosylation Sites, Amino Acid Lengths, and Isoelectric Points in V1–V4 Between Closest Source Sequences Versus Closest Recipient Sequences, Closest Source Sequences Versus Other Source Sequences, and Closest Recipient Sequences Versus Other Recipient Sequences

| Variable (No. of Sequences) | Mean No. of PNGS ± SD | P Value | Mean Amino Acid Length of V1–V4 ± SD | P Value | Mean Isoelectric Point ± SD | P Value |
| Closest source vs closest recipient |  | .751 |  | .439 |  | .947 |
| Closest source sequences (56) | 20.93 ± 1.75 |  | 283.93 ± 8.90 |  | 8.03 ± 0.41 |  |
| Closest recipient sequences (58) | 20.83 ± 1.65 |  | 282.66 ± 8.60 |  | 8.02 ± 0.43 |  |
| Closest sources vs other sources |  | .012 |  | .708 |  | .002 |
| Closest source sequences (89) | 21.35 ± 2.09 |  | 284.90 ± 8.51 |  | 7.94 ± 0.44 |  |
| Other source sequences (1144) | 20.75 ± 2.16 |  | 285.28 ± 9.32 |  | 8.09 ± 0.45 |  |
| Closest recipients vs other recipients |  | .001 |  | .01 |  | .0001 |
| Closest recipient sequences (555) | 20.79 ± 1.68 |  | 285.03 ± 9.98 |  | 8.10 ± 0.33 |  |
| Other recipient sequences (697) | 20.49 ± 1.39 |  | 283.69 ± 7.93 |  | 7.97 ± 0.50 |  |
Abbreviations: PNGS, potential N-linked glycosylation sites; SD, standard deviation.


## DISCUSSION

The ability to identify viral genetic elements that are conserved or selected for during the sexual transmission of HIV-1 could be very important in the development of biomedical prevention interventions, including vaccines or microbicides [ 9 , 10 ]. Previous HIV transmission studies have reported discordant findings, which may be explained by different modes of transmission, sex of hosts, HIV-1 subtype, stage of infection, number of clonal sequences generated, analytical method used, and anatomic source of virus. This study used multiple methods to analyze data from all available transmission cohorts to help clarify discrepancies between studies and provide a clearer indication of the factors in HIV-1 envelope associated with sexual transmission.

While it may be convenient to postulate that the transmitted variant simply is the most recent common ancestor or consensus sequence of the viral population sampled from a recently infected individual, most transmission pairs (60%) in this study had a significant evolutionary distance separating source and recipient sequences. Viral evolution continues in both source and recipient partners following transmission, and this evolution will not be negligible unless both partners are sampled densely and sufficiently close to the event. The degree of uncertainty about the identity of the transmitted strain (or strains) introduced by the within-host evolution or insufficient sampling coverage will differ from pair to pair, but it must be quantified. We evaluated various approaches to address these issues.

As might be expected, this study found that the univariate and multivariate analyses of these sequences can be biased when there are differing numbers of evolutionary correlated clones per host; therefore, we reanalyzed a subset of the sequences in which each host contributed an equal number of sequences to the dataset. To eliminate the bias of repeated sampling, we equilibrated the sample sizes of sequences, but this results in a considerable loss of observations. We then used mixed-effects analysis to evaluate these sequence features. In this analysis, viral subtype, exposure risk, virus in the recipient partner, tissue origin of the sample, and predicted viral tropism correlated with varying degrees with the length of V1–V4, the number of PNGS, and isoelectric point of Env. Some of these differences could represent true biological differences (eg the viral subtype); however, some of these factors were not completely congruent with comparative analyses performed on sequences annotated in the HIV LANL database (Supplementary Table 4). In the analyses of transmission pairs’ data, sequences from MSM had more PNGS and longer V1–V4 than sequences from heterosexuals, but isoelectric points were not different. In the analyses of LANL data, MSM had longer V1–V4, more PNGS, and lower isoelectric point than subjects with heterosexual risk. Sequences with subtype B had the largest number of PNGS, and it was consistent with LANL data. The identified factors may also represent selection biases inherent in the sampling of the transmission pairs, the HIV LANL database, or both, which may explain at least some of the conflicting results in previous studies.

Previous studies suggested differences in the biology of sexual transmission between viral subtypes. The transmission of subtype A and C viruses (but not B) appears to favor compact variable loops [ 9 , 10 , 12 ]. Additionally, comparisons between subtype B and C envelope sequences collected during acute or early infection demonstrated that subtype C gp120 sequences were shorter and had fewer glycosylation sites than acute or early subtype B sequences [ 13 , 32 ]. These differences were also apparent in analyses using subtype B and C sequences collected during chronic infection from the LANL HIV database (Supplementary Table 4). Despite the remaining discrepancies, however, our analyses showed that sequences from source partners had virus with longer V1–V4 coding regions and more PNGS than those from recipient partners even after adjusting for infecting subtype ( Table 3 ).

Evaluating sequences from the source partners permits an estimation of the viral variants at risk for transmission, while evaluating sequences from the recipients permits an estimation of evolution that occurred in a recipient following transmission. To distinguish between the potential bottleneck from the source partner and evolution in the recipient following transmission, we used source and recipient sequences that were phylogenetically closest to each other and compared them to the rest of the source and recipient sequences. We hypothesized that sampling the virus from the shortest phylogenetic paths connecting source and recipient sequences would be a reasonable approach to reflect the uncertainty due to unobserved evolution.

Comparisons between the one source sequence that was closest to the matched recipient sequences with all other source sequences—that is, potential transmission bottleneck—found that the transmitted variant has more PNGS and lower isoelectric point ( Table 5 ). The reason for selective transmission of a viral variant with more PNGS and lower isoelectric points remains unclear, but may reflect the biologic origin of the transmitted viral variant during sexual exposure. For example, the viruses most representative of transmitted variants may have more glycosylation sites and lower isoelectric points than the rest of the source viruses only for male source partners. In addition, viral sequences derived from seminal plasma had more glycosylation sites and lower isoelectric points than sequences derived from blood, consistent with the putative transmitted variant ( Table 2 ), but as only 10 sequences were available from seminal plasma, no robust conclusions can be made.

The recipient viruses demonstrated evolution, likely in the absence of neutralizing antibody response, and consisted of shorter V1–V4 coding regions and fewer glycosylation sites ( Table 5 ). Although the functional effect of this change remains unclear, a compact V1–V4 region with fewer glycans could increase exposure of the CD4 and CCR5 binding domains [ 33–36 ], and perhaps enhance the HIV entry process [ 36 ]. These early changes in the viral population while it is expanding in the new host perhaps confounded previous studies, which evaluated the viral population only during recent infection [ 13 ].

In this meta-analysis, the recipient partner had shorter V1–V4 region and fewer PNGS than sequences from the source partner. In addition, transmitted virus had a tendency to have more PNGS and lower isoelectric points than virus that was not transmitted. Once transmitted, however, the virus evolved in the recipients to create viral populations with shorter length in the V1–V4 coding region, reduced number of PNGS, and lower isoelectric points. This could benefit the virus to increase exposure of the CD4 and chemokine receptor binding sites, and could be explained by evolution toward enhanced viral entry into CD4 + lymphocytes at a time when no countervailing selective pressures are exerted by the humoral immune response (ie, high levels of replication during acute infection) [ 37 ]. These findings might help to guide the rational design of effective vaccines or microbicides.


## Supplementary Data

Supplementary materials are available at [JOURNAL REDACTED] online. Consisting of data provided by the authors to benefit the reader, the posted materials are not copyedited and are the sole responsibility of the authors, so questions or comments should be addressed to the corresponding author.
