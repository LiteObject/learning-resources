# Core Machine Learning Concepts

## Machine Learning Model
**Model = Training (Algorithm + Data)**

A machine learning model is a mathematical representation or algorithm that learns patterns and relationships from data to make predictions or take decisions without being explicitly programmed. It is the result of training a machine learning algorithm on a dataset to capture patterns, extract insights, and generalize to new, unseen data.

In essence, a machine learning model is a mapping from input data to output predictions or decisions. It takes input features or variables (also known as independent variables) and produces output predictions or labels (also known as dependent variables) based on the learned patterns from the training data.

## Common Types of Machine Learning Models

### Regression Models
- **Linear Regression**: Models the relationship between independent variables and a continuous dependent variable using a linear equation.

### Classification Models
- **Logistic Regression**: Models the probability of a binary outcome or class membership based on independent variables using a logistic function.
- **Naive Bayes**: A probabilistic model based on Bayes' theorem that predicts the probability of different outcomes based on independent features.

### Both Classification & Regression
- **Decision Trees**: Models decisions or classifications by splitting the data based on a series of hierarchical rules or conditions.
- **Random Forest**: An ensemble model that combines multiple decision trees to make predictions by averaging or voting.
- **Support Vector Machines (SVM)**: Models data by finding a hyperplane that best separates different classes or groups. Can be extended to regression (SVR).
- **Neural Networks**: Deep learning models composed of interconnected layers of artificial neurons that can learn complex patterns and relationships.

## Ordinary Least Squares (OLS)
It is a method used in statistics and econometrics to estimate the parameters of a linear regression model.

In the context of linear regression, the OLS model aims to find the best-fitting line that minimizes the sum of the squared differences between the observed dependent variable values and the predicted values based on the independent variables.

The "ordinary" in Ordinary Least Squares refers to the fact that the method assumes that the errors or residuals of the model are normally distributed and have constant variance (known as homoscedasticity). The "least squares" part of the name refers to the minimization of the sum of the squared errors.

## Objective Functions
An objective function, also known as a cost function, loss function, or optimization function, is a mathematical function that defines the goal or objective of an optimization problem. In optimization, the objective function quantifies the performance or quality of a solution or a set of parameters.

The objective function is typically designed to be minimized or maximized based on the problem's requirements. For example, in a minimization problem, the objective function should be minimized, while in a maximization problem, the objective function should be maximized.

## Optimizers
In the context of machine learning, an optimizer is an algorithm or method used to adjust the parameters of a model in order to minimize the error or loss function during the training process. The optimizer plays a crucial role in the training phase of machine learning models, as it determines how the model's parameters are updated in response to the training data.

During the training phase, the model iteratively makes predictions on the training data and calculates the associated error or loss. The optimizer then adjusts the model's parameters based on the error, aiming to minimize the loss function and improve the model's performance.

## Key Performance Concepts

### Overfitting
When a model performs well on training data but fails to generalize to new, unseen data due to excessive complexity.

### Underfitting
When a model is too simple to capture the underlying patterns in the data, resulting in poor performance.

### Bias-Variance Tradeoff
The balance between a model's ability to fit the training data (low bias) and its ability to generalize to new data (low variance). Finding the right balance is crucial to avoid underfitting or overfitting.

### Regularization
Techniques used to prevent overfitting by adding additional constraints or penalties to the model during training.

## Training Process Concepts

### Loss Function
A measure of how well a model's predictions align with the actual values, used to optimize the model during training.

### Gradient Descent
An optimization algorithm that adjusts the model's parameters iteratively to minimize the loss function.

### Backpropagation
An algorithm used to compute the gradients of the loss function with respect to the parameters of a neural network, enabling efficient parameter updates during training.

Video Explanation: [Backpropagation](https://www.youtube.com/watch?v=S5AGN9XfPK4)

### Hyperparameters
Parameters set before training that influence the model's learning process, such as learning rate or number of layers.

### Cross-Validation
A technique to assess model performance by splitting data into multiple subsets for training and evaluation.

## Data Processing Concepts

### Feature Extraction
The process of selecting or transforming relevant features from raw data to improve model performance.

### Inference
Inference refers to the process of using a trained model to make predictions or draw conclusions based on new, unseen data. It involves applying the learned knowledge from the model to make decisions or generate outputs.

### Quantization
Quantization refers to the process of reducing the precision or number of bits used to represent numerical values. It involves converting continuous values into a discrete set of values. Quantization is often used to compress models or reduce memory usage, making them more efficient for deployment on resource-constrained devices.

## Technical Terminology

### Slug
A slug typically refers to a short, human-readable text string that is used to identify a specific resource, such as a dataset, model, or project. It is often used in URLs or file names to provide a concise and descriptive identifier.

### Token
A token refers to a unit of text that is treated as a single entity. It can be a word, a character, or even a subword, depending on how the text is processed. Tokenization helps in organizing and analyzing text data in a structured manner.

### Chain-of-thought
It refers to the sequential flow of reasoning or decision-making processes within a model. It represents how information is processed and transformed as it moves through different layers or components of the model.

### Activation Function
A mathematical function applied to the output of a neuron in a neural network, introducing non-linearity and enabling complex mappings between inputs and outputs.

### Batch Size
The number of training examples used in each iteration of the training process. Larger batch sizes can lead to faster training, but may require more memory.

### Learning Rate
A hyperparameter that determines the step size at which the model's parameters are updated during training. It influences the speed and stability of the learning process.

### Dropout
A regularization technique used during training to randomly deactivate a certain percentage of neurons in a neural network, reducing overfitting and improving generalization.

### Bias
An additional parameter in a machine learning model that allows for shifting the output in a non-linear manner, providing flexibility and improving model performance.
