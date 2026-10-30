# De-Identified Manuscript `ANON_115`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

The gut microbiota is a fundamental component of human health and has been increasingly implicated in the etiology of neurological disorders. Neurotransmitters, acting as key mediators of gut-brain communication, are closely associated with both the progression and therapeutic modulation of brain diseases. Despite significant advancements in microbiome research, the complex interplay between gut microbiota and neurological disorders remains poorly understood, and a comprehensive resource integrating these associations is lacking. To bridge this gap, we developed the Brain Disease Gut Microbiota Database (BGMDB), a rigorously curated repository documenting experimentally validated relationships between gut microbiota and brain diseases. BGMDB encompasses 1419 associations involving 609 gut microbiota taxa and 43 brain disorders, along with 184 tripartite interactions linking brain diseases, neurotransmitters, and microbiota across six neurotransmitter systems. Additionally, BGMDB integrates genetic data from the gutMGene database, allowing users to explore microbiota-mediated genetic associations with brain disease pathology and neuroanatomical alterations. A user-friendly interface enables researchers to navigate relevant information through graphical query tools, comprehensive browsing functionalities, and data retrieval options. Our BGMDB provides an unparalleled resource for advancing mechanistic insights into gut-brain interactions, facilitating novel microbiota-targeted therapeutic strategies for neurological disorders. BGMDB is freely available at: http://bgmdb.online/bgmdb .

Keywords: Gut microbiota, Brain disease, Database, Neurotransmitters


## Graphical Abstract


## 1. Introduction

The gut microbiota, a diverse and dynamic community of microorganisms inhabiting the human gastrointestinal tract, plays a crucial role in numerous physiological processes, including digestion, immune modulation, and neurotransmitter synthesis [1] , [2] . Estimates suggest that the gut microbiota comprises approximately 38 trillion microbial cells, surpassing the number of human cells in the body [3] . Recent studies have emphasized its critical influence on the gut-brain axis, a bidirectional communication system linking the gut and central nervous system via neural, endocrine, immune, and metabolic pathways [4] , [5] . The integrity of this axis is essential for maintaining neurological homeostasis, and disruptions in gut microbiota composition—commonly referred to as dysbiosis—have been increasingly associated with a spectrum of neurological and psychiatric disorders, including Alzheimer’s disease, Parkinson’s disease, multiple sclerosis, schizophrenia, and autism spectrum disorders [6] , [7] .

Mechanistically, the gut microbiota influences brain function through multiple interconnected pathways. First, it synthesizes and regulates the metabolism of neurotransmitters such as serotonin, dopamine, gamma-aminobutyric acid (GABA), acetylcholine, norepinephrine, and histamine, which are crucial for synaptic signaling and cognitive functions [8] . Additionally, microbial metabolites such as short-chain fatty acids (SCFAs), lipopolysaccharides (LPS), and secondary bile acids have profound effects on neuroinflammation, blood-brain barrier permeability, and neurodegenerative processes. In particular, SCFAs, including butyrate, propionate, and acetate, have been shown to promote neuroprotection by modulating microglial activation and histone deacetylase (HDAC) inhibition, thereby reducing neuroinflammation.

Emerging evidence from human and animal model studies suggests that gut microbiota dysbiosis can contribute to cognitive decline, motor dysfunction, and mood disorders through both direct and indirect mechanisms [9] . For instance, Helicobacter pylori infection has been linked to an increased risk of Parkinson’s disease, while Bacteroides fragilis dysregulation has been implicated in autism spectrum disorders. Furthermore, alterations in Lactobacillus and Bifidobacterium populations have been reported in patients with major depressive disorder (MDD) and generalized anxiety disorder (GAD), highlighting the relevance of microbiota-based interventions in mental health treatment.

With the advent of high-throughput sequencing technologies, shotgun metagenomics, and metabolomic profiling, researchers now have unprecedented access to microbiota-related data. Despite this progress, current databases such as Disbiome [10] , MicrobiomeDB [11] , and MASI [12] primarily focus on general disease-microbiota associations and lack a dedicated emphasis on brain disorders and their link to neurotransmitters and genetic regulation. In response to this limitation, we developed BGMDB, the first comprehensive database integrating gut microbiota, brain diseases, neurotransmitters, and genetic interactions in a structured and accessible manner. BGMDB aims to advance the field of neuro-gastroenterology by providing researchers with curated experimental data, facilitating hypothesis-driven research, and enabling the identification of novel microbiota-targeted therapeutic strategies for neurological disorders.


## 2. Methods


### 2.1. Data collection and standardization

To construct a high-quality dataset, we systematically extracted data from PubMed [13] , Web of Science, MicroPhenoDB [14] , Peryton [15] , and gutMDisorder [16] . Literature searches were conducted using keywords such as “microbiota,” “microbiome,” “microbe,” “bacteria,” “gut,” “intestinal,” “brain disease,” “brain disorder,” “gut microbiota,” “gut flora,” “intestinal bacteria,” “neurotransmitter,” “serotonin,” “dopamine,” “norepinephrine,” “GABA,” “histamine,” and “acetylcholine.” Utilize MeSH terms and their synonyms to expand the search scope, incorporating standard terminology, aliases and abbreviations to construct a precise and high-recall search strategy, minimizing information loss due to terminological variations. This process yielded 1445 research articles, from which we manually extracted interaction records. To enhance the accuracy and reliability of the dataset, all extracted associations underwent rigorous manual verification through an extensive review of the literature.

During data integration, we implemented standardization and quality control strategies to enhance consistency and reliability. By normalizing synonyms and abbreviations, we incorporated MeSH terms, the NCBI classification system, and databases such as gutMDisorder to ensure standardized terminology. A rule-based mapping approach was used to unify terms across studies (e.g., “gut flora” and “intestinal microbiota”). For common abbreviations (e.g., AD for Alzheimer’s disease), manual verification was performed to ensure accuracy. Additionally, we curated microbe-disease associations, assessing data reliability based on experimental methods and sample size reported in the original literature. To further improve credibility, we analyzed consistency across multiple studies and excluded highly uncertain or conflicting results.

Additionally, we proposed an indicator called Association Strength ( A S e ij ) to quantify the confidence level of associations, positing that reliable associations are shaped by: 1) the number of corroborating publications, 2) journal impact factor, 3) availability of experimental raw data, and 4) database inclusion of the association. The Association Strength can be calculated using the following formula:



| A S e ij = w 1 SN e ij + w 2 SF e ij + w 3 SRD e ij + w 4 SD e ij | (1) |
| --- | --- |


where e ij represents the relationship between disease i and microbe j ; SN e ij , SF e ij , SRD e ij and SD e ij denote publication number, journal impact factor, the state of availability for experimental raw data and the situation of inclusion in database, respectively. Log 10 and Sigmoid transformation are carried out on SN eij and SF eij carried out on each entry. For SF e ij , we consider the cumulative impact factor of all supporting publications, SRD e ij and SD e ij are both modeled as binary variables. The weight factor values are adopted as w 1 = 0.5 , w 2 = 0.3 , w 3 = 0.1 and w 4 = 0.1 , respectively.( Table 1 )


#### Table 1.

Microbial species AND Brain disease data in the database.



|  | Classes | Amount | Total |
| --- | --- | --- | --- |
| Types of brain diseases | Mental Disorders | 17 | 43 |
| Nervous System Diseases | 26 |
| Microbial Species | Kingdom | 2 | 609 |
| Phylum | 18 |
| Class | 16 |
| Order | 25 |
| Family | 71 |
| Genus | 206 |
| Species | 122 |
| Other | 149 |
| Neurotransmitter | Cholines | 1 | 6 |
| Monoamines | 4 |
| Other | 1 |
| Encephalic Region | Brodmann Areas | 8 | 8 |


We further integrated neurotransmitter-related associations from the MiKG4MD database [17] ，MMiKG [18] and gene-specific data from the gutMGene [19] database. Standardized nomenclature was applied using Medical Subject Headings (MeSH) for diseases and the NCBI Taxonomy Database for microbiota.


## 3. Database contents and usage


### 3.1. Database contents

Database Structure and Content BGMDB provides a structured repository comprising 1419 experimentally validated associations involving 609 gut microbiota taxa and 43 human brain diseases. Each brain disease entity within the database encompasses various fields, including disease name, related references, experimental data, and gut microbiota associations. Similarly, the microbiota entity comprises microbiota name, classification information, references, and related disease information. The related references provide details such as title, author, journal, and abstract, while the experimental data encompass experiment type, design, sample size, and more. Furthermore, we have gathered and organized information on neurotransmitters that interact with specific brain diseases and gut microbiota. Additionally, gene information of gut microbiota, including gene name, gene ID, and sequence information, has been recorded. Users can conveniently access the desired information by entering keywords or selecting specific categories of disease, microbiota, or neurotransmitter. Moreover, relevant data can be downloaded from the “Download” interface in CSV format, enabling users to conduct in-depth analysis ( Fig. 1 ).


#### Fig. 1.


> **Figure/Table Caption:** BGMDB Function Display and Search. The search function allows users to quickly retrieve and view pertinent information, while the data interface presents a detailed display. Users can click on individual data points to open a pop-up window with further details.


### 3.2. Encephalic region and disease-microbe network

The concept of the encephalic region (ER) is derived from medical research on the functional divisions of the brain, integrating insights from modern scientific psychology [20] . A widely accepted method for brain segmentation is the Brodmann Areas classification, which delineates the brain into 52 distinct regions. As the central regulator of human behavior, the brain relies on coordinated interactions among multiple regions. Prior research by Zhao et al. [21] has demonstrated that structural abnormalities in the brain can contribute to the development of various neurological disorders and that a potential genetic link may exist between brain diseases and region-specific neuroanatomical changes. Building upon this hypothesis, we investigated the associations between brain diseases and specific encephalic regions, while also exploring their interactions with intestinal microbiota. Within the brain region interface, users can select specific brain areas to retrieve comprehensive information on corresponding diseases, or alternatively, select a disease to view its associated brain regions. However, due to data limitations, the current database includes documented associations between eight encephalic regions and 12 brain diseases ( Fig. 2 A). To further elucidate the interplay between brain diseases and gut microbiota, we developed the Brain Disease-Intestinal Microbe Relationship Network. This feature enables users to explore disease-microbe associations by selecting specific diseases or microbial taxa of interest. The relationships are presented through interactive network visualizations and tabular formats, providing clear and intuitive representations of the data ( Fig. 2 B).


#### Fig. 2.


> **Figure/Table Caption:** The encephalic region and network function schematic diagram.


### 3.3. Database design

The BGMDB web application follows a Model-View-Controller (MVC) architecture, developed using Spring Boot and deployed on an Apache Tomcat server. Data retrieval, search functionalities, and visualization features are implemented using Ajax API technology, enabling dynamic and responsive interactions. The browsing and search interface is designed using Java Server Pages (JSP) to enhance user accessibility. This architectural framework supports efficient data management and provides researchers with a comprehensive and interactive resource for exploring gut microbiota–brain disease associations ( Fig. 3 ).


#### Fig. 3.


> **Figure/Table Caption:** BGMDB construction process. To construct the BGMDB, a comprehensive collection of data was meticulously gathered from a diverse range of carefully selected literature sources. This data was then organized, modified, and subsequently used to create data tables and databases specifically tailored for the BGMDB.


## 4. Results


### 4.1. Web interface

The platform offers a user-friendly web interface that allows users to search, browse, download, and analyze the associations between gut microbiota and brain disorders. Furthermore, the website includes specialized search applications for specific microbiota or diseases, enabling users to access prioritized relationships. Users can also download the prioritized associations of microbiota and diseases as CSV files for further analysis. The hierarchies of microbiota and diseases are individually presented on the “Data” webpage. To ensure robust performance, we conducted testing of the BGMDB website across various web browsers, including Mozilla Firefox, Google Chrome, and Internet Explorer ( Fig. 4 ).


#### Fig. 4.


> **Figure/Table Caption:** BGMDB function page.


### 4.2. Usage notes

Recent studies have highlighted a significant relationship between gut microbiota and brain diseases such as Anxiety [22] , Depression [23] , and Parkinson's disease. Researchers leverage data from various public databases to delve into this correlation. BGMDB stands out as an online knowledge-based database offering the most up-to-date insights into the connection between gut microbiota and brain disease. By clicking on the name of a specific brain disease or gut microbiota, users can access detailed information, including the MeSH ID and abbreviation of the brain disease, along with related experiments, samples, associated gut microbiota, and relevant references.

Researchers utilize the data within BGMDB to scrutinize the alterations in gut microbiota communities among patients with brain diseases and investigate the link between these changes and disease progression. To strengthen comprehension of BGMDB's utilization, we present application cases.


### 4.3. Applications and use cases


#### 4.3.1. Identifying homologous brain disorders

BGMDB facilitates the identification of homologous brain diseases that share similar gut microbiota profiles. For instance, researchers can navigate through the “Data” and “Retrieval” interfaces to discover that Alzheimer's disease is classified under Central Nervous System Diseases. Similarly, Tourette Syndrome [24] , Attention Deficit Disorder with Hyperactivity [25] , and Autistic Disorder [26] , among others, are considered parallel brain disorders. Furthermore, Neurotic Anorexia, Anxiety Disorder, Bipolar Disorder, and others fall within the same category as Central Nervous System Diseases ( Fig. 5 ).


> **Figure/Table Caption:** Mining homologous brain diseases.


#### 4.3.2. Investigating microbial symbiosis in brain diseases

Understanding microbial co-occurrence patterns can inform microbiota-targeted therapies. BGMDB enables researchers to explore microbial hierarchies, revealing taxa such as Coriobacteriaceae and Staphylococcus that are consistently associated with neurodegenerative diseases. For example, the researcher can explore the gut microbiota correlated with Alzheimer's disease and its taxonomic levels, such as Coriobacteriaceae [27] at the family level, Staphylococcus [28] at the genus level, and others. Furthermore, researchers may note that both stroke disease patients and Alzheimer’s disease patients harbor Pseudomonas data readily accessible through the “Data-Download” section ( Fig. 6 ).


> **Figure/Table Caption:** Mining symbiotic microorganisms.


#### 4.3.3. Exploring neurotransmitter-microbiota interactions

Neurotransmitters play a pivotal role in gut-brain signaling. BGMDB provides insights into the impact of microbial taxa on neurotransmitter dynamics. For example, researchers can click on the Superior Parietal region, and BGMDB will display associated brain diseases such as Anxiety and Depressive disorders along with the corresponding gut microbiota on the right side ( Fig. 7 ).


> **Figure/Table Caption:** Mining brain regions and neurotransmitters.

Neurotransmitters play a crucial role as intermediate messengers within the brain-gut axis, attracting significant interest from researchers due to their involvement in the interplay between microbes and brain disorders, which is pivotal for diagnosis and treatment. In the “Network” section of BGMDB, researchers can explore the relationship network between brain diseases, gut microbiota, and neurotransmitters. This allows them to understand, for instance, how variations in Lactobacillus plantarum bacteria in Alzheimer's disease patients are influenced by Acetylcholine [29] and how variations in Escherichia bacteria in Alzheimer's disease patients are modulated by Serotonin [30] .

With the information and insights gained from these findings, researchers can utilize the data from BGMDB to pinpoint potential targets and drug candidates. Comparative analysis within BGMDB enables exploration of differences in gut microbiota between patients with various brain disorders and healthy individuals as well as potential synergistic or antagonistic effects. BGMDB proves to be an indispensable resource for researchers, offering novel perspectives and methodologies in the field of bioinformatics.


### 4.4. Comparison with existing databases

While databases such as Disbiome, gutMDisorder, and MASI offer valuable insights into disease-microbiota interactions, they lack a dedicated focus on neurological disorders. Unlike these resources, BGMDB provides a comprehensive dataset that specifically integrates brain disease-microbiota associations, neurotransmitter interactions, and genetic data. Additionally, BGMDB features advanced query functionalities tailored for neurological research, making it a uniquely valuable tool for studying the gut-brain axis and its implications for neurodegenerative and psychiatric diseases.


## 5. Discussion and future work

The gut microbiota plays a pivotal role in human health and disease development, influencing a wide range of conditions, including intestinal disorders, neurodegenerative diseases, psychiatric disorders, and even oncological pathologies [31] . The intricate interactions between gut microbiota and brain function have become a focal point of neuroscientific and microbiome research, as evidence continues to mount supporting a microbial contribution to neurological disorders. While traditional perspectives on brain diseases have largely attributed their pathogenesis to genetic and environmental factors, emerging research suggests that microbial dysbiosis is a critical, yet often overlooked, contributor to neuroinflammation, neurotransmitter imbalances, and neurodegeneration.

Advancements in high-throughput sequencing technologies, metagenomics, and metabolomics have greatly enhanced our ability to profile the gut microbiota and its metabolic products, leading to an increasing number of studies exploring gut-brain interactions. As a result, thousands of experimental findings detailing associations between gut microbiota and brain diseases have been published. However, the lack of a centralized, curated repository that systematically organizes and integrates this knowledge has hindered the translation of these findings into meaningful clinical applications. To address this gap, BGMDB was developed as a comprehensive platform that consolidates experimentally validated gut microbiota-brain disease interactions, providing a structured, searchable, and interactive resource for researchers in neuroscience, microbiology, and computational biology.

The establishment of BGMDB represents a significant advancement in the study of microbiota-brain interactions. By cataloging 1419 associations spanning 609 microbiota taxa and 43 brain diseases, the database enables researchers to identify key microbial players, evaluate their potential roles in neurological disorders, and develop hypotheses for microbiota-targeted interventions. Beyond simply aggregating data, BGMDB applies network analyses to visualize microbiota-disease relationships, integrating neurotransmitter interactions and genetic associations to offer deeper insights into disease mechanisms.

To ensure continued relevance and accuracy, we propose several key strategies for the ongoing development and enhancement of BGMDB. Firstly, automated text-mining and natural language processing (NLP) tools (such as Entrezpy [32] ) will be employed to systematically extract brain disease-microbiota associations from an expanding corpus of scientific literature. By utilizing AI-driven algorithms, we aim to enhance the efficiency and accuracy of data collection while minimizing human error. Secondly, a continuous manual curation process will be implemented to cross-check automated extractions and maintain data integrity. This hybrid approach will ensure that BGMDB remains an authoritative and up-to-date resource for microbiota-brain disease associations. Thirdly, the database will be updated quarterly to integrate the latest research findings, ensuring that users have access to the most recent discoveries in the field.

In addition to these enhancements, we recognize the potential of graph database technologies to facilitate the exploration of complex microbiota-disease networks [33] . Recent studies have demonstrated the utility of graph-based models in elucidating multi-layered biological interactions, including those involving host-microbiome dynamics. The implementation of graph databases in BGMDB would enable researchers to perform sophisticated network-based queries, visualize multi-omic relationships, and identify previously unrecognized disease-microbiota associations.

Furthermore, machine learning and deep learning approaches will be leveraged to uncover hidden patterns in gut microbiota-disease interactions. By applying predictive modeling techniques, BGMDB could facilitate the identification of novel therapeutic targets, improve disease risk stratification, and guide precision medicine initiatives [34] , [35] , [36] , [37] . These advancements could revolutionize the field of neurogastroenterology by providing data-driven insights into microbiota-based diagnostics and interventions.

As the field progresses, BGMDB will expand its scope beyond the current 43 documented brain diseases to include additional neurodevelopmental, neurovascular, and psychiatric conditions. Moreover, multi-omics data integration—incorporating transcriptomics, proteomics, and metabolomics—will allow for a more comprehensive understanding of gut-brain interactions at the molecular level. Such expansions will further enhance the utility of BGMDB as a platform for systems-level investigations into the gut-brain axis [38] .

Ultimately, BGMDB serves as a crucial foundation for advancing research into the gut microbiota’s role in neurological disorders. By providing a structured and interactive repository of microbiota-brain disease associations, we aim to bridge the gap between microbiome research and clinical applications, fostering the development of microbiota-targeted therapeutics for neurological and psychiatric conditions. Future efforts will focus on refining database functionalities, expanding its dataset, and incorporating AI-powered analytical tools [39] , [40] to maintain its status as an indispensable resource for the scientific community.


## CRediT authorship contribution statement

Yu Juehua: Writing – review & editing, Conceptualization. Dong Huachen: Validation, Software. Li Lin: Software, Methodology, Data curation. He Qisheng: Visualization, Validation, Investigation. Zhao Pengyang: Methodology, Data curation. Shi Kai: Writing – original draft, Investigation, Funding acquisition, Formal analysis, Data curation, Conceptualization. Liu Qiaohui: Visualization, Validation. Wang Yanjun: Visualization, Validation. Wu Zhengxia: Methodology, Formal analysis.


## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.


## Acknowledgements

The authors thank the anonymous referees for suggestions that helped improve the paper substantially. Research supported by the National Natural Science Foundation of China (62162019), Scientific Research and Technology Development Program of Guangxi (ZY22096025), the startup Grant in Guilin University of Technology, and Innovation Project of Guangxi Graduate Education (YCSW2024357). The authors declare that they have no conflicts of interest.
