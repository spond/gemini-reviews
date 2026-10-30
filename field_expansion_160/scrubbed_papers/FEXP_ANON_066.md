# FEXP_ANON_066

## Abstract

Asthma, a chronic respiratory disease affecting millions worldwide, poses a significant public health burden. Cathepsins, a group of proteolytic enzymes, have recently been implicated in asthma pathophysiology, though their exact causal role remains unclear. To address this gap, we conducted univariate and multivariate Mendelian randomization (MR) analyses using data from the INTERVAL study (3301 European ancestry participants) and FinnGen consortium (46,684 asthma cases and 219,734 controls). Our analysis employed inverse variance weighting (IVW), median weighting, and MR-Egger regression to ensure robustness and explore causality from multiple perspectives. Sensitivity analyses were performed to assess heterogeneity and pleiotropy.Results indicated a significant association between elevated cathepsin L2 levels and increased asthma risk (OR 1.058, 95% CI 1.016–1.101, P = 0.006), suggesting a potential role of cathepsin L2 in asthma pathogenesis. No significant effect of asthma status on cathepsin L2 levels was observed ( P = 0.550), ruling out reverse causality. Multivariable MR further confirmed the independent association of cathepsin L2 with asthma risk. Sensitivity analyses supported these findings with no evidence of significant pleiotropy.This study is the first to apply Mendelian randomization to explore the causal relationship between cathepsins and asthma, highlighting cathepsin L2 as a key player in asthma pathophysiology. These findings offer novel insights into asthma mechanisms and suggest cathepsin L2 as a potential therapeutic target warranting further investigation.

The online version contains supplementary material available at [REDACTED].

Keywords: Asthma, Cathepsin, Mendelian randomization analysis, Causality

Subject terms: Genetics, Diseases, Risk factors


## Introduction

Asthma is a chronic respiratory disease characterized by inflammation of the airways, enhanced bronchial responsiveness, and variable airflow obstruction 1 . As a common chronic respiratory disease, asthma greatly affects the quality of life of millions worldwide 2 . In extreme cases, this illness may trigger serious health events, including death 2 . The prevalence and severity of the disease pose a remarkable challenge to global health systems and burden socio-economic development 3 . Despite the significant progress that has been made in asthma research over the year, the definite cause of the disease is still not completely known. Recently, emerging evidence has pointed toward an important role that cathepsins might play in the pathologic pathways of asthma 4 , 5 .

Cathepsin, which is a protease or proteolytic enzyme group member, is found in all parts of the human body and is responsible for the organism’s core functions.Different studies note such a big variety of isoforms of cathepsin that bring the organism into function, starting from the basic level-protein breakdown to the most complicated ones 6 , 7 . Cathepsin S is highly expressed in the airways of asthmatic patients, as extensively reported 8 .Furthermore, there is evidence from studies that cathepsins like cathepsin S and cathepsin B might directly link airway remodeling and the initiation of inflammation in asthma 9 , 10 . These studies have, indeed, shed light on the functions of cathepsins in asthma; however, individual antecedent environmental factors, genetic predispositions, and lifestyle choices may have confounded the findings or affected them otherwise. Moreover, misleading results could have originated from reverse mechanism leading to causal links. Looking at it from this side, the question arises that whether cathepsins are the major determinants of asthma or other factors either environmental, genetic, or lifestyles play a key role. Causal inferences of associations between exposure factors and disease outcomes were performed using MR analysis.

Mendelian Randomization (MR) analysis was used to elucidate causal associations between exposure factors and disease outcomes.By using genetic variants as instrumental variables, this method aims to effectively control confounding factors and reverse causality, providing more reliable evidence for causal inference between exposure factors and disease outcomes 11 .The advantage of MR is that it utilizes the random assignment characteristics of genetic variation, simulating the conditions of randomized controlled trials and effectively reducing potential bias in observational studies 12 .This method has been widely used in various research fields, especially in studying the etiology of complex diseases, providing a new approach to reveal potential causal relationships 13 .

The current study was designed to investigate the probable cause-effect relationship between the occurrence of asthma and the level of cathepsins by the univariate and multivariate Mendelian Randomisation approaches. The investigators applied the results from genome-wide association studies to recognize the gene variants which connect to cathepsin production to work as instrumental variables for estimating the impact they have on asthmatic risk. These findings further the understanding of asthma pathogenesis and perhaps may indicate new molecular targets for future therapeutic intervention.


## Methods


## Study design

Figure 1 presents a summary of the study design. The authors used two-sample mendelian randomization to test the causal effect of cathepsin on asthma. In the Mendelian randomization analysis, genetic variants previously linked to cathepsin expression were selected as instrumental variables. Nine cathepsins were prioritized based on existing evidence of airway involvement and data availability.Here, cathepsin served as the exposure variable, while asthma was the outcome variable (Data sources are detailed in Table 1 ).These are expressed as follows: Hypothesis 1: There is a significant association between genetic instrumental variables and cathepsins. Hypothesis 2: The genetic instrumental variables are not significantly associated with factors other than cathepsins and asthma. Hypothesis 3: Genetic instrumental variables influence asthma risk only through cathepsins 14 .The research was performed in accordance with the international ethical rules, and additional agreement from the institutional review board was not necessary as the investigation used only publicly accessible data abstracts.


> **Fig. 1:** The Mendelian randomization study design. MR assumptions: assumption 1, 2 and 3. ① Cathepsins genetic instrument variants are reliably associated with cathepsins levels and influence the risk of asthma through the cathepsins in assumptions 1; ② Cathepsins genetic instrument variants are not associated with any measured or unmeasured confounders in assumption 2 and in assumption 3; ③ genetic instruments affect the outcome only via the exposure.


### Table 1: Data sources for cathepsins and asthma.

| Trait name | Data sources | Population | Samplesize | PMID or GWAS |
| exposure | Cathepsin B | The INTERVAL study | European | 3,301 | 29,875,488 |
| Cathepsin E | The INTERVAL study | European | 3,301 | 29,875,488 |
| Cathepsin F | The INTERVAL study | European | 3,301 | 29,875,488 |
| Cathepsin G | The INTERVAL study | European | 3,301 | 29,875,488 |
| Cathepsin H | The INTERVAL study | European | 3,301 | 29,875,488 |
| Cathepsin O | The INTERVAL study | European | 3,301 | 29,875,488 |
| Cathepsin S | The INTERVAL study | European | 3,301 | 29,875,488 |
| Cathepsin L2 | The INTERVAL study | European | 3,301 | 29,875,488 |
| Cathepsin Z | The INTERVAL study | European | 3,301 | 29,875,488 |
| outcome | Asthma | FinnGen | European | 266,418 | J10_ASTHMA_EXMORE |

## Data sources for cathepsins

Genetic variant data for nine cathepsins were obtained among 3,301 individuals of European ancestry from the INTERVAL study 15 . For each cathepsin, SNPs significantly associated with its serum or tissue levels were identified. The following approaches were used to increase the robustness: only SNPs that reached genome-wide significance ( P < 5 × 10 − 6 ) were selected as instrumental variables 16 ; the physical distance in the genome between the selected SNPs was ensured to be more than 10,000 kb to reduce the possible effect of linkage disequilibrium; LD R 2 among the selected SNPs was less than 0.001, ensuring independence of genetic variation; and SNPs with palindromic structures were excluded to avoid possible bias in the analysis. SNPS for exposure data are detailed in (Supplementary Table S1 ).


## Asthma data sources

Asthma GWAS data from the FinnGen database including 46,684 asthma cases and 219,734 controls 17 . Project FinnGen is a broadly consented research resource that combines clinical data from health registries, genetic data and biobank samples from Finland with the aim to study genetic background of diseases 18 . The goal of this investigation was to find the genetic relationship between the SNPs found in the cathepsin GWAS and the possibility of getting asthma, which was accomplished by using the GWAS summary data extracted from the FinnGen database.


## Selection of instrumental variables

Our exclusion of SNPs that were barely related to exposure factors was followed by the selection of instrumental variable (IVs) and its validation through F-statistics. The F-statistic is found from the formula 19 , 20 :

Where, R 2 is the proportion of genetic variation explaining the variance of the exposure factors, N is the sample size, and K is the number of instrumental variables 21 . Where F value > 10, there is no significant weak instrument bias in the IVs 22 . While the F-statistic threshold mitigates weak instrument bias, future studies should validate these SNP-cathepsin associations in multi-ethnic populations to ensure generalizability.


## MR analysis and sensitivity analysis

In this study, inverse variance weighting (IVW) was selected as the primary Mendelian randomization (MR) analysis to assess the causal effect between cathepsin levels and asthma risk 23 .Additionally, MR-Egger regression, weighted median method, simple pattern method, and weighted pattern method were used as supplementary analyses 24 – 27 .These methods aim to assess causality from different perspectives, ensuring multi-angle validation of the results.To ensure the robustness of the results and explore potential pleiotropy, multiple sensitivity analyses, including MR-Egger regression, weighted median method, and MR-PRESSO method, were performed 28 , 29 . MR-PRESSO identified outliers using a 10% significance threshold for distortion testing, with P < 0.05 for the global test of pleiotropy.These methods were chosen for their ability to identify and correct potential bias in MR analysis.Cochran’s Q statistic was used to assess heterogeneity between genetic instrumental variables.This meta-analysis detects whether the instrumental variables show inconsistent effect sizes; a p-value less than 0.05 suggests that the basic assumption of the IVW method may be violated 30 .Additionally, the intercept of the MR-Egger regression was used to detect horizontal pleiotropy, as significant intercepts may indicate pleiotropy bias. To further explore genetic variants which may be impacted by single genetic variants, leave-one-out analyses were produced.

Furthermore, we applied reverse MR analysis to estimate the potential for asthma to cause cathepsin, so we made asthma as the exposure and cathepsin as the outcome factor. Power calculations for the reverse MR analysis confirmed > 80% power to detect OR ≥ 1.10, aligning with the forward MR study design .Thus, we were able to estimate the potential for reverse causality observing the possible bidirectional causality listed above. In these reverse MR analyses, the same GWAS dataset was used, and asthma-related instrumental variables were selected from the Finnish databases, while cathepsin expression levels from the INTERVAL study were used as the outcome measure. Reverse MR SNPs were filtered to exclude associations with non-asthma respiratory phenotypes using PhenoScanner V2.To investigate the possible confounding among the nine cathepsins, we also conducted MVMR analysis. The purpose of this MVMR analysis was to study the independent causal effects of various cathepsins on the risk of asthma and further to adjust for the pleiotropic effect among them 12 .

In this study, all statistical analyses were performed using R software, version 4.2.2, with packages “TwoSampleMR (version 0.5.7)” and “MRPRESSO (version 1.0)”. In the current study, the level of significance was considered at a probability level of 0.05. The results are presented as odds ratios (ORs) and 95% confidence intervals (CIs) where applicable.


## Results


## Selection of IVs

This dataset comprised genetic variants for nine cathepsins, each with F-statistics exceeding 10 for the chosen instrumental variables (IVs). Specific details of the instrumental variables used are included within Table S2 of the supplementary material.


## MR analysis and sensitivity analysis

The results from univariate MR revealed that cathepsins are causally related to the risk of asthma. In this study, a total of nine cathepsins were investigated, and their estimated causal association with asthma is shown in (Fig. 2 ). IVW analysis suggested that higher cathepsin L2 was significantly associated with increased asthma risk (OR = 1.058, 95% CI 1.016–1.101, P = 0.006), suggesting that genetically higher levels of cathepsin L2 are associated with a higher risk of asthma. For the remaining cathepsins, the IVW method did not reveal any significant causal association with asthma risk ( P > 0.05).


> **Fig. 2:** Forest plots of univariable Mendelian randomization analysis of the relationship between cathepsins and asthma. IVW inverse varients weighting, CI confidence interval.

Furthermore, MR-Egger regression analysis did not provide any significant evidence of directional pleiotropy (intercept = 0.016, p = 0.090), indicating that pleiotropy is unlikely to bias the results (Table 2 ). In the heterogeneity test, we found that both MR-egger and inverse variance weighting methods showed statistical P > 0.05 (Table 3 ). Leave-one-out analysis showed that the results of individual SNPs across zero line, which suggest potential heterogeneity (Supplementary Figure S1 ). However, MR-PRESSO analysis did not detect any abnormal value, and total test for heterogeneity was not significant ( p = 0.387), which indicated no significant pleiotropy or heterogeneity among the selected instrumental variables (Supplementary Table S3 ).


### Table 2: Pleiotropy test of cathepsins L2 genetic variants in the risk of Asthma.

| Outcome | Exposure | Egger_intercept | se | pval |
| Asthma | Cathepsin B | 0.016 | 0.008 | 0.049 |
| Asthma | Cathepsin E | 0.011 | 0.006 | 0.102 |
| Asthma | Cathepsin F | 0.008 | 0.008 | 0.335 |
| Asthma | Cathepsin G | (0.007) | 0.008 | 0.369 |
| Asthma | Cathepsin H | 0.006 | 0.005 | 0.239 |
| Asthma | Cathepsin O | 0.006 | 0.008 | 0.460 |
| Asthma | Cathepsin S | 0.000 | 0.005 | 0.986 |
| Asthma | Cathepsin L2 | 0.016 | 0.009 | 0.090 |
| Asthma | Cathepsin Z | (0.010) | 0.007 | 0.160 |

### Table 3: Heterogeneity test of cathepsins L2 genetic variants in the risk of Asthma.

| Outcome | Exposure | Method | Q | Q_df | Q_pval |
| Asthma | Cathepsin B | MR Egger | 16.295 | 17 | 0.503 |
| Asthma | Inverse variance weighted | 20.805 | 18 | 0.289 |
| Asthma | Cathepsin E | MR Egger | 5.578 | 7 | 0.590 |
| Asthma | Inverse variance weighted | 9.122 | 8 | 0.332 |
| Asthma | Cathepsin F | MR Egger | 14.602 | 11 | 0.201 |
| Asthma | Inverse variance weighted | 15.949 | 12 | 0.194 |
| Asthma | Cathepsin G | MR Egger | 8.305 | 11 | 0.686 |
| Asthma | Inverse variance weighted | 9.182 | 12 | 0.687 |
| Asthma | Cathepsin H | MR Egger | 7.063 | 9 | 0.631 |
| Asthma | Inverse variance weighted | 8.653 | 10 | 0.565 |
| Asthma | Cathepsin O | MR Egger | 11.795 | 10 | 0.299 |
| Asthma | Inverse variance weighted | 12.493 | 11 | 0.328 |
| Asthma | Cathepsin S | MR Egger | 35.077 | 21 | 0.028 |
| Asthma | Inverse variance weighted | 35.077 | 22 | 0.038 |
| Asthma | Cathepsin L2 | MR Egger | 7.751 | 9 | 0.559 |
| Asthma | Inverse variance weighted | 11.353 | 10 | 0.331 |
| Asthma | Cathepsin Z | MR Egger | 21.762 | 11 | 0.026 |
| Asthma | Inverse variance weighted | 26.248 | 12 | 0.010 |
In the reverse MR analysis, asthma was taken as the exposure factor and SNPs strongly associated with asthma ( P < 5 × 10 − 5 ) were used as instrumental variables while taking all nine cathepsins as outcome factors. The results of this reverse MR indicated a statistically significant association between asthma with high levels of cathepsin B (Supplementary Figure S2 ). The reverse MR analysis leveraged a large asthma GWAS ( N = 266,418), ensuring sufficient power. The null association robustly supports the unidirectional causality from cathepsin L2 to asthma.

Moreover, MVMR analysis could determine the causality of associations between various cathepsins and asthma risk not affected by potential confounders. The results from IVW in MVMR analysis showed again that the increased level of cathepsin L2 was significantly associated with the increasing risk of asthma (OR = 1.060, 95% CI = 1.015–1.106, P = 0.008) (Fig. 3 ).


> **Fig. 3:** Forest plots of multivariable Mendelian randomization analysis of the relationship between cathepsins and asthma.


## Discussion

In the present MR analysis, for the first time, we investigated a possible causal relationship between genetically predicted levels of nine cathepsins and asthma risk. The smaller exposure sample ( N = 3,301) may reduce precision in SNP-cathepsin associations. However, MR methods remain unbiased under valid instruments (F > 10), as demonstrated in simulations 31 . Indeed, through both univariate and multivariate MR analyses, high levels of cathepsin L2 were significantly associated with an increased risk of asthma. While the p-value for cathepsin L2 ( P = 0.006) approaches the Bonferroni threshold ( P = 0.05/9 ≈ 0.0055), multivariate MR (MVMR) confirmed independence from confounding by other cathepsins ( P = 0.008). MR-Egger regression further ruled out directional pleiotropy (intercept P = 0.090), supporting the robustness of our primary finding. Such results further extend new theoretical insights into asthma pathophysiology, indicating that, among all the cathepsins tested in this study, only cathepsin L2 may play a specific role in the pathogenesis of asthma. Though the effect size is small, population-level impacts could be substantial given asthma’s high prevalence. For instance, a 5.8% increase in risk across millions of individuals may justify targeted therapeutic strategies.

Interestingly, Our study found a clear causal association between asthma and elevated cathepsin B levels. This finding suggests that the presence of asthma may affect cathepsin B levels, rather than cathepsin B being the direct cause of asthma. We speculate that one explanation is that asthma, as a chronic inflammatory disease, may induce changes in lysosomal enzymes such as cathepsin B through feedback mechanisms 32 – 34 . Elevated cathepsin B levels may be a secondary consequence of the chronic inflammation and immune cell activation characteristic of asthma 34 . For example, inflammatory cytokines and proteases are known to regulate lysosomal enzyme activity, and asthma-related lung tissue remodeling may up-regulate cathepsin B expression 35 .

This study observed a significant positive correlation between cathepsin L2 and asthma risk, which is rare as previous studies have focused on other cathepsins in airway remodeling and inflammation in asthma 36 .For example, literature reports indicate that cathepsin B expression is increased in the airway epithelial cells of asthma patients, potentially exacerbating asthma symptoms by promoting inflammatory responses and airway remodeling 37 , 38 .Additionally, other studies have found that cathepsin S expression is significantly increased in asthma patients, associated with increased airway inflammation, and may play a key role in asthma pathogenesis by promoting cytokine secretion and regulating immune cell activity 8 , 39 .Another study mentioned that cathepsin S is expressed in various immune cells, especially macrophages and dendritic cells, and its role in antigen presentation may affect the immune response, thereby aggravating asthma symptoms 40 .However, this study revealed that cathepsin L2 is an independent risk factor for asthma.Cathepsin L2 is highly expressed in epithelial tissues and is closely related to immune response and extracellular matrix degradation 41 .Its overexpression may promote tissue remodeling and airway inflammation in asthma by degrading key extracellular matrix proteins and promoting inflammatory cell infiltration into the airway 10 , 42 .This mechanism aligns with the known pathophysiological features of asthma, including chronic inflammation and airway structural changes. While the observed OR for cathepsin L2 (1.058) is modest, its population-level impact is substantial given asthma’s high prevalence. Small genetic effects are characteristic of complex traits and do not preclude clinical relevance, as exemplified by statins’ success despite targeting variants with OR ~ 1.3 43 . Cathepsin L2 may guide biomarker development or subgroup-specific therapies.

Sensitivity analyses did not alter the findings of this study; thus, these results are robust. MR-Egger regression analysis did not indicate horizontal pleiotropy. These results supported the main analysis, and weighted median and MR-PRESSO estimates gave more confidence to our causal inference. Potential biases from horizontal pleiotropy and weak instruments were rigorously addressed via MR-Egger, weighted median, and MR-PRESSO. The consistency across methods supports the robustness of cathepsin L2’s causal role.The fact that there was no heterogeneity and no outliers adds to the confirmation of the suitability of the genetic instrumental variables applied to assess cathepsin L2, so our findings are unlikely to be influenced by confounding and pleiotropic bias 44 .

Although previous studies have implicated specific cathepsins, in particular cathepsins S and B, in asthma pathogenesis, the current study reveals no significant causal association of genetically predicted levels of those enzymes with the risk of asthma 45 . The finding indicates that the function of these proteases may be significantly affected by environmental factors that cannot be fully captured by Mendelian randomization studies of genetic instrumental variables 46 . In addition, multivariate MR Analysis onfirmed the independence of cathepsin L2 for confusion with other proteases, while sensitivity analyses excluded outlier-driven enzymes, further understanding of the relationship between these cathepsin and asthma.After adjusting for the effects of other cathepsins, only cathepsin L2 remained significantly associated with asthma. This suggests that the initial univariate association observed between cathepsin B and asthma in reverse MR May have been confounded by other cathepsins, especially cathepsin L2. The lack of significance of cathepsin B in multivariate analysis reinforces that its role in asthma may be secondary or reactive.

The power of this research provided by a statistically reliable and large implementation of GWAS, which in turn enables the precise estimation of the causal effects was the highlights in this study. While pooled GWAS data may introduce confounding (e.g., population stratification), MR’s reliance on genetic instruments minimizes such biases, as alleles are randomly assigned at conception 11 .We also conducted multiple sensitivity analyses to further shore up our findings and in turn lower the threat of horizontal pleiotropy or confounding bias. Also, using MR, we can get outcomes regarding whether there are potential causal relationships thus, we partially resolve one of the drawbacks of typical observational studies.Traditional studies often involve confounding due to environmental and lifestyle factors. MR represents, however, a more stringent causal inference framework through the use of genetic variation as instrumental variables 47 .

First, there are several limitations that have to be acknowledged. The sample consisted of subjects of European ancestry only, which may limit the generalization to other racial or ethnic groups. Our focus on European-ancestry populations limits the generalizability of findings. Genetic architecture (e.g., allele frequency, LD patterns), environmental exposures, and asthma phenotypes vary across populations, which may alter cathepsin L2’s causal role. Future trans-ethnic MR studies are critical to validate these associations in diverse cohorts.Future studies in this context should include non-European populations in order to analyze ethnic differences in the association of cathepsin L2 with asthma. Although MR analysis is a powerful tool for causal inference, its validity depends on the critical assumption that genetic variation used as an instrumental variable influences the outcome exclusively through cathepsin levels. We have conducted extensive sensitivity analyses to identify and adjust for possible pleiotropy; however, we could not fully rule out residual pleiotropy. This work examined the levels of circulating cathepsin, which may be an unreliable indicator of the roles of these enzymes in lung tissue. Cathepsins in the lung may have different levels of expression and activity than the ones present in the blood. Targeting cathepsin L2 may complement existing therapies, particularly in subsets with protease-driven pathophysiology. Pharmacological inhibition (e.g., small-molecule inhibitors) or biomarker-guided interventions could maximize clinical benefit while minimizing off-target effects.Thus, upcoming research has to reveal the particular duties cathepsins perform inside the lung, in order to completely comprehend their functions in asthma. Advanced computer vision algorithms, such as DeepLab 48 for semantic segmentation and Feature Pyramid Networks 49 for multi-scale feature extraction, could quantitatively analyze high-resolution imaging data (e.g., chest CT scans or histopathological slides) to map airway remodeling patterns. For instance, DeepLab’s deep convolutional neural networks can segment bronchial wall thickness and mucus plugging, while FPN’s hierarchical architecture captures both local and global structural changes. These methods may reveal spatial correlations between cathepsin L2 expression (via immunohistochemistry) and specific remodeling features, providing visual validation of genetic-pathological links.


## Conclusions

In summary, this study is the first to establish a causal link between elevated cathepsin L2 levels and an increased risk of asthma. These findings shed new light on asthma treatment and suggest that cathepsin L2 could serve as a promising biomarker and therapeutic target. Mechanistic studies in animal models or human airway epithelial cells are needed to validate cathepsin L2’s role in airway remodeling and inflammation.


## Findings

The study shows that cathepsin L2 is positively correlated with the risk of asthma.


## Electronic supplementary material

Below is the link to the electronic supplementary material.

Supplementary Material 1

We thank all the researchers and participants of the studies involved in the Mendelian randomization.

H.L and X.R conceptualized the study design and interpreted the results. F.Q, W.S, X.Q and YF.L analyzed the data and drafted the manuscript. F.Q, and W.S provided the methodological suggestions and revised the manuscript.

Hua Lu is supported by Wuxi Taihy Talent Medical and HealthCare Project (Project number453205005THGD). Ran Xu is supported by Wuxi Municipal Health Commission Youth Project (Project number Q202108).


## Data availability

All the data used in the present study had been publicly available, and The comprehensive details for GWAS database used in this research. Summary statistics for cathepsins are available via the INTERVAL study ( https://www.intervalstudy.org.uk/ ) and can be accessed upon request to the INTERVAL Data Access Committee. Asthma GWAS data are publicly accessible through FinnGen ( https://www.finngen.fi/ ). All analyzed data are available from the corresponding author upon reasonable request.


## Associated Data


## Supplementary Materials

Supplementary Material 1


## Data Availability Statement

All the data used in the present study had been publicly available, and The comprehensive details for GWAS database used in this research. Summary statistics for cathepsins are available via the INTERVAL study ( https://www.intervalstudy.org.uk/ ) and can be accessed upon request to the INTERVAL Data Access Committee. Asthma GWAS data are publicly accessible through FinnGen ( https://www.finngen.fi/ ). All analyzed data are available from the corresponding author upon reasonable request.