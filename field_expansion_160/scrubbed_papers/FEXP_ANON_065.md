# FEXP_ANON_065

## Abstract

Increasing evidence suggests that branched-chain amino acids (BCAAs) are associated with frailty. However, whether there is a causal relationship between them remains to be seen. In addition, the metabolism of amino acids in the body is complex, and many previous studies have neglected the effects of their metabolites. The aim of this study was to investigate the relationship between BCAAs and their metabolites and indicators of frailty through Mendelian randomization (MR) methods, so as to determine the causal relationship between the 2, and to provide potential information for preventive and therapeutic strategies for frailty. A MR study was conducted using public genome-wide association studies (GWAS) data, applying inverse variance weighted as the primary method and complementary methods such as MR-Egger, weighted median, and mode. Cochran Q and MR-Egger were used to assess heterogeneity and pleiotropy. MR-PRESSO was utilized to detect and correct horizontal pleiotropy effects. The inverse variance weighted analysis suggested significant causal associations between acetoacetate levels and hand grip strength (left), acetoacetate levels, plasma isobutyrylcarnitine (C4) levels in chronic kidney disease and leucine and hand grip strength (right), leucine, valine, isoleucine and total concentration of BCAAs (leucine + isoleucine + valine) and frailty index, isoleucine, leucine, total concentration of BCAAs (leucine + isoleucine + valine) and valine and usual walking pace, propionylcarnitine levels and isobutyrylcarnitine (c4) levels and weight loss ( P < .05), while no causal associations between BCAA and other frailty traits. The sensitivity analysis found the results to be robust. This study provided support for a causal association between BCAAs and their metabolites and frailty. Further exploration was still required to understand the potential mechanism.


## 1. Introduction

As the global population ages, frailty is becoming increasingly prominent and drawing international attention. [ 1 ] Frailty is a medical syndrome involving multiple organs and systems, characterized by declines in strength, endurance, and physiological function, thereby increasing an individual’s vulnerability to stressors and/or mortality. [ 2 – 4 ] It may arise from senility, but more frequently accompanies chronic diseases such as cardiovascular, respiratory, digestive, neurological, cancer, autoimmune, metabolic, and endocrine disorders, even depression and anxiety. [ 5 – 7 ] Additionally, frailty can also manifest as a primary symptom but lacks specific etiology and known pathophysiological mechanisms. [ 8 ] Defining and measuring this clinical phenomenon, especially when associated with chronic diseases, presents significant challenges. The typical symptoms in most frail patients are increased mortality, hospitalization rates, fall rates, and long-term care requirements. Patients may exhibit reduced physical activity, diminished muscle strength, weight loss, poor sleep, decreased appetite, and changes in mental state. [ 9 – 11 ] However, the exact casual association between essential nutritional factors and frailty preventions remains unexplored systematically.

Branched-chain amino acids (BCAAs) are a type of essential amino acids, including leucine, isoleucine, and valine, which must be obtained through dietary intake. [ 12 ] BCAAs play key physiological roles in the regulation of skeletal muscle mass, energy homeostasis, nutrition metabolism, immune response, and disease susceptibility in both humans and animals. [ 13 ] In states of frailty, inadequate nutrient intake due to chronic illness, malnutrition, or other factors may lead to skeletal muscle loss. BCAAs can facilitate the building and maintenance of skeletal muscle by directly contributing to protein synthesis and providing metabolic support for muscle cells. [ 14 ] Frailty is frequently accompanied by an energy deficit, during which BCAAs can serve as intermediates entering the citric acid cycle for ATP production. They may also function as substrates for hepatic gluconeogenesis, being converted into glucose within the liver to maintain blood sugar levels and supply energy to tissues throughout the body. [ 15 ] BCAAs also participate in regulating protein metabolism through various mechanisms, including promoting synthesis, inhibiting breakdown, and providing substrates for protein synthesis. [ 16 ] Therefore, appropriate intake of BCAAs may be beneficial in the treatment and prevention of frailty, especially for those with chronic illnesses or malnutrition.

The disturbance of BCAAs homeostasis may play key roles in triggering frailty. A cross-sectional study from longevity County, Guangxi Province, China, indicated a significant negative correlation between BCAAs and frailty scores among oldest-old subjects ( P < .001). [ 17 ] Nutritional status plays a significant role in frailty associated with various diseases. Research indicates that supplementation with BCAAs may help improve frailty resulting from decompensated and compensated advanced chronic liver disease, thereby alleviating malnutrition and related complications. [ 18 ] And a clinical crossover trial showed that the BCAA metabolite succinate appeared significantly different before and after exercise. [ 19 ] Moreover, seniors with frailty and sarcopenia have reduced levels of succinate dehydrogenase complex. [ 20 ] Another observational clinical study showed that acetoacetate levels were significantly higher in patients with frailty due to gastrointestinal cancers compared to controls. [ 21 ] A clinical study showed that leucine administration improved sarcopenia in participants compared to a placebo group. [ 22 ] Nevertheless, another clinical study concluded that leucine supplements were ineffective in improving muscle mass and function. [ 23 ] In addition, basic research suggests that administration of the BCAAs metabolite succinic acid improves muscle oxidative metabolism in mice. [ 24 ] However, the causal relationship between frailty and BCAAs and their metabolites has yet to be elucidated.

Mendelian randomization (MR), as an emerging method for causal inference, is widely utilized in the field of genetic epidemiology. It utilizes open comprehensive statistical data from genome-wide association studies (GWAS) to infer causal relationships between certain diseases and exposure factors, thereby identifying potential risk factors. [ 25 ] As genetic alleles are randomly assigned during conception, MR results are not influenced by confounding factors, [ 26 ] with single-nucleotide polymorphisms (SNPs) strongly related to exposure factors used as instrumental variables (IVs) to estimate the causal effect with outcome. [ 27 ]

Previous studies have more often investigated the role of BCAAs, ignoring the fact that their metabolites may be direct performers or key intermediates in exerting biological effects. In this study, we utilized published GWAS data and employed a two-sample MR analysis to explore the association between BCAAs and their metabolites with indicators of frailty. This contributes to a deeper understanding of the specific mechanisms of action of BCAAs, providing robust evidence for developing prevention and treatment strategies for frailty in clinical practice.


## 2. Methods


## 2.1. Study design

This study employed a two-sample MR design to investigate the causal relationship between BCAAs and their metabolites and frailty extracting summary data from GWAS. The exposure factors were 11 BCAAs and their metabolites, and the outcome indices were 6 types of frailty traits including frailty index, weight loss, physical activity, usual walking pace, right hand grip strength, and left hand grip strength. Summary statistics for frailty were derived from a meta-analysis of GWAS, which included 164,610 European participants (60–70 years) and 10,616 Swedish participants (41–87 years). The analysis identified modifiable traits and exposures that may affect frailty risk. [ 28 ] The summary data of BCAAs and their metabolites were obtained from public MRC-IEU database (Table S1, Supplemental Digital Content, https://links.lww.com/MD/R33 ). Given that all of the analyses were based on publicly accessible GWAS summary statistics, no additional ethics approval or informed consent was required.


## 2.2. IVs selection

The SNPs meeting the following selection criteria were employed as IVs: Since there were insufficient exposure-related SNPs screened according to the 5*10 −8 criterion, the screening criterion for SNPs related to alpha-keto-beta-methylvalerate/alpha-ketoisocaproate levels in chronic kidney disease, acetoacetate levels, plasma succinate levels in chronic kidney disease, succinate levels, and plasma isobutyrylcarnitine (C4) levels in chronic kidney disease were 5*10 −6 . The screening criterion for other exposure factors was 5*10 −8[ 29 ] ; minimum allele frequency (MAF) > 0.01 [ 30 ] ; linkage disequilibrium (LD) effects R 2 < 0.001 and a window distance of 10,000kb [ 31 , 32 ] ; alternative SNPs with high LD ( R 2 > 0.8) were used when the selected IVs were not present in the summary data of the outcome [ 33 ] ; the F value > 10 was used for assessing the strength of the IVs and eliminating potential weak instrument bias. The formula was as follows: F = R 2 (N − 2)/(1 − R 2 ), R 2 denotes the variance of exposure explained by each IV. [ 34 ] Finally, we harmonized the BCAA and their metabolites and frailty datasets by excluding ambiguous SNPs with conflicting alleles and SNPs with intermediate allele frequencies, ensuring that the effect alleles were from the same allele. These final SNPs were utilized for MR analysis as genetic IVs.


## 2.3. MR analysis

In this study, the inverse variance weighted (IVW) was employed as the principal analytical approach. It evaluated the causal association between exposure and outcome risk by calculating the odds ratio (OR) and 95% confidence interval (CI). IVW was reliable and robust for interpreting MR results, which calculated the weighted average of the effect size by computing the inverse variance of each SNP as weights. [ 35 ] The MR-Egger, weighted median, and weighted mode methods were also used to evaluate the robustness of the analysis. The MR-Egger method considered the intercept and provided accurate causal effect estimates in the presence of pleiotropy bias. [ 36 ] The weighted median method assumed that half of the IVs were effective and analyzed the causal association between exposure and outcome, allowing the existence of invalid instruments. [ 37 ] All statistical analyses were conducted using the TwoSampleMR and MR-PRESSO packages in R software (Version 4.0.5). Visualization was performed using forest plots, scatter plots, and funnel plots.


## 2.4. Sensitivity analysis

Sensitivity analysis was conducted to detect potential heterogeneity and pleiotropy in MR studies. In this study, Cochran Q test was used for identifying heterogeneity among IVs, with a P > .05 indicating low heterogeneity, suggesting that the estimates among IVs are randomly distributed and have little impact on IVW results. [ 38 ] MR-Egger regression method was used to explore the effect of horizontal pleiotropy. It indicates no pleiotropy when the regression intercept of MR-Egger approaches zero or lacks statistical significance. [ 39 ] Furthermore, the MR pleiotropy residual sum and outlier (MR-PRESSO) method was utilized to detect potential bias-causing SNPs ( P < .05), and after removing them, causal associations were re-estimated to correct for horizontal pleiotropy. [ 40 ] Finally, a “leave-one-out” sensitivity analysis was conducted to identify influential SNPs. The presence of influential SNPs might compromise the robustness of causal estimates. [ 41 ]


## 3. Results


## 3.1. SNP characteristics for analysis

In this study, we identified 134 independent SNPs with significant P -values as IV SNPs for BCAA and their metabolites. All F -statistic values surpassed 10, with an average of 38.07 for BCAA and their metabolites (Table S2, Supplemental Digital Content, https://links.lww.com/MD/R33 ). Detailed information on IVs for BCAA and their metabolites are listed in Table S3 (Supplemental Digital Content, https://links.lww.com/MD/R33 ).


## 3.2. MR analysis

The IVW analysis suggested significant causal associations between acetoacetate levels (OR = 1.0108, 95% CI: 1.0001–1.0215, P = .0476) and hand grip strength (left), acetoacetate levels (OR = 1.0115, 95% CI: 1.0015–1.0215, P = .024) and plasma isobutyrylcarnitine (c4) levels in chronic kidney disease (OR = 1.0108, 95% CI: 1.0019–1.0198, P = .0177) and hand grip strength (right), valine (OR = 1.0409, 95% CI: 1.0046–1.0786, P = .027) and isoleucine (OR = 1.0839, 95% CI: 1.0215–1.1502, P = .0077) and frailty index, isoleucine (OR = 0.9655, 95% CI: 0.9385–0.9934, P = .0155), leucine (OR = 0.971, 95% CI: 0.9463–0.9964, P = .0254), total concentration of BCAAs (leucine + isoleucine + valine) (OR = 0.9724, 95% CI: 0.9502–0.9952, P = .0177) and usual walking pace, propionylcarnitine levels (OR = 15.9473, 95% CI: 1.0279–247.4089, P = .048) and weight loss (Table 1 ).


### Table 1: MR estimates.

| Exposure | Outcome | nsnp | Method | or_ci | pval |
| Acetoacetate levels | Frailty index | 13 | Inverse variance weighted | 0.9855 (0.9641–1.0073) | .1916 |
| Acetoacetate levels | Hand grip strength (left) | 13 | Inverse variance weighted | 1.0108 (1.0001–1.0215) | .0476 |
| Acetoacetate levels | Hand grip strength (right) | 13 | Inverse variance weighted | 1.0115 (1.0015–1.0215) | .024 |
| Acetoacetate levels | Physical activity | 11 | Inverse variance weighted | 0.9911 (0.9751–1.0074) | .2819 |
| Acetoacetate levels | Usual walking pace | 13 | Inverse variance weighted | 1.0014 (0.9914–1.0114) | .7883 |
| Acetoacetate levels | Weight loss | 13 | Inverse variance weighted | 1.1399 (0.8812–1.4746) | .3188 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Frailty index | 8 | Inverse variance weighted | 0.9914 (0.9716–1.0117) | .4038 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Hand grip strength (left) | 8 | Inverse variance weighted | 0.9929 (0.9744–1.0118) | .4582 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Hand grip strength (right) | 8 | Inverse variance weighted | 0.9923 (0.9774–1.0074) | .3174 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Physical activity | 8 | Inverse variance weighted | 1.0085 (0.9945–1.0228) | .2346 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Usual walking pace | 8 | Inverse variance weighted | 1.0015 (0.9938–1.0093) | .7038 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Weight loss | 8 | Inverse variance weighted | 0.7842 (0.607–1.0131) | .0629 |
| Isobutyrylcarnitine (c4) levels | Frailty index | 6 | Inverse variance weighted | 0.9915 (0.9744–1.009) | .3388 |
| Isobutyrylcarnitine (c4) levels | Hand grip strength (left) | 6 | Inverse variance weighted | 1.0047 (0.9962–1.0133) | .2771 |
| Isobutyrylcarnitine (c4) levels | Hand grip strength (right) | 6 | Inverse variance weighted | 1.0061 (0.9954–1.0168) | .2645 |
| Isobutyrylcarnitine (c4) levels | Physical activity | 6 | Inverse variance weighted | 1.0047 (0.9957–1.0138) | .3084 |
| Isobutyrylcarnitine (c4) levels | Usual walking pace | 6 | Inverse variance weighted | 1.0019 (0.9939–1.01) | .6423 |
| Isobutyrylcarnitine (c4) levels | Weight loss | 6 | Inverse variance weighted | 1.2773 (0.9297–1.7547) | .1309 |
| Isoleucine | Frailty index | 9 | Inverse variance weighted | 1.0839 (1.0215–1.1502) | .0077 |
| Isoleucine | Hand grip strength (left) | 9 | Inverse variance weighted | 0.9838 (0.9367–1.0331) | .512 |
| Isoleucine | Hand grip strength (right) | 9 | Inverse variance weighted | 0.9844 (0.9386–1.0324) | .5169 |
| Isoleucine | Physical activity | 9 | Inverse variance weighted | 1.009 (0.9634–1.0568) | .7036 |
| Isoleucine | Usual walking pace | 9 | Inverse variance weighted | 0.9655 (0.9385–0.9934) | .0155 |
| Isoleucine | Weight loss | 9 | Inverse variance weighted | 1.3379 (0.6648–2.6924) | .4146 |
| Leucine | Frailty index | 16 | Inverse variance weighted | 1.0645 (0.9978–1.1356) | .0583 |
| Leucine | Hand grip strength (left) | 16 | Inverse variance weighted | 0.9813 (0.9451–1.0189) | .3244 |
| Leucine | Hand grip strength (right) | 16 | Inverse variance weighted | 0.9797 (0.9456–1.015) | .257 |
| Leucine | Physical activity | 15 | Inverse variance weighted | 0.9977 (0.9665–1.03) | .8893 |
| Leucine | Usual walking pace | 16 | Inverse variance weighted | 0.971 (0.9463–0.9964) | .0254 |
| Leucine | Weight loss | 14 | Inverse variance weighted | 0.913 (0.4566–1.8256) | .7968 |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Frailty index | 13 | Inverse variance weighted | 0.9857 (0.9657–1.0061) | .1691 |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Hand grip strength (left) | 13 | Inverse variance weighted | 1.0077 (0.9999–1.0155) | .0528 |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Hand grip strength (right) | 13 | Inverse variance weighted | 1.0108 (1.0019–1.0198) | .0177 |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Physical activity | 13 | Inverse variance weighted | 1.0063 (0.9958–1.0169) | .2385 |

## 3.3. Sensitivity analysis

The results of MR-Egger regression showed that the analysis of succinate levels versus weight loss was affected by level polytropy (Table 2 ). Cochran Q test showed that there was heterogeneity in some of the results, and some heterogeneity was acceptable because of the IVW methodology (Table 2 ). In addition, the MR-PRESSO analysis showed that there were outliers in some of the results (Table 3 ). After eliminating outliers, leucine (OR = 0.9703, 95% CI: 0.9522–0.9888, P = .002) and total concentration of BCAAs (leucine + isoleucine + valine) (OR = 0.9717, 95% CI: 0.9563–0.9873, P = .0004) with usual walking pace results remain significant, isobutyrylcarnitine (c4) levels (OR = 1.4751, 95% CI: 1.1504–1.8915, P = .002) with weight loss, leucine (OR = 0.9733, 95% CI: 0.9476–0.9996, P = .046) with Hand grip strength (right), total concentration of BCAAs (leucine + isoleucine + valine) (OR = 1.0687, 95% CI: 1.0147–1.1256, P = .012), and leucine (OR = 1.0665, 95% CI: 1.0162–1.1193, P = .009) with frailty index, valine (OR = 0.9778, 95% CI: 0.9594–0.9966, P = .021) with usual walking pace results turn significant, and other results remain without causation (Table 4 and Table S4, Supplemental Digital Content, https://links.lww.com/MD/R33 ). The MR-Egger and Cochran Q analyses after eliminating outliers are shown in Table S5 (Supplemental Digital Content, https://links.lww.com/MD/R33 ). Foster plots, scatter plots, funnel plots and leave-one-out plots of all positive results are displayed as Figures S1 to S14 (Supplemental Digital Content, https://links.lww.com/MD/R34 ) for further visualization.


### Table 2: Sensitivity analysis of the Mendelian randomization analysis results.

| Exposure | Outcome | Q statistic (IVW) | H.P value | MR-Egger Intercept | P.P value |
| Acetoacetate levels | Frailty index | 8.879149632 | .713216552 | -0.000318222 | .919085513 |
| Acetoacetate levels | Hand grip strength (left) | 13.79941205 | .313700526 | 0.000142831 | .928133047 |
| Acetoacetate levels | Hand grip strength (right) | 9.389457361 | .669354642 | 0.001195832 | .406167241 |
| Acetoacetate levels | Physical activity | 8.388267864 | .590967682 | 0.002711148 | .295389116 |
| Acetoacetate levels | Usual walking pace | 16.96143329 | .15105383 | 0.001355106 | .355706205 |
| Acetoacetate levels | Weight loss | 12.48604224 | .407475471 | -0.00982016 | .794453534 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Frailty index | 5.825556596 | .560259685 | 0.003842611 | .521737047 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Hand grip strength (left) | 30.15970953 | 8.88E-05 | -0.005716862 | .310900335 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Hand grip strength (right) | 19.51960032 | .006706387 | -0.004805843 | .288184893 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Physical activity | 6.270474435 | .508546305 | 0.006526257 | .136624927 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Usual walking pace | 2.72939036 | .908857151 | -0.000672987 | .765519649 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Weight loss | 6.503923677 | .482287441 | 0.020215526 | .789914831 |
| Isobutyrylcarnitine (c4) levels | Frailty index | 9.26610995 | .098909209 | 0.00555808 | .18423764 |
| Isobutyrylcarnitine (c4) levels | Hand grip strength (left) | 10.80342356 | .055419866 | -0.000485099 | .832694491 |
| Isobutyrylcarnitine (c4) levels | Hand grip strength (right) | 16.80339673 | .004888155 | -0.001366112 | .629253643 |
| Isobutyrylcarnitine (c4) levels | Physical activity | 2.930431787 | .710710427 | -0.00020614 | .924818462 |
| Isobutyrylcarnitine (c4) levels | Usual walking pace | 13.27792883 | .020908921 | -0.002955419 | .105332375 |
| Isobutyrylcarnitine (c4) levels | Weight loss | 15.09975331 | .009944504 | 0.004730417 | .955129303 |
| Isoleucine | Frailty index | 9.496608235 | .302147741 | 0.004193159 | .348455487 |
| Isoleucine | Hand grip strength (left) | 32.10596924 | 8.92E-05 | 0.006117762 | .069711998 |
| Isoleucine | Hand grip strength (right) | 30.22043255 | .000193226 | 0.00594357 | .069756979 |
| Isoleucine | Physical activity | 12.30511763 | .138100653 | -0.000168967 | .962280171 |
| Isoleucine | Usual walking pace | 14.8416266 | .062299081 | 0.001143711 | .600909202 |
| Isoleucine | Weight loss | 5.902219974 | .658183829 | -0.037058701 | .463818645 |
| Leucine | Frailty index | 35.39605366 | .002158855 | 0.004944879 | .17145583 |
| Leucine | Hand grip strength (left) | 59.22414772 | 3.43E-07 | 0.000691562 | .749581772 |
| Leucine | Hand grip strength (right) | 52.41923606 | 4.81E-06 | 0.001256142 | .536213754 |
| Leucine | Physical activity | 15.94152285 | .316958461 | -0.00034567 | .849286463 |
| Leucine | Usual walking pace | 38.25886059 | .000826116 | -0.000966421 | .512641057 |
| Leucine | Weight loss | 13.39869739 | .41750804 | -0.016063549 | .663838 |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Frailty index | 22.39517197 | .033322285 | 0.003877601 | .272932109 |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Hand grip strength (left) | 15.78883656 | .201100297 | -0.000695446 | .611383608 |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Hand grip strength (right) | 20.80562746 | .053300215 | -0.001178254 | .450628706 |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Physical activity | 7.006899458 | .85715727 | 0.000798675 | .654963619 |

### Table 3: MR-PRESSO results.

| Exposure | Outcome | R.OR (CI%) | R.P | O.OR (CI%) | O.P | Global P | Number of outliers | Distortion P |
| Acetoacetate levels | Frailty index | 0.9855 (0.9671–1.0043) | .154867053 | NA (NA–NA) | NA | .7166 | NA | NA |
| Acetoacetate levels | Hand grip strength (left) | 1.0108 (1.0001–1.0215) | .070985074 | NA (NA–NA) | NA | .3306 | NA | NA |
| Acetoacetate levels | Hand grip strength (right) | 1.0115 (1.0026–1.0203) | .025356856 | NA (NA–NA) | NA | .6895 | NA | NA |
| Acetoacetate levels | Physical activity | 0.9911 (0.9764–1.006) | .267255277 | NA (NA–NA) | NA | .6012 | NA | NA |
| Acetoacetate levels | Usual walking pace | 1.0014 (0.9914–1.0114) | .792865409 | NA (NA–NA) | NA | .1583 | NA | NA |
| Acetoacetate levels | Weight loss | 1.1399 (0.8812–1.4746) | .338445853 | NA (NA–NA) | NA | .4025 | NA | NA |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Frailty index | 0.9914 (0.9733–1.0099) | .390554416 | NA (NA–NA) | NA | .556 | NA | NA |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Hand grip strength (left) | 0.9929 (0.9744–1.0118) | .482331221 | 1.0004 (0.9886–1.0123) | .952266877 | 1.00E-04 | 3 | <1e-04 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Hand grip strength (right) | 0.9923 (0.9774–1.0074) | .35068121 | 0.9973 (0.9841–1.0106) | .703911332 | .0103 | 1 | .1789 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Physical activity | 1.0085 (0.9952–1.022) | .249468256 | NA (NA–NA) | NA | .5238 | NA | NA |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Usual walking pace | 1.0015 (0.9967–1.0063) | .561841061 | NA (NA–NA) | NA | .911 | NA | NA |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Weight loss | 0.7842 (0.6126–1.0038) | .094956976 | NA (NA–NA) | NA | .5466 | NA | NA |
| Isobutyrylcarnitine (c4) levels | Frailty index | 0.9915 (0.9744–1.009) | .382740406 | NA (NA–NA) | NA | .179 | NA | NA |
| Isobutyrylcarnitine (c4) levels | Hand grip strength (left) | 1.0047 (0.9962–1.0133) | .326723356 | NA (NA–NA) | NA | .1485 | NA | NA |
| Isobutyrylcarnitine (c4) levels | Hand grip strength (right) | 1.0061 (0.9954–1.0168) | .315251705 | NA (NA–NA) | NA | .04885 | NA | NA |
| Isobutyrylcarnitine (c4) levels | Physical activity | 1.0047 (0.9978–1.0117) | .240803286 | NA (NA–NA) | NA | .75585 | NA | NA |
| Isobutyrylcarnitine (c4) levels | Usual walking pace | 1.0019 (0.9939–1.01) | .661808204 | NA (NA–NA) | NA | .08355 | NA | NA |
| Isobutyrylcarnitine (c4) levels | Weight loss | 1.2773 (0.9297–1.7547) | .191328684 | 1.4751 (1.1504–1.8915) | .037489475 | .03605 | 1 | .38185 |
| Isoleucine | Frailty index | 1.0839 (1.0215–1.1502) | .028590723 | NA (NA–NA) | NA | .39655 | NA | NA |
| Isoleucine | Hand grip strength (left) | 0.9838 (0.9367–1.0331) | .53044385 | 0.9834 (0.9428–1.0259) | .467996702 | .00065 | 2 | .98645 |
| Isoleucine | Hand grip strength (right) | 0.9844 (0.9386–1.0324) | .535045031 | 0.9894 (0.9515–1.0287) | .609980244 | 7.00E-04 | 2 | .54375 |
| Isoleucine | Physical activity | 1.009 (0.9634–1.0568) | .71345631 | NA (NA–NA) | NA | .1646 | NA | NA |
| Isoleucine | Usual walking pace | 0.9655 (0.9385–0.9934) | .041816482 | NA (NA–NA) | NA | .08775 | NA | NA |
| Isoleucine | Weight loss | 1.3379 (0.7338–2.4394) | .369993322 | NA (NA–NA) | NA | .6186 | NA | NA |
| Leucine | Frailty index | 1.062 (0.9978–1.1303) | .077086325 | 1.0638 (1.0152–1.1147) | .021318499 | .008 | 2 | .92645 |
| Leucine | Hand grip strength (left) | 0.9848 (0.9484–1.0226) | .437899009 | 0.9766 (0.9477–1.0064) | .147135176 | <5e-05 | 3 | .7151 |
| Leucine | Hand grip strength (right) | 0.9816 (0.9484–1.016) | .305930091 | 0.9757 (0.9502–1.0019) | .091390823 | 1.00E-04 | 3 | .6626 |
| Leucine | Physical activity | 1.0015 (0.9696–1.0346) | .926893766 | NA (NA–NA) | NA | .2224 | NA | NA |
| Leucine | Usual walking pace | 0.9706 (0.947–0.9949) | .030913357 | 0.9699 (0.9526–0.9875) | .004956943 | .00435 | 2 | .9427 |
| Leucine | Weight loss | 0.9328 (0.4836–1.7994) | .838661469 | NA (NA–NA) | NA | .52285 | NA | NA |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Frailty index | 0.9857 (0.9657–1.0061) | .194248862 | NA (NA–NA) | NA | .0548 | NA | NA |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Hand grip strength (left) | 1.0077 (0.9999–1.0155) | .076712852 | NA (NA–NA) | NA | .265 | NA | NA |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Hand grip strength (right) | 1.0108 (1.0019–1.0198) | .03534248 | NA (NA–NA) | NA | .0645 | NA | NA |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Physical activity | 1.0063 (0.9983–1.0144) | .148869634 | NA (NA–NA) | NA | .8808 | NA | NA |

### Table 4: MR estimates of eliminated outliers.

| Exposure | Outcome | nsnp | Method | or_ci | pval |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Hand grip strength (left) | 5 | Inverse variance weighted | 1.0004 (0.9884–1.0125) | .9498 |
| Alpha-keto-beta-methylvalerate or alpha-ketoisocaproate levels in chronic kidney disease | Hand grip strength (right) | 7 | Inverse variance weighted | 0.9973 (0.9841–1.0106) | .6901 |
| Isobutyrylcarnitine (c4) levels | Weight loss | 5 | Inverse variance weighted | 1.4751 (1.1504–1.8915) | .0022 |
| Isoleucine | Hand grip strength (left) | 6 | Inverse variance weighted | 0.9983 (0.9596–1.0386) | .9326 |
| Isoleucine | Hand grip strength (right) | 6 | Inverse variance weighted | 1.0005 (0.9588–1.044) | .9824 |
| Leucine | Frailty index | 14 | Inverse variance weighted | 1.0665 (1.0162–1.1193) | .009 |
| Leucine | Hand grip strength (left) | 13 | Inverse variance weighted | 0.9725 (0.9456–1.0002) | .0516 |
| Leucine | Hand grip strength (right) | 13 | Inverse variance weighted | 0.9733 (0.9476–0.9996) | .0465 |
| Leucine | Usual walking pace | 14 | Inverse variance weighted | 0.9703 (0.9522–0.9888) | .0017 |
| Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease | Usual walking pace | 12 | Inverse variance weighted | 1.0081 (0.9993–1.017) | .0726 |
| Propionylcarnitine levels | Frailty index | 2 | Inverse variance weighted | 1.0508 (0.7045–1.5673) | .8082 |
| Propionylcarnitine levels | Hand grip strength (left) | 2 | Inverse variance weighted | 0.9347 (0.8002–1.0917) | .3936 |
| Propionylcarnitine levels | Hand grip strength (right) | 3 | Inverse variance weighted | 0.9031 (0.4774–1.7085) | .7541 |
| Succinate levels | Weight loss | 5 | Inverse variance weighted | 1.2316 (0.7514–2.0185) | .4087 |
| Total concentration of branched-chain amino acids (leucine + isoleucine + valine) | Frailty index | 14 | Inverse variance weighted | 1.0687 (1.0147–1.1256) | .0121 |
| Total concentration of branched-chain amino acids (leucine + isoleucine + valine) | Hand grip strength (left) | 12 | Inverse variance weighted | 0.9825 (0.9539–1.012) | .2417 |
| Total concentration of branched-chain amino acids (leucine + isoleucine + valine) | Hand grip strength (right) | 11 | Inverse variance weighted | 0.9798 (0.9529–1.0076) | .1526 |
| Total concentration of branched-chain amino acids (leucine + isoleucine + valine) | Usual walking pace | 13 | Inverse variance weighted | 0.9717 (0.9563–0.9873) | .0004 |
| Valine | Hand grip strength (left) | 16 | Inverse variance weighted | 1.0163 (0.9929–1.0401) | .1731 |
| Valine | Hand grip strength (right) | 17 | Inverse variance weighted | 1.0033 (0.9757–1.0317) | .8164 |
| Valine | Usual walking pace | 18 | Inverse variance weighted | 0.9778 (0.9594–0.9966) | .0211 |

## 4. Discussion

As mentioned earlier, previous studies have mostly favored exploring the relationship between amino acids and frailty indices, and have less frequently addressed the role of amino acid metabolites. As the direct executors of exerting biological effects, the study of branched-chain amino acid metabolites can help to gain a deeper understanding of the specific mechanisms of BCAAs’ actions. This MR study provides strong genetic evidence for a causal relationship between BCAAs and their metabolites and frailty. We found that acetoacetate levels were positively associated with hand grip strength (left); acetoacetate levels and plasma isobutyryl carnitine (c4) levels in chronic kidney disease were positively associated with hand grip strength (right), whereas leucine was negatively associated with hand grip strength (right); leucine, valine, isoleucine and total concentration of BCAAs (leucine + isoleucine + valine) were positively associated with frailty index; isoleucine, leucine, total concentration of BCAAs (leucine + isoleucine + valine) and valine were negatively associated with usual walking pace; propionylcarnitine levels and isobutyrylcarnitine (c4) levels were positively associated with weight loss. The use of multiple MR methods and sensitivity analyses enhanced the robustness of the findings. This study not only deepens our understanding of the pathogenesis of frailty, but also provides new potential targets for precision medicine, facilitates the development of preventive and therapeutic strategies for related diseases, and promotes interdisciplinary collaboration and research.

Several clinical studies have shown that supplementation with BCAAs improves frailty and enhances muscle strength in specific populations (e.g., patients with cirrhosis and postlumbar spinal stenosis). [ 42 , 43 ] However, MR results suggested that valine and isoleucine were positively associated with frailty. This means that higher BCAA levels may be associated with a higher risk of frailty. As to the reasons for this paradoxical phenomenon, we believe that it is firstly related to the dual role of BCAAs. In healthy individuals or in certain pathological states, high levels of BCAAs may reflect the presence of metabolic disorders or other underlying diseases in the body, leading to frailty. For example, in patients with insulin resistance or diabetes, accumulation of BCAAs has been shown to correlate with poor health outcomes. [ 44 ] Conversely, in patients who are malnourished or have severe protein-energy depletion (e.g., patients with cirrhosis), supplementation with BCAAs can help restore muscle mass and function because they are important raw materials for the synthesis of new proteins and are involved in regulating the synthesis and breakdown of muscle proteins. [ 45 ] Alternatively, it may be related to differential effects in different populations. In populations with chronic diseases such as cirrhosis or lumbar spinal stenosis, supplementation with BCAAs may facilitate the recovery process by providing essential nutrients to improve muscle mass and strength, which in turn may reduce symptoms of frailty. [ 46 ] In contrast, in the general population or in nonspecific frailty states, excessively high levels of BCAAs may not always be beneficial, but may instead be indicative of broader metabolic problems. [ 47 ] So on the clinical side, given the complex effects of BCAAs in different contexts, it is crucial to develop individualized interventions. In patients with clear indications (e.g., cirrhosis or severe malnutrition), supplementation with BCAAs may be beneficial in moderate doses, while in the general population or in individuals at risk for metabolic disorders, it should be used with caution. Further studies are still needed in the future to investigate the specific mechanism of action of BCAAs in different types of frailty, especially the differential manifestation in different pathological conditions (e.g., chronic diseases, recovery from acute injuries, etc).

MR studies have shown that the total concentration of BCAAs (leucine + isoleucine + valine) is negatively correlated with daily walking speed, i.e., higher levels of BCAAs may reduce walking speed, suggesting that they may promote frailty. A basic study had similar results. [ 48 ] This study concluded that restricting dietary BCAAs may prolong healthy lifespan and longevity in mice. [ 48 ] We suggest that the metabolism of BCAAs in the body occurs primarily in muscle, where they are important components of protein synthesis and are involved in the regulation of energy metabolism. [ 49 ] High levels of BCAAs may affect insulin sensitivity and glucose metabolism, [ 50 , 51 ] which in turn may negatively affect muscle function. On the other hand, BCAAs, especially leucine, can activate the mTOR signaling pathway, [ 13 ] which is essential for cell growth and proliferation. However, excessive activation of mTOR has been shown to be associated with an accelerated aging process. [ 52 ] Therefore, lowering BCAA levels may slow down the aging process by inhibiting mTOR signaling. The results of this study provide new perspectives for understanding the role of BCAAs in human health. For the elderly or those at risk of frailty, rational control of BCAA intake may contribute to improved health and longevity. However, complete restriction of BCAA intake may not be suitable for all populations due to its important role in maintaining muscle function and fighting fatigue. Therefore, a personalized nutritional plan needs to be developed on an individual basis.

In addition, MR studies have shown that elevated levels of propionylcarnitine and isobutyrylcarnitine are positively associated with weight loss (OR > 1). Specifically, our analysis identified a statistically significant causal association between propionylcarnitine levels and weight loss (OR = 15.9473, 95% CI: 1.0279–247.4089, P = .0477). Although the CI is relatively wide – likely due to limited sample size or a small number of IVs – the P -value met the threshold for statistical significance, indicating a potentially meaningful causal relationship that warrants further investigation. Interestingly, this finding is partially supported by a previous experimental study by Piirsalu et al, in which pharmacological intervention led to reduced body weight in mice alongside decreased levels of propionylcarnitine. [ 53 ] Carnitine plays an important role in fatty acid metabolism by transporting long-chain fatty acids into mitochondria for beta-oxidation. [ 54 ] Propionylcarnitine and isobutyrylcarnitine are metabolites of carnitine, and their elevated levels may reflect abnormal fatty acid metabolism in the body. For the underlying biological mechanisms, we suggest that, on the one hand, there may be an increase in fatty acid oxidation that leads to increased energy expenditure, which in turn causes weight loss. For example, fatty acid oxidation may be enhanced in certain disease states, such as hyperthyroidism and diabetes mellitus, [ 55 , 56 ] resulting in elevated levels of propionylcarnitine and isobutyrylcarnitine. On the other hand, there may also be abnormalities in the carnitine metabolic pathway, leading to increased production or excretion of propionylcarnitine and isobutyrylcarnitine. Therefore, understanding the causal relationship between propionylcarnitine and isobutyrylcarnitine and weight loss can help provide new ideas and methods for weight management. For example, the fatty acid metabolic status of an individual can be assessed by testing the levels of propionylcarnitine and isobutyrylcarnitine, which can provide a basis for the development of a personalized weight loss program. Meanwhile, the mechanism of propionylcarnitine and isobutyrylcarnitine in weight regulation can also be further investigated, and drugs or nutritional supplements targeting carnitine metabolism can be developed to assist in weight management.

For other positive results of MR findings, such as acetoacetate levels and plasma isobutyryl carnitine (c4) levels were positively correlated with right hand grip strength. Due to the plethora of positive results, this will be further explored in depth in subsequent studies. For example, it can be mentioned that acetoacetate is a type of ketone body and its elevated level may be related to energy metabolism status, whereas left-handed grip strength is an important indicator of muscle strength, and the correlation between the 2 deserves further study to reveal its potential mechanism.

This study supported the causal association between BCAAs and their metabolites and frailty, suggesting that BCAA supplementation may be an effective strategy to improve nutritional status and mitigate frailty. It highlighted the importance of nutritional intervention in clinical practice, especially for patients with malnutrition or those suffering from debilitating diseases. Malignant tumors, chronic infections, or burns may increase the body’s demand for nutrients or protein metabolism, [ 57 , 58 ] where BCAA supplementation may help maintain protein metabolism balance. Patients undergoing surgery may experience metabolic disturbances and tissue damage, where BCAA supplementation help promote tissue repair and physical recovery. For some patients with chronic diseases such as chronic kidney disease or liver disease, [ 59 , 60 ] nutritional support and adjustment may require BCAA supplementation. However, excessive intake of BCAAs may lead to adverse effects such as hepatic encephalopathy. [ 61 ] Individual patients may have different needs and responses to BCAAs and their metabolites, and thus treatment plans should consider individual circumstances and requirements. Therefore, BCAA supplementation should be conducted under the professional guidance of a physician. Additionally, large-scale randomized controlled trials (RCTs), long-term cohort studies, and research on changes in biomarkers related to BCAA and their metabolites and frailty are still needed to gain deeper insights into the mechanisms of action of BCAA and their metabolites in frailty. Basic research is necessary to delve into the molecular-level mechanisms by which BCAA and their metabolites regulate protein metabolism, muscle function, immune regulation, and elucidate their relationship with frailty. Conducting nutritional intervention studies to explore the effects of BCAA supplementation at different doses, forms, and durations on frailty patients will provide scientific evidence for developing more effective treatment strategies.

While some of the observed odds ratios in our MR analyses are modest (e.g., ORs close to 1), it is important to interpret these effects within the context of a complex, polygenic, and age-related phenotype such as frailty. Small but statistically robust causal effects may still reflect biologically important pathways. For instance, alterations in BCAA metabolism have been mechanistically linked to mitochondrial dysfunction, insulin resistance, and chronic inflammation – key hallmarks of aging and frailty progression. From a public health perspective, even a small increase in risk per genetic unit can have meaningful implications at the population level, especially when the exposure (e.g., elevated BCAA levels) is prevalent. For example, if a large proportion of older adults exhibit dysregulated BCAA metabolism, a modest per-individual risk elevation could translate into a significant burden of frailty cases in the population. Moreover, these findings may support the development of early-life or mid-life prevention strategies. Identifying individuals with genetically predicted BCAA imbalances could enable targeted interventions – such as personalized nutrition, exercise programs, or metabolic monitoring – before clinical frailty manifests. Thus, while the individual-level effect may appear limited, the cumulative biological and population health impact remains clinically meaningful.

It is important to acknowledge several limitations of this MR study. First, the use of GWAS summary statistics from European and Swedish populations limits the generalizability to other ethnic groups. In future, validation within non-European cohorts will be required to confirm the applicability of our findings across different populations. Second, we report nominal P -values without correction for multiple comparisons, increasing the risk of false-positive results. Third, wide CIs indicate uncertainty in effect size estimates, likely due to limited sample sizes and IVs. Moreover, despite employing multiple MR methods (such as MR-PRESSO, MR-Egger, and weighted median) to detect and correct for horizontal pleiotropy, residual bias cannot be entirely ruled out. Lastly, while our findings suggest potential causal relationships, they do not elucidate underlying biological mechanisms. Future studies should address these limitations by using larger samples, independent cohorts, and rigorous statistical adjustments, as well as incorporating functional studies to explore molecular pathways.

This study provides evidence supporting causal associations between BCAAs and their metabolites with various frailty-related traits. The observed relationships highlight a potential role for BCAA metabolism in the onset and progression of frailty, offering insights into its underlying mechanisms. These findings may contribute to the development of novel preventive and therapeutic strategies targeting frailty in aging populations.

Conceptualization: Yichan Zhou, Wenjuan Di.

Data curation: Wenjuan Di.

Formal analysis: Yichan Zhou.

Investigation: Wenjuan Di.

Methodology: Wenjuan Di.

Writing – original draft: Wenjuan Di.

Writing – review & editing: Yichan Zhou, Wenjuan Di.