
```
Machine Learning Notebook
│
├── 01 Fundamentals
│   ├── Core Concepts
│   │   ├── Model = Training (Algorithm + Data)
│   │   ├── Mapping: Inputs → Outputs (generalization)
│   │   ├── Objective Functions (Loss / Cost)
│   │   ├── Ordinary Least Squares (OLS)
│   │   ├── Optimization: Gradient Descent, Backpropagation, Optimizers
│   │   └── Performance: Overfitting, Underfitting, Bias–Variance, Regularization
│   ├── Math & Statistics
│   │   ├── Linear Algebra (vectors, matrices, dot product)
│   │   ├── Calculus (derivatives, gradients)
│   │   ├── Probability (Bayes, conditional, distributions)
│   │   ├── Statistics (mean, variance, hypothesis testing)
│   │   └── Optimization foundations (convexity, constraints)
│   └── Terminology (grouped)
│       ├── Learning Approaches: Supervised, Unsupervised, Semi, Reinforcement, Transfer, Fine-tuning, Ensemble, Meta, Few-shot, Zero-shot, Curriculum
│       ├── Optimization: Learning Rate, Momentum, L1/L2, Early Stopping, Weight Decay, BatchNorm, Dropout
│       ├── Data: Feature Extraction/Selection, Dimensionality Reduction, Augmentation, Normalization, One-Hot Encoding, Splits
│       ├── Evaluation: Accuracy, Precision, Recall, F1, AUC, MSE, MAE
│       └── General: Inference, Quantization, Token, Slug, Latent Space, Epoch, Mini-batch, Checkpoint
│
├── 02 Learning Types
│   ├── Supervised
│   │   ├── Tasks: Classification, Regression
│   │   └── Algorithms: Linear/Logistic Regression, Trees, SVM, Naive Bayes, Neural Nets
│   ├── Unsupervised
│   │   ├── Clustering: K-Means, Hierarchical, DBSCAN
│   │   ├── Association Rules
│   │   ├── Dimensionality Reduction: PCA, t-SNE, UMAP
│   │   └── Anomaly Detection
│   └── Reinforcement Learning
│       ├── Elements: Agent, Environment, State, Action, Reward, Policy
│       ├── Paradigms: Model-Free vs Model-Based; On-Policy vs Off-Policy
│       ├── Algorithms: Q-Learning, DQN, Policy Gradient, Actor-Critic
│       └── RLHF Overview (Pretrain → Preference Model → RL Fine-tune)
│
├── 03 Models & Algorithms
│   ├── Traditional
│   │   ├── Linear / Logistic Regression
│   │   ├── Decision Tree / Random Forest
│   │   ├── KNN / SVM / Naive Bayes
│   │   └── Clustering (K-Means, Hierarchical)
│   ├── Ensemble Methods
│   │   ├── Bagging (Random Forest)
│   │   ├── Boosting (AdaBoost, Gradient Boosting, XGBoost)
│   │   └── Stacking / Blending
│   └── Neural Networks
│       ├── Components: Layers, Weights, Biases, Activations
│       ├── Architectures: Feedforward, CNN, RNN, LSTM, Transformer, GAN, Autoencoder
│       ├── Mechanisms: Attention, Encoder–Decoder, Embeddings
│       ├── Training: Forward Pass, Backpropagation, Losses (Cross-Entropy, MSE)
│       └── Regularization: Dropout, BatchNorm, L1/L2, Weight Decay
│
├── 04 Advanced Topics
│   ├── RAG Systems (Retrieval-Augmented Generation)
│   │   ├── Retrieval: Query → Embeddings → Vector Store
│   │   ├── Chunking & Indexing
│   │   ├── Context Assembly (Top-k selection)
│   │   └── Prompt Augmentation → LLM Generation
│   ├── Multi-Agent Systems
│   │   ├── Properties: Autonomy, Decentralization, Interdependence
│   │   ├── Coordination & Communication
│   │   ├── Applications: Distributed Optimization, Resource Allocation
│   │   └── Challenges: Trust, Conflict Resolution, Scalability
│   └── RLHF (Reinforcement Learning from Human Feedback)
│       ├── Data: Human Preference Collection
│       ├── Reward Modeling
│       ├── Policy Optimization (PPO / variants)
│       └── Challenges: Alignment, Bias, Robustness
│
├── 05 Deployment (MLOps)
│   ├── Lifecycle: Problem → Data → Train → Evaluate → Deploy → Monitor → Iterate
│   ├── Versioning: Data, Model, Code (Reproducibility)
│   ├── CI/CD for Models (Pipelines)
│   ├── Serving: Batch, Online, Streaming
│   ├── Monitoring: Performance, Drift (Data/Concept), Latency, Errors
│   ├── Governance & Compliance: Audit Trails, Explainability
│   └── Automation: Feature Stores, Model Registry
│
├── 06 AI Types
│   ├── By Capability: Narrow (ANI) → General (AGI) → Superintelligence (ASI)
│   └── Cognitive Progression: Reactive → Limited Memory → (Theory of Mind) → (Self-Aware) *theoretical*
│
├── Cross-Cutting Optimization
│   ├── Objective / Loss Functions
│   ├── Optimizers: SGD, Adam, RMSProp, Adagrad, AdamW
│   ├── Hyperparameters: Learning Rate, Batch Size, Epochs, Regularization Strength
│   └── Tradeoffs: Bias–Variance, Exploration–Exploitation (RL), Accuracy–Latency
│
├── Data & Processing
│   ├── Feature Engineering / Selection
│   ├── Normalization / Standardization / Scaling
│   ├── Augmentation & Synthetic Data
│   ├── Splits: Train / Validation / Test; Cross-Validation (k-fold, stratified)
│   ├── Handling: Missing Values, Imbalance (Resampling, Class Weights)
│   └── Compression: Quantization, Pruning, Distillation
│
└── Evaluation & Monitoring
    ├── Classification: Accuracy, Precision, Recall, F1, AUC, Confusion Matrix
    ├── Regression: MSE, MAE, RMSE, R²
    ├── Clustering: Silhouette, Davies–Bouldin, Inertia
    ├── Ranking / Retrieval: Precision@k, MRR, NDCG
    ├── Drift: Data Drift, Concept Drift
    └── Operational: Latency, Throughput, Error Rate, Resource Cost
```