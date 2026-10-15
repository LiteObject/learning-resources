# Machine Learning Terminology

## Neural Networks
- **Artificial Neural Network**: Deep learning models composed of interconnected layers of artificial neurons
- **Convolutional Neural Network (CNN)**: Neural networks specifically designed for processing grid-like data, such as images or audio, by using convolutional layers to extract relevant features
- **Recurrent Neural Network (RNN)**: Neural networks that can process sequential data by utilizing feedback connections, making them suitable for tasks like natural language processing and speech recognition
- **Long Short-Term Memory (LSTM)**: A type of RNN that can learn long-term dependencies
- **Generative Adversarial Network (GAN)**: A framework where two neural networks compete against each other
- **Transformer**: Architecture using self-attention mechanisms; foundation of modern NLP models like GPT and BERT
- **Attention Mechanism**: Technique allowing models to focus on relevant parts of input data
- **Encoder-Decoder**: Architecture pattern for sequence-to-sequence tasks
- **Autoencoder**: Neural network that learns compressed representations of data
- **Embedding Layer**: Layer that converts discrete inputs to dense vectors

## Learning Approaches
- **Supervised Learning**: A type of ML where the model learns from labeled data to make predictions or classifications
- **Unsupervised Learning**: ML technique where the model learns patterns and structures from unlabeled data without specific guidance
- **Semi-Supervised Learning**: Learning approach that uses both labeled and unlabeled data
- **Reinforcement Learning**: A type of Machine Learning where an agent learns to make decisions by interacting with an environment and receiving feedback in the form of rewards or penalties
- **Transfer Learning**: The practice of leveraging knowledge gained from training one model on a specific task to improve the performance of a different but related task
- **Fine-tuning**: Adapting pre-trained models to specific tasks by continuing training on task-specific data
- **Ensemble Learning**: A technique that combines multiple models, known as an ensemble, to make predictions or classifications. It often leads to improved performance and robustness
- **Meta-learning**: Learning to learn; models that adapt quickly to new tasks
- **Few-shot Learning**: Learning from very few examples
- **Zero-shot Learning**: Making predictions on classes never seen during training
- **Curriculum Learning**: Training strategy that presents examples in meaningful order

## Model Evaluation
- **Overfitting**: When a model performs well on training data but fails to generalize to new, unseen data due to excessive complexity
- **Underfitting**: When a model is too simple to capture the underlying patterns in the data, resulting in poor performance
- **Bias**: An additional parameter in a machine learning model that allows for shifting the output in a non-linear manner, providing flexibility and improving model performance
- **Variance**: The model's sensitivity to fluctuations in the training data
- **Loss Function**: A measure of how well a model's predictions align with the actual values, used to optimize the model during training
- **Regularization**: Techniques used to prevent overfitting by adding additional constraints or penalties to the model during training
- **Accuracy**: Percentage of correct predictions out of total predictions
- **Precision**: Ratio of true positives to predicted positives (TP / (TP + FP))
- **Recall (Sensitivity)**: Ratio of true positives to actual positives (TP / (TP + FN))
- **F1 Score**: Harmonic mean of precision and recall, balancing both metrics
- **Confusion Matrix**: Table showing true positives, true negatives, false positives, and false negatives
- **ROC Curve/AUC**: Receiver Operating Characteristic curve and Area Under Curve; metrics for binary classification performance
- **Mean Squared Error (MSE)**: Common loss function for regression that penalizes larger errors more
- **Mean Absolute Error (MAE)**: Regression metric measuring average absolute difference between predictions and actual values

## Optimization Techniques
- **Gradient Descent**: An optimization algorithm that adjusts the model's parameters iteratively to minimize the loss function
- **Backpropagation**: An algorithm used to compute the gradients of the loss function with respect to the parameters of a neural network, enabling efficient parameter updates during training
- **Dropout**: A regularization technique used during training to randomly deactivate a certain percentage of neurons in a neural network, reducing overfitting and improving generalization
- **Batch Normalization**: A technique to normalize inputs to each layer
- **Learning Rate**: A hyperparameter that determines the step size at which the model's parameters are updated during training. It influences the speed and stability of the learning process
- **Hyperparameter**: Parameters set before training that influence the model's learning process, such as learning rate or number of layers
- **Optimizer Types**: Algorithms for parameter updates including Adam, SGD (Stochastic Gradient Descent), RMSprop, and AdaGrad
- **Momentum**: Technique to accelerate gradient descent by accumulating velocity in consistent directions
- **L1 Regularization (Lasso)**: Adds absolute value of coefficients as penalty term, can lead to sparse models
- **L2 Regularization (Ridge)**: Adds squared magnitude of coefficients as penalty term
- **Weight Decay**: Form of regularization that gradually shrinks weights toward zero
- **Early Stopping**: Stopping training when validation performance stops improving to prevent overfitting

## Data Processing
- **Feature Extraction**: The process of selecting or transforming relevant features from raw data to improve model performance
- **Feature Selection**: The process of selecting the most relevant features for model training
- **Dimensionality Reduction**: Techniques to reduce the number of features while preserving important information
- **Word Embedding**: Dense vector representations of words that capture semantic meaning
- **Data Augmentation**: Techniques to artificially expand training datasets (e.g., rotating images, adding noise)
- **Normalization/Standardization**: Scaling features to similar ranges to improve model convergence
- **One-Hot Encoding**: Converting categorical variables to binary vectors
- **Train-Test Split**: Dividing data into separate sets for training and evaluation
- **Validation Set**: Data used to tune hyperparameters and monitor performance during training
- **Test Set**: Data held out for final model evaluation, never used during training
- **Imbalanced Data**: When classes have significantly different sample sizes
- **Data Leakage**: When training data contains information about test data, leading to overly optimistic results

## Algorithms
- **Linear Regression**: Models the relationship between independent variables and a continuous dependent variable using a linear equation
- **Logistic Regression**: Models the probability of binary outcomes using a logistic function
- **Naive Bayes**: Probabilistic classifier based on Bayes' theorem assuming feature independence
- **Support Vector Machine (SVM)**: Models data by finding a hyperplane that best separates different classes or groups
- **Decision Tree**: Models decisions or classifications by splitting the data based on a series of hierarchical rules or conditions
- **Random Forest**: An ensemble model that combines multiple decision trees to make predictions by averaging or voting
- **XGBoost/Gradient Boosting**: Ensemble method using boosted decision trees, building models sequentially to correct errors
- **K-Nearest Neighbors (KNN)**: A simple algorithm that classifies data points based on the majority class of their k nearest neighbors
- **Clustering**: Unsupervised learning technique that groups similar data points together

## Natural Language Processing (NLP)
- **Natural Language Processing (NLP)**: Field of AI focused on enabling computers to understand, interpret, and generate human language
- **Sentiment Analysis**: The process of determining the emotional tone or opinion expressed in text
- **Token**: A unit of text that is treated as a single entity. It can be a word, a character, or even a subword, depending on how the text is processed
- **Chain-of-thought**: The sequential flow of reasoning or decision-making processes within a model

## General Terms
- **Slug**: A short, human-readable text string that is used to identify a specific resource, such as a dataset, model, or project
- **Inference**: The process of using a trained model to make predictions or draw conclusions based on new, unseen data
- **Quantization**: The process of reducing the precision or number of bits used to represent numerical values
- **Activation Function**: A mathematical function applied to the output of a neuron in a neural network, introducing non-linearity
- **Batch Size**: The number of training examples used in each iteration of the training process
- **Mini-batch**: Subset of training data used in one iteration of training
- **Epoch**: One complete pass through the entire training dataset
- **Cross-Validation**: A technique to assess model performance by splitting data into multiple subsets for training and evaluation
- **Checkpoint**: Saved model state during training, allowing recovery or evaluation at specific points
- **Latent Space**: Hidden representation learned by models, capturing underlying data structure

## Computer Vision
- **Object Detection**: Identifying and locating objects in images with bounding boxes
- **Image Segmentation**: Classifying each pixel in an image into categories
- **Pooling**: Downsampling operation in CNNs to reduce spatial dimensions (Max Pooling, Average Pooling)

## Production & Deployment
- **Model Serving**: Deploying models for production use and handling inference requests
- **Model Drift**: When model performance degrades over time due to changes in data distribution
- **A/B Testing**: Comparing model versions in production to evaluate performance
- **MLOps**: Practices for deploying, monitoring, and maintaining ML systems in production
