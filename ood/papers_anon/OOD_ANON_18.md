# De-Identified Manuscript `OOD_ANON_18`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Drug-target interaction (DTI) prediction is a critical task in computational drug discovery, enabling drug repurposing, precise medicine, and large-scale virtual screening. Traditional in-silico methods, such as molecular docking, classical machine learning, and deep learning, have made significant progress in addressing this issue. However, existing approaches are hindered by computational inefficiencies, reliance on manual feature engineering, and struggles to generalize across diverse molecular structures, limiting their molecular capabilities. Recent advancements in Quantum Machine Learning (QML) are paving the way for its practical applications, unlocking unprecedented capabilities in predictive accuracy, scalability, and efficiency by leveraging the unique powers of quantum computing, namely superposition and entanglement. This study proposes QKDTI - Quantum Kernel Drug-Target Interaction, a novel quantum-enhanced framework for DTI prediction. It used Quantum Support Vector Regression (QSVR) with quantum feature mapping that takes into account a quantum feature space for molecular descriptors and allows encoding molecular and protein features, improved predictions of binding affinities. To enhance the model to be more computationally feasible, integration of the Nystrom approximation into the model allows providing an efficient kernel approximation while reducing overhead expenses. QKDTI was evaluated on benchmark datasets - Davis and KIBA, and validated independently on BindingDB. This model achieves 94.21% accuracy on DAVIS, 99.99% on KIBA, and 89.26% on BindingDB, significantly outperforming classical and other quantum models. Further, the statistical tests have been conducted on the compared models to provide the reliability of the results. This indicates that introducing quantum computing into DTI pipeline can revolutionize computational drug discovery by improving predictive accuracy and providing a better generalization over multiple datasets.

Keywords: Drug–Target interaction, Quantum kernel, Computational drug discovery, Quantum mapping, Quantum machine learning

Subject terms: Computational biology and bioinformatics, Health care


## Introduction

DTI prediction is a fundamental aspect of computational drug discovery, identifying how small molecules interact with biological macromolecule targets like proteins, enzymes, receptors, etc 1 . Understanding these drug interactions is crucial for pharmacology to identify therapeutic effects, unwanted side effects, and toxic potencies of drug compounds. High-throughput screening has been widely used to examine binding interactions. However, these methods are time-consuming and expensive, particularly when dealing with the vast number of potential combinations. The exploration of modern techniques can speed up drug candidate testing before clinical trials 2 .

Traditional In-silico methods for DTI prediction include molecular docking, machine learning (ML), and deep learning models (DL). While these methodologies have shown potential results, they come with inherent challenges. Molecular docking simulations are computationally expensive and frequently fail to scale across diverse chemical structures. Classical models rely on feature engineering and require huge knowledge to extract accurate representations of molecules and proteins 3 . DL has improved automatic feature extraction but requires large labeled datasets, which are often scarce in drug discovery. Moreover, these models struggle with high-dimensional molecular data and the complexity of biochemical interactions, which limits their ability to generalize across different drug classes and target proteins 4 .

Recent evolutions in quantum computing have introduced new possibilities in computational drug discovery, particularly in quantum machine learning (QML). Quantum computing (QC) has the potential to process high-dimensional data more effectively by leveraging quantum superposition and entanglement, allowing faster and more complex calculations that classical computers would struggle to handle 5 . Unlike classical models that rely on predefined feature spaces, quantum models can encode molecular and protein features into quantum states, capturing better structural and interaction information. This capability alleviates predictive performance, better generalization, and improved efficiency in DTI tasks 6 . This study is motivated by the growing demand for contemporary computational approaches that can tackle the limitations of existing DTI prediction models. While DL has endorsed a significant rise over traditional ML models, it has some challenges related to scalability, interpretability, and data efficiency. QML and hybrid models provide an alternative by combining quantum feature embedding and quantum kernels, possibly giving better drug target affinity prediction.


### Research questions

RQ1 - Can quantum computing improve the performance of drug-target interaction predictions?

RQ2 - How does quantum computing’s performance compare to classical approaches in terms of efficiency?

RQ3 - How does quantum computing handle complex biochemical data compared to classical methods?

By delving into these questions, this study explores the following research objectives.


### Objectives of the study

This study intended to develop and evaluate a quantum-enhanced machine learning framework for DTI prediction, focusing on its practical feasibility in drug discovery. The specific objectives are:

To develop a quantum-enhanced framework for predicting drug-target interactions by integrating quantum computing principles with classical ML techniques.

To compare the performance of quantum machine learning models and classical machine learning models in terms of accuracy, efficiency, and predictive reliability.

To analyze the ability of quantum computing to handle high dimensional data, mainly in representing molecular structures and protein-ligand interactions.

By addressing these objectives, this study contributes to the evolving field of quantum drug discovery, providing visions of how quantum computing can transform the landscape of computational pharmaceutical research.

This study provides a novel quantum kernel-based regression framework (QKDTI) that integrates a quantum support vector regression model with the computed Nystrom approximation kernels, which is not been explored previously for the datasets KIBA, DAVIS, and Binding DB. The proposed model transforms the classical biochemical features into the quantum Hilbert spaces using parameterized RY and RZ-based quantum circuits, capturing non-linear biochemical interactions through quantum entanglement and inference where whereas the classical machine learning on shallow kernels and deep learning models rely on neural networks. Technically, this model overcomes scalability limitations by using a batched and parallel quantum kernel computation pipeline, enabling efficient processing of molecular samples. This architecture allows a quantum kernels integrated into a classical pipeline, combining quantum-enhanced features with robustness and interpretability of classical algorithms. This provides a computationally efficient, generalizable model that maintains high performance across all the real-world datasets. This framework provides a draught for future quantum-classical hybrid models in drug discovery, which bridges theoretical advancements in QML with practical biomedical applications. The findings could improve precision medicine, drug repurposing, and large-scale drug screening, making it a valued step towards incorporating quantum computing into biomedical applications.


## Literature review

Over the years, computational methods have played an important role in the drug discovery process. One crucial task in this process is predicting DTI. Methods like classical ML and DL have been used for this purpose.

Molecular docking is one of the earliest computational processes developed to predict binding interactions between drug molecules and proteins. It is performed by simulating the physical and chemical interactions between molecules, directing to quote the binding affinity of a drug to its target. Although docking gave impressive results, it struggles with flexible molecular structures, which may lead to inaccurate predictions and the process is computationally expensive. To cover these issues, ML and DL models are introduced to improve DTI predictions 7 .


### Machine learning models

Classical ML models like support vector machines (SVM), random forest (RF), and K-nearest neighbors have been used in the DTI prediction. These models performed well on structured datasets, and their dependence on feature engineering made them less adaptable to complex and high-dimensional biochemical data.

SVMs are supervised learning models that classify data by finding the optimal hyperplane separating different classes. In DTI prediction, SVM has been utilized to distinguish between interacting and non-interacting drug–target pairs by mapping input features into high-dimensional spaces. However, their performance heavily depends on the quality of feature engineering and the selection of appropriate kernels, which can be challenging when dealing with complex biochemical data 8 . RFs are ensemble learning methods that construct multiple decision trees during training and output the mode of the classes for classification tasks 9 . They have been employed in DTI prediction to handle large datasets and model nonlinear relationships. Despite their robustness, RFs require extensive feature engineering to effectively capture the intricacies of molecular interactions, limiting their adaptability to high-dimensional data 10 . The k-NN algorithm classifies data points based on the majority class among their k-nearest neighbors in the feature space. In the context of DTI prediction, k-NN has been applied to predict interactions by assessing the similarity between drug and target features. However, k-NN’s reliance on distance metrics makes it sensitive to the curse of dimensionality, posing challenges when dealing with complex molecular descriptors. While these traditional ML models have achieved success with structured datasets, their dependence on manual feature extraction limits their scalability and effectiveness in capturing the multifaceted nature of drug–target interactions. This limitation has led to the exploration of DL approaches, which can automatically learn feature representations from raw data, thereby enhancing the prediction accuracy of DTI.


### Deep learning models

DL is another impressive method used for DTI prediction that addresses the limitations caused by classical machine learning models, like automating feature extraction and learning large molecular patterns. DL uses techniques like representation learning, which allows for extracting suitable, meaningful features directly from the raw input data. Some of the DL approaches like convolutional neural network 11 , long short-term memory 12 , and graph convolutional network 13 has been applied to the DTI tasks, which improved the performance. Methods such as Deep DTI 14 introduced an unsupervised refined molecular representation before classification, outperforming traditional ML models. PADME (Protein And Drug Molecule interaction prEdiction) 15 used deep neural networks combined with molecular graph convolutions to address complex problems where novel drug-target pairs had no subsequent interaction data, thus improving generalization. DL models require vast datasets to attain optimal performance, and their black-box nature raises challenges in interpretability, limiting their direct adoption in clinical applications 16 , 17 . One of the studies 18 introduced a deep ensemble model that integrates diverse neural networks across multiple datasets, achieving robust performance. Similarly 19 , proposed global local hybrid approach that used contextual embedding to combine protein sequence with substructure molecular features. Another advanced study 20 represents a molecule representation block using multi-head attention and skip connections, capturing local and long-range dependencies. As DL pushes the boundaries of DTI prediction, researchers are exploring quantum computing as a novel approach to overcome the challenges posed by classical machine learning and DL methods.


### Quantum models

Quantum computing is powerful due to features like superposition and entanglement, which allow it to process complex and high-dimensional interactions more effectively. These features can encode the molecular and protein features into quantum states, allowing better representation of interactions. Recent studies introduced quantum machine learning techniques, such as quantum kernels, variational quantum circuits (VQC), and hybrid quantum models, to enhance DTI prediction 21 . Quantum feature mapping enhances molecular interaction calculations, improving affinity predictions compared to classical kernel methods. One of the earliest applications of quantum computing in DTI involved VQC, which demonstrated competitive performance in classifying drug-protein interactions. In one study, a quantum-enhanced classification model achieved a concordance index of 0.802, surpassing traditional linear regression methods and DL models. The ability of quantum models to optimize hyperparameters like qubit count and circuit depth further enhances their adaptability to complex biochemical data. Beyond classification, quantum computing has been integrated into binding affinity prediction, focusing on challenges like convergence stability and accuracy. A hybrid quantum-classical framework featuring 3D and spatial graph convolutional neural networks was proposed to improve affinity prediction, yielding a 6% increase in all the metrics (R 2 , MAE, Pearson, Spearman, RMSE) over classical models. To ensure scalability on current NISQ devices, quantum error mitigation techniques have been introduced to effectively reduce errors without computational overhead 22 .

Table 1 provides a summary of the DTI prediction and bioinformatics modeling incorporating three computing paradigms: classical machine learning, deep learning, and quantum computing. Existing models exhibit limitations, which include dependency on feature engineering, limited generalizability issues under high-dimensional settings. DL models are more powerful than ML, which suffer from interpretability challenges, while quantum models remain constrained by hardware capabilities and are typically restricted to small molecules. The binary classification approaches fail to capture the continuous nature of binding affinities. The proposed model addresses these challenges through a hybrid model that uses quantum-enhanced feature representation by integrating both sequence and structural modalities with quantum kernels. This model enhances predictive accuracy and generalizability that enabling regression-based affinity estimation and improved interpretability. This positions our approach as a robust and scalable solution in the evolving landscape of quantum-assisted drug discovery. Upcoming research is expected to improve quantum feature encoding, optimize hybrid models, and address hardware limitations, paving the way for quantum-enhanced precision medicine.


#### Table 1.

Summary of previous studies.



| Year | Ref. | Model | Dataset(s) | Performance Metrics | Key Findings | Limitations |
| --- | --- | --- | --- | --- | --- | --- |
| 2020 | 23 | IDTI-ESBoost | Gold Standard, DrugBank | Accuracy: 0.87, AUC: 0.92 | Combined stacking and boosting with evolutionary features; outperformed baseline ML methods | Complex feature engineering; requires 3D structures |
| 2021 | 24 | TTModel | KEGG, DrugBank | AU-PR: ~1 | Graph-based model improved prediction for sparse interaction networks | Lacks deeper hierarchical data |
| 2022 | 25 | MFCDA | DrugBank, SIDER | AUPR: 0.86, AUC: 0.93 | Multi-view matrix factorization with side effect integration; 8–12% accuracy improvement | Depends on comprehensive side-effect data |
| 2022 | 26 | DTiPred | DrugBank, BindingDB, E. coli | F1: 0.94, AUC: 0.96 | SVM with ensemble feature selection reduced dimensionality while maintaining performance | Binary classification limits affinity prediction |
| 2023 | 27 | RFC-DTI | BindingDB, DrugBank | Accuracy: 0.93, AUC: 0.88 | Multiple logistic regression with pharmacological features; highly interpretable model | Performance gap compared to DL |
| 2021 | 28 | GraphDTA | DAVIS, KIBA | MSE: 0.261, CI: 0.878 | Graph neural networks captured complex molecular structures; improved binding affinity prediction | Computationally expensive; requires structural data |
| 2020 | 29 | MolTrans | Uniprot, CHEMBL | CI: 0.89, RMSE: 0.42 | Molecular transformer with interaction fingerprints; captured substructure interactions | Limited to small/medium proteins; data imbalance sensitivity |
| 2022 | 30 | DESERT | PDBbind | RMSD < 2Å: 38% | Equivariant diffusion model for binding pose prediction; state-of-the-art docking accuracy | High computational requirements; complex implementation |
| 2024 | 31 | DRAGON Multi-Modal | BindingDB, PDBbind, DUD-E | AUROC: 0.98, EF1%: 56.7 | Integrated 3D structure with sequence data; achieved top performance on multiple benchmarks | Requires comprehensive structural data; complex preprocessing |
| 2022 | 32 | QMugs | CHEMBL | Chemical validity: 92% | Quantum mechanical properties of drug-like molecules | Current hardware limitations; small molecule scope |
| 2021 | 33 | DVAE-RBM | ChEMBL | Tanimoto similarity precision: +12% | Quantum generated 2331 novel chemical structures with medicinal chemistry | Limited to quantum simulators; scalability issues |
| 2025 | 34 | MolFP | MF | AUROC: 0.89, MCC: 0.76 | Quantum circuit for molecular fingerprinting; demonstrated advantage for specific molecules | Hardware limitations; difficult implementation |
| 2024 | 35 | SSCRBM | 37 circRNA–RBP interaction datasets | Average AUC: 97.66% | Lightweight model integrating sequence and structural features using multi-scale attention mechanism | Limited to circRNA–RBP prediction; generalizability concerns |
| 2025 | 36 | ATFPGT-multi | Aquatic toxicity datasets (BS, RT, FHM, SHM) | AUCs, ACCs, PREs, REs for each species | Multi-task learning model integrating multiple molecular fingerprint representations and graph transformer networks | Sample imbalance across species; high computational demand |
| 2024 | 37 | SNMGCDA | circRNA–drug similarity datasets | AUC, AUPR, Accuracy, F1-score, Precision, Recall, Specificity | Integrates sparse autoencoders, NMF, and multi-head GAT to fuse similarity-based circRNA and drug features | High performance dependent on data availability and quality |
| 2024 | 38 | DMFPGA | DILI-labeled compound dataset | AUC: 0.935, Accuracy: 0.934 (5-fold CV) | Multi-head graph attention for node-level features and multiple molecular fingerprints for compound-level feature fusion | Dataset size and composition not clearly stated; validation needed |
| 2023 | 39 | DCAMCP | Carcinogenicity prediction dataset | Various metrics | Capsule networks with attention mechanisms to predict carcinogenicity; outperforms previous models | Moderate accuracy; generalizability to novel compounds unclear |
| 2022 | 40 | GCNCRF | LncRNASNP2 | AUROC: 0.947 (5-fold CV) | GCN and CRF with attention for predicting human lncRNA–miRNA interactions; better than existing methods | Relies on pre-existing similarity networks and feature matrices |
| 2024 | 41 | VQC-DTI | KIBA | Accuracy: 0.85, F1: 0.83 | Variational quantum circuits for molecule encoding; demonstrated on NISQ hardware | Limited to small molecules; quantum noise sensitivity |
| 2023 | 42 | QC-DTI | PDBbind | Accuracy: 0.80, AUROC: 0.91 | Quantum computing classifier for protein-ligand interactions using tensor networks | Requires hybrid quantum-classical resources; limited dataset size |



## Methodology

This study proposed QKDTI - Quantum Kernel Drug-Target Interaction, a novel quantum-enhanced regression framework for DTI prediction that enhance the accuracy and efficiency of Drug-Target Interaction prediction. By leveraging quantum kernels, QKDTI captures complex molecular interactions more effectively than classical machine-learning approaches.

Traditional methods, such as classical ML and DL approaches, struggle with high-dimensional feature spaces, computational inefficiencies, and nonlinear interactions between molecular structures. SVR is a widely used machine learning technique for predicting continuous values, particularly in scenarios where the relationship between input features and output is complex and nonlinear. Traditional SVR relies on kernel functions such as linear, polynomial, and radial basis function kernels to project data into a higher-dimensional space where a linear regression model can be fit.

QKDTI provides an alternative approach by utilizing quantum kernels to map complex molecular interactions into higher-dimensional Hilbert spaces 43 , capturing non-linearity more effectively than classical models. Unlike classical kernels, quantum kernels utilize quantum superposition and entanglement to capture intricate molecular structures and protein-ligand interactions more efficiently. This allows QKDTI to handle non-linearity in drug-target binding affinity predictions with improved precision. This study investigates the capability of quantum kernel learning for predicting binding affinity values in drug discovery applications. The methodology incorporates quantum-enhanced feature transformations with quantum machine learning techniques to optimize performance. The proposed framework consists of the following steps as shown in Fig. 1 .


### Fig. 1.


> **Figure/Table Caption:** Proposed QKDTI model.


### Dataset description

This study is based on datasets from the Therapeutics Data Commons: a widely used source of curated datasets for drug discovery 34 . Among its extensive collection, three widely used datasets DAVIS, KIBA, and BindingDB were selected for training, testing, and validation of the proposed model. These datasets were retrieved using the TDC Python library interface, specifically from the multi-prediction DTI task module. Each dataset includes drug-target pairs along with their measured binding affinities, reported using experimental metrics such as Kd, IC50, Ki or integrated scores like the KIBA score.

Molecular Representations.

Drugs - Small Molecules: Represented using SMILES - Simplified Molecular Input Line Entry System strings, a text-based encoding of molecular structure.

Targets - Proteins: Represented using FASTA sequences, encoding the amino acid sequence of each protein target.

To prepare the raw molecular and protein data for machine learning models:

Molecular fingerprints 44 , 45 or learned embeddings are derived from SMILES using RDKit cheminformatics tools.

Protein features are extracted via pre-trained models or sequence-based descriptors like ProtBERT or physicochemical proper encodings.

Each dataset includes experimentally determined binding affinity values:

DAVIS: Reports binding affinities in Kd (nM), specifically for kinase inhibitors.

KIBA: Provides KIBA Scores, which are normalized affinity scores integrating multiple biochemical measurements.

BindingDB: Includes a wide range of binding values reported as Kd, IC50, or Ki in nM, µM, or mM units.

The Binding affinity measurements and units are observed in Table 2 .


#### Table 2.

Binding affinity measurement and Units.



| Score | Dataset(s) | Meaning | Units |
| --- | --- | --- | --- |
| Kd | DAVIS, BindingDB | Dissociation constant which measures binding strength. | nM, µM, mM |
| IC50 | BindingDB | The concentration needed to inhibit 50% of the target activity. | nM, µM, mM |
| Ki | BindingDB | The inhibition constant represents enzyme inhibitor binding strength. | nM, µM, mM |
| KIBA Score | KIBA | Composite bioactivity score integrated from Kd, IC50, Ki, etc. | Arbitrary unit |


Due to this wide scale in binding affinities from picomolar (pM) to millimolar (mM) raw values exhibit significant variance that could affect training stability.


#### Dataset composition

The chosen datasets vary in size, drug target pairs, and binding metrics, ensuring that the study covers a broad spectrum of drug-target binding prediction. The dataset characteristics are presented in Table 3 .

Characteristics of datasets.



|  | Dataset | Drugs | Targets | Interactions | Train | Test | Interaction Type | Binding Metric |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Training & Testing | DAVIS | 68 | 442 | 30,056 | 24,044 | 6012 | Kinase-Protein | Kd |
| KIBA | 2,111 | 229 | 118,254 | 94,603 | 23,651 | Kinase-Protein | KIBA Score |
| Validation | BindingDB | ~ 8,000 | ~ 1,500 | ~ 1,000,000 | - | - | Small Molecule-Protein | Kd, IC50, Ki |


The DAVIS and KIBA datasets were used for training and testing in an 80:20 split, while the BindingDB dataset was employed exclusively for independent validation to assess the model’s ability to generalize to novel drug-target pairs can be observed in Fig. 2 . To mitigate overfitting and ensure a clear evaluation of the model’s generalization capability, we deliberately limited the training and test datasets to subset samples. This controlled setting enables us to assess how well the model performs on unseen data. Datasets were selected because of their diversity, reliability, and relevance in drug discovery applications. These datasets are well-suited and standard for high-precision affinity models for DTI prediction. Exploratory data analysis has been done to reveal more molecular characterizations of the datasets.


> **Figure/Table Caption:** Training, testing, and validation split up.


#### Exploratory data analysis (EDA)

Exploratory Data Analysis (EDA) was conducted to understand the distribution and relationships among molecular descriptors, including molecular weight, lipophilicity (logP), hydrogen bond donors, and hydrogen bond acceptors, concerning binding affinity values.

Figures 3 and 4 , and 5 show the scatterplots of these descriptors across the DAVIS, KIBA, and BindingDB datasets, showing their distributions and pairwise correlations with binding affinity. These visualizations focus on how physicochemical properties influence interaction strength across different datasets. The observed variability in binding affinity, spanning from nanomolar (nM) to millimolar (mM) concentrations, necessitated logarithmic transformation to normalize the values and reduce variance during model training. This transformation enhances numerical stability and facilitates regression modeling.


> **Figure/Table Caption:** Davis Dataset.


> **Figure/Table Caption:** KIBA Dataset.


> **Figure/Table Caption:** Binding_DB Dataset.


#### Statistical analysis of datasets

To further understand the dataset properties, the log-transformed binding affinity values were subjected to statistical analysis. Table 4 presents the mean, standard deviation, and skewness for every dataset. Observably, the KIBA dataset shows the smallest variance (σ = 0.031) and maximum skewness and has a more uniform and right-tailed affinity score distribution, which are reasons for its higher model stability and performance. Conversely, BindingDB has the largest variance (σ = 1.372), implying a broader range of molecular interactions and higher complexity. The DAVIS dataset, while smaller, exhibits moderate variability and positive skewness, reflecting a prevalence of strong interactions with occasional weak binders.

Statistical analysis of binding affinities across Datasets.



| Dataset | Mean (log) | Standard Deviation (σ) | Skewness |
| --- | --- | --- | --- |
| DAVIS | 5.407 | 0.826 | 2.336 |
| KIBA | 7.928 | 0.031 | 3.233 |
| BindingDB | 5.881 | 1.372 | 0.855 |


These results demonstrate the non-linear, complicated nature of molecular descriptors vs. binding affinity, lending validity to the implementation of quantum-improved kernel learning within the QKDTI approach. The mapping of molecular attributes to a Hilbert space within quantum can enhance the ability of the model to capture the complexities of such relationships, allowing for better generalization and prediction performance.


### Data preprocessing

The preprocessing phase is the critical step in developing a model. In this phase, it guarantees that the training and testing of the proposed model can be performed efficiently.

This process involves several operations shown in Fig. 6 applied to the DAVIS, KIBA, and BindingDB datasets, which serve as validation sets and contain diverse DTI pairs with varying binding affinity measurements. Due to the imbalance and heterogeneity of these datasets, feature transformation and standardization techniques were employed to maintain consistency across inputs and optimize model performance. At the outset, each of these datasets got its respective binding values from all data retrieved with ranges from nanomolar (nM) to millimolar (mM) concentrations. To normalize a vast extent of range, majorly fluctuating binding values were logarithmically transformed as:



|  | 1 |
| --- | --- |



#### Fig. 6.


> **Figure/Table Caption:** QKDTI Preprocessing Steps.

Where Y represented the original binding affinity value, and Y log described the transformed value of Y. This transformed log ensures that extremely large values would not dictate the learning trend while also providing variance stabilization for their multipurpose conformity towards regression models. Subsequently, to the transformation, standardization of features was performed using Z-score normalization, which scales each feature by subtracting the mean and dividing by the standard deviation as derived from the following:



|  | 2 |
| --- | --- |


Where X is the original value of the feature, µ is the mean across all instances for that feature while, σ is the standard deviation. This step was crucial in ensuring that no single feature disproportionately influenced the model, particularly when integrating quantum feature mapping techniques. To address missing values, a dataset-specific approach was taken. If any binding affinity values were missing, the corresponding data entries were removed. For missing molecular descriptors, the mean of the respective feature was used for imputation. Additionally, protein sequence embeddings were recomputed where necessary, ensuring a complete dataset for training.

Given the high-dimensional nature of drug and protein representations, principal component analysis was applied to reduce dimensionality while preserving 95% of the variance, making subsequent quantum computations more efficient. Finally, preprocessed datasets were then converted into a precomputed kernel format, enabling efficient training of the QKDTI model. These preprocessing steps ensured that the DAVIS, KIBA, and BindingDB datasets were well-structured and computationally optimized, allowing for seamless integration into the hybrid quantum-classical learning pipeline. This preprocessing framework improves numerical stability and facilitates effective comparisons between quantum kernel learning and classical techniques in DTI prediction.


### Model development

In the previous section, the preprocessing pipeline was described to convert unstructured drug-target data to be built into a feature space suitable for machine learning models. Techniques including log transformation, standardization, quantum feature mapping, nyström kernel approximation, and feature fusion were applied to optimize learning conditions and enhance the model. Following data preprocessing, model training is performed. This section focuses on training strategies, optimization, and evaluation of QSVR meant for predicting drug-target binding affinities. The next steps should include an evaluation and training phase for several methods. This work aims to determine if the quantum-enhanced model provides explicit benefits in terms of accuracy, generalization, and computational efficiency. Already having outlined the details of the process including training with the QKDTI model, there are differences in contrast to classical models which do not rely on any manually developed kernels-either linear, polynomial, or RBF. Rather, QKDTI uses quantum feature mapping to produce kernels that exploit quantum entanglement and superposition to allow for a richer representation of data.


#### Quantum feature mapping

Once preprocessing was complete, the data was organized for quantum feature mapping, where molecular features were encoded into a quantum Hilbert space via parameterized quantum circuits (PQC) 34 can be observed in Fig. 7 .


> **Figure/Table Caption:** Feature Mapping.

The quantum circuit used for QKDTI visualized in Fig. 8 , consists of 𝑛 qubits corresponding to the molecular descriptor, which allows the embedding of high-dimensional molecular features into the quantum system. Each qubit is initialized in the standard basis state ∣0⟩. A Hadamard (𝐻) gate is applied on each of the qubits to attain the even distribution state, which allows for quantum parallelism:



|  | 3 |
| --- | --- |



> **Figure/Table Caption:** QKDTI Quantum Circuit.

This superposition allows the system to access multiple states of molecular features at once, boosting the model’s generalization capacity over different chemical structures. Once the Hadamard operation is performed, encoding of features is done using successive and parameterized rotation gates, namely the 𝑅𝑌 and 𝑅𝑍, which variably influence the qubit state from the descriptor value input given by the molecule. The transformation applied to each qubit is given by:



|  | 4 |
| --- | --- |




|  | 5 |
| --- | --- |


Here, denotes the 𝑖th feature for the input molecular vector. These gates guarantee that the quantum amplitudes represent the molecular descriptors in a high-dimensional feature space. Controlled-Z (𝐶𝑍) gates couple adjacent qubits to introduce a dependence and correlation of features. The 𝐶𝑍 gate is defined as:



|  | 6 |
| --- | --- |


Here, it introduces correlations among phases across neighboring qubits, with a corresponding interaction angle that incorporates molecular interactions, which cannot be done by classical feature representations. The entanglement thus created ensures the quantum feature encoding captures complicated relations among molecular descriptors, finally enhancing the expressiveness of the quantum feature map.

Once the quantum feature encoding is complete, the expectation values of the quantum states are measured to compute the quantum kernel, which serves as the core of the QSVR model. The quantum kernel function was then computed using:



|  | 7 |
| --- | --- |


Here, 𝜙( ) represents a quantum-encoded transformation of the input features. Due to the exponentially rising computation complexity of the quantum kernel matrix for large datasets, a batch-wise computation strategy was adopted, splitting pairs into batches of 50 samples to ensure training efficiency. Besides, nyström approximation was additionally used to better improve computation efficiency and scalability to approximate the quantum kernel matrix.

As shown in Fig. 9 , the Nyström method permits approximation of large kernel matrices using a small set of landmark points, defined as follows:



|  | 8 |
| --- | --- |



> **Figure/Table Caption:** Nystrom Approximation.

Where , which contains a subset of the full kernel matrix computed using a limited number of samples, and which gives the projection of the full dataset on these selected samples. By this approximation, the computational complexity is tremendously reduced, and at the same time, high accuracy concerning the actual kernel is retained.


#### Quantum optimization

Once the quantum kernel is calculated, it is used as an input to the QKDTI model and follows a standard epsilon-SVR optimization framework. The SVR objective function minimizes the following loss function.



|  | 9 |
| --- | --- |


Subject to the constraints.



|  | 10 |
| --- | --- |




|  | 11 |
| --- | --- |


w is the weight vector that the model learns. 𝜉𝑖 and 𝜉𝑖∗ allow small errors in predictions. 𝐶 controls the trade-off between accuracy and model complexity. 𝜖 sets the margin within which predictions are considered acceptable. This function helps QSVR find a balance between accuracy and generalization, preventing overfitting.

To train the QKDTI model effectively, we optimize various hyperparameters to achieve the best possible performance. The training process involves fine-tuning parameters that control the model’s complexity, computational efficiency, and generalization ability.


### Hyperparameters

To optimize the performance of the QKDTI model, hyperparameters were carefully selected and tuned to ensure effective prediction.


#### Quantum circuit parameters

The quantum feature mapping in QKDTI utilizes eight qubits, each one representing a molecular descriptor. The qubits are put in a superposition state with Hadamard (𝐻) gates, then followed by parameterized rotation gates 𝑅𝑌(𝑥) and 𝑅𝑍(𝑥), which encode classical molecular feature values into quantum states. To introduce quantum entanglement and increase the correlation of the features, Controlled-Z (𝐶𝑍) gates were applied on pairs of adjacent qubits to exploit the complex interdependencies that can exist among molecular descriptors. The quantum circuit hyperparameters used in this study are represented in Table 5 .

Quantum circuit Hyperparameters.



| Hyperparameter | Description | Selected Value |
| --- | --- | --- |
| Number of Qubits | Each qubit represents a molecular descriptor. | 8 |
| Hadamard (H) Gates | Induces superposition across molecular features. | Applied to all qubits |
| Rotation Gates 𝑅𝑌(𝑥), 𝑅𝑍(𝑥) | Encode feature values into quantum states. | Parameterized |
| Controlled-Z (CZ) Gates | Introduces entanglement between adjacent qubits. | Applied to neighboring pairs |



#### Quantum kernel approximation

To avoid kernel evaluations that would normally be found overpowering, the nyström approximation was adopted. This was achieved by picking out a batch of 50 to approximate the full kernel matrix, which would save on enormous costs while not significantly troubling the accuracy of the kernel. Furthermore, the double-batch computation considers 50 samples to be the batch during processing when ensuring extensive-scale kernel evaluation. The quantum kernels were fed to the SVR model when fitting it. SVR hyperparameters were thus jointly chosen for an optimal trade-off between model complexity and prediction accuracy. The hyperparameters related to the quantum kernel are outlined in Table 6 .

Quantum kernel Hyperparameters.



| Hyperparameter | Description | Selected Value |
| --- | --- | --- |
| Batch Size for kernel computation | Reduces computational load for large datasets | 50 samples per batch |
| Nyström approximation - landmark points | Approximates the full kernel matrix | 50 reference points |
| Kernel matrix storage | Precomputed kernel matrix for efficient access | Optimized storage format |



#### Support vector regression (SVR) parameters

The regularization parameter (𝐶) was assigned a value of 1.0 to control the trade-off between efforts to minimize training error and maximize margin generalization. The epsilon (𝜖) parameter was set to 0.1, defining a tolerance range, with predictions inside that range being accepted as valid. The SVR model was fit using the Sequential Minimal Optimization (SMO) solver, which optimally solves the regression function. In the early stages of the modeling process, feature preprocessing is crucial to prepare input data for quantum embedding. In this study, PCA is used to reduce the dimensions of the features retained, accounting for 95% of the variance, so that only the most pertinent information is kept. In addition, Z-score normalization ensured that the molecular descriptors had a zero mean and unit variance before encoding them into quantum states. The SVR hyperparameters are provided in Table 7 .



| Hyperparameter | Description | Selected Value |
| --- | --- | --- |
| C | Controls the trade-off between model complexity and error tolerance | 1.0 |
| ϵ | Defines tolerance within which predictions are accepted | 0.1 |
| Solver | The algorithm used for SVR optimization | SMO |


Optimal hyperparameter selection was essential for high predictive performance and low error rates. The Nyström approximation provided computational effectiveness without compromising the expressiveness of kernels. PCA-driven dimensionality reduction also enhanced generalization by reducing redundant molecular descriptors. Through the use of these optimizations, QKDTI showed substantial superiority over traditional models in binding affinity prediction on the DAVIS, KIBA, and BindingDB datasets.


### Computational environment

The QKDTI model was implemented and tested using the following quantum-classical hybrid environment to ensure computational feasibility and performance evaluation.

Quantum Machine Learning: PennyLane.

Quantum Backend: Qiskit for quantum kernel evaluations.

Classical ML Libraries: Scikit-learn, PyTorch, TensorFlow.

Hardware & Execution Environment:

Quantum Simulations: Conducted using PennyLane simulator.

GPU Acceleration: NVIDIA T4 GPU on Kaggle (cloud-based execution).


## Experimental results and discussion

The experimental evaluation of the QKDTI model was conducted on three benchmark datasets: DAVIS, KIBA, and BindingDB, assessing its performance in predicting drug-target interaction binding affinity. The experiments aimed to compare the effectiveness of QKDTI against classical machine learning models, particularly standard SVR, in terms of prediction accuracy, generalization ability, and computational efficiency.


### Performance metrics


#### Mean squared error

Mean Squared Error (MSE) is one of the most commonly used metrics for regression tasks. It quantifies the average squared difference between the actual binding affinity values and the model’s predictions:



|  | 12 |
| --- | --- |


represents the actual drug-target binding affinity.

is the predicted binding affinity from the QSVR model.

N is the total number of drug-target pairs. A lower MSE value indicates that the model’s predictions are closer to the actual binding affinity values, meaning better accuracy.


#### Root mean squared error (RMSE)

The Root Mean Squared Error (RMSE) is another regression metric provides a more interpretable measure of prediction error by maintaining the same unit as target variable



|  | 13 |
| --- | --- |


A lower RMSE indicates that, smaller deviation to the actual values.


#### Prediction accuracy

While regression models do not have a traditional “accuracy” metric like classification models 40 , we define a prediction accuracy measure to assess how close the predicted values are to the actual values:



|  | 14 |
| --- | --- |


A higher accuracy percentage means that the model’s predictions closely match the real binding affinities.


#### R 2 score

R² Score identifies the amount of dependent variable variation that independent variables can predict:



|  | 15 |
| --- | --- |


Where is the mean of actual values. The model’s fit strength increases when the value of R 2 approaches 1, but decreases when it becomes negative.


#### Pearson correlation coefficient(r)

The actual and predicted value relationship gets measured through Pearson’s r. It is computed as:



|  | 16 |
| --- | --- |


The value scale extends from − 1 to 1 with 1 representing a perfect positive linear association between variables. Better predictive correlation exists when values rise.


#### Area under ROC curve

The AUC-ROC serves as a typical classification metric but for DTI regression by applying thresholding to affinity scores to determine model discrimination between strong and weak binders. The performance of a classification system becomes more accurate as the AUC value approaches 1 even when using threshold-based approximations.


### Results and discussion

The experimental results demonstrate the effectiveness of the QKDTI prediction across three benchmark datasets: DAVIS, KIBA, and BindingDB can be observed in Table 8 . To determine the efficacy of prediction, QKDTI was trained on the datasets, ensuring computational feasibility.


#### Table 8.

Performance of propose model across three datasets.



| Dataset | Model | MSE | RMSE | Accuracy | R ² Score | Pearson r | AUC-ROC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DAVIS | QKDTI | 0.255 | 0.5212 | 94.21 | 0.8531 | 0.924 | 0.9543 |
| KIBA | QKDTI | 0.0003 | 0.0173 | 99.99 | 0.6415 | 0.7924 | 0.8125 |
| BindingDB | QKDTI | 0.4592 | 0.534 | 89.26 | 0.5928 | 0.7642 | 0.9168 |


To evaluate the performance, the proposed method is compared with multiple classical and quantum models. The efficacy of QKDTI was evaluated using performance metrics predicting the binding affinity. This comparison includes three quantum models for evaluation: Quantum Neural Networks (QNN), Variational quantum circuit (VQC), Quantum Feature Fusion Regression (QFFR), and Quantum Transformers. The QNN model used quantum rotation encoding through RY and RZ gates along with Pauli-Z measurements to build its basic variational quantum circuit design. Strongly Entangling Layers added to the QFFR model allowed it to create complex quantum feature interactions, which captured molecular relationships at higher dimensions. Quantum Transformer utilized a multi-head attention mechanism and feed-forward networks to serve as the quantum model for the molecular descriptor relationship.


### Comparative analysis

The performance of various classical and quantum machine learning models was evaluated across the three datasets. The results are summarized in the following figures, tables, and discussions.

Across all the datasets and models, QKDTI consistently outperformed classical and quantum models.

To evaluate the performance of QKDTI, we compared it against a curated set of classical and quantum models across the benchmark datasets: DAVIS, KIBA, and BindingDB. These models were selected based on the following rationale:

Models like SVR, Ridge Regression, and Random Forest are standard baselines in DTI tasks and have shown strong performance across multiple benchmark studies 20 , 23 , 29 .

Included a broad spectrum of model typeslinear, nonlinear, ensemble, and deep learning, as well as quantum models—to ensure comprehensive evaluation.

Quantum Neural Networks (QNN), Quantum Feature Fusion Regression (QFFR), Variational Quantum Circuits (VQC), and Quantum Transformers represent cutting-edge developments in quantum machine learning for molecular modeling and DTI prediction.

Performance evaluation was based on multiple metrics, including MSE, RMSE, R², AUC-ROC, Pearson correlation, and prediction accuracy to assess regression performance across classical and quantum paradigms. These models were used extensively to perform regression tasks in computational drug discovery because of their validation with benchmark DTI datasets. Performance comparison can occur among linear, non-linear, and ensemble-based machine learning paradigms, with a focus on MSE, RMSE, R 2 , AUC-ROC, Pearson and Accuracy.

The results from Figs. 10 , 11 and 12 visualization analysis correlate with the interesting trend: Among classical machine-based learning models and quantum-enhanced models, notably QKDTI, work closer to physically realistic representations of molecular interactions, hence providing better binding affinity predictions. On the KIBA dataset, QKDTI achieved low MSE of 0.0003 and R 2 of 0.6415 indicating strong prediction. QKDTI performed well with the DAVIS dataset also with the MSE of 0.25 and a pearson correlation of 0.921, confirming its generalizability. In the case of BindingDB, which is a raw dataset proposed model provided a lower RMSE of 0.9722 and a reasonable R 2 0.521. Among the three databases considered in this work, KIBA yields the highest accuracies across all models, with QKDTI achieving as high as 99.99% in comparison to performances over DAVIS. This result has been achieved mainly due to the well-structured and canonical scoring system in KIBA, which assimilates several bioactivity estimations like Ki, Kd, IC50, and EC50 into a single KIBA score, all of which lower noise and variation for a more uniform and predictable dataset for machine learning algorithms. KIBA mainly consists of kinase inhibitors, a drug category with highly correlated molecular structures and interaction patterns, allowing the models to extract significantly more meaningful features. The higher signal-to-noise ratio and better feature consistency further enable quantum-enhanced models like QKDTI to achieve superior predictive accuracy by effectively mapping molecular interactions into quantum states. Moreover, KIBA ensures better generalization, unlike DAVIS and BindingDB, which contains higher variability in binding affinity scores. The consistency in prediction performance across the DAVIS, KIBA, and BindingDB datasets also shows the great potential of quantum-enhanced regression technologies to revolutionize computational drug discovery, opening a door to more accurate and scalable predictive modeling.


#### Fig. 10.


> **Figure/Table Caption:** Performance of QKDTI – KIBA dataset.


#### Fig. 11.


> **Figure/Table Caption:** Performance of QKDTI – DAVIS dataset.


#### Fig. 12.


> **Figure/Table Caption:** Performance of QKDTI – BindingDB dataset.

To assess the significance of the performance between different models the statistical analysis is performed. This study conducted paired t-tests and Wilcoxon signed-rank tests on the prediction outputs of all the datasets. The analysis can be observed in the Table 9 .


#### Table 9.

Statistical analysis of classical and quantum models.



| Dataset | KIBA |  | DAVIS |  | Binding DB |  |
| --- | --- | --- | --- | --- | --- | --- |
| Metrics | Paired t-test (t-stat, p-value) | Wilcoxon Test (statistic, p-value) | Paired t-test (t-stat, p-value) | Wilcoxon Test (statistic, p-value) | Paired t-test (t-stat, p-value) | Wilcoxon Test (statistic, p-value) |
| Classical Models |
| Linear Regression | (−2.315, 0.045) | (3.0, 0.078) | −2.4538, 0.0331 | 2.0000, 0.0451 | (−4.7687, 0.0006) | (0.0, 0.0010) |
| Support Vector Regressor (SVR) | (−3.025, 0.015) | (1.0, 0.031) | −3.1085, 0.0082 | 3.0000, 0.0105 | (−3.0388, 0.0113) | (4.0, 0.0068) |
| Ridge Regression | (−2.850, 0.022) | (2.0, 0.045) | 1.4216, 0.1648 | 6.0000, 0.2451 | (0.2441, 0.8117) | (27.0, 0.6191) |
| Random Forest | (2.950, 0.018) | (5.0, 0.063) | 1.8724, 0.0625 | 5.0000, 0.1583 | (2.2689, 0.0444) | (13.0, 0.0801) |
| Gradient Boosting | (3.100, 0.014) | (3.0, 0.039) | 3.1476, 0.0033 | 4.0000, 0.0267 | (6.2202, 0.0001) | (0.0, 0.0020) |
| XGBoost | (3.520, 0.008) | (1.0, 0.016) | −0.8699, 0.3991 | 7.0000, 0.1123 | (−0.6209, 0.5473) | (29.0, 0.7441) |
| LightGBM | (3.450, 0.009) | (1.0, 0.016) | 2.8014, 0.0079 | 3.0000, 0.0312 | (6.2202, 0.0001) | (0.0, 0.0020) |
| MLP | (−0.600, 0.560) | (6.0, 0.219) | −1.2592, 0.2102 | 5.0000, 0.0551 | (−3.4320, 0.0056) | (2.0, 0.0029) |
| QKDTI (Proposed) | (4.200, 0.003) | (0.0, 0.008) | 2.5214, 0.0182 | 0.0000, 0.1250 | 3.5123, 0.0045 | 0.0, 0.0020 |
| Quantum Models |
| QKDTI (Proposed) | (3.050, 0.014) | (2.0, 0.031) | 2.5214, 0.0182 | 0.0000, 0.1250 | (3.5123, 0.0045) | (0.0, 0.0020) |
| QFFR | (2.900, 0.018) | (3.0, 0.039) | −0.4725, 0.6377 | 4.0000, 0.2500 | (−0.8794, 0.4212) | (4.0, 0.6250) |
| QNN | (2.850, 0.021) | (3.0, 0.045) | 1.4324, 0.1638 | 3.0000, 0.1995 | (1.9655, 0.0931) | (2.0, 0.2500) |
| VQC | (2.200, 0.056) | (4.0, 0.078) | 2.8114, 0.0452 | 0.0000, 0.0625 | (2.8114, 0.0482) | (0.0, 0.1250) |
| Quantum Transformer | (4.050, 0.004) | (0.0, 0.008) | −1.0563, 0.2926 | 2.0000, 0.3750 | (−2.9210, 0.0432) | (0.0, 0.1250) |


To validate the performance gains of quantum models over classical approaches, statistical tests were conducted across the KIBA, DAVIS, and BindingDB datasets. The proposed QKDTI model consistently yielded statistically significant improvements, with p-values below 0.05 in both paired t-tests and Wilcoxon signed-rank tests. Notably, on the KIBA dataset, QKDTI achieved a t-statistic of 3.05 ( p = 0.014) for MSE and 2.0 ( p = 0.031) in the Wilcoxon test, while Quantum Transformer exhibited a strong correlation performance with a t-statistic of 4.05 ( p = 0.004). Similar trends were observed on DAVIS and BindingDB, confirming that quantum models not only reduced prediction errors but also better captured drug-target interaction patterns. These statistically significant results underscore the robustness and reliability of quantum-enhanced models in DTI prediction tasks.


### Discussion

This study introduces QKDTI, a novel framework, confirming its ability to enhance DTI prediction through quantum-enhanced learning techniques. The research objectives were systematically addressed:

QKDTI is a quantum-enhanced framework that integrates QSVR and quantum feature mapping to optimize molecular interaction predictions.

Performance comparisons demonstrated QKDTI’s superiority over classical ML models, showing higher accuracy and statistical significance was done using the paired t–tests and Wilcoxon confirming that the improvement was reasonable not by chance.

Quantum computing enabled QKDTI to handle biochemical data more effectively, improving binding affinity predictions and generalization across datasets.

While most of the studies in DTI used the classification techniques leading imbalance class distribution, this work used a continuous distribution by applying a log transformation to binding affinity scores, which minimizes the skewness. This helps to handle class imbalance and provides and good binding strength.

The findings provide strong evidence that quantum-enhanced models like QKDTI can revolutionize computational drug discovery, offering higher predictive reliability, computational efficiency, and improved scalability for high-throughput screening applications. This work relies on quantum simulation which is restricted by the number of qubits, short coherence time due to the deployment of real-time quantum devices. Quantum models possess complex structures that make it difficult to obtain easily interpretable biological information from their learned representations. The quantum models on working on experimental validation can be successful to drug discovery when performed on quantum hardware.


## Conclusion and future work

This study proposed QKDTI - Quantum Kernel Drug-Target Interaction, a novel quantum-enhanced framework for drug-target interaction prediction. By combining quantum feature mapping with QSVR through the QKDTI model predict binding affinity more accurately and efficiently. The encoding process becomes easier through QKDTI because quantum kernel learning in the framework enables better model generalization across different datasets. The nyström approximation functions as a computational optimization tool by ensuring scalability and using fewer resources in comparison to traditional methods. QKDTI trains on DAVIS and KIBA datasets and then evaluates its predictions on the independent BindingDB, where the proposed model provides superior result compared to traditional machine learning models and other quantum regression models. The implemented results resulted in substantial progress through reduced errors together with higher predicted binding affinities. Data imbalance challenge was addressed by the model through log transformation and other strategies that enhanced its generalization and robustness performance. As part of the system integration with quantum computing principles, the developers created an advanced molecular interaction model that maintained accuracy levels with subset data.

In addition to its predictive advantages, QKDTI meets sustainability goals by integrating a lower computational burden into classical drug discovery. While classical in-silico approaches typically require high-computing platforms, which contribute to energy consumption and subsequently increase carbon footprints, the principles of quantum computing incorporated into QKDTI offer a green alternative that supports sustainability in pharmaceutical sciences. The model’s optimized computational framework solves the redundancy problem, making it a viable, sustainable option for large-scale biomedical applications that promote responsible and resource-efficient AI in drug discovery.

The future work shall additionally bear witness to widening the scope of biochemical datasets considered by QKDTI, further refinement of the hybrid quantum-classical architectures deployed, and achieving better interpretability of outputs to make them useful in clinical decision-making. QKDTI can be extended beyond protein target predictive capabilities to non-coding RNAs (ncRNAs), including microRNAs, since these regulatory elements play an important role in disease progression 39 , 41 , 44 . The prediction of microRNA–small molecule interactions through QKDTI adaptation offers exciting research potential because recent investigations show RNA-targeted interactions have therapeutic value. The proposed model can be used for RNA sequence embeddings and structural descriptions because its quantum kernel framework works with different input modalities, making it suitable for tasks requiring minimal experimental data. Another scope includes refining the hybrid quantum-classical model to improve stability and convergence, especially as current quantum backends are constrained by limited qubit counts, noise, and decoherence that restrict model complexity and scalability. By propounding a scalable and sustainable quantum-driven approach, this research also paves the way for the next generation of computational drug discovery by providing a green path toward energy-efficient and high-accuracy molecular interaction predictions that support global health objectives through its contribution to United Nations Sustainable Development Goal 3: Good Health and Well-Being.



A.A. conceptualized the study and designed the methodology. G.P. implemented the Quantum Kernel Drug-Target Interaction (QKDTI) framework and performed the experiments. R.P.K. supervised the research and provided critical revisions. G.P. and A.A. wrote the main manuscript text. R.P.K. reviewed and edited the manuscript. All authors reviewed and approved the final manuscript.


## Data availability

The dataset used in this proposed research is available in open access. The codes for implementation and numerical analysis used in this work will be made available online in GitHub resources for the research community to explore based on the request to the corresponding author.


## Declarations


### Competing interests

The authors declare no competing interests.


## Footnotes

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Data Availability Statement

The dataset used in this proposed research is available in open access. The codes for implementation and numerical analysis used in this work will be made available online in GitHub resources for the research community to explore based on the request to the corresponding author.
