# De-Identified Manuscript `OOD_ANON_35`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Drug–target interaction (DTI) prediction is a critical task in drug discovery. However, the differences in size between drugs and proteins present significant challenges in accurately predicting binding sites. Additionally, the issue of modality imbalance, which arises from modality learning biases, undermines the contribution of multimodal representations to DTI prediction. To address these challenges, we propose DDGR-DTI, which is based on an innovative D ecoupled D ual- G ranularity Framework and a R ebalanced pyramid network (RPN). This framework divides the DTI task into two levels of granularity. The macro level, which decomposes it into subtasks based on modality, and the micro level further decomposes the representation within each subtask. Furthermore, the dual-stream attention module is utilized to perform fine-grained substructure-level interactions within each subtask, thereby enabling accurate identification of binding sites. Simultaneously, we employ an RPN, which effectively alleviates the bias towards the dominant modality in multimodal fusion through a hierarchical aggregation mechanism, emphasizing the synergistic advantages brought by modality balance. Benchmark results demonstrate that DDGR-DTI outperforms existing state-of-the-art models in both prediction performance and generalization ability.

Availability : The source code and dataset can be found at [GITHUB_REPO_REDACTED] .

Keywords: drug–target interaction, drug discovery, decoupled dual-granularity, rebalanced pyramid network


## Introduction

Drug discovery is typically both costly and time-consuming, and accurate prediction of drug–target interactions (DTIs) has emerged as a pivotal step in streamlining this process, reducing development expenses, and increasing success rates [ 1 , 2 ]. Traditional computational approaches, such as molecular docking [ 3 ] and molecular dynamics simulations [ 4 ], can accurately predict DTIs. However, they require specialized knowledge of molecular spatial structures and rely heavily on substantial computational resources. In addition, these methods often suffer from low throughput, which limits their applicability in large-scale screening scenarios. These limitations have prompted researchers to explore more efficient and scalable prediction strategies.

Deep learning methods have demonstrated immense potential in drug discovery [ 5 ], significantly reducing screening time and computational costs. These methods achieve this by efficiently filtering out irrelevant molecules from large biological databases. Unlike traditional approaches, deep learning models excel at feature representation, enabling them to learn underlying patterns in drug and protein molecules. This ability is crucial for accurately predicting their interaction relationships. Current research in this field can be broadly categorized into three main approaches.

The first category of methods for DTI prediction is a sequence-based approaches, which utilize the SMILES strings of drugs and the amino acid sequences of proteins as input to automatically extract features and model interactions, reducing the reliance on predefined descriptors [ 6 ]. Early works, such as DeepDTA [ 7 ] and DeepConv-DTI [ 8 ], demonstrate the effectiveness of sequence-based models in predicting drug–target binding. To further enhance prediction accuracy, advanced techniques such as Transformer [ 9 ] and LSTMs [ 10 ] have been integrated. For instance, HyperAttentionDTI [ 11 ] introduces an attention mechanism to capture complex interactions, improving model interpretability. Similarly, DeepCDA [ 12 ] enhances DeepDTA by adding both LSTMs and an attention mechanism, improving performance on datasets with varying marginal distributions. However, relying solely on sequence information is insufficient, as the structural characteristics of drugs and proteins, which encode rich chemical properties, are essential for accurate molecular interaction prediction.

Another class of methods for DTIs involves graph-based approaches. Chemical structures inherently form non-Euclidean graphs, where nodes lack a natural order, making graph convolutional networks (GCNs) [ 12 ] ideal for learning latent spatial and functional representations of drugs and proteins. GraphDTA [ 13 ], the first deep learning model incorporating drug structural information, demonstrates that GCNs can effectively learn chemical properties of drug molecules without prior knowledge. Similarly, CPI-GNN [ 14 ] combines convolutional neural networks (CNNs) with GCN to improve the representation of both drugs and targets. CPGL [ 15 ] further integrates graph attention networks and bidirectional LSTMs (BiLSTM) [ 10 ] to optimize feature representations of compounds and proteins. The advancement of 3D structure prediction tools like AlphaFold [ 16 ] and ESMFold [ 17 ] has refined protein structural representations, with models like WGNN-DTA [ 18 ] using molecular structure and contact maps to extract features through multi-layer GCNs and graph attention networks. SP-DTI [ 19 ] enhances DTI prediction accuracy by combining 3D structural predictions with pretrained language model (PLM) features. These approaches have significantly improved DTI prediction by enriching structural information. However, efficiently integrating features from various modalities remains a challenge in modeling DTIs.

The final category of methods is hybrid-based approaches, which aim to enhance interaction modeling for the multimodal representations of drugs and targets. MolTrans [ 20 ] proposes a molecular interaction transformer that maps drug substructure graphs and amino acid subsequences for interaction modeling. Similarly, DrugBan [ 21 ] uses a deep bilinear attention network for local joint interactions, with a bilinear attention map that enhances prediction interpretability. MCANet [ 22 ] utilizes a cross-attention mechanism to connect drugs and proteins, striking a balance between computational resources and prediction accuracy. CPInformer [ 23 ] introduces a densely connected multi-scale network and functional class fingerprints (FCFPs) [ 24 ] to capture complementary features. MulinforCPI [ 25 ] applies transfer learning to address missing atomic coordinates and distances in sequence data. To improve multimodal data interaction, HMSA [ 26 ] breaks modal constraints and enhances cross-modal fusion. MIN [ 27 ] introduces a multi-channel interaction network that utilizes contrastive learning and a multi-channel interaction module to identify patterns at various levels. Overall, hybrid-based approaches not only leverage the advantages of integrating sequence and graph structure information but also enhance the interaction between features from various modalities, resulting in improved model interpretability and prediction performance.

Currently, hybrid-based coarse-grained interaction methods can typically capture only the ambiguous binding relationships between drugs and entire proteins. The pronounced size differences between drugs and proteins are a key factor contributing to the difficulty of identifying binding sites. Furthermore, the issue of modality imbalance in multimodal fusion [ 28 ] often biases feature learning towards dominant modalities. This issue also affects multimodal DTI methods, where modality learning biases hinder the discovery of binding site clues [ 29 ]. Therefore, alleviating modality imbalance has become crucial for achieving effective information aggregation and improving prediction accuracy.

To address the size differences between drugs and proteins, we propose the DDGR-DTI model (see Fig. 1 ), which employs a decoupled dual-granularity framework, providing a foundation for achieving interactions at the substructure-level. Specifically, at the macro level, sequence-level interactions, graph-level interactions, and PLM-derived representations are processed, respectively. At the micro level, we decompose the representations of each subtask to the substructure-level and employ a dual-stream attention module (DAM) for interaction. This module enhances local interactions and identifies potential binding sites. Furthermore, we design a rebalanced pyramid network (RPN) to replace the general classifier. This network employs a hierarchical aggregation strategy, designed to capture discriminative features and achieve balanced multimodal feature learning. This approach thereby compensates for the dominance of any single modality caused by learning biases, which often leads to the overlook of valuable complementary information from other modalities.


### Figure 1.


> **Figure/Table Caption:** The architecture of DDGR-DTI, including (a) data processing with three modality representations (i-iii), (b) feature extraction and interaction for sequence (b1) and graph structure (b2) information, and (c) feature fusion and prediction.

Our contributions are mainly as follows:

We propose a decoupled dual-granularity framework that decomposes the DTI task at both macro and micro levels, providing a foundation for fine-grained interactions between drugs and targets.

The DAM is designed to capture substructure-level interactions between drugs and targets, enabling the accurate identification of binding sites.

The RPN achieves modality balance learning in DTI tasks through a hierarchical aggregation strategy, thereby fully leveraging complementary advantages of multimodal representations.


## Materials and methods

In this section, we will introduce the DDGR-DTI, an end-to-end deep learning model designed for predicting DTIs. The DDGR-DTI model decomposes the prediction task into both macro and micro levels. At the macro level, the DTI task is divided into three subtasks based on various modalities: sequence modality, graph modality, and PLM modality. At the micro level, the features of the sequence and graph modalities are further decomposed and enhanced to achieve fine-grained interactions.


### Data processing


#### Sequence modality representations

The SMILES strings of drugs and protein sequences are utilized as sequence-level information for initial input into the model. Through tokenizers (Encoding), SMILES strings and protein sequences are split into two token sets. The protein tokenizer operates at the residue level, with a vocabulary containing the single-letter codes for each amino acid. The drug tokenizer ensures atom-level tokenization, meaning that each atom in the SMILES string is assigned a unique token.


#### Graph modality representations

For graph-level representation, the drug molecule graph and the residue contact map are constructed before inputting them into the multi-layer graph neural network. Specifically, the drug molecule graph consists of the atom set and the chemical bonds between atoms, , generated using the RDKit library [ 30 ]. To capture the protein conformation information, we employ the protein structure prediction model ESMFold, which infers residue-level contact probabilities to construct a weighted residue contact map. In the residue contact map, represents the set of residues, and represents the set of contact edges between residues. A stable contact is established between residues if the contact probability exceeds 0.5, and an edge is created to represent this relationship. The contact probabilities are used as edge weights, reflecting the relative strength of different contacts, thus enabling the comprehensive capture of protein conformation features.


#### Pretrained language model modality representations

To enhance the generalization performance of the model and achieve superior results in DTI tasks, the PLM for both protein and drug representations is introduced. ChemBERTa [ 31 ] is an advanced model based on the Transformer architecture, specifically designed for predicting molecular properties. By leveraging a large SMILES strings dataset for self-supervised pretraining, it captures various chemical properties and encodes rich molecular representations. In this work, SMILES strings are input into ChemBERTa. The output is which provides contextual information for drug molecules. ESM-1b [ 17 ] is a language model similar to those used in natural language processing, but it is specifically designed to process the amino acid sequences that comprise proteins. Similarly, protein sequences are input into the ESM-1b, and the resulting serves as a supplementary biological prior knowledge for the complex structure of proteins.


### Feature extraction and interaction

After obtaining the representations of various modalities, the DDGR-DTI model centers on two major tasks: (i) feature extraction and interaction (further divided into sequence and graph modalities) and (ii) feature fusion and final prediction. The architecture of the core network modules is illustrated in Fig. 2 .


#### Figure 2.


> **Figure/Table Caption:** The architecture of the network components, including (a) the framework of the GUM, (b) the framework of the DAM, and (c) the architecture of the RPN.


#### Sequence modality feature extraction and interaction

After processing through the embedding layer [ 32 ], these token sets are transformed into two distinct features: , where denotes the length of the target sequence, and represents the dimensionality of the feature, and , where indicates the length of the SMILES string, and refers to the dimensionality of the feature.

The grouping update module (GUM) divides the input features into smaller groups, transforming continuous and high-dimensional sequences into a differences representation suitable for interaction. GUM performs a preliminary screening of the fragments containing binding sites, even if it disrupts the integrity of biological semantic units during segmentation. Specifically, GUM divides encoded sequence features along the -dimension of the sequence into groups, with each group having a length of . For each group, it is first average-pooled along the -dimension, and then element-wise multiplied with the corresponding original group, yielding the updated vector . The updated vector is normalized by subtracting its mean and then dividing by its standard deviation. The output can be expressed as follows:



|  | (1) |
| --- | --- |


where and are the mean and standard deviation, and is a small constant. The normalized vector is then projected using learned parameters and biases . is the sigmoid activation function. The calculation of can be expressed as follows:



|  | (2) |
| --- | --- |


After processing by the GUM, the obtained , which indicates that is divided into groups, and , which indicates that is divided into groups, are fed into the BiLSTM [ 10 ] module to capture long-range dependencies within the SMILES strings and protein sequences. This process can be expressed as:



|  | (3) |
| --- | --- |




|  | (4) |
| --- | --- |


Finally, the outputs are fed into the DAM for modeling the interactions between the SMILES string and protein sequence:



|  | (5) |
| --- | --- |


Here, denotes the interaction strength between the th fragment of the protein sequence and the th fragment of the SMILES string, while represents the interaction strength between the th fragment of the SMILES string and the th fragment of the protein sequence. The GUM is responsible for filtering the local initial features, thereby laying the foundation for the DAM to model interaction relationships among multiple discrete groups.


#### Graph modality feature extraction and interaction

To encode the graph data, both and are input into a three-layer graph attention network (GAT) [ 33 ]. The input vectors are aggregated, producing , where denotes the number of nodes contained in , and , where denotes the number of nodes contained in , which represent the aggregated features of the drug and target, respectively.

Before interacting with the structural information of the drug and target, it is necessary first to extract the graph structure information corresponding to the drug molecular graph and the residue contact map. We employ a multi-level readout strategy to extract both global molecular information and local atomic-level details. This strategy consists of adaptive max pooling and average pooling operations, which perform adaptive pooling based on the number of nodes in the molecule, focusing on atomic-level variations and the overall global structure of the molecule, respectively. Specifically, and correspond to the global features, while and emphasize the local features. Subsequently, these representation vectors are concatenated ( denotes the concatenate operator) and then fed into the Linear Decoder for adjustment and fusion. and can be expressed as:



|  | (6) |
| --- | --- |




|  | (7) |
| --- | --- |


where and . The Linear Decoder itself consists of two linear layers, two dropout layers, and an activation layer, ultimately producing a comprehensive graph representation of both the drug and protein.

The DAM, as a core of fine-grained interaction modeling, achieves precise binding site localization by combining interaction results from different modalities. This module not only enables local interactions with the grouped representations generated by GUM but also achieves fine-grained interactions at the substructure-level. By fusing interaction information from various modalities, the model effectively overcomes the challenges posed by the size differences between drugs and proteins, thereby resolving the problem of ambiguous localization of binding sites. Specifically, the module compresses the graph structure information of the input proteins and drugs through max pooling, obtaining and , which highlight the drug atoms and protein residues that are likely to interact through the assignment of greater weights. Next, a linear attention block (LAT) is employed to perform a linear transformation on the input features and their corresponding weights. This block consists of a linear layer followed by an ReLU activation function [ 34 ], which is used to generate a linear representation of the input vectors. Then, the Hadamard Product ( ) is applied to obtain the interaction matrices. and can be expressed as follows:



|  | (8) |
| --- | --- |




|  | (9) |
| --- | --- |


The resulting interaction matrix is normalized with the sigmoid activation function and then multiplied by the representations of the input drug or protein to obtain the interaction results:



|  | (10) |
| --- | --- |




|  | (11) |
| --- | --- |


where denotes the interaction strength between the th residue in the residue contact map and the th atom in the drug molecular graph, while represents the interaction strength between the th atom in the drug molecular graph and the th residue in the residue contact map. During the multi-level interaction between the drug molecular graph and the residue contact map, the interaction matrix reflects the potential interaction likelihood between atoms and residues, which can be utilized for interpretability analysis of the network.


#### Feature fusion and prediction

Imbalanced aggregation of multimodal representations can limit the predictive performance of DTI. Inspired by the pyramid network in the field of vision [ 35 ], we design a pyramid-like hierarchical feature aggregation module, RPN. This network is essentially a data-driven implicit optimization process guided by a hierarchical structure. Specifically, the rebalancing mechanism of the RPN is manifested in three interconnected layers. First, in the intra-modal fusion stage, we provide an independent feature optimization path for each modality. This stage ensures that the information of a single modality is dense and discriminative, thus avoiding initial imbalance due to differences in the scale or distribution of the original features. Building on this, inter-modal fusion utilizes an MLP to dynamically adjust the relative weights of features from different modalities, effectively preventing any single modality from dominating the fusion process and ignoring information from other modalities.

In the proposed network, the RPN is used to integrate the sequence features, PLM features, and graph features. In the sequence fusion channel, the processed drug and protein sequence are processed through max pooling to obtain and , which are then fed into a three-layer MLP network . This channel is designed to fuse sequence-level features:



|  | (12) |
| --- | --- |


In the graph fusion channel, the drug and protein graph representations are processed through max pooling to obtain and , which are input into a three-layer MLP network . This channel is used to fuse structural-level features:



|  | (13) |
| --- | --- |


Before feeding the PLM-derived representations into the PLM fusion channel, we first adjust these features to enhance their suitability for the DTI prediction task. The generation of and is represented as follows:



|  | (14) |
| --- | --- |




|  | (15) |
| --- | --- |


Subsequently, and are provided as inputs to a three-layer MLP network , which is used for fusing PLM features. After intra-modal interaction, we obtain three representations:



|  | (16) |
| --- | --- |


For cross-modality fusion, sequence features and PLM features are passed into the text fusion channel , which is composed of a three-layer MLP network. This produces the fused feature :



|  | (17) |
| --- | --- |


Similarly, graph features and PLM features are input into the structure fusion channel , which is a three-layer MLP network. The output is the fused feature .



|  | (18) |
| --- | --- |


Finally, both and are passed into the mixture fusion channel for the final fusion, which is used for feature fusion and predicting DTIs.



|  | (19) |
| --- | --- |


The RPN continuously updates and optimizes throughout the training process, allowing for complementary adjustments between various modalities to enhance prediction accuracy. In the experimental section, we will discuss the performance and interpretability of this network.


## Results

To demonstrate the learning effectiveness and generalization capability of DDGR-DTI in the DTI prediction task, both warm start and cold start experiments are conducted, comparing the results with baseline methods. Additionally, various ablation studies on the network framework and internal modules are performed to validate the rationality of the design.


### Datasets and evaluation metrics

In this study, we evaluate the performance of DDGR-DTI in predicting DTIs using three benchmark datasets: Davis [ 36 ], KIBA [ 37 ], and DrugBank [ 38 ]. The Davis dataset focuses on the kinase protein family, with drug activity quantified by the dissociation constant (Kd). In contrast, KIBA integrates multiple bioactivity measures, including Kd, Ki, and IC50. DrugBank offers comprehensive information on drugs and their targets, serving as a classical DTI benchmark. For Davis and KIBA datasets based on DTA, binary labels are constructed using affinity thresholds of 5.0 and 12.1, respectively. For DrugBank, interaction labels indicating whether a drug–target pair interacts are directly obtained from the database. The Davis dataset initially covers interactions between 72 kinase inhibitors and 442 kinases. After preprocessing, we retain 68 drugs and 379 proteins, resulting in 7320 positive and 18 452 negative samples. The KIBA dataset, which focuses on kinase inhibitor bioactivity, comprises 2068 drugs and 225 proteins, resulting in 22 154 positive and 94 196 negative samples. For DrugBank, following the dataset construction protocol of HyperAttentionDTI, we exclude tiny drug molecules and those unrecognized by RDKit, resulting in 4294 proteins and 6655 drugs, with 17 511 positive and 17 511 negative samples. To ensure data validity, we perform rigorous preprocessing, which includes: (i) generating binary labels based on prior methods, updating the data, and removing redundancies, (ii) using the ESMFold to obtain residue contact maps, and (iii) excluding tiny drug molecules or those incompatible with RDKit.

In this section, we adopt the commonly used metrics for performance comparison with baseline methods, including AUC, Precision, Accuracy, Recall, and F1 Score.


### Experiment setting

The DDGR-DTI model is implemented in PyTorch [ 39 ] and trained using the Adam optimizer [ 40 ] with a learning rate of 0.001 and for 200 epochs. All experiments are conducted on an NVIDIA GeForce RTX 4070 Ti GPU. In the BiLSTM module, the input embedding size is 128, with a hidden dimension of 256 and a dropout rate of 0.1. For the GUM, SMILES strings and protein sequences are split into segments of 20 and 200 characters, respectively. The dataset is divided into training, validation, and test sets with a ratio of 8:1:1. The values of and are set to 1000 and 100, respectively.


### Baseline models

We evaluate the performance of the proposed model against several leading DTI prediction models, including MCANet [ 22 ], DrugBAN [ 21 ], DeepConv-DTI [ 8 ], DO-GMA [ 41 ], MMDG-DTI [ 42 ], and MolTrans [ 20 ]. Each baseline model is replicated using the recommended parameters. The brief description of the baselines is listed below:

MCANet [ 22 ]: a weight-sharing cross-attention network is designed to simulate interactions between SMILES strings and protein sequences.

DrugBAN [ 21 ]: a cross-domain adaptive bilinear attention explainable network is employed for modeling local interactions between drugs and proteins.

DeepConv-DTI [ 8 ]: a pioneering deep learning-based DTI prediction network that employs convolution and max pooling to process the encoding of protein sequences and drug fingerprints for binding sites determination.

DO-GMA [ 41 ]: integrating deep over-parameterized CNNs and gated multi-head attention mechanisms with shared learning queries and bilinear models for DTI identification.

MMDG-DTI [ 42 ]: this model improves its generalization ability by fusing multimodal features and utilizing domain adversarial training and contrastive learning.

MolTrans [ 20 ]: the model utilizes the substructure pattern mining and enhanced transformer encoders to achieve semantic interaction modeling at the substructure-level.


### Comparative analysis of various methods

We conduct experiments on three public datasets (Davis, KIBA, and DrugBank) to evaluate the baseline methods and the DDGR-DTI model, with detailed results shown in Table 1 . The authoritative Davis dataset reveals significant improvements in AUC, Accuracy, and Precision for DDGR-DTI. Compared to the second-best performer, HyperAttentionDTI, our method achieves increases of 1.9%, 2.8%, and 3.1% in these metrics, respectively. Although DO-GMA and MCANet demonstrate high performance on the KIBA dataset, our approach outperforms them, particularly in Precision, where it surpasses MCANet by 5.5%. On the balanced DrugBank dataset, DDGR-DTI outperforms all models across five evaluation metrics, notably exceeding MMDG-DTI by 1.8% in AUC and 2.3% in Accuracy. Our method facilitates more effective integration and interaction of multimodal information, which is a key factor contributing to its superior performance.


#### Table 1.

Comparative performance analysis of DDGR-DTI and baseline methods on the benchmark datasets



| Dataset | Methods | AUC (std) | Accuracy (std) | Precision (std) | Recall(std) | F1 (std) |
| --- | --- | --- | --- | --- | --- | --- |
| Davis | MolTrans | 0.890 (0.011) | 0.748 (0.021) | 0.539 (0.018) | 0.892 (0.020) | 0.748 (0.021) |
|  | HyperAttentionDTI | 0.924 (0.008) | 0.868 (0.019) | 0.780 (0.011) | 0.759 (0.029) | 0.769 (0.022) |
|  | DrugBan | 0.883 (0.007) | 0.758 (0.018) | 0.551 (0.013) | 0.712 (0.023) | 0.624 (0.027) |
|  | MCANet | 0.922 (0.013) | 0.866 (0.029) | 0.760 (0.021) | 0.772 (0.037) | 0.765 (0.029) |
|  | DO-GMA | 0.914 (0.021) | 0.815 (0.027) | 0.629 (0.021) | 0.874 (0.034) | 0.839 (0.033) |
|  | MMDG-DTI | 0.923 (0.011) | 0.854 (0.017) | 0.788 (0.021) | 0.752 (0.023) | 0.769 (0.020) |
|  | DDGR-DTI | 0.943 (0.009) | 0.896 (0.021) | 0.811 (0.022) | 0.823 (0.033) | 0.817 (0.031) |
| KIBA | MolTrans | 0.924 (0.004) | 0.816 (0.007) | 0.512 (0.011) | 0.882 (0.015) | 0.695 (0.011) |
|  | HyperAttentionDTI | 0.932 (0.006) | 0.872 (0.009) | 0.625 (0.013) | 0.825 (0.017) | 0.711 (0.017) |
|  | DrugBan | 0.922 (0.003) | 0.845 (0.006) | 0.564 (0.010) | 0.842 (0.014) | 0.675 (0.013) |
|  | MCANet | 0.931 (0.007) | 0.896 (0.011) | 0.725 (0.017) | 0.746 (0.021) | 0.735 (0.022) |
|  | DO-GMA | 0.938 (0.006) | 0.849 (0.013) | 0.571 (0.016) | 0.882 (0.023) | 0.865 (0.029) |
|  | MMDG-DTI | 0.937 (0.013) | 0.844 (0.017) | 0.778 (0.019) | 0.742 (0.024) | 0.747 (0.023) |
|  | DDGR-DTI | 0.949 (0.009) | 0.914 (0.012) | 0.780 (0.019) | 0.755 (0.027) | 0.768 (0.025) |
| DrugBank | MolTrans | 0.890 (0.021) | 0.787 (0.019) | 0.753 (0.023) | 0.853 (0.019) | 0.793 (0.023) |
|  | HyperAttentionDTI | 0.894 (0.023) | 0.818 (0.024) | 0.808 (0.027) | 0.832 (0.022) | 0.820 (0.027) |
|  | DrugBan | 0.893 (0.022) | 0.826 (0.023) | 0.825 (0.026) | 0.825 (0.021) | 0.823 (0.021) |
|  | MCANet | 0.894 (0.024) | 0.819 (0.029) | 0.817 (0.030) | 0.822 (0.024) | 0.820 (0.029) |
|  | DO-GMA | 0.921 (0.031) | 0.849 (0.027) | 0.850 (0.028) | 0.847 (0.027) | 0.848 (0.031) |
|  | MMDG-DTI | 0.923 (0.027) | 0.853 (0.025) | 0.868 (0.021) | 0.857 (0.024) | 0.855 (0.033) |
|  | DDGR-DTI | 0.941 (0.027) | 0.876 (0.031) | 0.885 (0.029) | 0.865 (0.025) | 0.875 (0.029) |


Bold denotes best values and underline denotes second best.


### Performance comparison in three real-world scenarios

To simulate real-world scenarios in drug discovery, we evaluate the generalization ability of the model in the DTI task using three dataset partitioning strategies: drug cold start, target cold start, and all unseen, applied to the DrugBank dataset. The specific experimental results are shown in Table 2 . Unlike general DTI prediction methods based on random dataset splits, cold start partitioning is more aligned with real-world drug discovery scenarios. This setup requires the model to fit data types better and distributions that differ from those in the training set, imposing higher demands on performance.


#### Table 2.

The Performance evaluation of DDGR-DTI on the DrugBank dataset under cold start settings



| Setting | Methods | AUC(std) | Accuracy(std) | Precision(std) | Recall(std) | F1(std) |
| --- | --- | --- | --- | --- | --- | --- |
| Drug cold start | MolTrans | 0.810 (0.031) | 0.709 (0.037) | 0.669 (0.028) | 0.859 (0.039) | 0.709 (0.032) |
|  | HyperAttentionDTI | 0.873 (0.035) | 0.800 (0.023) | 0.811 (0.026) | 0.762 (0.032) | 0.785 (0.029) |
|  | DrugBan | 0.858 (0.030) | 0.775 (0.035) | 0.763 (0.027) | 0.734 (0.027) | 0.748 (0.031) |
|  | MCANet | 0.837 (0.028) | 0.748 (0.029) | 0.720 (0.026) | 0.775 (0.024) | 0.747 (0.028) |
|  | DO-GMA | 0.875 (0.027) | 0.796 (0.031) | 0.796 (0.025) | 0.811 (0.038) | 0.799 (0.030) |
|  | MMDG-DTI | 0.891 (0.029) | 0.802 (0.027) | 0.799 (0.024) | 0.807 (0.026) | 0.811 (0.034) |
|  | DDGR-DTI | 0.919 (0.021) | 0.846 (0.025) | 0.847 (0.022) | 0.823 (0.026) | 0.835 (0.024) |
| Target cold start | MolTrans | 0.752 (0.035) | 0.597 (0.031) | 0.540 (0.032) | 0.901 (0.026) | 0.639 (0.032) |
|  | HyperAttentionDTI | 0.803 (0.029) | 0.731 (0.027) | 0.801 (0.030) | 0.640 (0.034) | 0.712 (0.033) |
|  | DrugBan | 0.808 (0.032) | 0.743 (0.031) | 0.742 (0.029) | 0.594 (0.035) | 0.660 (0.034) |
|  | MCANet | 0.806 (0.027) | 0.737 (0.033) | 0.823 (0.024) | 0.627 (0.031) | 0.841 (0.026) |
|  | DO-GMA | 0.802 (0.030) | 0.706 (0.029) | 0.646 (0.028) | 0.814 (0.032) | 0.740 (0.033) |
|  | MMDG-DTI | 0.869 (0.027) | 0.773 (0.025) | 0.767 (0.025) | 0.759 (0.021) | 0.763 (0.033) |
|  | DDGR-DTI | 0.924 (0.022) | 0.843 (0.025) | 0.883 (0.021) | 0.825 (0.024) | 0.853 (0.022) |
| All unseen | MolTrans | 0.710 (0.040) | 0.625 (0.038) | 0.551 (0.037) | 0.832 (0.031) | 0.568 (0.035) |
|  | HyperAttentionDTI | 0.766 (0.029) | 0.686 (0.032) | 0.756 (0.030) | 0.461 (0.035) | 0.573 (0.031) |
|  | DrugBan | 0.799 (0.028) | 0.751 (0.026) | 0.766 (0.027) | 0.544 (0.031) | 0.636 (0.028) |
|  | MCANet | 0.796 (0.027) | 0.743 (0.029) | 0.777 (0.025) | 0.609 (0.030) | 0.796 (0.026) |
|  | DO-GMA | 0.731 (0.030) | 0.601 (0.033) | 0.530 (0.031) | 0.916 (0.028) | 0.713 (0.032) |
|  | MMDG-DTI | 0.801 (0.031) | 0.709 (0.035) | 0.699 (0.035) | 0.688 (0.029) | 0.703 (0.033) |
|  | DDGR-DTI | 0.874 (0.020) | 0.782 (0.026) | 0.842 (0.022) | 0.738 (0.028) | 0.787 (0.025) |


Bold denotes best values and underline denotes second best.

Table 2 presents the performance results of various baseline methods in the cold start setting using the DrugBank dataset. Since the drug cold start setting removes the same drugs from the test set, all models show a performance decrease, which also widens the gap between DDGR-DTI and baseline methods. Under the drug cold start setting, DDGR-DTI improves by 2.8% in AUC and 4.4% in Accuracy compared with the second-best performing model, MMDG-DTI. In the target cold start setting, the baseline methods perform even worse, likely because they rely on simple sequence embeddings for protein feature extraction, which limit the model’s generalization capability. In contrast, the proposed method performs better, particularly in terms of AUC and Precision, with improvements of 5.5% and 7.0%, respectively, compared with the second-best model. Ultimately, in all unseen settings, our method leverages the relevant features provided by the PLM, achieving superior performance compared with other baseline methods. The experimental results in the cold start setting fully demonstrate that our approach is more suitable for drug discovery scenarios. This superiority is not only due to the rich features provided by the PLM, but also due to the powerful complementary integration capability of multimodal data in our method.


### Ablation study

To highlight the contribution of each module to the model’s performance, we conduct ablation experiments on the network components using the Davis dataset, with detailed results presented in Table 3 . We compare DDGR-DTI against five ablation models configured as follows: w/o GUM (removing the GUM), w/o DAM (removing the DAM), w/o Fusion (removing the RPN), w/o Readout (removing the multi-level readout strategy), and w/o PLM (removing features from the PLM). These experiments confirm the contribution of each module to the overall effectiveness of the model.


#### Table 3.

Ablation experiment results for all modules on the Davis dataset



| Settings | AUC(std) | ACC(std) |
| --- | --- | --- |
| w/o GUM | 0.939 (0.012) | 0.879 (0.018) |
| w/o DAM | 0.931 (0.014) | 0.866 (0.019) |
| w/o Fusion | 0.937 (0.013) | 0.871 (0.017) |
| w/o Readout | 0.941 (0.011) | 0.892 (0.015) |
| w/o PLM | 0.940 (0.010) | 0.891 (0.016) |
| DDGR-DTI | 0.943 (0.009) | 0.896 (0.014) |


Bold denotes best values and underline denotes second best.

As illustrated in Table 3 , the removal of various components has a significant impact on the performance of the model. The “w/o Fusion” and “w/o DAM” configurations lead to substantial declines in both AUC and ACC, underscoring their critical importance. Although the absence of “w/o GUM,” “w/o Readout,” and “w/o PLM” also results in decreased performance, the impact is comparatively less severe. Overall, each module plays a vital role in ensuring the effectiveness of DDGR-DTI, with the complete model demonstrating the highest AUC (0.943) and ACC (0.896), thereby validating the value of integrating these components. Additionally, we conduct comprehensive ablation experiments on the multi-level readout strategy (see Fig. 3c ). The results indicate that the inclusion or removal of local and global features affects model performance and that integrating both feature types for downstream interactions further enhances predictive performance.


#### Figure 3.


> **Figure/Table Caption:** Panel (a) shows length distributions of SMILES and Sequences across the three datasets, panel (b) presents hyperparameter results for GUM length divisions, and panel (c) analyzes the multi-level readout strategy.

Additionally, we further analyze the superior performance of DDGR-DTI in the cold start experiment. The ablation experiment results of DDGR-DTI in all unseen settings are shown in Table 4 . The addition of PLM-derived features has a significant impact on the performance of the model in invisible predictions. The prior knowledge is crucial for the ability of the model to identify binding to unseen drug targets. It is worth noting that RPN ablation also has a significant impact on model performance, which not only highlights the importance of PLM modal feature injection but also underscores the substantial value of balancing the aggregation of different modal representations.


#### Table 4.

Ablation experiment results on the DDGR-DTI conducted using the DrugBank dataset in the all unseen setting



| Settings | AUC(std) | ACC(std) |
| --- | --- | --- |
| w/o GUM | 0.863 (0.018) | 0.772 (0.023) |
| w/o DAM | 0.857 (0.017) | 0.761 (0.023) |
| w/o Fusion | 0.843 (0.027) | 0.755 (0.031) |
| w/o Readout | 0.869 (0.022) | 0.778 (0.028) |
| w/o PLM | 0.821 (0.019) | 0.733 (0.021) |
| DDGR-DTI | 0.874 (0.020) | 0.782 (0.026) |


Bold denotes best values and underline denotes second best.

To thoroughly evaluate the performance of the RPN, we structurally decompose this module and conduct corresponding ablation experiments. The specific results are shown in Table 5 . We compare RPN against three ablation variants configured as follows: w/o Intra-Modal, remove intra-modal fusion channels; w/o Inter-Modal, remove inter-modal fusion channels; w/o Mixture, remove the mixture fusion channel. The experimental results demonstrate that the fusion channels within each modality and the fusion channels between modalities have a particularly significant impact on the outcomes. The impact is likely due to the effective representation of single-modal features and the elimination of differences between modalities, both of which play crucial roles in the model.


#### Table 5.

Ablation experimental results of RPNs on the Davis dataset



| Settings | AUC(std) | ACC(std) |
| --- | --- | --- |
| w/o Intra-Modal | 0.939 (0.017) | 0.877 (0.019) |
| w/o Inter-Modal | 0.940 (0.014) | 0.885 (0.011) |
| w/o Mixture | 0.941 (0.015) | 0.892 (0.014) |
| w/o Fusion | 0.937 (0.013) | 0.871 (0.017) |
| DDGR-DTI | 0.943 (0.009) | 0.896 (0.014) |


Bold denotes best values and underline denotes second best.


#### Hyperparameter analysis

The sequence partitioning setting is investigated through further hyperparameter analysis experiments, as shown in Fig. 3b . We statistically analyze the lengths of SMILES strings and protein sequences across three datasets, finding that the ratio of SMILES string length to protein sequence length is 1:10 (see Fig. 3a ). Accordingly, the partition length ratio for SMILES strings and protein sequences is set to 1:10. Experimental results indicate that dividing drug sequences into units of 20 and protein sequences into units of 200 (20/200) yields the best AUC value.


#### Analysis of rebalanced pyramid network

To investigate how the RPN achieves modality rebalancing and its impact on DTI prediction, we visualize the feature fusion process using t-SNE (see Fig. 4 ).


> **Figure/Table Caption:** t-SNE visualizations illustrate the evolving feature distributions across different stages of the RPN, encompassing the initial features, and the features after intra-modal, inter-modal, and mixture fusion.

Initially, the distribution of input features exhibits a chaotic state, with overlapping clusters of positive and negative samples, reflecting the inherent inconsistencies between multimodal representations. After intra-modal fusion, the number of clusters corresponds to the subtask categories, including graph-level, sequence-level, and PLM-level aggregation. The intra-modal aggregation mechanism focuses on unifying features within the same modality by enhancing their discriminative patterns. However, the imbalance between positive and negative samples within each cluster indicates a difference in the contribution of various modalities to the prediction. Through inter-modal fusion, the clusters begin to converge into a shared feature space, with positive and negative samples forming more distinguishable groups. This distribution indicates inter-modal fusion, which effectively aggregates various modalities within the same space, significantly eliminating inconsistencies between modalities and reducing the dominant influence of any single modality on the outcomes. Ultimately, the mixture fusion integrates these rebalanced representations into tightly clustered groups, with positive and negative samples forming distinct and non-overlapping distributions.

This entire process validates the rebalancing mechanism of the RPN. By employing hierarchical aggregation, the network dynamically adjusts the contribution of each modality according to its relevance to the DTI patterns, ensuring that no single modality overshadows the others. In summary, the separated and well-clustered enhance the quality of feature representations, eliminate inconsistencies present in multimodal representations, and strengthen the contributions of multimodal representations. t-SNE visualizations indicate that the RPN effectively addresses the imbalances encountered during the aggregation of multimodal representations.


## Conclusion

In summary, the decoupled dual-granularity rebalanced pyramid network offers a significant improvement in DTI prediction by addressing the size differences between drugs and proteins. The decoupled dual-granularity framework facilitates a deeper understanding of interactions at both macro and micro levels, while the RPN effectively aggregates diverse modality features, maximizing their complementary strengths. Benchmark results confirm that DDGR-DTI outperforms existing state-of-the-art models, demonstrating robust generalization capabilities, particularly with unseen drugs and targets. This work represents a significant advancement and provides a reliable tool for future drug discovery efforts.

The practical utility of the model is further highlighted in real docking scenarios, where it accurately predicts atoms in ligand molecules that participate in specific interactions, such as hydrogen bonds and stacking. However, a comprehensive assessment highlights a notable limitation: the attention weights generated by the DAM do not always correlate strongly with actual interaction sites. This inconsistency suggests that the DAM may learn data-driven correlations rather than consistently capturing the underlying biophysical principles. Similarly, while the RPN plays a crucial role in achieving balanced multimodal integration, we acknowledge that its “rebalancing” effect emerges implicitly as a black-box characteristic of the architecture and training process. This lack of transparency and direct control over the fusion process prevents us from precisely guiding or interpreting how the final balance is achieved.

In the future, we will apply the proposed approach to other biological entity link prediction tasks, such as miRNA–disease association [ 43 ] and protein functional annotation [ 44 ].


### Key Points

We propose a decoupled dual-granularity framework that decomposes the drug–target interaction (DTI) task at both macro and micro levels, providing a foundation for fine-grained interactions between drugs and targets.

The dual-stream attention module is designed to capture substructure-level interactions between drugs and targets, enabling the accurate identification of binding sites.

The rebalanced pyramid network achieves modality balance learning in DTI tasks through a hierarchical aggregation strategy, thereby fully leveraging complementary advantages of multimodal representations.


## Contributor Information

Zhiyuan Dong, School of Computer and Artificial Intelligence, Zhengzhou University, No. 100 Science Avenue, Zhengzhou 450000, China.

Yijia Zhang, The Second Affiliated Hospital of Dalian Medical University, 467 Zhongshan Road, Shahekou District, Dalian 116023, China.

Yang Shi, Institute of Medical Technology, Peking University Health Science Center, No. 38 Xueyuan Road, Haidian District, Beijing 100191, China.

Chao Zhang, The Second Affiliated Hospital of Dalian Medical University, 467 Zhongshan Road, Shahekou District, Dalian 116023, China.

Chaoyang Han, The Second Affiliated Hospital of Dalian Medical University, 467 Zhongshan Road, Shahekou District, Dalian 116023, China.

Hongfeng Li, Institute of Medical Technology, Peking University Health Science Center, No. 38 Xueyuan Road, Haidian District, Beijing 100191, China.

Yajuan Gao, Department of Radiology, Peking University Third Hospital, No. 49 Huayuan North Road, Haidian District, Beijing 100191, China; Beijing Key Laboratory of Magnetic Resonance lmaging Devices and Technology, Peking University Third Hospital, No. 49 Huayuan North Road, Haidian District, Beijing 100191, China.

Wanyi Fu, Institute of Medical Technology, Peking University Health Science Center, No. 38 Xueyuan Road, Haidian District, Beijing 100191, China.

Yanye Lu, Institute of Medical Technology, Peking University Health Science Center, No. 38 Xueyuan Road, Haidian District, Beijing 100191, China.

Ping Ren, The Second Affiliated Hospital of Dalian Medical University, 467 Zhongshan Road, Shahekou District, Dalian 116023, China.

Lei [AUTHOR], Peking University and Director of the Ultrasound Department, Aerospace Center Hospital, No. 15 Yuquan Road, Haidian District, Beijing 100049, China.

Zhiyu Liu, The Second Affiliated Hospital of Dalian Medical University, 467 Zhongshan Road, Shahekou District, Dalian 116023, China.



Zhiyuan Dong (Data curation, Methodology, Writing), Yijia Zhang (Data curation, Methodology, Writing), Shi Yang (Data curation, Methodology, Writing), Chao Zhang (Conceptualization, Methodology, Software), Chaoyang Han (Conceptualization, Methodology, Software), Hongfeng Li (Conceptualization, Methodology, Software), Yajuan Gao (Conceptualization, Methodology, Software), Wanyi Fu (Writing—reviewing and editing), Yanye Lu (Writing—reviewing and editing), Ping Ren (Visualization, Investigation), Lei [AUTHOR] (Visualization, Investigation), and Zhiyu Liu (Visualization, Investigation)



## Funding

This work is supported by the National Natural Science Foundation of China (grant no. 62371423) and the Natural Science Foundation of Henan (grant no. 252300421226).


## Data availability

The datasets used in this project are updated and available at [GITHUB_REPO_REDACTED] .

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials


### Data Availability Statement

The datasets used in this project are updated and available at [GITHUB_REPO_REDACTED] .
