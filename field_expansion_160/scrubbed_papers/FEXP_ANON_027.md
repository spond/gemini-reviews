# FEXP_ANON_027

## Abstract

In order to distinguish the traditional Chinese medicine Bupleurum falcatum and its adulterants effectively and develop a better understanding of the factors affecting synonymous codon usage, codon usage patterns of chloroplast genome, we determine the complete chloroplast (cp) genome of B. falcatum and clarify the main factors that influence codon usage patterns of 78 genes in B. falcatum chloroplast genome.

The total genomic DNA of fresh leaves from a single individual of B. falcatum was extracted with EASYspin plus Total DNA Isolation Kit and 2 μg genome DNA was sequenced using Illumina Hiseq 2500 Sequencing Platform. The cp genome of B. falcatum was reconstructed with MITObim v1.8 and annotated in the program CPGAVAS2 with default parameters. Python script and Codon W were used to calculate the codon usage bias parameters.

The full length of B. falcatum cp genome was 155 851 bp, 132 different genes were annotated in this cp genome containing 80 protein-coding genes, 30 tRNA genes, and four rRNA genes. The codon usage models tended to use A/T-ending codons. The neutrality plot, ENC plot, PR2-Bias plot and correspondence analysis showed that both compositional constraint under selection and mutation could affect the codon usage models in B. falcatum cp genome. Furthermore, three optimal codons were identified and most of these three optimal codons ended with G/U.

The cp genome of B. falcatum has been characterized and the codon usage bias in B. falcatum cp genome is influenced by natural selection, mutation pressure and nucleotide composition. The results will provide much more barcode information for species discrimination and lay a foundation for future research on codon optimization of exogenous genes, genetic engineering and molecular evolution in B. falcatum.


## Introduction

Chloroplast, also called cp or ct, is generally composed of a closed double-stranded ring DNA. As the cpDNA sequence is high homology, the replication rate of cpDNA is higher than that of nuclear DNA. The cp genome is unified in a conserved quadripartite structure. Ordinarily, the cpDNA consists of a large single copy (LSC), a small single copy (SSC), and a set of mutually inverted repeat sequences (IRa and IRb) ( Gray, 1989 ). The structure and the gene order of the cp genome is highly conserved. Thus, the chloroplast genome information can be used to identify taxonomical position, genetic diversity analysis, DNA barcoding and population biology ( Hollingsworth et al., 2011 , Powell et al., 1995 , Ma et al., 2021 ).

The genetic information in DNA is transmitted in the form of triplet codons in the process of transferring from mRNA to protein. The genetic code is redundant, some amino acids are coded by more than one codon. Codons encoding the same amino acid are defined as synonymous codons ( Plotkin & Kudla, 2011 ). The using frequency of synonymous codons probability is different during the process of protein synthesis, which commonly referred to as “codon usage bias”. Some main factors, such as mutational pressure, natural selection, and random genetic drift, play major roles in shaping codon usage bias ( Long et al., 2018 , Wang et al., 2018 ). For example, as the sequence information is sufficient for further analysis, the codon usage in Arabidopsis thaliana (L.) Heynh. and Oryza sativa L. has been investigated extensively. As the studies revealed, the codon usage patterns between A. thaliana and O. sativa were different, but the main factors that affected the codon usage bias in the two plants were all the same including the GC composition of genes, the expression level of gene and CDS (Coding DNA sequence) length, etc ( Morton and Wright, 2007 , Liu et al., 2004 ). However, due to the limited available genomic information, the codon usage patterns of other plants have not been fully investigated.

Bupleurum falcatum L. is an important Chinese medicinal plant, which belongs to family Apiaceae and is used throughout East Asia. Traditionally, the dried roots of B. falcatum have been widely used for treating the common cold, fever, hepatitis, inflammation, and also the symptoms of menopausal syndrome, such as hot flashes and depressive mood change ( Yang et al., 2017 ). However, the adulterants of B. falcatum have threatened the clinical medication safety. Whole-plastid-based barcodes have shown great potential in species discrimination. So we decided to determine the complete chloroplast (cp) genome of B. falcatum . Meanwhile codon usage in B. falcatum has not been investigated in any details, it is not clear how and why different genes should vary. By analyzing the codon use bias of B. falcatum cp genome, the expression level of the target gene can be increased via genetically engineering, and the expression of exogenous genes can be more efficient and stable. Moreover, it also has important data reference value in the improvement of B. falcatum varieties.


## Materials and methods


## Plant preparation and DNA isolation

Fresh leaves of a single B. falcatum plant were collected from Anguo Plantation (N38.41391 and E115.32321). A voucher specimen (No. CHAIH-19–0620) was deposited at the herbarium of Hebei University, Baoding, China. EASYspin plus Total DNA Isolation Kit (Aidlab, Beijing, China) was used to isolate the total genomic DNA following the user instructions.


## DNA sequencing, genome assembly and annotation

Genomic DNA (5 μg) was used for performing high-throughput sequencing on the Illumina Hiseq 2500 platform by Benagene Technologies, Inc. (Wuhan, China). In total, 2.0-Gb raw data of 150 bp pair-end reads were obtained, and the CLC Genomics Workbench 9.5.2 (CLC Inc., Rarhus, Denmark) was used to trim the adapter sequences with the default parameters set. We took the B. chinense cp genome ( MN337347 ) ( Zhang, Zhao, Yuan, Chen, & Huang, 2019 ) as a reference sequence to assemble the complete cp genome of B. falcatum with MITObim v 1.8 ( Hahn, Bachmann, & Chevreux, 2013 ). The online program CPGAVAS2 was used to annotate the whole B. falcatum cp genome with the default parameter ( Shi et al., 2019 ). The map of the circular B. falcatum chloroplast genome was drawn through the online tool OGDRAW version 1.3.1 ( Greiner, Lehwark, & Bock, 2019 ). To minimize sampling errors, only CDS sequences that were more than or equal to 100 codons in length had corrected initial and termination codons were hold for further analysis. Finally, 78 genes were left for the downstream codon usage analysis.


## Relative synonymous codon usage

Relative synonymous codon usage (RSCU) value refers to the ratio of the average usage frequency of a codon to the expected unbiased usage frequency ( Cai et al., 2009 ). If RSCU = 1, it indicates that the codons are used with no preference, whereas RSCU > 1 indicates the codon usage is positively high and If RSCU < 1 it indicates that the frequency of the codon usage is relatively low. In the high frequency codon, the codon with the highest RSCU value and the most frequent occurrence is considered to be the optimal codon of the gene ( Sharp & Li, 1986 ).


## ENC‑plot analysis

Effective number of codons (ENC) was used to measure bias of synonymous codon for a certain gene. The range of ENC values is from 20 to 61. When a gene with ENC = 20 means extremely preference and the amino acid encoded by only one codon. When ENC value = 61, it indicates no codon usage preference ( Wright, 1990 ). ENC-plot analysis refers to the decisive factor of codon preference analysis by constructing ENC values with GC3S. ENC standard curve indicates: the gene is located on or near the standard curve, the codon preference of the gene is greatly affected by mutation, while far away from the standard curve, the codon usage pattern is greatly affected by natural selection under the condition of guaranteeing the best use of codons ( Hussain & Rasool, 2017 ).


## Neutrality plot

A neutrality plot (GC12 against GC3) can indicate the effects of mutation pressure and natural selection on codon usage patterns ( Wang, Meng, & Wei, 2018 ). In the neutral map, GC12 indicates the average values of GC1 and GC2 of each gene, which is ordinate, GC3 is horizontal ordinate, if the correlation between GC12 and GC3 variations is close to 1, it indicates that there is no significant difference among the three base positions of the codon, and the codon uses only affected by the mutation pressure; If the correlation coefficient between GC12 and GC3 shows no significant difference, it shows that natural selection is the main determinant of codon usage patterns ( He, Zhang, Xiu, & Xing, 2013 ).


## Software used

All codon usage bias parameters were calculated by Codon W ( Peden, 1999 ) and CUSP of EMBOSS ( https://genopole.toulouse.inra.fr/bioinfo/emboss ). The nucleotide compositions were calculated by Python script ( Zhang et al., 2017 ).


## Statistical analysis

The correlation analysis was carried out using SPSS 20.0 software based on the Spearman’s rank correlation method (with a level of significance of P < 0.05 or P < 0.01).


## Results


## Chloroplast genome structure of B. Falcatum

The cp genome of B. falcatum (GenBank: MT797174 ) was 155 851 bp in length, including a pair of inverted repeats (IR) regions of 26 305 bp, a large single-copy (LSC) region of 85 763 bp and a small single-copy (SSC) region of 17 528 bp. The overall GC content of the chloroplast genome was 37.68%. A total of 132 genes were annotated in the B. falcatum cp genome, including 80 protein-coding genes, 30 tRNAs (25 species) and four rRNAs. The B. falcatum cp genome was rich in Adenine–Thymine (AT) content according to the gene map ( Fig. 1 ). Fig. 1 Gene map of B. falcatum chloroplast genome.


> **Fig. 1:** Gene map of B. falcatum chloroplast genome.

A neighbor-joining phylogenetic tree was reconstructed using the coding sequences of 77 PCGs for a panel of 21 species in Apiaceae with the MEGA X program ( Kumar, Stecher, Li, Knyaz, & Tamura. 2018 ). The phylogenetic tree suggested that B. falcatum and other species of genus Bupleurum formed a monophyletic group and was sister to other groups of Apiaceae ( Fig. 2 ). The complete cp genome information of B. falcatum is significant for Araliaceae species conservation and identification. Fig. 2 Phylogenetic relationships of 20 species within Apiaceae family based on neighbor-joining (NJ) analysis.


> **Fig. 2:** Phylogenetic relationships of 20 species within Apiaceae family based on neighbor-joining (NJ) analysis.


## Nucleotide composition of genes in B. falcatum chloroplast genome

Codon usage pattern can be affected by the genome nucleotide content significantly ( van Hemert & Berkhout, 2016 ), so we analyzed the nucleotide composition of the 78 CDS in B. falcatum chloroplast genome. The overall GC contents and GC contents at the third codon positions of genes were investigated. The GC contents of genes ranged from 30.4% to 50.8% (SD = 3.81%, average = 38.7%), and most were between 35% and 45% ( Fig. 3 ), suggesting that the B. falcatum chloroplast genome is slightly AT-rich rather than GC-poor. The GC1, GC2 and GC3 were 0.468, 0.397 and 0.295, respectively, illustrating that the GC1 was the highest, and the GC3 was minimal. These results indicated that the B. falcatum chloroplast genome favored to use A/U-ending codons. Fig. 3 Distribution of GC contents of reconstructed genes in B. falcatum .


> **Fig. 3:** Distribution of GC contents of reconstructed genes in B. falcatum .

The relationship between the GC12 and the GC3 was analyzed using neutrality plots (GC12 vs GC3). Based on the neutrality analysis, we found that the GC3 values of B. falcatum chloroplast genome exhibited a narrow range (0.21–0.375) and no significant correlation between GC12 and GC3 ( R 2 = 0.0015, P > 0.05; Fig. 4 ), suggesting that the natural selection, rather than mutational pressure, is the main determinant of codon usage in the B. falcatum chloroplast genome. Fig. 4 Neutrality plot (GC12 vs GC3).


> **Fig. 4:** Neutrality plot (GC12 vs GC3).


## ENC plot analysis

To detect the degree of codon usage bias of the coding genes in B. falcatum cp genome, ENC values were calculated. The ENC values ranged from 30.98 to 60 and the average was 48.48, suggesting that these genes possessed low codon usage bias. The ENC versus GC3 plot was drawn to understand the relationship between codon usage bias and nucleotide contents of B. falcatum chloroplast genome. It showed that most points of the coding genes were in a discrete distribution ( Fig. 5 ), although some points were observed to distribute on or very close to the expected curve, pointing that other important factor, such as natural selection and translational selection effect may exist. Fig. 5 Neutrality plot (ENC vs GC3).


> **Fig. 5:** Neutrality plot (ENC vs GC3).

The (ENCexp-ENCobs)/ENCexp values were calculated to distinguish the difference between observed and expected ENC values. The results showed that the (ENCexp-ENCobs)/ENCexp values of most genes were within 0–0.1, indicating that difference between the observed and expected ENC values was very slight ( Fig. 6 ). All the results suggested that although mutation is a very important factor, but it is not the only player involved in the codon usage bias. Fig. 6 Frequency distribution of ENC ratio.


> **Fig. 6:** Frequency distribution of ENC ratio.


## PR2-Bias plot analysis

The PR2 bias plot was carried out to analyze relationship between AT content and GC content ( Fig. 7 ). It could be seen that G and T were used more frequently than C and A in B. falcatum chloroplast genome. The results suggested that other factors (e.g. translational selection) contribute to codon usage bias in addition to mutation. Fig. 7 PR2-Bias plot [A3/ (A3 + T3) vs G3/(C3 + G3)].


> **Fig. 7:** PR2-Bias plot [A3/ (A3 + T3) vs G3/(C3 + G3)].


### Table 1: Correlation analysis of B. falcatum chloroplast genome gene-related parameters.

| Parameters | GC3 | GCall | ENC | CAI | Axis1 |
| GC12 | 0.001 | 0.008 | 0.087 | 0.05* | 0.142** |
| GC3 |  | 0.02 | 0.04 | 0.006 | 0.276 |
| GCall |  |  | 0.075* | 0.043 | 0.016 |
| ENC |  |  |  | 0.028 | 0.003 |
| CAI |  |  |  |  | 0.001 |

## Identification of optimal codons

The average RSCU values of the highly - expressed and lowly - expressed genes were calculated to identify the optimal codons ( Table 2 ). Three optimal codons were identified as significantly more frequently used condons among the highly - expressed genes ( P < 0.01) according to the chi-square test. Two optimal codons ended with a U, and one with a G. These results indicated that codon usage of B. falcatum chloroplast genome is biased to U-ending synonymous codons. Table 2 Optimal codons of B. falcatum chloroplast genome genes based on the RSCU. Amino acid Codon High Low Amino acid Codon High Low RSCU(N) RSCU(N) RSCU(N) RSCU(N) Phe UUU 1.25 (5) 1.13 (9) Ser UCU 1.50 (2) 0.95 (3) UUC 0.75 (3) 0.88 (7) UCC 0.00 (0) 0.95 (3) Leu UUA 2.00 (6) 2.10 (14) UCA 0.75 (1) 1.58 (5) UUG 0.33 (1) 1.50 (10) UCG* 2.25 (3) 0.00 (0) CUU 1.33 (4) 0.90 (6) Pro CCU* 4.00 (3) 1.00 (1) CUC 0.00 (0) 0.30 (2) CCC 0.00 (0) 0.00 (0) CUA 1.67 (5) 0.75 (5) CCA 0.00 (0) 1.00 (1) CUG 0.67 (2) 0.45 (3) CCG 0.00 (0) 2.00 (2) Ile AUU 1.29 (6) 1.59 (9) Thr ACU* 3.11 (7) 1.33 (6) AUC 0.64 (3) 0.35 (2) ACC 0.44 (1) 0.89 (4) AUA 1.07 (5) 1.06 (6) ACA 0.00 (0) 0.67 (3) Met AUG 1.00 (3) 1.00 (5) ACG 0.44 (1) 1.11 (5) Val GUU 1.14 (2) 1.80 (9) Ala GCU 2.29 (4) 0.80 (3) GUC 0.00 (0) 0.80 (4) GCC 0.00 (0) 1.60 (6) GUA 1.71 (3) 1.00 (5) GCA 1.14 (2) 1.33 (5) GUG 1.14 (2) 0.40 (2) GCG 0.57 (1) 0.27 (1) Tyr UAU 2.00 (5) 1.25 (5) Cys UGU 0.00 (0) 2.00 (6) UAC 0.00 (0) 0.75 (3) UGC 0.00 (0) 0.00 (0) TER UAA 0.00 (0) 1.00 (1) TER UGA 2.00 (2) 0.00 (0) UAG 1.00 (1) 2.00 (2) Trp UGG 1.00 (1) 1.00 (5) His CAU 0.00 (0) 1.60 (2) Note: *Codons that occur significantly more often ( P < 0.01).


### Table 2: Optimal codons of B. falcatum chloroplast genome genes based on the RSCU.

| Amino acid | Codon | High | Low | Amino acid | Codon | High | Low |
| RSCU(N) | RSCU(N) | RSCU(N) | RSCU(N) |
| Phe | UUU | 1.25 (5) | 1.13 (9) | Ser | UCU | 1.50 (2) | 0.95 (3) |
| UUC | 0.75 (3) | 0.88 (7) | UCC | 0.00 (0) | 0.95 (3) |
| Leu | UUA | 2.00 (6) | 2.10 (14) | UCA | 0.75 (1) | 1.58 (5) |
| UUG | 0.33 (1) | 1.50 (10) | UCG* | 2.25 (3) | 0.00 (0) |
| CUU | 1.33 (4) | 0.90 (6) | Pro | CCU* | 4.00 (3) | 1.00 (1) |
| CUC | 0.00 (0) | 0.30 (2) | CCC | 0.00 (0) | 0.00 (0) |
| CUA | 1.67 (5) | 0.75 (5) | CCA | 0.00 (0) | 1.00 (1) |
| CUG | 0.67 (2) | 0.45 (3) | CCG | 0.00 (0) | 2.00 (2) |
| Ile | AUU | 1.29 (6) | 1.59 (9) | Thr | ACU* | 3.11 (7) | 1.33 (6) |
| AUC | 0.64 (3) | 0.35 (2) | ACC | 0.44 (1) | 0.89 (4) |
| AUA | 1.07 (5) | 1.06 (6) | ACA | 0.00 (0) | 0.67 (3) |
| Met | AUG | 1.00 (3) | 1.00 (5) | ACG | 0.44 (1) | 1.11 (5) |
| Val | GUU | 1.14 (2) | 1.80 (9) | Ala | GCU | 2.29 (4) | 0.80 (3) |
| GUC | 0.00 (0) | 0.80 (4) | GCC | 0.00 (0) | 1.60 (6) |
| GUA | 1.71 (3) | 1.00 (5) | GCA | 1.14 (2) | 1.33 (5) |
| GUG | 1.14 (2) | 0.40 (2) | GCG | 0.57 (1) | 0.27 (1) |
| Tyr | UAU | 2.00 (5) | 1.25 (5) | Cys | UGU | 0.00 (0) | 2.00 (6) |
| UAC | 0.00 (0) | 0.75 (3) | UGC | 0.00 (0) | 0.00 (0) |
| TER | UAA | 0.00 (0) | 1.00 (1) | TER | UGA | 2.00 (2) | 0.00 (0) |
| UAG | 1.00 (1) | 2.00 (2) | Trp | UGG | 1.00 (1) | 1.00 (5) |
| His | CAU | 0.00 (0) | 1.60 (2) |  |  |  |  |

## Discussion


## Whole-plastid-based barcodes

B. falcatum belongs to the Apiaceae family in plant taxonomy. Nowadays, several chloroplast genomes of the Apiaceae and Araliaceae families have been studied including Panax ginseng C. A. Meyer, Atriplex undulata (Moq.) D. Dietr., Daucus carota L. and Anthriscus cerefolium Hoffm. ( Kim and Lee, 2004 , Li et al., 2013 , Zhao et al., 2015 ). The complete chloroplast genome of B. falcatum indicates that there are no significant differences between B. falcatum chloroplast genome and those from the two closely related families (Apiaceae and Araliaceae) in the genome size and physical shape. But the information of the cp-genome has shown great potential in species discrimination, especially for closely related taxa ( Li, Yang, & Henry, 2015 ). B. falcatum cp-genome as a “super-barcode” could be an effective option that might be widely to distinguish the traditional Chinese medicine B. falcatum and its adulterants effectively.


## Main factors affect codon usage patterns

Our study analyzed the codon usage patterns and nucleotide composition of 78 genes in B. falcatum cp genome. We found that the codon usage patterns of B. falcatum cp genome were impacted by several factors, such as mutational pressure, translational selection and compositional constraints ( Li et al., 2019 , Sueoka, 1988 ).

Generally, codon usage bias is thought to be affected by compositional constraints. In Oncidium Gower Ramsey cp genome, the codon usage bias is significantly affected by compositional constraints ( Xu et al., 2011 ). In our RSCU analysis, we can infer that codon usage patterns are mainly influenced by compositional constraints under mutational pressure. In addition, the codon usage patterns analysis together with gene map reveals that the B. falcatum cp genome is slightly rich in AT and exhibits some compositional bias towards A or T nucleotide which was consistent with previous studies on higher plant cpDNA ( He et al., 2017 , Zhang et al., 2018 ) that clarify the reliability of our research results.

In mammals, there is no correlation between codon usage bias and gene expression level ( Karlin and Mrázek, 1996 ). But in plants (e.g., Lonicera macranthoides Hand.-Mazz. and Rheum palmatum L.), codon usage bias is strongly affected by the translation level, ( Liu et al., 2019 , Huo et al., 2021 ). In the present study, the mean ENC value of B. falcatum cp genome was 48.48, indicating that codon usage bias of the coding genes was very low. Our data demonstrated that there was not significantly correlation between the CAI and ENC values, suggesting that gene expression level was not the main influence factor which was inconsistent with the previous studies. There are some deviations among these results due to the small sample size, as only 78 genes were left for the codon usage analysis. In summary, the codon usage bias in B. falcatum cp genome is low, influenced by natural selection, mutation pressure, nucleotide composition.

Codon optimization has been widely applied in heterologous system used to increase protein expression ( Peng, Yao, Xiong, Chen, & Li, 2006 ). It is valuable to recognize that optimal codons rather than overall abundant codons could be used for the optimization. In this study, we defined three codons as the ‘‘optimal codons’’, that will be significant to introducing point mutation and modifying heterologous genes to increase the expression level of specific protein.


## Conclusion

In summary, we have determined the cp genome of B. falcatum and investigated the factors affecting codon usage bias in B. falcatum cp genome. The features of B. falcatum cp genome can be used to provide much more barcode information for species discrimination and the results of codon usage bias provide theoretical basis for codon optimization of exogenous genes and improve the prediction accuracy for new members of chloroplast genome and identification of unknown genome.

