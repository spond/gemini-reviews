# De-Identified Manuscript: AN_ANON_039

> **Blinding Note:** All title, author, affiliation, journal, year, software, and identifier metadata have been scrubbed for unbiased methodological review.

## Abstract

## Jennifer [AUTHOR]


## Dave [AUTHOR]


## Daniel [AUTHOR]


## James Taylor


## Anton [AUTHOR]


## Abstract

Innovations in biomedical research technologies continue to provide experimental biologists with novel and increasingly large genomic and high-throughput data resources to be analyzed. As creating and obtaining data has become easier, the key decision faced by many researchers is a practical one: where and how should an analysis be performed? Datasets are large and analysis tool set-up and use is riddled with complexities outside of the scope of core research activities. The authors believe that Galaxy provides a powerful solution that simplifies data acquisition and analysis in an intuitive Web application, granting all researchers access to key informatics tools previously only available to computational specialists working in Unix-based environments. We will demonstrate through a series of biomedically relevant protocols how Galaxy specifically brings together (1) data retrieval from public and private sources, for example, UCSC's Eukaryote and Microbial Genome Browsers, (2) custom tools (wrapped Unix functions, format standardization/conversions, interval operations), and 3rd-party analysis tools.

Keywords: Galaxy, comparative genomics, genomic alignments, Web application, genome variation


## Introduction

Most experimental biologists cannot fully take advantage of genomic data due to a formidable wall of countless and unnecessary computational issues. The goal of Galaxy ( [AUTHOR et al.], [YEAR] ; Goecks et al., [YEAR] ) is to solve these issues. Consider the following example: a researcher wants to identify protein-coding exons containing the highest density of SNPs. Most biologists know three primary sources of genome-wide data for vertebrates: Entrez at the National Center for Biotechnology Information (NCBI; UNIT 1.3 ; Maglott et al., [YEAR] ), the Genome Browser at the University of California at Santa Cruz ( unit 1.4 ; Karolchik et al., [YEAR] ; Schneider et al., [YEAR] ; Rosenbloom et al., [YEAR] ), and Ensembl ( unit 1.15 ; Birney et al., [YEAR] ) at the EBI/Wellcome Trust Sanger Institute (U.K.). Although these three sources offer extensive information about genes, including genomic structure, gene expression profiles, and SNPs, the end user must still perform this task elsewhere—the listed resources do not provide functionality necessary to perform this analysis. Typically, the project ends up in the hands of a graduate student who might initially try to achieve the analysis using popular desktop applications. Unfortunately, Excel (like many other desktop applications) cannot handle that much data. As a result, this relatively simple task becomes a complex endeavor that may easily take weeks or months. In the authors' view, this does not have to be complicated. Galaxy bridges the gap between data and analyses by allowing experimental biologists without programming experience to easily perform large-scale studies from within their Web browsers.

In this unit, the authors describe the functionality of Galaxy using a series of examples that correspond to the following protocols. Basic Protocol 1 covers the most fundamental features of Galaxy. Basic Protocol 2 elaborates on different types of data accepted by Galaxy. It also shows the user how to upload data and set data attributes. Basic Protocol 3 demonstrates analysis with ChIP-seq high throughput sequencing data. Basic Protocol 4 shows that manipulation of genomic intervals is one of Galaxy's greatest strengths. Basic Protocol 5 explains how Galaxy enables users to manipulate multiple alignments.

In addition, a fully interactive supplement titled “Using Galaxy to Perform Large-Scale Interactive Data Analysis: A live supplement” is available on the main public [WORKFLOW_PLATFORM] under Shared Data: Published Pages: Using Galaxy [YEAR], at http://[WORKFLOW_PLATFORM]/u/[WORKFLOW_PLATFORM]/p/using-galaxy-[YEAR] . For each protocol, the input datasets, a complete history, and any workflows are included along with the exact methods and a screencast (video tutorial). These items can be examined, copied, rerun, and modified at the main public [WORKFLOW_PLATFORM] ( http://[WORKFLOW_PLATFORM] ) and downloaded for use in a local or cloud instance ( http://getgalaxy.org ).


## Basic Protocol 1


## Finding Human Coding Exons with Highest SNP Density

Suppose one wants to find the top hundred protein-coding exons in the human genome with the highest density of single nucleotide polymorphisms (SNPs). Answering this question is not trivial. To do so, one needs to compare all human exons to all human SNPs. To put this into perspective, the current version of the human genome at UCSC for hg19 includes over 350,000 known coding exons and dbSNP build 134 ( Sherry et al., [YEAR] ) contains nearly 49 million SNPs. Galaxy is specifically designed to make such large-scale analyses fast and user-friendly. Galaxy's interface is accessible from http://[WORKFLOW_PLATFORM] . In the following protocol, the authors will use RefSeq ( Karolchik et al., [YEAR] ; Pruitt et al., [YEAR] ) exons and dbSNP annotations on chromosome 22 extracted from the UCSC Table Browser ( Fujita et al., [YEAR] ).

An Internet-connected computer

Internet browser that supports JavaScript (e.g., most current browsers such as Mozilla Firefox, Safari, Opera, Chrome, or Microsoft Internet Explorer)

After registering, you will be automatically logged in. For subsequent sessions, log in using your e-mail and password. Hover over User in the top menu and click Login in the submenu.

Click the Get Data link at the top of the Tools panel.

In the Tools panel, click Get Data, and then UCSC Main under it.

Click Operate on Genomic Intervals in the Tools panel.

Click Statistics in the Tools panel.

Galaxy interface contains four areas: the top bar, Tools panel (left column), detail panel (middle column), and History panel (right column). The top bar contains user account controls as well as help and contact links. The left panel lists the analysis tools and data sources available to the user. The middle panel displays interfaces for tools selected by the user. The right panel (the History panel) shows datasets and the results of analyses performed by the user. Pictured here are four history items in two different stages of completion: The two “FASTQ Groomer” items are yellow, meaning they are in progress, while the two “ungroomed” items are shown in green, meaning they have completed successfully. Every action by the user generates one or more new history items, which can then be used in subsequent analyses, downloaded, or visualized. For the color version of this figure go to http://www.currentprotocols.com/protocol/bi1005 .

Uploading a list of protein-coding exons (in BED format) of known human genes from the UCSC Table browser involves two steps ( A and B ) described in the text.

When a job is queued, a history item is initially gray. When a job is running, a history item is yellow. When a job is complete, a history item is green (successful) or red (error). For the color version of this figure go to http://www.currentprotocols.com/protocol/bi1005 .

Close up of Galaxy history item. Clicking on links and icons triggers the following events: eye = shows a preview of the dataset in Galaxy's middle panel; pencil = open metadata editor. This brings up an interface in the middle panel of the Galaxy screen that allows one to edit the attributes of the current history item. For example, one may wish to give the history item a more descriptive name or change column assignments (see Basic Protocol 2); × = delete item from the history (To undelete or permanently delete, use the history's Options menu and select “View deleted datasets”.); “save” = copy dataset to your computer; “i” = view details about this dataset in center panel, including the dataset(s), if any, that it was generated from; “rerun” = display this tool in center panel with the same settings it was run with, allowing this step to be exactly rerun or to be modified and rerun; “tags” = add free text tags to this dataset; “sticky note” = add free text annotation. Finally, if the dataset can be visualized in a browser, links to the Galaxy Track Browser (stacked bars icon) and to UCSC, GeneTrack, Ensembl, and others will also be displayed.

The “Edit Attributes" form in the center panel. Each attribute can be modified and saved. In this figure, the system-generated name has been copied to the Info field, and a short descriptive name entered in the Name field.

Data manipulation tools: Join ( A ), Count ( B ), Sort ( C ), Select first lines ( D ), and Compare two datasets ( E ).

Result of joining two interval datasets, highlighting a single exon that contains (overlaps with) 4 SNPs.


## Basic Protocol 2


## Loading Data and Understanding Datatypes

In Galaxy, information is stored in “datasets”, which are analogous to files. Datasets can be added to your history by uploading files from your computer, or extracting from external data sources integrated with Galaxy such as UCSC's ENCODE datasets ( [AUTHOR et al.], [YEAR] ; Raney et al., [YEAR] ). Transferring external data via http/ftp, copying from shared or public Galaxy histories and libraries, and running data manipulation and analysis tools within Galaxy are explained. In addition to their data contents, each Galaxy “dataset” is associated with “metadata”. Metadata is information that describes the characteristics of a dataset. These can include the assigned and given names/annotation, the associated reference genome and build, the format datatype, and, frequently, additional datatype-specific labels and definitions.

In this protocol, we demonstrate how metadata are assigned and modified for common genome analysis datasets uploaded into Galaxy using the methods listed above. We also use Galaxy to transform a dataset from a custom format into a standard BED format.

An Internet-connected computer

Internet browser that supports JavaScript (e.g., most current browsers such as Mozilla Firefox, Safari, Opera, Chrome, or Microsoft Internet Explorer) and an FTP client, such as FileZilla

Return to the main Galaxy interface by going to the URL http://[WORKFLOW_PLATFORM] .

Create a new history. In the History panel, click on Options and select Create New.

Name the new history by clicking on the text Unnamed History and entering Basic Protocol 2 .

The data library ChIP-Seq Mouse Example is imported from a library into a history.

Filezilla ( http://filezilla-project.org ) is one example of a desktop FTP client that works well with Galaxy.

Get Data: Upload File tool. After a file has been uploaded using FTP, it appears in the “Files uploaded via FTP” section.

The Cut tool form and parameter options to select a single column (number 2, or “c2”) from a tab-delimited dataset.

Edit Attributes form in center panel, showing default metadata attributes assigned for the Interval format dataset.

Diagram of the columns “Cut” from the Interval formatted dataset to create a BED formatted dataset. The result “BED6” format contains the six fields: chromosome, start (0-based), end, name, score, and strand.


## Basic Protocol 3


## Calling Peaks for ChIP-seq Data

The decreasing cost and increasing throughput of sequencing technologies has made chromatin immunoprecipitation followed by sequencing (ChIP-seq) an essential tool for genome-wide profiling of protein-binding, histone modification, and nucleosome positioning ( Park, [YEAR] ; Pepke et al., [YEAR] ). There are numerous tools for various stages of ChIP-seq analysis, and this protocol will focus on the use of MACS (Model-based Analysis of ChIP-Seq; Zhang et al., [YEAR] ) to perform peak calling that identifies regions of the mouse genome that are positive for zinc-finger CTCF tags versus a control. CTCF is a transcription factor that can function as either a repressor or activator. Though known to bind to several thousand different genomic locations, it has also been experimentally associated with cancer tumors including, but not limited to, testis, prostate, lung, and breast ( Phillips and Corces, [YEAR] ). This protocol begins with FASTQ Tag and Control datasets that are groomed (using FASTQ Groomer, a Galaxy tool that normalizes quality scores and FASTQ formatting; [AUTHOR et al.], [YEAR] ) and mapped (using Bowtie, a DNA short read aligner; Langmead et al., [YEAR] ), and ends with peak calling by MACS.

An Internet-connected computer

Internet browser that supports JavaScript (e.g., most current browsers such as Mozilla Firefox, Safari, Opera, Chrome, or Microsoft Internet Explorer)

Results from Basic Protocol 2, step 4 (see for sources, methods, and references).

Datasets: Main Galaxy public instance http://[WORKFLOW_PLATFORM]

Shared Data: Data Library: ChIP-Seq Mouse Example

(both created or imported by user)

The Copy History form. The Source History on the left side of the center panel is the prior history from Basic Protocol 2. The Destination History on the right side of the center panel in the new history for Basic Protocol 3.

The FASTQ Groomer tool form in the center panel with input-data specific quality score type option selected.

The Bowtie tool form in the center panel with appropriate options selected. The highlighted parameters are those that are configured differently than the tool's default options.

View of MACS tool form in the center panel with the appropriate options selected. The highlighted parameters are those that are configured differently than the tool's default options.

History result datasets and HTML report detail produced by the MACS run.


## Basic Protocol 4


## Compare Datasets using Genomic Coordinates

The protocol describing finding human exons with highest SNP density (Basic Protocol 1) used the join operation to find all protein-coding exons that contain SNPs. This is just one of many interval operations offered in Galaxy, which are based on the bx-python package ( [BITBUCKET_REPO_REDACTED] ) developed at [INSTITUTION_REDACTED] University and Emory University. These include intersect, subtract, complement, merge, concatenate, cluster, coverage, base coverage, and join. Some operations are analogous to relational database queries, such as join and coverage ( UNIT 9.2 ). Other operations are analogous to set operations. Figures 10.5.19 and 10.5.20 show examples of input and output produced by individual interval operations. In the following protocol, the authors use two human chromosome 22 annotation datasets as examples. The first dataset, Exons, representing protein-coding exons, is imported from the “Basic Protocol 1” history. The second dataset “Repeats”, representing interspersed repeats (also known as transposable elements or simply repeats in the text), is retrieved from the UCSC Table Browser.

Graphical explanation showing input and output datasets for several interval operations, including ( A ) Overlapping intervals, ( B ) Overlapping pieces of intervals, ( C ) Intervals with no overlap,( D ) Non-overlapping pieces of intervals, ( E ) Concatenated intervals, ( F ) Merge.

Examples highlighting the functionality of coverage tools.

An Internet-connected computer

Internet browser that supports JavaScript (e.g., most current browsers such as Mozilla Firefox, Safari, Opera, Chrome, or Microsoft Internet Explorer)

Create a new history. In the History panel click on Options and select Create New.

Name the new history by clicking on the text Unnamed History and entering Basic Protocol 4 .

Refresh the History panel and use the pencil icon (see Fig. 10.5.4 ) to change the name of the new dataset to Exons on the Edit Attributes form, as shown in Figure 10.5.5 .

Graphical explanation of the ( A ) Complement, ( B ) Find clusters, and ( C ) Merge clusters interval tools.

Graphical explanation of genomic interval Join operations in Galaxy. ( A ) Only records that are joined, ( B ) All records of the first dataset, ( C ) Only records of second dataset, and ( D ) All records of both datasets. ( E ) Shows how all 4 variations are implemented on two small datasets.


## Basic Protocol 5


## Working with Multiple Sequence Alignments

Galaxy includes several tools to specifically work with paired and multiple sequence alignment format (MAF) datasets. The tool functions can upload, extract, and summarize the content of MAF datasets sourced from the UCSC Browser with the goal of maximizing analytical access to the underlying data. Both custom and standard MAF datasets can be uploaded and used with the majority of tools. The MAF manipulation tools used in this protocol were developed by the Galaxy team ( [AUTHOR et al.], [YEAR] ).

Part A of this protocol will demonstrate how to extract regions from a standard Conservation MAF reference track (hg19), based on the query interval ranges from Basic Protocol 1, step 20: top 100 SNP containing human coding exons on chromosome 22.

Part B of this protocol will demonstrate how to generate coverage statistics from a standard Conservation MAF reference track (hg19), based on the query interval ranges from Basic Protocol 1, step 20: top 100 SNP containing human coding exons on chromosome 22.

Part C of this protocol will demonstrate how to extract and manipulate syntenic “transcript” FASTA sequence from a standard Conservation MAF reference track (hg19), based on the query interval ranges from a human RefSeq Genes track, as extracted in BED format from the UCSC Table Browser, limited to chromosome 22.

An Internet-connected computer

Internet browser that supports JavaScript (e.g., most current browsers such as Mozilla Firefox, Safari, Opera, Chrome, or Microsoft Internet Explorer)

Results from Basic Protocol 1, Step 20 (see for sources, methods, and references):

SNP Coding Exons chr22

(created or imported by user)

UCSC Browser tracks for Conservation and RefSeq Genes:

Conservation 46-way multiZ track for hg19

(local on Main Galaxy public instance http://[WORKFLOW_PLATFORM] )

RefSeq Genes hg19 chr22

(imported by user into Galaxy history)

Workflow: Main Galaxy public instance http://[WORKFLOW_PLATFORM]

Shared Data: Published Workflows

Transform ‘Stitch Gene blocks’ FASTA blocks to standardized FASTA file (imported by user)


## Part A: Tool “Extract MAF blocks given a set of genomic intervals”

3. Extract conserved MAF blocks for primate species.

| Human | Homo sapiens | Feb. [YEAR] hg19/GRCh37 |
| Chimp | Pan troglodytes | Mar. [YEAR] panTro2 |
| Gorilla | Gorilla gorilla gorilla | Oct. [YEAR] gorGor1 |
| Orangutan | Pongo pygmaeus abelii | July [YEAR] ponAbe2 |
| Rhesus | Macaca mulatta | Jan. [YEAR] rheMac2 |
| Baboon | Papio hamadryas | Nov. [YEAR] papHam1 |
| Marmoset | Callithrix jacchus | June [YEAR] calJac1 |
| Tarsier | Tarsius syrichta | Aug. [YEAR] tarSyr1 |
| Mouse lemur | Microcebus murinus | Jun. [YEAR] micMur1 |
| Bushbaby | Otolemur garnettii | Dec. [YEAR] otoGar1. |
Extract MAF blocks tool form highlighting a subset of the tool options.

Result file produced by the Extract MAF blocks tool. Data are the MAF alignment blocks corresponding to the query interval ranges.


## Part B: Tool “MAF Coverage Stats Alignment coverage information”

MAF Coverage Stats tool form highlighting the tool options.

Result file produced by the MAF Coverage Stats tool using the option Coverage by Region. Data are counts for covered and not covered query bases that represent predicted evidence of conservation between the two species.

Result file produced by the MAF Coverage Stats tool using the option Summarize Coverage. Data has three columns: species, nucleotides, and coverage, where coverage is defined as number of nucleotides divided the by the total length of the provided intervals.


## Part C: Tool “Stitch Gene blocks given a set of coding exon intervals”

| Rhesus | Macaca mulatta | Jan. [YEAR] rheMac2. |
Click on Convert Formats in the left Tool panel to expand the list.

Click on Convert Formats in the left Tool panel to expand the list.

Click on “FASTA manipulation” in the left Tool panel to expand the list.

Result file produced by the Fetch Alignments: Stitch Gene blocks tool. Gapped bases are represented by the symbol “-”. It is expected that some MAF blocks will contain results with sequence, sequence plus gaps, or gaps only. Large gaps in the query or target genome may be interpreted as a region that is not well conserved. Input type should be carefully evaluated when choosing a MAF (or any) tool. The complete absence of sequence in the input query (as in the case of a non-coding RefSeq Gene, represented in the second block of this example) produces no results (sequence or gaps) in the output. As the Stitch Gene blocks tool is specifically designed to extract and stitch coding regions from the query input BED file, this is the correct result. To perform a similar function as Stitch Gene block for non-coding genes, the tool Stitch MAF blocks would be a better choice.

Shared Data: Published Workflows on the Main [WORKFLOW_PLATFORM] at [WORKFLOW_PLATFORM] with the features for an individual workflow highlighted: Name (of workflow), Annotation (free text), Owner (Galaxy user name), Community Rating, Community tags (searchable keywords), Last Updated.

Detailed view of an individual workflow's steps with the “Import workflow" link highlighted.

Your workflows page listing the newly imported workflow with the action menu highlighted. Menu selections: Edit, Run, Share or Publish, Download or Export, Clone, Rename, and Delete.

A workflow that is selected to Run is displayed as a form in the center panel. User-specified input selections from the current history are made by using a step's pull-down menu, as highlighted.

Confirmation display when a workflow is executed (started) successfully. As the workflow is run, individual datasets produced by the workflow steps/jobs will be independently colored as gray (waiting to run), yellow (running), green (successful), and red (error). Note that all steps in the workflow are listed, including steps that produce hidden datasets. For the color version of this figure go to http://www.currentprotocols.com/protocol/bi1005 .

Tools can sometimes produce datasets that no longer should be assigned to the current (or any single) reference genome. Use the Edit Attributes form to assign/reassign a new reference genome (see Figure 10.5.37 ) or to unassign a reference genome (as shown) by selecting the menu title (interpreted as a “null" database) from the list.

Filter tool form showing options, with the filter expression box highlighted containing a free text string. This specific filter string is designed to remove species rows that have no conserved genome sequence in the output of the Fetch Alignments: Stitch Gene blocks tool.

Select tool form showing options, with the select expression box highlighted containing a free text string. This specific select string is designed to extract lines from a file that start with “rheMac.”.

Tools can sometimes produce datasets that no longer should be assigned to the current (or any single) reference genome. Use the Edit Attributes form to assign/reassign a reference genome (as shown, in this case rheMac2) or to unassign a reference genome (see Figure 10.5.34 ).


## Guidelines for Understanding Results

Galaxy was designed to be an interactive system, and in most cases results will be self-descriptive, depending on which tools were applied to the original data. As always, caution should be used when interpreting genomic data—the information produced by Galaxy is only as good as the underlying data imported.


## Commentary


## Background Information

Modern Web-based genomic resources offer many facilities for retrieval and visualization of data. However, few of these resources offer sophisticated tools for further analysis of these data. As a result, almost every experimental biologist has to analyze data on his/her own, struggling with numerous difficulties arising from format incompatibility or incomprehensible user interfaces. Although our computational colleagues are happy to help, few are willing to devote time and resources to develop a good user interface (a significant challenge). Galaxy is a system designed to help both sides. For experimental biologists, Galaxy provides an intuitive user interface offering a direct connection to many widely used data sources and browsers, a simplified FTP data-loading procedure, and a custom genome option for most tools including the native Galaxy Track Browser (GTB, or Trackster ). The Galaxy workspace includes a unique history system to organize, label and display data, to track datasets and analysis for sharing and/or publishing, and to extract analysis functions into workflows for re-use. For computational biologists, Galaxy provides a framework that can integrate command-line tools with almost no effort. For each tool, Galaxy generates an interface and provides all housekeeping (e.g., input and output management, job control, error catching, and testing facilities). As this text was compiled with experimental biologists in mind, it does not contain any information on technical aspects of the [WORKFLOW_PLATFORM] (found at http://[WORKFLOW_PLATFORM] ).


## Critical Parameters and Troubleshooting

Galaxy allows performing an infinite number of analyses on genomic data. In designing the system, the authors tried to put as few constraints on the user as possible. In that sense Galaxy is similar to a car with a manual gearbox—it gives you more control if you know what you are doing (e.g., you do not shift from fifth to reverse). Fortunately, user feedback provides convincing evidence that a short test drive is sufficient to understand how Galaxy works. This text is equivalent to such a test drive. Below, the authors list the most common problems encountered by Galaxy users. They can be condensed into two categories: (1) data format issues and (2) genome build incompatibilities.

Galaxy “understands” several datatypes including genomic coordinates (e.g., BED, GFF/GTF, Wig), sequences (e.g., FASTQ, FASTA), and alignments (e.g., SAM/BAM and MAF). Most of the tools require data to be in one of these formats. For example, the genomic intervals operations described in Basic Protocol 4 can only be performed on data in interval format. In most cases, changing your data to interval format is as simple as correctly setting metadata, as shown in Basic Protocol 2, step 6.

Galaxy supports interactive genome analyses that use a mix of different genomes within a single analysis space (History). In the authors' opinion, such “mixing” is essential for a true comparative genomics resource. The ease of mixing also means that, in some cases, users will accidentally attempt comparing data from different genomes. Thus, when using tools that operate on more than one history item (i.e., most genomic interval operations), make sure that all data come from the same genome build.

Galaxy has a vibrant and growing user and developer community. If you want to learn more or encounter problems, the best places to find out how to get connected are in the Galaxy Wiki ( http://[WORKFLOW_PLATFORM] ), specifically our Learning Hub ( http://[WORKFLOW_PLATFORM]/Learn ) and Support Resource ( http://[WORKFLOW_PLATFORM]/Support ) pages.

A vision for Galaxy was originally articulated by Ross Hardison, who is also the major source of support and critical feedback. The authors would like to thank Jim Kent and David Haussler for their continuing support and making UCSC Genome Browser uplink and connection possible. Ist-van Albert pioneered initial aspects of Galaxy design. Efforts of the Galaxy Team (Enis Afgan, Guru Ananda, Dannon Baker, Nate Coraor, Jeremy Goecks, Greg Von Kuster, Ross Lazarus) were instrumental in making this work happen. The following individuals also contributed to the [WORKFLOW_PLATFORM] at different stages: Richard Burhans, Ramkrishna Chakrabarty, Laura Elnitski, Belinda Giardiane, Bob Harris, Jianbin He, Kanwei Li, Webb Miller, Cathy Riemer, Kelly Vincent, and Yi Zhang. Robert Castelo, France De-noeud, Roderic Guigo, Erika Kvikstad, Julien Lagarde, and Kateryna Makova provided critical comments during software testing. Ramana Davuluri gave permission to use the MPromDB data in these protocols. This work was funded by an NIH grant GM07226405S2 to KDM, a Beckman Foundation Young Investigator Award to AN, NSF grant DBI 0543285 and NIH grants HG004909 and HG006620 to AN and JT, NIH grants HG005133 and HG005542 to JT and AN, as well as funds from [INSTITUTION_REDACTED] University and [INSTITUTION_REDACTED] Institute for Cyber Science and the Huck Institutes for the Life Sciences to AN and from Emory University to JT. Additional funding is provided, in part, under a grant with the Pennsylvania Department of Health using Tobacco Settlement Funds. The Department specifically disclaims responsibility for any analyses, interpretations, or conclusions.
