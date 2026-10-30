# De-Identified Manuscript `OOD_ANON_38`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract


### Abstract

Predicting protein-ligand binding affinity is essential for understanding protein-ligand interactions and advancing drug discovery. Recent research has demonstrated the advantages of sequence-based models and graph-based models. In this study, we present a novel hybrid multimodal approach, DeepTGIN, which integrates transformers and graph isomorphism networks to predict protein-ligand binding affinity. DeepTGIN is designed to learn sequence and graph features efficiently. The DeepTGIN model comprises three modules: the data representation module, the encoder module, and the prediction module. The transformer encoder learns sequential features from proteins and protein pockets separately, while the graph isomorphism network extracts graph features from the ligands. To evaluate the performance of DeepTGIN, we compared it with state-of-the-art models using the PDBbind 2016 core set and PDBbind 2013 core set. DeepTGIN outperforms these models in terms of R, RMSE, MAE, SD, and CI metrics. Ablation studies further demonstrate the effectiveness of the ligand features and the encoder module. The code is available at: [GITHUB_REPO_REDACTED] .


### Scientific contribution

DeepTGIN is a novel hybrid multimodal deep learning model for predict protein-ligand binding affinity. The model combines the Transformer encoder to extract sequence features from protein and protein pocket, while integrating graph isomorphism networks to capture features from the ligand. This model addresses the limitations of existing methods in exploring protein pocket and ligand features.


### Supplementary Information

The online version contains supplementary material available at [REDACTED_DOI].

Keywords: Protein-ligand binding affinity prediction, Transformer, Graph isomorphism network, Multimodal


## Introduction

As a prominent topic in drug discovery research [ 1 , 2 ], drug-target binding affinity prediction can significantly accelerate drug discovery [ 3 , 4 ] and facilitate drug repositioning [ 5 ]. Drugs typically act as ligands, exerting their effects through specific interactions with target proteins [ 6 – 8 ]. The key metric for measuring these interactions is affinity [ 9 ]. Therefore, calculating protein-ligand affinity (PLA) is essential in drug discovery [ 10 ]. However, experimentally determining the affinity between proteins and ligands is both time-consuming [ 11 ] and costly [ 2 , 12 ]. Deep learning methods offer a faster approach to calculating affinity [ 13 – 15 ]. These methods can be categorized into sequence-based models [ 16 – 19 ], graph-based models [ 20 – 23 ], and multimodal models [ 24 – 27 ].

As a typical sequence-based model, DeepDTA [ 16 ] uses protein sequences and SMILES (Simplified Molecular Input Line Entry System) [ 28 ] representations of ligands as inputs. The DeepDTA model utilizes two convolutional neural network (CNN) blocks to learn features of proteins and ligands, followed by a multi-layer perceptron (MLP) to predict affinity. A similar model, DeepCDA [ 17 ], combines CNN and long short-term memory (LSTM) networks to learn features of proteins and ligands and the occurrence patterns of local substructures. This model introduces a two-sided attention mechanism to encode the interaction strength, enhancing the understanding of protein-ligand interactions, and finally uses a fully connected layer to predict affinity. DeepDTAF [ 29 ] is another protein-ligand affinity prediction model that integrates global and local features. Specifically, the entire protein is used as a global feature, and the protein binding pocket, which has direct binding properties with the ligand, is used as a local feature. Three different groups of CNN modules are employed to learn the features of the proteins, protein pockets, and ligands. Finally, three fully connected layers are used to predict affinity. The advantage of the sequence-based model is that it can learn the contextual information in the sequence and is relatively mature in the field of representing proteins and ligands [ 30 ]. However, they have notable disadvantages, such as ignoring important structural features in proteins and ligands.

Graph-based models can account for important structural features of proteins and ligands. DGraphDTA [ 20 ] is a graph-based model for drug-target affinity prediction using graph neural network (GNN) and contact maps. The DGraphDTA converts protein sequences into graphs, with the ligand graph derived from SMILES. Two GNN blocks are used to learn the features of proteins and ligands, respectively. Finally, two fully connected layers are used to predict affinity. Similar models, such as InteractionGraphNet (IGN) [ 21 ], convert the protein-ligand complex into three independent molecular graphs: the protein graph, the bipartite protein-ligand graph, and the ligand graph. The graph convolution module is used to learn their features, and a fully connected neural network (FCNN) is then used to predict affinity. These graph-based models can effectively represent the structural information of proteins and ligands, thereby improving the prediction accuracy. However, these models also have certain limitations. For example, for computational convenience, IGN uses only the protein atoms of the binding sites in the protein graph. This approach ignores the influence of protein regions that are far away from the binding site on affinity. Using graph structure to represent proteins and ligands has certain limitations, such as the graph construction method significantly affecting the representation of proteins and ligands.

A category of multimodal models can leverage the advantages of both sequence-based and graph-based models. For example, the protein-ligand binding affinity prediction model via comprehensive molecular representations (PLA-MoRe) [ 26 ] utilizes a transformer encoder to learn features from protein sequences and GNNs to learn structural features of ligands. PLA-MoRe introduces bioactivity data of ligands, which can improve the model’s predictive performance. Similarly, a multimodal attention-based model (AttentionMGT-DTA) [ 27 ] employs two graph transformer modules to learn the structural features of ligand graphs and protein pocket graphs, while incorporating 1D sequence embeddings of proteins as protein sequence features. This model uses both sequence and structural features to further improve predictive performance.

Other multimodal models, such as GraphDTA [ 24 ] and DeepGLSTM [ 25 ], integrate various data features, considering protein and ligand features from multiple perspectives, thus effectively enhancing prediction performance and model robustness [ 31 ]. However, there are still limitations in these models. For instance, the GraphDTA and AttentionMGT-DTA models use 5 and 8 atomic properties as node features in ligand molecular graphs, respectively. These models still do not consider enough atomic properties of ligands, making the comprehensive representation of ligand characteristics a challenge.

Protein pockets are regions that directly bind with ligands, typically composed of crucial residues [ 32 ] that interact with the ligand through various interactions such as hydrogen bonds, van der Waals forces, and hydrophobic interactions [ 33 – 35 ]. However, considering only directly binding residues may overlook the influence of other residues on the ligands. For instance, global structural changes in proteins and residues far from the binding site may affect the affinity to the ligand [ 36 ]. In the study of PLA, accurately extracting the features of pockets remains a significant challenge [ 37 ]. In models that consider pockets, such as DeepDTAF, although the sequence features of pockets are used, the structural features are neglected. IGN considers the structural features of pockets but neglects the global features of proteins. Therefore, these models have certain limitations.

To address these issues, we propose a novel multimodal model for protein-ligand affinity, named DeepTGIN. Our model utilizes a transformer encoder to learn sequence features of proteins and pockets, and a GIN encoder to learn structural features of ligand molecular graphs. Our model comprehensively incorporates sequence features, structural features, both global and local features of proteins, and the atomic properties of ligands. We compared DeepTGIN with other baseline models using two test sets, and the results demonstrated that DeepTGIN outperformed the other models. Ablation studies further proved the importance of the key components of our model to the overall performance. Additionally, we visualized the attention scores of each residue to analyze the residues that contribute significantly to the protein-ligand affinity prediction. These results indicate that DeepTGIN is a reliable and effective protein-ligand affinity prediction model.

The contributions of our model are listed as follows.

This study introduces a novel hybrid approach, termed DeepTGIN, which successfully integrates the strengths of sequence-based models and graph-based models, utilizing two identical transformers for protein sequence and protein pocket feature extraction, and GIN for ligand feature extraction.

DeepTGIN features a modular architecture comprising three key components: the data representation module, the encoder module, and the prediction module. This design facilitates efficient learning of both sequential and graph features, thereby improving predictive performance.

Comparative evaluations using the PDBbind 2016 and PDBbind 2013 core sets demonstrate that DeepTGIN outperforms state-of-the-art models across several metrics, including R, RMSE, MAE, SD, and CI. Ablation studies highlight the critical role of ligand features and the encoder module in the overall performance of the model, underscoring the importance of these components in achieving accurate predictions.


## Materials and methods


### Datasets

The PDBbind database [ 38 ] is a comprehensive collection of experimentally measured binding affinity data for biomolecular complexes deposited in the Protein Data Bank, including Kd , Ki , and IC 50 values obtained through experimental verification. It is widely used for predicting protein-ligand binding affinity. In this study, we use the PDBbind2020 version as our primary dataset, which is the latest open source. As depicted in Fig. 1 , the PDBbind2020 database is divided into four subsets: the general set, the refined set, the PDBbind 2016 core set, and the PDBbind 2013 core set. These subsets contain 14127, 5316, 285, and 195 protein-ligand complexes, respectively.


#### Fig. 1.


> **Figure/Table Caption:** Components of the PDBbind2020 dataset. The PDBbind2020 dataset is divided into a general set, a refined set, the PDBbind 2016 core set, and the PDBbind 2013 core set. The training set and the validation set are derived from the general set and refined set. The PDBbind 2016 core set and the PDBbind 2013 core set are used as the test sets. Among them, there are 107 duplicated complexes between v2016 and v2013

We used the PDBbind 2016 core set [ 39 ] (also known as CASF-2016) as our test set and the PDBbind 2013 core set [ 40 ] (CASF-2013) as an additional test set. The PDBbind2016 core set is a smaller collection of protein-ligand complexes that serves as a popular and primary test set and does not change with the annual updates of PDBbind. Both of these core sets are widely recognized and commonly used benchmarks in the field of protein-ligand affinity prediction. To obtain the training set and validation set, we followed a methodology similar to Kaili Wang et al. [ 29 ]. We combined the general set and refined set and then removed any duplicate complexes in the test sets. Then, we randomly selected 1,000 protein-ligand complexes as the validation set, with the remaining complexes used as the training set.


### Overview of our DeepTGIN model

In this section, we introduce DeepTGIN, a novel multimodal protein-ligand binding affinity prediction model that combines a Transformer with a GIN. The model accepts three types of inputs: the protein residue sequence, the pocket residue sequence, and the ligand molecular graph. The overall architecture of the model is illustrated in Fig. 2 . The model comprises three main components: the data representation module, the encoder module, and the prediction module. The encoder module consists of three sub-components: a GIN encoder and two identical Transformer encoders. The prediction module utilizes an MLP to generate the final predictions.


#### Fig. 2.


> **Figure/Table Caption:** Architecture of DeepTGIN. A Data representation module: This module includes three inputs: the ligand molecular graph, the pocket residue sequence, and the protein residue sequence. B Encoder Module: This module learns the features of the ligand molecular graph using the GIN Encoder and learns the features of the protein residue sequence and pocket residue sequence using the Transformer Encoder. C Prediction Module: This module predicts the binding affinity. D GIN Encoder: The GIN Encoder comprises 4 layers of GIN. E Transformer Encoder: The Transformer Encoder consists of 4 layers of a single transformer encoder. F Single Transformer Encoder: Details about the single transformer encoder


### Data representation module

Previous studies have highlighted the importance of sequence information [ 16 – 18 ], graph structure [ 20 , 21 , 41 ], and pocket structure [ 19 , 27 , 29 ] in understanding protein-ligand pairs. In our study, we use the sequence of the protein and the protein pocket, and the graph structure of the ligand for data representation. Therefore, the data representation includes ligand representation, pocket representation, and protein representation.


#### Ligand representation

To learn ligand representation, we first use the RDKit [ 42 ] tool to transform ligands into molecular graphs. In a molecular graph, each node represents an atom in the ligand, and each edge represents the relationship between two atoms. Ten different atom properties are included as node attributes, as listed in Table 1 . We use 108-dimensional one-hot encoding as the feature vector of the node, from which the original ligand representation is obtained.

Properties of ligand atoms used in this study



| Feature type | Type values |
| --- | --- |
| Atom type | C, N, O, S, F, Si, P, Cl, Br, .... |
| Implicit valence | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| Chiral tag | unspecified, tetrahedral-cw, tetrahedral-ccw, other |
| Degree | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| Formal charge | − 5, − 4, − 3, − 2, − 1, 0, 1, 2, 3, 4, 5 |
| Number of hydrogens | 0, 1, 2, 3, 4, 5, 6, 7, 8 |
| Number of radical electrons | 0, 1, 2, 3, 4 |
| Hybridization | SP, SP2, SP3, SP3D, SP3D2 |
| Is aromatic | 0, 1 |
| Is in ring | 0, 1 |



#### Protein representation and pocket representation

To obtain the original protein representation, the protein sequence is used as the input. Each letter in the sequence represents a residue, and each residue type is encoded as an integer based on its corresponding alphabetical symbol. For example, Aspartic Acid (D) is 4, Glutamic Acid (E) is 5, Glycine (G) is 7, etc. This encoding method transforms the protein into an integer sequence. Similarly, the original pocket representation is obtained in the same manner. Due to the varying lengths of proteins and protein pockets, truncation lengths are employed in this study. The thresholds for the protein sequence length and the protein pocket sequence length are set to 1000 and 63, respectively, according to Wang et al. [ 29 ]. If the sequence length exceeds the threshold, the corresponding representation vector is truncated. Otherwise, the shorter sequences are padded with zeros.


### Encoder module


#### Ligand GIN encoder

In the ligand graph encoder, four GIN [ 43 ] layers and a pooling layer are designed to encode the ligand molecular graph. Unlike the original GIN, each GIN layer in our model includes a batch normalization operation to improve the model’s training stability. Each GIN layer uses summation as the aggregation function. According to Xu et al. [ 43 ], each GIN layer can be formulated as a graph-level representation learning process, as shown in Eq. 1 .



| h G = CONCAT ( f r ( { h v k / v ∈ G } ) ) | 1 |
| --- | --- |


In Eq. 1 , h G represents the graph G representation, h v k represents the node v representation, f r represents the readout function that calculates all node representations in graph G , and CONCAT represents a concatenation operation that combines the output values from the readout function.

In our ligand graph encoder, each GIN layer includes an additional batch normalization operation, as shown in Eq. 2 .



| h G ^ = γ × h G ^ - h G ¯ δ ( h G ) + ϵ + ( 1 - γ ) | 2 |
| --- | --- |


In Eq. 2 , h G ¯ represents the mean value of the graph representation h G , δ ( h G ) represents the standard deviation, and these values are calculated per dimension over the mini-batches. γ is a learnable parameter vector ranging from zero to one, and ϵ is a small value used to avoid division by zero.


#### Protein and pocket transformer encoder

As shown in Fig. 2 , both the protein transformer encoder and the pocket transformer encoder consist of four transformer encoder layers [ 44 ]. The protein transformer encoder and the pocket transformer encoder use an embedding layer and predefined position encoding to encode the input sequences. Each encoder comprises four transformer encoder blocks, utilizing multi-head attention mechanisms and feed-forward neural networks.

The equations for Multi-Head Attention is as follows:



| Q i = X × W Q i , K i = X × W K i , V i = X × W V i | 3 |
| --- | --- |




| h e a d i = Attention ( Q i , K i , V i ) | 4 |
| --- | --- |




| MultiHead ( Q , K , V ) = CONCAT ( h e a d 1 , ⋯ , h e a d 4 ) W O | 5 |
| --- | --- |


In these equations, i ∈ { 1 , ⋯ , 4 } , W Q i ∈ R d × d k , W K i ∈ R d × d k , W V i ∈ R d × d v , and W O ∈ R h d v × d k . The dimensionality d is set to 120, h is set to 4, and the size of the hidden layer in the feed-forward network is set to 512.

The parameters in the protein and pocket Transformer encoders are identical. We feed the integer encoding of the input into the embedding layer, converting a sparse vector into a dense vector. Proteins and pockets are represented as matrices of dimensions (1000, 120) and (63, 120), respectively. To adapt to the input of the transformer, we add the predefined position encoding to the input matrix, forming the final input to the transformer.


#### Prediction module

In the prediction module, the outputs from the three encoder modules are first concatenated. These combined results are then fed into a prediction module, which utilizes an MLP to generate the final prediction outcome.


#### Loss function

Our work is a regression task, so we choose the commonly used MSE as our loss function. Its formula is as follows.



| M S E = 1 N ∑ i = 1 N ( y t ( i ) - y p ( i ) ) 2 | 6 |
| --- | --- |


In Eq. 6 , n is the number of protein-ligand complexes, y p ( i ) and y t ( i ) represent the predicted and true affinity values of the i -th protein-ligand complex, respectively.


## Experimental results


### Hyperparameter settings

Detailed hyperparameter details can be found in Supplementary Sec.1. The parameter details of other baselines are in Supplementary Sec.2.


### Evaluation metrics

In this study, five widely used evaluation metrics are employed to assess the performance of different models. These metrics include the Pearson correlation coefficient (R), root mean square error (RMSE), mean absolute error (MAE), standard deviation (SD), and concordance index (CI).

The Pearson correlation coefficient (R) measures the degree of linear relationship between two variables. It is calculated as follows:



| R = ∑ i = 1 N ( y t ( i ) - y t ¯ ) ( y p ( i ) - y p ¯ ) ∑ i = 1 N ( y t ( i ) - y t ¯ ) 2 ∑ i = 1 N ( y p ( i ) - y p ¯ ) 2 | 7 |
| --- | --- |


In Eq. 7 , y p ( i ) and y t ( i ) represent the predicted and true affinity values of the i -th protein-ligand complex, respectively. y p ¯ and y t ¯ represent the mean values of y p ( i ) and y t ( i ) , respectively. N is the number of protein-ligand complexes. A larger R-value indicates a better model.

Root mean square error (RMSE) quantifies the average magnitude of the errors between predicted and true values, giving more weight to larger errors. It is calculated as follows:



| R M S E = 1 N ∑ i = 1 N ( y t ( i ) - y p ( i ) ) 2 | 8 |
| --- | --- |


In Eq. 8 , y p ( i ) and y t ( i ) represent the predicted and true affinity values of the i -th protein-ligand complex, respectively. N is the number of protein-ligand complexes. Lower RMSE values indicate better model performance.

Mean absolute error (MAE) measures the average absolute difference between predicted and true values. It is calculated as follows:



| M A E = 1 N ∑ i = 1 N y p ( i ) - y t ( i ) | 9 |
| --- | --- |


In Eq. 9 , y p ( i ) and y t ( i ) represent the predicted and true affinity values of the i -th protein-ligand complex, respectively. Lower MAE values indicate better model performance.

Standard deviation (SD) measures the amount of variability or dispersion in a dataset. It is calculated as follows:



| S D = 1 N - 1 ∑ i = 1 N [ y p ( i ) - ( a · y t ( i ) + b ) ] 2 | 10 |
| --- | --- |


In Eq. 10 , y p ( i ) and y t ( i ) represent the predicted and true affinity values of the i -th protein-ligand complex, respectively. N is the number of protein-ligand complexes, and a and b represent the slope and intercept of the line between the true and predicted values. Lower SD values indicate better model performance.

The concordance index (CI) estimates the probability that the predicted results are consistent with the true results. It is calculated as follows:



| C I = 1 N ∑ y p ( i ) > y p ( j ) f ( y p ( i ) - y p ( j ) ) | 11 |
| --- | --- |




| f ( x ) = 1.0 , if x > 0 0.5 , if x = 0 0.0 , if x < 0 | 12 |
| --- | --- |


In Eq. 11 , y p ( i ) and y t ( i ) represent the predicted and true affinity values of the i -th protein-ligand complex, respectively, and N is the number of protein-ligand complexes. The function f ( x ) is a segmented function as shown in Eq. 12 . A larger CI value indicates better model performance.


### Baselines

Several representative state-of-the-art models are chosen as baselines to evaluate the performance of DeepTGIN. These models include DeepDTA [ 16 ], DeepDTAF [ 29 ], IGN [ 21 ], GraphDTA [ 24 ], DeepGLSTM [ 25 ], TEFDTA [ 18 ], CAPLA [ 19 ], and GIGN [ 22 ].


### Performance of our DeepTGIN model

To test the performance of our DeepTGIN model, we used the PDBbind2016 and PDBbind2013 core sets, naming them the PDBbind2016 test set and PDBbind2013 test set, respectively. Our DeepTGIN model was trained on the training set and validated on the validation set over 100 epochs. After the training process, the evaluation metric values of our trained DeepTGIN model are summarized in Table 2 .


#### Table 2.

Performance of the DeepTGIN model



| Models | R( ↑ ) | RMSE( ↓ ) | MAE( ↓ ) | SD( ↓ ) | CI( ↑ ) |
| --- | --- | --- | --- | --- | --- |
| Training | 0.927 | 0.693 | 0.539 | 0.690 | 0.881 |
| Validation | 0.736 | 1.277 | 0.981 | 1.254 | 0.768 |
| PDBbind2016 test set | 0.834 | 1.203 | 0.949 | 1.197 | 0.823 |
| PDBbind2013 test set | 0.787 | 1.388 | 1.123 | 1.386 | 0.792 |


↑ indicates that larger values indicate better performance, while ↓ indicates that smaller values indicate better performance

For the training set, our DeepTGIN model achieved an R value of 0.927, an RMSE value of 0.693, an MAE value of 0.539, an SD value of 0.690, and a CI value of 0.881. Similarly, on the validation set, our model achieved an R value of 0.736, an RMSE value of 1.277, an MAE value of 0.981, an SD value of 1.254, and a CI value of 0.768.

Subsequently, we evaluated our DeepTGIN model on the two test sets: the PDBbind2016 test set and the PDBbind2013 test set. The detailed results are provided in Table 2 and Fig. 3 .


#### Fig. 3.


> **Figure/Table Caption:** Performance of the DeepTGIN model on the training set A , validation set B , PDBbind2016 test set C , and PDBbind2013 test set D for the prediction of binding affinity


### Results on PDBbind2016 test set and PDBbind2013 test set


#### Comparison with other models on PDBbind 2016 test set

To evaluate the performance of our DeepTGIN model, we conducted a comparative analysis against eight representative models using the PDBbind2016 and PDBbind2013 test sets. The experimental results are summarized in Tables 3 and 4 . According to Table 3 , our DeepTGIN model consistently outperforms the compared models across all five evaluation metrics: R, RMSE, MAE, SD, and CI. The CAPLA model achieves the second-best results on the PDBbind2016 test set in terms of R, RMSE, SD, and CI evaluation metrics, while the GIGN model follows with the third-best performance. Notably, the MAE evaluation of the GIGN model is relatively higher than that of the CAPLA model. Compared to CAPLA, DeepTGIN shows improvements of 4.3 % , 9.1 % , 10.7 % , 8.4 % , and 3.2 % in R, RMSE, MAE, SD, and CI, respectively. Moreover, compared to GraphDTA, DeepTGIN achieves substantial enhancements of 18.1 % , 22.0 % , 19.7 % , 22.2 % , and 9.0 % across the same metrics.

Results of the DeepTGIN model and other compared models on the PDBbind2016 test set



| Models | R( ↑ ) | RMSE( ↓ ) | MAE( ↓ ) | SD( ↓ ) | CI( ↑ ) |
| --- | --- | --- | --- | --- | --- |
| GraphDTA | 0.706 | 1.543 | 1.183 | 1.539 | 0.755 |
| DeepGLSTM | 0.722 | 1.516 | 1.147 | 1.512 | 0.768 |
| DeepDTAF | 0.758 | 1.438 | 1.148 | 1.416 | 0.778 |
| TEFDTA | 0.772 | 1.390 | 1.065 | 1.379 | 0.782 |
| DeepDTA | 0.782 | 1.351 | 1.038 | 1.352 | 0.787 |
| IGN | 0.786 | 1.342 | 1.049 | 1.341 | 0.791 |
| GIGN | 0.788 | 1.351 | 1.045 | 1.336 | 0.792 |
| CAPLA | 0.799 | 1.324 | 1.063 | 1.307 | 0.797 |
| DeepTGIN | 0.834 | 1.203 | 0.949 | 1.197 | 0.823 |


↑ indicates that larger values indicate better performance, while ↓ indicates that smaller values indicate better performance. The best results are shown in bold

Results of the DeepTGIN model and other compared models on the PDBbind2013 test set



| Models | R( ↑ ) | RMSE( ↓ ) | MAE( ↓ ) | SD( ↓ ) | CI( ↑ ) |
| --- | --- | --- | --- | --- | --- |
| GraphDTA | 0.674 | 1.661 | 1.287 | 1.660 | 0.740 |
| DeepGLSTM | 0.676 | 1.654 | 1.276 | 1.651 | 0.742 |
| DeepDTAF | 0.728 | 1.581 | 1.277 | 1.547 | 0.769 |
| TEFDTA | 0.736 | 1.536 | 1.210 | 1.522 | 0.762 |
| IGN | 0.782 | 1.411 | 1.135 | 1.406 | 0.788 |
| GIGN | 0.780 | 1.407 | 1.133 | 1.409 | 0.780 |
| CAPLA | 0.744 | 1.524 | 1.233 | 1.502 | 0.767 |
| DeepTGIN | 0.787 | 1.388 | 1.123 | 1.386 | 0.792 |


↑ indicates that larger values indicate better performance, while ↓ indicates that smaller values indicate better performance. The best results are shown in bold


#### Comparison with other models on PDBbind 2013 test set

The experimental results of the compared models on the PDBbind2013 test set are presented in Table 4 . Our DeepTGIN model outperforms all other models in terms of all five evaluation metrics. Specifically, compared to IGN, DeepTGIN shows improvements of 0.6 % , 1.6 % , 1 % , 1.4 % , and 0.5 % in terms of R, RMSE, MAE, SD, and CI, respectively. Moreover, DeepTGIN achieves significant improvements of 16.7 % , 16.4 % , 12.7 % , 16.5 % , and 7 % over GraphDTA across the same metrics.

Based on these results, we attribute the improved performance of DeepTGIN to its effective utilization of protein pockets as crucial features for binding affinity prediction. IGN, GIGN, CAPLA, and DeepTGIN leverage protein pockets as key model inputs, demonstrating their effectiveness. While DeepDTAF also incorporates protein pockets, it does not emphasize the critical components of these pockets nor establish strong connections between protein pockets and ligands, resulting in comparatively poorer performance. IGN and GIGN are graph-based models, CAPLA is a sequence-based model, and DeepTGIN combines multimodal approaches, harnessing the strengths of both graph-based and sequence-based methodologies to achieve superior predictive accuracy.


### Results visualization


#### Visualization of model learning features

To gain deeper insights into the features learned by our model, we examined the outputs from the embedding layer, encoder module, and the second linear layer in MLP. Subsequently, we applied t-distributed Stochastic Neighbor Embedding (t-SNE) to reduce the high-dimensional representations into lower-dimensional visualizations, as depicted in Fig. 4 . Figure 4 A illustrates that many points of varying colors cluster closely together, appearing indistinguishable and sparsely distributed. In contrast, Fig. 4 B shows distinct clustering of dark and light points after passing through the encoder module. Finally, Fig. 4 C demonstrates improved separation of points with different colors after traversing two linear layers in MLP. These visualizations indicate that our model effectively learns to differentiate protein-ligand complexes based on their binding affinities, progressively refining its representations through successive layers of the model architecture.


> **Figure/Table Caption:** t-SNE visualization results. A The result after embedding layer. B The result after encoder module. C The output of the second linear layer in MLP


#### Attention visualization

To interpret the results of our model, we visualized attention scores and utilized PyMOL [ 45 ] to visualize a protein-ligand complex pair. Figure 5 A and B demonstrate that our model places significant attention on PRO residues (P) within both the protein and protein pocket regions. Notably, PRO residues exhibit the highest attention scores and are involved in crucial interactions with ligands. For instance, PRO151 forms a hydrogen bond with the ligand [ 46 ], while PRO152, PRO153, PRO219, PRO222, and PRO223 engage in hydrophobic interactions. The attention visualization highlights DeepTGIN’s capability to identify pivotal residues involved in protein-ligand binding, offering insights that can aid researchers in identifying critical residues efficiently and reducing experimental time costs.


> **Figure/Table Caption:** Visualization of attention scores: A Attention scores for protein. B Attention scores for protein pocket. C Visualization of a protein-ligand complex in PyMOL. Green residues represent important residues identified by DeepTGIN, while the yellow part denotes the ligand. Notably, PRO151 forms a hydrogen bond with the ligand


### Ablation study

To demonstrate the impact of protein pocket and ligand chemical properties on model performance, we performed two groups of ablation studies.


#### Protein pocket ablation studies

In the first group, we removed the input and transformer encoder of the protein pocket part, resulting in a model named DeepTGIN w i t h o u t _ p o c k e t . The results obtained by retraining are shown in Tables 5 and 6 . According to Table 5 , the five evaluation metrics all decrease to varying degrees without the pocket feature. Specifically, the R-value decreased by 13.6 % , the RMSE increased by 26.3 % , the MAE increased by 24.7 % , the SD increased by 25.8 % , and the CI decreased by 7.6 % . According to Table 6 , DeepTGIN w i t h o u t _ p o c k e t , the R-value decreased by 18.5 % , the RMSE increased by 24.8 % , the MAE increased by 23.5 % , the SD increased by 24.5 % , and the CI decreased by 19 % .

The ablation experimental result on the PDBbind2016 test set



| Models | R( ↑ ) | RMSE( ↓ ) | MAE( ↓ ) | SD( ↓ ) | CI( ↑ ) |
| --- | --- | --- | --- | --- | --- |
| DeepTGIN w i t h o u t _ p o c k e t | 0.720 | 1.520 | 1.184 | 1.506 | 0.760 |
| DeepTGIN w i t h o u t _ l i g a n d | 0.723 | 1.512 | 1.185 | 1.501 | 0.763 |
| DeepTGIN cnn | 0.745 | 1.458 | 1.132 | 1.449 | 0.769 |
| DeepTGIN lstm | 0.725 | 1.502 | 1.130 | 1.495 | 0.763 |
| DeepTGIN | 0.834 | 1.203 | 0.949 | 1.197 | 0.823 |


↑ indicates that larger values indicate better performance, while ↓ indicates that smaller values indicate better performance

The ablation experimental result on the PDBbind2013 test set



| Models | R( ↑ ) | RMSE( ↓ ) | MAE( ↓ ) | SD( ↓ ) | CI( ↑ ) |
| --- | --- | --- | --- | --- | --- |
| DeepTGIN w i t h o u t _ p o c k e t | 0.641 | 1.733 | 1.387 | 1.726 | 0.641 |
| DeepTGIN w i t h o u t _ l i g a n d | 0.686 | 1.653 | 1.349 | 1.635 | 0.748 |
| DeepTGIN cnn | 0.700 | 1.610 | 1.304 | 1.605 | 0.748 |
| DeepTGIN lstm | 0.674 | 1.670 | 1.312 | 1.661 | 0.737 |
| DeepTGIN | 0.787 | 1.388 | 1.123 | 1.386 | 0.792 |


↑ indicates that larger values indicate better performance, while ↓ indicates that smaller values indicate better performance

To prove the effect of the Transformer encoder on protein pocket sequences, we used CNN and LSTM to learn the sequence features of protein pockets, and the results obtained after retraining are shown in Tables 5 and 6 , named DeepTGIN cnn and DeepTGIN lstm . Using CNN to learn sequence features of pockets, the R, RMSE, MAE, SD, and CI on the PDBbind2016 test set varied by 10.6 % , 21.1 % , 19.2 % , 21 % and 6.5 % respectively. On the PDBbind2013 test set, they varied by 11 % , 15.9 % , 16.1 % , 15.8 % , and 5.5 % . We replace CNN with LSTM, and compare the results on the PDBbind2016 test set, showing variations of 13 % , 24.8 % , 19 % , 19.8 % , and 6.9 % . On the PDBbind2013 test set, they varied by 14.3 % , 20.3 % , 16.8 % , 19.8 % , and 6.9 % .


#### Ligand properties ablation studies

In the second group, we modified the input features of the ligand graph part, and we reduced the 10 properties per atom to 5, the same as GraphDTA [ 24 ]. The properties we removed were c h i r a l t a g , f o r m a l c h a r g e , n u m b e r o f r a d i c a l e l e c t r o n s , hybridization , and i s i n r i n g . The results are shown in the Tables 5 and 6 , named DeepTGIN w i t h o u t _ l i g a n d . From Table 5 we can see, that the results of five evaluation metrics also showed varying degrees of decline. The R value decreased by 13.3 % , the RMSE increased by 25.6 % , the MAE increased by 24.8 % , the SD increased by 25.3 % , and the CI decreased by 7.2 % . From Table 6 , the R value decreased by 12.8 % , the RMSE increased by 19 % , the MAE increased by 20.1 % , the SD increased by 17.9 % , and the CI decreased by 5.8 % .

In summary, the incorporation of protein pockets and the careful selection of properties of ligand atoms can markedly improve the performance of the model. With the advancement of technology, we anticipate that integrating additional chemical characteristics of ligand atoms as input to the ligand graph may yield even better results.


## Conclusion

This study presents DeepTGIN, a hybrid multimodal approach that integrates transformers and GINs for predicting protein-ligand binding affinity. DeepTGIN effectively combines the advantages of sequence-based and graph-based models, utilizing transformers to extract features from protein sequences and protein pockets, and graph isomorphism networks to capture features from ligands. The architecture of DeepTGIN, consisting of a data representation module, an encoder module, and a prediction module, facilitates efficient learning of both sequential and graph features, improving the model’s predictive capabilities. Evaluation of the PDBbind 2016 and PDBbind 2013 core sets shows that DeepTGIN surpasses state-of-the-art models in terms of R, RMSE, MAE, SD, and CI metrics. Ablation studies confirm the importance of ligand atomic properties and the encoder module in boosting the model’s performance, highlighting their crucial roles in achieving accurate predictions. DeepTGIN marks a significant improvement in protein-ligand binding affinity prediction. Its robust framework lays the foundation for incorporating additional chemical characteristics of ligand atoms, potentially leading to further advancements in drug discovery.


## Supplementary Information


## Abbreviations

Protein-ligand affinity

Simplified Molecular Input Line Entry System

Convolutional neural network

Multi-layer perceptron

Long short-term memory

Fully connected neural network

Graph isomorphism network

Pearson correlation coefficient

Root mean square error



GW derived the concept. HZ wrote most of the code and performed preliminary experiments. GW wrote the main manuscript. HZ, MS and YF helpted refining manuscript. CC and XH provided financial support, supervised the entire work process and guided the research direction. All authors reviewed and refined the manuscript.


## Funding

The research is supported by the National Natural Science Foundation of China (Grant No.62102068 and 62231013), the Natural Science Foundation of Jilin Province (Grant No.YDZJ202201ZYTS424), the Project of Education Department of Jilin Province named “Research on drug interaction prediction method based on graph node sequence representation”


## Availability of data and materials

The dataset used in this study is sourced from PDBBind ( http://pdbbind.org.cn/ ). Our code and related data are publicly available on Github ( [GITHUB_REPO_REDACTED] )


## Declarations


### Ethics approval and consent to participate


### Consent for publication


### Materials availability


### Competing interests

The authors report no Competing interests.


## Footnotes

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


## Contributor Information

Chen Cao, Email: [EMAIL_REDACTED].

Xiaowen Hu, Email: [EMAIL_REDACTED].

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials


### Data Availability Statement

The dataset used in this study is sourced from PDBBind ( http://pdbbind.org.cn/ ). Our code and related data are publicly available on Github ( [GITHUB_REPO_REDACTED] )
