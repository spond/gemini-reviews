# Anonymous Manuscript ID: TIME_ANON_0292

*(All identifying metadata, author names, journal titles, DOIs, and publication/citation calendar years have been scrubbed for temporally blinded review.)*

## Abstract

Ticks are obligate blood-sucking ectoparasite and common vector of a wide variety of zoonotic pathogens. In this research, we sequenced and assembled the circular complete mitogenome information of Chinese isolates of Hyalomma anatolicum maintained at the Laboratory. The 14,714 bp mitogenome consists of 37 genes, including 13 protein-coding genes (PCGs), 22 transfer RNA (tRNA) genes and 2 ribosomal RNA (rRNA). The nucleotide sequence of Hy. anatolicum mitogenome includes approximately A (35.05%), G (8.70%), T (41.20%) and C (11.26%), the proportion of A + T (80.04%) is substantially higher than G + C (19.96%). We compared mitogenome selection pressure of the Hy. anatolicum and found that positive selection signatures were detected in atp8, contrasting sharply with the strong purifying selection observed in cox1. Phylogenomic reconstruction using concatenated PCGs robustly placed Hy. anatolicum within a clade sister to Hy. excavatum . We further validated cox3, cytb, nad1, nad2, nad3, nad4, nad4L, nad5 and nad6 as lineage-specific markers mirroring full mitogenome topology, proposing their cost-effective use in Hyalomma systematics. The divergence time analysis suggests that Hy. anatolicum was the most recent species in Hyalomma , 1.95 Mya. As far as we know, this is the first study exploring the complete mitogenome for Hy. anatolicum . Here, we obtained the whole mitogenome sequence for the species Hy. anatolicum , which enriched the mitogenome data of ticks, provided new idea for future research on the molecular evolution, population heredity and systematics of ticks.

Keywords: Ticks, Hyalomma anatolicum , Mitogenome, Phylogeny


## Introduction

Ticks are obligate blood-sucking ectoparasites that can parasitize most vertebrates. Tick-borne diseases pose a significant threat to human and animal health (Jongejan and Uilenberg [YEAR] ), hence ticks were considered to be second only to mosquitoes as the most common vectors of a wide variety of zoonotic pathogens, including bacteria, viruses, and protozoa. They facilitate the transmission of a broad spectrum of infections and diseases, thereby holding substantial public health importance (Duron et al. [YEAR] ; Gulia-Nuss et al. [YEAR] ). In China, ticks are widely distributed and cause substantial annual economic losses (Strydom et al. [YEAR] ). Current records indicate 124 validated tick species and 103 tick-borne pathogens including 29 pathogens infective to humans in China ([REDACTED_AUTHOR] et al. [YEAR] ).

The genus Hyalomma , belonging to the family Ixodidae, comprises 27 recognized species naturally occurring in the tropical and subtropical regions of Asia, Africa, and Europe (Kumar et al. [YEAR] ). These ticks are known vectors of numerous pathogens affecting animals and humans, including the Crimean-Congo hemorrhagic fever (CCHF) virus, West Nile virus, Venezuelan equine encephalitis virus, African horse sickness virus, Rickettsia aeschlimannii , Anaplasma marginale , Coxiella burnetii , Theileria annulata , Theileria lestoquardi , Theileria ovis , Theileria equi , Babesia occultans , Babesia caballi , and Babesia sp. Xinjiang (Bonnet et al. [YEAR] ).

Hyalomma anatolicum , a species of major medical and veterinary concern, is predominantly distributed across Asia and infests a wide range of vertebrate hosts. It transmits several pathogens to humans and livestock, including the CCHF virus, Thogoto virus, Wad Medani virus, Ehrlichia spp., Rickettsia spp., Coxiella spp., Theileria spp., and Babesia spp., (Choubdar et al. [YEAR] ).

Emerging resistance of Hy. anatolicum to commonly used insecticides, such as fipronil, ivermectin, diazinon, deltamethrin, and cypermethrin, has been reported in Pakistan and India (Bonnet et al. [YEAR] ; Gupta et al. [YEAR] ). In China, pyrethroids are the primary chemical insecticides for tick control. However, overreliance on this class of insecticides may accelerate resistance development. Additionally, as the geographic range of Hy. anatolicum expands, it is increasingly crucial to explore its genetic diversity and population structure.

The mitogenomes are highly valued in phylogenetic analysis and molecular evolution due to their maternal inheritance, haploid nature, rapid evolution rate, and low recombination, alongside its low molecular weight, high copy number, and genetic conservation (Winn et al. [YEAR] ). The mitogenome, comprising of 13 protein-coding genes (PCGs), 22 transfer RNAs (tRNAs), and two ribosomal RNAs (rRNAs), has proven to be an invaluable tool for identifying tick species as well as elucidating their pathogenic, geographical relationships, and evolutionary dynamics (Chen et al. [YEAR] ). Researchers have employed mitogenome as informative molecular markers to conduct extensive evolutionary studies across various animal taxa (Ciloglu et al. [YEAR] ). In addition, mitochondrion has been considered as the target for exploring the insecticides and acaricides by inhibiting mitochondrial electron transport (Lummen [YEAR] ).

In this study, we sequenced, annotated and analyzed the complete mitogenome of a Chinese isolate of Hy. anatolicum using Illumina sequencing technology. Our findings contribute to future phylogenetic and taxonomic research on the Ixodidae family, offering a foundation for better understanding the population genetics, phylogenetics and molecular epidemiology, and exploring the insecticides of this significant tick species.


## Materials and methods


## Tick samples

Adult Hy. anatolicum ticks (Fig. 1 ) used in this study were maintained and reared as a laboratory stock at the Laboratory of Ticks and Tick-Borne Diseases (TTBD) in Lanzhou Veterinary Research Institute, Chinese Academy of Agricultural Sciences (Lanzhou, China).


> **Fig. 1:** Morphology of a female adult Hy. anatolicum . ( A ) dorsal view, ( B ) ventral view


## DNA extraction and mitogenome sequencing

One Hy. anatolicum specimen was immersed in sterile distilled water for 45 min to remove microorganisms from the surface. Genomic DNA was isolated from ticks with the QIAamp DNA Blood and Tissue Mini Kit (Qiagen, Cat No: 51306, Hilden, Germany) according to the manufacturer’s instructions. The quality of the DNA was evaluated using an Aglient 4200 Bioanalyzer. The isolated DNA was used to construct libraries and sequenced using a standard Illumina HiSeq [YEAR] platform with PE150 ([REDACTED_AUTHOR] et al. [YEAR] ).


## Genome assembly and annotation

Genome assembly was performed using NECAT (v0.0.1) and NextDenovo de novo assemblers ([REDACTED_AUTHOR] et al. [YEAR] ). We used the quickmerge package ( [GITHUB_REPO_REDACTED] ) to merge the assembly output derived from these de novo tools (NextDenovo and NECAT). MITOS Web Server ( http://mitos.bioinf.uni-leipzig.de/index.py ) was used to predict the orientation, size and position of PCGs, tRNA genes and rRNA genes under the genetic code “05-invertebrate”. A circular mitochondrial genomic map was constructed using Proksee (Grant et al. [YEAR] ) ( https://proksee.ca/ ). We calculated nucleotide composition of the complete mitogenome, PCGs, tRNAs and rRNAs in Geneious, and measured the skewness using the following formulas: AT skew = (A-T)/(A + T) and GC skew = (G-C)/(G + C) (Perna and Kocher [YEAR] ). Nucleotide composition, codon usage, and relative synonymous codon usage (RSCU) values as well as nucleotide substitution statistics were determined using MEGA7. The annotated mitogenome sequence was submitted to China National Center for Bioinformation (CNCB, https://www.cncb.ac.cn/ ) with accession number CRA010187.


## Ka/Ks analysis

Thirteen species of Ixodidae (Table 1 ) and Hy. anatolicum (isolated in this study) were used for substitution calculation. We calculated the non-synonymous (Ka) and synonymous (Ks) substitution rates of 13 PCGs using KaKs calculator (v2.0). We used KaKs calculator based on pairwise codon alignments to calculate the Ka/Ks ratios, M0 model (Branch site model) and invoked from PAML (Di Maro et al. [YEAR] ).


### Table 1: List of the 50 reported mitogenomes analyzed in this study with their GenBank accession numbers

| Genus | Species | GenBank No | Length |
| Rhipicephalus | Rhipicephalus australis | KC503255 | 14,891 bp |
|  | Rhipicephalus microplus | MW751680 | 14,763 bp |
|  | Rhipicephalus decoloratus | NC052828 | 15,268 bp |
|  | Rhipicephalus geigyi | KC503263 | 14,948 bp |
|  | Rhipicephalus evertsi | KY457538 | 14,740 bp |
|  | Rhipicephalus maculatus | KY457539 | 14,714 bp |
|  | Rhipicephalus appendiculatus | NC052829 | 15,001 bp |
|  | Rhipicephalus zambeziensis | KY457543 | 14,691 bp |
|  | Rhipicephalus simus | KY457542 | 14,721 bp |
|  | Rhipicephalus turanicus | NC035946 | 14,717 bp |
|  | Rhipicephalus sanguineus | JX416325 | 14,714 bp |
| Rhipicentor | Rhipicentor nuttalli | NC_039828 | 14,779 bp |
| Dermacentor | Dermacentor rhinocerinus | KY457526 | 14,708 bp |
|  | Dermacentor nitens | NC023349 | 14,839 bp |
|  | Dermacentor reticulatus | MT478096 | 14,806 bp |
|  | Dermacentor everestianus | NC042764 | 15,191 bp |
|  | Dermacentor marginatus | MK905212 | 15,067 bp |
|  | Dermacentor nuttalli | NC028528 | 15,086 bp |
|  | Dermacentor silvarum | NC026552 | 14,945 bp |
| Archaeocroton | Archaeocroton sphenodonti | JN863731 | 14,772 bp |
| Hyalomma | Hyalomma asiaticum | MF101817 | 14,720 bp |
|  | Hyalomma anatolicum | MW546283 | 14,731 bp |
|  | Hyalomma rufipes | KY457528 | 14,748 bp |
|  | Hyalomma truncatum | KY457529 | 14,779 bp |
|  | Hyalomma scupense | NC_062166 | 14,721 bp |
|  | Hyalomma marginatum | NC_056189 | 14,764 bp |
|  | Hyalomma excavatum | MW546284 | 14,733 bp |
| Amblyomma | Amblyomma triguttatum | NC005963 | 14,740 bp |
|  | Amblyomma cajennense | NC020333 | 14,780 bp |
|  | Amblyomma sculptum | NC032369 | 14,780 bp |
|  | Aponomma fimbriatum | NC017759 | 14,705 bp |
| Bothriocroton | Bothriocroton undatum | NC017757 | 14,769 bp |
|  | Bothriocroton concolor | NC017756 | 14,809 bp |
| Haemaphysalis | Haemaphysalis nepalensis | OL875096 | 14,720 bp |

## Phylogenetic and topological analysis

We downloaded 50 published complete mitogenome sequences from NCBI, 42 species of Ixodidae, 6 species of Argasidae, Nuttalliella namaqua and horseshoe crab Limulus polyphemus (Table 1 ). The phylogenetic tree was built on the concatenated datasets of 13 PCGs using ML (maximum likelihood) method. We used MEGA 11 for alignment and splicing and used IQ-Tree for establishment of the phylogenetic tree with 1000 bootstrap replications. We employed Limulus polyphemus (GenBank accession number NC_003057 ) as the outgroup ([REDACTED_AUTHOR] et al. [YEAR] ). We selected 7 species of Hyalomma for topological analysis, employed Rhipicentor nuttalli as the outgroup. Phylogenetic trees were built on 13 individual PCGs of Hy. anatolicum mitogenome in the same method as above.


## Divergence times estimates

Divergence time were estimated using MEGA 11 (Tamura et al. [YEAR] ), the clock method was set to RelTime-ML method and General Time Reversible model, the rates among sites was set to Gamma Distributed (G) and employed Limulus polyphemus as the outgroup. We selected three times calibrations to effectively increase the accuracy of divergence time estimation. Pairwise divergence time for “ Amblyomma triguttatum ” and “ Rhipicephalus sanguineus ”; “ Ixodes uriae ” and “ Rhipicephalus sanguineus ”; “ Ixodes uriae ” and “ Ornithodoros rostratus ” were 99 million years ago (Mya) (95% HPD 44.2–225.5), 192 Mya (95% HPD 62.1–316.5) and 288 Mya (95% HPD 83.8–394.3), respectively (Howard et al. [YEAR] ; Lozano-Fernandez et al. [YEAR] ; Bakkes et al. [YEAR] ).


## Results


## Mitogenome annotation and organization

The mitogenome of Hy. anatolicum is a circular double-stranded DNA molecule with a length of 14,714 bp. It includes 13 PCGs (nad1-6, nad4L, cox1-3, cytb, atp6, atp8), 2 rRNA genes (rrnL and rrnS) and 22 tRNA genes, which is consistent with the mtgenomes of the other Hyalomma species. The organization of the 37 genes is displayed in a circular map (Fig. 2 ).


> **Fig. 2:** Circular map and organization of the mitogenome of Hy. anatolicum . CDS protein coding sequences, tRNA transfer RNA genes, rRNA ribosomal RNA genes

Twenty three out of the 37 genes were encoded by the majority strand (J-strand) (trnI, trnT, nad6, cytb, trnS2, trnC, trnM, nad2, trnW, cox1, cox2, trnK, trnD, atp8, atp6, cox3, trnG, nad3, trnA, trnR, trnN, trnS1 and trnE) and the remaining genes encoded by the minority strand (N-strand) (trnQ, trnF, nad5, trnH, nad4, nad4L, trnP, trnL1, trnY, nad1, trnL2, rrnL, trnV and rrnS). The Hy. anatolicum mitogenome is relatively compact, it had 16 gene overlap regions and 14 gene intergenic regions (Table 2 ), with entire size of overlap regions is 254 bp (ranging from 1 to 59 bp) and intergenic regions is 183 bp (ranging from 2 to 51 bp). The intergenic region occurred at 24 gene junctions. The longest intergenic sequence (51 bp) was found between nad1 and trnL2, and the shortest intergenic sequence (2 bp) was found between trnI and trnQ, nad4L and trnT. Overlap regions occurred at 27 gene junctions. The longest overlap sequence (59 bp) was found between cox3 and trnG. The shortest overlap region (1 bp) was found between trnS2 and trnL1, trnK and trnD, nad3 and trnA.


### Table 2: Descriptive details of the Hy. anatolicum mitogenome indicating the gene order, location, Intergenic, initiation and termination codon, anticodon and coding strand

| Gene | Type | Location | Intergenic | Initiation and stop codon | Anticodon | Stand |
| trnI (Ile) | tRNA | 307–369 | 2 |  | GAT | + |
| trnQ (Gln) | tRNA | 372–436 | 21 |  | TTG | - |
| trnF (Phe) | tRNA | 458–517 |  |  | GAA | - |
| nad5 | CDS | 518–2173 |  | ATT/TAA |  | - |
| trnH (His) | tRNA | 2174–2235 | 6 |  | GTG | - |
| nad4 | CDS | 2242–3558 | −7 | ATG/TAA |  | - |
| nad4L | CDS | 3552–3827 | 2 | ATG/TAA |  | - |
| trnT (Thr) | tRNA | 3830–3890 |  |  | TGT | + |
| trnP (Pro) | tRNA | 3891–3953 | −31 |  | TGG | - |
| nad6 | CDS | 3923–4390 | 3 | ATT/TAA |  | + |
| cytb | CDS | 4394–5473 |  | ATG/TAA |  | + |
| trnS2 (Ser) | tRNA | 5474–5542 | −1 |  | TGA | + |
| trnL1 (Leu) | tRNA | 5542–5607 | 7 |  | TAG | - |
| trnC (Cys) | tRNA | 5915–5969 | 5 |  | GCA | + |
| trnM (Met) | tRNA | 5975–6038 | 27 |  | CAT | + |
| nad2 | CDS | 6066–7001 |  | ATT/TAA |  | + |
| trnW (Trp) | tRNA | 7002–7062 | −2 |  | TCA | + |
| trnY (Tyr) | tRNA | 7061–7122 | −8 |  | GTA | - |
| cox1 | CDS | 7115–8653 | 3 | ATT/TAA |  | + |
| cox2 | CDS | 8657–9341 | −12 | ATG/ACT |  | + |
| trnK (Lys) | tRNA | 9330–9396 | −1 |  | CTT | + |
| trnD (Asp) | tRNA | 9396–9457 |  |  | GTC | + |
| atp8 | CDS | 9458–9619 | −7 | ATT/TAA |  | + |
| atp6 | CDS | 9613–10,278 | 4 | ATG/TAA |  | + |
| cox3 | CDS | 10,283–11119 | −59 | ATG/TAA |  | + |
| trnG (Gly) | tRNA | 11,061–11122 |  |  | TCC | + |
| nad3 | CDS | 11,123–11,461 | −1 | ATT/TAA |  | + |
| trnA (Ala) | tRNA | 11,461–11,521 | 5 |  | TGC | + |
| trnR (Arg) | tRNA | 11,527–11,588 | −2 |  | TGF | + |
| trnN (Asn) | tRNA | 11,587–11,648 | −3 |  | GTT | + |
| trnS1 (Ser) | tRNA | 11,646–11,702 | 5 |  | TCT | + |
| trnE (Glu) | tRNA | 11,708–11770 | −48 |  | TTC | + |
| nad1 | CDS | 11,723–12,655 | 51 | ATT/TAA |  | - |
| trnL2 (Leu) | tRNA | 12,707–12769 | −25 |  | TAA | - |
The nucleotide composition of the Hy. anatolicum mitogenome includes approximately adenine = 5715 (35.05%), guanine = 1280 (8.70%), thymine = 6062 (41.20%) and cytosine = 1657 (11.26%). The proportion of adenine + thymine (80.04%) is substantially higher than proportion of guanine + cytosine (19.96%) (Charrier et al. [YEAR] ). AT-skew ranged from −0.2260 (for nad4L) to 0.1764 (trnD), while GC-skew ranged from −0.3282 (for nad2) to 0.5555 (for trnH). The whole AT-skew and GC-skew in the entire mitogenome was −0.0295 and −0.1284, respectively, indicating A and G base appears more infrequently than their counterpart bases (Table 3 ).


### Table 3: Composition and skew values in Hy. anatolicum

| Gene | Type | Size (bp) | A | G | T | C | A + T % | G + C % | AT-skew | GC-skew |
| Mitogenome |  | 14,714 | 5715 | 1280 | 6062 | 1657 | 80.04 | 19.96 | −0.02946 | −0.12836 |
| trnI (Ile) | tRNA | 63 | 23 | 10 | 25 | 5 | 76.19 | 23.81 | −0.04167 | 0.333333 |
| trnQ (Gln) | tRNA | 65 | 29 | 5 | 28 | 3 | 87.69 | 12.31 | 0.017544 | 0.25 |
| trnF (Phe) | tRNA | 60 | 26 | 5 | 24 | 5 | 83.33 | 16.67 | 0.04 | 0 |
| nad5 | CDS | 1656 | 583 | 158 | 789 | 126 | 82.85 | 17.15 | −0.15015 | 0.112676 |
| trnH (His) | tRNA | 62 | 27 | 7 | 26 | 2 | 85.48 | 14.52 | 0.018868 | 0.555556 |
| nad4 | CDS | 1317 | 437 | 140 | 640 | 100 | 81.78 | 18.22 | −0.18849 | 0.166667 |
| nad4L | CDS | 276 | 89 | 30 | 141 | 16 | 83.33 | 16.67 | −0.22609 | 0.304348 |
| trnT (Thr) | tRNA | 61 | 24 | 7 | 26 | 4 | 81.97 | 18.03 | −0.04 | 0.272727 |
| trnP (Pro) | tRNA | 63 | 28 | 8 | 24 | 3 | 82.54 | 17.46 | 0.076923 | 0.454545 |
| nad6 | CDS | 468 | 168 | 25 | 241 | 34 | 87.39 | 12.61 | −0.17848 | −0.15254 |
| cytb | CDS | 1080 | 348 | 103 | 486 | 143 | 77.22 | 22.78 | −0.16547 | −0.1626 |
| trnS2 (Ser) | tRNA | 69 | 34 | 6 | 24 | 5 | 84.06 | 15.94 | 0.172414 | 0.090909 |
| trnL1 (Leu) | tRNA | 66 | 29 | 8 | 22 | 7 | 77.27 | 22.73 | 0.137255 | 0.066667 |
| trnC (Cys) | tRNA | 54 | 26 | 3 | 20 | 5 | 85.19 | 14.81 | 0.130435 | −0.25 |
| trnM (Met) | tRNA | 64 | 24 | 10 | 21 | 9 | 70.31 | 29.69 | 0.066667 | 0.052632 |
| nad2 | CDS | 936 | 341 | 44 | 464 | 87 | 86 | 14 | −0.1528 | −0.32824 |
| trnW (Trp) | tRNA | 61 | 28 | 4 | 24 | 5 | 85.25 | 14.75 | 0.076923 | −0.11111 |
| trnY (Tyr) | tRNA | 62 | 22 | 10 | 26 | 4 | 77.42 | 22.58 | −0.08333 | 0.428571 |
| cox1 | CDS | 1539 | 485 | 195 | 618 | 241 | 71.67 | 28.33 | −0.12058 | −0.1055 |
| cox2 | CDS | 685 | 248 | 62 | 278 | 97 | 76.79 | 23.21 | −0.05703 | −0.22013 |
| trnK (Lys) | tRNA | 67 | 25 | 10 | 24 | 8 | 73.13 | 26.87 | 0.020408 | 0.111111 |
| trnD (Asp) | tRNA | 62 | 30 | 6 | 21 | 5 | 82.26 | 17.74 | 0.176471 | 0.090909 |
| atp8 | CDS | 162 | 72 | 5 | 66 | 19 | 85.19 | 14.81 | 0.043478 | −0.58333 |
| atp6 | CDS | 666 | 223 | 57 | 320 | 66 | 81.53 | 18.47 | −0.17864 | −0.07317 |
| cox3 | CDS | 837 | 264 | 85 | 394 | 94 | 78.61 | 21.39 | −0.19757 | −0.05028 |
| trnG (Gly) | tRNA | 62 | 31 | 3 | 25 | 3 | 90.32 | 9.68 | 0.107143 | 0 |
| nad3 | CDS | 339 | 113 | 25 | 178 | 23 | 85.84 | 14.16 | −0.22337 | 0.041667 |
| trnA (Ala) | tRNA | 61 | 24 | 6 | 26 | 5 | 81.97 | 18.03 | −0.04 | 0.090909 |
| trnR (Arg) | tRNA | 62 | 23 | 7 | 25 | 7 | 77.42 | 22.58 | −0.04167 | 0 |
| trnN (Asn) | tRNA | 62 | 24 | 9 | 22 | 7 | 74.19 | 25.81 | 0.043478 | 0.125 |
| trnS1 (Ser) | tRNA | 57 | 24 | 4 | 23 | 6 | 82.46 | 17.54 | 0.021277 | −0.2 |
| trnE (Glu) | tRNA | 63 | 22 | 7 | 29 | 5 | 80.95 | 19.05 | −0.13725 | 0.166667 |
| nad1 | CDS | 933 | 332 | 104 | 415 | 82 | 80.06 | 19.94 | −0.11111 | 0.11828 |

## Protein-coding genes

The total length of the PCGs was 10,894 bp, which is a proportion of 74.04% of the entire mitogenome. The nad5 (1656 bp) was the longest while atp8 (162 bp) was the shortest of PCGs. The genome composition of PCGs was adenine (33.99%), thymine (46.17%), guanine (9.48%) and cytosine (10.35%), which exhibits the popularity of biasness towards AT content among the PCGs (Table 3 ). Similar to insects, ticks usually adopt the “ATN” type codon as the initial codon in PCGs (Guo et al. [YEAR] ; Liu et al. [YEAR] , [YEAR] ) (Table 2 ), TAA was the most prevalent termination codon (Guo et al. [YEAR] ; Liu et al. [YEAR] ), cox2 use ACT termination codon and other genes (nad5, nad4, nad4L, nad6, cytb, nad2, cox1, cox2, atp8, atp6, nad3, nad1) use TAA termination codon. In addition, nad4 and nad4L; atp8 and atp6 have 7 overlapping nucleotides.

Analysis of codon usage showed that codons for all the 20 amino acids are present in all PCGs. The most frequently used codons are for amino acids Leu (12.44%), Phe (12.30%), Lys (9.81%), Asn (9.77%) and Ser (9.77%). The least used codons are Arg (0.57%), Gly (0.71%), Ala (0.76%) and Asp (1.02%) (Fig. 3 ). We calculated relative synonymous codon usage (RSCU) of Hy. anatolicum mitogenome (Fig. 3 ; Table 4 ). RSCU values > 1.0, equal and < 1.0 are considered to indicate positive, random, and negative codon usage bias, respectively (Liu et al. [YEAR] ). We found that UAA, GCU and CAU are the most biased codons, while the least used codons are CCG, CUG and CAC.


> **Fig. 3:** Codon usage pattern ( A ) and the relative synonymous codon usage (RSCU) ( B ) of Hy. anatolicum mitogenome. The box below the bar chart represents all codons encoding each amino acid, and the height of the column above represents the sum of all RECU values


### Table 4: Relative synonymous codon usage (RSCU) for Hy. anatolicum mitogenome

| Aminoacid | Codon | RSCU | Aminoacid | Codon | RSCU | Aminoacid | Codon | RSCU |
| Ala | GCG | 0.3243 | Pro | CCG | 0.1765 | Val | GUG | 0.3111 |
|  | GCA | 0.9730 |  | CCA | 1.3529 |  | GUA | 1.5556 |
|  | GCU | 1.7297 |  | CCU | 1.0588 |  | GUU | 1.6000 |
|  | GCC | 0.9730 |  | CCC | 1.4118 |  | GUC | 0.5333 |
| Cys | UGU | 1.3333 | Gln | CAG | 0.3059 | Trp | UGG | 0.9091 |
|  | UGC | 0.6667 |  | CAA | 1.6941 |  | UGA | 1.0909 |
| Asp | GAU | 1.6000 | Arg | CGG | 1.2857 | Tyr | UAU | 1.6209 |
|  | GAC | 0.4000 |  | CGA | 1.2857 |  | UAC | 0.3791 |
| Glu | GAG | 0.4348 |  | CGU | 1.0000 | Leu | UUG | 0.8361 |
|  | GAA | 1.5652 |  | CGC | 0.4286 |  | UUA | 3.1574 |
| Phe | UUU | 1.4992 | Ser | AGG | 0.8685 |  | CUG | 0.1869 |
|  | UUC | 0.5008 |  | AGA | 1.1858 |  | CUA | 0.6885 |
| Gly | GGG | 0.8000 |  | AGU | 0.8685 |  | CUU | 0.6885 |
|  | GGA | 1.2571 |  | AGC | 0.8685 |  | CUC | 0.4426 |
|  | GGU | 1.3714 |  | UCG | 0.3340 | Met | AUG | 0.4473 |
|  | GGC | 0.5714 |  | UCA | 1.5198 |  | AUA | 1.5527 |
| His | CAU | 1.7037 |  | UCU | 1.3194 | Thr | ACG | 0.4387 |
|  | CAC | 0.2963 |  | UCC | 1.0355 |  | ACA | 1.0323 |
| Ile | AUU | 1.5822 | Asn | AAU | 1.6367 |  | ACU | 1.6516 |
|  | AUC | 0.4178 |  | AAC | 0.3633 |  | ACC | 0.8774 |
| Lys | AAG | 0.3202 |  |  |  |  |  |  |
|  | AAA | 1.6798 |  |  |  |  |  |  |

## Transfer and ribosomal RNA genes

The whole length of tRNA genes was 1,373 bp with the length ranging from 54 nucleotide (trnC) to 69 nucleotide (trnS2). In recent years, mitochondrial 12S and 16S rRNA gene have been extensively used as genetic targets in phylogenetic research of ticks (Williams-Newkirk et al. [YEAR] ). The Hy. anatolicum 12S and 16S rRNA length were 697 bp and 1238 bp, respectively, they were clamped by trnI and trnL2 and were divided by the gene trnV. The AT-skew values were computed as 0.0414 and 0.0699, while GC-skew values were computed as 0.1549 and 0.1923 (Table 3 ), which revealed more adenine and guanine nucleotide prevalence among rRNAs.


## Selective pressure analysis

The ratio nonsynonymous (Ka) and synonymous (Ks) substitution rates (Ka/Ks) is a measure used in molecular evolution to assess the selective presence acting on PCGs. The Ka/Ks > 1 indicates positive selection, Ka/Ks = 1 indicates neutral evolution, and Ka/Ks < 1 indicates negative and purifying selection (Hurst [YEAR] ). In this study, we selected the 13 tick species that are most closely related to Hy. anatolicum and calculated the Ka/Ks of 13 PCGs to investigate the evolutionary traits of selective pressure. The Ka/Ks values of most PCGs are < 1, which indicates a strong purifying and negative selection in Hy. anatolicum (Fig. 4 , Table 5 ). However, the Ka/Ks ratios of atp8 in R. microplus, D. marginatus, Hy. rufipes and R. decoloratus are > 1, which indicated the existence of positive selection. The overall average Ka/Ks values of each PCG show that the highest average Ka/Ks value is found for atp8 (0.9356), followed by nad2 (0.4979), nad4L (0.4403), nad6 (0.3836), nad5 (0.3825), nad3 (0.3824), nad4 (0.3104), nad1 (0.2923), atp6 (0.2830). The genes cox3, cytb and cox2 show lower values of 0.1561, 0.1517 and 0.1005, respectively. The cox1 gene shows the lowest average Ka/Ks value (0.0640) and has little variation among genera, suggesting that cox1 is very conserved and undergoes strong purifying selection. The atp8 was the most variable gene, cox1-3 and cytb being reported as the most conserved mitochondrial genes in most metazoans (Saccone et al. [YEAR] ). Therefore, we suggest cox1-3 and cytb may be evaluated as potential molecular markers for species identification in Hy. anatolicum .


> **Fig. 4:** Evolutionary rates (Ka/Ks) of 13 PCGs of Hy. anatolicum


### Table 5: Evolutionary rates (Ka/Ks) of Hy. anatolicum and 13 species of Ixodidae

| Hy.anatolicum | atp6 | atp8 | cox1 | cox2 | cox3 | cytb | nad1 | nad2 | nad3 | nad4 | nad4L | nad5 | nad6 |
| Dermacentor everestianus | 0.305 | 0.942 | 0.078 | 0.11 | 0.199 | 0.207 | 0.452 | 0.708 | 0.6 | 0.34 | 0.579 | 0.497 | 0.616 |
| Dermacentor marginatus | 0.281 | 1.061 | 0.074 | 0.104 | 0.125 | 0.161 | 0.409 | 0.506 | 0.375 | 0.442 | 0.419 | 0.441 | 0.338 |
| Dermacentor nitens | 0.317 | 0.92 | 0.072 | 0.101 | 0.15 | 0.174 | 0.305 | 0.533 | 0.297 | 0.373 | 0.449 | 0.421 | 0.593 |
| Dermacentor reticulatus | 0.268 | 1.023 | 0.065 | 0.078 | 0.164 | 0.17 | 0.316 | 0.648 | 0.468 | 0.434 | 0.658 | 0.435 | 0.436 |
| Dermacentor rhinocerinus | 0.301 | 0.809 | 0.067 | 0.121 | 0.171 | 0.159 | 0.3 | 0.453 | 0.321 | 0.291 | 0.444 | 0.402 | 0.377 |
| Hyalomma asiaticum | 0.168 | 0.278 | 0.037 | 0.036 | 0.115 | 0.073 | 0.108 | 0.247 | 0.132 | 0.169 | 0.25 | 0.117 | 0.168 |
| Hyalomma rufipes | 0.227 | 1.355 | 0.058 | 0.078 | 0.172 | 0.117 | 0.163 | 0.294 | 0.45 | 0.2 | 0.408 | 0.196 | 0.276 |
| Hyalomma truncatum | 0.156 | 0.793 | 0.04 | 0.062 | 0.124 | 0.106 | 0.12 | 0.273 | 0.224 | 0.178 | 0.273 | 0.164 | 0.181 |
| Rhipicentor nuttalli | 0.375 | 0.859 | 0.062 | 0.114 | 0.19 | 0.226 | 0.42 | 0.457 | 0.358 | 0.335 | 0.427 | 0.389 | 0.427 |
| Rhipicephalus decoloratus | 0.408 | 1.569 | 0.077 | 0.149 | 0.192 | 0.159 | 0.34 | 0.762 | 0.518 | 0.342 | 0.359 | 0.543 | 0.454 |
| Rhipicephalus microplus | 0.386 | 1.001 | 0.07 | 0.186 | 0.155 | 0.163 | 0.326 | 0.722 | 0.423 | 0.358 | 0.474 | 0.482 | 0.466 |
| Rhipicephalus sanguineus | 0.234 | 0.833 | 0.07 | 0.095 | 0.156 | 0.145 | 0.304 | 0.465 | 0.399 | 0.287 | 0.472 | 0.476 | 0.328 |
| Rhipicephalus simus | 0.254 | 0.72 | 0.061 | 0.072 | 0.117 | 0.113 | 0.236 | 0.406 | 0.406 | 0.287 | 0.511 | 0.411 | 0.327 |

## Phylogenetic and topological analysis

The phylogenetic tree constructed from mitogenome reveals evolutionary relationships among tick species. We concatenated nucleotide sequences of 13 PCGs of the 50 reported mitogenomes obtained from NCBI (Table 1 ). The tree had three branches, Ixodidae (blue), Argasidae (yellow) and Nuttalliellidae (green), with the same family species gathering in the same branch.

The phylogenetic tree could be clearly divided into two clades within the genus Hyalomma . One clade composed of sister-groups of ( Hy. marginatum + Hy. rufipes ) + ( Hy. excavatum + Hy. anatolicum ) and Hy. truncatum . The other clade was composed of ( Hy. asiaticum + Hy. scupense ) sister species. The tree showed that Hy. anatolicum exhibits a close relationship with Hy. excavatum (Fig. 5 ). The same or different phylogenetic topologies were due to different protein-coding of Hyalomma mitogenome (Fig. 6 ). Specifically, only cox1, cox2, atp6 and atp8 could not infer the exact same topology as inferred by the concatenated mitochondrial phylogeny. These protein-coding genes were identified as new genetic markers for the phylogenetic and evolutionary studies of Hyalomma .


> **Fig. 5:** Phylogenetic tree showing evolutionary relationship among tick species based on concatenation of 13 PCGs. Limulus polyphemus ( NC_003057 ) is an outgroup. The percentage of bootstrap support is given at each node


> **Fig. 6:** Fourteen topological phenograms based on each PCG (ATP6 – NAD6) and concatenation of 13 PCGs. The Rhipicentor nuttalli is the outgroup. The percentage of the bootstrap support is given at each node


## Divergence times analysis

The divergence time analysis suggests that Hyalomma were the most recent genus in hard ticks. Their diversification occurred 45.12 Mya during the Paleogene, this coincides with the radiation of artiodactyls, the primary hosts of extant Hyalomma species, suggesting host-driven cladogenesis. Strikingly, intrageneric diversification continued until 1.95 Mya with Hy. anatolicum , corresponding to aridification pulses in Asia that shaped its xeric adaptations. Contrasting with this recent divergence, older genera demonstrate deeper evolutionary roots: Ixodes diverged in the Jurassic (167.68 Mya) alongside early mammalian lineages, while Amblyomma (64.39 Mya) and Dermacentor (50.98 Mya) emerged during angiosperm-dominated ecosystem shifts (Fig. 7 ).


> **Fig.7:** Divergence time estimates tree. Node values indicate median divergence time estimates, the red points indicate fossil calibrations, the green bar represents an interval of 95% highest probability density


## Discussion

The integration of mitochondrial genomics has proven indispensable for resolving taxonomic uncertainties in ticks, as mitogenomes provide robust phylogenetic signals across multiple evolutionary scales ([REDACTED_AUTHOR] et al. [YEAR] ). This study represents the first comprehensive analysis of Hy. anatolicum (14,714 bp), comprising 13 PCGs, 22 tRNAs, and 2 rRNAs. Notably, the genome exhibited a pronounced T/C nucleotide bias, supported by negative AT-skews and GC-skews, a pattern consistent with other hard tick mitogenomes (Lu et al. [YEAR] ; Tang et al. [YEAR] ).

Evolutionary analysis identified positive selection signatures in atp8 (Ka/Ks = 0.278—1.569), contrasting sharply with the strong purifying selection observed in cox1 (Ka/Ks = 0.037—0.078). This positions atp8 as a promising marker for intrageneric divergence analysis in Hyalomma. Phylogenomic reconstruction based on concatenated PCGs showed that Hy. anatolicum exhibits a close relationship with Hy. excavatum , consistent with previous findings by Sand et al. (Sands et al. [YEAR] ). While nad5 has been shown to differentiate Haemaphysalis japonica and H. megaspinosa (Moustafa et al. [YEAR] ), we further propose cox3, cytb, nad1, nad2, nad3, nad4, nad4L, nad5, and nad6 as core markers capable of replicating the topology of concatenated sequences of 13 PCGs, providing cost-effective alternatives to whole-genome sequencing, a critical advance given the prohibitive complexity of tick mitogenome amplification. Of course, their validity remains to be validated when more tick mitogenome were available. The divergence time analysis suggested that most genera of hard ticks began to form during the Paleogene, was attributed to the Cretaceous-Paleogene mass extinction that caused extinction of numerous groups (Klein et al. [YEAR] ), and its aftermath was a rapid diversification of surviving animals.

Mitochondrial markers have become an increasingly useful tool for tick identification (Zhang and Zhang [YEAR] ). Out of the 27 valid species of Hyalomma , approximately 15 implicated in pathogen transmission to humans and livestock (Sajid et al. [YEAR] ). However, despite their veterinary and medical importance, much less research has been dedicated to molecular classification of Hyalomma , and only a few mitogenome have been resolved (Hekimoglu and Ozer [YEAR] ; Liu et al. [YEAR] ). To our knowledge, this is the first study exploring the complete mitogenome of Hy. anatolicum and this becomes an important molecular marker for phylogeny of ticks. Our findings enhance the mitogenomic database for ticks, aiding species delineation, taxonomic classification, and future strategies for tick-borne disease control.

Jin Che: Data curation, Software and Writing – original draft. Yijun [REDACTED_AUTHOR]: Writing – original draft. Wei Li: Resources. Jin Luo: Resources. Qiaoyun Ren: Resources. Shuaiyang [REDACTED_AUTHOR]: Resources. Qingli Niu: Resources. Guiquan [REDACTED_AUTHOR]: Writing—Review and Supervision. Jinming [REDACTED_AUTHOR]: Conceived of study and Funding acquisition. Hong Yin: Writing—Review and Funding acquisition. Declaration of competing interest. All authors reviewed the manuscript.

The study was financially supported by the Science Fund for Creative Research Groups (22 JR5RA024), Special Project (22 CX8 NA011) and Natural Science Foundation (22 JR5RA031) of Gansu Province, National Key Research and Development Program of China (2022YFD1800200), NSFC (№31972701), the Innovation Program of Chinese Academy of Agricultural Sciences (CAAS-ASTIP-[YEAR]-LVRI), NBCITS (CARS-37), National Parasitic Resources Center (NPRC-[YEAR]–194-30).


## Data availability

The mitogenome sequence was submitted to China National Center for Bioinformation (CNCB, https://www.cncb.ac.cn/ ) with accession number CRA010187.


## Consent for publication


## Compliance with ethical standards

The authors declare that they have no competing interests.


## Associated Data


## Data Availability Statement

The mitogenome sequence was submitted to China National Center for Bioinformation (CNCB, https://www.cncb.ac.cn/ ) with accession number CRA010187.