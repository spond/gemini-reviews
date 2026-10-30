# FEXP_ANON_042

## Abstract

Pancreatic head cancer (PHC) and pancreatic body/tail cancer (PBTC) have distinct clinical and biological behaviors. The microbial and metabolic differences in PHC and PBTC have not been studied. The pancreatic microbiota and metabolome of 15 PHC and 8 PBTC tissues and their matched nontumor tissues were characterized using 16S rRNA amplicon sequencing and untargeted metabolomics. At the genus level, Bradyrhizobium was increased while Corynebacterium and Ruminococcus were decreased in the PHC tissues (Head T) compared with the matched nontumor tissues (Head N) significantly. Shuttleworthia , Bacillus , and Bifidobacterium were significantly decreased in the PBTC tissues (Body/Tail T) compared with the matched nontumor tissues (Body/Tail N). Significantly, Ileibacterium was increased whereas Pseudoxanthomonas was decreased in Head T and Body/Tail T, and Lactobacillus was increased in Head T but decreased in Body/Tail T. A total of 102 discriminative metabolites were identified between Head T and Head N, which were scattered through linoleic acid metabolism and purine metabolism pathways. However, there were only four discriminative metabolites between Body/Tail T and Body/Tail N, which were related to glycerophospholipid metabolism and autophagy pathways. The differential metabolites in PHC and PBTC were commonly enriched in alpha‐linolenic acid metabolism and choline metabolism in cancer pathways. Eubacterium decreased in Head T was positively correlated with decreased linoleic acid while negatively correlated with increased arachidyl carnitine and stearoylcarnitine. Bacillus decreased in Body/Tail T was negatively correlated with increased L‐carnitine. These microbiota and metabolites deserve further investigations to reveal their roles in the pathogenesis of PHC and PBTC, providing clues for future treatments.

bile acid–cholic acid

adoptive T cell therapy

Akaike information criterion

American Joint Committee on Cancer

PBTC‐matched nontumor tissues

central carbon metabolism

glycerophosphocholine

PHC‐matched nontumor tissues

Kyoto Encyclopedia of Genes and Genomes

Kirsten rat sarcoma viral oncogene homolog

liquid chromatography–mass spectrometry

linear discriminant analysis

linear discriminant analysis effect size

mitogen‐activated protein kinase

orthogonal least partial squares discriminant analysis

operational taxonomic unit

pancreatic body/tail cancer

principal coordinate analysis

pancreatic ductal adenocarcinoma

pancreatic head cancer

short‐chain fatty acids

tumor microenvironment

Union for International Cancer Control

variable importance in the projection


## INTRODUCTION

Pancreatic cancer, mainly pancreatic ductal adenocarcinoma (PDAC), is one of the most lethal diseases in the world. PDAC is the third leading cause of cancer‐related death in the United States, with a 5‐year survival rate of only 12%. 1 It is predicted to become the second leading cause of cancer‐related death in the United States by 2030. 2

Pancreatic ductal adenocarcinoma is a multifactorial disease, and the initiation, progression, and metastasis of PDAC require changes in the tumor microenvironment (TME). 3 As a part of the TME, microbiota have received increasing attention because they affect the growth and spread of PDAC in a variety of ways. 4 Microbiota cause changes in metabolism, contributing to metabolic diseases such as obesity and diabetes, which are also essential factors in the development of PDAC. 5 , 6 For example, short‐chain fatty acids (SCFAs), which are enriched in obese individuals, can activate the mitogen‐activated protein kinase (MAPK) signaling pathway through G‐protein‐coupled receptors, leading to cancer cell proliferation. 6 Microbiota may participate in the development of PDAC through some metabolic mechanisms.

Pancreatic ductal adenocarcinoma can be divided into pancreatic head cancer (PHC) and pancreatic body/tail cancer (PBTC) according to its anatomical structure. 7 There is increasing evidence that tumors at different sites exhibit different clinical manifestations, patient outcomes, and genetic or molecular diversity. 8 , 9 Patients with PBTC had a lower rate of tumor‐related surgery (16% vs. 30%) and a lower median survival time (4 vs. 6 months) than patients with PHC. 10 The survival difference is attributed to the relatively late clinical presentation of PBTC and the lack of overt symptoms such as obstructive jaundice. 11 However, there is also evidence proving that the worse survival of PBTC is unrelated to the disease stage. 12 The frequency of SMAD4 mutation in PBTC was higher than in PHC at early stages. In the late stage, PBTC had a higher Kirsten rat sarcoma viral oncogene homolog (KRAS) mutation rate and MAPK pathway mutation frequency. 9

These differences in prognosis and molecular characteristics between PHC and PBTC have been explored for decades. However, the microbial and metabolic differences between PHC and PBTC have yet to be thoroughly studied. We aimed to investigate the microbial and metabolic differences between PHC and PBTC and to explore the etiology and development of PHC and PBTC by 16S rRNA amplicon sequencing and untargeted metabolome analysis.


## MATERIALS AND METHODS


## Samples

We performed an observational study of 23 PDAC patients who underwent PDAC surgery enrolled from January 2022 to December 2022 at the Qilu Hospital of Shandong University. According to the Union for International Cancer Control (UICC), we divided the patients with PDAC into a PHC group and a PBTC group, including 15 patients with lesions at the uncinate process, head, and neck of the pancreas and 8 patients with lesions at the body and tail of the pancreas. 13 All PDAC patients were diagnosed via postoperative pathology. The exclusion criteria were as follows: (I) comorbidity with other cancers; (II) underwent preoperative chemotherapy, radiotherapy, or other biological treatment; and (III) use of routine antibiotics, probiotics, prebiotics, or synbiotics in the previous month. The clinicopathological staging was in accordance with the 8th edition of the American Joint Committee on Cancer (AJCC) TNM staging system for PDAC. The research followed the Declaration of Helsinki and was approved by the Ethics Committee of the Qilu Hospital of Shandong University (KYLL‐202107‐097). Informed written consent was obtained from each patient before enrollment.


## DNA extraction, 16S rRNA amplicon sequencing, and data analysis

According to the manufacturer's instructions, total microbial genomic DNA was extracted from pancreatic samples using the E.Z.N.A.® soil DNA Kit (Omega Bio‐tek). The quality and concentration of DNA were determined by 1.0% agarose gel electrophoresis and a NanoDrop® ND‐2000 spectrophotometer (Thermo Scientific Inc.). The hypervariable region V3–V4 of the microbial 16S rRNA gene was amplified with primer pairs 338F and 806R by an ABI GeneAmp® 9700 PCR thermocycler (ABI). Purified amplicons were pooled in equimolar amounts, and paired‐end sequenced on an Illumina MiSeq PE300 platform/NovaSeq PE250 platform (Illumina) according to the standard protocols by Majorbio Bio‐Pharm Technology Co. Ltd. Raw FASTQ files were demultiplexed using an in‐house perl script and then quality filtered by fastp version 0.19.6 and merged by FLASH version 1.2.7. 14 Then the optimized sequences were clustered into operational taxonomic units (OTUs) using UPARSE 7.1 with a 97% sequence similarity level. Bioinformatic microbiome analysis was carried out using the Majorbio Cloud platform ( https://cloud.majorbio.com ). Stepwise regression analysis was performed in the R environment (v4.3.3) using MASS package. 15


## Metabolome detection and data analysis

To extract the metabolites, 50 mg of tissue samples was used. The instrument platform for liquid chromatography–mass spectrometry (LC/MS) analysis was the UHPLC‐Q Exactive system of Thermo Fisher Scientific. The mobile phases consisted of 0.1% formic acid in water–acetonitrile (95:5, v/v) (solvent A) and 0.1% formic acid in acetonitrile–isopropanol–water (47.5:47.5:5, v/v) (solvent B). The solvent gradient changed according to the following conditions: from 0 to 0.1 min, 0% B to 5% B; from 0.1 to 2 min, 5% B to 25% B; from 2 to 9 min, 25% B to 100% B; from 9 to 13 min, 100% B to 100% B; from 13 to 13.1 min, 100% B to 0% B; from 13.1 to 16 min, 0% B to 0% B for equilibrating the systems. The sample injection volume was 2 μL, and the flow rate was 0.4 mL/min. The raw data of LC/MS was preprocessed by Progenesis QI (Waters Corporation) software. The metabolites were searched and identified, and the primary databases were the HMDB ( http://www.hmdb.ca/ ), Metlin ( https://metlin.scripps.edu/ ), and Majorbio Database. After the database search, the data were uploaded to the Majorbio cloud platform ( https://cloud.majorbio.com ) for data analysis. 16 The R package ropls (Version 1.6.2) performed the orthogonal least partial squares discriminant analysis (OPLS‐DA). The metabolites with variable importance in the projection (VIP) >1 and p < 0.05 were significantly differential. The functions of these metabolites and metabolic pathways were analyzed using the Kyoto Encyclopedia of Genes and Genomes (KEGG) database. Stepwise regression analysis was performed with the R environment (v4.3.3) using MASS package. 15


## Combined microbiome–metabolome analysis

According to the one‐to‐one correspondence relationship between samples, the correlation between the different microbiota and metabolites was calculated. Spearman correlation calculation method was utilized for the correlation algorithm.


## RESULTS


## Differences in microbial diversity, richness, and composition between PHC and PBTC

We enrolled 23 subjects, of whom 15 had PHC and 8 had PBTC (Figure 1 ). Basic demographic and clinical data were collected during inclusion (Table S1 ). We first measured the pancreatic microbial alpha diversity using different methodologies. Both the Sobs and Shannon indices of the PHC tissues (Head T) were lower than those of the matched nontumor tissues (Head N), and those of the PBTC tissues (Body/Tail T) were also lower than those of the matched nontumor tissues (Body/Tail N), although there was no significant difference (Figure 2A,B ). We performed a beta diversity analysis to compare the microbial composition. Clustering was detected for the weighted UniFrac principal coordinate analysis (PCoA) between Head T, Body/Tail T, and the matched nontumor tissues (Figure 2C ). At the phylum level, the top five pancreatic bacteria identified in Head N and Head T were Proteobacteria , Firmicutes , Bacteroidota , unclassified_k__norank_d__Bacteria , and Actinobacteriota , indicating a broad phyla‐level similarity with Body/Tail T and Body/Tail N flora (Figure 2D ). However, differences emerged at the genus level. The top ten genera in Head T were Achromobacter , Enterococcus , Pedobacter , Pseudomonas , Lactobacillus , Acinetobacter , Streptococcus , Peptostreptococcus , others, and unclassified_k__norank_d__Bacteria . The top ten genera in Head N were Achromobacter , Pedobacter , Enterococcus , Pseudomonas , unclassified_k__norank_d__Bacteria , others, Peptostreptococcus , Lactobacillus , Streptococcus , and Veillonella . Achromobacter , Pedobacter , Acinetobacter , Pseudomonas , unclassified_k__norank_d__Bacteria , others, Peptostreptococcus , Streptococcus , Gemella , and Veillonella were the top ten genera detected in Body/Tail T. Lastly, the top ten genera in Body/Tail N were Achromobacter , Pedobacter , unclassified_k__norank_d__Bacteria , Pseudomonas , others, Lactobacillus , Acinetobacter , Streptococcus , Staphylococcus , and Kocuria (Figure 2E ). We provided stacked bar plots for all samples at the phylum and genus levels (Figures S1 and S2 ).


> **FIGURE 1:** Overview of the study design. Using 16S rRNA amplicon sequencing and untargeted metabolomics, the pancreatic microbiota and metabolome of 15 pancreatic head cancer (PHC) and 8 pancreatic body/tail cancer (PBTC) tissues and their matched nontumor tissues were characterized.


> **FIGURE 2:** Altered pancreatic microbiota in 15 pancreatic head cancer (PHC) tissues and 8 pancreatic body/tail cancer (PBTC) tissues compared with matched nontumor tissues. (A, B) The Sobs and Shannon indices were used to evaluate the microbial diversity of the four groups. The Sobs index reflects species richness, and the Shannon index reflects species richness and evenness. (C) Principal coordinate analysis (PCoA) of weighted UniFrac distance demonstrated that the four groups showed four distinct clusters. OTU, operational taxonomic unit. (D, E) The microbial relative abundance of the four groups at the phylum and genus levels.


## Analysis of the differential microbiota between Head T and Head N

The linear discriminant analysis (LDA) effect size (LEfSe) method (LDA >2.5, corrected p ‐value <0.05) was used to analyze the microbial composition in Head T and Head N. At the order level, only Cyanobacteriales was significantly increased in Head T compared with Head N, while Oscillospirales , Corynebacteriales , Bacillales , and Oceanospirillales were significantly decreased. At the genus level in Head T, we observed a significant elevation of Lactobacillus , Rhodobacter , Faecalibaculum , and Bradyrhizobium but a significant reduction of Corynebacterium , Pseudoxanthomonas , BIyi10 , Eubacterium , Oscillibacter , and so on. (Figure 3A,B ). Based on these differential genera, we performed stepwise regression and identified the genera with the best Akaike information criterion (AIC) values, including Coprococcus , Faecalibaculum , Nocardioides , and so on (Table S2 ).


> **FIGURE 3:** Differential microbiota between Head T and Head N. (A, B) Differential microbiota at different levels and cladogram identified by linear discriminant analysis (LDA) effect size (LEfSe) analysis (LDA > 2.5, Q < 0.05).


## Analysis of the differential microbiota between Body/Tail T and Body/Tail N

Similarly, the LEfSe method (LDA >2.5, corrected p ‐value <0.05) was used to analyze the microbial composition in Body/Tail T and Body/Tail N. At the order level, there was no microbiota significantly increased in Body/Tail T. Meanwhile, Micrococcales , Rhizobiales , Chloroplast , Actinomycetales , Bacillales , Sphingomonadales , and Christensenellales were significantly decreased in Body/Tail T. At the genus level in Body/Tail T, we observed a significant elevation of Ileibacterium but a significant reduction of Lactobacillus , Terrisporobacter , Actinomyces , Shuttleworthia , Pseudoxanthomonas , and so on. (Figure 4A,B ). After stepwise regression, the genera of Bacillus , Ileibacterium , Pseudoxanthomonas , and so on were identified with the best AIC values (Table S3 ).


> **FIGURE 4:** Differential microbiota between Body/Tail T and Body/Tail N. (A, B) Differential microbiota at different levels and cladogram identified by linear discriminant analysis (LDA) effect size (LEfSe) (LDA > 2.5, Q < 0.05).


## Differential microbiota in Head T and Body/Tail T compared with their respective nontumor samples

Microbial composition was analyzed using the Wilcoxon signed‐rank test (Table S4 ). At the family level, Muribaculaceae was increased while Leuconostocaceae was decreased in both Head T and Body/Tail T. At genus level, Ileibacterium and g__norank_f__Muribaculaceae were significantly increased while Weissella was significantly decreased in both Head T and Body/Tail T. Besides, we observed a significant enrichment of Peptostreptococcus whereas a significant reduction of Prevotella , Corynebacterium , g__unclassified_f__Lachnospiraceae , UCG‐005 , and so on in Head T. We also observed a significant reduction of Staphylococcus , g__norank_f__MWH‐CFBk5 , Novosphingobium , and Curtobacterium in Body/Tail T.


## Differences in the metabolome between Head T and Head N

By LC/MS analysis, we further investigated the differences in the metabolome between Head T and Head N. OPLS‐DA showed that Head T and Head N were separated into two distinct clusters (R2Y = 0.958 and R2X = 0.424) (Figure 5A ). The test for the OPLS‐DA model illustrated that the R2 value was larger than the Q2 value and that the Q2 regression line had a negative intercept (R2 = [0.0, 0.9001], Q2 = [0.0, −0.3442]), indicating that the OPLS‐DA model for this study was valid (Figure 5B ). A total of 310 metabolites (VIP >1 and p < 0.05) altered significantly in Head T compared with Head N; 150 were upregulated and 160 downregulated (Figure 5C ). After p ‐value correction by the Bonferroni method, 102 significantly different metabolites were identified between Head T and Head N (Table S5 ). VIP analysis showed that PC(18:3(9,11,15)‐OH(13)/16:0), glutaminylcysteine, ectoine, N‐Succinimidyl 6‐maleimidohexanoate, arabinofuranosylcytosine, and so on were significantly upregulated while neoporrigenin B, arg‐3‐hyp‐7‐phe‐bradykinin, lysoPC(22:5(4Z,7Z,10Z,13Z,16Z)/0:0), PC(20:5(7Z,9Z,11E,13E,17Z)‐3OH(5,6,15)/DiMe(13,5)), tryptophyl‐glutamine, and so on were significantly downregulated in Head T (Figure 5D ). The discriminative metabolites were enriched in multiple pathways, including linoleic acid metabolism, purine metabolism, alpha‐linolenic acid metabolism, nucleotide metabolism, central carbon metabolism (CCM) in cancer, glyoxylate and dicarboxylate metabolism, glutathione metabolism, PPAR signaling pathway, arginine biosynthesis, protein digestion and absorption, and so on (Figure 5E,F and Table S6 ). The linoleic acid metabolism pathway was the top enriched pathway in Head T. Based on these differential metabolites, we also screened more important differential metabolites by stepwise regression, including L‐glutamine, arachidyl carnitine, stearoylcarnitine, and so on (Table S7 ).


> **FIGURE 5:** Metabolite differences between Head T and Head N. (A, B) Orthogonal least partial squares discriminant analysis (OPLS‐DA) showed that Head T and Head N were separated into two clusters. Test for the OPLS‐DA model showed that the model for this study was valid. (C) Volcano map of differential metabolites between Head T and Head N (variable importance in the projection [VIP] >1 and p < 0.05). (D) Heatmap of representative differential metabolites between Head T and Head N. The right side shows the VIP bar chart of the metabolite, and the length of the bar represents the contribution value of the metabolite to the difference between the two groups, * p < 0.05; ** p < 0.01; *** p < 0.001. (E) The abscissa represents the pathway name, and the ordinate axis represents the enrichment rate, which represents the ratio of the number of metabolites enriched in the pathway to the number of metabolites annotated to the pathway (background number). The larger the ratio, the greater the degree of enrichment. (F) Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway‐based differential abundance scoring of Head T. The differential abundance score reflects the overall changes of all metabolites in the metabolic pathway, with a differential abundance score of 1 indicating an upregulation of the expression trend of all annotated differential metabolites in the pathway and −1 indicating a downregulation of the expression trend of all annotated differential metabolites in the pathway. The size of the dot indicates the number of differential metabolites annotated in the pathway.


## Differences in the metabolome between Body/Tail T and Body/Tail N

We also explored the differences in the metabolome between Body/Tail T and Body/Tail N by LC/MS analysis. OPLS‐DA showed that the two groups were also separated into two distinct clusters (R2Y = 0.988 and R2X = 0.403) (Figure 6A ). The test for the OPLS‐DA model illustrated that the R2 value was larger than the Q2 value and that the Q2 regression line had a negative intercept (R2 = [0.0, 0.9676], Q2 = [0.0, −0.0203]), indicating that the OPLS‐DA model for this study was valid (Figure 6B ). A total of 102 metabolites (VIP >1 and p < 0.05) changed in Body/Tail T compared with Body/Tail N; 72 were upregulated and 30 downregulated (Figure 6C ). Following p ‐value correction by the Bonferroni method, four significantly different metabolites were discovered between Body/Tail T and Body/Tail N (Table S8 ). VIP analysis showed glycyrrhizin, cinobufotalin, zedoarondiol, 2‐hydroxydecanoate, (2S,3R)‐2‐amino‐4‐octadecene‐3‐ol, and so on were significantly upregulated while lysoPC(20:0/0:0), (3Z)‐2‐propylpent‐3‐enoic acid, propafenone, deoxyloganin, lysoPI(18:1(9Z)/0:0), and so on were significantly downregulated in Body/Tail T (Figure 6D ). The discriminative metabolites were enriched in multiple pathways, including choline metabolism in cancer, glycerophospholipid metabolism, retrograde endocannabinoid signaling, autophagy–other, pathogenic Escherichia coli infection, alpha‐linolenic acid metabolism, apoptosis, butanoate metabolism, Kaposi sarcoma‐associated herpesvirus infection, autophagy–animal, and so on (Figure 6E,F and Table S9 ) The choline metabolism in cancer pathway was the top enriched pathway in Body/Tail T. We further screened more important differential metabolites by stepwise regression and deferoxamine, L‐carnitine, citrulline, and so on were found with the best AIC values (Table S10 ).


> **FIGURE 6:** Metabolite difference between Body/Tail T and Body/Tail N. (A, B) Orthogonal least partial squares discriminant analysis (OPLS‐DA) showed that Body/Tail T and Body/Tail N were separated into two clusters. Test for the OPLS‐DA model showed that the model for this study was valid. (C) Volcano map of differential metabolites between Body/Tail T and Body/Tail N (variable importance in the projection [VIP] >1 and p < 0.05). (D) Heatmap of representative differential metabolites between Body/Tail T and Body/Tail N. The right side shows the VIP bar chart of the metabolite, and the length of the bar represents the contribution value of the metabolite to the difference between the two groups, * p < 0.05; ** p < 0.01; *** p < 0.001. (E) The abscissa represents the pathway name, and the ordinate axis represents the enrichment rate, which represents the ratio of the number of metabolites enriched in the pathway to the number of metabolites annotated to the pathway (background number). The larger the ratio, the greater the degree of enrichment. (F) Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway‐based differential abundance scoring of Body/Tail T. The differential abundance score reflects the overall changes of all metabolites in the metabolic pathway, with a score of 1 indicating an upregulation of the expression trend of all annotated differential metabolites in the pathway and −1 indicating a downregulation of the expression trend of all annotated differential metabolites in the pathway. The size of the dot indicates the number of differential metabolites annotated in the pathway.


## Differential metabolites and pathways in Head T and Body/Tail T compared with their respective nontumor samples

Compared with the PBTC, there were more differential metabolites between Head T and Head N. Some of the differential metabolites in Head T and Body/Tail T compared with their respective nontumor samples are the same, as are the trends of content changes in T groups. PC(18:3(9,11,15)‐OH(13)/16:0), glutaminylcysteine, arabinofuranosylcytosine, arachidyl carnitine, palmitoyl‐L‐carnitine, and formyl‐5‐hydroxykynurenamine were enriched in both Head T and Body/Tail T. In contrast, kukoamine D, deoxyloganin, and ditekiren were reduced in both Head T and Body/Tail T. However, prostaglandin A2, buthionine sulfoximine, and thymopentin (TP5) were significantly reduced only in Head T, whereas deferoxamine was significantly reduced only in Body/Tail T. The alpha‐linolenic acid metabolism and choline metabolism in cancer pathways were significantly enriched in both Head T and Body/Tail T. The OPLS‐DA score plot delineated that Head N and Body/Tail N were not divided into two clusters (R2Y = 0.891 and R2X = 0.301) (Figure S3 ).


## The relationship between differential genera and metabolites

Spearman's correlation analysis was performed to analyze the relationship between differential genera and metabolites identified by stepwise regression. In Head T, Eubacterium , Corynebacterium , and Coprococcus were significantly decreased. Eubacterium was significantly positively correlated with linoleic acid while negatively correlated with the increased arachidyl carnitine and stearoylcarnitine. Corynebacterium and Coprococcus were significantly negatively correlated with the increased hypoxanthine, arachidyl carnitine, and stearoylcarnitine (Figure 7A ). In Body/Tail T, Ileibacterium was significantly increased and negatively correlated with the decreased LysoPC(20:0/0:0). Decreased Bacillus was negatively correlated with the increased L‐carnitine (Figure 7B ).


> **FIGURE 7:** The correlation analysis between differential genera and metabolites identified by stepwise regression using Spearman's correlation method. (A) Head T versus Head N; (B) Body/Tail T versus Body/Tail N. The abscissa represents differential genera, and the ordinate represents differential metabolites. * p < 0.05; ** p < 0.01; *** p < 0.001.


## DISCUSSION

To our knowledge, this is the first study to explore the differences in microbiota and metabolites between PHC and PBTC. The correlation between microbiota and metabolites was preliminarily discussed. Most interestingly, we found that the Eubacterium decreased in Head T was positively correlated with decreased linoleic acid while negatively correlated with increased arachidyl carnitine and stearoylcarnitine. Bacillus decreased in Body/Tail T was negatively correlated with increased L‐carnitine.

Herein, the richness and diversity of Head T and Body/Tail T were lower than those of the matched nontumor tissues. Riquelme et al. found a higher alpha diversity in the pancreatic tumor microbiota of long‐term survival (LTS) PDAC patients compared with short‐term survival (STS) patients, which may contribute to the antitumor response by favoring recruitment and activation of CD8 + T cells (CTLs) and determining a differential enrichment of metabolic pathways between LTS and STS cases. 17 Whether higher microbial alpha diversity can inhibit the occurrence of PDAC warrants further investigation.

There were some similar differential microbes in Head T and Body/Tail T compared with their respective nontumor samples. These may be involved in the occurrence of PHC and PBTC simultaneously. At the genus level, Ileibacterium was significantly increased in both Head T and Body/Tail T, which has been demonstrated to promote colorectal cancer progression by synthesizing bile acid–cholic acid (AA‐CA). 18 Pseudoxanthomonas was significantly decreased in both Head T and Body/Tail T, which has been identified as an intratumoral microbiome signature highly predictive of long‐term survivorship. 17 Lactobacillus was increased in Head T but decreased in Body/Tail T, which has been found to induce anticancer action by enhancing cancer cell apoptosis and protecting against oxidative stress. 19 This may be associated with the worse prognosis of PBTC.

Microbiota that differ only in Head T or Body/Tail T may influence the development of PDAC. At the genus level, Bradyrhizobium was increased in Head T, and Bradyrhizobium japonicum has been found in patients with lung cancer, which is associated with gut microbiota‐associated genomic instability. 20 Corynebacterium and Ruminococcus were decreased in Head T. Studies have confirmed that Corynebacterium parvum can exhibit an antitumor activity. 21 Ruminococcus was decreased in colon cancer and can modulate the efficacy of cancer immunotherapy. 22 Shuttleworthia , Bacillus , and Bifidobacterium were decreased in Body/Tail T. Shuttleworthia has been identified as enriched in responders to neoadjuvant chemoradiotherapy of rectal cancer patients. 23 Bacillus subtilis can ameliorate intestinal tumorigenesis. 24 The well‐known probiotic Bifidobacterium has been proved by many studies to promote antitumor immunity and facilitate response to checkpoint inhibitor immunotherapy. 25 Whether these differential microbiota are involved in the occurrence of PHC and PBTC needs to be further studied.

These differential metabolites in Head T and Body/Tail T compared with their respective nontumor samples were commonly related to the alpha‐linolenic acid metabolism and choline metabolism in cancer pathways. The abnormal choline metabolism is accompanied by elevations in phosphocholine (PCho) and glycerophosphocholine (GPC) and may serve as a marker of metabolic reprogramming in cancer because tumor cells convert a large amount of choline into phosphatidylcholine to synthesize cell membranes. Furthermore, the abnormal choline metabolite profile can be used as an assistant method for diagnosing tumors. 26 Differently, the differential metabolites of PHC were also enriched in the pathways, including linoleic acid metabolism, purine metabolism, CCM in cancer, and so on. Linoleic acid is the main component of the linoleic acid metabolism pathway and was decreased in Head T. Linoleic acid is a primary positive regulator of CTL activity, making linoleic acid treatment an adoptive T cell therapy (ACT) potentiator in tumor therapy. 27 Purine metabolism pathway has been found to be significantly enriched in PDAC. 28 In our study, the abundance of L‐lactic acid and L‐glutamine in the CCM in cancer pathway was increased significantly in Head T. Circulating lactic acid is an essential contributor to tumors' tricarboxylic acid (TCA) cycle. 29 The accumulation of lactic acid plays a vital role in establishing a favorable microenvironment for tumor occurrence. L‐glutamine is involved in many pathways, including purine metabolism, CCM in cancer, and glutamatergic synapse pathways, which is crucial for many cell functions of cancer cells. 30 Therefore, it is a potential therapeutic target for PDAC. In contrast, the differential metabolites of PBTC were enriched in glycerophospholipid metabolism and autophagy pathways. LysoPCs are involved in the glycerophospholipid metabolism pathway. Studies have found that the reduced lysoPC level was related to the activation of inflammatory state in cancer. 31 Autophagy was upregulated in PDAC and could contribute to tumor survival and growth and facilitate metastasis when subjected to environmental stresses. 32 , 33 These pathways may be potential therapy targets particularly for PBTC.

According to Spearman's correlation analysis, there may be mutual influences between the differential microbiota and metabolites. In Head T, reduced Eubacterium , Corynebacterium , and Coprococcus , exerting anticancer activity, 21 , 34 were generally negatively correlated with enriched arachidyl carnitine and stearoylcarnitine. Accordingly, arachidyl carnitine is reported as a serum biomarker for hepatocellular carcinoma. 35 Stearoylcarnitine showed a strong metabolite risk signal associated with prostate cancer. 36 Eubacterium was significantly positively correlated with the anticancer linoleic acid. In Body/Tail T, enriched Ileibacterium was negatively correlated with the reduced anticancer LysoPC(20:0/0:0). Reduced antibiotics Bacillus was negatively correlated with enriched L‐carnitine, which can protect tumor cells and lead to poor survival in glioblastoma multiforme. 37 This indicated that the differential microbiota may influence the occurrence of PHC and PBTC by upregulating or downregulating their related metabolites. However, the underlying mechanisms remain to be clarified.

Our study also had several limitations. First, the sample size of PHC and PBTC was limited. Second, no further experiments have been undertaken to determine whether the differences in the microbiota and metabolome were results or causes of PHC and PBTC. Third, we did not follow up on the prognosis to verify the difference in survival between PHC and PBTC patients. Furthermore, the matched nontumor tissues were not completely normal tissues, and chronic pancreatitis may occur due to obstruction of main pancreatic duct, especially PHC. In the future, more research is needed to validate our results with a larger sample size and combined with in vivo and in vitro experiments.

To our knowledge, this is the first study to describe the differences in microbial composition and metabolites in PHC and PBTC. Further studies regarding the functions of the abovementioned microbiota and metabolites are warranted, as the results may reveal the different mechanisms underlying the occurrence and development of PHC and PBTC and provide a basis for future treatments.

Yiqing Zhu: Data curation; formal analysis; investigation; project administration; supervision; validation; visualization; writing – original draft. Xiao Liang: Investigation; methodology; project administration; supervision; validation; visualization; writing – original draft. Guoming Zhang: Methodology; project administration; software; visualization. Feng Li: Data curation; investigation; resources. Jianwei Xu: Data curation; funding acquisition; resources. Ruiguang Ma: Conceptualization; data curation. Xinyu Chen: Supervision; validation. Miaomiao Ma: Conceptualization; methodology. Yifan Wang: Investigation; project administration. Changxu Chen: Data curation; formal analysis. Haoyun Tang: Investigation; resources. Lixiang Li: Resources; software; supervision; validation; visualization; writing – review and editing. Zhen Li: Conceptualization; data curation; formal analysis; funding acquisition; investigation; methodology; project administration; writing – review and editing.


## Supporting information


## DATA AVAILABILITY STATEMENT

The data supporting the conclusions of this article are available from the corresponding authors, Z.L. and LX.L. upon reasonable request.