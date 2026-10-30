# De-Identified Manuscript: SP_ANON_142

> **Blinding Note:** All title, author, affiliation, journal, and identifier metadata have been scrubbed for unbiased methodological review.

## Abstract & Main Text

## Morgan E Wirthlin


## Tobias A Schmid


## Julie E Elie


## Xiaomeng Zhang


## Amanda Kowalczyk


## Ruby Redlich


## Varvara A Shvareva


## Ashley Rakuljic


## Maria B Ji


## Ninad S Bhat


## Irene M Kaplow


## Daniel E Schäffer


## Alyssa J Lawler


## Andrew Z Wang


## BaDoi N Phan


## Siddharth Annaldasula


## Ashley R Brown


## Tianyu Lu


## Byung Kook Lim


## Eiman Azim


## Nathan L Clark


## Wynn K Meyer


## Sergei L [AUTHOR]


## Maria Chikina


## Michael M Yartsev


## Andreas R Pfenning

Present address: Allen Institute for Brain Science; Seattle, WA 98109, USA.

Present address: Broad Institute, Massachusetts Institute of Technology; Cambridge, MA 02142, USA.

Present Address: Massachusetts Institute of Technology; Cambridge, MA 02139

These authors contributed equally to this work

These authors jointly supervised the work

Zoonomia Consortium Members listed at the end of the Main Text document

Author Contributions:

Conceptualization: ARP, MEW, TAS, JEE, MMY

Methodology: ARP, MEW, TAS, JEE, MMY, IMK

Resources: TAS, MMY, ARB, WM, EA, BKL

Data Curation: TAS, JEE, XZ, BNP, AZW

Investigation: MEW, TAS, JEE, VAS, AR, MBJ, NSB, TL, MMY, ARP

Software: MEW, XZ, IMK, DES, SA, JEE, APR

Formal analysis: MEW, XZ, IMK, DES, AJL, ARP, MMY, TAS, JEE, VAS, AR, MBJ, NSB

Funding acquisition: ARP, MMY

Supervision: ARP, MEW, MMY, TAS, IMK

Writing – original draft: MEW, JEE, TAS, ARP

Writing – review & editing: MEW, JEE, TAS, IMK, DES, AJL, MMY, ARP

Corresponding authors. [EMAIL_REDACTED] , [EMAIL_REDACTED]

Issue date 2024 Mar 29.


## Abstract

Vocal production learning is a convergently evolved trait in vertebrates. To identify brain genomic elements associated with mammalian vocal learning, we integrated genomic, anatomical and neurophysiological data from the Egyptian fruit-bat with analyses of the genomes of 215 placental mammals. First, we identified a set of proteins evolving more slowly in vocal learners. Then, we discovered a vocal-motor cortical region in the Egyptian fruit-bat, an emergent vocal learner, and leveraged that knowledge to identify active cis -regulatory elements in the motor cortex of vocal learners. Machine learning methods applied to motor cortex open chromatin revealed 50 enhancers robustly associated with vocal learning whose activity tended to be lower in vocal learners. Our research implicates convergent losses of motor cortex regulatory elements in mammalian vocal learning evolution.


## One-Sentence Summary:

A bat vocal brain region is identified and leveraged in comparative genomic analyses to reveal the evolution of mammal vocal behavior.

Vocal production learning—the ability of an organism to modify the acoustic properties of its vocalizations as a result of social experience—is an example of convergent evolution, having evolved independently within multiple lineages of birds and mammals, including humans, where it manifests as speech ( Fig. 1A ) ( 1 , 2 ). Vocal production learning (“vocal learning”) has been extensively studied in songbirds, highlighting numerous shared behavioral features of birdsong and speech learning, such as a dependence on auditory input during a critical developmental period and a juvenile babbling phase of sensorimotor exploration prior to the maturation of the adult vocalizations ( 1 ). Convergence between song-learning birds and humans extends to neuroanatomical specializations, including direct corticobulbar projections from the vocal motor cortex analog to the hindbrain motoneurons controlling the vocal apparatus ( 3 ) and shared transcriptional specializations in analogous speech- and song-specialized brain regions ( 4 ). Thus, songbirds have become a premier model for exploring the fundamental brain anatomical, molecular, and genomic features associated with vocal learning ( 1 , 3 ). An expanding literature on vocal learning behavior across mammals suggests an underappreciated diversity in the phenotypic expression of vocal learning across the taxa traditionally thought to possess it ( 2 , 5 – 8 ). Study of the diverse forms of mammalian vocal learning behaviors could broaden our understanding of the core molecular, anatomical and physiological brain mechanisms of vocal learning and of the mechanisms underlying the convergent evolution of skilled motor behaviors more broadly.


## Figure 1. Convergent changes in protein sequence associated with vocal learning evolution across 215 mammalian species.

(A) A cladogram of mammalian species whose genomes were analyzed in this study highlights the convergent evolution of vocal learning species (in red) relative to non-learners (in black). The phylogenetic tree used in our analyses was derived from ( 98 ). Each of the genes implicated by RERconverge with lower ( B) or higher ( C ) evolutionary rates in vocal learners are annotated based on whether or not they show a significant signature within the four vocal learning clades based on a Bayes factor ≥ 5 ( 18 ). All significant gene ontology categories (adjusted p < 0.10, EnrichR) are plotted for the 200 genes with conserved (D) and accelerated (E) selection in vocal learning clades, based on the combination of RERconverge and [SOFTWARE] RELAX. The points are colored by the odds ratio within the set of implicated genes relative to the genes outside of the set, which corresponds to the degree of enrichment within that set.

We evaluated evidence of convergent genomic specializations shared among four lineages of vocal learning mammals that independently evolved this trait — bats, cetaceans, pinnipeds, and humans ( Fig. 1A ) — using whole-genome datasets and recently developed computational approaches. Specifically, we used protein-coding sequences from genomes generated by the Zoonomia Consortium ( 9 , 10 ) and models of evolutionary rate convergence ( 11 , 12 ) to identify protein-coding regions repeatedly associated with the evolution of vocal learning across mammals. Although we found 200 protein-coding genes significantly associated with vocal learning, none of them showed strong evidence of selection in all four mammalian clades and only five showed strong evidence of selection in three out of the four clades. Due to individual lineages contributing disproportionately to many of the protein-coding results, we hypothesized that noncoding regulatory elements might also be under constraint for the evolution of vocal learning.. We next profiled open chromatin, a proxy for regulatory element activity ( 13 ), in multiple brain regions and somatic tissues in the Egyptian fruit bat, a mammal with robust vocal plasticity ( 14 – 16 ) to identify vocalization-associated regulatory genomic specializations. We accomplished this by combining anatomical tracing and electrophysiological recordings in vocalizing bats to identify a region of motor cortex associated with vocal production. The vocalization-associated epigenomic data collected from this region of this bat species — combined with hundreds of mammalian genomes ( 17 , 18 ), their associated reference-free whole-genome alignments ( 19 ), and high-quality epigenomic data from the motor cortex of multiple additional mammalian species ( 20 – 22 ) — provided the foundation to apply a machine learning approach, the Tissue-Aware Conservation Inference Toolkit (TACIT) ( 23 ). This approach allowed us to identify putative enhancers, distal regulatory elements that tend to be highly tissue-specific, associated with the convergent evolution of vocal learning. In sum, we combined recently developed computational tools and neuroanatomical experiments in the Egyptian fruit bat and found evidence of convergent evolution in both protein-coding and noncoding DNA sequences.


## Results:


## Convergent Evolution in Protein Sequence Associated with Vocal Learning Behavior

To explore the possibility of shared genomic specializations associated with vocal learning, we first applied RERconverge ( 11 ) to recently released protein-coding alignments obtained for hundreds of mammals ( 10 ) to identify protein-coding genes whose relative rates of evolution differ between vocal learners and other mammals, and which may thus be under selection related to vocal learning ( 11 , 24 ). We analyzed 16,209 high-quality protein-coding gene alignments across 215 boreoeutherian mammals, including 26 vocal learning species, 164 vocal non-learners, and 25 species without confident annotations ( Fig. 1A , Data S1 ; Materials and Methods). We found evidence for lower evolutionary rates in vocal learners compared to non-learners in 804 genes and evidence for elevated evolutionary rates in 102 genes (Tau adj. p < 0.01 and permulations ( 24 ) adj. p < 0.01) ( Data S2 ; Fig. S1 ). To identify which specific clades were driving the differential rates of evolution, we applied a Bayes Factor analysis that examines each clade individually for evidence of selection ( 18 ) ( Data S2 ). Despite the large number of significant associations based on RERconverge, we found no single protein-coding gene with consistently lower or elevated evolutionary rates in all four vocal learning clades. Among the genes with reduced evolutionary rates in vocal learning species, we found only five out of 804 protein-coding genes with strong evidence of selective pressure in three out of the four vocal learning clades: CENPC , CATSPERG , MGA , TREML2 , and ZCWPW1 (Bayes Factor > 5) ( Fig. 1B , C ). None of these proteins reached the threshold for selection in the human lineage (Materials and Methods), which could indicate different mechanisms of evolution in the laurasiatherian vocal learning clades relative to humans. Our results suggest that the vast majority of protein-coding genes that we identify are evolving much faster or much slower in one clade, but are only weakly associated with vocal learning across the other lineages.

The most strongly associated genes were CENPC ( Fig. S2A ; Tau = −0.30; Tau adj. p = 8.7 × 10 −6 ; permulations adj. p <= 0.001), and GRM8 ( Fig. S2B , Tau = 0.26; Tau adj. p = 3.5×10 −4 ; permulations adj. p <= 0.001). GRM8 represents an especially promising candidate because it has previously been linked to anatomical specializations for vocal learning in songbirds ( 25 ) and is a known target of the speech-associated FOXP2 transcription factor ( 26 ). In primates and rodents, both GRM8 and FOXP2 are markers of a rare class of medium spiny neurons implicated in motor control that coexpress both DRD1 and DRD2 dopamine receptors ( 27 – 29 ). Overall, our results support a model where vocal learning behavior is only partially explained by differences in protein-coding gene evolutionary rates.

To further explore selection on these vocal learning-associated protein-coding genes, we applied an additional set of tools from the [SOFTWARE] package that compares non synonymous (dN) and synonymous (dS) substitution rates in the nucleotides of the amino acid sequence ( 30 ). Here, these sensitive evolutionary models of codon substitution formally compare selective regimes, modeled as dN/dS distributions, between branches annotated with the vocal learning phenotype and the rest of the phylogenetic tree ( 12 , 30 ). The results were largely consistent with amino-acid level methods: the protein-coding genes with lower protein evolutionary rates in vocal learning clades also tended to be under higher constraint in vocal learning clades (Wilcoxon p = 2.5 × 10 −4 ), and the genes with higher evolutionary rates in vocal learning species showed evidence of accelerated evolution in these same clades (Wilcoxon p = 7.9 × 10 −9 ) ( Fig. S3 ; Data S3 ). To further explore the functional trends of protein-coding genes associated with the evolution of vocal learning, we focused on the set of proteins that showed consistent behavior between RERconverge and the [SOFTWARE] RELAX model (Benjamini-Hochberg false discovery rate q < 0.05). This yielded a set of 126 proteins that were more slowly evolving in vocal learning clades and 74 with an elevated rate of evolutionary changes relative to other species. The complementary approaches of RERconverge and [SOFTWARE] RELAX identify a total of 200 vocal learning-associated genes and suggest that this behavior, vocal learning, is having a substantial impact on protein evolutionary rates.

We further interrogated evolutionary pressures across the vocal learning-associated genes by looking for evidence of diversifying position selection using the [SOFTWARE] BUSTED-PH model. Evidence of diversifying positive selection was found in 6.3% (13 transcripts, 9 genes) within the set of genes with elevated rates of evolution in vocal learning species based on RER-Converge and the [SOFTWARE] RELAX model. As expected, we identified much lower rates of diversifying positive selection in the gene with lower rates of evolution in vocal learning species (1.0%) and within the set of randomly chosen transcripts (2.0%). Among the 9 genes that showed evidence of positive selection, 8 have been associated with neurodevelopment ( CCDC136 , KIDINS220 , LRRN1 , RSG5 , CYLD , GABRA5 , NETO2 , KIAA1109 ) ( 31 – 38 ). The gene CCDC136 has more directly been associated with multiple language-related phenotypes in humans( 31 , 39 , 40 ). These results suggest that the vocal learning-associated genes across mammals may tend to play a role in human brain development and vocal behavior.

To more systematically explore the functional trends within these 126 and 74 protein-coding genes, we conducted a gene ontology analysis using EnrichR. Protein-coding genes with lower evolutionary rates in vocal learning species were associated with Regulation of DNA-templated Transcription (p=1.10×10 −6 , adj. p=1.9×10 −5 ), Regulation of Canonical Wnt Signaling Pathway (p=5.1×10 −5 , adj. p=0.013), and the Autism human phenotype ontology (p=5.8×10 −6 , adj. p=0.0028) ( Fig. 1F , G ; Data S4 ). The genes with accelerated evolutionary rates were not enriched for any pathways at an adjusted p < 0.05 with at least 5 genes contributing. The enrichment of autism-associated genes among the set of genes with greater levels of conservation in vocal learners ( MECP2 , RAD21 , DYRK1A , SIM1 , FTSJ1 , MEIS2 , FGFR1 ) is particularly interesting given prevalence of speech delay and early vocal production differences in human subjects with autism ( 41 , 42 ) and the previous association between autism genes and the evolution of vocal behavior in birds and bats ( 43 , 44 ). Based on the association with autism, we further explored the function of the vocal learning-conserved gene set in the context of early vocal production differences. Although only four human loci have been associated with differences in early vocal production, protein-coding genes overlapping two of these loci show higher levels of conservation in vocal learning clades ( INSC , DAPK3 ) ( 45 ).


## Identification of a Vocal Production Region in Egyptian Fruit Bats

The enrichment of transcription factors in the set of vocal learning-associated proteins suggests that differences in gene regulation are likely to be a major factor in the evolution of vocal learning. Since gene regulation is often tissue-specific, we sought to identify motor regions of the brain involved in vocal production and contrast their epigenomic profiles with motor regions not involved in vocal production. We conducted this comparison in the Egyptian fruit bat, Rousettus aegyptiacus , a mammalian species with robust vocal plasticity ( 16 , 46 ) and with data on its motor cortex mapping ( 47 ). To identify a candidate region, we were guided by the hypothesis that fine vocal-motor control, a key ability to vocal learning, may be associated with the anatomical specialization of the motor cortex ( 48 – 51 ). In particular, previous work suggested that a cortical region controlling complex vocal behavior would be characterized by a direct, monosynaptic projection onto the motoneurons controlling the vocal source (in mammals, the larynx) ( 48 – 52 ). Such a direct connection has been observed robustly in humans ( 53 – 56 ) and vocal learning birds (songbirds, parrots and hummingbirds, ( 57 – 59 )), but has not been reliably found in vocal non-learning species such as chimpanzees ( 41 ) or mice ( 60 )

We first determined whether a direct corticobulbar anatomical connection existed in R. aegyptiacus . Guided by cortical mapping experiments ( 47 ), we injected anterograde tracers into the part of the motor cortex that has been associated with orofacial motor control (ofM1) and identified fluorescently labeled descending cortical fibers in the hindbrain region where the laryngeal motoneurons reside: the nucleus ambiguus (NA) ( Fig. 2A , Fig. S4A - B and Movie S1 ). To test the existence of a direct monosynaptic projection, we also specifically identified laryngeal motoneurons in the NA by retrogradely labeling them through bilateral muscular injection of CTB (Cholera Toxin B) into the cricothyroid muscles of the bat larynx ( Fig. 2A ). We validated the colocalization of descending cortical fibers and local synaptic boutons with laryngeal motoneurons using two complementary labeling approaches: one relying on immunostaining of synapses (VGLUT1) and the other one using viral labeling of synapses (SYN) ( Fig. 2B - F ; Fig. S5 ). Across five bats, 79.2% of the retrogradely labeled motoneurons (61/77) colocalized with descending cortical fibers and 26% of them (20/77) colocalized with both cortical fibers and synaptic boutons, pointing to the existence of a robust direct corticospinal projection to laryngeal motoneurons ( Fig. 2G ). This colocalization in the NA was consistent across the different techniques ( Fig. 2G , Fig. S5 ) and could not be found in any other brainstem motor nuclei, including the hypoglossal nucleus, which controls the tongue and neck muscles ( Fig. S4C - E ). We noted that the corticobulbar fibers crossed the midline anterior to the NA at the level of the facial nucleus, offering a direct contralateral path for the innervation of the NA ( Fig. S4F ). These anatomical findings highlight the bat ofM1 as a possible candidate region associated with vocal production.

(A) Right: schematic of anatomical tracing approaches. Retrograde tracer cholera toxin B (CTB, purple) was injected bilaterally into the cricothyroid muscles to label brainstem motoneurons in nucleus ambiguus (NA). Simultaneously, an anterograde viral tracer (channelrhodopsin-2, ChR2, or Synapsin/synaptophysin dual-label, SYN; green) was injected bilaterally into the orofacial motor cortex (ofM1) to label corticobulbar projections into NA. Left: example coronal section showing cortical injection sites with anterograde tracer (ChR2, green) and DAPI labeling (cyan). (B-F) Laryngeal motoneurons in the NA identified using a retrograde tracer (CTB, purple), cortical fibers labeled with ChR2 (green), corticobulbar synapses labeled with VGLUT1 (red), and DAPI (blue). B and C are overlaid images showing colocalization of fibers with a synaptic bouton on the retrograde labeled cell (white arrow). (G) Percentage of laryngeal motoneurons labeled with CTB that are colocalized with cortical fibers (blue) or with both cortical fibers and synaptic boutons (red). Note that both tracing techniques qualitatively yielded similar results: ChR2, n = 51 cells from 3 bats; Synapsin/synaptophysin dual-label virus (SYN), n = 26 cells from 2 bats. (H) Illustration of the experimental setup during which wireless electrophysiological recordings were conducted from the identified cortical region in freely behaving and vocalizing bats. (I) Spiking activity of an example ofM1 neuron aligned to the onset of vocalizations produced (bat’s own calls, orange) or heard (other bats’ calls, blue) by the bat subject. Top row , time varying mean firing rate and corresponding raster plot below. Colored lines in the raster plot show the duration of each vocalization. Note the increased firing rate during vocal production as compared to hearing. (J) Information (see Methods ) between the time varying firing rate and the amplitude of produced (x-axis) vs. heard (y-axis) vocalizations for 219 single units (marker shapes indicate bat ID, n =4 bats). The cell shown in (I) is highlighted in red. Inset shows the distribution of D-prime between motor and auditory information for the same cells. Note that the distribution is heavily skewed towards higher motor information rather than auditory information coded in the activity of the recorded neurons. Error bars are mean +/− SEM throughout the figure.

To further corroborate the role of ofM1 in vocal control, we tested whether ongoing single-cell neural activity in this area was associated with vocal production. We performed wireless electrophysiological recordings from four bats engaged in free vocal interactions with peers ( Fig. 2H ). Vocalizations were identified and recorded using wireless call detectors placed around the necks of the individual bats (see Materials and Methods, ( 46 )). We found that about half of the recorded single units in ofM1 (115/237) showed a significant change in firing rates when the bats produced vocalizations as compared to staying quiet ( Fig. S6A - C ; ANOVA with a Poisson Generalized Linear Model per cell; p-value threshold = 0.001; Materials and Methods). In 25% of ofM1 cells that were excited during vocal production (26/104), the change of activity could not be accounted for by jaw or tongue movements, indicating that these cells were engaged in the motor control of movements specific to vocal production ( Fig. S6D ). Furthermore, many of the single units had a sustained increase of activity during production of vocalizations, but not during perception of vocalizations ( Fig. 2I ). To further assess this specific neural modulation during vocal-motor production, we quantified the information between the time-varying firing rate and the amplitude modulation of the vocalizations. This analysis confirmed that ofM1 neurons had significantly higher motor than auditory information ( Fig. 2J ; likelihood-ratio test on LME models, N=219, LRStat = 62.515, df = 1, p = 2.6645×10 −5 ; average d-prime change in information gain during motor production = 0.15 ± 0.13, corresponding to an increase of 0.286 ± 0.035 bits/s). Combined, the results of the anatomical and electrophysiological study defined ofM1 as a motor cortical area associated with vocal production in R. aegyptiacus .


## Epigenomic Specializations in the Vocal Production Region of the Egyptian Fruit Bat Motor Cortex

We next sought to epigenomically profile candidate regulatory elements in vocal and non-vocal brain regions in R. aegyptiacus to identify vocal learning-associated regulatory genomic specializations. We generated a multi-tissue atlas of open chromatin data — indicative of regulatory activity — by performing ATAC-seq (assay for transposase-accessible chromatin sequencing ( 61 )) across 7 brain regions and 3 somatic tissues of R. aegyptiacus (Materials and Methods), including ofM1 ( Fig. 3A ). From a total set of 88,389 noncoding, non-promoter open chromatin regions (OCRs) in primary motor cortex (M1), we identified 348 candidate enhancers with differential open chromatin between orofacial motor cortex (ofM1) and wing motor cortex (wM1) (p < 0.05; Fig. 3B , Data S5 , Materials and Methods). Genes proximal to OCRs with differential open chromatin between ofM1 and wM1 were significantly enriched for functional association with neuronal projections and transcriptional regulation ( Data S6 ). These included OCRs near the genes of 51 known transcription factors (TFs), including FOXP2 , a TF that has been extensively implicated in human speech and vocal learning ( Fig. 3C ) ( 62 ). Notably, genes near OCRs differentially open between bat ofM1 and wM1 included genes we had identified as being under convergent acceleration in vocal learners using evolutionary approaches: RERconverge analysis (n = 11) and the [SOFTWARE] RELAX analysis (n=3; GATA3 , LRRN1 , TNIP3 ) ( Data S6 ). These specialized regions of open chromatin, coupled with an enrichment of transcription factors in the set of vocal learning-associated protein-coding genes, suggest that both cis and trans differences in gene regulation contribute to the evolution of vocal learning behaviors.

(A) Open chromatin was profiled from 7 dissected brain regions of Egyptian Fruit bats. (B) Volcano plot of ATAC-seq OCRs with differential activity between the orofacial and wing subregions of primary motor cortex (ofM1 and wM1, respectively) of Egyptian fruit bat. (C) Genome browser showing ofM1 and wM1 ATAC-seq traces at the 3’ end of the FOXP2 locus. Reproducible M1 open chromatin regions (OCRs) are indicated in blue, with a differentially active OCR in ofM1 relative to wM1 highlighted in red.


## Convergent Evolution in Candidate Enhancer Sequences Associated with Vocal Learning Behavior

Since there is accumulating evidence that cis -regulatory differences in enhancer regions are driving the evolution of complex traits ( 63 – 65 ), we sought to identify OCRs whose tissue- and cell type-specificity would be shared across species of vocal learners. Detecting cis -regulatory element differences associated with trait evolution is challenging because many enhancers can preserve the same regulatory function even when the underlying genome sequence is highly divergent, and many cis -regulatory elements have tissue-specific activity ( 66 – 68 ). Thus, methods for convergent evolution that rely on the alignment of individual nucleotides between species (e.g. ( 11 , 69 , 70 )) are likely to miss a substantial proportion of key candidate enhancers.

We therefore sought to extend our search for cis -regulatory elements whose evolution is associated with vocal learning behavior using a recently developed machine learning approach, TACIT (Tissue-Aware Conservation Inference Toolkit ( 23 )). Given that it is infeasible to map the brains and collect motor cortex tissue from each vocal learning and closely related non-learning species, the TACIT approach uses machine learning models ( 23 ) to predict motor cortex open chromatin across orthologous regions of the genome ( 66 – 68 ). TACIT then associates predictions with vocal learning in a way that corrects for phylogenetic relationships ( Fig. 4A ). We used the predictions from convolutional neural networks (CNNs) that were previously trained using DNA sequence-based M1 open chromatin data obtained in this study for R. aegyptiacus with ATAC-seq and collected earlier for the mouse ( 21 ), the rat, and the macaque ( 20 ) to predict motor cortex open chromatin across 222 mammalian genomes (Materials and Methods, ( 23 )). Given that parvalbumin has been shown to be a shared marker of brain areas critical for vocal learning in songbirds and humans ( 4 ), we also used CNNs trained to predict cell type-specific open chromatin using ATAC-seq data from mouse and human M1 parvalbumin-positive neurons (M1-PV+) ( 22 , 23 , 71 ). We identified regions whose predicted open chromatin was consistently lower or higher in vocal learners relative to vocal non-learners using phylogenetic logistic regression ( 72 , 73 ) with phylogenetic permutations ( 24 ) (permulations adj. p < 0.1; Fig. 4A , Materials and Methods, ( 23 )). We identified 33 open chromatin regions from our M1 CNN models that had lower predicted open chromatin in vocal learning species and 11 that had higher predicted open chromatin in vocal learning species ( Fig 4D ; Table S1 ; Data S7 ). From the M1-PV+ predictions, we identified five candidate enhancers that had lower predicted activity in vocal learning species and one candidate enhancer that had higher predicted regulatory activity in vocal learning species. ( Table S2 ; Data S7 ). Unlike the protein-coding genes, the majority of vocal learning-associated enhancers showed evidence of higher or lower activity in at least three out of the four vocal learning clades ( Fig. 4B , C , D ; Data S8 ). Consistent with the finding that convergent vocal learning-associated gene regulation is primarily repressive ( 4 ), we found that the majority of candidate enhancers (n = 38/50 OCRs, 76%) had lower predicted open chromatin activity in vocal learning relative to vocal non-learning mammals ( Fig. S7 ).

(A) Overview of applying the Tissue-Aware Conservation Inference Toolkit (TACIT ( 23 )) approach to vocal learning. OCRs (left) identified in motor cortex (M1). Measured open chromatin from M1 (4 species) were used to train convolutional neural networks (CNNs) to predict M1 open chromatin from sequence alone. Red bars and corresponding arrows indicate the presence of a peak while the blue bars represent the absence. The same OCRs were then mapped across 222 mammalian genomes (left) and the identified sequences were used as input to the CNNs to predict open chromatin activity. TACIT identified OCRs whose predicted open chromatin across species was significantly associated with those species’ vocal learning status. (B-C) The 4-way Venn diagrams represent the number of OCRs implicated by TACIT (both M1 and PV+) as displaying low (B) or high (C) activity in each of the vocal learning clades based on a t-test. (D) The heatmap visualizes specific open chromatin regions along the rows (predicted higher in vocal learners in green; predicted lower in vocal learners in purple) across 222 mammals in the columns (vocal learner in red, vocal nonlearner in black, insufficient or conflicting evidence in gray). The color in each cell corresponds to the z-scored predicted open chromatin, with low open chromatin in blue, mean open chromatin in white, and high open chromatin in red. For open chromatin regions predicted to be significantly less (E) or more (F) open in vocal learning species (p<0.05), the red point shows the number of overlapping regions (y-axis) across mouse cortical cell types (x-axis). The bar-plot shows the distribution across 1,000 permutations of the peaks implicated by TACIT. The notches extend 1.58 * IQR / sqrt(n), which gives a roughly 95% confidence).

To interpret potential functions of the vocal learning-associated candidate enhancers, we annotated the nearest genes in the mouse ( Data S9 ). In many cases, the genes closest to these putative enhancers have been associated with significant developmental delay or complete absence of speech when disrupted in humans ( Tables S1 - 2 ). Four of the OCRs identified by the M1 model were proximal to genes— GALC , TCF4 , TSHZ3 , and ZNF536 —that were also near OCRs with differential activity between bat ofM1 and wM1 ( Data S6 ). Two of the vocal learning-associated M1 OCRs were proximal to genes— DAAM1 and VIP —previously shown to have convergent gene expression between humans and song-learning birds ( 4 ). To further explore the function of the vocal learning-associated OCRs in the motor cortex, we annotated their cell type-specificity using publicly available mouse BICCN data ( 74 ). The cell type most enriched for OCRs predicted to be lower in vocal learning species was Layer V ET (extra-telencephalic) neurons, which have previously been implicated in vocal learning ( 75 ), but strong enrichments were also found for other cortical excitatory neurons ( Fig. 4E , F ; Data S10 ).

Among genes near vocal learning-associated OCRs, the DACT1 (TACIT adj. p = 0.0014; RERconverge Tau adj. p<0.0001) and CELF4 (TACIT adj. p < 0.023; RERconverge Tau adj. p<0.0034) proteins also displayed significantly lower relative evolutionary rates in vocal learners. Despite the lack of direct evidence in the literature for its role in speech production, CELF4 has been associated with autism in the human population ( 76 ) and its function in Layer V pyramidal neurons has been linked with seizures in mice ( 77 ).

Multiple M1-PV+ interneuron OCRs associated with vocal learning are near genes previously associated with autism. For example, an OCR that is negatively associated with vocal learning evolution is in an intron of the gene CCSER1 , which has nonsense mutations implicated in autism ( 78 ) and is in a locus associated with musical beat synchronization ( 79 ). An OCR that is positively associated with the evolution of vocal learning is in an intron of the gene CNTNAP4 , whose deletions and copy number variation in humans and mice have been implicated in neurological disorders, including autism in humans ( 80 , 81 ). To test whether these associations would have been identified by chance, we tested whether vocal learning-associated OCRs tended to be near genes associated with autism. We found the M1-PV+ OCRs with human orthologs near genes associated with autism ( 82 ) tend to be more significantly associated with vocal learning evolution than other OCRs with human orthologs (Wilcoxon p=0.0071).


## Discussion:

Convergent evolution of vocal production learning has been associated with convergent evolution at the neuroanatomical level: cortical motor regions driving vocal production in humans and songbirds (human motor cortex and songbird RA) show increased connectivity with the brainstem and striatum ( 3 ). These same motor regions also show convergent evolution in patterns of gene expression, with commonly decreased gene expression found in both song-learning birds and humans ( 4 ). In this study, we investigated convergent evolution of vocal learning in mammals, both at the anatomical and the genetic level. First, we found a direct motor corticobulbar connection from a cortical region implicated in vocal production in a vocal learning bat. Second, we revealed widespread evidence of convergent evolution across vocal learning mammals in protein-coding sequences and candidate regulatory enhancers.

Our parallel study of both coding and noncoding regions linked with the vocal learning trait identifies many protein-coding genes (200) and a smaller number of noncoding regions (50), distal sites of open chromatin, that are associated with vocal learning. Although a larger number of significant protein-coding genes are identified, the vast majority of these are primarily driven by strong evidence in one of the vocal learning clades and only weak evidence in the other three. In contrast, the majority of significant noncoding regions show robust evidence of convergent selective pressure in at least three out of the four clades. The larger number of identified proteins relative to open chromatin regions could be due to better statistical power from being able to directly model nucleotide evolution in protein-coding sequence, which tend to be more stable than regulatory elements across species ( 11 , 12 ). We note, however, that only 5/200 of the significantly associated protein-coding genes showed robust evidence of differential rates of evolution in at least three of four vocal learning clades. Out of these 200 proteins, many were neurodevelopmental transcription factors, which are among the most highly conserved genes in mammals ( 83 ) and thus likely to play roles in a broad range of contexts that could constrain their evolution. It is also possible that some of the identified proteins could be associated with other convergent traits that correlate with vocal learning across mammals, including echolocation (bats, cetaceans), marine adaptations (cetaceans, pinnipeds), or increased longevity (bats, cetaceans, humans).

In contrast, 33/50 vocal learning-associated OCRs had differential predicted open chromatin in at least three of four vocal learning clades; this independent convergence of gene regulatory function suggests that these OCRs may be critical for the evolution of vocal learning. Enhancers tend to have functions that are much more context- and tissue-specific ( 68 ), making them less functionally constrained than protein-coding genes, which could perhaps allow more flexibility for an individual enhancer to evolve a new role for a specific trait like vocal learning. In sum, our results suggest that the evolution of mammalian vocal learning is largely driven by changes to the noncoding regulatory elements that orchestrate gene expression rather than to the protein-coding genes themselves.

Despite the different methodologies applied to identify convergent evolution in coding and noncoding regions, both protein coding- and regulatory element-focused approaches implicated gene functional pathways associated with human autism. In our protein-coding analyses, genes with lower evolutionary rates based on both RERconverge and [SOFTWARE] RELAX were enriched for autism function. Likewise, in our analyses of regulatory evolution, multiple autism-linked genes were near human orthologs of the vocal learning-associated M1-PV OCRs. In humans, autism is often associated with speech delays and differences in social behavior, both of which could be related to the evolutionary trait of vocal learning ability( 84 ). Broadly, this could be evidence that genomic loci associated with a complex trait across mammals may also be associated with variations in related traits within the human population.

The bulk motor cortex OCRs with lower predicted open chromatin in vocal learners show the strongest tendency to overlap with OCRs in Layer V ET neurons, which form long range projections ( Fig. 4E ). These results are consistent with our previous findings showing decreases in the expression of axon guidance genes in the motor cortex of vocal learning species ( 4 ). Among other functions, the Layer V ET neurons implicated by TACIT create the corticospinal projections that have been hypothesized as an anatomical landmark of vocal learners ( 2 , 3 , 48 , 49 , 56 , 85 , 86 ). Furthermore, the neuroethological and anatomical experiments we conducted in R. Aegyptiacus provide evidence that corticospinal projection neurons are present in the motor cortex of that bat species and that this motor cortical region participates in vocal production. Thus, consistent with previous literature, our results support a model in which the loss of regulatory element activity in the motor cortex influences axon guidance properties of long range projection neurons, which allow more robust connectivity between the cortex and the brainstem of vocal learning mammals ( 4 , 85 , 87 ). Alternatively, these genetic differences could relate to potential differences in the density of disynaptic connections that have been associated with skilled motor behavior, including vocalization in non-human primates ( 88 , 89 ). Notably, these long range projection neurons have also been associated with predisposition to autism ( 90 ).


## Methods Summary

To find vocal learning-associated convergent evolution in protein-coding sequences of the mammalian genome, we began with amino acid level multiple sequence alignments produced by the Zoonomia consortium ( 10 ). Those served as input to two classes of methods, RERconverge ( 11 ) and [SOFTWARE] ( 30 ). RERconverge with an additional permutations correction for phylogenetic structure ( 24 ) was used to find protein-coding sequences whose evolutionary rates were associated with the presence or absence of vocal learning. [SOFTWARE] RELAX was used to find protein-coding sequences that were evolving more slowly, neutrally, or faster in vocal learning species. In addition, the [SOFTWARE] BUSTED-PH method ( 12 ) was applied to find evidence of diversifying positive selection. The gene ontology analysis was performed on the intersection of the RERconverge and [SOFTWARE] results using EnrichR ( 91 ). To control for false positives across all methods, Benjamini-Hochberg false discovery rate correction ( 92 ) was applied.

To examine the existence of a direct monosynaptic projection in a vocal learning mammal, the corticobulbar projections in Egyptian fruit-bats were mapped by tracing the projection from the orofacial motor cortex and from the cricothyroid muscles of the vocal cords. Performing immunohistochemistry in the brainstem revealed that synaptic boutons of cortical projection neurons overlapped with retrogradely-labeled motoneurons - confirming the existence of a direct monosynaptic projection. The role of the orofacial motor cortex during vocal production was then validated by quantifying the information between the vocalization amplitude and single cortical neuron activity measured wirelessly in vivo while the bats produced and listened to vocalizations.

To create an atlas of open chromatin regions in the bat motor cortex (M1), several brain regions, including wing-M1 and orofacial-M1, were separately dissected. The samples were cryopreserved, then the nuclei were isolated, and subsequently ATAC-Seq was performed to measure open chromatin. The open chromatin regions from this experiment were combined with previously published experiments in macaque, rat ( 23 ), and mouse ( 21 ) to create an atlas of cross-species motor cortex open chromatin.

To find vocal learning-associated convergent evolution in noncoding regions of the Boreoeutherian mammalian genome, the TACIT machine learning approach, was applied. Orthologous regions across genomes were found by combining the CACTUS whole genome multiple sequence alignment ( 19 ), halLiftover ( 93 ) and HALPER ( 94 ). Phyloglm ( 72 ) was then used to associate predicted motor cortex and parvalbumin-positive inhibitory interneuron open chromatin with binary annotations of vocal learning behavior. Phylogenetic permutations were applied to correct for phylogenetic tree structure and Benjamini-Hochberg to correct for multiple hypothesis testing. To identify potential trends in the cell type-specificity of the implicated regions, permutations on the regions of the genome that were predicted to have significantly higher or lower open chromatin in vocal learning species were conducted.
