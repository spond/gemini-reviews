# De-Identified Manuscript `ANON_77`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract


### Background

Parkinson’s disease (PD) is affecting 5 million people worldwide, but the response mechanisms of the striatum are still unclear. Therefore, identification of gene expression alterations in the striatum will greatly assist the development of novel therapy strategies.


### Methods

We performed a comprehensive gene expression analysis in 15 PD patients and 15 normal controls to identify differentially expressed genes (DEGs) using the expression profile GSE20291 from Gene Expression Omnibus (GEO). Gene Ontology (GO) analysis and Kyoto Encyclopedia of Gene and Genome (KEGG) pathway enrichment analysis were used to define functions and pathways altered in PD. Protein-protein interaction network was constructed to find out the modules with close interactions.


### Results

Total715 DEGs including 268 up-regulated and 447 down-regulated genes were obtained. GO functional enrichment analysis indicated that the genes related with neurons function and cell morphogenesis might be changed upon PD. KEGG pathway enrichment analysis showed that most of the genes were enriched in the nodes of Gap junction, calcium signaling pathway, phosphatidylinositol signaling system, long-term potentiation, Alzheimer’s disease and GnRH signaling pathway. Protein-protein interaction network and module analysis suggested that some apoptosis related genes, such as PRKCA, CDC42 and BCL2 may play critical roles in striatal neurons growth.


### Conclusion

Intrinsic striatal tyrosine hydroxylase interneurons growth may be promoted by changes in several genes expression and thus reduce the functional excitatory synapses.

Keywords: Parkinson’s disease, Neuron, Calcium signal, Gap junction, Protein-protein interaction, Module


## Background

Parkinson’s disease (PD) is a progressive neurodegenerative disorder affecting approximately 1% of the population over 60 years in industrialized countries [ 1 ]. PD is characterized pathologically with dopaminergic neurons degeneration in the substantia nigra with concomitant reduction of dopamine levels in the striatum, especially putamen, which lead to motor impairments, including tremor, rigidity and bradykinesia [ 2 , 3 ] and non-motor symptoms including pain [ 4 ]. Treatments with carbidopa, levodopa, dopamine agonists, monoamine oxidase type B inhibitors, catechol-O-methyltransferase inhibitors or amantadine are effective to control symptoms in the early stages of PD disease but eventually fail or are associated with unacceptable side effects [ 5 , 6 ]. Thus, novel diagnosis and treatment strategies are urgently needed to be developed [ 7 ].

Recent studies have indicated several compensatory mechanisms for dopamine loss in the striatum [ 8 ]. For example, depletion of dopaminergic nigrostriatal output leads to enhanced D2 receptors expression level in the striatum, which promotes the inhibitory effect of the rest dopamine in the striatum on the activity of the indirect pathway and delay manifestations of PD motor symptoms [ 9 ]. Down-regulation of dopamine transporter causes decreased dopamine reuptake [ 10 ]. Activation of peroxisome proliferator–activated receptor γ coactivator-1α (PGC-1α) may result in increased expression of nuclear-encoded subunits of the mitochondrial respiratory chain in the putamen of PD patients with dyskinesias [ 11 ] and block of the dopaminergic neuron loss caused by mutant α-synuclein or the pesticide rotenone [ 12 ]. High expression level of glial cell line-derived neurotrophic factor (GDNF) is also observed in the putamen of PD patients to promote intrinsic striatal TH interneuronsas growth [ 13 ]. Infusion or viral vector-mediated delivery of GDNF into the striatum has been associated with significant clinical benefits [ 14 ]. However, the compensatory or response mechanisms in the putamen of PD patients are not very clear and underlying therapeutic targets are still needed to be investigated.

Microarrays which allow to rapidly scanning for candidate genes and biomarkers can interrogate in parallel expression levels of thousands of genes in tissue samples from patients with PD [ 15 ]. In the present study, we aimed to analyze the expression data from putamen samples of PD patients and normal control and tried to offer new insights into the gene changes in the putamen and potential treatment targets for PD.


## Methods


### Source of data

We extracted the GSE20291 microarray expression profile from Gene Expression Omnibus (GEO, http://www.ncbi.nlm.nih.gov/geo/ ) database based on the Affymetrix Human Genome U133A Array. A total of 30 samples of putamen tissue were available, including 15 of PD patients samples approved by the ethic committee of the Fourth Affiliated Hospital of China Medical University and 15 pathologically normal controls samples, and there has no significant differences in the sample ages, gender, postmortem intervals and PH between the control group and the PD group [ 16 ].

The probe-level data in CEL files were converted into expression measures and background correction and quartile data normalization were performed by the robust multiarray average (RMA) algorithm to obtain the expression profile data [ 17 ]. After deleting the Entrez Genes with the same probe and averaging the values for the entrez genes with multiple probes, we obtained 12688 genes of the expression profile for the 35 samples.


### Identification of differentially expressed genes (DEGs)

Because the DEGs have more relationship with the development of disease, Student’s t-test was used to identify the DEGs between PD patients and normal controls. All the genes with p-value < 0.05 were selected as DEGs for further study.


### Functional enrichment analysis

Functional enrichment analysis was performed using the online tool DAVID (Database for Annotation, Visualization, and Integrated Discovery) [ 18 ]. GO (gene ontology) terms and KEGG (Kyoto Encyclopedia of Genes and Genomes) pathways were selected with an adjusted p-value less than 0.1 calculated by the Expression Analysis Systemic Explorer (EASE) test which was implemented in the DAVID tool [ 19 ]. Benjamini-Hochberg method was used to further adjust the p-value [ 20 ].


### Protein–protein interaction (PPI) network construction

The overlapping clusters were detected by CFinder [ 21 ] based on the Clique Percolation Method (CPM) [ 22 ]. For the CPM, a protein complex is defined as a union with all k-cliques can be reached via a series of adjacent k-cliques (two k-cliques share exactly k - 1 vertices are adjacent). Results of CFinder are highly correlated to the value of the parameter k. Larger values of k correspond to smaller subgraphs of higher density.

PPI data in Human Protein Reference Database (HPRD) [ 23 ] are experimentally derived and manually extracted from the literature by expert biologists who read, interpret and analyze the published data.

In the study, we downloaded PPI data from HPRD on the website http://www.hprd.org/download . The DEGs were mapped into the PPI network to find out the molecular mechanism of the PD from protein-protein interactions. A biological graph visualization tool Cytoscape software was used to construct the PPI networks [ 24 ]. In the PPI networks, proteins/genes were represented with nodes, while the interaction derived from experimental repositories and computational prediction methods between any two proteins/genes therein was represented using an edge.


## Results


### DEGs analysis

We used the Student’s t-test to analyze the microarray dataset GSE20291 from GEO database in order to identify the DEGs between PD patients and normal controls. As a result, 715 genes were screened between PD patients and normal controls with p-value < 0.05, including 268 up-regulated genes and 447 down-regulated genes.


### GO functional enrichment and KEGG pathway enrichment analysis

GO functional enrichment analysis indicated that 715 DEGs were significantly enriched in 225 GO terms and the top 15 functional nodes were selected in which 5 functional nodes were related with neuron function, including neuron development, neuron differentiation, neuron projection development, neuron projection morphogenesis, and cell morphogenesis involved in neuron differentiation (Table 1 ). Furthermore, other 4 functional nodes having a close relationship with neurons were selected when using p-value < 0.1 as the threshold, including neuron projection regeneration, central nervous system neuron differentiation, central nervous system neuron development and neuron recognition. Thus, we suggest that these abnormal functions of these 9 functional nodes may be responsible for putamen response for the PD. Subsequently, we integrated all the genes in the above 9 functional nodes related with neurons together, containing a cluster of 40 DEGs, 22 down-regulated genes and 18 up-regulated genes.


#### Table 1.

Results of functional enrichment analysis for DEGs (top 15)



| Term | Name | Count | P-value | Adjusted p-value |
| --- | --- | --- | --- | --- |
| GO:0032990 | Cell part morphogenesis | 33 | 9.58E-09 | 2.64E-05 |
| GO:0048812 | Neuron projection morphogenesis | 28 | 1.04E-07 | 1.44E-04 |
| GO:0048858 | Cell projection morphogenesis | 30 | 1.58E-07 | 1.45E-04 |
| GO:0032989 | Cellular component morphogenesis | 40 | 1.93E-07 | 1.33E-04 |
| GO:0048667 | Cell morphogenesis involved in neuron differentiation | 27 | 2.62E-07 | 1.45E-04 |
| GO:0031175 | Neuron projection development | 30 | 4.04E-07 | 1.86E-04 |
| GO:0007409 | Axonogenesis | 25 | 7.62E-07 | 3.00E-04 |
| GO:0000902 | Cell morphogenesis | 36 | 8.12E-07 | 2.80E-04 |
| GO:0000904 | Cell morphogenesis involved in differentiation | 28 | 1.61E-06 | 4.93E-04 |
| GO:0030030 | Cell projection organization | 36 | 1.76E-06 | 4.85E-04 |
| GO:0048666 | Neuron development | 34 | 2.10E-06 | 5.27E-04 |
| GO:0030182 | Neuron differentiation | 40 | 2.32E-06 | 5.34E-04 |
| GO:0008285 | Negative regulation of cell proliferation | 33 | 2.07E-05 | 0.004395 |
| GO:0046907 | Intracellular transport | 49 | 3.65E-05 | 0.00717 |
| GO:0031099 | Regeneration | 12 | 8.25E-05 | 0.015071 |


Count: the number of differentially expressed gene; P-value was obtained by expression analysis systemic explorer test; P-value was adjusted by Benjamini-Hochberg method.

The other important functional nodes in Table 1 were related with cell morphogenesis, including cell morphogenesis, cellular component morphogenesis, cell projection morphogenesis and cell projection organization. Our results showed that the nodes related with neurons had a father-and-son relationship with those nodes related with cell morphogenesis.

To functionally classify these DEGs in the interaction network, we performed pathway enrichment analysis by mapping these genes to KEGG database. The top 6 pathways were chosen according to their statistical significance (Table 2 ). The enriched pathways included Gap junction, Calcium signaling pathway, Phosphatidylinositol signaling system, long-term potentiation, Alzheimer’s disease and GnRH signaling pathway.


#### Table 2.

Results of KEGG pathway enrichment analysis for DEGs



| Term | Name | Count | P-value | Adjusted p-value |
| --- | --- | --- | --- | --- |
| hsa04540 | Gap junction | 14 | 2.47E-04 | 0.038054 |
| hsa04020 | Calcium signaling pathway | 20 | 5.87E-04 | 0.045063 |
| hsa04070 | Phosphatidylinositol signaling system | 11 | 0.002342 | 0.059518 |
| hsa04720 | Long-term potentiation | 11 | 0.001217 | 0.061717 |
| hsa05010 | Alzheimer’s disease | 18 | 0.001671 | 0.063516 |
| hsa04912 | GnRH signaling pathway | 13 | 0.002101 | 0.063907 |


Count: the number of differentially expressed gene; P-value was obtained by expression analysis systemic explorer test; P-value was adjusted by Benjamini-Hochberg method.


### PPI network

In order to mine more important data in the nodes related with neurons, we constructed the PPI network to identify more important DEGs and biological modules in the development of PD. We downloaded protein interaction data from HPRD. First, we mapped the genes of these proteins to Entrez Gene and got 34,180 binary non-redundant human PPI in HPRD. The number of genes annotated with at least one interaction was 9,518. Then we overlapped the genes in Affymetrix Human Genome U133A Array chip platform to the 9,518 genes and got a network with 7,670 genes and 31,041 interactions. Next, the 40 genes enriched in the 9 neurons functional nodes were annotated in the network. We got 735 direct interactions with the 40 genes. Cytoscape software was used to display the network graph of 40 genes in the PPI (Figure 1 ).


#### Figure 1.


> **Figure/Table Caption:** PPI interactions network of 40 differentially expressed genes related with neurons function. Nodes and links represent human proteins and protein interactions. Nodes represent the encoding genes of proteins. Red color indicates up-regulated genes annotated in the PPI network. Blue color indicates the down-regulated genes annotated in the PPI network. Gray color indicates the genes which have interactions with DEGs.

In the network, PRKCA, RXRA, CDC42, BCL2, CEBPB, NOTCH1, GNAO1, SNAP25, PAX6 and VCAN were located in the central position with degrees of 166, 81, 70, 69, 48, 40, 32, 22, 21 and 19 respectively. PRKCA had the highest degree among the 10 genes. The degree of a gene is the number of its neighborhood genes in PPI network. One gene with high degree, termed a hub gene, plays a key role in maintaining the interactions between this gene and its neighborhood genes. The changes of the genes in the central position of network have more effects compared with those with smaller degree.

In order to reveal the mechanism of PD, Clique Percolation Method in cfinder software was employed to find out the modules with close relationship in the PPIs network. Under the conditions of K = 3, we got 5 modules. Figure 2 shows one module containing the most nodes (Figure 2 ). In the module, 3 DEGs, including PRKCA (up-regulated), BCL2 (up-regulated) and CDC42 (down-regulated) were involved in the module. PRKCA with the highest degree had an interaction with all the other genes in the module.


#### Figure 2.


> **Figure/Table Caption:** One module in the PPI network. Nodes indicate encoding genes of proteins; red color indicates up-regulated genes annotated in the network; and blue color indicates down-regulated genes annotated in the network.


## Discussion

In the present study, we analyzed the expression changes in the putamen of PD patients. A total of 715 genes were differentially expressed in the putamen of PD patients, including 268 up-regulated and 447 down-regulated. GO functional enrichment analysis for these DEGs showed that the genes related with neuron function and cell morphogenesis were altered as the disease progressed. Some studies have shown that a significant (30–50%) reduction in spine density in both the caudate nucleus and putamen of severely dopamine-depleted striata [ 25 ]. OPHN1(oligophrenin-1), a Rho-GTPase activating protein that is required for dendritic spine morphogenesis was up-regulated in our study as a compensation mechanism [ 26 ]. Lacking the transcription factor Pax6 has been associated with defects of tyrosine hydroxylase (TH)-immunoreactive neurons in the brains [ 27 ]. In this study, Pax6 was also up-regulated and thus intrinsic striatal TH interneurons might be increased. Intrinsic striatal TH interneurons, positioned within the striatum itself, are able to compensatorily produce dopamine [ 28 , 29 ]. Besides, the nodes of neuron function have father-and-son relationship with the nodes of cell morphogenesis. This indicates that in the progress of PD, neurons dysfunction may affect their morphogenesis.

The KEGG pathway enrichment result showed that these DEGs were significantly enriched in Gap junction, Calcium signaling pathway, Phosphatidylinositol signaling system, long-term potentiation, Alzheimer’s disease and GnRH signaling pathway. Gap junctions (GJs) are found to be expressed in most cell types in the nervous system, such as neuronal stem cells, neurons, astrocytes, oligodendrocytes, blood brain barrier cells and microglia/macrophages under inflammatory conditions. Some studies have shown that phosphorylated gap junction protein connexin 43 is selectively enhanced in the basal ganglia regions, which contain dopamine neurons or their terminal areas (striatum) [ 30 , 31 ]. PD is ameliorated by Gastrodin by downregulating connexin 43 [ 32 ].

Calcium signaling pathway and phosphatidylinositol signaling system have been demonstrated to be related with gap junctions. Ca 2+ is central to a wide variety of cellular processes ranging from the regulation of enzyme activity and gene expression to programmed cell death. When controlled properly, Ca 2+ fluxes through the plasma membrane and between intracellular compartments are responsible for the fundamental functions of neurons, such as synaptic transmission and plasticity, neurite outgrowth and synaptogenesis, [ 33 ]. Studies about patients, animals and cells have provided large amounts of data which could confirm that the alterations in Ca 2+ regulation are involved in the stroke and chronic neurodegenerative disorders [ 34 ]. Calcium-calmodulin-dependent kinase II (CaMKII), a Ser/Thr kinase, is highly expressed in the striatum and down-regulation of CaMKII results in the reduction of functional excitatory synapses and enhancement of intrinsic excitability [ 35 ]. As expected, CaMKII was upregulated in this study. Gap junctions can mediate Ca 2+ signals to neighbour cells [ 36 ]. Connexin 36 deficiency leads to reduced CaMKII levels in the striatum and motor behavioral changes [ 37 ].

Our PPI network analysis showed that 10 DEGs (PRKCA, RXRA, CDC42, BCL2, CEBPB, NOTCH1, GNAO1, SNAP25, PAX6 and VCAN) were hub nodes. Further module analysis suggested that PRKCA, CDC42 and BCL2 might be more important in the same module with the same apoptosis or cell cycle function. It has been reported that PRKCA can be selectively involved in neurite outgrowth and cytoskeletal changes of filamentous actin and b-tubulin of GT1 hypothalamic neuronal cells via ERK signal pathway [ 38 ]. PRKCA mediates Bcl2 phosphorylation and accounts for the increased cell survival observed following chemotherapy [ 39 ]. Inhibition of PRKCA leads to a decrease in Bcl-xL gene expression and consequent induction of apoptosis [ 40 ].

Cdc42, a Rho-related member of the Ras superfamily, acts as a GTP-binding protein/molecular switch to control a diversity of cellular processes. Earlier biochemical studies in neuronal cells have shown that Cdc42, along with Rac1, is a positive regulator, whereas RhoA functions as a negative regulator in neurite initiation, axon growth and branching, and spine formation [ 41 ]. In particular, Cdc42 plays a key role in oligodendrocyte differentiation and in neuronal polarity/axon outgrowth and neuronal migration. In our analysis, Cdc42 is downregulated [ 42 - 44 ]. These results have suggested that lower Cdc42 may promote phagocytosis of degenerating dopaminergic neurons in vivo in PD patients [ 42 ].

BCL2 is a major regulator of neural plasticity and cellular resilience. Recent findings have indicated that interaction between Bcl-2 and inositol 1,4,5-trisphosphate (IP3) receptor Ca 2+ channels on the endoplasmic reticulum could inhibitIP3-mediated Ca 2+ signals to induce neuron apoptosis and enhance Ca 2+ signals to support neuron cell survival [ 45 , 46 ]. The concentrations of Bcl-2 in the nigrostriatal dopaminergic regions are significantly higher in parkinsonian patients than those in controls [ 47 ], which was also confirmed in our study.


## Conclusion

In conclusion, our results suggest that in response to dopamine deprived in the striatum of PD patients, expressions of several genes are changed (OPHN1, Pax6, connexin 43, CaMKII, PRKCA, CDC42 and BCL2) and these genes may play important roles in promoting intrinsic striatal TH interneurons growth and inhibit its apoptosis. However, further experiments are still needed to confirm the results of our study.


## Abbreviations

PD: Parkinson’s disease; DEGs: Differentially expressed genes; GEO: Gene expression omnibus; GO: Gene ontology; KEGG: Kyoto Encyclopedia of gene and genome; PGC-1α: Peroxisome proliferator–activated receptor γ coactivator-1α; GDNF: Glial cell line-derived neurotrophic factor; RMA: Robust multiarray average; EASE: Expression analysis systemic explorer; HPRD: Human protein reference database.


## Competing interests

The authors declared that they have no competing interest.


## Authors’ contributions

LG and HG participated in the design of this study, and they both performed the statistical analysis. HZ carried out the study, together with LG, collected important background information, and drafted the manuscript. YX conceived of this study, and participated in the design and helped to draft the manuscript. All authors read and approved the final manuscript.


## Pre-publication history

The pre-publication history for this paper can be accessed here:

http://www.biomedcentral.com/1471-2377/13/181/prepub


## Contributor Information

Lianbo Gao, Email: [EMAIL_REDACTED].

Honghua Gao, Email: [EMAIL_REDACTED].

Huan Zhou, Email: [EMAIL_REDACTED].

Yanyuan Xu, Email: [EMAIL_REDACTED].


## Acknowledgements

We thank all members of Department of Neurology for their advices and assistance.
