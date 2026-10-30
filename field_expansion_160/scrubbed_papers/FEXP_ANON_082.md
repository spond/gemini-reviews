# FEXP_ANON_082

## Abstract

Early diagnosis and prognostic evaluation of hepatocellular carcinoma (HCC) remain significant challenges in clinical management. This study aims to identify prognostic biomarkers in HCC and to explore their implications in immune microenvironment infiltration.

In this study, we constructed a single-cell transcriptomic atlas of HCC, focusing on the expression profiles of T cell-related genes. Analytical approaches included cell-cell communication analysis and pseudotime trajectory analysis. To further predict and validate T cell-associated prognostic genes, we integrated transcriptomic data from The Cancer Genome Atlas (TCGA) and Gene Expression Omnibus (GEO) datasets. Patients were stratified into high- and low-risk groups based on a prognostic model derived from these biomarkers. Immune infiltration levels in the tumor microenvironment were then evaluated across risk groups.

A total of eight primary tumor samples and seven normal tissue samples were included as raw data in this study. Following stringent quality control and filtering, 53,477 cells were retained for downstream analysis. From these, we isolated 12,333 T cells, which were subjected to further clustering and annotation. The T cell subpopulations identified included 6314 natural killer T cells (NK T cells), 5199 effector memory CD4 + T cells, and 820 central memory CD8 + T cells. By integrating transcriptomic data from TCGA-LIHC and GEO datasets, we identified six prognostic biomarkers: LYZ, SPP1, EGR1, MARCO, FCN3, and PTTG1. A prognostic model was developed based on these biomarkers, enabling risk stratification into high- and low-risk groups. The model demonstrated robust predictive performance in estimating patient survival rates and immune cell infiltration levels within the tumor microenvironment.

This study identified and validated prognostic biomarkers in HCC that effectively predict patient survival rates and immune infiltration characteristics. These findings provide a potential foundation for precision medicine strategies in HCC, offering novel insights into the tumor-immune microenvironment and its clinical implications.


## Introduction

Liver cancer ranks as the third leading cause of cancer-related mortality worldwide [ 1 ], characterized by its significant heterogeneity. Among all liver cancer cases, more than 90% are hepatocellular carcinoma (HCC), followed by intrahepatic cholangiocarcinoma (ICC) and combined hepatocellular cholangiocarcinoma (CHC) [ 1 – 3 ]. Liver cancer is associated with a multitude of risk factors, including hepatitis virus infections, non-alcoholic fatty liver disease (NAFLD), alcoholic fatty liver disease, smoking, diabetes, and obesity [ 4 ]. Current therapeutic strategies for liver cancer include surgical resection, liver transplantation, and chemotherapy. However, the majority of liver cancer patients are diagnosed at advanced stages, leading to poor outcomes for those undergoing drug treatment or local surgical interventions, except for liver transplantation [ 5 , 6 ]. Therefore, early diagnosis of liver cancer is crucial.

With the advancement of genomics and high-throughput sequencing technologies, researchers can now investigate liver cancer at the molecular level with high resolution using transcriptome sequencing. This approach has identified potential biomarkers, such as alpha-fetoprotein (AFP) [ 7 ]. However, studies have demonstrated that AFP is not a highly reliable diagnostic marker for liver cancer, as 32% to 59% of liver cancer patients exhibit normal AFP expression levels [ 8 , 9 ]. Single-cell RNA sequencing (scRNA-seq) offers higher resolution, enabling the identification and characterization of diverse cell types, thus providing insights into the heterogeneity of liver cancer [ 10 , 11 ]. Furthermore, scRNA-seq allows in-depth analysis of immune cell infiltration within the tumor microenvironment, facilitating the identification of diagnostic and prognostic biomarkers for liver cancer [ 12 – 14 ].

In this study, we utilized publicly available databases to obtain scRNA-seq and transcriptome data from HCC patients. We constructed a single-cell atlas of liver cancer samples, identified various cell types, and performed further analyses focusing on T cell subtypes using tools such as CellChat, SCENIC, and trajectory analysis. Additionally, we integrated transcriptome sequencing data from the TCGA and GEO databases to predict prognostic signature genes in HCC patients, constructed a prognostic model, and analyzed immune infiltration levels based on the risk scores derived from the model. This study provides valuable insights into the diagnosis and prognosis of liver cancer.


## Results


## Single-cell atlas of liver cancer

This study incorporated eight primary tumor tissues and seven normal tissue samples from the GSE149614 dataset as raw data. Low-quality data were filtered, retaining 53,477 cells for subsequent analysis. Samples were integrated using an anchoring integration method to eliminate batch effects. The integrated data underwent normalization, centering, and dimensionality reduction via PCA, retaining 20 dimensions. The t-SNE method was used to display clustering results. Figure 1 A shows the single-cell atlas among different samples, while Fig. 1 B presents the atlas of normal versus tumor samples. Figure 1 C reveals that 53,477 cells were clustered into 21 groups. Cell annotation using Single R identified eight cell types (Fig. 1 D), including CD79A-high B cells, FABP4-high endothelial cells, GNLY-high NK cells, IL7R-high T cells, ACTA2-high smooth muscle cells, APOA2-high hepatocytes, C1QB-high macrophages, and S100A8-high monocytes (Figs. 1 F, G). Figure 1 E displays the proportions of these cell types in different samples, with T cells, hepatocytes, and NK cells dominating the samples.


> **Fig. 1:** Single-cell atlas of hepatocellular carcinoma (HCC) patients. A t-SNE clustering of the samples. B t-SNE clustering of normal and tumor tissues. C t-SNE plot showing 21 clusters in single-cell samples. D t-SNE plot of identified cell types. E Proportions of different cell types in the samples. F Violin plots of the expression of eight cell marker genes. G t-SNE plots of eight cell marker genes


## Single-cell atlas and enrichment analysis of T cells

T cells constituted the majority in the liver cancer single-cell atlas. Therefore, 12,333 T cells were extracted for further clustering and annotation. Figure 2 A shows that T cells were reclustered into 17 groups, with annotations identifying 6,314 NK cells, 5,199 effector memory CD4 + T cells, and 820 central memory CD8 + T cells (Fig. 2 B). Figure 2 C and D display marker genes for each T cell subtype, including APOA2 for effector memory CD4 + T cells, CMC1 for NK cells, and RPL17 for central memory CD8 + T cells. Figure 2 E illustrates the top 10 DEGs for each subtype. GO enrichment analysis revealed that T cell-related genes were enriched in biological processes such as immune system regulation, immune response, and cell activation (Fig. 2 F). Cellular component enrichment highlighted cell surface, side of membrane, and external side of plasma membrane, while molecular function analysis emphasized signaling receptor binding, antigen binding, and immunoglobulin receptor binding. KEGG enrichment analysis revealed that T cell-related genes were primarily concentrated in the cytokine-cytokine receptor interaction pathway, lipid and atherosclerosis signaling pathway, and Toll-like receptor signaling pathway (Fig. 2 G).


> **Fig. 2:** Single-cell atlas of T cells in the samples. A t-SNE plot of T cells re-clustered into 17 clusters. B t-SNE plot of identified T cell types. C Bubble plot of marker genes for three T cell subtypes. D t-SNE plot of marker genes for three T cell subtypes. E Heatmap showing the top 10 differentially expressed genes in three T cell subtypes. F GO: BP enrichment analysis of T cell differentially expressed genes. G KEGG pathway enrichment analysis of T cell differentially expressed genes


## Cell-cell communication

Using the CellChat function, ligand-receptor interactions among different cell types were modeled, revealing intercellular communication networks (Fig. 3 A). Among signaling pathways, CXCL and TNF were frequently observed, with CXCR4 and TNFRSF18 showing high expression in multiple cell types (Fig. 3 B-G).


> **Fig. 3:** Cell-cell communication analysis. A Network diagram showing ligand-receptor interaction frequencies between different cell types. B Cell communication network in the CXCL signaling pathway. C Cell communication network in the TNF signaling pathway. D Heatmap of ligand-receptor interactions in the CXCL signaling pathway across different cells. E Heatmap of ligand-receptor interactions in the TNF signaling pathway across different cells. F Expression of representative genes in the CXCL signaling pathway across different cell types. G Expression of representative genes in the TNF signaling pathway across different cell types


## T cell trajectory analysis

Cell trajectory analysis, also known as pseudotime analysis, simulates the developmental trajectories of different cells based on the temporal expression of genes in single-cell samples. Developmental trajectories of T cells were analyzed using pseudotime sequencing. T cell differentiation followed two branches (Fig. 4 A), with five differentiation states observed during the process (Fig. 4 B, E). Figure 4 C and D illustrate the chronological progression of T cell differentiation, showing NK cells in the early stages and effector memory CD4 + and central memory CD8 + T cells at the terminal stages. Using the BEAM function, heatmaps depicted pseudotime gene expression in different branches. GO enrichment analysis indicated that branch 1 was associated with processes like regulation of leukocyte activation, response to unfolded protein, positive regulation of immune response, and leukocyte differentiation, while branch 2 was related to regulation of T cell activation, mononuclear cell differentiation, and cellular response to epidermal growth factor stimulus (Fig. 4 F, G).


> **Fig. 4:** Trajectory analysis of T cell differentiation. A Cell trajectory plot for T cell clusters. B Trajectory plot showing different stages of T cell differentiation. C Pseudotime cell trajectory plot of T cell development. D Trajectory plot of T cell subtypes differentiated by pseudotime. E Independent visualization of different stages of T cell subtype differentiation by pseudotime. F Differential gene expression along branch 1 divided into four subgroups, with GO: BP terms provided on the left. G Differential gene expression along branch 2 divided into four subgroups, with GO: BP terms provided on the left


## Prognostic signature prediction and validation

Differential gene analysis on the TCGA-LIHC dataset (Supplementary Figure: Volcano plot) identified 1629 DEGs. By intersecting these with the 1169 T cell-related DEGs from the single-cell dataset, 21 overlapping genes were obtained ( Fig. 5 A ) . The expression matrix was first normalized, followed by LASSO regression analysis to construct a prognostic model and calculate risk scores, with TCGA-LIHC as the training set and GSE25097 as the test set. Prognostic genes included LYZ, SPP1, EGR1, MARCO, FCN3, and PTTG1. Risk scores divided patients into high- and low-risk groups (Fig. 5 B–D, G). Kaplan–Meier curves showed poorer prognosis in the high-risk group for both training and test sets (Fig. 5 E, H). The time-dependent ROC curve results demonstrated that the aforementioned prognostic signature genes performed well in predicting overall survival for HCC patients at 1, 3, and 5 years (AUC ≈ 0.6 in both the training and testing sets) (Fig. 5 F, I). Bubble plots displayed the expression of six prognostic genes in single-cell samples (Fig. 6 A). The correlation between the expression of six prognostic genes and 22 immune cell types was analyzed, revealing strong associations between PTTG1 and various T cell subtypes (Fig. 6 B).


> **Fig. 5:** Prediction and validation of T cell-related prognostic signature genes. A Venn diagram of overlapping genes between T cell-related differentially expressed genes and TCGA-LIHC sample differentially expressed genes. B LASSO regression model constructed using TCGA-LIHC samples as the training set. C Cross-validation for optimizing model parameters. D Scatter plot of risk scores and survival status distribution in the training set. E Kaplan–Meier survival curve based on risk scores and survival status in the training set. F Time-dependent ROC curves predicting 1-, 3-, and 5-year survival probabilities for patients in the training set. G Scatter plot of risk scores and survival status distribution in the GSE25097 testing set. H Kaplan–Meier survival curve based on risk scores and survival status in the testing set. I Time-dependent ROC curves predicting 1-, 3-, and 5-year survival probabilities for patients in the testing set


> **Fig. 6:** Correlation analysis between T cell-related prognostic signature genes and immune cells. A Bubble plot of T cell-related prognostic signature gene expression in single-cell samples. B Heatmap of the correlation between T cell-related prognostic signature genes and immune cells


## Clinical correlation analysis

To further investigate risk factors for HCC and validate the risk scores of existing prognostic signature genes, Cox regression analysis was performed using clinical data from patients. Univariate Cox regression analysis identified tumor pathologic stage (HR = 1.833, 95% CI = 1.432–2.346, p < 0.001); T stage (HR = 1.309, 95% CI = 1.051–1.632, p < 0.05); N stage (HR = 1.323, 95% CI = 1.133–1.545, p < 0.001); M stage (HR = 2.241, 95% CI = 1.234–4.069, p < 0.01)and risk scores (HR = 2.337, 95% CI = 1.799–3.306, p < 0.001) as adverse prognostic factors for OS. Additionally, these factors were identified as poor prognostic indicators (Fig. 7 A). Multivariate analysis confirmed these as independent prognostic factors (HR = 1.664, 95% CI = 1.275–2.170, p < 0.001 for tumor pathologic stage; HR = 2.594, 95% CI = 2.013–3.911, p < 0.05 for T stage; HR = 3.005, 95% CI = 0.890–4.141, p < 0.05 for M stage; HR = 2.138, 95% CI = 1.618–2.826, p < 0.001 for risk score) (Fig. 7 B). A nomogram was constructed to evaluate clinical information, including age, gender, tumor T, N, M staging, and risk scores, predicting 1, 3, and 5-year survival probabilities (Fig. 7 C). Finally, decision curve analysis (DCA) of the prognostic model demonstrated superior net benefit compared to universal intervention or non-intervention strategies across clinically relevant risk thresholds (20%−80%), indicating its utility for optimizing clinical decision-making in hepatocellular carcinoma management (Fig. 7 D).


> **Fig. 7:** Analysis of clinical risk indicators in patients. A Univariate Cox regression analysis of patient age, sex, tumor stage, and risk score. B Multivariate Cox regression analysis of patient age, sex, tumor stage, and risk score. C Nomogram based on clinical information for predicting 1-, 3-, and 5-year survival probabilities in patients. D Decision curve analysis based on prognostic signature genes


## Immune infiltration analysis of prognostic genes

To explore the relationship between the tumor microenvironment and prognostic signature genes in high- and low-risk groups, the proportions of 22 immune cell types in the samples were visualized using the CIBERSORT algorithm (Fig. 8 A). Using the ESTIMATE algorithm, immune scores revealed significantly higher scores in the low-risk group ( p < 0.0001) (Fig. 8 B). ssGSEA analysis indicated higher proportions of regulatory T cells, M0 macrophages, plasma cells, and resting dendritic cells in the high-risk group, while the low-risk group showed more naive B cells, resting memory CD4 T cells, monocytes, M1 macrophages, M2 macrophages, and resting mast cells (Fig. 8 C). These findings suggest that low-risk patients possess higher proportions of immune cells with antitumor activity, highlighting the critical role of the immune microenvironment in tumor progression.


> **Fig. 8:** Immune infiltration analysis of T cell prognostic signature genes. A Proportions of 22 immune cell types. B Box plot of immune scores for patients grouped by high- and low-risk based on prognostic signature gene risk scores. C Comparison of infiltration levels of 22 immune cell types between high- and low-risk patient groups


## Discussion

T cells are well-known as pivotal components of the immune system, playing a crucial role in orchestrating immune responses and serving as key determinants in the elimination of cancer cells within the tumor microenvironment (TME) [ 15 , 16 ]. In this study, we constructed a single-cell map of HCC by analyzing 53,477 cells derived from eight primary tumor samples and seven normal tissue samples based on the publicly available, subsequently identifying 12,333 T cells. These T cells were further classified into three subtypes: 6314 NK T cells, 5199 effector memory CD4 + T cells, and 820 central memory CD8 + T cells. NK T cells are a critical component of tumor immune responses. Upon activation, they release cytotoxic substances, including perforin and granzymes, to directly lyse tumor cells [ 17 ]. Additionally, they secrete chemokines such as interferon-gamma (IFN-γ) and tumor necrosis factor-alpha (TNF-α), mediating immunoregulatory effects [ 18 , 19 ]. Effector memory CD4 + T cells represent a subtype of memory CD4 + T cells, which also include central memory T cells and tissue-resident memory T cells. These memory CD4 + T subsets collectively play indispensable roles in defending against pathogen invasion [ 20 – 22 ]. Effector memory CD4 + T cells, which constitute the majority of memory CD4 + T cells, preferentially recirculate between blood and peripheral tissues. They exhibit rapid effector functions, producing cytokines such as IFN-γ, IL-4, and IL-2 [ 23 , 24 ], and have demonstrated roles in inhibiting tumor progression and lymph node metastasis [ 25 ]. Central memory CD8 + T cells, a subset of memory CD8 + T cells alongside effector memory CD8 + T cells and tissue-resident memory cells, are essential for long-term protective immunity [ 26 , 27 ]. Among these subsets, central memory CD8 + T cells exhibit superior antitumor activity. Their longevity enables them to provide central immunosurveillance by patrolling lymphoid organs and peripheral tissue sites [ 28 – 30 ].

Cell-cell interaction network analysis highlighted the frequent involvement of the CXCL and TNF signaling pathways in intercellular communication. Heatmaps revealed that CXCL signaling was particularly active in interactions involving macrophages and B cells, macrophages and NK cells, and macrophages and T cells. Tumor-associated macrophages (TAMs), pivotal components of the tumor immune microenvironment, demonstrate remarkable plasticity by dynamically transitioning between anti-tumor M1 and pro-tumor M2 polarization states in response to microenvironmental signals [ 31 ]. Through integrated single-cell analysis, Li et al. delineated the cellular communication network between TAMs and T cells in HCC, identifying the CXCL10/CXCL11-CXCR3 and CXCL12-CXCR4 chemokine axes as critical mediators orchestrating immune crosstalk within the hepatic tumor landscape [ 32 ].Previous research by Xu et al. demonstrated that elevated levels of chemokines such as CXCL2 and CXCL8 recruit neutrophils, creating an immunosuppressive microenvironment that promotes HCC progression [ 33 ]. TNF signaling was prominent in interactions between endothelial cells and macrophages, NK cells and macrophages, and T cells and macrophages. As a multifunctional cytokine, TNF-α induces diverse biological responses in the liver, including hepatocyte apoptosis and necroptosis, liver inflammation and regeneration, and progression to HCC [ 34 – 36 ].

The prognosis of HCC remains poor. To identify precise diagnostic and prognostic markers and predict patient survival, we constructed a risk model by intersecting DEGs from the TCGA-LIHC and T-cell-related DEGs from GSE149614 datasets. This analysis identified six prognostic signature genes: LYZ, SPP1, EGR1, MARCO, FCN3, and PTTG1. Lysozyme (LYZ), an antimicrobial secretory protein expressed in monocytes and macrophages, is a key component of the innate immune system. Recent reports indicate that LYZ exhibits opposite expression patterns between tumor and adjacent normal tissues in different subtypes of HCC. Elevated expression of LYZ in HCC tissues is associated with poor prognosis. LYZ promotes HCC cell proliferation and migration via autocrine and paracrine interactions with GRP78 on the cell surface. Targeted inhibition of LYZ expression significantly reduces HCC growth in vitro and in vivo [ 37 , 38 ]. Secreted phosphoprotein 1 (SPP1) and macrophage receptor with collagenous structure (MARCO) are positively correlated with poor prognosis in HCC. SPP1-expressing macrophages enhance tumor stemness via a vitronectin-dependent paracrine mechanism, and targeting this macrophage-tumor feedback loop increases chemosensitivity in HCC. Similarly, MARCO-expressing tumor-associated macrophages exert strong immunosuppressive effects by secreting IFN-β and reducing the expression and infiltration of antigen-presenting molecules, and CD8 + T-cell dysfunction, creating an immunosuppressive TME. Targeting the macrophage subsets with high MARCO expression significantly improves resistance to anti-PD-L1 therapy in hepatocellular carcinoma, making it a promising therapeutic target [ 39 , 40 ]. Early growth response 1 (EGR1), a zinc-finger transcription factor, plays roles in cell growth, migration, apoptosis, and DNA repair. Downregulation of EGR1 in HCC promotes tumor cell proliferation and xenograft tumor growth by interacting with the promoter region of phosphofructokinase-1, liver type (PFKL), thereby repressing PFKL-mediated aerobic glycolysis [ 41 , 42 ]. The complement system, a component of the immune system, relies on FCN as one of its major constituents. Reduced FCN3 expression in HCC tissues correlates with poor prognosis. FCN3 overexpression inhibits the IR/SREBPc signaling axis, suppressing MUFA synthesis and promoting ferroptosis, thereby limiting HCC progression [ 43 , 44 ]. Pituitary tumor-transforming gene 1 (PTTG1) regulates cell cycle and apoptosis. High PTTG1 expression in HCC tissues is associated with poor prognosis. PTTG1 promotes asparagine synthetase (ASNS) transcription, elevating asparagine levels, which activate the mTOR pathway to drive HCC progression [ 45 , 46 ]. These prognostic genes are closely associated with HCC outcomes and could serve as potential diagnostic and therapeutic targets.

We validated the predictive accuracy of the risk model using the GSE25097 dataset. Immune cell infiltration analysis revealed that the low-risk group had higher proportions of naive B cells, resting memory CD4 + T cells, monocytes, M1 macrophages, M2 macrophages, and resting mast cells, suggesting a more robust immune infiltration in these patients. These findings further support the effectiveness of our prognostic model.

However, this study is limited by its reliance on publicly available datasets with small sample sizes and the absence of experimental validation. Future studies should incorporate larger clinical cohorts and molecular experiments to confirm these findings.


## Conclusion

In summary, this study utilized single-cell sequencing data to construct a single-cell atlas of HCC, providing insights into the roles of T cells in cellular differentiation, transcription factor regulatory networks, and intercellular communication. By integrating single-cell data with TCGA and GEO datasets, we identified and validated T-cell-related prognostic signature genes that predict 1-, 3-, and 5-year survival rates in HCC patients. Furthermore, these prognostic genes demonstrated predictive potential for immune infiltration in the TME.


## Methods


## Data acquisition and preparation

Single-cell data for liver cancer were obtained from the published study, “A single-cell atlas of the multicellular ecosystem of primary and metastatic hepatocellular carcinoma”, available in the Gene Expression Omnibus (GEO) database ( https://www.ncbi.nlm.nih.gov/gds ) under accession number GSE149614 [ 47 ]. Eight primary tumor tissues and seven normal tissue samples were selected as raw data. The inclusion criteria for this study were: (1) each sample contained between 300 and 7,000 cells; (2) each cell expressed more than 300 genes; (3) each gene was expressed in at least three cells [ 48 ]; and (4) mitochondrial RNA content was less than 20% in each cell. After filtering, we used the R package Seurat (version 4.1.3) to retain 53,477 cells for downstream analyses.

HCC RNA-seq data and corresponding clinical information were obtained from the TCGA public database via the GDC data portal ( https://gdc.xenahubs.net ), which includes 281 samples: 50 normal and 231 tumor samples. Differentially expressed genes (DEGs) were identified using the DESeq2 package (version 4.1.3) with thresholds of |log2FoldChange| >2 and adjusted p -value < 0.05 for downstream analyses [ 49 ]. Similarly, the GSE25097 dataset with corresponding clinical information, containing 268 tumor and 243 adjacent non-tumor samples, was obtained from the GEO database [ 50 ]. For this study, 221 tumor samples with comprehensive clinical data were selected for further analyses.


## Data integration

Following data filtering, normalization was performed using the “NormalizeData” function in the R Seurat package. Gene expression values were scaled by dividing each gene’s expression by the total expression per cell, multiplying by 10,000, and applying log transformation (log (number + 1)). Highly variable genes ( n = 3000) were identified using the “FindVariableFeatures” function, and centralization was applied using the “ScaleData” function. Data integration was achieved by setting 2000 anchor points using the “FindIntegrationAnchors” function. This integration strategy minimizes batch effects by aligning cell types across datasets based on anchor points [ 51 ].


## Dimensionality reduction and clustering

Given that each gene in the sample represents a distinct dimension, visualizing high-dimensional data can be challenging. To overcome this, we employed dimensionality reduction techniques to capture the underlying structure of the data using as few dimensions as possible [ 52 ]. To reduce the high dimensionality of single-cell data, we performed principal component analysis (PCA) on highly variable genes using the “RunPCA” function in the Seurat package. Subsequently, clustering was conducted using the “FindNeighbors” and “FindClusters” functions. For improved visualization of clustering results, t-distributed stochastic neighbor embedding (t-SNE) was employed via the “RunTSNE” function with parameters dims = 1:20 and resolution = 1.0.


## Cell annotation, DEG analysis, and marker gene identification

Cell types were annotated using the SingleR package, which calculates the correlation between single-cell gene expression and reference datasets to infer cell identities [ 53 ]. In this study, the “ref_Human_all” reference dataset was used for annotation. DEGs were identified using the “FindAllMarkers” function in Seurat with thresholds |log2FoldChange| >2 and adjusted p -value < 0.05. Marker genes for each cell type were identified using the “FindMarkers” function and visualized.


## GO and KEGG pathway enrichment analyses

Gene Ontology (GO) and Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway enrichment analyses were performed using the DAVID ( https://david.ncifcrf.gov/ ) and Metascape ( https://metascape.org/ ) databases. Results were visualized using the R package ggplot2 [ 54 , 55 ].


## Cell-cell communication analysis

Ligand-receptor interactions on cell surfaces play crucial roles in various biological processes. To explore intercellular interactions, the “CellChat” package was used to construct a cell communication network based on scRNA-seq data. This tool quantitatively infers and analyzes intercellular communication by modeling networks of ligands, receptors, and co-factors [ 56 ].


## Pseudotime analysis

Cellular processes are in a constant state of dynamic change, where one cell type transforms into another, accompanied by functional alterations. This transition results in distinct gene expression profiles before and after the change [ 57 ]. Pseudotime analysis organizes cells along a continuous trajectory, placing them in pseudotime according to their gene expression patterns. This method enables the classification of samples into distinct cell populations at various differentiation stages. In this study, we performed pseudotime analysis on T cell subsets using the Monocle2 package [ 58 ]. To explore the differentiation trajectories and associated genes of T cell subtypes in different states, we applied the “plot_cell_trajectory” function to arrange the cells along pseudotime. The “BEAM” function was utilized to identify genes involved in the differentiation of cells into distinct branches. The results were visualized using the “plot_genes_branched_heatmap” function.


## Lasso regression analysis

This study utilized the intersection of T-cell-related DEGs from liver cancer single-cell samples with DEGs from the TCGA-LIHC dataset. These intersecting genes were employed to construct a prognostic model, which was subsequently validated using the GSE25097 dataset. Both the construction and validation of the model employed the Least Absolute Shrinkage and Selection Operator (LASSO) method [ 59 ]. The “glmnet” package was used to identify prognostic genes and calculate risk scores. Patients were categorized into low-risk and high-risk groups based on the median risk score. Survival curves were plotted using the “Survival” package, risk plots were generated using the “ggrisk” package, and time-dependent receiver operating characteristic (ROC) curves were generated using the “timeROC” package to evaluate overall survival (OS) at 1, 3, and 5 years for liver cancer patients.


## Cox regression analysis and nomogram construction

Using the prognostic genes derived from the LASSO regression analysis and patients’ overall survival, univariate and multivariate Cox regression analyses were conducted to determine whether a risk factor could serve as an independent prognostic factor for liver cancer patients. These analyses were conducted using the “Survival” and “Survminer” packages, and forest plots were generated using the “foreplot” package. A nomogram was constructed using the “Survival”, “foreign”, “rms”, and “tidyverse” packages based on patients’ clinical information to provide an intuitive assessment of patient risk.


## Immune infiltration analysis

Gene expression data from liver cancer tumor tissue samples were analyzed using the “ESTIMATE” package to calculate immune scores. Patients were divided into high- and low-risk groups based on the median risk score predicted by the LASSO regression model, and results were visualized using GraphPad Prism (version 7.00). Using the “CIBERSORT” package, immune cell infiltration within the samples was visualized. CIBERSORT is a widely used tool for deconvoluting the immune cell expression matrix based on linear support vector regression, quantifying the proportion of infiltrating immune cells via marker gene expression [ 60 , 61 ].


## Data analysis

R (version 4.1.3) was employed for data processing and statistical analysis ( https://www.r-project.org/ , accessed on March 28, 2022). Statistical significance between two groups was analyzed using the Student’s t -test, while the Wilcoxon test was used for continuous variable correlations. Kaplan–Meier analysis with log-rank statistics was conducted to evaluate survival differences between high- and low-risk groups. A p -value of < 0.05 was considered statistically significant.


## Data availability

This study only conduct analysis based on TCGA and GEO public database, with no experiments on humans and/or the use of human tissue samples involved.

The authors would like to express their gratitude to Yi Tong for providing assistance in editing and refining the manuscript.

Y. Z.and X. F. participated in the design of research ideas and the drafting of manuscripts. S.L., P.Y. and J.W. made some well-intentioned suggestions. J. L., H. L., and P. L. helped analyse the data. M. G. and T.Z. helped draw relevant pictures.

This work was supported by the Natural Science Foundation of China (Grant NO.82074284), China National Traditional Chinese Medicine Inheritance and Innovation Team Sub-project (Grant No. ZYYCXTD-C-202005-10), China Medical Association of Minorities Research Project (Grant No. 2020MZ298-110101), Open Fund Project, Associated Key Laboratory of Traditional Mongolia Medicine Research and Development, National Ethnic Affairs Commission and Ministry of Education of China (Grant No. MDK2020013).


## Data availability

The datasets analysed during the current study are available in the GEO and TCGA repositories, https://www.ncbi.nlm.nih.gov/gds and https://gdc.xenahubs.net .


## Consent for publication

The authors declare no competing interests.


## Contributor Information

Peizhi Ye, Email: [EMAIL_REDACTED].

Jiarui Wu, Email: [EMAIL_REDACTED].


## Associated Data


## Data Availability Statement

This study only conduct analysis based on TCGA and GEO public database, with no experiments on humans and/or the use of human tissue samples involved.

The datasets analysed during the current study are available in the GEO and TCGA repositories, https://www.ncbi.nlm.nih.gov/gds and https://gdc.xenahubs.net .