# De-Identified Manuscript `OOD_ANON_04`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Drug-target interactions (DTIs) are pivotal in drug discovery and development, and their accurate identification can significantly expedite the process. Numerous DTI prediction methods have emerged, yet many fail to fully harness the feature information of drugs and targets or address the issue of feature redundancy. We aim to refine DTI prediction accuracy by eliminating redundant features and capitalizing on the node topological structure to enhance feature extraction. To achieve this, we introduce a PCA-augmented multi-layer heterogeneous graph-based network that concentrates on key features throughout the encoding-decoding phase. Our approach initiates with the construction of a heterogeneous graph from various similarity metrics, which is then encoded via a graph neural network. We concatenate and integrate the resultant representation vectors to merge multi-level information. Subsequently, principal component analysis is applied to distill the most informative features, with the random forest algorithm employed for the final decoding of the integrated data. Our method outperforms six baseline models in terms of accuracy, as demonstrated by extensive experimentation. Comprehensive ablation studies, visualization of results, and in-depth case analyses further validate our framework’s efficacy and interpretability, providing a novel tool for drug discovery that integrates multimodal features.

Keywords: DTIs prediction, Heterogeneous graph attention networks, Feature concatenation, PCA, Random forest


## Introduction

Drug development is a lengthy, expensive, and high-risk complex process that encompasses several key stages, including discovery, development, clinical trials, and marketing. In recent years, with advancements in science and technology and improvements in data analysis methods, researchers have been able to predict associations between drugs and targets more accurately, significantly shortening development cycles and enhancing the efficiency of drug development. However, traditional methods for determining drug-target interactions (DTIs) are often time-consuming, labor-intensive, and costly. Therefore, it is crucial to develop efficient computational methods for predicting drug-target associations.

In recent years, computational methods have proven to be effective in several tasks within the field of bioinformatics, such as predicting disease-related miRNAs [ 1 , 2 ],predicting drug-target affinity [ 3 ],identifying potential disease-related genes [ 4 ] and disease-associated lncRNAs [ 5 – 7 ],predicting drug-drug interactions [ 8 ], protein-protein interactions [ 9 ], and specific protein localization within cells [ 10 ]. Some existing models in the field of drug discovery [ 11 , 12 ] have been successfully applied to DTI prediction tasks through further expansion and optimization, demonstrating their effectiveness and efficiency. DTI computational prediction has enormous research potential and broad application prospects, offering advantages such as short time, low cost, high precision, and wide range in uncovering potential DTIs [ 13 ].

According to different methods, existing prediction models can mainly be divided into four categories: molecular docking-based methods, text mining-based methods, ligand-based methods, and chemogenomics-based methods. Molecular docking-based methods predict binding situations by simulating the physical and chemical interactions between drug molecules and target proteins [ 14 ], which have high biological interpretability. Text mining-based methods make predictions by extracting and analyzing relevant information from scientific literature, patents, and databases [ 15 ]. Ligand-based methods use the characteristics of known active ligands to predict new drug-target interactions through similarity searching and modeling [ 16 ], allowing for rapid predictions and suitable for high-throughput screening. Chemogenomics-based methods [ 17 ] integrate chemical and genomic data to predict drug-target interactions by constructing chemical-biological networks. Depending on the implementation, these methods can be further refined into similarity-based, pharmacological characteristic-based, and network-based methods [ 18 , 19 ]. Similarity-based methods include the nearest neighbor method [ 20 , 21 ], bipartite local model (BLM) [ 22 , 23 ], and matrix factorization methods [ 24 ]. Network-based methods make associative predictions by constructing and analyzing network structures, which can be divided into binary network methods [ 25 ] and heterogeneous network methods [ 26 , 27 ] according to different network topologies. Currently, many DTI prediction methods combine deep learning with heterogeneous networks [ 28 – 33 ]. Deep learning-based methods utilize the advantages of neural networks to automatically learn the features of nodes and the complex relationships between nodes.

Recently, a method combining metapath-based graph convolutional networks with large-scale heterogeneous networks to effectively learn representations of drugs and target proteins [ 34 ] has been proposed. Additionally, a metapath-based hierarchical transformer combined with an attention network for drug-target interaction prediction [ 35 ] has been proposed. This method applies a metapath instance-level transformer, single-semantics attention, and multi-semantics attention to generate low-dimensional vector representations of drugs and proteins. Additionally, the CFSSynergy method, which combines feature-based and similarity-based approaches, demonstrates outstanding performance in drug synergy prediction [ 36 ]. This method extracts discriminative features from drugs and cell lines, utilizes the Node2Vec algorithm to compute protein similarities, and ultimately feeds these features into XGBoost for prediction. Furthermore, the methods of constructing heterogeneous knowledge graphs, employing heterogeneous graph transformer networks, and calculating relationship scores using fully connected networks have also proven to be highly effective [ 37 ], further highlighting the potential of heterogeneous graph neural networks in diverse applications. These studies still do not fully exploit the feature information of drugs and targets in DTI prediction, and the associations in heterogeneous biological information networks have not been fully utilized. At the same time, issues such as redundant features and low robustness of decoding methods have not been addressed. How to effectively utilize the topological structure between nodes to deeply mine feature information for DTI prediction remains an urgent problem to be solved. We aim to address the issue of redundant features and effectively leverage the topological structure among nodes to deeply mine feature information for DTI prediction.Therefore, we propose a framework MHAPR that constructs highly integrated multi-level information by concatenating feature vectors obtained from each convolutional layer in a multimodal heterogeneous graph attention network and then combines feature optimizer PCA [ 38 ] and random forest algorithm [ 39 , 40 ].

More specifically, MHAPR first constructs a heterogeneous graph from various similarity information between drugs and targets, using the heterogeneous graph as input to the graph neural network for encoding. By aggregating heterogeneous nodes through the graph attention mechanism and setting up a multi-head self-attention mechanism and metapath weighting strategy, deep integration of multi-source similarity information in the heterogeneous graph is achieved. Then, the aggregated representation vectors of the heterogeneous graph neural networks with self-attention are concatenated, preserving multi-level representation information. Subsequently, we apply various effective feature selection methods to the representation encoding for feature selection and finally use Principal Component Analysis (PCA) to improve the quality of features. Compared to traditional models, MHAPR places greater emphasis on extracting key feature information and enhances the model’s generalization ability through the robust ensemble learning mechanism of the random forest algorithm.In summary, our main contributions to this work are as follows:

Multimodal information fusion By constructing a concatenated multi-layer heterogeneous graph attention network, we integrated various similarity information from drugs and targets (such as sequence and Gaussian similarity), enabling deep extraction and fusion of heterogeneous node representations. This method effectively captures the complex interactions between drugs and targets.

Feature selection and optimization Through extensive experimentation, we demonstrated that different feature selection methods significantly enhance the quality of representation encoding. We explored their impact on improving multimodal biological information capabilities, providing theoretical support for feature optimization.

Selection of feature dimensionality reduction By comparing four dimensionality reduction algorithms, we ultimately chose PCA as the feature optimizer, aiming to reduce feature redundancy and computational complexity while ensuring the model focuses on key biological information, thereby enhancing prediction accuracy and reliability.

Enhancing model robustness The reduced features were input into a random forest algorithm, leveraging its powerful ensemble learning mechanism to improve the model’s tolerance to data noise, thereby enhancing overall robustness. This strategy ensures the model’s stability and practicality in real-world applications.


## Method and materials


### Data collection

To validate the generalizability of our model, we downloaded two drug-target protein datasets for benchmarking from references [ 41 , 42 ], both sourced from relevant databases. The first dataset, named the FSL dataset, is derived from the work of Tangmanussukum et al. [ 42 ] After removing duplicate relationships, it contains 862 drugs, 1,517 target proteins, and 3,583 known DTIs. The second dataset, named the DC dataset, is sourced from the work of Peng [ 41 ]. Drug nodes, known DTIs, and drug-drug interactions were extracted from the DrugBank database [ 43 ], while protein nodes and protein-protein interactions were extracted from the HPRD database [ 44 ]. This resulted in 708 drug samples, 1512 target protein samples, and 1923 known DTIs,Table 1 provides a detailed description of the datasets.


#### Table 1.



| Datasets | Proteins | Drugs | Interactions | Interaction proportion (%) |
| --- | --- | --- | --- | --- |
| DC | 708 | 1512 | 1923 | 0.17 |
| FSL | 1517 | 862 | 3583 | 0.27 |


We found that the number of unknown association samples far exceeds the known ones, with a significant amount of noisy data. To mitigate noise and ensure dataset balance, we labeled all known drug-target protein associations as positive 1 and randomly selected an equal number of negative samples, labeling them as 0. We then used five-fold cross-validation, with 80% of the samples for training and 20% for testing.


### Overview of processes

In bioinformatics research, biological information features that are noisy and high-dimensional often hinder models from capturing comprehensive and discriminative relationships within the data. Therefore, based on extensive comparative experiments and comprehensive consideration of the effectiveness of various feature combinations and their computational complexity, we propose a three-layer computational framework based on HAN-PCA-RF for predicting potential drug-target interactions. Figure 1 provides a detailed illustration of the DTI-MHAPR workflow, which specifically includes the following steps:

Constructing a heterogeneous graph from target protein sequence similarity, Gaussian similarity, drug structure similarity, Gaussian similarity matrices, and known DTIs information. This heterogeneous graph effectively represents the multifaceted relationships between different types of nodes and edges.

After applying a linear transformation and ReLU activation to the embeddings of different nodes, a graph neural network is used to encode the heterogeneous graph, incorporating multi-head self-attention mechanisms and meta-path weighting strategies to achieve deep integration of multi-source similarity information within the heterogeneous graph.

Concatenating the representation vectors obtained from multiple layers of the heterogeneous attention network to retain and integrate multi-level representation information.

PCA to project the original representation vectors onto the principal components, reducing the feature dimensions while focusing the model on key information.

Using the random forest algorithm to predict the final interaction scores between drugs and target proteins, leveraging its ensemble learning capabilities to handle high-dimensional data and capture nonlinear relationships effectively.


#### Fig. 1.


> **Figure/Table Caption:** Workflow diagram of DTI-MHAPR


### Multi-view similarity feature integration

To gain a deeper understanding of the similarity information between drugs and targets, we employed a multi-modal feature extraction approach. Initially, we applied the Gaussian kernel function to the topological structure association network between bioinformatic nodes [ 45 ]. This method allows us to obtain more accurate Gaussian interaction profile kernel similarities by computing the Gaussian interaction profile kernel similarity. Similarly, we applied the Gaussian kernel function to the drug structure similarity matrix to derive the Gaussian similarity matrix for drugs.

Subsequently, we performed integration of multi-view similarity matrices to extract similarity features between drug-drug and target-target. This integration process comprehensively considers the similarities from different data perspectives, providing a more holistic and precise similarity assessment.



| M t = mean { S t , G t } | 1 |
| --- | --- |




| M d = mean { S d , G d } | 2 |
| --- | --- |


where the drug structure similarity matrix S t ∈ R T × T , the Gaussian similarity matrix G t ∈ R T × T ; the target sequence similarity matrix S d ∈ R D × D , and the Gaussian similarity matrix G d ∈ R D × D .


### Heterogeneous graph attention network

HAN [ 46 , 47 ] applies the popular multi-head self-attention mechanism to the metapath node feature representation of a heterogeneous graph, then uses semantic-level attention to weight and aggregate the metapath attention, obtaining the final semantic representation that includes node features and domain structure features. In a heterogeneous graph, drugs can reach other drugs or targets can reach other targets through different paths, which are called metapaths.In this paper, two types of meta-paths are considered: drug-edge-target and target-edge-drug.

In our in-depth study of the node-level attention framework, we focused on how to effectively process and integrate information from diverse metapath neighbors to construct richer and more meaningful embedding representations for each drug and target node. In this process, the node-level attention mechanism plays a crucial role, allowing the model to dynamically consider the importance of each neighbor node when aggregating neighbor information, thereby enhancing the model’s expressiveness and adaptability. First, we use a specific type of transformation matrix M ϕ i for each type of node to project the features of different types of nodes into the same feature space. The projection process is as follows:



| h i ′ = M ϕ i · h i | 3 |
| --- | --- |


In the context of self-attention mechanism, h i represents the original features of node i , and h i ′ denotes the projected features. Using self-attention allows dynamic learning of relationship weights between different nodes, enhancing the model’s understanding of relative importance among various node pairs. Within the self-attention framework, the importance of node pairs (i, j), especially those connected via specific metapaths ∅ i , can be represented by calculating their attention scores. This mechanism considers not only the nodes’ own features but also their interactions, thereby more accurately capturing dependencies and information flow between nodes. The computational formula is as follows:



| e ij ∅ = att node ( h i ′ , h j ′ ; ∅ ) | 4 |
| --- | --- |


Here,the node attention value e ij ∅ indicates the importance of node j to node i , while h i ′ and h j ′ represent the projected features of nodes i and j , respectively. att node represents a deep neural network that executes node-level attention. Then, structural information is injected into the model through masked attention. After obtaining the importance between node pairs based on meta-paths, these are normalized using the softmax function to obtain weight coefficients.)



| α ij ∅ = softmax j ( e ij ∅ ) = exp ( σ ( a ∅ T · [ h i ′ / / h j ′ ] ) ) ∑ k ∈ N i ∅ exp ( σ ( a ∅ T · [ h i ′ / / h k ′ ] ) ) | 5 |
| --- | --- |


The symbol | | represents the concatenation operation, a ∅ T is the node-level attention vector for the metapath ∅ , and α ij ∅ denotes the weight coefficient for each feature vector.The embedding z i ∅ based on the metapath ∅ for node i can be aggregated using the projected features of its neighboring nodes weighted by corresponding attention coefficients, and then passed through an activation function, as shown below:



| z i ∅ = σ ∑ k ∈ N i ∅ α ij ∅ · h j ′ | 6 |
| --- | --- |


Due to the scale-free nature of heterogeneous graphs and their high variance in data, to further optimize the information aggregation process, we employ a multi-head attention mechanism. This mechanism runs multiple attention “heads” in parallel, allowing the model to capture information in different subspaces. Each “head” focuses on different types of information. Through this approach, the model can achieve more comprehensive and in-depth learning by integrating information from multiple dimensions. Ultimately, the attention scores computed by these different “heads” are combined to generate a comprehensive and informative new feature representation for each node i :



| z i ∅ = ‖ k = 1 K σ ∑ j ∈ N i ∅ α ij ∅ · h j ′ | 7 |
| --- | --- |


After concatenating embeddings, we obtain a node embedding set for specific semantics, denoted as Z ( ∅ 1 ) , … , Z ( ∅ p ) . Each element of this specific semantic node embedding set serves as input. The learning weights for each metapath ( ω ( ∅ 1 ) , … , ω ( ∅ p ) ) are computed as follows:



| ( ω ( ∅ 1 ) , … , ω ( ∅ p ) ) = att sem ( { Z ( ∅ 1 ) , … , Z ( ∅ p ) } ) | 8 |
| --- | --- |


Here, att sem represents a deep neural network performing semantic-level attention.Next, we calculate the importance f ( ∅ i ) of each metapath ( ∅ i ) . First, we use a single-layer MLP followed by an activation function for nonlinear transformation. Then, we measure the importance of specific semantic embeddings by their similarity to the semantic-level attention vector q :



| f ( ∅ i ) = 1 / v / ∑ i ∈ v q T · tanh ( W · z i ( ∅ p ) + b ) | 9 |
| --- | --- |


For different tasks, metapaths ( ∅ p ) may have varying weights. By using learned weights as coefficients, we can integrate these specific semantic embeddings to obtain the final embedding vector Z , which combines the features of drugs and targets incorporating information from neighboring nodes:



| Z = ∑ P = 1 P ω ( ∅ p ) · Z ( ∅ p ) | 10 |
| --- | --- |


Here, ω ( ∅ p ) represents the normalized importance of each metapath.


### Feature optimiser

In our study, the multi-modal feature vectors extracted through the multi-layer heterogeneous graph attention network [ 46 ] contain rich information but also exhibit high dimensionality and a certain level of noise. To optimize these features and enable machine learning algorithms to more effectively learn discriminative information, we decided to use the PCA algorithm as a feature optimization tool within our framework.

Initially, we applied the heterogeneous graph attention network to extract a series of multi-modal feature vectors. Subsequently, we employed a strategy of concatenating feature vectors from various convolutional layers to integrate information from different levels. This process helps to maximize the retention of useful information while enhancing the diversity of features.



| Z M-view = Concat ( Z conv1 , Z conv2 , Z conv3 ) | 11 |
| --- | --- |


The vectors Z conv1 , Z conv2 , Z conv3 are feature vectors from different convolutional layers, and concat denotes the operation of concatenating these feature vectors from different layers. The vector Z M-view is the resulting concatenated representation.

During the feature optimization phase, we input the integrated feature vector Z M-view into the feature optimizer, compute the covariance matrix of the centered feature matrix, and then perform eigenvalue decomposition to select the principal components based on their eigenvalues. Through orthogonal transformation, PCA converts the originally potentially correlated feature vector variables into a set of linearly independent variables, thereby identifying the principal components of the data. This not only reduces the dimensionality of the data but also minimizes information loss to the greatest extent possible, effectively removing noise from the feature vectors.



| Z ~ M-view = Z M-view - μ col | 12 |
| --- | --- |




| C d - t = Z ~ M-view T · Z ~ M-view | 13 |
| --- | --- |




| W k = Sort { Decomp [ C d - t ] } | 14 |
| --- | --- |




| Z final = Z ~ M-view · W k | 15 |
| --- | --- |


Here,the vector μ col represents the mean vector for centering, and Z ~ M-view denotes the centered feature vector, which is obtained by subtracting the mean of each column from the original feature vectors to ensure that the mean of the data in each dimension is zero. This is a necessary step for performing PCA. C d - t represents the covariance matrix of the centered feature matrix, and W k is the transformation matrix. Decomp denotes the decomposition of the covariance matrix, and Sort refers to the process of sorting the eigenvectors by the magnitude of their corresponding eigenvalues. The transformation matrix is constructed by selecting the eigenvectors corresponding to the eigenvalues that collectively account for 99.80% of the cumulative variance contribution rate,the vector Z final is obtained by multiplying the centered feature vector Z ~ M-view with the transformation matrix W k . This represents the dimensionality-reduced feature representation after PCA processing, which retains the most important information in the data.

In practical applications, we selected a dimensionality reduction index of 0.9980, which means that we retained 99.8% of the data’s principal components. This choice was based on a trade-off between data simplification and information retention, ensuring that while significantly reducing data complexity, we preserved the vast majority of information critical to the model’s predictive performance. This step is crucial for enhancing the overall performance and prediction accuracy of the model, providing a solid foundation for deeply mining and understanding complex bioinformatics data.


### Classifier

After obtaining the optimized embedding vectors, we employ the random forest (RF) algorithm to predict the final drug-target interaction (DTI) associations. The RF algorithm introduces randomness during the training process to reduce the risk of overfitting, thereby exhibiting strong resistance to overfitting. Additionally, it consists of multiple trees, each trained on a different dataset, enabling the capture of various patterns in the data, which grants it a superior generalization capability compared to other machine learning algorithms.

The concatenated features resulting from the embedding process comprise M × N vectors, each with 2 × L in features. These features serve as the input to the random forest, which generates a series of decision trees. Through bootstrap aggregating, k samples are drawn with replacement from the dataset to form the training sets, and w decision trees are trained. Each training set contains duplicate samples. The final prediction value is obtained by aggregating the mean predictions of the w decision trees.



| T i ← Train ( X ( i ) ) , i = 1 , 2 , … , w | 16 |
| --- | --- |


where X ( i ) denotes the i -th generated training set.



| y ^ DTI = 1 w ∑ i = 1 w T i ( x ) | 17 |
| --- | --- |


where y ^ DTI is the predicted drug-target interaction value.

By utilizing this approach, the RF algorithm effectively aggregates the predictions from multiple decision trees, thereby enhancing the robustness and accuracy of the DTI association predictions.


## Experiments and results

To evaluate the accuracy of the MHAPR computational framework in predicting drug-target interactions, we compared its performance on two benchmark datasets with seven state-of-the-art baseline models: MNGACDA [ 48 ], GATECDA [ 49 ], MINIMDA [ 50 ], HFHLMDA [ 51 ], CGHCN [ 52 ],MIDTI [ 53 ] and DTI-CNN [ 41 ].

MNGACDA [ 48 ] constructs a multimodal network using various information sources from drugs and circRNA, and then applies an inner product decoder based on the embedding representations of drugs and circRNA to predict their interaction scores. GATECDA [ 49 ] employs a graph attention autoencoder (GATE) to extract low-dimensional representations of drugs/circRNA, effectively preserving key information from sparse high-dimensional features and realizing effective integration of node neighborhood information. MINIMDA [ 50 ] constructs an integrated disease similarity network and miRNA similarity network using multiple information sources, then combines mixed high-order neighborhood information from multimodal networks to obtain disease and miRNA embeddings, and finally uses a multi-layer perceptron (MLP) for prediction. HFHLMDA [ 51 ] utilizes a hypergraph learning model to learn a projection matrix for calculating the association scores of uncertain diseases and miRNAs. CGHCN [ 52 ] combines graph convolutional networks and hypergraph convolutional networks, while DTI-CNN [ 41 ] leverages the Jaccard similarity coefficient and random walk model to obtain feature embeddings, and then uses convolutional neural networks to predict drug-target protein interactions after dimensionality reduction.The MIDTI method [ 53 ] first utilizes graph convolutional networks (GCNs) to simultaneously obtain the embedding representations of drugs and targets from multi-type networks. Then, it employs a deep interactive attention mechanism to further learn the discriminative embeddings of drugs and targets while fully considering the known DTI relationships.

To ensure fair and accurate results, we used the same similarity data for the baseline methods, specifically drug structure similarity, drug Gaussian similarity, target sequence similarity, and target Gaussian similarity. For the single-modal models CGHCN [ 52 ] and HFHLMDA [ 51 ], we only used the drug-target similarity matrix as training data.

To verify the generalizability of the model, we split the two benchmark datasets into training and testing sets with a 4:1 ratio, and applied 5-fold cross-validation (5-CV) on the training set to adjust the model parameters and structure. During the training process, for the FSL dataset, the embedding dimension was set to 1024, the number of attention mechanism heads to 4, and the number of layers in the heterogeneous attention network to 6. For the DC dataset, the embedding dimension was set to 512, the number of attention mechanism heads to 6, and the number of layers in the heterogeneous attention network to 4. The number of training epochs was set to 500, and the Adam optimizer was used. The optimal hyperparameter combination was a learning rate of 0.001 and a weight decay rate of 0.0002. Additionally, the dropout rate was set to 0.5 to randomly ignore some neurons, preventing overfitting.


### Performance evaluation of the DC dataset

On the DC dataset, we trained the model using five-fold cross-validation. As shown in Table 2 and Fig. 2 , compared to other methods, the DTI-MHAPR computational framework achieved significant improvements across six evaluation metrics, except for Recall. Notably, it also attained a commendable score in Recall.


#### Table 2.

Comparison of performance using 5-CV on the DC dataset



| Method | Auc | Aupr | F1-score | Acc | Recall | Spec | Precision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CGHCN | 0.9001 | 0.9007 | 0.8370 | 0.8309 | 0.8664 | 0.7956 | 0.8107 |
| DTI-CNN | 0.9358 | 0.9423 | 0.8636 | 0.9412 | 0.8685 | 0.8726 | 0.8148 |
| GATECDA | 0.7918 | 0.8000 | 0.7501 | 0.7205 | 0.8270 | 0.6170 | 0.7011 |
| HFHLMDA | 0.8411 | 0.7529 | 0.8042 | 0.7938 | 0.8465 | 0.7407 | 0.7662 |
| MINIMDA | 0.9537 | 0.9359 | 0.9074 | 0.9030 | 0.9491 | 0.8569 | 0.8695 |
| MNGACDA | 0.8927 | 0.7500 | 0.9031 | 0.8928 | 1.0000 | 0.7854 | 0.8234 |
| MIDTI | 0.9769 | 0.9615 | 0.9609 | 0.9583 | 0.9938 | 0.9236 | 0.9285 |
| Our model | 0.9950 | 0.9941 | 0.9738 | 0.9735 | 0.9875 | 0.9595 | 0.9606 |



#### Fig. 2.


> **Figure/Table Caption:** Visualisation of AUC and AUPR values compared with the baseline model on the 5-CV


### Performance evaluation of the FSL dataset

In addition to the aforementioned seven methods, we also compared our results with those obtained using the Heterogeneous Network that employs the Forward Similarity Integration (FSI) algorithm [ 42 ] on this dataset. We conducted five-fold cross-validation experiments and the results are presented in Table 3 , showcasing the model’s performance across seven evaluation metrics. Figure 3 visualizes the training curves. It can be observed that the DTI-MHAPR computational framework achieved an AUC of 98.90% and an AUPR of 98.69%, demonstrating significant improvements.


#### Table 3.

Comparison of performance using 5-CV on the FSL dataset



| Method | Auc | Aupr | F1-score | Acc | Recall | Spec | Precision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CGHCN | 0.9058 | 0.9061 | 0.8441 | 0.8456 | 0.8375 | 0.8542 | 0.8524 |
| GATECDA | 0.9146 | 0.9276 | 0.8372 | 0.8396 | 0.8266 | 0.8520 | 0.8497 |
| HFHLMDA | 0.8875 | 0.8715 | 0.8217 | 0.8145 | 0.8547 | 0.7740 | 0.7922 |
| MINIMDA | 0.9408 | 0.9198 | 0.8898 | 0.8840 | 0.9356 | 0.8327 | 0.8489 |
| MNGACDA | 0.9674 | 0.9629 | 0.9086 | 0.9035 | 0.9585 | 0.8474 | 0.8640 |
| MIDTI | 0.9634 | 0.9578 | 0.9032 | 0.8997 | 0.9497 | 0.8676 | 0.8831 |
| Our model | 0.9890 | 0.9869 | 0.9544 | 0.9535 | 0.9778 | 0.9295 | 0.9324 |



#### Fig. 3.


> **Figure/Table Caption:** Visualisation of AUC and AUPR values compared with the baseline model on the 5-CV

In summary, these experiments conducted on two independent datasets indicate that the performance of DTI-MHAPR surpasses all other tested methods. This demonstrates the broad applicability of our approach, effectively enhancing the prediction of drug-target interactions (DTIs).


### Dimensionality reduction analysis

The DC dataset contains 708 drugs and 1512 target proteins, while the FSL dataset includes 862 drugs and 1517 target proteins. Consequently, the dimensionality of the multi-modal feature vectors obtained after feature fusion is extremely high. Handling such high-dimensional data poses significant challenges for the model. However, much of this data is highly redundant. By employing dimensionality reduction algorithms, we can focus the network layers on key information, enabling the model to learn more discriminative features. Based on prior research, we experimented with various types of dimensionality reduction algorithms, including both linear and nonlinear methods. By comparing different algorithms and analyzing the performance of the model with varying dimensionality reduction parameters, we identified the optimal parameters for the model.


#### An exploration of dimensionality reduction algorithms

Feature engineering is an important preprocessing step that helps to extract transformational features from raw data to simplify machine learning models and improve the quality of machine learning algorithm results.Machine learning practitioners spend most of their time on data cleaning and feature engineering, so we are inspired to focus on the investigation of downscaling optimisation of the multimodal features mined by the HAN network, and the experimental steps are as follows:

1) Using segmented sampling method and dense sampling method to apply PCA [ 38 ], t-SNE [ 54 ], LLE (Locally Linear Embedding) [ 55 ], FastICA (Fast Independent Component Analysis) [ 56 ] algorithms are applied to the normalised dataset and the resulting dimensionality reduced dataset is experimented with using the ML algorithm.

2) Analyse the results obtained by the linear dimensionality reduction algorithms PCA, FastICA and the nonlinear dimensionality reduction algorithms LLE, t-SNE after dimensionality reduction using the ML algorithm, and investigate the effect of dimensionality reduction on the prediction performance of the ML algorithm with respect to DTIs.

After conducting the experiments, we obtained the results shown in Tables 4 and 5 , with optimal values selected after intensive sampling. Among them, DRA represents different types of dimensionality reduction algorithms. The optimal AUC and AUPR values for PCA on the DC dataset are higher than those of the other three dimensionality reduction algorithms, reaching 99.50% and 99.41%, respectively. The two evaluation indexes of the PCA algorithm are also superior to the other algorithms on the FSL dataset, and only the AUC value of the t-SNE The AUC value of PCA algorithm is slightly higher than that of t-SNE algorithm.

Comparison of PCA dimensionality reduction versus t-SNE dimensionality reduction on the DC dataset



| DRA | Optimal AUC | Optimal AUPR | Best_n_components |
| --- | --- | --- | --- |
| PCA | 0.9950 | 0.9941 | 0.9980 |
| t-SNE | 0.9927 | 0.9912 | 3 |
| LLE | 0.9943 | 0.9933 | 70 |
| FastICA | 0.9882 | 0.9875 | 32 |


Comparison of PCA dimensionality reduction versus t-SNE dimensionality reduction on the FSL dataset



| DRA | Optimal AUC | Optimal AUPR | Best_n_components |
| --- | --- | --- | --- |
| PCA | 0.9890 | 0.9869 | 0.9980 |
| t-SNE | 0.9891 | 0.9867 | 3 |
| LLE | 0.9886 | 0.9860 | 24 |
| FastICA | 0.9872 | 0.9868 | 48 |


We found that t-SNE algorithm needs to calculate the similarity between the samples in each iteration, and the time complexity required in processing a large amount of data is much larger than that of PCA. Therefore, considering the accuracy and time complexity of the prediction of DTIs, the use of PCA algorithm as the feature optimisation algorithm of our DTIs prediction framework is suitable for us. Therefore, considering the accuracy and time complexity of DTIs prediction, it is suitable to use PCA as our feature optimisation algorithm for DTIs prediction framework.


#### An investigation of the effect of PCA downscaling index on DTI prediction accuracy

After exploring two sets of advanced dimensionality reduction algorithms (linear and nonlinear), the result obtained is that PCA dimensionality reduction is superior to several other dimensionality reduction algorithms, next we will focus our attention on PCA dimensionality reduction (dense sampling after segmented sampling method).

PCA finds the main direction of the data by calculating the covariance matrix of the original data, and then solves for the eigenvalues and eigenvectors of this covariance matrix using eigenvalue decomposition. The eigenvalues represent the variance of the data in the direction of the eigenvectors, while the eigenvectors represent the main distribution of the data in each direction. It will select the eigenvectors with the largest eigenvalues as the principal components, and map the data onto the subspaces tensored by the principal components, thus achieving the purpose of data dimensionality reduction. For PCA dimensionality reduction index the experimental results are as follows Tables 6 and 7 .Among them, DC denotes the percentage of principal components retained by the PCA algorithm.

Dimensionality reduction analysis on the DC dataset



| DC | AUC | PRC | F1_Score | Acc | Recall | Specificity | Precision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| None | 0.9808 | 0.9800 | 0.9225 | 0.9212 | 0.9396 | 0.9029 | 0.9072 |
| 0.9980 | 0.9950 | 0.9941 | 0.9738 | 0.9735 | 0.9875 | 0.9595 | 0.9606 |
| 0.9960 | 0.9941 | 0.9929 | 0.9722 | 0.9719 | 0.9845 | 0.9596 | 0.9603 |
| 0.9940 | 0.9939 | 0.9928 | 0.9714 | 0.9711 | 0.9823 | 0.9601 | 0.9607 |
| 0.9920 | 0.9936 | 0.9925 | 0.9689 | 0.9685 | 0.9833 | 0.9538 | 0.9550 |


Dimensionality reduction analysis on the FSL dataset



| DC | AUC | PRC | F1_Score | Acc | Recall | Specificity | Precision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| None | 0.9825 | 0.9822 | 0.9239 | 0.9228 | 0.9351 | 0.9105 | 0.9140 |
| 0.9980 | 0.9890 | 0.9869 | 0.9544 | 0.9535 | 0.9778 | 0.9295 | 0.9324 |
| 0.9960 | 0.9862 | 0.9835 | 0.9480 | 0.9468 | 0.9722 | 0.9220 | 0.9253 |
| 0.9940 | 0.9787 | 0.9724 | 0.9332 | 0.9305 | 0.9742 | 0.8872 | 0.8960 |
| 0.9920 | 0.9756 | 0.9682 | 0.9292 | 0.9266 | 0.9672 | 0.8855 | 0.8941 |


It can be seen that on the DC dataset, the PCA dimensionality reduction index between 0.9920 and 0.9980 will play a role in eliminating redundant information in the data, improving the efficiency of data representation, and can reduce the cost of computation and storage, especially when the dimensionality reduction index is 0.9980 (i.e., 99.8% of the principal components are retained), the AUC value on this dataset reaches 99.50%, the The AUPR value reaches 99.41%, and the other five metrics are all improved in different magnitudes relative to no dimensionality reduction;

On the FSL dataset, the downscaling indices between 0.9960 - 0.9980 are better optimised for multimodal features, similarly, when the downscaling index is 0.9980, the AUC value reaches 98.90%, the AUPR value reaches 98.69%, and the other five evaluation metrics are also improved in different magnitudes compared to no downscaling.

Despite the fact that the heterogeneous graph network consists of nonlinear data, the feature matrix input to the PCA algorithm remains linear after feature extraction using HAN. It is important to note that PCA assumes the data follows a linear distribution, so it may fail when the data has a nonlinear structure. Additionally, the results of PCA are influenced by eigenvalue decomposition, and for high-dimensional data, approximate calculations of eigenvalue decomposition may be required, increasing computational complexity.

Notwithstanding these challenges, we achieved good results on both datasets, demonstrating that the PCA dimensionality reduction algorithm effectively optimizes features. Moreover, applying the PCA algorithm with a dimensionality reduction index of 0.9980 significantly improved the classification performance of multimodal data features in machine learning. Taking the DC dataset as an example, the embedding dimensions of drug and target features were 1536 before dimensionality reduction. Notably, since the data for each fold is reduced to different dimensions during the dimensionality reduction process, the final embedding dimensions of each fold vary. In five-fold cross-validation, the embedding dimensions for drug nodes were 8, 9, 10, 9, and 11, while for target nodes, they were 9, 8, 10, 9, and 12. For the FSL dataset, the embedding dimensions for drug nodes were 4, 6, 5, 6, and 4, while for target nodes, they were 3, 6, 5, 6, and 2.


### Choice of classifier

We explore the classification effectiveness of seven machine learning algorithms on two datasets using grid point search. The evaluation metrics of the machine learning algorithms on five-fold cross-validation are shown in Tables 8 and 9 , and their AUC vs. AUPR graphs are shown in Figs. 4 and 5 . In the table, RF outperforms all other algorithms in five of the seven metrics and has the highest values of AUC vs. AUPR among the seven algorithms, indicating that the Random Forest algorithm outperforms other machine learning algorithms on both datasets. Therefore, we choose the random forest algorithm for supervised learning to perform DTI prediction. SVM refers to support vector machine, RF refers to random forest, XGB refers to eXtreme gradient boosting, KNN refers to K-nearest neighbors, DT refers to decision tree, LR refers to logistic regression, and NB refers to Naive Bayes.


#### Table 8.

Performance of different machine learning algorithms for 5-CV on the FSL dataset



| Classifier | AUC | PRC | F1_Score | Acc | Recall | Spec | Precision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KNN | 0.9493 | 0.9377 | 0.8939 | 0.8859 | 0.9650 | 0.8062 | 0.8329 |
| NB | 0.8969 | 0.8414 | 0.8483 | 0.8256 | 0.9773 | 0.6730 | 0.7497 |
| SVM | 0.9724 | 0.9434 | 0.9489 | 0.9477 | 0.9758 | 0.9200 | 0.9241 |
| LR | 0.8941 | 0.8124 | 0.8587 | 0.8468 | 0.9339 | 0.7601 | 0.7967 |
| RF | 0.9890 | 0.9869 | 0.9544 | 0.9535 | 0.9778 | 0.9295 | 0.9324 |
| DT | 0.9423 | 0.8955 | 0.9438 | 0.9282 | 0.9251 | 0.9711 | 0.8800 |
| XGB | 0.9842 | 0.9787 | 0.9542 | 0.9534 | 0.9763 | 0.9305 | 0.9331 |



#### Table 9.

Performance of different machine learning algorithms for 5-CV on the DC dataset



| Classifier | AUC | PRC | F1_Score | Acc | Recall | Spec | Precision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KNN | 0.9659 | 0.9570 | 0.9317 | 0.9269 | 0.9952 | 0.8583 | 0.8761 |
| NB | 0.9301 | 0.8844 | 0.9009 | 0.8900 | 0.9995 | 0.7804 | 0.8201 |
| SVM | 0.9850 | 0.9754 | 0.9706 | 0.9704 | 0.9807 | 0.9600 | 0.9608 |
| LR | 0.9402 | 0.8672 | 0.9262 | 0.9210 | 0.9921 | 0.8495 | 0.8686 |
| RF | 0.9950 | 0.9941 | 0.9738 | 0.9735 | 0.9875 | 0.9595 | 0.9606 |
| DT | 0.9569 | 0.9227 | 0.9512 | 0.9501 | 0.9760 | 0.9242 | 0.9278 |
| XGB | 0.9926 | 0.9898 | 0.9715 | 0.9711 | 0.9870 | 0.9554 | 0.9566 |



#### Fig. 4.


> **Figure/Table Caption:** AUC and AUPR curves for seven machine learning algorithms on the DC dataset


#### Fig. 5.


> **Figure/Table Caption:** AUC and AUPR curves for seven machine learning algorithms on the FSL dataset

The random forest algorithm has two critical parameters: n_estimators and max_depth. Generally, increasing n_estimators enhances the model’s performance but also raises computational costs. The max_depth parameter controls the complexity of the trees, thereby preventing overfitting. We employed grid search to determine the optimal parameters for RF within the MHAPR framework.

As illustrated in Fig. 6 , for the FSL dataset, the model achieves the highest AUC and AUPR values when max_depth is set to 20 and n_estimators is 300. For the DC dataset, shown in Fig. 7 , the model reaches its optimal performance with a max_depth of 20. The AUC achieves its peak when n_estimators is 500, while the AUPR continues to show minor improvements up to n_estimators of 800. However, since the AUPR increases marginally beyond n_estimators of 500 and the model complexity significantly increases, we determined that the optimal parameters for the DC dataset are n_estimators of 500 and max_depth of 20.


#### Fig. 6.


> **Figure/Table Caption:** Parameter grid search on the DC dataset


#### Fig. 7.


> **Figure/Table Caption:** Parameter grid search on the FSL dataset


### Ablation experiment

To evaluate the effectiveness of various modules within the MHAPR computational framework, we proposed three model variants: MHAPR-PCA, MHAPR-dropout, and MHAPR-concat. By controlling for major variables, we systematically excluded the PCA layer, dropout layer, and concat layer from the framework to understand the performance of each module within DTI-MHAPR. To assess the impact of the PCA layer in feature optimization, we first removed this layer from the model, naming this approach -PCA. Similarly, to evaluate the effect of the concat layer, we excluded the concatenation layer in the forward propagation, naming this approach -concat. The model with the dropout layer removed is referred to as -dropout.

All three methods are used in the DTI prediction task to compare the performance and the comparison results are shown in Fig. 8 . The results show that the DTI-MHAPR framework can simultaneously obtain higher AUC, AUPR, F1-score, and ACC scores compared to the other three methods on both datasets, and the standard deviation of our model is very small with good generalisation ability, which indicates that the three modules of our model are well-designed.


#### Fig. 8.


> **Figure/Table Caption:** Ablation experiment results on different network architectures. Mean represents the average, STD represents the standard deviation, and the vertical axis represents the evaluation indicators corresponding to each variant


### Case study

We extracted the known DTIs from the DrugBank database and similarly selected the three drugs with high number of interactions among the known DTIs, which are Olanzapine, Quetiapine and Cabergoline.Then we found out the prediction results of the three drugs and obtained the target proteins with the score ranked in the top 20 for validation, and it was found that the The vast majority of DTIs were validated by the DrugBank database, as shown in Tables 10 , 11 ,and 12 below, which shows the three drugs corresponding to the target proteins with the top 20 scores. In addition, in Fig. 9 ,we selected ten DTIs to be visualised using the knowledge graph, and the weights between the edges are the predicted scores for the extent to which the target is associated with the drug. These results indicate that the DTI-MHAPR method has good performance in drug-target interaction prediction.


#### Table 10.

The top 20 targets associated with the drug Olanzapine



| Ranking | Target | Evidence | Ranking | Target | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | P21728 | DrugBank | 11 | P28335 | DrugBank |
| 2 | P20309 | DrugBank | 12 | P34969 | None |
| 3 | P21918 | DrugBank | 13 | P28221 | DrugBank |
| 4 | P08912 | None | 14 | P28222 | DrugBank |
| 5 | P08908 | DrugBank | 15 | P08913 | None |
| 6 | P18825 | None | 16 | P08172 | DrugBank |
| 7 | P21917 | DrugBank | 17 | P18089 | None |
| 8 | P08173 | DrugBank | 18 | P35368 | DrugBank |
| 9 | P28223 | DrugBank | 19 | P35462 | DrugBank |
| 10 | P35348 | DrugBank | 20 | P14416 | DrugBank |



#### Table 11.

The top 20 targets associated with the drug Quetiapine



| Ranking | Target | Evidence | Ranking | Target | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | P28223 | DrugBank | 11 | P08173 | DrugBank |
| 2 | P08913 | DrugBank | 12 | P21728 | DrugBank |
| 3 | P08172 | DrugBank | 13 | P20309 | DrugBank |
| 4 | P14416 | DrugBank | 14 | P35462 | DrugBank |
| 5 | P35368 | DrugBank | 15 | P30536 | None |
| 6 | P08908 | DrugBank | 16 | P18825 | DrugBank |
| 7 | P35348 | DrugBank | 17 | P08912 | DrugBank |
| 8 | P18089 | DrugBank | 18 | P34969 | DrugBank |
| 9 | P28222 | DrugBank | 19 | P21918 | DrugBank |
| 10 | P28221 | DrugBank | 20 | P41595 | None |



#### Table 12.

The top 20 targets associated with the drug Cabergoline



| Ranking | Target | Evidence | Ranking | Target | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | P28223 | DrugBank | 11 | P08173 | DrugBank |
| 2 | P08913 | DrugBank | 12 | P21728 | DrugBank |
| 3 | P08172 | None | 13 | P20309 | None |
| 4 | P14416 | DrugBank | 14 | P35462 | DrugBank |
| 5 | P35368 | DrugBank | 15 | P18825 | DrugBank |
| 6 | P08908 | DrugBank | 16 | P08912 | None |
| 7 | P35348 | DrugBank | 17 | P34969 | DrugBank |
| 8 | P18089 | DrugBank | 18 | P21918 | DrugBank |
| 9 | P28222 | DrugBank | 19 | P41595 | DrugBank |
| 10 | P28221 | DrugBank | 20 | P28335 | DrugBank |



#### Fig. 9.


> **Figure/Table Caption:** Drug-target association subnetwork. The pink nodes represent the three drugs and the light blue nodes represent the top10 targets associated with the drugs


## Discussion

Motivated by the potential to harness the rich information encoded in the topological structure, our study introduces the DTI-MHAPR framework, which efficiently prioritizes and encodes the most salient features during the encoding-decoding process, thereby significantly enhancing the prediction of drug-target interactions.MHAPR integrates diverse biological information of drugs and targets, providing the model with a rich biological information base. Additionally, by employing a hierarchical structure of multi-layer HAN, the framework effectively achieves deep representation extraction and fusion of multi-layer heterogeneous nodes. Furthermore, prior to feature decoding, MHAPR utilizes the PCA algorithm for feature optimization and employs the random forest algorithm as the classifier, enhancing the model’s tolerance to data noise and improving overall robustness. Experimental results indicate that DTI-MHAPR outperforms existing methods in key evaluation metrics such as AUC, AUPR, and F1-Score.

However, despite the excellent performance of DTI-MHAPR, the framework still faces certain challenges and limitations. Specifically, in the application of the PCA algorithm, the computational complexity of eigenvalue decomposition for high-dimensional data is relatively high, sometimes necessitating the use of approximate computation methods, which increases computational complexity.

To reduce the computational cost and complexity of the proposed method, we will implement model compression techniques in the future, utilizing pruning and quantization strategies to decrease the model’s storage and computational demands. Additionally, we will optimize the data preprocessing pipeline by employing streaming processing techniques to filter and standardize data in real time, thereby enhancing the efficiency of subsequent training and prediction. Through these specific measures, we aim to improve the model’s operability and efficiency, alleviating the high computational complexity associated with the eigenvalue decomposition of high-dimensional data from PCA, ensuring that it maintains good performance in larger-scale applications.

Moreover, the potential extensibility of the DTI-MHAPR framework opens new directions for future research. We plan to apply this framework to predict other types of interactions, such as drug-drug, drug-disease, and protein-disease interactions, to verify its applicability and extend its application scope.


## Conclusion

In this study, we propose a novel computational method, DTI-MHAPR, designed to predict potential interactions between drugs and targets. Compared to existing models, DTI-MHAPR not only integrates sequence and Gaussian similarity information of drugs and targets but also constructs a multi-layer heterogeneous graph attention network (HAN) that effectively encodes and extracts representation vectors of drugs and targets. This approach can deeply explore the complex and subtle relationships between drugs and targets, enhancing the representation capability between nodes. To optimize model features, this study also investigates four different feature selection methods and ultimately adopts the PCA algorithm to improve the quality of feature representation and enhance the model’s discriminative power. Extensive experimental results demonstrate that DTI-MHAPR provides an efficient new method for drug-target identification, contributing to the advancement of precision medicine and personalized treatment strategies.

In future research, we will focus on addressing the computational challenges of the PCA algorithm in handling high-dimensional data from the perspective of feature optimization. We plan to adopt advanced approximate eigenvalue decomposition methods, such as the Lanczos or Arnoldi algorithms, which can significantly reduce computational complexity, accelerate feature extraction speed, and enhance the model’s responsiveness. Additionally, we will explore the introduction of ensemble learning methods to combine multiple feature selection algorithms, automatically identifying the features that contribute most to model performance, thereby reducing computational load while retaining important information.


## Acknowledgements

We express our gratitude to the School of Information and Artificial Intelligence, Anhui Agricultural University, for providing the computational resources.


## Abbreviations

Drug-target interactions

Principal component analysis

Locally linear embedding

T-distributed stochastic neighbor embedding

Fast independent component analysis algorithms

Heterogeneous graph attention network

Random forest algorithm

Support vector machine

EXtreme gradient boosting



G.Y. was responsible for the main manuscript writing, conducting the experiments, and drawing the flowcharts. Y.B.L. was in charge of code modification and improvement. S.J.W. was responsible for the creation of Tables 1–4, W.X.C. for the creation of Tables 5–8, and X.L.Z. for the creation of Tables 9–11. Y.M.W. was responsible for revising the details of the manuscript.


## Funding

This study was supported by the National Key Research and Development Program of China (Grant No. 2023YFC3205701) and also by the Anhui Beidou Precision Agriculture Information Engineering Research Center (Grant Nos. BDSY2023002 and 2022AH040122).


## Availability of data and materials

The datasets and source code utilized in this study are publicly accessible via the following GitHub repository: [GITHUB_REPO_REDACTED] .


## Declarations


### Ethics approval and consent to participate


### Consent for publication


### Competing interests

The authors declare no competing interests.


## Footnotes

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Data Availability Statement

The datasets and source code utilized in this study are publicly accessible via the following GitHub repository: [GITHUB_REPO_REDACTED] .
