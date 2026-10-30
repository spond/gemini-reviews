# FEXP_ANON_044

## Abstract

Recent studies have indicated that the lung microbiome may contribute to the development and progression of lung cancer, although the precise mechanisms remain to be fully elucidated. This study sought to delineate the microbial composition within lung cancer tissues and identify potential microbial risk factors. Tissue samples were collected from patients newly diagnosed with pulmonary opacities, and metagenomic next-generation sequencing was employed to analyze these samples. Tissue samples were collected from 130 patients with pulmonary opacities, categorized into lung cancer (50 cases), pulmonary infection (53 cases), and non-infectious pulmonary diseases (27 cases). The non-infectious group served as the primary control. The diversity of the lung microbiome in lung cancer tissues was found to be comparable to that observed in non-infectious benign pulmonary conditions. Specific phyla and genera exhibited increased abundance in lung cancer tissues. Additionally, correlations were established between certain microorganisms and clinical characteristics associated with lung cancer. Multivariate binary logistic regression analysis revealed that age and Shewanella were independent risk factors for lung cancer development. This study suggests that the composition of the lung microbiome differs significantly between individuals with lung cancer and those with benign pulmonary conditions, with certain microbes such as Shewanella potentially serving as risk factors for lung cancer progression.

The online version contains supplementary material available at [REDACTED].

Keywords: Lung cancer, Microbiome, Metagenomic next generation sequencing (mNGS), Binary logistic regression

Subject terms: Cancer, Oncology


## Introduction

Cancer remains a leading global cause of mortality, influenced by genetic, environmental, and microbial factors. Emerging evidence highlights microbiota roles in carcinogenesis across malignancies 1 – 3 . Lung cancer has the second highest incidence and the highest mortality among all malignancies 4 . The lung tissue was previously considered to be sterile environment, while it was recognized that there were abundant and diverse microorganisms according to high-throughput sequencing technology, even in the healthy human lungs 5 . In addition, accumulating evidence has also suggested that there a significant differences in the pulmonary microenvironment among different pulmonary disease, such as asthma, chronic obstructive pulmonary disease (COPD), idiopathic pulmonary fibrosis (IPF) and lung cancer 6 – 9 .

Moreover, it has been reported that the carcinogenesis of many kinds of tumors were closely related to specific microorganisms, such as Helicobacter pylori and gastric cancer, Human Papilloma virus ( HPV) and cervical cancer, Epstein-Barr virus ( EBV) and nasopharyngeal cancer, Hepatitis B Virus ( HBV) , Hepatitis C Virus (HCV) and liver cancer 10 . Recently, whether microorganism is a key factor for the lung carcinogenesis is beginning to be explored 11 . Liang HY and Pallis AG et al. demonstrated that Mycobacterium tuberculosis ( TB ) was a risk factor for lung cancer 12 , 13 . While, Laroumagne et al. identified Haemophilus influenzae , Enterobacter spp. and Escherichia coli as colonizing organism in lung cancer tissue by analyzing 216 bronchoscopic samples 14 . Several studies have reported the characteristics of the microbiome in bronchoalveolar lavage fluid (BALF) of patients with lung cancer comparing with benign pulmonary diseases 9 , 15 .

However, previous studies have mostly used sputum and BALF samples, which were inevitably contaminated with potential microorganisms of mouth and upper respiratory tract. Furthermore, the small sample size in previous studies resulted in poor consistency between different studies. In addition, microbial detection techniques used in previous studies, such as traditional culture or 16s RNA sequencing, are less sensitive and accurate than metagenomic next generation sequencing (mNGS) 16 . Therefore, percutaneous lung biopsy specimens from 130 patients (including lung cancer, non-pulmonary infection and pulmonary infection) were tested for microbiome by mNGS to further explore the relationship between microbiome and lung cancer.


## Methods


## Study design and sample collection

In total, 130 patients were included in this study. The inclusion criteria of this study were as follows: (a) Patients were hospitalized in the Department of Pulmonary and Critical Care Medicine of Huashan Hospital from January 2018 to August 2021 due to lung shadow of unknown causes; (b) Blood test, tracheoscopy and other examinations were still unable to make a definitive diagnosis; (c) CT-guided percutaneous lung puncture was performed. Two or three pieces of lung tissue obtained by CT-guided percutaneous lung puncture were immediately placed in formalin and sterile tubes for pathological examination and mNGS testing, respectively 17 . Patients were stratified into three diagnostic groups: lung cancer, pulmonary infections (bacterial/fungal/viral), and non-infectious pulmonary diseases (e.g., organizing pneumonia, connective tissue disease-associated interstitial lung disease). The non-infectious group served as the primary control for comparative microbiome analysis. Baseline clinical characteristics such as gender, age, smoking history, blood tests, tumor staging, genetic testing and expression levels of PD-L1 and Ki-67 were recorded.

The study protocol was approved by the Ethics Committee of Huashan Hospital, Fudan University (KY2016−369). All research activities were conducted in accordance with relevant ethical guidelines and regulations, including the Declaration of Helsinki. Informed consent was obtained in writing from all participants.


## Sample processing and DNA extraction

Lung biopsy tissue was collected from patients, and 450µL lung tissue homogenate were added with 11.5 µL of 1.0% saponin (final concentration was 0.025%). After fully vortexed for 15s, lung tissue homogenate was incubated at room temperature for 5 min, then added with 75µL of host removal reaction MIX (BGI Biotech, Wuhan, China) and fully vortexed for 15s, and warm bathed at 37℃ for 10 min. After centrifuged at 18,000 g for 5 min, 450µL of supernatant was carefully aspirated and discarded, and about 70–80µL of liquid remained at the bottom. After added with 800µL of PBS to the tube, the mixture was fully blown or mixed by vortex shock. After centrifugation at 18,000 g for 5 min, 800 µl of supernatant was carefully aspirated and discarded. About 70–80µL of liquid remained at the bottom. 370 µl LTE-buffer (BGI Biotech, Wuhan, China) was added to the tube, mixed with shaking, 7.2µL Lyticase (RT410-TA, TIANGEN BIOTECH, Beijing, China) was added for enzyme wall breaking reaction, and then 250µL 0.5 mm glass beads (BGI Biotech, Wuhan, China) were added for physical wall breaking. After mixing and shaking, 300µL of sample was taken for later use.


## DNA library construction

DNA was extracted according to the instructions of the TIANMicrobe Magnetic Bead Method Pathogenic Microorganism DNA/ Retrieval Kit (NG550-01, TIANGEN BIOTECH, Beijing, China) as recommended by the manufacturer. The extracted nucleic acid was segmented by enzyme digestion, terminal repair, splicing and PCR reaction to construct the library. Agilent 2100 Bioanalyzer (Agilent Technologies, USA) was used to normalize the fragment size of the library to about 300 bp. Qubit dsDNA HS Assay Kit (ThermoFisher Scientific, MA, USA) was used to control the concentration of DNA libraries, and the constructed libraries were pooled according to the concentration after examination. DNB nanospheres were then generated by rolling ring replication (RCA). The prepared DNB nanospheres were loaded into the sequencing chip and sequenced using BGISEQ-50/MGISEQ-2000 (MGI, Shenzhen, China).


## Data analysis

Data analysis was performed following the procedure outlined in the study by Zhan D (2023) 18 . Fastp software was used to filter low-quality bases and joints from sequencing data 19 . Hisat2 (version 2.2.1) with default parameters was mapped to the reference genome of the human genome GRCh38 and the sequences mapped to the human genome were deleted 20 . A custom database was built using Refseq data and the filtered sequences were analyzed and species identified using Kraken2 software 21 .

Non-normally distributed continuous variables are described by interquartiles. Counting data is described in terms of quantities and percentages (n, %). In addition, the Wilcoxon rank sum test was used to evaluate the significance of the difference between the two groups. The Kruskal-Wallis test was used to assess the differences between the three groups. Shannon index for microbial α diversity and Bray-Curtis difference for microbial β diversity were calculated using the “vegan” package in R (v4.2.2), and Principal Coordinate Analysis (PCA) plots were drawn using the factoextra package. The risk factors of lung cancer were analyzed by univariate and then multivariate binary logistic regression analysis. Moreover, spearman correlation analysis was performed to evaluate the relationship between tumor markers and microbial enrichment in lung cancer tissue.


## Code availability

Upon reasonable request and contingent upon approval, the authors are willing to provide the original code utilized for processing and analyzing the data presented in this article. Researchers interested in accessing the code should reach out to the corresponding author.


## Results


## Baseline clinical characteristics and diagnosis of patients with lung shadow

Totally 130 patients were recruited in this study, including 50 patients (38.5%) pathologically diagnosed lung cancer and 80 patients (61.5%) diagnosed with benign pulmonary diseases, which is composed of 53 cases (40.8%) of pulmonary infections and 27 cases (20.8%) of non-pulmonary infection diseases (Fig. S1 A). The demographic and clinical characteristics of patients in the non-infectious pulmonary disease group ( N = 27), pulmonary infectious group ( N = 53) and lung cancer group ( N = 50) were shown in Table 1 and S1 . In the pulmonary infection group, bacterial infections were the most common organism (40, 75.4%), followed by fungal infections (11, 20.8%) and viral infections (2, 3.8%) (Fig. S1 B). Among the top three non-infectious pulmonary diseases, there were 8 cases (29.6%) of organizing pneumonia, 7 cases (25.9%) of Granulomatosis with Polyangiitis (GPA) and 5 cases (18.5%) of connective tissue disease-associated interstitial lung disease (CTD-ILD) (Fig. S1 C). Adenocarcinoma (32, 64.0%) and squamous cell carcinoma (11, 22.0%) predominated in the lung cancer group, which also included adeno-squamous cell carcinoma, unclassified non-small cell lung cancer and small cell lung cancer (SCLC) (Fig. S1 D). Further analysis of lung cancer patients found that 40 patients (80.0%) were performance status 0–1 (Fig. S1 E), 37 patients (74.0%) were TNM stage IV (Fig. S1 F). Other clinical features of lung cancer patients, such as T stage, N stage, M stage, EGFR gene detection, PD-L1 and Ki-67 expression levels, were shown in Fig. S2A-G. In summary, the diagnosis of patients with lung shadow was mainly composed of lung infectious disease, lung cancer and non-infectious pulmonary disease.


### Table 1: Baseline clinical characteristics of the three enrolled groups.

|  | non-lung cancer | lung cancer |
| non-Pulmonary infections | Pulmonary infections |
| Age, years (IQR) | 56(33–62) | 52(36–61) | 66(55–72) |
| Gender, n(%) |
| Male | 12 (44.4) | 35 (66.1) | 38 (76.0) |
| Female | 15 (55.6) | 18 (33.9) | 12 (24.0) |
| Smoking, n(%) |
| Yes | 9 (33.3) | 16 (30.2) | 26 (52.0) |
| No | 18 (66.7) | 37 (69.8) | 24 (48.0) |
| Complications, n(%) |
| COPD | 0 | 0 | 7 (14.0) |
| Asthma | 0 | 0 | 1 (2.0) |
| Bronchiectasis | 0 | 0 | 1 (2.0) |
| Pulmonary fibrosis | 0 | 4 (7.5) | 1 (2.0) |
| Diabetes mellitus | 4 (14.8) | 7 (13.2) | 4 (8.0) |
| Hypertention | 4 (14.8) | 10 (18.9) | 16 (32.0) |
| Coronory heart disease | 1 (3.7) | 2 (3.8) | 3 (6.0) |
| Autoimmune disease | 8 (29.6) | 3 (5.7) | 2 (4.0) |
| Cerebrovascular disease | 0 | 1 (1.9) | 2 (4.0) |
| Hepatic injury | 0 | 5 (9.4) | 1 (2.0) |
| Cancers (excluding lung cancer) | 2 (7.4) | 1 (1.9) | 0 |

## Alpha and Beta diversity between lung cancer and non-lung cancer groups

Alpha diversity refers to the microbiota diversity within a particular environment or ecosystem and is primarily used to reflect species richness and evenness, as well as sequencing depth. Beta diversity is an important component of biodiversity, which is mainly used to study the difference of species community structure among different samples or treatment groups. The difference between Beta diversity and Alpha diversity is that Alpha diversity is only used to describe the species diversity of a single sample, whereas Beta diversity is used to compare the diversity of different samples (ecosystems). Beta diversity and alpha diversity together constitute the overall diversity or biological heterogeneity of a given environmental community. At genus levels, richness and evenness of pulmonary microorganisms in lung cancer had no significant difference compared to those in non-pulmonary infection and pulmonary infection by analyzing observed species (p = 0.732), chao (p = 0.830), ace (p = 0.934), shannan’s diversity (p = 0.439), simpson’ diversity ( p = 284) and Good’s coverage ( p = 0.955) (Fig. 1 A-F). Although there was a significant difference in beta diversity between pulmonary infections and non-pulmonary infections or lung cancer groups (Fig. 1 G), the diversity between non-pulmonary infections and lung cancer was similar according to PCA analysis (Fig. 1 H).


> **Fig. 1:** Alpha and beta diversity of the lung microbiota among the three groups. ( A–F ) Observed species ( A ), chao ( B ), ace ( C ), shannon’s diversity ( D ), simpson’ diversity ( E ) and Good’s coverage ( F ) were used to evaluate the community richness and diversity among the three groups. Wilcoxun rank sum test. ns > 0.5; ( G ) Difference in microbial composition among the three groups based on Bray-Curtis metrics was calculated by the Wilcoxun rank sum test. ns > 0.5, *** p < 0.001, **** p < 0.0001; ( H ) Principle coordinate analysis of Bray-Curtis metrics.


## Atlas of Microbiome characteristics of lung cancer different from non-pulmonary infection

According to the relative abundance of microbiota in the percutaneous lung puncture tissues of the three groups, classification and relative difference analysis were carried out on the phylum, class, order, family, genus and species levels respectively. In addition, the taxonomic profiles of the lung microbiota composition were presented at bacterial, fungal and non-fungal eukaryotic levels respectively.

At the bacterial phylum level, Proteobacteria , Firmicutes , Actinobacteria and Bacteroidetes were the most common organisms in all the three groups (Fig. 2 A). The relative abundance of Proteobacteria, Fimicutes and Bacteroidetes increased significantly in lung cancers compared with non-pulmonary infections (Fig. 2 B). Additionally, at the bacterial order level, Bacillales , Alteromonadales , Burkholderiales , Enterobacterales , Pseudomonadales accounted for the top five organisms among the three groups (Fig. 2 C). The relative abundance of Bacillales , Bacteroidales , Burkholderiales , Enterobacterales , Xanthomonadales , Pseudomonasales , Pasteurellales , Aquificales and Micrococcales increased significantly in lung cancers compared with non-pulmonary infections (Fig. 2 D). At the bacterial genus level, the top five bacteria with the relative higher proportion were Shewanella , Staphylococcus , Bacillus , Acinetobacter and Mycobacterium among the three groups (Fig. 2 E). While, Acidibacillus and Enterobacter were more enriched in lung cancer group than those in non-pulmonary infections group (Fig. 2 F).


> **Fig. 2:** Taxonomic profiles of the pulmonary bacteria among the three groups. ( A )The relative abundance of the pulmonary bacteria in each CT-guided percutaneous lung biopsy at the phylum level; ( B ) Significantly different bacterial phyla were shown by box plot. Kruskal-Wallis tes. ns > 0.5, * p < 0.05; ( C ) The relative abundance of the pulmonary bacteria in each CT-guided percutaneous lung biopsy at the order level; ( D ) Significantly different bacterial orders were shown by box plot. Kruskal-Wallis test. ns > 0.5, * p < 0.05; ( E ) The relative abundance of the pulmonary bacteria in each CT-guided percutaneous lung biopsy at the genus level; ( F ) Significantly different bacterial genera were shown by box plot. Kruskal-Wallis tes. ns > 0.5, ** p < 0.01.

At the fungal phylum level, Ascomycota , Basidiomycota and Mucoromycota were the core categories among the three groups (Fig. S3A). No significant differences were found at the fungal phylum level between the lung cancer group and the non-pulmonary infection group. Furthermore, at the fungal genus level, the relative proportion of Aspergillus , Amorphotheca , Rhizophagus , Malassezia and Phycomyces ranked the top five among the three groups (Fig. S3B). Dothidotthia , Jamina , Microsporum , Purpureocillium , Venustampulla , Trichomonascaceae and Rhodotorula were enriched significantly in lung cancers compared with non-pulmonary infections (Fig. S3C).

Moreover, the taxonomic profiles of pulmonary non-fungal eukaryotes at phylum, order and genus levels among the three groups were shown in Fig. S4A and S4B. However, there were no statistical differences between lung cancer group and non-pulmonary infection group.


## Correlation between microorganisms and clinical characteristics of lung cancer patients

In the lung cancer group, the correlation between microorganisms and 10 clinical characteristics of lung cancer was analyzed at genus level. Acidibacillus , Enterobacter , Escherichia , Keratinibaculum , Rhizobium and Vibrio were enriched in male, while Bacteroides , Helicobacter , Mycoplasma , Polaribacter were abundant in female (Fig. 3 A). The relative abundance of Azoarcus was higher in patients > 65 years old than that of younger patients (Fig. 3 B). In addition, the relative abundance of Acidibacillus , Keratinibaculum and Komagataeibacter was significantly increased in smoking patients compared with non-smoking patients (Fig. 3 C). Furthermore, only Herbaspirillum was enriched in squamous cell carcinoma compared with adenocarcinoma (Fig. 3 D). The abundance of Massilia , Shewanellla and Staphylococcus was enriched in lung cancer tissues with tumor size ≤ 3 cm compared with those in lung cancer tissues larger than 5 cm (Fig. 3 E). Moreover, the abundance of Cloacibacterium and Halomonas in lung tissues of patients with TNM stage I-III was significantly more than that of patients with TNM stage IV (Fig. 3 F).


> **Fig. 3:** Correlation between microorganisms and clinical characteristics in patients with lung cancer at the generic level. ( A )Significantly differences in microbial enrichment in lung cancer between men and women at the generic level. Wilcoxun rank sum test. *<0.05, ** p < 0.01, **** p < 0.0001; ( B ) Significantly differences in microbial enrichment in lung cancer between patients aged > 65 years and those aged ≤ 65 years at the generic level. Wilcoxun rank sum test. *<0.05; ( C ) Significantly differences in microbial enrichment in lung cancer between smoking and non-smoking lung cancer patients at the generic level. Wilcoxun rank sum test. *<0.05; ( D ) Significantly differences in microbial enrichment in lung cancer between adenocarcinoma and squamous cell carcinoma at the generic level. Wilcoxun rank sum test. *<0.05; ( E ) Significantly differences in microbial enrichment in lung cancer between lung cancers of different sizes at the generic level. Kruskal-Wallis test. ns > 0.5, *<0.05, ** p < 0.01; ( F ) Significantly differences in microbial enrichment in lung cancer between different stages of lung cancer at the generic level. Wilcoxun rank sum test. *<0.05; ( G ) Significantly differences in microbial enrichment in lung cancer between Ki-67 > 10% and Ki-67 ≤ 10% lung cancer tissues at the generic level. Wilcoxun rank sum test. *<0.05; ( H ) Significantly differences in microbial enrichment in lung cancer between PD-L1 < 1% and PD-L1 ≥ 1% lung cancer tissues at the generic level. Wilcoxun rank sum test. *<0.05; ( I ) Significantly differences in microbial enrichment in lung cancer between EGFR-negative and different EGFR-mutated (L858R, 19del and others) lung cancer tissues at the generic level. Kruskal-Wallis test. ns > 0.5, *<0.05, ** p < 0.01, *** p < 0.001; ( J ) Heat map of correlation between tumor markers and microbial enrichment in lung cancer tissue at the generic level. Only microorganisms with a correlation coefficient greater than 0.3 are shown. Spearman correlation. ** p < 0.01.

At the molecular pathological levels, the abundance of Hydrogenobacter and Moraxella was significantly increased in lung cancer tissues with Ki-67 expression positive proportion>10%, while the abundance of Algibacter , Enterococcus and Acytostelium was significantly enriched in lung cancer tissues with Ki-67 ≤ 10% (Fig. 3 G). In addition, Butyrivibrio , Caloramator , Chlamydia , Clostridioides , Mucilaginibacter , Phyllobacterium and Vanderwaltozyma were enriched in lung cancer tissues with PD-L1 ≥ 1%, while Aquabacterium , Phreatobacter and Malassezia were enriched in PD-L1 negative lung cancer tissues (Fig. 3 H). Compared with EGFR drive mutation-negative lung cancer tissues, only the abundance of Burkholderia in lung cancer tissues with L858R mutation was significantly decreased, while Abiotrophia , Acidibacillus , Bacillus , Campylobacter , Clostridiodes , Clostridium , Cronobacter , Enterococcus , Keratinibaculum , Listeria , Mycobacterium , Pyramidobacter , Vibrio , Amorphotheca , Candida , Exophiala , Toxoplasma and Trypanosoma were significantly reduced in 19del lung tissues (Fig. 3 I).

In addition to the above, CA-199 expression level had significant positive correlation with the enrichment of Cutibacterium and Cloacibacterium in lung cancer tissues (Fig. 3 J). However, NSE expression level was positively correlated with the enrichment of Escherichia , Burkholderia , Klebsiella , Stenotrophomonas , Cupriavidus , Xanthomonas , Massilia , Variovorax , Lysobacter , Bordetella , Cloacibacterium , Mycolicibacterium and Achromobacter in lung cancer tissues (Fig. 3 J).


## Potential microbial risk factors for lung cancer

130 patients were divided into lung cancer group and non-lung cancer group for binary logistic regression assay. In order to investigate whether microorganisms are potential risk factors for lung cancer, binary logistic regression was performed at the microbial level of phylum, class, order, family and genus in addition to the basic clinical characteristics. Male gender, older age (> 65 years) and smoking history increased the risk of lung cancer according to univariate binary logistic regression at different microbial level analysis (Fig. 4 A, C and E). Howerver, only older age was an independent risk factor according to multivariate binary logistic regression (Fig. 4 B, D and F). Microorganism risk factor analysis found that patients with high relative abundances of Firmicutes and Bacillariophyta had a significant risk of lung cancer development at the phylum level (Fig. 4 A). While, only Bacillariophyta was an independent risk factor of lung cancer according to multivariate binary logistic regression (Fig. 4 B). Furthermore, at the order level, Xylariales , Onygenales , Hypocreales , Eurotiales , Salinisphaerales , Legionellales and Alteromonadales might increase the risks for lung cancer according to univariate binary logistic regression (Fig. 4 C). However, multivariate logistic regression showed that only Alteromonadales might be independent risk factor for lung cancer (Fig. 4 D). Similarly, univariate binary logistic regression showed that Theileria , Heterostelium , Pyricularia , Naumovozyma , Melampsora , Dothidotthia , Botrytis , Aspergillus , Shewanella , Salinisphaera , Pseudomonas , Prevotella and Legionella were all risk factors for lung cancer at the generic level (Fig. 4 E). However, only Shewanella was found to be an independent risk factor for lung cancer according to multivariate binary logistic regression (Fig. 4 F). It was interesting that Aspergillus was found as a protective factor, but without statistical significance (Fig. 4 F). This might be due to the limited sample size and deserved further study.


> **Fig. 4:** Potential microbial risk factors for lung cancer at different level of microbial categories. ( A and B ) Potential microbial risk factors for lung cancer was analyzed by univariate and multivariate binary logistic regression at the phylum level; ( C and D ) Potential microbial risk factors for lung cancer was analyzed by univariate and multivariate binary logistic regression at the order level; ( E and F ) Potential microbial risk factors for lung cancer was analyzed by univariate and multivariate binary logistic regression at the genus level.


## Discussion

Microorganisms colonized in human body could shift the metabolism, growth pattern and function of neoplastic cells 22 . However, only a few microorganisms have been identified directly initiate carcinogenesis. In this study, the microbiome profile of lung cancer and benign pulmonary disease tissues acquired by CT-guided percutaneous lung puncture was characterized and the relationship between microbiome and lung cancer was further analyzed by binary logistic regression.

The results of microbial diversity between lung cancer and benign pulmonary disease varied between studies. Chen C et al. reported bronchoalveolar lavage fluid microbial beta diversity was significantly different between lung cancer and benign lung disease, while alpha diversity was similar 15 . However, Zhou Y et al. Found that diversity and species richness were similar between cancerous tissue and paracancerous tissue 23 . This is consistent with our study that microbial alpha diversity is similar between lung cancer and non-infectious pulmonary disease. Pulmonary infection itself contains a large number of pathogenic microorganisms which may explain the significant difference in microbial beta diversity between pulmonary infection and non-infectious pulmonary diseases or lung cancer.

Proteobacteria and Firmicutes were reported as the most abundant phylum categories of BALF or lung puncture tissue in lung cancer 15 . The relative abundance of Proteobacteria and Firmicutes in lung cancer tissue was higher than that in benign pulmonary disease in our research, which was consistent with previous studies 9 , 15 . At the generic level, previous reports have shown that Veillonella , Megasphaera , c: TM7-3 , Capnocytophaga , Sediminibacterium , Gemmiger , Blautia and Oscillospira were enriched in lung cancer 9 , 15 . In this study, Acidibacillus , Enterobacter , Dothidotthia , Jamina , Purpureocillium , Venustampulla , Trichomonascaceae and Rhodotorula were more abundant in lung cancer compared with non-infectious benign pulmonary disease. These results indicate that differences existed in microbial community between lung cancer and benign pulmonary disease, which may be potential new targets for lung cancer prevention and/or therapy. As for the differences in the abundance of microorganisms between lung cancer and benign pulmonary diseases in different studies may be caused by different inclusion criteria, sampling methods, microbial detection methods, and sample size.

The relationship between the gut microbiota and various diseases has been intensively studied, and therapeutic approaches targeting the gut microbiota have begun to be applied to clinical research 24 – 28 . However, previous studies have mostly been limited to the association between microbes and lung cancer. This study further explored the potential microbial risk factors for lung cancer at different microorganism levels through binary logistic regression. Univariate logistic regression results showed that elder, male gender and smoking history are risk factors for lung cancer, which is consistent with previous studies. However, in multivariate logistic regression, only older age (> 65 year) was an independent risk factor for lung cancer among the three risk factors mentioned above. This may be caused by small sample size and adjusted by microorganisms. Furthermore, it was found that Alteromonadales and Shewanella were independent risk factors for lung cancer at the order and generic levels, respectively. Shewanella is the type genus and, at the present, the sole genus of the family Shewanellaceae ascribed to the order Alteromonadales . Shewanella is gramnegative, indole-negative, and gelatinase-, sucrose-, and maltose-positive. This genus is positive for catalase and can reduce nitrate (NO3 − ) to nitrite (NO2 − ). Members of this genus are aerobic or facultative anaerobic, and some species can ferment D-glucose and N-acetylglucosamine to produce acid, usually without gas. Most of the Shewanella strains also present H 2 S-producing, urea-, arginine hydrolase-, lysine decarboxylase negative phenotypes 29 . Chen et al.. reported that Shewanella was significantly over-abundant in prostate cancer compared with benign prostate tissue 30 . Additionally, Aspergillus was an risk factor for lung cancer at genus levels in this study by univariate logistic regression. However, in the multivarious logistic regression study, Aspergillus was found as an protective factor, but without statistical significance due to the limited sample size. These results from our study highlight microbes, such as Aspergillus and Shewanellla , as an interesting candidate for further investigation of the association with lung cancer.

This is the first study to explore the relationship between microbes and lung cancer using second-generation sequencing to detect microorganisms in pulmonary puncture tissue with a relatively large sample size. Percutaneous pulmonary puncture minimizes contamination from oral and upper respiratory tract microorganisms. However, there are also some limitations in this study. First, relatively small sample size of this study may contribute to heterogeneity of the final results. Furthermore, although a wide range of microorganisms were detected by second-generation sequencing, species could not be accurately identified and classified due to the limitation of sequencing depth, and RNA microorganisms were not detected in this study. Moreover, antibiotic use history was not systematically recorded, which may influence microbial composition. In addition, all participants included in this study were Chinese, which may limit the generalizability of this findings. Above all, this is a single-center cross-sectional study, which needs to be further verified by multi-center prospective studies with larger sample sizes in the future.


## Conclusions

This study identifies distinct microbial profiles in lung cancer tissues, characterized by an increased abundance of Proteobacteria and Firmicutes. Multivariate analysis reveals Shewanella as an independent risk factor, while alpha diversity remains comparable between lung cancer and non-infectious pulmonary diseases. These findings underscore the potential role of specific microbes in the process of lung carcinogenesis.


## Electronic supplementary material

Below is the link to the electronic supplementary material.

Supplementary Material 1

Sincerely thanks to Lijuan He (from BGI Genomics) for her support in the data analysis.


## Abbreviations

Metagenomic next generation sequencing

Chronic obstructive pulmonary disease

Idiopathic pulmonary fibrosis

Human Papilloma virus

Mycobacterium tuberculosis

Bronchoalveolar lavage fluid

Principal Coordinate Analysis

Granulomatosis with Polyangiitis

Connective tissue disease-associated interstitial lung disease

Small cell lung cancer

Ruzetuoheti Yiminniyaze, Youzhi Zhang, and Ning Zhu conducted this study, analyzed the data, and drafted the manuscript. Xiujuan Zhang, Daibing Zhou, Jingwen Xia, Liang Dong, and Yuanyuan Zhang contributed to the collection of pulmonary biopsy specimens. Chengwei Li, Jing Wang, Gulinuer Wumaier, and Shuanghui Li assisted in presenting the results and designing the typographic layout. Yuhai Zhang and Shengqing Li designed this study and supervised the manuscript preparation. All authors have read and approved the final version of the manuscript.

This study was funded by National Natural Science Foundation of China (No. 82270058) and Key Special Project (No. 82241028), Shanghai Year 2022 Science and Technology Innovation Action Plan Medical Innovation Research Special Project (No. 22Y11900600).


## Data availability

The datasets generated and analyzed during the current research are not publicly available due to stringent data protection regulations. However, they can be obtained from the corresponding author upon reasonable request.


## Ethical approval

This study was approved by the Institutional Review Board of Huashan Hospital, affiliated with Fudan University (Permit Number: KY2016-369). All patients enrolled in the study signed voluntary informed consent forms. All research data were anonymously analyzed.


## Contributor Information

Yuhai Zhang, Email: [EMAIL_REDACTED].

Shengqing Li, Email: [EMAIL_REDACTED].


## Associated Data


## Supplementary Materials

Supplementary Material 1


## Data Availability Statement

The datasets generated and analyzed during the current research are not publicly available due to stringent data protection regulations. However, they can be obtained from the corresponding author upon reasonable request.