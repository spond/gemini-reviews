# De-Identified Manuscript: AN_ANON_023

> **Blinding Note:** All title, author, affiliation, journal, year, software, and identifier metadata have been scrubbed for unbiased methodological review.

## Abstract

## Yin Tang


## Emil [AUTHOR]


## Chun Kit Kwok


## Yiliang Ding


## Anton [AUTHOR]


## Philip C [AUTHOR]


## Sarah M [AUTHOR]

† Present address: Department of Chemistry, University of Cambridge, Lensfield Road, Cambridge CB2 1EW, UK

‡ Present address: Department of Cell and Developmental Biology, John Innes Centre, Norwich Research Park, Norwich NR4 7UH, UK

*To whom correspondence should be addressed.

† Present address: Department of Chemistry, University of Cambridge, Lensfield Road, Cambridge CB2 1EW, UK

‡ Present address: Department of Cell and Developmental Biology, John Innes Centre, Norwich Research Park, Norwich NR4 7UH, UK

Associate Editor: Anna Tramontano

Received [YEAR] Dec 23; Revised [YEAR] Mar 30; Accepted [YEAR] Apr 12; Issue date [YEAR] Aug 15.


## Abstract

Motivation: RNAs fold into complex structures that are integral to the diverse mechanisms underlying RNA regulation of gene expression. Recent development of transcriptome-wide RNA structure profiling through the application of structure-probing enzymes or chemicals combined with high-throughput sequencing has opened a new field that greatly expands the amount of in vitro and in vivo RNA structural information available. The resultant datasets provide the opportunity to investigate RNA structural information on a global scale. However, the analysis of high-throughput RNA structure profiling data requires considerable computational effort and expertise.

Results: We present a new platform, StructureFold, that provides an integrated computational solution designed specifically for large-scale RNA structure mapping and reconstruction across any transcriptome. StructureFold automates the processing and analysis of raw high-throughput RNA structure profiling data, allowing the seamless incorporation of wet-bench structural information from chemical probes and/or ribonucleases to restrain RNA secondary structure prediction via the RNAstructure and ViennaRNA package algorithms. StructureFold performs reads mapping and alignment, normalization and reactivity derivation, and RNA structure prediction in a single user-friendly web interface or via local installation. The variation in transcript abundance and length that prevails in living cells and consequently causes variation in the counts of structure-probing events between transcripts is accounted for. Accordingly, StructureFold is applicable to RNA structural profiling data obtained in vivo as well as to in vitro or in silico datasets. StructureFold is deployed via the [WORKFLOW_PLATFORM].

Availability and Implementation: StructureFold is freely available as a component of Galaxy available at: https://[WORKFLOW_PLATFORM]/ .

Contact: yxt148@psu.edu or sma3@psu.edu

Supplementary information: Supplementary data are available at Bioinformatics online.


## 1 Introduction

RNA plays vital roles in myriad cellular functions, including regulation of transcription, RNA processing and stability, and translation ( Mortimer et al. , [YEAR] ; Sharp, [YEAR] ). The secondary and tertiary structures of RNAs are integral to their biological functions; e.g. as ligand-binding sensors (riboswitches), enzymes (ribozymes) or temperature sensors (RNA thermometers). Therefore, knowledge of RNA structure, especially in vivo , is essential for a mechanistic understanding of RNA function.

Understanding of RNA structure has been greatly advanced through the development of computational approaches for RNA secondary and tertiary structure prediction ( Schroeder, [YEAR] ). Resultant software packages ( Table 1 ) include RNAstructure ( Reuter and Mathews, [YEAR] ), ViennaRNA package ( Lorenz et al. , [YEAR] ), MC-Fold/MC-Sym ( Parisien and Major, [YEAR] ) and SeqFold ( Ouyang et al. , [YEAR] ). Each method has its advantages (cf. Table 1 ), including pseudoknot predictions, local folding, G-quadruplex folding and prediction of 3D structure. Nonetheless, any purely computational RNA structure prediction method has severe limitations due to incomplete knowledge of free energy parameters, RNA interaction with other molecules ranging from ligands to proteins, and kinetically controlled RNA folding. To overcome these limitations, RNA-modifying agents can be used to provide experimental restraints regarding the single- and double-stranded regions of the RNA. For example, critical RNA structural information can be provided using nucleases ( Kertesz et al. , [YEAR] ; Knapp, [YEAR] ; Underwood et al. , [YEAR] ; Zheng et al. , [YEAR] ) such as RNase V1, which cleaves double-stranded RNA sites, and RNase S1, which cleaves single-stranded RNA sites. However, a limitation of such nuclease-based structure probing is that it can only be applied in vitro. RNA structures in vivo can be very different due to protein binding, RNA–RNA interactions, ionic and pH conditions, and other aspects of the cellular milieu such as molecular crowding and the influence of metabolites that are impossible to either completely model in silico or reconstitute in vitro ( [AUTHOR et al.] , [YEAR] ; Zaug and Cech, [YEAR] ).


## Table 1.

Comparison of commonly used software for RNA structure prediction

| Software | Restraint | Algorithm | Special attributes |
| RNAstructure | Structural reactivity/Hard restraint | Thermodynamics | Pseudoknot prediction |
| ViennaRNA Package | Hard restraint | Thermodynamics | Local folding, G-quadruplex prediction |
| MC-Fold/MC-Sym | Semi-hard restraint | Nucleotide cyclic motif | 3D RNA structure prediction |
| SeqFold | Structural reactivity | Sample and select | − |
RNAstructure ( Reuter and Mathews, [YEAR] ); ViennaRNA package ( Lorenz et al. , [YEAR] ); MC-Fold/MC-Sym ( Parisien and Major, [YEAR] ); SeqFold ( Ouyang et al. , [YEAR] )

As an alternative to nucleases, several RNA modifying chemicals, including dimethyl sulfate (DMS; Zaug and Cech, [YEAR] ) and Selective 2′-Hydroxyl Acylation analyzed by Primer Extension (SHAPE) reagents ( Wilkinson et al. , [YEAR] ) can be employed to report the presence of single-stranded nucleotides in RNA and thus provide experimental information on RNA structure. DMS methylates the Watson–Crick N1 position of adenine and N3 position of cytosine when these positions are not engaged in Watson–Crick base pairing or other interactions. SHAPE reagents acylate the 2′-hydroxyl group on the sugar of flexible nucleotides of all four nucleotide types. An advantage of chemical probing methods is that many can be applied in vivo as well as in vitro ( [AUTHOR et al.] , [YEAR] ; Spitale et al. , [YEAR] ; Wells et al. , [YEAR] ; Zaug and Cech, [YEAR] ).

Nuclease-based cleavage truncates the RNA template available for reverse transcriptase (RT), while the above chemical modifications of the RNA halt the reverse transcriptase one nucleotide before the modification ( Ehresmann et al. , [YEAR] ). Both of these effects can be read out as ‘stops’ in reverse transcription using conventional methods based on gel (PAGE) or capillary electrophoresis ( Fig 1 ). Such electrophoresis-based methods, however, only read out this structural information for relatively short segments of individual RNAs and so are low-throughput and incapable of providing transcriptome-wide data.


## Fig. 1.

Electrophoresis-based versus NGS-based RNA structure probing. The left side diagrams the standard electrophoresis-based method, while the right side diagrams the next-generation-sequencing (NGS)-based approach, as exemplified by Structure-Seq. Chemical probe treatment can be in vivo or in vitro ; nuclease treatment is in vitro. Chemical probe treatments usually result in a covalent modification of the RNA that terminates reverse transcription (RT). Nuclease treatment results in cleavage of the RNA (not explicitly illustrated). Green lines indicate several copies of a transcript. Gold indicates 32 P radiolabel. Black, red, and purple lines indicate cDNA. Red lines indicate RT products resulting from imperfect RT processivity; such RT dropoff products will on average be accounted for by comparison to control data produced without nuclease or chemical probe treatment. In the NGS-based readout, purple lines indicate 5′-runoff RT products; although they do not provide information on RT structure stops, inclusion of these reads (as well as red and black reads) in the Structure-Seq method is critical as it allows proper normalization for transcript abundance

Recently, genome-wide methods employing high-throughput sequencing techniques to identify the RT stops resulting from cleavages or chemical modifications have been developed (e.g. Fig 1 ). These methods make it possible to obtain structural information on thousands of RNAs in a single experiment. To date, such studies have been conducted in vitro in yeast ( Kertesz et al. , [YEAR] ), mouse ( Incarnato et al. , [YEAR] ; Underwood et al. , [YEAR] ), Drosophila , C. elegans ( Li et al. , 2012a ), Arabidopsis ( Zheng et al. , [YEAR] ) and human ( Wan et al. , [YEAR] ), and in vivo in Arabidopsis ( [AUTHOR et al.] , [YEAR] ), yeast ( Rouskin et al. , [YEAR] ; Talkish et al. , [YEAR] ) and human cells ( Rouskin et al. , [YEAR] ). Another method, SHAPE-MaP, that relies on mutagenesis rather than RT stops, has been applied in vitro to the HIV-1 RNA genome ( Siegfried et al. , [YEAR] ). We recently reviewed many of these approaches ( [AUTHOR et al.] , [YEAR] ).

While the combination of RNA structure probing with high-throughput sequencing is a major advance in the RNA field, it requires intensive computational efforts to derive the explicit predicted reactivities and secondary structures transcriptome-wide from high-throughput RNA structure profiling data. Some efforts have been made to develop algorithms and implement software tools and webservers to facilitate the data analysis process for high-throughput RNA structure profiling ( Table 2 ), which includes reads mapping, normalization, reactivity derivation and RNA structure prediction ( Aviran et al. , [YEAR] ; Li et al. , 2012b ; Loughrey et al. , [YEAR] ; Siegfried et al. , [YEAR] ; Talkish et al. , [YEAR] ). Here we provide a brief overview of these methods and then indicate the advances provided by StructureFold.


## Table 2.

Comparison of platforms (software) performing analysis on high-throughput RNA structure profiling data (raw sequence)

| Platform | Structural reactivity (# transcripts) | RNA structure prediction | Local install | Webserver |
| Spats | Multiple | No | Yes | No |
| Mod-seeker | Transcriptome-wide | No | Supplementary Data | No |
| SAVoR | Individual | Yes | No | Yes |
| ShapeMapper/SM_folding_pipeline | Multiple | Yes | Yes | No |
| StructureFold | Transcriptome-wide | Yes | Yes | Yes |
Spats ( Loughrey et al. , [YEAR] ); Mod-seeker ( Talkish et al. , [YEAR] ); SaVoR ( Li et al. , [YEAR] , b ); ShapeMapper/SM_folding_pipeline ( Siegfried et al. , [YEAR] ); StructureFold (this study).

Spats ( Aviran et al. , [YEAR] ; Loughrey et al. , [YEAR] ) is a method to derive reactivities from Shape-seq raw data ( Lucks et al. , [YEAR] ) based on maximum likelihood, primarily to solve the problem arising from the signal decay that occurs at the 3′ end of each cDNA read when using a single fixed primer that initiates reverse transcription at the 3′ end of the RNA. Mod-seeker ( Talkish et al. , [YEAR] ) is a method that identifies significantly enriched sites of DMS modification by Cochran–Mantel–Haenszel tests on each transcript and defines structural reactivity as the fold enrichment of RT stops on each nucleotide in the DMS treated library relative to a control library with no DMS treatment. While Spats and Mod-seeker provide methods to derive structural reactivities from high-throughput RNA structure profiling data, Spats focus on reactivity information for individual RNAs, while the structural reactivities provided by Mod-seeker are not directly comparable between different RNAs in a transcriptome. In addition, while these programs calculate reactivities, they do not include the essential step of actual prediction of RNA structures.

SAVoR takes RNA sequences and mapped high-throughput RNA structure profiling data as inputs, and outputs individual RNA structures from the RNAfold program in the ViennaRNA package ( Lorenz et al. , [YEAR] ), either including experimental restraints as derived from mapped high-throughput RNA structure profiling data or without any restraints. The online SAVoR platform is easy to use but it cannot be downloaded and installed locally, and it does not provide an option to output transcriptome-wide RNA structural reactivities or structures, which is crucial for deriving global principles of RNA folding and function.

ShapeMapper and the SM_folding_pipeline software developed in the SHAPE-MaP approach ( Siegfried et al. , [YEAR] ) rely on mutagenesis rather than stops during RT. The programs output structural reactivities as well as predicted RNA structures.

Here we describe our development of StructureFold, a series of software packages that integrates reads mapping, RT stop count calculation, reactivity derivation, and structure prediction in a web-based interface. The two inputs to StructureFold are transcriptome sequence and (optional) high-throughput RNA structure profiling data; the outputs are structural reactivities on each nucleotide transcriptome-wide and the corresponding RNA structures predicted with or without the experimental restraints. By taking into account the differential abundances and lengths of RNAs in a transcriptome, StructureFold provides values of in vivo structural reactivities of nucleotides on different RNAs that are directly comparable. StructureFold is provided as a component of the [WORKFLOW_PLATFORM] ( http://www.[WORKFLOW_PLATFORM] ) and takes advantage of the computational tools available in Galaxy ( Goecks et al. , [YEAR] ), such as Bowtie ( Langmead et al. , [YEAR] ) and SAMtools ( Li et al. , [YEAR] ). StructureFold consists of a series of intuitive modules that are easy to use, either online or after local installation.


## 2 Methods/software implementation

We developed StructureFold as four modules that perform two major functions. The first function employs the first three modules to derive structural reactivities on each nucleotide in a transcriptome based on input of raw sequencing reads. The second function, encompassed in the fourth module, predicts RNA secondary structures transcriptome-wide. StructureFold takes in high-throughput sequencing data from control datasets and from treated datasets consisting of nuclease-based or chemical-based (e.g. DMS or SHAPE) structure probing data and outputs predicted RNA secondary structures in just a few simple steps. Figure 2 provides an overview of how StructureFold works.


## Fig. 2.

StructureFold calculates reactivities from experimental RNA structure profiling data and predicts RNA structures with or without these experimental restraints. StructureFold consists of 4 modules: Iterative Mapping, Get RT Stop Counts, Reactivity Calculation, and RNA Structure Prediction. Circles represent inputs, boxes represent processes, and ovals represent outputs. Outputs of modules that are also inputs for the next module are left as ovals

StructureFold is implemented as follows:

The first module in StructureFold is the Iterative Mapping module. This module maps the raw reads from the sequencer to the reference transcriptome library using Bowtie ( Langmead et al. , [YEAR] ), allowing up to the maximum number of mismatches specified by the user. The two inputs are raw sequencing reads and the corresponding reference library (i.e. the transcriptome or RNA genome of interest), provided as Fasta/Fastq and Fasta files, respectively. Bowtie is used to iteratively map the reads to the reference library. Users can use the −5/−3 flag in Bowtie to remove a user-specified number of nucleotides at the 5′ and/or 3′ end of each read. This process is useful for removing adapter sequence from the read. Users can also use the –v option to set the flag for the number of mismatches allowed while mapping. If a read cannot be mapped, it may be because of internal mismatches between the read and the reference library sequence, or because adapter sequence is included in the read. Accordingly, if a read cannot be mapped, it is trimmed by a user-specified number of nucleotides at the 3′ or 5′ end, and mapping to the reference library is again attempted. The process is iterated until the read either properly maps or is less than the minimum length requirement specified by the user, which typically corresponds to the minimum length required for unique mapping of a read to the reference library. Each successfully mapped read with its mapping location is collected and the information is stored as a .bam file.

The second module in StructureFold is the Get RT Stop Counts module. This module calculates the number of RT stops that map to each nucleotide of each transcript. The inputs are a mapped dataset (in . bam format), typically from the preceding Iterative Mapping module, and the reference library that was used to map the reads, and the output is an RT Stop Counts (RTSC) text file, which contains RT stop counts mapped to each of the four nucleotides (A, C, G, U) in each transcript.

To obtain the number (count) of RT stops for each nucleotide, the mapping location of each RT stop is first considered. For chemical modification, mapping allows identification of the nucleotide immediately 5′ to the RT stop on the RNA, which is the nucleotide that was modified and so receives the stop count. When nucleases are used for structure mapping, the nucleotide that will receive the count according to this procedure is the nucleotide on the 5′ side of the cleavage site on the RNA. The counts of the RT stops of all the nucleotides of each of the RNAs in the experimentally queried transcriptome are combined into a RT termination (stop) count .txt file for each type of library: control and reagent treated. The control library is used to account for background RT stops arising from reverse transcriptase drop off at non-exogenously modified or non-nuclease cleaved sites, which can result from a number of factors including imperfect processivity of the reverse transcriptase, the presence of endogenous RNA modifications, or degradation of the RNA template.

3.The third module of StructureFold is the Reactivity Calculation module. This module calculates reactivity based on the RTSC file generated from the preceding Get RT Stop Counts module.

The Reactivity Calculation module begins with a two-step normalization of the RT stop counts:

Step 1: The RT stop counts on each nucleotide of each mapped transcript in the plus and minus reagent conditions are incremented by 1 and the natural log (ln) is taken of the resultant value. This provides the numerator in Equations (1) and (2) . These raw data are typically skewed, and taking the ln results in a distribution much closer to Gaussian ( Fig 3 ). Incrementing by 1 avoids an undefined value of the natural logarithm if there are zero RT stop counts.

Step 2: The ln of RT stop counts on each nucleotide of each mapped transcript in the plus and minus reagent conditions are normalized by the transcript’s abundance and length. For a transcript, suppose P r ( i ) and M r ( i ) are the raw ‘ r ’ numbers of RT stops mapped to nucleotide i (all four nucleotides are included) on the transcript in the plus (P) and minus (M) reagent libraries, respectively, and l is the length of the transcript. P r ( 0 ) and M r ( 0 ) are the raw numbers of 5′-runoff RT reads (purple-coded reads in Fig 1 ) on the transcript in the plus and minus reagent libraries, respectively. The denominators in Equations 1 and 2 thus represent the abundance normalized by transcript length.


## Fig. 3.

RT stop count distribution on 18S rRNA in the (+) DMS library from [AUTHOR et al.] ([YEAR]) . a. Before ln transformation. b. After ln transformation. The RT stop count distribution is quite skewed before ln transformation and is much closer to a Gaussian distribution after ln transformation

Equation (1) provides the normalized RT stop count for nucleotide i in the plus reagent library.

| P ( i ) = l n [ P r ( i ) + 1 ] ( ∑ i = 0 l l n [ P r ( i ) + 1 ] ) / l | (1) |
Equation (2) provides the normalized RT stop count for nucleotide i in the minus reagent library.

| M ( i ) = l n [ M r ( i ) + 1 ] ( ∑ i = 0 l l n [ M r ( i ) ] + 1 ) / l | (2) |
‘Final structural reactivities’ (FSRs) are then calculated from the normalized RT stop counts in equations 1 and 2 in three steps. First, values of a term denoted ‘raw structural reactivity’ (RSR) are defined. Raw structural reactivities (RSRs) are calculated by subtracting the normalized RT stop count on each nucleotide in the minus reagent library from the normalized RT stop count on each corresponding nucleotide in the plus reagent library. If the value is negative, it is set to zero. Second, 2–8% normalization is applied to the RSRs. In 2–8% normalization, the top 2% of the data are initially removed and the average value of the remaining top 8% of the data is then calculated ( Low and Weeks, [YEAR] ). Then all the data (here, all the RSRs) are divided by this average value to obtain the ‘normalized structural reactivities’ (NSRs). The purpose of this normalization is to convert RSRs into a range that can be used as restraints for RNA structure prediction in RNAstructure and ViennaRNA package. As with SHAPE data ( Deigan et al. , [YEAR] ), this normalization places most reactivities between 0 and 1, with the few reactivities larger than 1 representing highly reactive nucleotides. Third, the NSRs are capped by a user-specified threshold. Capping avoids extremely high structural reactivities, which could introduce bias when investigating meta properties of RNA structural patterns ( Kertesz et al. , [YEAR] ). The resultant values are the ‘final structural reactivities’ (FSRs) for each nucleotide in the transcriptome.

The output from this module (.txt file), which is indicative of the tendency of a nucleotide to be single-stranded, can be used as input for the next module or can be used directly (i.e. without the next module) to carry out meta analyses. For instance, we used FSRs to evaluate periodicity in mRNA reactivity and relationships between FSRs and alternative polyadenylation or alternative splicing ( [AUTHOR et al.] , [YEAR] ).

4. The fourth module of StructureFold is the RNA Structure Prediction module. This module predicts RNA structures using the RNAstructure program (V5.6; http://rna.urmc.rochester.edu/RNAstructure.html ) and ViennaRNA package (V2.1.9). The module can predict RNA secondary structures from sequence data alone, or with inclusion of restraints from structural reactivities as provided by the first three modules. Lastly, the user has the option of creating bar plots to illustrate the distribution of the FSRs of the nucleotides in any transcript specified by the user ( Fig 4 a).


## Fig. 4.

Sample outputs of StructureFold. a. Final structural reactivity (FSR) distribution of AT5G53300.3 (Ubiquitin Conjugating Enzyme 10) used for prediction in panel b. Predicted RNA structure of AT5G53300.3 with in vivo restraints derived from [AUTHOR et al.] ([YEAR]) . c. Predicted RNA structure of AT5G53300.3 (471 nt) in silico (unrestrained)

The RNA Structure Prediction module requires one or more transcript IDs from the reference library as input; these are provided as a .txt file with each ID on one line. StructureFold will find the RNA sequence in the reference library corresponding to the ID provided. If the FSR on each nucleotide of the RNA is provided, the module can output bar plots that illustrate the distribution of the FSRs (generated from the third module) of the nucleotides in any transcript specified by the user ( Fig 4 a). When the FSRs are provided, the module outputs the predicted structures of the RNA with these restraints ( Fig 4 b). Otherwise the module outputs the predicted structures without restraints, i.e. an in silico prediction that does not incorporate any experimental data ( Fig 4 c).

Explicit inputs and outputs for all four modules in StructureFold can be found in the Supplementary Note .


## 2.1 ROC curve generation

ROC curves were generated on regions of 18S and 25S rRNAs for both gel-based and NGS-based readouts. These curves are based on phylogenetic secondary structures, derived by the Gutell lab based on comparative analyses of RNA sequences and their secondary structures ( Cannone et al. , [YEAR] ; http://www.rna.icmb.utexas.edu ). We define a single-stranded nucleotide in the phylogenetic structure as condition positive. We vary a reactivity threshold from 0 to 7 evenly with 15 000 divisions. For a given threshold, each nucleotide with FSR (or normalized gel intensity) that is above the threshold is designated as test outcome positive. We calculate sensitivity (true positive rate) and 1—specificity (false positive rate) at each threshold and use this information to generate the ROC curves.


## 2.2 Gel-based structure probing

In vivo DMS modification was performed on etiolated Arabidopsis seedlings, and the structure probing results were analyzed by gel electrophoresis ( Fig 1 ) as described previously ( [AUTHOR et al.] , [YEAR] ; [AUTHOR et al.] , [YEAR] ). Briefly, the DMS-treated and DMS-untreated (control) RNA were used as the inputs for rRNA structure probing. Approximately 1 µg of total RNA was used for the (+) and the (−) DMS conditions and total RNA was used for dideoxy sequencing. 32 P radiolabelled 18S or 25S rRNA-specific primers were used for the reverse transcription: for 18S region one (5′-AACTGATTTAATGAGCCATTCGCAG-3′), for 18S region two (5′-GAGCCCGCGTCGACCTTTTATC-3′), for 18S region three (5′-GGTAATTTGCGCGCCTGCT-3′), for 25S region one (5′-AAGCGCCATCCATTTTCGG-3′). The labeled cDNA fragments were size fractionated by PAGE and detected using a Typhoon phosphorimager. Gel intensity was quantified using ImageQuant 5.2. Gel-based DMS reactivity was normalized ( [AUTHOR et al.] , [YEAR] ) by 2–8% normalization based on Low and Weeks ([YEAR]) .


## 3 Results


## 3.1 Comparison between structural reactivities and gel-based assay intensities

We used ROC curves to compare the similarity of structural reactivities generated by the NGS-based Structure-Seq method ( [AUTHOR et al.] , [YEAR] ) analyzed via StructureFold to DMS reactivities derived from the classical gel-based method of RNA structure-probing ( Fig 5 ). The Structure-Seq FSRs and normalized in vivo gel-based assay intensities have similar performance on all of the rRNA regions tested, which strongly validates the DMS reactivities generated from StructureFold. The observation that the ROC curves are above the diagonal line of no discrimination indicates that the methods perform much better than random prediction, and the observation that the curves track each other on each of the plots indicates that the two methods have similar performance.

Comparison between Final Structural Reactivities (FSRs) derived by StructureFold ( [AUTHOR et al.] , [YEAR] ) versus gel-based assay in which reactivity is read out as band intensity. a. In vivo DMS treatment was performed on 1 μg of total RNA and analyzed using 32 P radiolabelled 25S rRNA-specific primer (lane 2). A control with no DMS treatment was performed in parallel (lane 1). Dideoxy sequencing was conducted using 1 µg of total RNA (lanes 3–6). The region of 25S rRNA analyzed is nucleotides 1217–1303. b. FSRs derived by StructureFold (red) compared to normalized gel-based assay intensities (blue) on 25S rRNA for nucleotides 1217–1303. R = 0.69. c. ROC curve based on FSRs derived by StructureFold versus gel-based reactivities on 25S rRNA (nucleotides 1217–1303). d–g. ROC curves based on FSRs derived by StructureFold versus gel-based reactivities on 18S rRNA: nucleotides 17–86 (d), 87–207 (e), 298–428 (f), panels d–f combined (g)


## 3.2 Comparison between structural reactivities derived from StructureFold and Mod-seeker

To compare our method of deriving structural reactivities with the previously published method, Mod-seeker, we applied the Mod-seeker approach to our high-throughput structural profiling data on rRNA from [AUTHOR et al.] ([YEAR]) . For Arabidopsis 18S and 25S rRNAs, we observed a high correlation between the structural reactivities derived using StructureFold and those from Mod-seeker [Pearson correlation coefficient (PCC) = 0.91 and PCC = 0.93, respectively]. In addition, as shown in Table 3 , the structural reactivities derived from both programs are consistent with the phylogenetic structures of 18S and 25S rRNA.

Comparison between the structural reactivities derived on Arabidopsis rRNAs using StructureFold or Mod-seeker

| (a) 18S rRNA |
|  | Structural reactivity from StructureFold |
|  | High | High + medium | Low (%) |
| Single-stranded | 86.7% (96.7%) | 75% (92.2%) | 48 |
| Base-paired | 13.3% (3.3%) | 25% (7.8%) | 52 |
|  | Structural reactivity from Mod-seeker |
|  | Significant | Non-significant (%) |
| Single-stranded | 76.8% (93.1%) | 48.7 |
| Base-paired | 23.2% (6.9%) | 51.3 |
| (b) 25S rRNA |
|  | Structural reactivity from StructureFold |
|  | High | High + medium | Low (%) |
| Single-stranded | 78.6% (93.1%) | 70.0% (91.9%) | 44.2 |
| Base-paired | 21.4% (6.9%) | 30.0% (8.1%) | 55.8 |
|  | Structural reactivity from Mod-seeker |
|  | Significant | Non-significant (%) |
| Single-stranded | 70.0% (91.8%) | 45.7 |
| Base-paired | 30.0% (8.2%) | 54.3 |
Number in each cell is the percentage of the nucleotides with the specified level of reactivity that are single-stranded or base-paired in the phylogenetic structure. Number in parentheses is the percentage of the nucleotides with the specified level of reactivity that are single-stranded or positioned either at the end of a helix or adjacent to a helical defect in the phylogenetic structure. Here, types of reactivities are defined as follows: High: reactivity ≥ 0.6; Medium: 0.6 > reactivity ≥ 0.3; Low: 0.3 > reactivity; Significant: Reactivity of significantly enriched sites of DMS modification identified by Mod-seeker; Non-significant: Reactivity of the sites that are not significantly enriched in DMS modification


## 3.3 Sample outputs from StructureFold

In addition to providing FSRs, StructureFold can provide RNA structures in the following two ways:

The RNA Structure Prediction module can predict RNA structures at a user-chosen temperature without the imposition of any restraints. In this case, StructureFold employs RNAstructure ( Reuter and Mathews, [YEAR] ) or ViennaRNA package ( Lorenz et al. , [YEAR] ) with default thermodynamic parameters to predict RNA structures directly from the RNA sequence according to thermodynamics. Candidate structures selected are those with minimum free energy.

StructureFold can take as input experimentally-generated high-throughput RNA structure profiling data to restrain structure prediction. By sequentially employing the preceding Iterative Mapping, Get RT Stop Counts, and Reactivity modules, StructureFold will derive the FSR reactivity for each nucleotide, which is a quantification of the likelihood that the nucleotide is single-stranded.

The RNA Structure Prediction module in StructureFold then predicts RNA structures using these reactivities as restraints. The method converts reactivities into pseudo-free energy terms, or ‘soft restraints’ that are used to adjust the purely model oligonucleotide based thermodynamic free energies ( Turner and Mathews, [YEAR] ; Xia et al. , [YEAR] ) of the candidate structures. Reactivities are used as restraints in an analogous way as previously described for DMS and SHAPE data ( Cordero et al. , [YEAR] ; Deigan et al. , [YEAR] ). After our own assessment ( Supplementary Table S1 ), we opted to use the same slope and intercept parameters for StructureFold as those used by Hajdin et al. ([YEAR]) . The corresponding equation is:

| Δ G ( i ) = 1.8 l n [ Reactivity( i ) + 1 ] − 0.6 (in kcal mol − 1 ) | (3) |
where ‘ i ’ is the i th nucleotide in a given transcript.

StructureFold outputs include the RNA structure predicted with and without restraints and a bar plot that illustrates the per nucleotide reactivity of the RNA ( Fig 4 ). It is evident from Figure 4 that this RNA structure predicted with restraints is quite different from that predicted without restraints, an observation that is generally true ( [AUTHOR et al.] , [YEAR] ) and highlights the importance of experimentally-derived restraints.


## 4 Discussion

StructureFold is the first computational platform designed specifically for transcriptome-wide RNA structure mapping and reconstruction. In addition to enabling transcriptome-wide prediction of RNA secondary structures in silico (unrestrained), StructureFold can output FSRs that can then be used for transcriptome-wide prediction of experimentally-restrained RNA structures. In the future, we anticipate StructureFold outputs being used to assess and compare the restrained predictions resulting from RNA structure profiling data generated by numerous experimental methods, including nuclease, SHAPE, DMS, and other chemical probing agents ( Kwok et al ., [YEAR] ).

StructureFold has several advantages over other software platforms for analysis of RNA structure ( Table 2 ). Compared to SAVoR ( Li et al. , 2012b ), StructureFold outputs transcriptome-wide structural reactivities on each nucleotide, allowing investigation of global structural patterns. Compared to Spats ( Aviran et al. , [YEAR] ) and Mod-seeker ( Talkish et al. , [YEAR] ), StructureFold predicts RNA structures in addition to deriving structural reactivities. In contrast to Mod-seeker, StructureFold takes the abundance of transcripts into consideration and thus can be used for comparative analyses of in vivo as well as in vitro high throughput RNA structure data within and between transcriptomes. Compared to ShapeMapper, StructureFold provides a user-friendly online platform where high-throughput data probing RNA structures can be analyzed directly.

StructureFold is straightforward to use online or to install for local use on UNIX systems. Through incorporation into the [WORKFLOW_PLATFORM], StructureFold takes advantage of the computational infrastructure and tools, as well as the ongoing curation provided by Galaxy ( Goecks et al. , [YEAR] ). For example, outputs from read mapping algorithms in Galaxy such as Bowtie ( Langmead et al. , [YEAR] ) and BWA ( Li and Durbin, [YEAR] ) directly provide the input to the Get RT Stop Counts module of StructureFold.

In the future, StructureFold could be extended in several ways:

(i) Methods for reads trimming

StructureFold employs iterative mapping to remove adapter sequences; this method uses the exact biological sequence to identify the presence of adapter sequence but requires more computational time. The cutadapt program ( Martin, [YEAR] ) is commonly used to remove adapter sequence but has difficulty to identify the adapter sequence if only a small portion of the adapter is present. Iterative mapping and cutadapt could possibly be integrated.

(ii) More options to derive reactivities from RT stop count files

Currently, three experimental approaches have been applied for in vivo transcriptome-wide profiling of RNA structure: Structure-Seq ( [AUTHOR et al.] , [YEAR] ), Mod-seq ( Talkish et al. , [YEAR] ) and DMS-seq ( Rouskin et al. , [YEAR] ). Each approach has its advantages and limitations. For example, StructureFold takes the transcript abundance into account and avoids skewness of the raw number of RT stops by ln transformation but it is still susceptible to experimental noise to some extent, especially on low-abundance RNAs. RNAs with low abundance have fewer RT stops mapped in total, and so are proportionately more affected by stops resulting from drop off of the RT primer. One way to compensate for this is simply to obtain more reads. Mod-seeker ( Talkish et al. , [YEAR] ) is more resistant to experimental noise than StructureFold because it identifies significantly enriched sites of DMS modification before deriving the final DMS reactivity. Mod-seeker and StructureFold have very similar performance on deriving structural reactivities of individual rRNAs as shown in Table 3 ; however, DMS reactivities derived by Mod-seeker on different transcripts are not directly comparable because each nucleotide in a library is normalized by the same value, which does not take into account differences in transcript abundance. DMS-Seq ( Rouskin et al. , [YEAR] ) normalizes RT stops mapped to each position proportionally to the most highly reactive base within a given structured window (50–200 nucleotides in length). The method avoids local bias of the RT stops on each RNA, but the length of the window is fairly arbitrary ( Aviran and Pachter, [YEAR] ). Moreover, local region normalization assumes independence of the different regions of the transcript, which is not always a valid assumption ( Behrouzi et al. , [YEAR] ; Strulson et al. , [YEAR] ). In the future, StructureFold could be expanded to provide options for users to choose among methods of reactivity calculation.

(iii) More alternatives for predicting RNA structures

StructureFold employs the free energy minimization program in RNAstructure ( Reuter and Mathews, [YEAR] ) or the ViennaRNA package ( Lorenz et al. , [YEAR] ) to predict RNA structures. Both RNAstructure and ViennaRNA predict RNA structures according to thermodynamic parameters (Turner Rules) measured on model oligonucleotides and provide the candidate structures with the lowest free energy. RNAstructure is able to use the experimentally-derived reactivities as soft restraints, which improves the accuracy of the prediction. By contrast, the ViennaRNA package incorporates the experimental data only as hard restraints for RNA structure prediction. Hard restraints are digital (0/1) restraints that designate each nucleotide to be base-paired or non-base paired, which may result in less accurate structure prediction than the use of soft restraints. The ViennaRNA package uniquely allows local folding (RNALfold) and G-quadruplex prediction, which are advantageous for some applications.

MC-Fold/MC-Sym ( Parisien and Major, [YEAR] ), another commonly used RNA structure prediction package, can also use restraints for structure prediction, wherein the user must designate the reactivity for each nucleotide as high, low or medium. MC-Fold uses a knowledge-based scoring function rather than thermodynamics for 2D RNA structure prediction, and MC-Sym is further able to predict the 3D structures of the RNAs based off the 2D MC-Fold structures. In the future, incorporation of MC-Fold and MC-Sym algorithms as choices in StructureFold could provide additional information on individual RNA structures.

We believe that StructureFold is well-suited for use by any scientist interested in generating and analyzing high-throughput RNA structure profiling data. Given the current rapid development of the RNA structure field, the user-friendly nature of the StructureFold platform, and the plentiful computational resources available on the [WORKFLOW_PLATFORM], StructureFold will facilitate genome-wide RNA structure prediction by both experimentally-focused and computationally-focused groups.


## Supplementary Material

We thank the [INSTITUTION_REDACTED] Galaxy team for advice on software development, Prof. Dave Mathews for advice on the manuscript, Dr. Alex Spasic and Mr. Lin An for testing StructureFold implemented in Galaxy, and Prof. Joel McManus for assistance with Mod-seeker comparisons.
