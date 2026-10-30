# FEXP_ANON_067

## Abstract

This study aims to discover drug targeted genes and explore the potential [REDACTED_VENUE] mechanisms in bronchiectasis. Cis-expression quantitative trait locus (eQTL) was obtained as exposure, and bronchiectasis from the FinnGen cohort was used as outcome. Mendelian Randomization (MR) was performed to identify therapeutic targets associated with bronchiectasis. Colocalization and summary-data-based MR (SMR) analyses were carried out to further confirm the causal roles of candidate genes in bronchiectasis. The value of these drug targets was validated via drug prediction and molecular docking. Finally, we used mediation analysis to identify the DNA methylation QTLs to bronchiectasis mediated by candidate genes. Ten drug targets were significantly associated with bronchiectasis. Strong evidence for the colocalization of ACVR2A and VRK2 with bronchiectasis was found (PP.H4 > 0.75). SMR analysis revealed that higher expressions of DDR1 and VRK2 were linked to a higher risk of bronchiectasis, and higher expressions of SCD5 , TNFRSF4 and XCL2 were linked to a lower risk of bronchiectasis. Finally, mediation analysis revealed potential causality effect of the DNA methylation site cg21568453 to bronchiectasis risk via VRK2 . The increased expression of VRK2 regulated by DNA methylation at cg21568453 may promote the occurrence of bronchiectasis.


## Introduction

Bronchiectasis is a chronic disease characterized by unusual enlargement or infection-related thickening, widening, and destruction of the bronchial tubes [ 1 ]. Epidemiological data highlight a notable increase in prevalence across Europe. In Germany, the rate has surged from 52.5 to 94.8 per 100,000 population between 2009 and 2017 [ 2 ]. Similarly, in the United Kingdom, there has been a significant rise from 350.5 to 566.1 per 100,000 women and from 301.2 to 485.5 per 100,000 men between 2004 and 2013 [ 3 ]. The global economic burden of bronchiectasis is vastly greater than previously estimated. According to a study in Germany, direct expenditures for patients with bronchiectasis were 31.0% higher than for matched controls, with costs of EUR 18,634.57 and EUR 14,236.99, respectively [ 4 ]. A systematic review and meta-analysis conducted in Europe, which included 16,963 patients with bronchiectasis from 28 countries, showed that European bronchiectasis patients bear a heavy disease burden, typically experiencing two exacerbations annually [ 5 ]. Hospital admissions are therefore frequent among bronchiectasis patients, imposing a significant economic burden on healthcare systems [ 4 , 6 ]. Daily cough, sputum production, and recurrent respiratory infections significantly impair the quality of life in patients with bronchiectasis, which eventually leads to a long-term decline in lung function and a high death rate [ 7 , 8 ]. Different causes contribute to the common complex interactions between host and environmental factors in bronchiectasis, and genetic determinants may be significant moderating or causative factors [ 9 ]. Treatment of bronchiectasis primarily consists of airway clearance therapies and antibiotic therapies. However, the responses of bronchiectasis patients to these treatments are inconsistent across several randomized controlled trials (RCTs) [ 10 , 11 ]. Thus, the identification of novel drug targets for the treatment of bronchiectasis via genetic-level techniques might guide us towards precision medicine and, subsequently, improve clinical outcomes.

RCTs are the gold standard for establishing an effective role of drug treatment. Regrettably, few large-scale, high-quality RCTs have examined the effects of drug targets on bronchiectasis, which may be explained by the cost and unfeasibility of RCTs. In recent years, Mendelian randomization (MR) has become an useful epidemiologic technique, providing new insights into causality. MR analysis has been applied to several diseases, such as Alzheimer’s disease [ 12 ], myopia [ 13 ], idiopathic pulmonary fibrosis (IPF) [ 14 ], chronic obstructive pulmonary disease (COPD) [ 15 ] and asthma [ 16 ], without requiring drug intervention. Genetic variants related to drug target messenger RNA expression or protein levels, also referred to as expression or protein quantitative trait loci (eQTLs or pQTLs, respectively), are frequently regarded as proxies of MR instruments for drug exposure. The MR analyses are likely to yield the most reliable results when the exposure variable represents the direct product of a coding gene region and the analysis is confined to genetic variants located within that specific genomic region [ 17 ]. Compared with genome-wide MR analyses (e.g., using variants associated with exposure in any region of the genome), biologically motivated MR analyses (particularly cis-MR analyses) have more plausible instrumental variable assumptions, and cis-MR analyses can be particularly suitable for specific intervention pathways [ 18 ]. However, no investigations have focused on the genomic evidence supporting a variety of possible pharmacological targets for bronchiectasis. The underlying mechanisms are not entirely understood beyond causality. Aberrant patterns of DNA methylation, an important epigenetic mechanism of transcriptional control, can also lead to development of many respiratory diseases [ 19–21 ]. Therefore, we hypothesize that DNA methylation of the specific genes might be involved in the pathological process of bronchiectasis.

In this study, we performed MR analyses by combining cis-eQTLs from a pool of 4479 druggable genes encoding drug targets with a genome-wide association study (GWAS) dataset of bronchiectasis, and subsequent colocalization, summary-data-based MR (SMR) and phenome-wide association studies (PheWAS) were conducted to offer insightful guidance for the development of more effective and targeted treatment approaches. To further explore the underlying mechanisms among gene methylation, gene expression, and bronchiectasis, a two-step mediation MR analysis was performed to investigate the relationship between methylation of candidate genes and bronchiectasis influenced by indirect factors of candidate genes.


## Materials and methods


## Exposure data

The list of druggable genes used in this study was derived from a previous study that used a computational approach that combined multiple sets of available GWAS data. A total of 4479 druggable genes were identified via this computational method, which sought to identify genes encoding proteins and connect them to well-known pharmaceutical agents [ 22 ]. Out of the 4,479 druggable genes, only 2,525 genes’ eQTL data in the blood were acquired by the eQTLGen consortium ( https://eqtlgen.org/ ), which comprises 16,989 genes from 31,684 blood samples of healthy European ancestors.


## Instrumental variables (IVs) selection

Three vital MR analysis assumptions must be met to guarantee the validity and accuracy of our findings [ 23 ]. First, instrumental variables (IVs) are highly correlated with exposure (relevance). Second, IVs are unaffected by any confounding factors (independence). Third, horizontal pleiotropy is absent, indicating that IVs influence the result solely through exposure and not via any other possible route (exclusion restriction, also known as ‘no horizontal pleiotropy’) [ 24 ]. Consistent with these presumptions, the selection criteria for IVs included the following steps: (1) Identification of single nucleotide polymorphisms (SNPs) associated with druggable genes at the locus-wide significance threshold ( p < 5.0 × 10 −8 ) as potential IVs to ensure strong link between IVs and druggable genes [ 25 ]; (2) To maintain the IVs’ independence and remove the linkage disequilibrium (LD) effect, we used a clumping approach with a window size of 10,000 kb and r2 < 0.1 [ 14 ]; (3) Since weak SNPs have the potential to skew two-sample MR results in favour of the null, we used an F-statistic threshold of larger than 10 to eliminate them [ 26 ]. The strength of IVs was estimated via the R 2 and F-statistic (R 2 = 2×(1− MAF)×MAF×(β/SD) 2 ; F=[R 2 ×(N−K − 1)]/[k×(1−R 2 )]) [ 27 ].


## Outcome data

We restricted the genetic background of the population in our drug target MR to individuals from European populations to prevent any potential bias resulting from diverse populations. We obtained publicly available case‒control GWAS summary data for bronchiectasis, with 2597 cases and 372,627 controls from the FinnGen consortium (R11) ( https://www.finngen.fi/en ).


## Mendelian randomization analysis

The R package ‘TwoSampleMR’ (version 0.5.11) was used to perform MR analysis. The Wald ratio was used if only one SNP was available as the IV. MR‒Egger, weighted median, weighted mode, inverse variance weighted (IVW), and simple mode were the five methods used when two or more IVs were available. The greatest statistical power is obtained by the IVW method, which assumes the validity of all the instruments [ 28 ]. Even when there are 50% invalid IVs, the weighted median approach accounts for their impact and produces a reliable evaluation [ 29 ]. The SNP pleiotropy criterion is loosened by the MR-Egger, and horizontal pleiotropy can be evaluated using its intercept. In the MR-Egger intercept test, the MR-Egger intercept term is compared to zero. Large horizontal pleiotropy is present when there is a significant disparity [ 30 ]. Due to simple and weighted mode methods have weaker statistical efficacy than IVW, they are mainly used to verify the robustness of IVW [ 31 ]. Thus, IVW was used as the main result when the results of the five MR methods were not consistent [ 32 ], and false discovery rate (FDR) <0.05 was considered significant [ 33 ]. The associations between the cis-eQTLs and the outcomes were obtained through the computation of odds ratios (ORs) and corresponding confidence intervals (CIs). For genes containing more than two IVs, the MR‒Egger intercept and Cochran’s Q tests were used to assess horizontal pleiotropy and heterogeneity, respectively. p < 0.05 indicated evidence of pleiotropy and heterogeneity.


## Phenome‐wide association analysis

PheWAS was conducted on the AstraZeneca PheWAS Portal ( https://azphewas.com/ ) to assess the horizontal pleiotropy of prospective therapeutic targets and potential side effects [ 34 ]. A subset of approximately 450,000 exome sequencing participants provided data of approximately 15.5K binary and 1.5K continuous phenotypes, which were published by the UK Biobank and used in the original study [ 34 ].


## Enrichment analysis

R (version 4.3.3) was used to conduct enrichment analysis for Gene Ontology (GO) and Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway enrichment, which was used to evaluate the functional attributes and biological significance of the identified potential therapeutic target genes. GO analysis includes molecular function (MF), cellular component (CC), and biological process (BP) categories, and the results of the KEGG enrichment analysis primarily highlight the enrichment of genes involved in metabolic pathways.


## Colocalization and SMR analysis

Using the ‘coloc’ R package (version 5.2.3), colocalization analysis was performed for genes whose MR correlations were significant. A total of five hypotheses were examined: H0 neither trait is associated, H1 only trait 1 is associated, H2 only trait 2 is associated, H3 both traits are associated, but two of them have different causal variants, and H4 both traits are associated, and the same shares causal variant for both traits [ 35 ]. Genes with strong colocalization were considered possible drug target candidate genes, with a posterior probability (PPH4) ≥0.75 indicating strong colocalization [ 36 ]. SMR analysis was performed as an additional technique to validate the causal relationships between gene expression and bronchiectasis [ 37 ]. Using multiple SNPs in a region, the heterogeneity in dependent instruments (HEIDI) test was used to identify genes linked to bronchiectasis risk due to shared genetic variants rather than genetic linkages. SMR software was used to conduct the SMR and HEIDI tests (SMR version 1.3.1). p < 0.05 of SMR test was established as the SMR significance level, and the p value of the HEIDI test, which was greater than 0.05, suggested that linkage disequilibrium was not the primary driver of the gene – bronchiectasis association [ 26 ].


## Candidate drug prediction

The large Drug Signatures Database (DSigDB, http://dsigdb.tanlab.org/DSigDBv1.0/ ) [ 38 ] contains 17,389 distinct compounds across 19,531 genes and 22,527 gene sets. To predict potential medications and assess the pharmacological activity of target genes, we uploaded previously discovered significant druggable genes to DSigDB to assess the pharmacological activity of target genes and potential medications.


## Molecular docking

The PubChem Compound Database ( https://pubchem.ncbi.nlm.nih.gov/ ) [ 25 ] provides drug structural data, which are downloaded in SDF format and subsequently converted to mol2 format via OpenBabel 3.3.1. We obtained protein structure information from the Protein Data Bank (PDB, http://www.rcsb.org/ ). AutoDock Vina 1.2.3 was utilized for molecular docking [ 39 ], and PyMol was used to further analyse and visualize the docking results.


## Mediated MR Analysis to determine DNA methylation regulation of candidate genes

To determine whether candidate genes were affected by methylation regulation in the development of bronchiectasis, we download DNA methylation QTL (mQTL) from GoDMC ( http://mqtldb.godmc.org.uk/downloads ), and the methylation sites of candidate genes were obtained from EWAS Data Hub ( https://ngdc.cncb.ac.cn/ewas/datahub/exploration ). We additionally carried out a two-step MR, and the first step involved determining the causal relationships between candidate genes (mediator) and mQTL (exposure). We calculated the causal relationships between candidate genes and bronchiectasis (the result) in the second step. The product of the effects from steps 1 and 2 of the two-step MR was then used to determine the indirect effect via candidate genes as a mediator. The IVW method was used to determine the causal estimates for both steps.


## Results


## Genetic-wide MR analysis identified 10 genes associated with bronchiectasis

A summary of the study design and the main findings are displayed in Figure 1 . The expression of 10 druggable genes was found to be significantly associated with bronchiectasis susceptibility at FDR < 0.05 via the IVW method ( Table 1 , Figure 2 ), and all 10 genes demonstrated a consistent direction of impact across the five methods (IVW, MR Egger, weighted median, simple mode, and weighted mode). ACVR2A , DDR1 and VRK2 act as risk factors for bronchiectasis, and CASP9 , SCD5 , ACLY , SOD2 , TNFRSF4 , XCL2 and SRPK1 are protective factors ( Table 1 , Figure 2 ). The results of MR-Egger regression (Additional file 1: Table S1) and Cochran’s Q test (Additional file 1: Table S2) revealed no pleiotropy or heterogeneity in IVs for significant genes. The R 2 and F-statistics values for the identified genes were provided in Additional file 1: Table S3. Figure 1. Overview of the study design. Figure 2. Forest plot of 10 significant genes related to bronchiectasis from blood. Table 1. Results of the five Mendelian randomization methods of 10 genes with bronchiectasis. Gene Methods nsnp Beta SE pval ACVR2A MR Egger 15 0.43 0.17 2.43E–02 Weighted median 15 0.45 0.11 3.91E–05 Inverse variance weighted 15 0.43 0.08 9.92E–08 Simple mode 15 0.39 0.18 5.09E–02 Weighted mode 15 0.45 0.12 1.86E–03 DDR1 MR Egger 27 0.17 0.08 5.61E–02 Weighted median 27 0.22 0.06 4.36E–04 Inverse variance weighted 27 0.22 0.05 1.98E–06 Simple mode 27 0.16 0.12 1.78E–01 Weighted mode 27 0.19 0.08 2.06E–02 VRK2 MR Egger 20 0.30 0.13 3.67E–02 Weighted median 20 0.33 0.10 6.01E–04 Inverse variance weighted 20 0.31 0.07 2.17E–06 Simple mode 20 0.20 0.17 2.38E–01 Weighted mode 20 0.32 0.09 2.47E–03 CASP9 MR Egger 25 −0.20 0.09 4.41E–02 Weighted median 25 −0.22 0.07 1.07E–03 Inverse variance weighted 25 −0.23 0.05 2.32E–06 Simple mode 25 −0.33 0.12 8.90E–03 Weighted mode 25 −0.21 0.07 4.32E–03 SCD5 MR Egger 33 −0.14 0.05 4.70E–03 Weighted median 33 −0.14 0.05 2.09E–03 Inverse variance weighted 33 −0.14 0.03 3.55E–06 Simple mode 33 −0.16 0.08 4.78E–02 Weighted mode 33 −0.15 0.04 1.59E–03 ACLY MR Egger 6 −0.46 0.23 1.13E–01 Weighted median 6 −0.53 0.13 7.32E–05 Inverse variance weighted 6 −0.51 0.11 3.83E–06 Simple mode 6 −0.54 0.19 3.83E–02 Weighted mode 6 −0.55 0.15 1.61E–02 SOD2 MR Egger 27 −0.16 0.06 8.87E–03 Weighted median 27 −0.14 0.06 1.46E–02 Inverse variance weighted 27 −0.19 0.04 6.16E–06 Simple mode 27 −0.19 0.11 9.98E–02 Weighted mode 27 −0.15 0.06 1.22E–02 TNFRSF4 MR Egger 9 −0.16 0.14 2.99E–01 Weighted median 9 −0.29 0.10 5.96E–03 Inverse variance weighted 9 −0.35 0.08 1.22E–05 Simple mode 9 −0.41 0.16 2.93E–02 Weighted mode 9 −0.28 0.11 3.13E–02 XCL2 MR Egger 26 −0.06 0.03 3.26E–02 Weighted median 26 −0.06 0.02 1.32E–02 Inverse variance weighted 26 −0.08 0.02 1.39E–05 Simple mode 26 −0.16 0.05 6.10E–03 Weighted mode 26 −0.07 0.02 9.05E–03 SRPK1 MR Egger 27 −0.15 0.12 2.29E–01 Weighted median 27 −0.25 0.09 3.63E–03 Inverse variance weighted 27 −0.26 0.06 1.57E–05 Simple mode 27 −0.28 0.16 9.24E–02 Weighted mode 27 −0.25 0.08 6.22E–03


> **Figure 1.:** Overview of the study design.


> **Figure 2.:** Forest plot of 10 significant genes related to bronchiectasis from blood.


### Table 1.: Results of the five Mendelian randomization methods of 10 genes with bronchiectasis.

| Gene | Methods | nsnp | Beta | SE | pval |
| ACVR2A | MR Egger | 15 | 0.43 | 0.17 | 2.43E–02 |
|  | Weighted median | 15 | 0.45 | 0.11 | 3.91E–05 |
|  | Inverse variance weighted | 15 | 0.43 | 0.08 | 9.92E–08 |
|  | Simple mode | 15 | 0.39 | 0.18 | 5.09E–02 |
|  | Weighted mode | 15 | 0.45 | 0.12 | 1.86E–03 |
| DDR1 | MR Egger | 27 | 0.17 | 0.08 | 5.61E–02 |
|  | Weighted median | 27 | 0.22 | 0.06 | 4.36E–04 |
|  | Inverse variance weighted | 27 | 0.22 | 0.05 | 1.98E–06 |
|  | Simple mode | 27 | 0.16 | 0.12 | 1.78E–01 |
|  | Weighted mode | 27 | 0.19 | 0.08 | 2.06E–02 |
| VRK2 | MR Egger | 20 | 0.30 | 0.13 | 3.67E–02 |
|  | Weighted median | 20 | 0.33 | 0.10 | 6.01E–04 |
|  | Inverse variance weighted | 20 | 0.31 | 0.07 | 2.17E–06 |
|  | Simple mode | 20 | 0.20 | 0.17 | 2.38E–01 |
|  | Weighted mode | 20 | 0.32 | 0.09 | 2.47E–03 |
| CASP9 | MR Egger | 25 | −0.20 | 0.09 | 4.41E–02 |
|  | Weighted median | 25 | −0.22 | 0.07 | 1.07E–03 |
|  | Inverse variance weighted | 25 | −0.23 | 0.05 | 2.32E–06 |
|  | Simple mode | 25 | −0.33 | 0.12 | 8.90E–03 |
|  | Weighted mode | 25 | −0.21 | 0.07 | 4.32E–03 |
| SCD5 | MR Egger | 33 | −0.14 | 0.05 | 4.70E–03 |
|  | Weighted median | 33 | −0.14 | 0.05 | 2.09E–03 |
|  | Inverse variance weighted | 33 | −0.14 | 0.03 | 3.55E–06 |
|  | Simple mode | 33 | −0.16 | 0.08 | 4.78E–02 |
|  | Weighted mode | 33 | −0.15 | 0.04 | 1.59E–03 |
| ACLY | MR Egger | 6 | −0.46 | 0.23 | 1.13E–01 |
|  | Weighted median | 6 | −0.53 | 0.13 | 7.32E–05 |
|  | Inverse variance weighted | 6 | −0.51 | 0.11 | 3.83E–06 |
|  | Simple mode | 6 | −0.54 | 0.19 | 3.83E–02 |
|  | Weighted mode | 6 | −0.55 | 0.15 | 1.61E–02 |
| SOD2 | MR Egger | 27 | −0.16 | 0.06 | 8.87E–03 |
|  | Weighted median | 27 | −0.14 | 0.06 | 1.46E–02 |
|  | Inverse variance weighted | 27 | −0.19 | 0.04 | 6.16E–06 |
|  | Simple mode | 27 | −0.19 | 0.11 | 9.98E–02 |

## PheWAS

According to the PheWAS results, certain diseases or characteristics are linked to genetically determined protein expression. None of the eight drug targets, except DDR1 and TNFRSF4 , were substantially linked to any other traits at the gene level (Additional file 1: Fig. S1 – Fig. S20), which indicates that the presence of horizontal pleiotropy in these genes and the possible adverse effects of medications acting on these targets are probably minimal, further demonstrating the validity of the study’s findings.


## Enrichment analysis

As shown in Figure 3a , the most significant pathways in the BP category were related to apoptosis and inflammation (the intrinsic apoptotic signalling pathway in response to DNA damage, the cellular response to interleukin-1, and the response to interleukin-1). Drug target genes in class CC were enriched for the caspase complex, nucleoid, mitochondrial nucleoid, endopeptidase complex, and azurophil granule lumen. With respect to MF, these genes also participate in apoptosis, such as cysteine-type endopeptidase activity involved in the apoptotic process, and death receptor activity. The top three pathways analysed by KEGG enrichment were lipid and atherosclerosis, biosynthesis of unsaturated fatty acids and cytokine‒cytokine receptor interaction ( Figure 3b ). Figure 3. Results of (a) GO and (b) KEGG enrichment for 10 genes.


> **Figure 3.:** Results of (a) GO and (b) KEGG enrichment for 10 genes.


## Colocalization analysis and SMR test

We performed colocalization analysis to determine the probability of cis-eQTL and bronchiectasis sharing a causal variant for the druggable genes with significant MR results. Colocalization analysis identified ACVR2A (PP.H4 = 0.922) and VRK2 (PP.H4 = 0.784) as shared causal variants with bronchiectasis susceptibility at threshold of PP.H4 > 0.75 ( Table 2 ). We conducted SMR and HEIDI tests for 10 genes with complete summary-level data to confirm the observed results. No association was found to be caused by a linkage in the SMR method, according to the HEIDI test ( p > 0.05, Table 2 ). Table 2. Summary results from MR, colocalization, and SMR for 10 MR-identified genes. Gene nsnp MR Colocalization SMR Category OR P FDR PPH4 OR P PHEIDI ACVR2A 15 1.54 9.92E–08 0.000 0.922 1.04 5.49E–01 7.74E–01 tier2 DDR1 27 1.25 1.98E–06 0.006 0.322 1.20 1.79E–02 4.04E–01 tier2 VRK2 20 1.36 2.17E–06 0.006 0.784 2.18 3.63E–03 2.95E–01 tier1 CASP9 25 0.79 2.32E–06 0.007 0.033 0.87 4.52E–01 1.16E–01 tier3 SCD5 33 0.87 3.55E–06 0.010 0.398 0.72 2.91E–03 7.58E–01 tier2 ACLY 6 0.60 3.83E–06 0.011 0.615 NA NA NA tier3 SOD2 27 0.83 6.16E–06 0.018 0.191 NA NA NA tier3 TNFRSF4 9 0.70 1.22E–05 0.035 0.189 0.58 8.86E–03 9.83E–01 tier2 XCL2 26 0.92 1.39E–05 0.040 0.166 0.82 1.73E–02 2.39E–01 tier2 SRPK1 27 0.77 1.57E–05 0.045 0.304 NA NA NA tier3


### Table 2.: Summary results from MR, colocalization, and SMR for 10 MR-identified genes.

| Gene | nsnp | MR |  |  | Colocalization | SMR |  |  | Category |
|  |  | OR | P | FDR | PPH4 | OR | P | PHEIDI |  |
| ACVR2A | 15 | 1.54 | 9.92E–08 | 0.000 | 0.922 | 1.04 | 5.49E–01 | 7.74E–01 | tier2 |
| DDR1 | 27 | 1.25 | 1.98E–06 | 0.006 | 0.322 | 1.20 | 1.79E–02 | 4.04E–01 | tier2 |
| VRK2 | 20 | 1.36 | 2.17E–06 | 0.006 | 0.784 | 2.18 | 3.63E–03 | 2.95E–01 | tier1 |
| CASP9 | 25 | 0.79 | 2.32E–06 | 0.007 | 0.033 | 0.87 | 4.52E–01 | 1.16E–01 | tier3 |
| SCD5 | 33 | 0.87 | 3.55E–06 | 0.010 | 0.398 | 0.72 | 2.91E–03 | 7.58E–01 | tier2 |
| ACLY | 6 | 0.60 | 3.83E–06 | 0.011 | 0.615 | NA | NA | NA | tier3 |
| SOD2 | 27 | 0.83 | 6.16E–06 | 0.018 | 0.191 | NA | NA | NA | tier3 |
| TNFRSF4 | 9 | 0.70 | 1.22E–05 | 0.035 | 0.189 | 0.58 | 8.86E–03 | 9.83E–01 | tier2 |
| XCL2 | 26 | 0.92 | 1.39E–05 | 0.040 | 0.166 | 0.82 | 1.73E–02 | 2.39E–01 | tier2 |
| SRPK1 | 27 | 0.77 | 1.57E–05 | 0.045 | 0.304 | NA | NA | NA | tier3 |
One gene passed all tests and was classified into tier 1 ( VRK2 ). Five genes that failed colocalization analysis or the SMR test or that could not be tested due to a lack of data ( ACVR2A, DDR1, SCD5, TNFRSF4 and XCL2) were classified into tier 2. Four genes ( CASP9, ACLY, SOD2 , and SRPK1 ) that were not included in either the colocalization analysis or the SMR test were classified into tier 3 ( Table 2 ).


## Drug prediction and molecular docking

We used the DSigDB database to predict potential effective intervention drugs for VRK2 . The top five potential chemical compounds are shown on the basis of adjusted p values ( Table 3 ). We used AutoDock 4.2.6 to analyse the binding sites and interactions between the top five candidate drugs and VRK2 . The amino acid residues and hydrogen bond lengths are shown in Figure 4 . Figure 4. Molecular docking results of VRK2 and the top five drugs. (a) WZ3105, (b) Flavopiridol, (c) Bosutinib, (d) Phenol and (e) SKI-606 Kinome Scan. Table 3. Docking results between top five small molecules and VRK2. Target PDB ID Drug PubChem ID VRK2 9FET WZ3105 42628507 VRK2 9FET Flavopiridol 5287969 VRK2 9FET Bosutinib 5328940 VRK2 9FET Phenol 996 VRK2 9FET SKI-606 Kinome Scan 20072150


> **Figure 4.:** Molecular docking results of VRK2 and the top five drugs. (a) WZ3105, (b) Flavopiridol, (c) Bosutinib, (d) Phenol and (e) SKI-606 Kinome Scan.


### Table 3.: Docking results between top five small molecules and VRK2.

| Target | PDB ID | Drug | PubChem ID |
| VRK2 | 9FET | WZ3105 | 42628507 |
| VRK2 | 9FET | Flavopiridol | 5287969 |
| VRK2 | 9FET | Bosutinib | 5328940 |
| VRK2 | 9FET | Phenol | 996 |
| VRK2 | 9FET | SKI-606 Kinome Scan | 20072150 |

## The methylation of cg21568453 promotes the risk of bronchiectasis by VRK2

We observed evidence of an indirect effect via VRK2 (beta = −0.064, p = 0.0055) using the IVW method, suggesting potential mediation of the DNA methylation at cg21568453 to bronchiectasis causality via VRK2 . The estimated proportion of the mediated effect via VRK2 was 0.54 (95% CI 0.16–0.92), indicating that any potential mediation via VRK2 would account for 54% of the total effect. The DNA methylation at cg21568453 in VRK2 was associated with lower expression of VRK2 ( Figure 5 ), which fitted with the negative effect of DNA methylation at cg21568453 on bronchiectasis ( Figure 5 ). Figure 5. The VRK2 mediated the causal effect of cg21568453 on bronchiectasis.


> **Figure 5.:** The VRK2 mediated the causal effect of cg21568453 on bronchiectasis.


## Discussion

Here, we perform a thorough analysis of the relationships between 4479 blood genes and the risk of developing bronchiectasis. By the discovery of genome-wide MR data, 10 gene markers were found, of which 3 genes with relatively high levels and 7 genes with relatively low levels were linked to an increased risk of bronchiectasis. To understand the biological significance and interaction mechanisms of these drug targets, we conducted GO and KEGG enrichment analysis. PheWAS was also used to further highlight the potential pleiotropy of the target genes and possible drug side effects. The causal relationship between VRK2 and the risk of bronchiectasis was further supported by colocalization and SMR analyses. Molecular docking and drug prediction were carried out to confirm the pharmaceutical value of VRK2 . Finally, we found that downregulation of DNA methylation at cg21568453 was associated with an increased bronchiectasis risk via increasing VRK2 expression levels.

The VRK family of serine/threonine kinases is involved in the control of chromatin remodelling, nuclear envelope formation, transcription factor expression, and cell cycle progression [ 40 ]. VRK1, VRK2, and VRK3 are the three vaccinia-related kinases (VRKs) [ 41 ]. Whereas VRK2 is located in the cytoplasm, VRK1 and VRK3 are found in the nucleus [ 42 ]. Many pivotal biological processes are regulated by VRK2 , including apoptosis [ 43 , 44 ], cell growth [ 45 ], immune responses [ 46 ], tumor cell invasion [ 47 ], and the response to hypoxic stress [ 48 ]. VRK2 knockdown prevents the growth of pulmonary adenocarcinoma by targeting miR-145-5p to regulate the ERK1/2/AKT signalling pathway [ 49 ]. However, the role of VRK2 in bronchiectasis has not been reported.

Bronchiectasis is caused by excessive neutrophilic airway inflammation that damages the bronchial wall, which in turn fuels additional airway inflammation and bacterial infection, resulting in a vicious cycle [ 1 ]. Polymorphonuclear neutrophils are necessary for antimicrobial defense during natural resolution [ 50 ], and these cells must subsequently undergo apoptosis and are eliminated from the inflammatory site by macrophages [ 51 ]. Otherwise, the capacity of neutrophils to effectively phagocytose and eliminate bacteria is impaired [ 52 ]. Research has demonstrated that there is reduced airway neutrophil apoptosis and longer airway neutrophil survival in bronchiectasis [ 52 , 53 ]. Delaying neutrophil apoptosis results in a prolonged period of inflammation, which postpones the clearance of neutrophils by macrophages. Interestingly, when serum from healthy volunteers is added to the blood of patients suffering from bronchiectasis, neutrophil viability decreases, and the rate of apoptosis increases [ 52 ]. Although the mechanism behind these alterations remains unclear, subjects with bronchiectasis may benefit from increased neutrophil apoptosis.

Previous studies have revealed that VRK2 induces the phosphorylation of Bcl-2, which facilitates its interaction with BAX and prevents apoptosis [ 44 ]. P53, which thought to induce apoptosis [ 54 , 55 ], have also been reported as substrates for VRK2 [ 56 ]. VRK2 might contribute to bronchiectasis development by influencing neutrophil apoptosis, yet additional experiments are necessary to verify this.

DNA methylation offers a chance to comprehend the mechanisms underlying gene regulation and disease. Findings from the current MR investigation suggested that the methylation of cg21568453 might decrease the expression of VRK2 and thus lower the bronchiectasis risk. However, further research is still needed to fully understand whether DNA methylation at cg21568453 regulates expression of VRK2 to influence the bronchiectasis risk in order to translate current research findings into clinical practice.

This study has several limitations. First, The absence of functional validation for the methylation sites of VRK2 in bronchiectasis poses a notable limitation. This gap underscores the need for further experimental studies to clarify the role of VRK2 methylation at cg21568453 in pathogenesis of bronchiectasis. Second, all the participants in the GWAS were of European descent, and the applicability of our findings to other populations may be limited by this restriction. Third, the expression of only a single druggable gene can be used to assess its effect on bronchiectasis independently via MR. Therefore, it is not possible to concurrently evaluate the superposition or interaction of multiple genes for bronchiectasis. Fourth, clinical trials cannot be entirely replaced by drug-targeted MR, so clinical trials are needed to assess the effectiveness and safety of VRK2 in the treatment of bronchiectasis. Fifth, setting the colocalization PP.H4 threshold at 0.75 may heighten the risk of false positives. Hence, we additionally utilized SMR analysis to bolster the robustness of our findings. Finally, there are multiple causes of bronchiectasis, but the bronchiectasis data we used do not disentangle these causes.


## Conclusion

Our findings yielded insight to understand that the methylation and expression level of VRK2 in the pathogenesis of bronchiectasis. Nonetheless, RCTs must be carried out to assess the safety and effectiveness of VRK2 -based interventions for bronchiectasis.


## Data availability statement

The cis-eQTL data were obtained from the eQTLGen Consortium ( https://www.eqtlgen.org/cis-eqtls.html ). The GWAS statistic for bronchiectasis was obtained from the FinnGen consortium (R11) ( https://www.finngen.fi/en ).The DNA methylation QTL (mQTL) were available from GoDMC ( http://mqtldb.godmc.org.uk/downloads ), and the methylation sites of candidate genes were obtained from EWAS Data Hub ( https://ngdc.cncb.ac.cn/ewas/datahub/exploration ).