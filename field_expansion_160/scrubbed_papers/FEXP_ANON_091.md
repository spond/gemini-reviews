# FEXP_ANON_091

## Abstract

The development of the immune system (ISD) plays a pivotal role in both the genesis and progression of tumors, yet its specific functions in hepatocellular carcinoma (HCC) and the mechanisms behind sorafenib resistance remain elusive. In our investigation, we initially created 167 algorithms by amalgamating 10 distinct machine learning algorithms to identify an optimal and potent ISD-related signature (ISDRS), which proved to be superior to 73 previously published signatures. Moreover, we found that resistance to sorafenib was associated with both ISD levels and ISDRS. These, in turn, exhibited a positive correlation with the infiltration of T regulatory cells (Tregs) and a negative correlation with the levels of IL-6/IL-6R. Furthermore, through single-cell analysis, we uncovered a novel Tregs subgroup that contributes to sorafenib resistance and identified BATF as a potential biomarker for this subgroup.

The online version contains supplementary material available at [REDACTED].

Keywords: Hepatocellular carcinoma, Immune system development, Sorafenib resistance, Regulatory T cell

Subject terms: Cancer, Cancer, Cancer genomics, Cancer models, Oncogenes, Tumour biomarkers, Immunopathogenesis


## Introduction

Following the 2007 publication of the SHARP trial, sorafenib received approval as the premier first-line therapy for advanced HCC 1 . Beyond HCC, sorafenib has also been endorsed for the treatment of advanced renal cell carcinoma and radioiodine-resistant differentiated thyroid cancer 2 , 3 . Initially, sorafenib offered significant clinical advantages, but a substantial portion of patients eventually developed resistance to the drug, alongside experiencing adverse side effects, posing challenges for clinical practitioners 4 , 5 .

Sorafenib functions by targeting and inhibiting multiple kinases that are crucial for the proliferation of cancer cells and the formation of new blood vessels, such as RAF kinases and receptor tyrosine kinases including VEGFR and PDGFR 1 , 4 . This multi-target strategy effectively hampers tumor growth and angiogenesis, leading to reduced tumor cell proliferation, impaired blood supply, and induced apoptosis, particularly in certain cancer types 6 . Accumulating evidence has elucidated sorafenib’s mechanisms, highlighting alterations in its target kinases, activation of the PI3K/AKT/mTOR signaling pathway, drug efflux, and epithelial-mesenchymal transition 4 , 7 – 9 . Nonetheless, the impact of immune subpopulations has been less studied, and the immunological underpinnings of sorafenib resistance remain largely unexplored.

In the early 1950s, Medwar et al. 10 discovered that the early immune system possesses distinct functionalities that influence immune capabilities in adulthood 11 . The degree of ISD varies significantly among individuals, shaped by the embryonic microenvironment and the variety of pathogens and microorganisms encountered after birth 12 , 13 . Recent research indicates that the level of ISD plays a decisive role in shaping the hepatic immune landscape in the context of chronic inflammation and fibrosis. This includes the infiltration of CD8 + T cells and natural killer (NK) cells, which are linked to a better prognosis 14 , 15 . Conversely, variations in suppressive cell populations such as Tregs, tumor-associated macrophages (TAMs), tumor-associated neutrophils (TANs), and cancer-associated fibroblasts (CAFs) due to differing ISD levels are instrumental in fostering immunosuppression, thereby contributing to HCC progression and resistance to treatment 16 . Thus, there is a pressing need for more in-depth research into the mechanisms behind HCC prognosis and treatment resistance in relation to ISD levels.

In our study, we synthesized 167 algorithms by integrating 10 machine learning algorithms to identify an optimal and robust ISDRS for predicting HCC prognosis 17 . This was then validated across three public cohorts and benchmarked against 73 previously published signatures. We discovered a correlation between sorafenib resistance and both ISD levels and ISDRS. Furthermore, through single-cell analysis, we pinpointed a novel Tregs subgroup implicated in sorafenib resistance and identified BATF as a potential biomarker for this subgroup.


## Materials and methods


## Data sources

Gene expression profiles and corresponding detailed clinical information for HCC patients were download from the Cancer Genome Atlas (TCGA, https://cancergenome.nih.gov/ ), the International Cancer Genome Construction (ICGC, https://dcc.icgc.org/projects/LIRI-JP ), and Gene Expression Omnibus (GEO, https://www.ncbi.nlm.nih.gov/geo/ ). A total of 424 samples from TCGA (including 374 tumor tissues and 50 normal tissues), 240 samples from ICGC and 70 tumor samples from GSE144269 18 were included and analyzed for gene expression profiles and corresponding clinical information. The batch effect between TCGA, ICGC and GEO cohorts was eliminated using the “ComBat” method in the R package “sva”. Additionally, 67 patients with HCC treated with sorafenib included in GSE109211 19 were also evaluated to assess the response of sorafenib treatment. The baseline characteristics of the cohorts were summarized in Supplementary Table S1 .


## Clinical specimens

64 samples of HCC patients and 26 samples of paracancer from Mengchao Hepatobiliary Hospital (MCHH) between December 2015 and December 2018. Among them, 10 samples were from HCC patients treated with sorafenib for the development of postoperative recurrence. Two different clinical experts evaluated the response to sorafenib treatment. This study was approved by the ethics committee of the MCHH.


## Collection and quantification of ISD-related genes (ISDGs)

The list of ISDGs was retrieved from the Gene Set Enrichment Analysis (GSEA) website ( https://www.gsea-msigdb.org/GSEA/index.jsp , Supplementary Table S2 ). The single sample GSEA (ssGSEA) was performed on each sample using the R package “GSVA” to quantify the degree of immune system development and the abundance of 28 immune cells in the tumor immune microenvironment (TiME). Hereafter, the Pearson correlation analysis was performed to investigate the correlation between the ISD levels and the Tregs infiltration, expression of IL-6 and IL-6 receptor (IL-6R).


## Consensus molecular clustering of ISDGs

On the basis of the expression patterns of 1029 ISDGs, non-negative matrix factorization (NMF) was used to identify different expression patterns using the R package “NMF” (version 0.22.0). The expressions of ISDGs (matrix A) were decomposed into two non-negative matrices, W and H (i.e., A ≈ WH). A consistent cluster of HCC samples from TCGA was obtained by repeatedly decomposing matrix A and aggregating its output. Based on apparent, discrete, and silhouette coefficients, we selected the optimal k of clusters. Consensus clustering was performed using the Brunet algorithm with 200 iterations.


## Identification of hub ISDG

Gene expression profiles were analyzed using “limma” R package to identify differentially expressed genes (DEGs, P < 0.05, |log2FC| >1). Prognostic genes were screened using the univariate Cox regression model implemented in the “survival” R package ( P < 0.05). We considered genes that intersected with DEGs and prognostic genes as candidate genes to construct the signature.


## Integrated ISDRS generated by machine learning

Ten machine learning algorithms and 167 algorithm combinations were integrated to develop a consensus ISDRS with high accuracy and stability. A range of integrative algorithms were established in the TCGA cohort, including elastic networks (Enet), Least Absolute Shrinkage and Selection Operator(Lasso), Ridge, supervised principal components (SuperPC), stepwise Cox, random survival forests (RSF), generalized boosted regression models (GBMs), CoxBoost, partial least squares regression for Cox (plsRcox), and survival support vector machines (survival-SVMs), which were then validated by three other datasets (ICGC, GSE144269 , and meta-cohort). To determine which model was optimal, Harrell’s concordance index (C-index) was calculated across all validation datasets.


## Validation of ISDRS

The ISDRS of each patient was determined using Equation:

Based on the median risk score, patients were grouped into low- and high-ISDRS groups. We evaluated the prognostic power of the ISDRS using the “survmine” R package for Kaplan-Meier (K-M) survival curves, “survivalROC” R package for receiver operating characteristic (ROC) curves, and “survival” R package for univariate and multivariate Cox regression. A similar validation analysis was conducted in the cohorts of ICGC and GEO144269.


## Analysis of functional enrichment

A comprehensive analysis of the biological functions of the ISDRS was performed using Gene Ontology (GO) and Kyoto Encyclopedia of Genes and Genomes (KEGG) analyses via “clusterProfiler” R package, and visualizations were made using the “ggplot2” R package 20 – 22 .


## Analysis of molecularly targeted drugs (MTDs) response

For low- and high-ISDRS groups, the half-maximal inhibitory concentration (IC 50 ) calculated with the “pRRophetic” R package was used to predict response to MTDs.


## Single-cell RNA sequencing (scRNA-seq) data quality control and processing

The scRNA-seq data of 10 tumor samples from GSE149614 18 were downloaded via GEO database. Data analysis was conducted using the “Seurat” R package. Initially, the single-cell data were filtered by applying the criteria that each gene had to be expressed in at least 3 cells and each cell had to express at least 250 genes, resulting in a total of 16,709 cells. Subsequently, additional criteria were applied, including each cell expressed 100 to 5000 genes, having less than 25% mitochondrial content, and have 100 to 50,000 unique molecular identifier (UMI) counts. The data from the ten samples were individually normalized using log normalization. Then, the canonical correlation analysis (CCA) method was used to identify the sample batch, and the ten samples were integrated using the “harmony” R package. Anchors were obtained through principal component analysis (PCA) dimensionality reduction. Cell clustering was performed by setting the condition dim = 20 with a resolution of 0.2. To reduce the dimensionality of the cells, t-distributed Stochastic Neighbor Embedding (tSNE) was performed, and the subpopulations were annotated using classical immune cell markers based on the CellMarker 2.0 ( http://biocc.hrbmu.edu.cn/CellMarker/ ). Furthermore, the “scissor” R package was used to identify the phenotype-guided single-cell subpopulation. Besides, the score of pathway activities was calculated via the “GSVA” R package.


## Quantitative real time polymerase chain reaction (qRT-PCR)

RNA extraction and reverse transcription were performed based on previous study 23 . BATF expression was normalized to β-actin. qRT-PCR analysis was performed in triplicate, and the average value was calculated using the 2 −ΔΔCt method. The primer sequences for human BATF and β-actin can be found in Supplementary Table S3 .


## Immunohistochemistry (IHC)

IHC staining were performed using the antibodies against BATF (1:15000, CSB-PA619074LA01HU, CUSABIO) as described previously. All immunostaining images were evaluated blindly by pathologists from MCHH based on the histochemical score. The quantitative analysis of the IHC staining was performed according to a previous study 24 .


## Statistical analyses

This study used R-4.0.3 for all analyses. The normality of the variables was assessed using the Shapiro-Wilk test. Student’s t-test was employed to determine differences between two groups with normally distributed variables, while the Wilcoxon test was utilized to measure differences between two variables that were not normally distributed. For multiple group comparisons, parametric analysis of variance (ANOVA) test was used, and nonparametric Kruskal-Wallis tests were employed. Pearson correlation and distance correlation analyses were conducted based on correlation coefficients.


## Result


## The clinical significance and potential mechanism of ISD levels

Figure 1 showed the workflow chart of the whole study. To systematically evaluate the clinical significance and potential mechanism of ISD levels, we first calculated ISD levels and immune cells infiltration via ssGSEA algorithm for each HCC patient, and found that Tregs infiltration were upregulated significantly in the high-ISD levels group in the TCGA cohort (Fig. 2 A, P < 0.05), as well as in the cohort of GSE109211 (treated with sorafenib, P < 0.05, Fig S1 A). Further, we analyzed the IC 50 of MTDs in the TCGA cohort, and found that the treatment response to sorafenib, erlotinib and vorinostat were significantly lower in the high-ISD levels group and high-Tregs infiltration group (all P < 0.05, Fig. 2 B, C). Besides, both ISD levels and IL-6R were significantly increased in the high-Tregs infiltration group compared with the low-Tregs infiltration group (both P < 0.05, Fig. 2 D). Furthermore, correlation analysis confirmed a positive correlation between ISD levels and Tregs infiltration, but a negative correlation was found between ISD levels and IL-6R (Fig. 2 E). These findings above indicated that ISD levels might affect MTDs treatment response, especially sorafenib, by altering Tregs infiltration via IL-6/IL-6R axis, which were validated in the GSE109211 cohort (Fig S1 B-C).


> **Fig. 1:** Flowchart of the present study.


> **Fig. 2:** The clinical significance and potential mechanism of ISD levels. ( A ) ssGSEA of immune cells and immune-related functions between the low- and high-ISD group in the TCGA cohort. ( B , C ) Drug sensitivity analysis showed IC 50 of three molecular targeted drugs (Sorafenib, erlotinib and vorinostat) in different ISD levels and Treg infiltration. ( D ) Comparison of ISD levels, the expression of IL-6R and IL-6 between low- and high-Tregs infiltration group. ( E ) Scatter plot and heat map showed the correlations between ISD levels and Treg infiltration, ISD levels and IL-6R, and Treg infiltration and IL-6R. ssGSEA: Single sample Gene Set Enrichment Analysis; ISD: Immune system development; TCGA: The Cancer Genome Atlas; Tregs: regulatory T cells; IC 50 : The half-maximal inhibitory concentration; ns: not significant; *: P < 0.05; **: P < 0.01; ***: P < 0.001.


## Identification of hub ISD genes and construction of ISDRS

To further explore the significance of ISD in tumor immune microenvironment (TiME), we first used NMF to conduct clustering analysis. Fig S2 demonstrated that both the TCGA and ICGC cohorts exhibited the highest intra-group correlations and lowest inter-group correlations when k = 2. These findings suggested that patients can be classified into cluster 1 or cluster 2 based on 1029 ISDGs. Figure 3 A exhibited two distinct patterns of HCC patients, and cluster 2 possessed a markedly worse prognosis compared with cluster 1 ( P < 0.05, Fig. 3 B). Interestingly, a functional enrichment analysis of the differential genes between cluster 1 and cluster 2 revealed that both T-helper 17 (Th17) type immune response and Th17 cell differentiation were significantly enriched in the biological processes (Fig S3 A-D), and Th17 cell differentiation was also significantly enriched via KEGG (Fig S3 E-H) in all cohorts. A total of 313 ISDGs were identified as DEGs between the two clusters (Supplementary Table S4 ), while 699 ISDGs were selected as DEGs between tumor and normal tissues (Supplementary Table S5 ). In addition, 301 ISDGs were associated with overall survival (OS) based on univariate Cox regression analysis (Supplementary Table S6 ). As shown Figs. 3 C and 98 ISDGs that were converged by the above results as the candidate genes to establish prognosis signatures.


> **Fig. 3:** Identification of hub ISD genes and construction of ISDRS. ( A ) Heatmap representation of NMF clustering for ISDGs. ( B ) Kaplan-Meier curves of OS with two ISD clusters. ( C ) The 98 candidate genes were identified via venn diagram. ( D ) A total of 167 prediction models via LOOCV framework and the C-index of each model across all cohorts. ( E ) The Gini importance for top 15 candidate prognostic genes was calculated via RSF. ( F ) The coefficient value of the final seven ISDGs associated with the ISDRS. ( G – J ) Kaplan-Meier curves of OS with different ISDRS groups in the TCGA, ICGC, GSE144269 and mate-cohort. ISDRS: Immune system development related signature; NMF: non-negative matrix factorization; OS: Overall survival; ISD: Immune system development; LOOCV: Leave One Out Cross-Validation; RSF: Random survival forest; ISDGs: Immune system development related genes.

167 machine learning-based integrative procedures were fitted through leave-one-out cross-validation (LOOCV) framework among the TCGA cohort to develop ISDRS to predict the prognosis of HCC patients, and further the C-index of each model was calculated across all validation cohorts. Interestingly, a combination of the optimal model was RSF and stepwise Cox (direction = both) had the highest C-index in all validation cohorts with the mean C-index of 0.740 (Fig. 3 D). The Gini importance for each candidate prognostic genes was calculated via RSF (Fig. 3 E). After that, stepwise Cox (direction = both) screened seven genes (ZMPSTE24, CTNNB1, IRF2BP2, BATF, TREM2, ALAS1, and IL7R) and calculated ISDRS for each patient based on regression coefficients (Fig. 3 F). According to the median value of ISDRS, patients were divided into high-ISDRS and low-ISDRS group. As expected, the median OS of patients in high-ISDRS group was significantly shorter than that in low-ISDRS group in the cohort of TCGA, ICGC, GSE144269 , and meta-cohort (all P < 0.05, Fig. 3 G-J).


## Evaluation of ISDRS

The 1-year area under the curves (AUCs) of the ROC curves in TCGA, ICGC, GSE144269 and meta-cohort were 0.806, 0.715, 0.759 and 0.746 (Fig S4 A), with the corresponding 2-year AUCs of 0.745, 0.653, 0.689 and 0.688 (Fig S4 B) and the corresponding 3-year AUCs of 0.759, 0.670, 0.659, and 0.701, respectively (Fig S4 C). The C-index of ISDRS in the above four cohorts was 0.771, 0.725, 0.725 and 0.738 (Fig S4 D), which outperformed other variables (e.g., age, gender, stage, and grade) in prognosis prediction across the four cohorts (Fig S4 E-H). Multivariate Cox regression analysis indicated that the ISDRS was an independent risk factor for OS across the four cohorts (all P < 0.001, Fig S4 I-L). Furthermore, subgroup analysis was conducted to estimate the correlation between ISDRS and other clinicopathological characteristics (Fig S5 A). Specifically, significant differences were not observed in age and gender between low- and high-ISDRS subgroups (both P > 0.05, Fig S5 B-C), while there were significant differences in grades, and TNM stages between two subgroups (both P < 0.05, Fig S5 D-E).

To further validate the prognosis value of ISDRS, we retrieved 73 published prognostic signatures, including immune response, autophagy, ferroptosis, stemness, epithelial-mesenchymal transition were screened to compared the prognosis prediction power with the current ISDRS. Univariate Cox regressions analyses revealed that only ISDRS was significantly associated with prognosis in all cohorts ( P < 0.05, Fig. 4 A). As expected, the current ISDRS had a higher C-index than the included 73 signatures among the TCGA, ICGC, GSE144269 and meta-cohort (Fig. 4 B–E).


> **Fig. 4:** Comparison of ISDRS and other prognostic signatures in HCC. ( A ) Univariate Cox regression analysis of ISDRS and 73 published signatures in the TCGA, ICGC, GSE144269 and mate-cohort. ( B – E ) C-index of ISDRS and 73 published signatures in the TCGA, ICGC, GSE144269 and mate-cohort. ISDRS: Immune system development related signature; HCC: Hepatocellular carcinoma; TCGA: The Cancer Genome Atlas; ICGC: International Cancer Genome Construction.


## Predictive value of ISDRS in Sorafenib response

Similar to ISD levels, the high-ISDRS subgroup observed significantly worse treatment response to sorafenib compared with the low-ISDRS subgroup (Fig S6 A, P < 0.05). In the GSE109211 cohort of HCC patients treated with sorafenib, ROC curves revealed that ISDRS had better predictive capability than ISD levels, IL-6, IL-6R, PD-1, PD-L1 and CTLA-4 for sorafenib response with an AUC of 0.845 (Fig S6 B). Besides, ISDRS and ISD levels were significantly upregulated in the sorafenib-resistant group, while the opposite was observed in the expression of IL-6R and IL-6 ( P < 0.05, Fig S6 C).

Further analysis of the TiME of TCGA indicated that immune cells including Tregs, aDCs, iDCs, macrophages and Th2 cells were significantly increased in the high-ISDRS group similar to the ISD levels ( p < 0.05, Fig S7 A). Meanwhile, ISD levels were significantly increased in high-ISDRS group, whereas the expression of both IL-6 and IL-6R were significantly decreased in the high-ISDRS group ( P < 0.05, Fig S7 B). Further correlation analysis showed that ISDRS was positively correlated with Tregs infiltration and negatively correlated with IL-6R, while Tregs infiltration was also negatively correlated with IL-6R (Fig S7 C). These results were consistent with ISD levels, and the correlation index of ISDRS with Tregs infiltration and IL-6R expression was higher than that of ISD levels. These findings were also validated in in GSE109211 cohort treated with sorafenib (Fig S8 A-C). These findings provided further evidence that the interaction between ISDRS and sorafenib resistance, might be influenced by the modulation of Tregs infiltration via the IL-6/IL-6R axis.


## Landscape and potential mechanism of Sorafenib resistance via scRNA-seq

In addition, analysis of the scRNA-seq cohort ( GSE149614 ) further elucidate the potential mechanism in the sorafenib response of HCC. A total of 22 clusters were identified using an unsupervised clustering method based on shared nearest neighbors (SNN) (Fig. 5 A). Afterwards, these clusters were annotated with canonical marker genes of major cell types, including B cells, macrophages, hepatocytes, tissue stem cells, endothelial cells, CD8 + T cells, and Tregs (Fig. 5 B). Furthermore, sorafenib-resistant cells were identified using the “scissor” algorithm based on the response to sorafenib in GSE109211 . Further analysis revealed that both the percentage of Tregs and ISDRS of the sorafenib-resistant cells were significantly increased (Fig. 5 C-F). Besides, Fig S9 indicated a significant upregulation of ISDRS in Tregs and CD8 + T cells in sorafenib-resistant compared to the same cell types in others ( P < 0.05).


> **Fig. 5:** Landscape and potential mechanism of sorafenib resistance via scRNA-seq ( A ) The t-SNE plot of 22 cell clusters from the multicellular ecosystem of 10 HCC patients. ( B ) Dotplot showing the percentage of expressed cells and average expression levels of canonical marker genes of major cell types in 22 cell clusters. ( C , D ) t-SNE plot and bar plots indicating the landscape and proportion of major cell lineages between sorafenib resistant and the other cells. ( E , F ) t-SNE plot and violin plot showing the distribution of ISDRS between sorafenib resistant and the other cells. scRNA-seq: Single-cell RNA sequencing; t-SNE: t-distributed Stochastic Neighbor Embedding; HCC: Hepatocellular carcinoma; ISDRS: Immune system development related signature; ***: P < 0.001.


## BATF, a potential biomaker of sorafenib-resistant Tregs

To investigate the potential mechanism and key biomarkers that influence sorafenib resistance, we extracted Tregs from sorafenib-resistant cells, referred to as sorafenib-resistant Tregs 25 . Interestingly, only BATF was significantly increased in sorafenib-resistant Tregs (Fig. 6 A). While the IL-6R expression, and the ferroptosis and autophagy activities, which were all related to sorafenib resistance, were opposite to BATF expression ( P < 0.05, Fig. 6 A-E) 26 , 27 . In addition, the high-BATF group showed a significant reduction in the activities of ferroptosis and autophagy calculated by GSVA algorithm (both P < 0.001, Fig. 6 F and H), which had a negative correlation with BATF expression (both P < 0.001, Fig. 6 G and I). Similar findings were obtained in the GSE109211 cohort treated with sorafenib (Fig. 6 J-K). Besides, we observed a significant increase in BATF expression in sorafenib-resistant cells (Fig S10 A-B, P < 0.05). However, no notable differences were found in other resistant cell types like B cells and CD8 + T cells (Fig S10 C-F, P > 0.05). These findings suggested that BATF might be a crucial biomarker for identifying sorafenib-resistant Tregs. Based on the findings above, we compared BATF expression in 64 samples of HCC patients and 26 samples of paracancer from MCHH using qRT-PCR and IHC (including 10 samples from HCC patients who experienced postoperative recurrence and received sorafenib treatment). Actually, qRT-PCR and IHC analyses revealed a significant increase in BATF expression and increased infiltration of BATF-positive immune cells in the resistant group ( P < 0.05, Fig. 7 A-C). Additionally, in 26 paired HCC and paracancer samples, both mRNA and protein expression of BATF were significantly increased in HCC samples ( P < 0.05, Fig. 7 D-F). K-M survival curve showed distinct survival differences between the groups of high- and low-BATF ( P < 0.05, Fig. 7 G). Besides, BATF also demonstrated a strong prognostic predictive capability with a 2-year AUC of 0.795 (Fig. 7 H). Multivariate regression analysis showed that BATF was the only independent risk factor associated with OS (Fig. 7 I). Moreover, Fig S11 A-D showed that BATF expression was not significantly different in patients with each clinical clinicopathologic characteristic (all P > 0.05). These findings were further validated by IHC analysis (Fig. 8J-M, Fig S11 E-H), confirming that BATF was an essential biomarker in sorafenib-resistant HCC patients.


> **Fig. 6:** BATF, a potential biomarker of sorafenib-resistant Tregs. ( A ) t-SNE plot showing the expression levels of seven genes used to construct ISDRS and IL-6R, ferroptosis and autophagy in sorafenib resistant Tregs and the other Tregs, colored by gene expression. ( B – E ) Violin plots indicating the distribution of BATF expression, IL6R, ferroptosis and autophagy between sorafenib resistant- and the other-Tregs. ( F , G ) Violin plot and scatter plot showing the distribution and the correlations of ferroptosis and BATF expression. ( H , I ) Violin plot and scatter plot showing the distribution and the correlations of autophagy and BATF expression. ( J ) The distribution of seven genes used to construct ISDRS between sorafenib resistant- and sensitive-patients in the GSE109211 cohort. ( K ) Scatter plot and heat map shows the correlations between BATF and Treg infiltration, BATF and IL-6R, Treg infiltration and IL-6R, ferroptosis and IL-6R, and autophagy and IL-6R. Tregs: regulatory T cells; t-SNE: T-distributed Stochastic Neighbor Embedding; ISDRS: Immune system development related signature; ns: not significant; *: P < 0.05; **: P < 0.01; ***: P < 0.001.


> **Fig. 7:** BATF in relation to prognosis and sorafenib response in MCHH cohort. ( A ) Boxplot shows the distribution of BATF expression between resistant and sensitive samples. ( B , C ) IHC images and BATF-score based on IHC images showing the distribution of BATF expression between sorafenib resistant and sensitive samples (Red arrows: BATF + immune cells; black arrows: BATF- immune cells). ( D ) Paired plot shows the distribution of BATF expression between HCC and paracancer samples. ( E , F ) IHC images and BATF-score based on IHC images shows the distribution of BATF expression between HCC and paracancer samples (Black arrows: immune cells). ( G ) Kaplan-Meier curves of OS with high- and low-BATF expression groups. ( H ) Time-dependent ROC curve of BATF expression analysis for predicting OS at 1-, 2-, and 3-years. ( I ). Univariate and multivariate Cox regression analysis of BATF expression in HCC samples. ( J ) Kaplan-Meier curves of OS with high- and low-BATF score groups. ( K ) Time-dependent ROC curve of BATF-score analysis for predicting OS at 1-, 2-, and 3-years. ( M ) Univariate and multivariate Cox regression analysis of BATF-score expression in HCC samples. MCHH: Mengchao Hepatobiliary Hospital; IHC: Immunohistochemistry; HCC: Hepatocellular carcinoma; OS: Overall survival; ROC: Receiver operating characteristic; *: P < 0.05; **: P < 0.01.


## Discussion

In confronting the challenge of sorafenib resistance in HCC, our investigation reveals that an ISDRS is intricately linked with both the prognosis and the therapeutic response to sorafenib. Additionally, we delineate a previously unidentified subtype of Tregs, instrumental in mediating sorafenib resistance, with BATF emerging as a promising biomarker for this distinct subpopulation. This discovery not only enhances our understanding of the immune landscape’s role in drug resistance but also opens new avenues for targeted therapy.

ISD could impact the composition and function of immune cells in the TiME 28 . In this study, utilizing a sophisticated blend of NMF clustering, variance analysis, and univariate Cox analysis, we pinpointed 98 candidate genes integral to ISD. A novel, integrated approach harnessing ten machine learning algorithms enabled the crafting of a robust model that adeptly forecasts HCC prognosis, surpassing nearly all previously established signatures. This pioneering ISDRS stands as a beacon for potential clinical translation, offering a nuanced prognostic tool for HCC management.

In the realm of HCC, our exploration identifies a complex interplay of ISD-related genes (ISDGs) that either elevate risk or confer protection. Specifically, TREM2 29 , 30 , IRF2BP2 31 , CTNNB1 32 , ZMPSTE24 33 , and BATF 34 emerge as harbingers of increased HCC susceptibility, illustrating the diverse pathways through which tumor progression can be influenced. Conversely, ALAS1 35 and IL7R 36 stand out as guardians against HCC, offering new vistas into the genetic underpinnings of cancer resistance. This intricate genetic tapestry not only underscores the multifaceted nature of HCC pathogenesis but also points towards the transformative potential of leveraging ISDGs for prognostic precision and therapeutic targeting.

Despite sorafenib’s potential for treating HCC, response rates have been modest. This study uncovers a strong association between sorafenib resistance and ISD, highlighted by ISDRS that accurately predicts drug response with the AUC as high as 0.845. It further reveals that Tregs, known for their role in immune evasion and drug resistance, are significantly more prevalent in sorafenib-resistant patients. This correlation, along with the observed downregulation of the IL-6/IL-6R axis in resistant cases, suggests that targeting Treg activation and recruitment may offer a pathway to circumvent sorafenib resistance.

Relevant studies revealed that the composition and function of immune cells in TiME changed over the process of ISD 37 , 38 , especially Tregs 28 . In this study, we discovered a pronounced increase in Treg infiltration correlated with elevated ISD levels, further associated with enhanced IL-6 expression. Employing the NMF clustering algorithm, we categorized patients into distinct clusters, revealing a notable enrichment of Th17 type immune responses in one subset, hinting at a sophisticated interplay between Treg differentiation and the IL-6/IL-6R axis, potentially fueling sorafenib resistance.

As is known to all, there are heterogeneities among Tregs 31 . In this study, we pinpointed a novel subset implicated in sorafenib resistance through cutting-edge single-cell analysis and the “scissor” algorithm. This subset, characterized by elevated BATF expression, aligns with regions of high ISDRS, suggesting a potential biomarker role for BATF. Our findings, validated across datasets, reveal a downregulation of ferroptosis and autophagy in these resistant Tregs, further underscoring the intricate relationship between BATF expression and sorafenib resistance mechanisms, positioning BATF as a candidate biomarker for therapeutic targeting.

While this study offers novel insights into sorafenib resistance, it acknowledges limitations such as reliance on retrospective data, the challenge of basing conclusions on a single gene set, and the preliminary nature of findings around specific genes like BATF. The need for prospective validation, deeper investigation into ISDGs, and consideration of geographical variations in epidemiology highlight the path forward for refining our understanding and therapeutic strategies.


## Conclusion

In this research, we elucidate the critical influence of ISD on HCC progression and treatment outcomes, spotlighting ISDRS with robust prognostic and predictive capabilities for HCC patient responses to sorafenib. Our findings suggest ISD may enhance Treg recruitment via the IL-6 pathway, fostering sorafenib resistance. Additionally, we identify BATF as a potential biomarker for sorafenib-resistant Tregs, although further validation is needed to confirm its utility.


## Electronic supplementary material

Below is the link to the electronic supplementary material.

Supplementary Material 1

Supplementary Material 2

Supplementary Material 3

Supplementary Material 4

Supplementary Material 5

Supplementary Material 6

Supplementary Material 7

Supplementary Material 8

Supplementary Material 9

Supplementary Material 10

Supplementary Material 11

Supplementary Material 12

Supplementary Material 13

Supplementary Material 14

Supplementary Material 15

Supplementary Material 16

Supplementary Material 17

Supplementary Material 18

Supplementary Material 19

We thank the TCGA, ICGC and GEO database for providing valuable and public datasets.

Shiji Wu, Xingte Chen, Huipeng Fang, Lei Wang, Junxin Wu contributed to conception and design. Shiji Wu, Huipeng Fang conducted data collection and analyzed the data. Shiji Wu, Xingte Chen, Lei Wang interpreted the data. Shiji Wu, Hong Liang, Shao Lingdong drafted the manuscript. Lei Wang, Wu Junxin contributed critical revision of the manuscript. Qizhen Huang conducted the sample collection. All authors read and approved the final manuscript.

This research was funded by Fujian Province Gastrointestinal, Respiratory, Genitourinary Malignant Tumor Radiotherapy Radiation and Treatment Clinical Medical Research Center (2021Y2014), Fujian Provincial Clinical Medical Research Center for Tumor Precision Radiotherapy (2020Y20101), Fujian Province Science and Technology Innovation Joint Funding Project (2021Y9216), Fujian Province Natural Science Foundation (2021J01438 and 2022J01433), Fujian Cancer Hospital In-Hospital Funding Program (2021YN10), the Fujian Provincial Clinical Research Center for Cancer Radiotherapy and Immunotherapy (2020Y2012), Fujian Province Natural Science Foundation (2023J011288); Fujian provincial health and family planning research talent training program (2020QNA013),and the National Clinical Key Specialty Construction Program.


## Data availability

The datasets presented in this study can be found in online repositories. Data linking：https://www.jianguoyun.com/p/DYKNqsoQrLzdCxib2b0FIAA.


## Consent for publication

All authors have approved the publication of this paper.

The authors declare no competing interests.


## Contributor Information

Lei Wang, Email: [EMAIL_REDACTED].

Junxin Wu, Email: [EMAIL_REDACTED].


## Associated Data


## Supplementary Materials

Supplementary Material 1

Supplementary Material 2

Supplementary Material 3

Supplementary Material 4

Supplementary Material 5

Supplementary Material 6

Supplementary Material 7

Supplementary Material 8

Supplementary Material 9

Supplementary Material 10

Supplementary Material 11

Supplementary Material 12

Supplementary Material 13

Supplementary Material 14

Supplementary Material 15

Supplementary Material 16

Supplementary Material 17

Supplementary Material 18

Supplementary Material 19


## Data Availability Statement

The datasets presented in this study can be found in online repositories. Data linking：https://www.jianguoyun.com/p/DYKNqsoQrLzdCxib2b0FIAA.