# FEXP_ANON_061

## Abstract

Breast cancer, a complex disease influenced by metabolic and lipid profiles, requires a deeper understanding of causal relationships between dietary preferences, plasma metabolites, and cancer risk. This study employed Mendelian randomization (MR) to explore causal links between dietary preferences, plasma metabolites, and ER-negative/ER-positive breast cancer risk, alongside underlying mechanisms. The genome-wide association study (GWAS) data regarding dietary preferences, plasma metabolites, and plasma lipids were obtained from the GWAS database, with sample sizes of 161,625, 8,299, and 7,174 respectively. Meanwhile, the GWAS data related to breast cancer and its subtypes (ER + breast cancer and ER- breast cancer) were sourced from the IEU Open GWAS project, with sample sizes of 228,951, 175,475, and 127,442 respectively. Reverse MR and mediation analyses were conducted to assess bidirectional relationships and mediating roles of plasma biomarkers. The analysis revealed significant causal effects of dietary preferences and plasma metabolites on breast cancer risk. Mediation analysis identified key pathways: curry preference ( β = -0.015, 95% CI [-0.029, -0.001], P = 0.034) reduced breast cancer risk through increased phosphatidylcholine levels, while tomato preference ( β = 0.021, 95% CI [0.002, 0.041], P = 0.031) increased risk via the serine to α-tocopherol ratio. Additionally, bitter beer preference ( β = -0.012, 95% CI [-0.024, -0.000], P = 0.038) was inversely associated with ER-negative breast cancer risk, mediated by specific metabolites, whereas sweetened tea preference ( β = 0.015, 95% CI [0.030, 0.059], P = 0.026) positively correlated with ER-negative risk through distinct plasma biomarkers. These findings underscore the importance of dietary factors and plasma metabolites in modulating breast cancer risk across subtypes. The study highlights potential mediation mechanisms, offering insights into the complex interplay between diet, metabolism, and cancer. These results advance our understanding of breast cancer etiology and may inform personalized prevention and treatment strategies, emphasizing the role of targeted dietary interventions and biomarker-driven approaches.

The online version contains supplementary material available at [REDACTED].

Keywords: Plasma metabolomics, Lipids, Breast cancer risk, Causal links, Mendelian randomization


## Introduction

Breast cancer, a leading cause of cancer-related deaths, is the most prevalent cancer in women in 157 out of 185 countries, with 670,000 breast cancer fatalities worldwide in 2022. The significant incidence and mortality rates of breast cancer have emerged as a pressing social and public health issue of global significance [ 1 ]. Risk factors contributing to the onset and progression of breast cancer are intricately linked to genetics and lifestyle. Factors such as diet, environment, occupation, life stage, and estrogen medications can all serve as potential triggers for breast cancer development [ 2 , 3 ].

Diet, as a modifiable lifestyle factor, plays a critical role in cancer prevention and progression. Numerous studies have linked specific food preferences to breast cancer risk, beyond broad dietary patterns. For instance, high tomato consumption is associated with increased serum lycopene levels, which may affect estrogen metabolism and oxidative stress [ 4 ]. Beans and legumes are rich in phytoestrogens, which may have protective effects against hormone-related cancers [ 5 ]. Fish intake contributes beneficial omega-3 fatty acids, known for their anti-inflammatory and anti-tumor properties [ 6 ]. Conversely, red and processed meats (e.g., beef/steak) have been implicated in elevated cancer risk through mechanisms such as heme iron intake and nitrosamine formation [ 7 ]. Banana and cereal bars provide dietary fiber and micronutrients, potentially modifying cancer risk via gut microbiota or metabolic pathways [ 7 ]. Spices such as curry (rich in curcumin) and drinks like red wine (containing polyphenols such as resveratrol) have also been studied for their chemopreventive properties. The inclusion of a derived factor score for dessert preference (F–dessert liking) captures patterns of high sugar and fat consumption, which have been linked to increased cancer risk and recurrence. These exposures were selected based on a combination of biological plausibility, existing literature, and data availability within the GWAS datasets.

Metabolites are small molecules produced during the metabolic processes in living organisms. The levels of metabolites are influenced by various factors, including genetics, diet, and lifestyle [ 8 – 11 ]. Research indicates that metabolites and metabolic pathways play a role in breast cancer development, with breast cancer patients exhibiting metabolic disorders [ 12 ]. For instance, a metabolomic analysis of serum samples using proton NMR (1 H NMR) to detect and quantify metabolites found differences between breast cancer patients and the control group [ 13 ]. Plasma lipids play a crucial role in signaling, acting as second messengers and hormones. The significance of lipid metabolism in the initiation and progression of breast cancer has been increasingly recognized and studied [ 14 ]. By influencing cell apoptosis, inhibiting breast cancer cell proliferation through cell cycle arrest, and impeding migration, plasma lipid metabolism in tumor cells exhibits a close interplay with the tumor microenvironment. Exogenous fatty acids have been shown to promote cancer progression and enhance cell survival [ 15 , 16 ].

Previous studies have established connections between diet, plasma metabolites, plasma lipids, and breast cancer; however, the precise causal relationships and their respective contributions remain ambiguous. Mendelian randomization (MR) analysis is a powerful method for comprehensively evaluating potential causal associations between exposures and outcomes, utilizing genetic variation as an instrumental variable [ 17 ]. Genome-wide association analysis (GWAS) involves examining the genotype and phenotype of thousands of individuals to identify associations between genes and complex traits [ 18 ]. In the context of this study, Mendelian randomization analysis utilized data from GWAS to assess the causal relationships between diet, plasma metabolites, plasma lipids, and breast cancer. This study aimed to identify pathways linking various diets to breast cancer through the mediation of plasma metabolites and plasma lipids. By leveraging information from GWAS datasets, researchers were able to explore potential causal links and pathways that may contribute to breast cancer development.


## Materials and methods


## Study design

In this study, data on diet, plasma metabolites, plasma lipids, and breast cancer were sourced from the GWAS database (Table S1). A two-sample MR analysis was then conducted to examine the causal links between diet, plasma metabolites, plasma lipids, and breast cancer. Subsequently, a two-step approach along with a two-sample MR analysis were utilized to elucidate the mediating effects of plasma metabolites and plasma lipids on the association between diet and breast cancer. The research adhered to the STROBE-MR guidelines (Table S2). The study flowchart illustrating the methodology is depicted in Fig. 1 .


> **Fig. 1:** Study flow chart


## Data sources

Summary data for dietary liking were sourced from study accession numbers obtained from GWASGCST90094781-GCST90094771. The analysis encompassed 161,625 participants evaluating food liking using a 9-point scale, identifying 1,401 food liking associations [ 19 ]. Summary data for plasma metabolites were derived from study accession numbers obtained from GWASGCST90200687-GCST90200328, investigating the genome-wide association of 1,091 blood metabolites and 309 metabolite ratios [ 11 ]. Summary data for plasma lipids were obtained from study accession numbers obtained from GWASGCST90277249-GCST90277416, analyzing 179 lipid species in 7,174 Finnish individuals.

GWAS summary data for breast cancer outcomes were collected from large-scale GWAS or corresponding meta-analyses [ 20 ]. The clinical classification dataset for breast cancer outcomes, including breast cancer, ER + breast cancer, and ER-breast cancer, was downloaded from the IEU OpenGWAS database ( https://gwas.mrcieu.ac.uk/ ). The breast cancer dataset comprised 228,951 European individuals, with 122,977 patients and 105,974 controls. The ER + breast cancer dataset included 175,475 European individuals, with 69,501 patients and 105,974 controls. The ER-breast cancer dataset consisted of 127,442 European individuals, with 21,468 patients and 105,974 controls. Controls in these datasets were defined as individuals without a history of breast cancer. More detailed information can be found in Table 1 .


### Table 1: GWAS detailed information

| Trait | Data source | Ethnicity | Sample size | Web source |
| Exposure |  |  |  |  |
| Dietary preferences | GWAS Catalog | European | 161,625 | https://www.ebi.ac.uk/gwas/publications/35585065 |
| Mediation |  |  |  |  |
| Blood metabolites | GWAS Catalog | European | 8299 | https://www.ebi.ac.uk/gwas/publications/36635386 |
| Plasma lipids | GWAS Catalog | European | 7174 | https://www.ebi.ac.uk/gwas/publications/37907536 |
| Outcome |  |  |  |  |
| Breast cancer | IEU OpenGWAS | European | 228,951 | https://opengwas.io/datasets/ieu-a-1126 |
| ER + breast cancer | IEU OpenGWAS | European | 175,475 | https://opengwas.io/datasets/ieu-a-1127 |
| ER- breast cancer | IEU OpenGWAS | European | 127,442 | https://opengwas.io/datasets/ieu-a-1127 |

## Selection of tool variables

To identify SNPs that meet the criteria for Mendelian randomization (MR) as instrumental variables in the study, the following steps will be taken:

SNPs significantly associated with dietary factors with a p-value less than 5 * 10^-6 will be initially screened.

SNPs in linkage disequilibrium will be removed by setting the linkage disequilibrium coefficient r^2 less than 0.001 and a window size of 10,000 kb to ensure independence of the selected SNPs from each other and to exclude SNPs associated with potential confounding factors.

Ambiguous and palindromic structural SNPs with an improbable forward strand will be excluded to prevent confounding with non-effectual alleles.

The F statistic for each SNP will be calculated, and SNPs with an F value less than 10 will be removed to reduce bias from weak instrumental variables due to insufficient sample size [ 21 ].


## Statistical analysis

In this study, we utilized the inverse variance weighted (IVW), weighted median (WM), MR-Egger regression, Weighted mode, and simple mode methods for Mendelian randomization analysis. The IVW method was selected as the primary approach due to its robust causal inference capabilities when assuming all genetic variants as valid instrumental variables. Despite excluding known confounding SNPs, the presence of unknown confounders could still impact the estimates. Therefore, MR-PRESSO analysis was conducted to identify and remove outliers, ensuring the reliability of the Mendelian randomization estimates. The heterogeneity of the IVW model was assessed using Cochran’s Ω test, with a significance level of P < 0.05 indicating heterogeneity among the instrumental variables. The MR-Egger method was employed to detect horizontal pleiotropy and determine bias, with the intercept term P-value used to assess statistical significance.

Additionally, the leave-one-out method was utilized to evaluate the main effect by systematically removing one SNP at a time. All analyses were performed using the R software packages “Two-Sample-MR” and “MR-PRESSO” to conduct comprehensive Mendelian randomization analyses and ensure the validity and reliability of the results.

In mediation analysis, a triangular relationship is established when a dietary preference and a metabolite/lipids level are each causally associated with breast cancer, and the dietary preference is also causally associated with that metabolite/lipids. In this relationship, the dietary preference serves as the exposure, the metabolite/lipids as the mediator, and breast cancer as the outcome. To ensure the biological plausibility of the associations between dietary preferences and breast cancer risk, dietary preferences and metabolite/lipids, and metabolite/lipids and breast cancer risk, only pairs meeting one of the following criteria were included: (1) for dietary preferences positively associated with breast cancer, the direction of effect on the corresponding metabolite/lipids must be consistent with the metabolite/lipids effect on breast cancer; (2) for dietary preferences negatively associated with breast cancer, the direction of effect on the metabolite/lipids must be opposite to the effect of metabolite/lipids on breast cancer. For the dietary preference–metabolite/lipids pairs that met these criteria, mediation MR analysis was performed to assess the potential mediating role of plasma metabolite/lipids in the relationship between dietary preferences and breast cancer. Specifically, two-sample MR analysis was conducted to estimate the causal effect of each dietary preference (as the exposure) on the corresponding metabolite/lipids (as the outcome), followed by MR analysis of each metabolite/lipids (as the exposure) on breast cancer (as the outcome). The mediator effect was estimated using the product method, that is, the effect value of the exposure on the mediator multiplied by the effect value of the mediator on the outcome [ 22 ].


## Results


## The overall effect of diet liking on breast cancer

The study conducted a two-sample Mendelian randomization analysis to investigate the overall effect of diet liking on breast cancer. The analysis revealed 11 significant associations between diet preference and breast cancer, each with an odds ratio (OR) along with its 95% confidence interval (CI) and corresponding P-values.

The findings indicated that preferences for whole wheat bread, beans, curry, banana, artichoke, red wine, cereal bars, and dessert were negatively associated with breast cancer (OR < 1), suggesting that genetic variations influencing these food preferences may contribute to a reduced risk of breast cancer. On the other hand, preferences for tomato, beef/steak, and grilled/steamed fish were positively associated with breast cancer (OR > 1), indicating that genetic variations influencing these food preferences may be linked to an increased risk of breast cancer.

For instance, a preference for whole wheat bread was linked to a decreased risk of breast cancer (OR = 0.838, 95% CI [0.748, 0.938], P = 0.002), signifying a significant association with lower risk. Conversely, individuals who favored tomatoes were associated with an elevated risk of breast cancer (OR = 1.157, 95% CI [1.053, 1.273], P = 0.003). Most food preferences exhibited P-values below 0.05, indicating the statistical significance of these associations. Analysis through Cochran’s Q statistics, MR-Egger intercept test, and MR-PRESSO revealed no evidence of heterogeneity or horizontal pleiotropy in this Mendelian randomization analysis (Tables S3 and S4). Additionally, the sensitivity analysis demonstrated that the exclusion of specific single-nucleotide polymorphisms (SNPs) significantly altered the association between dietary preferences and breast cancer risk (Fig. 2 ).


> **Fig. 2:** MR analysis showed that the 11 dietary preferences were significantly causal for breast cancer. CI Confidence interval, MR Mendelian randomization, OR odds ratio, SNP single-nucleotide polymorphism


## The overall effect of dietary preference on ER + breast cancer

Through a two-sample Mendelian randomization analysis, we identified seven suggestive associations between dietary preferences and ER + breast cancer. Multiple associations were found between food preferences and genetic variations, including preferences for tomatoes, beef/steak, lamb, white rice, whole milk, beans, and barbecue/grilled meat. The number of SNPs used for these food preferences were 30, 41, 39, 20, 33, 65, and 42, respectively. Preferences for tomatoes, beef/steak, lamb, white rice, whole milk, and barbecue/grilled meat were positively associated with ER + breast cancer, indicating that individuals who preferred these foods had a higher risk of the disease.

Specifically, individuals who loved tomatoes were associated with an increased risk of breast cancer (OR = 1.181, 95% CI [1.060, 1.316], P = 0.002), as were those who preferred beef/steak (OR = 1.108, 95% CI [1.037, 1.185], P = 0.003), lamb (OR = 1.075, 95% CI [1.018, 1.136], P = 0.010), white rice (OR = 1.161, 95% CI [1.027, 1.313], P = 1.017), whole milk (OR = 1.083, 95% CI [1.007, 1.164], P = 0.032), and barbecue/grilled meat (OR = 1.066, 95% CI [1.003, 1.132], P = 0.041). In contrast, a preference for legumes showed an inverse association with health risk (OR = 0.960, 95% CI [0.924, 0.998], P = 0.037), suggesting that a preference for legumes may be associated with a reduced risk of ER + breast cancer. Sensitivity analysis confirmed that these results exhibited no heterogeneity or horizontal pleiotropy (Tables S5 and S6, Fig. 3 ).


> **Fig. 3:** MR analysis showed that seven dietary preferences were significantly causal for ER + breast cancer. CI Confidence interval, MR Mendelian randomization, OR odds ratio, SNP single-nucleotide polymorphism


## The overall effect of dietary liking on ER-breast cancer

Utilizing a two-sample Mendelian randomization approach, we identified nine significant associations between dietary preferences and ER-negative breast cancer, encompassing a variety of food choices such as whole wheat bread, red wine, whisky, sugar, sweetened tea, bell pepper, bitter beer, vegetables, bananas, and diet carbonated drinks, with corresponding SNP counts of 20, 50, 42, 22, 23, 41, 46, 29, and 48. The analysis revealed that preferences for whole wheat bread, red wine, whisky, bell pepper, bitter beer, vegetables, bananas, and diet carbonated drinks were inversely associated with ER-negative breast cancer outcomes. However, a preference for sugar-sweetened tea exhibited a positive association with ER-negative breast cancer (OR = 1.186, 95% CI [1.050, 1.339], P = 0.006), indicating a potential link between sugar-sweetened tea preference and an increased risk of ER-negative breast cancer. Sensitivity analysis confirmed the absence of heterogeneity and horizontal pleiotropy in these results (Tables S7 and S8, Fig. 4 ).


> **Fig. 4:** MR analysis showed that nine dietary preferences were significant for ER-breast cancer causality. CI Confidence interval, MR Mendelian randomization, OR odds ratio, SNP single-nucleotide polymorphism


## The overall effect of plasma lipids on breast cancer

Employing a two-sample Mendelian randomization approach, we identified 20 suggestive associations between plasma lipids and ER-negative breast cancer, examining various biomarkers including different types of triglycerides (Triacylglycerol), phosphatidylinositol (Phosphatidylinositol), phosphatidylethanolamine (Phosphatidylethanolamine), sphingomyelin (Sphingomyelin), and phosphatidylcholine (Phosphatidylcholine). The levels of these biomarkers were linked to odds ratios (OR) of health outcomes, along with their respective 95% confidence intervals (CI) and corresponding P-values as indicators of statistical significance. The study findings revealed that the levels of Triacylglycerol (53:4) (OR = 0.942, 95% CI [0.911, 0.974], P = 0.000), Phosphatidylinositol (16:0_18:1) (OR = 0.916, 95% CI [0.869, 0.965], P = 0.001), Phosphatidylethanolamine (O–18:2_18:2) (OR = 0.903, 95% CI [0.846, 0.963], P = 0.002), Triacylglycerol (58:8) (OR = 0.950, 95% CI [0.919, 0.983], P = 0.003), Phosphatidylcholine (O–18:0_16:1) (OR = 0.936, 95% CI [0.893, 0.981], P = 0.006), Diacylglycerol (18:1_18:1) (OR = 0.943, 95% CI [0.904, 0.983], P = 0.006), Triacylglycerol (50:5) (OR = 0.956, 95% CI [0.924, 0.990], P = 0.012), Triacylglycerol (52:2) (OR = 0.955, 95% CI [0.921, 0.991], P = 0.014), Phosphatidylinositol (18:1_18:2) (OR = 0.953, 95% CI [0.916, 0.992], P = 0.018), Phosphatidylcholine (16:0_20:1) (OR = 0.933, 95% CI [0.878, 0.991], P = 0.024), Triacylglycerol (52:3) (OR = 0.962, 95% CI [0.931, 0.995], P = 0.024), Phosphatidylinositol (16:0_18:2) (OR = 0.959, 95% CI [0.924, 0.996], P = 0.029), Phosphatidylinositol (18:0_18:2) (OR = 0.973, 95% CI [0.949, 0.998], P = 0.031), Triacylglycerol (56:4) (OR = 0.959, 95% CI [0.923, 0.996], P = 0.032), Triacylglycerol (56:8) (OR = 0.963, 95% CI [0.930, 0.998], P = 0.037), and Triacylglycerol (54:5) (OR = 0.957, 95% CI [0.917, 0.998], P = 0.041) were inversely associated with breast cancer outcomes. Thus, populations with higher levels of these biomarkers exhibited a statistically lower risk of breast cancer.

However, there were also a few biomarker levels that demonstrated a positive correlation with health outcomes, indicating that populations with higher levels faced a statistically higher health risk. Specifically, sphingomyelin (440:2) (OR = 1.048, 95% CI [1.017, 1.079], P = 0.002), Phosphatidylcholine (O–17:0_17:1) (OR = 1.050, 95% CI [1.013, 1.088], P = 0.008), Phosphatidylcholine (O–18:1_20:4) (OR = 1.041, 95% CI [1.005, 1.079], P = 0.026), and Phosphatidylcholine (O–16:1_18:1) (OR = 1.044, 95% CI [1.002, 1.088], P = 0.038) were positively associated with breast cancer outcomes, indicating an increased risk of breast cancer. Importantly, there was no evidence of heterogeneity or horizontal pleiotropy, and the specific SNPs did not influence the causal estimates (Tables S9 and S10, Fig. 5 ).


> **Fig. 5:** MR analysis shows a significant causality of 20 plasma lipids for breast cancer. CI Confidence interval, MR Mendelian randomization, OR Ratio, SNP Single-nucleotide polymorphism


## The overall effect of plasma lipids on ER + breast cancer

Through a two-sample Mendelian randomization analysis, we identified 20 suggestive associations between plasma lipids and ER-negative breast cancer. The study encompassed various lipid types, including triglycerides, phosphatidylcholine, phosphatidylinositol, and diacylglycerol. Within the triglyceride series, levels such as 52:6 (OR = 0.937, 95% CI [0.900, 0.976], P = 0.002), 58:8 (OR = 0.934, 95% CI [0.894, 0.975], P = 0.002), 53:4 (OR = 0.944, 95% CI [0.910, 0.980], P = 0.002), 50:5 (OR = 0.938, 95% CI [0.900, 0.978], P = 0.003), 52:2 (OR = 0.940, 95% CI [0.903, 0.979], P = 0.003), 49:1 (OR = 0.920, 95% CI [0.864, 0.979], P = 0.009), 52:4 (OR = 0.943, 95% CI [0.902, 0.986], P = 0.010), 56:6 (OR = 0.960, 95% CI [0.930, 0.990], P = 0.010), 52:5 (OR = 0.945, 95% CI [0.902, 0.990], P = 0.017), 54:7 (OR = 0.956, 95% CI [0.917, 0.997], P = 0.034), 48:2 (OR = 0.946, 95% CI [0.898, 0.997], P = 0.038), and 53:3 (OR = 0.960, 95% CI [0.923, 0.999], P = 0.044) all exhibited an inverse association with ER-negative breast cancer risk. Similarly, the phosphatidylcholine series, including levels like O-18:0_16:1 (OR = 0.905, 95% CI [0.859, 0.953], P = 0.000), 16:0_16:1 (OR = 0.906, 95% CI [0.853, 0.961], P = 0.001), 16:1_18:0 (OR = 0.930, 95% CI [0.881, 0.982], P = 0.009), 14:0_16:0 (OR = 0.927, 95% CI [0.873, 0.985], P = 0.014), displayed an inverse association with ER-negative breast cancer risk. The phosphatidylinositol series, featuring levels such as 16:0_18:1 (OR = 0.917, 95% CI [0.852, 0.986], P = 0.019), 16:0_18:2 (OR = 0.952, 95% CI [0.910, 0.995], P = 0.030), 18:1_18:2 (OR = 0.951, 95% CI [0.906, 0.998], P = 0.040), also demonstrated an inverse association with ER-negative breast cancer risk. Furthermore, the diacylglycerol series, with levels like 18:1_18:1 (OR = 0.923, 95% CI [0.882, 0.966], P = 0.001), 18:1_18:3 (OR = 0.942, 95% CI [0.889, 0.998], P = 0.044), showed an inverse association with ER-negative breast cancer risk. These reductions in lipid levels were linked to a decreased risk of ER-negative breast cancer, implying a potential protective role in lowering the likelihood of developing the disease. However, the phosphatidylcholine series levels exhibited a positive association with the risk of ER-negative breast cancer. Increased levels of these phosphatidylcholine variants were associated with an elevated risk of ER-negative breast cancer (Tables S11 and S12, Fig. 6 ).


> **Fig. 6:** MR analysis shows that 26 plasma lipids were significant and causal for ER + breast cancer. CI Confidence interval, MR Mendelian randomization, OR Ratio, SNP Single-nucleotide polymorphism


## The overall effect of plasma lipids on ER-breast cancer

Through a two-sample Mendelian randomization analysis, we identified 19 suggestive associations between plasma lipids and ER-negative breast cancer. Various lipid types were examined, including phosphatidylethanolamine, phosphatidylcholine, triglycerides, sphingomyelin, phosphatidylinositol, and sterol esters. Among the exposure factors with OR greater than 1, phosphatidylethanolamine (O-18:1_20:4) (OR = 1.110, 95% CI [1.043, 1.182], P = 0.001), phosphatidylcholine (O-18:0_20:4) (OR = 1.102, 95% CI [1.040, 1.168], P = 0.001), phosphatidylcholine (18:0_20:5) (OR = 1.069, 95% CI [1.023, 1.118], P = 0.003), phosphatidylcholine (O-16:1_20:4) (OR = 1.071, 95% CI [1.023, 1.122], P = 0.003), phosphatidylcholine (O-18:1_20:4) (OR = 1.094, 95% CI [1.026, 1.166], P = 0.006), sphingomyelin (d40:2) (OR = 1.083, 95% CI [1.023, 1.148], P = 0.007), phosphatidylethanolamine (O-16:1_20:4) (OR = 1.091, 95% CI [1.016, 1.172], P = 0.016), sterol ester (27:1/20:4) (OR = 1.037, 95% CI [1.006, 1.069], P = 0.020), sterol ester (27:1/20:5) (OR = 1.056, 95% CI [1.008, 1.106], P = 0.023), and phosphatidylinositol (16:0_20:4) (OR = 1.084, 95% CI [1.008, 1.165], P = 0.029) all exhibited positive associations with health risk. These findings indicate that elevated levels of these lipids may be linked to a higher risk of ER-negative breast cancer. Conversely, exposure factors with OR less than 1 included triacylglycerol (53:4) (OR = 0.917, 95% CI [0.866, 0.970], P = 0.003), phosphatidylcholine (18:1_20:2) (OR = 0.941, 95% CI [0.902, 0.982], P = 0.005), phosphatidylinositol (18:0_18:2) (OR = 0.955, 95% CI [0.922, 0.989], P = 0.010), phosphatidylcholine (18:2_20:1) (OR = 0.932, 95% CI [0.881, 0.986], P = 0.014), phosphatidylcholine (18:1_20:3) (OR = 0.933, 95% CI [0.878, 0.990], P = 0.023), phosphatidylcholine (O-18:1_20:3) (OR = 0.919, 95% CI [0.849, 0.995], P = 0.037), and phosphatidylcholine (O-16:1_18:0) (OR = 0.887, 95% CI [0.790, 0.995], P = 0.041). The results suggest that reduced levels of these lipids may be associated with a decreased risk of ER-negative breast cancer (Tables S13 and S14, Fig. 7 ).


> **Fig. 7:** MR analysis shows that 19 plasma lipids were significant for ER-breast cancer causality. CI Confidence interval, MR Mendelian randomization, OR odds Ratio, SNP Single-nucleotide polymorphism


## The overall effect of plasma metabolites on breast cancer

Through a two-sample Mendelian randomization analysis, we identified 66 suggested associations between plasma metabolites and breast cancer. These included metabolites such as 1-stearoyl-2-oleoyl-GPE (18:0 / 18:1), 3-indosulfate, α-hydroxyhexanoic acid, DHEAS, high citrulline, dodecanoic acid, 3-hydroxylate acid, docosaenoic acid (22:2n6), myristic acid (14:1n5), sevococapenoic acid (17:1n7), epiandrosterone sulfate, and γ-glutamyltryptophan. Elevated levels of these metabolites were associated with an increased risk of breast cancer. Notably, metabolites like 3-indosulfate and γ-glutamyltryptophan demonstrated significant associations with breast cancer risk across various MR methods, suggesting their potential importance in breast carcinogenesis.

These metabolites play crucial roles in various biological pathways, including lipid metabolism, amino acid metabolism, and hormone metabolism, indicating that the onset of breast cancer may be linked to disruptions in these metabolic pathways. Elevated levels of 3-indosulfate suggest abnormalities in gut microbial metabolism, while the levels of DHEAS, a metabolite of adrenal hormones, are associated with endocrine imbalances [ 23 , 24 ]. Furthermore, alterations in specific lipids such as myristic acid and docosadienoic acid can impact membrane fluidity and signaling pathways, potentially influencing the development of breast cancer [ 25 – 27 ] (Tables S15 and S16, Fig. 8 ).


> **Fig. 8:** Circular heat map of plasma metabolites for breast cancer; darker color indicates smaller p-value, or higher statistical significance


## The overall effect of plasma metabolites on ER + breast cancer

Through a two-sample Mendelian randomization study, we identified 44 suggestive associations between plasma metabolites and breast cancer, revealing several metabolites significantly associated with breast cancer risk. Specifically, we examined metabolites such as homocitrulline, 3-hydroxysebacate, epiandrosterone sulfate, and N-acetyl-L-glutamine. Isotype citrulline, an amino acid metabolite, may indicate disruptions in amino acid metabolism during cancer development and progression. The levels of 3-hydroxydecanoic acid, an organic acid, can reflect abnormalities in mitochondrial function, potentially playing a significant role in breast cancer development [ 26 ]. Epiandrosterone sulfate, a steroid metabolite, may be linked to hormone imbalances in breast cancer patients, affecting the growth and differentiation of breast cancer cells [ 28 – 30 ]. N-acetyl-L-glutamine, an important nitrogen metabolite, changes in levels of which may be associated with abnormalities in protein metabolism and energy metabolism in breast cancer patients [ 31 ] (Tables S17 and S18, Fig. 9 ).


> **Fig. 9:** Circular heat map of plasma metabolites for ER + breast cancer; darker color indicates smaller p-value, or higher statistical significance


## The overall effect of plasma metabolites on ER-breast cancer

Using a two-sample Mendelian randomization approach, we identified 68 suggestive associations between plasma metabolites and breast cancer, all with P values below 0.05, signifying statistically significant links to breast cancer. Specifically, we noted significant alterations in metabolite levels, including 1,2-dipalmitoyl-GPC, 16:0 / 16:0, N-acetylglycine, propionylglycine, butyrylglycine, and hexanoylglycine in breast cancer patients. These metabolite changes may indicate abnormalities in fatty acid and amino acid metabolism in breast cancer patients, possibly linked to the demands of tumor growth and energy metabolism. Further analysis reveals that variations in 1,2-dipalmitoyl-phosphatidylcholine levels could be associated with modified cell membrane composition and function, influencing cell signaling and cell-cell interactions [ 32 – 34 ]. The increase in N-acetylglycine and other acylglycines might be tied to shifts in amino acid metabolism, potentially driven by the elevated need for amino acids and altered nitrogen metabolism during tumor growth [ 35 , 36 ] (Tables S19 and S20, Fig. 10 ).


> **Fig. 10:** Circular heat map of plasma metabolites for ER-breast cancer; darker color indicates smaller p-value, or higher statistical significance


## Forest plot of the effects of a positive diet on plasma lipids and plasma metabolites in breast cancer

In our previous study, we identified 10 dietary preferences and 62 plasma lipids and metabolites that played crucial roles in breast cancer. Subsequently, we delved into investigating the causal effects of these 10 dietary preferences on the 62 plasma lipids and metabolites. Utilizing Mendelian randomization analysis, we found several significant associations. The preference for grilled/steamed fish was positively correlated with the glucuronidation of the piperidine derivative C17H21NO3 (OR = 1.19, 95% CI [1.01, 1.40], P = 0.039), indicating elevated levels of this biomarker in individuals favoring grilled/steamed fish. Similarly, the preference for bananas was positively linked to the glucuronidation level of the same piperidine derivative C17H21NO3 (OR = 1.26, 95% CI [1.02, 1.54], P = 0.028). Additionally, noteworthy positive correlations were observed between beef/steak preference and aspartate levels (OR = 1.14, 95% CI [1.02, 1.27], P = 0.017), and curry preference and phosphatidylcholine (O-18:0_16:1) levels (OR = 1.25, 95% CI [1.101, 1.43], P = 0.001). Furthermore, the positive associations between red wine preference and retinol (vitamin A) and retinol (linoleic) (OR = 1.14, 95% CI [1.04, 1.25], P = 0.004), as well as α-tocopherol (OR = 1.29, 95% CI [1.06, 1.57], P = 0.011, corroborated the positive relationship between food preferences and biomarker levels. The positive correlation between whole-grain bread preference and X-11315 level (OR = 1.37, 95% CI [1.05, 1.80], P = 0.021) also indicated a similar pattern. Furthermore, negative correlations between food preferences and biomarker levels were also observed.

For instance, the negative correlation between the preference for grilled/steamed fish and the levels of eneic acid (C18:1-DC) and deoxycholic acid (OR = 0.87, 95% CI [0.77, 0.98], P = 0.020 and OR = 0.87, 95% CI [0.76, 0.99], P = 0.030) suggests that populations favoring grilled/steamed fish exhibited lower levels of these biomarkers. Similarly, negative associations were observed between banana preference and sphingomyelin (d40:2) levels, as well as triacylglycerol (56:8) levels (OR = 0.70, 95% CI [0.57, 0.87], P = 0.001 and OR = 0.76, 95% CI [0.61, 0.94], P = 0.013). Furthermore, the negative correlation between legume preference and X-24,795 level (OR = 0.92, 95% CI [0.85, 0.99], P = 0.027), and beef/steak preference with sphingomyelin-1-phosphate and 3-methyl-xanthine levels (OR = 0.85, 95% CI [0.75, 0.97], P = 0.015 and OR = 0.87, 95% CI [0.78, 0.97], P = 0.015) provided additional evidence of the inverse relationship between food preference and biomarker levels.

The negative correlation between curry preference and cysteine glycine levels (OR = 0.88, 95% CI [0.77, 0.99], P = 0.037), and tomato preference and S-allyl cysteine levels (OR = 0.79, 95% CI [0.65, 0.96], P = 0.020) also highlighted the connection between food preferences and biomarker levels. This observation was further supported by the inverse correlation between whole wheat bread preference and α-ketobutyrate levels (OR = 0.75, 95% CI [0.57, 0.98], P = 0.036). These findings suggest that specific food preferences are linked to distinct biochemical markers, reflecting the potential impact of dietary choices on breast cancer risk. Positive associations indicate that populations favoring certain foods have higher levels of specific biomarkers, while negative associations suggest lower levels of these biomarkers in those populations (Tables S21 and S22, Fig. 11 ).


> **Fig. 11:** MR analysis shows 11 dietary preferences related to plasma lipids and metabolites CI confidence interval, GM intestinal flora, MR Mendelian randomization, OR odds ratio, SNP single nucleotide polymorphism


## Forest plot of the effect of positive diet on plasma lipids and plasma metabolites in ER + breast cancer

In our previous investigation, we identified seven dietary preferences and 42 plasma lipids and metabolites that played a crucial role in ER + breast cancer. Subsequently, we explored the causal effects of these seven dietary preferences and 42 plasma lipids and metabolites. Utilizing Mendelian randomization analysis, we found significant associations. The preference for BBQ/barbecue was positively correlated with 3-bromo-5-chloride-2,6-dihydroxybenzoic acid levels (OR = 1.20, CI [1.07, 1.35], P = 0.002) and quinolinic acid levels (OR = 1.19, CI [1.05, 1.35], P = 0.008). Furthermore, the positive correlation between bean preference and the ratio of glucose to N-palmitosylsphingosine (d18:0 to 16:0) (OR = 1.07, CI [1.01, 1.14], P = 0.031) was also notable. The positive association between lamb preference and triacylglycerol (49:1) levels (OR = 1.14, CI [1.20, 1.29], P = 0.050) further validated the positive link between food preference and biomarker levels. Moreover, the positive correlation of whole milk preference with 6-hydroxyinddo sulfate levels (OR = 1.12, CI [1.00, 1.24], P = 0.043) indicated similar relationships. Additionally, negative correlations between food preferences and biomarker levels were observed.

For instance, the negative correlation between BBQ/barbecue preference and the phosphate to valine ratio (OR = 0.86, CI [0.76, 0.96], P = 0.009) and the level of sphingomyelin (d18:1 / 20:0, d16:1 / 22:0) (OR = 0.89, CI [0.79, 0.99], P = 0.039) was observed. Similar patterns were identified through the negative correlation of mutton preference with 2-hydroxydodecane acid levels (OR = 0.87, CI [0.78, 0.96], P = 0.008) and X-12,193 levels (OR = 0.86, CI [0.77, 0.96], P = 0.009). Additionally, the negative correlation between white rice preference and the 6-HOS level (OR = 0.71, CI [0.57, 0.89], P = 0.002) and the 4-acetylcatechol sulfate (1) level (OR = 0.70, CI [0.56, 0.89], P = 0.003) indicated an inverse relationship between food preference and biomarker levels. This observation is further supported by the inverse association of whole milk preference with the level of linoleacyl arachidacylglycerol (18:2 / 20:4) (OR = 0.88, CI [0.79, 0.99], P = 0.033) (Tables S23 and S24, Fig. 12 ).


> **Fig. 12:** MR analysis shows: causality of 7 dietary preferences and plasma lipids and metabolites CI confidence interval, GM intestinal flora, MR Mendelian randomization, OR odds ratio, SNP single nucleotide polymorphism


## Forest plot of the effects of positive diet on plasma lipids and plasma metabolites in ER-breast cancer

In our prior research, we identified eight dietary preferences and 59 plasma lipids and metabolites that were crucial for ER-negative breast cancer. Subsequently, we investigated the causal effects of these eight dietary preferences and 59 plasma lipids and metabolites. Through Mendelian randomization analysis, we found that vegetable preference was positively associated with 1-stearoyl-2-oleacyl-gpc (18:0 / 18:1) levels (OR = 0.72, CI [0.57, 0.91], P = 0.006) and phosphatidylethanolamine (O-16:1_20:4) levels (OR = 1.39, CI [1.07, 1.82], P = 0.015). Additionally, the positive correlation between whole wheat bread preference and 3-methoxycatel sulfate (2) levels (OR = 1.37, CI [1.03, 1.82], P = 0.031) is also noteworthy. These findings indicate that populations favoring these foods exhibit higher levels of specific biomarkers.

In terms of negative correlations, the data also revealed an inverse relationship between food preferences and biomarker levels. For instance, banana preference was negatively correlated with phosphatidylcholine (18:0_20:5) levels (OR = 0.66, CI [0.52, 0.83], P = 0.000) and sterol esters (27:1 / 20:5) levels (OR = 0.68, CI [0.55, 0.85], P = 0.001). Similarly, bitter beer preference showed negative associations with the phosphate to glutamine ratio (OR = 0.85, CI [0.77, 0.94], P = 0.002) and phosphatidylcholine (18:1_20:2) levels (OR = 1.23, CI [1.08, 1.40], P = 0.002). Furthermore, the negative correlation between sweetened tea preference and the levels of N1-methylinosine (OR = 0.76, CI [0.67, 0.87], P = 0.000) and N-acetylglucosamine / N-galactosamine (OR = 0.78, CI [0.69, 0.90], P = 0.000) was also evident (Tables S25 and S26, Fig. 13 ).


> **Fig. 13:** MR analysis shows causal relationships between eight dietary preferences and plasma lipids and metabolites CI confidence interval, GM intestinal flora, MR Mendelian randomization, OR odds ratio, SNP single nucleotide polymorphism


## Reverse MR analysis of positive diet for 3 breast cancers

To investigate whether breast cancer has a causal impact on established dietary preferences (PIVW < 0.05), a reverse MR analysis was conducted. In this analysis, single nucleotide polymorphisms (SNPs) associated with breast cancer were used as instrumental variables (IVs), with breast cancer as the exposure and dietary preferences as the outcome. The reverse MR results revealed a significant causal effect of Cereal bar liking (OR = 1.03, 95% CI [1.00, P = 0.027]) on breast cancer, as well as a causal association of Diet fizzy drinks liking (OR = 0.96, 95% CI [0.92, 0.00], P = 0.047) in ER-negative breast cancer. Furthermore, no causal effect of ER-positive breast cancer on dietary preferences was observed. Notably, no heterogeneity or evidence of horizontal pleiotropy was detected in the analysis (Tables S27, S28, S26, and Fig. 14 ).


> **Fig. 14:** Forest plot of reverse MR analysis of positive diet against breast cancer, b of reverse MR analysis of positive diet against ER + breast cancer, and c of reverse MR analysis of positive diet against ER-breast cancer


## Causal role of diet on breast cancer

We identified five mediation relationships, and the mediation analysis revealed the following results:

Curry preference had a negative effect on breast cancer risk through phosphatidylcholine levels, with a total effect of -0.069. The direct effect was − 0.054, and the mediation effect was − 0.015 (95% CI [-0.029, -0.001], P = 0.034), indicating that the mediation effect accounted for 21.9% of the total effect.

Tomato preference had a positive effect on breast cancer risk through the serine to α-tocopherol ratio, with a total effect of 0.146. The direct effect was 0.125, and the mediation effect was 0.021 (95% CI [0.002, 0.041], P = 0.031), where the mediation effect accounted for 14.7% of the total effect.

Additionally, the effect of tomato preference on ER-positive breast cancer also passed through the same mediation factor, with a total effect of 0.167. The direct effect was 0.143, and the mediation effect was 0.023 (95% CI [0.001, 0.046], P = 0.035), accounting for 14.0% of the total effect.

The inverse association between bitter beer preference and ER-negative breast cancer risk was mediated by phosphatidylcholine levels, with a total effect of -0.119. The direct effect was − 0.106, and the mediation effect was − 0.012 (95% CI [-0.024, -0.000], P = 0.038), accounting for 10.4% of the total effect.

Similarly, the positive association between sweetened tea preference and ER-negative breast cancer risk was mediated by X-24,456 levels, with a total effect of 0.170. The direct effect was 0.139, and the mediation effect was 0.031 (95% CI [0.030, 0.059], P = 0.026), with the mediation effect accounting for 18.2% of the total effect. (Table S29)


## Discussion

In this study, MR analysis techniques were utilized to thoroughly assess the involvement of plasma lipids and the plasma metabolome in mediating the relationship between diet and breast cancer. We identified a potential causal relationship among 21 dietary preferences, 60 plasma lipids, 93 plasma metabolites (comprising 89 individual metabolites and 4 ratios), and 3 types of breast cancer. Additionally, the findings from the mediation analysis further endorse the role of plasma lipids and plasma metabolites in mediating the impact of diet on breast cancer.

The findings suggest that a preference for foods such as tomatoes, beef/steak, baked/steamed fish, lamb, whole milk, BBQ/grilled meat, and tea with sugar may be linked to an increased risk of breast cancer. One study examined the daily dietary habits and health records of 42,012 women aged 35 to 74 years through a questionnaire, considering factors such as age, weight, smoking habits, and family history of breast cancer. The analysis revealed that women who regularly consume red meat and processed meat products had a 22% higher risk of breast cancer compared to those with lower red meat intake [ 37 ]. A common impact of milk and soy intake on breast cancer risk was observed in women with the highest tenth percentile of dairy intake compared to the lowest 10. Additionally, the presence of sex hormones in milk may be associated with the development of breast, ovarian, and endometrial cancers in women [ 38 – 40 ].

Obesity and the resulting excessive accumulation of adipose tissue have been linked to an elevated risk of breast cancer, particularly among postmenopausal women [ 40 ], and serve as an independent adverse prognostic factor for breast tumors [ 41 ]. Research has demonstrated that breast cancer cells and adipocytes are key components of the breast tumor stroma and can directly interact with each other. Moreover, breast cancer cells have the ability to access and utilize the fatty acids generated by neighboring adipocytes. In this study, we identified a causal relationship between the levels of phosphatidylcholine, phosphatidylethanolamine, triacylglycerol, sphingosine, and phosphatidylinositol and the onset of breast cancer.

Changes in phosphatidylcholine metabolism can impact oncogenic signaling pathways in breast cancer cells and influence neighboring normal cell populations through lipid secretion components. Upregulation of phosphatidylcholine isomerase activity in breast cancer cells may impact the proliferation and invasion of tumor cells [ 42 ]. Sphingosine, a crucial bioactive lipid involved in cell signaling and intercellular communication, plays a significant role in breast cancer progression. Alterations in sphingosine levels in breast cancer may be linked to tumor advancement. The heightened activity of sphingosine kinase 1 (SPHK1) in breast cancer cells can affect the proliferation and invasion capabilities of these cells [ 43 ]. Sphingosine-1-phosphate (S1P), another bioactive lipid, exerts diverse pathological functions in conjunction with its receptor family (S1PRs). Given that breast cancer develops through S1P, the successful utilization of S1P antagonists based on gene expression advantages and disease prognosis has not been achieved. In our study investigating the effects of related genes in breast cancer patients, we observed that elevated gene expression involved in S1P synthesis suppressed disease progression in patients with basal breast cancer subtype or those undergoing adjuvant therapy [ 44 , 45 ].

Serine plays a vital role in one-carbon metabolism, nucleotide synthesis, and redox balance, all of which are critical in rapidly proliferating cells such as cancer cells [ 46 ]. Conversely, α-tocopherol (vitamin E) is a potent antioxidant known to counteract oxidative stress, which is a key driver of tumorigenesis [ 47 ]. The ratio of serine to α-tocopherol may therefore reflect a balance between pro-growth metabolic activity and antioxidant defense. A higher ratio might indicate a metabolic shift favoring proliferation and oxidative damage, potentially contributing to increased breast cancer risk. Although direct studies on this ratio are limited, prior research has linked elevated serine levels and decreased α-tocopherol levels to poor cancer outcomes, supporting the plausibility of this mediation pathway.

Plasma metabolites play a vital role in aiding in the early detection, molecular categorization, and prognostic evaluation of breast cancer. Research indicates that metabolite profiles in the plasma of breast cancer patients exhibit variations across different molecular subtypes, offering potential utility in the diagnosis and personalized treatment of the disease [ 23 ]. Specifically, the notable decrease in plasma levels of L-tryptophan in the luminal A (LA), triple-negative (TN), and HER2 molecular subtypes may be linked to immune evasion mechanisms employed by cancer cells. Furthermore, the reduced plasma concentrations of phosphoethanolamine and phospholipids suggest significant distinctions in lipid metabolism within breast cancer [ 48 ].

In this study, various metabolites including amino acids, fatty acids, sugars, nucleotides, and hormones were found to be linked to the risk of breast cancer. Glucose metabolites were particularly highlighted for their significant role in breast cancer. Beyond serving as an energy source, glucose metabolites function as signaling molecules that can activate transcription factors and signaling pathways within cells, thereby facilitating the expression of genes associated with breast cancer invasion and metastasis [ 49 ]. Breast cancer cells commonly demonstrate heightened glucose anabolism to meet the energy and carbon demands necessary for their accelerated growth and viability [ 50 ].

Glycogen synthase (GYS) serves as a pivotal enzyme in glycogen synthesis, and differential expression of GYS 1 and GYS 2 has been observed in breast cancer. Specifically, GYS 1 is significantly upregulated in breast cancer and is linked to poor prognosis and increased proliferation rates [ 51 , 52 ]. Moreover, deviations in glucose metabolism status, such as impaired glucose tolerance and diabetes, have been linked to an increased risk of developing breast cancer independently, suggesting a potential role of abnormal glucose metabolism in breast cancer initiation [ 49 ]. Hormonal metabolites, particularly estrogen and its metabolites, are closely intertwined with breast cancer development.

Estrogen undergoes metabolism through two primary pathways: 2-hydroxylation and 4-hydroxylation. The metabolite 2-methoxyestradiol, generated via the 2-hydroxylation pathway, is believed to have potential protective effects against breast cancer. Conversely, 4-hydroxyestradiol, produced through the 4-hydroxylation pathway, may have carcinogenic properties and could contribute to breast cancer development [ 53 ]. The ratio of 4-hydroxyestradiol to 2-hydroxyestradiol has been proposed as a biomarker for predicting the presence of malignant breast tumors [ 54 ].

An imbalance in estrogen metabolism raises the risk of breast cancer, with factors such as exposure duration, accumulation of genotoxic metabolites, and extent of DNA damage playing crucial roles. Enzymes involved in estrogen metabolism, such as cytochrome P450 (CYP) enzymes, are instrumental in this process, with CYP1B1 being frequently overexpressed in tumor tissues or cells of estrogen-related cancers like breast cancer [ 55 ]. Consequently, alterations in plasma metabolites play significant roles in the initiation, progression, and prognosis of breast cancer.


## Limitations of the study

The study’s generalizability may be limited by the specific population studied, potentially affecting the broader applicability of the findings. The availability and quality of data on dietary preferences, plasma biomarkers, and breast cancer risk factors could impact the precision of the results. Unaccounted confounding variables or residual confounding may influence the observed causal relationships. The complexity of mediation analysis and interactions between multiple variables present challenges in delineating causal mechanisms accurately. In addition, given the exploratory nature of the analysis, we did not apply multiple comparison corrections (such as FDR or Bonferroni), which may increase the risk of false-positive findings. We acknowledge this limitation and recommend that future studies validate these results in independent populations. Although Mendelian randomization provides a robust method for inferring causality, considerations such as instrument validity and pleiotropy need careful attention and addressing to ensure the study’s validity. Additionally, several methodological limitations should be considered. First, potential collider bias may arise from the selection of GWAS datasets, especially if inclusion is conditioned on health-related traits that are influenced by both exposure and outcome. Second, dietary preference data were based on self-reported questionnaires, which are subject to measurement error and recall bias, potentially attenuating observed associations. Third, while MR-based mediation provides a novel framework for inferring causal pathways, interpreting mediation effects in complex biological systems remains challenging, as multiple interacting pathways, pleiotropic effects, and feedback loops may complicate causal inference. Lastly, as the GWAS datasets primarily include individuals of European ancestry, caution is warranted when generalizing these findings to other populations with different genetic and dietary backgrounds.


## Future directions

Future research in this field should prioritize the inclusion of diverse populations to improve the external validity of findings and explore potential variations in causal relationships among different ethnic groups. Longitudinal studies are recommended to uncover temporal relationships between dietary preferences, plasma biomarkers, and breast cancer risk, providing a more comprehensive understanding of the dynamics involved. Further investigations into mechanistic pathways linking dietary factors, plasma biomarkers, and breast cancer risk could reveal the biological mechanisms underlying observed associations. We fully acknowledge the importance of correcting for multiple comparisons. Although such corrections were not applied in the current exploratory analysis, we have discussed this limitation explicitly and emphasized the need for replication of our findings in independent cohorts to ensure their robustness and generalizability. Validation of identified causal relationships and mediation pathways through clinical studies and experimental research is crucial to bolster the evidence base and facilitate the translation of findings into clinical practice. Moreover, the development of personalized risk assessment tools that integrate dietary preferences, plasma biomarkers, and other relevant factors could advance precision medicine approaches for breast cancer prevention and treatment.


## Conclusion

In conclusion, this study successfully elucidated the causal relationships between specific dietary preferences, plasma biomarkers, and breast cancer risk, particularly within ER-negative and ER-positive subtypes. The findings underscore the significance of considering individual dietary factors and plasma biomarkers in assessing breast cancer risk and understanding potential mediation mechanisms that influence disease development. By identifying key causal effects and mediation relationships, the study contributes valuable insights into the complex interplay of diet, biomarkers, and breast cancer. The results highlight the importance of tailored prevention and treatment strategies that account for the impact of dietary choices and plasma biomarkers on breast cancer risk across different subtypes. Moving forward, integrating these findings into personalized risk assessment models and clinical practice could pave the way for more targeted and effective interventions in breast cancer management. Ultimately, this research sets the stage for further exploration of mechanistic pathways, validation through clinical studies, and the development of individualized approaches to improve outcomes for individuals at risk of or affected by breast cancer.


## Supplementary Information

Supplementary material 1.

Supplementary material 2.


## Abbreviations

Dehydroepiandrosterone

Estrogen receptor negative

Estrogen receptor positive

Genome-wide association analysis

Inverse variance weighted

Mendelian randomization

Single nucleotide polymorphism

Lingyao Zhou and Yangwen Du: Writing–original draft, writing–review and editing, data curation, formal analysis, investigation, and methodology. Kumar Ganesan: Writing–original draft, writing–review and editing, data curation, formal analysis, resources, and data curation. Sitong Xian: resources, and data curation. Caiyue Lin: resources, and data curation. Hongbing Liu: resources, and data curation. Chen Jianhua: resources, and data curation. Chen Lin: Conceptualization, writing–original draft, writing–review and editing, methodology, project administration, supervision, resources, and data curation. Jianping Chen: Conceptualization, writing–original draft, writing–review and editing, methodology, project administration, supervision, resources, and data curation.

There is no funding to declare.


## Data availability

The datasets used and/or analyzed in this study are reported within the article and/or additional files are available from the corresponding authors or on reasonable request.


## Consent for publication

The authors declare no competing interests.


## Contributor Information

Chen Lin, Email: [EMAIL_REDACTED].

Jianping Chen, Email: [EMAIL_REDACTED].


## Associated Data


## Supplementary Materials

Supplementary material 1.

Supplementary material 2.


## Data Availability Statement

The datasets used and/or analyzed in this study are reported within the article and/or additional files are available from the corresponding authors or on reasonable request.