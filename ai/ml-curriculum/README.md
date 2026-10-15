# Machine Learning Notes

A comprehensive collection of machine learning concepts, algorithms, and techniques organized for easy learning and reference.

## Table of Contents

### [01 - Fundamentals](./01-fundamentals/)
Essential concepts and mathematical foundations for understanding machine learning.

- **[Core Concepts](./01-fundamentals/core-concepts.md)** - Fundamental ML concepts, models, optimization, and performance metrics
- **[Mathematics & Statistics](./01-fundamentals/math-and-statistics.md)** - Mathematical foundations required for ML
- **[Terminology](./01-fundamentals/terminology.md)** - Comprehensive glossary of ML terms and definitions

### [02 - Learning Types](./02-learning-types/)
Different approaches to machine learning based on the type of data and feedback available.

- **[Supervised Learning](./02-learning-types/supervised-learning.md)** - Learning from labeled data
- **[Unsupervised Learning](./02-learning-types/unsupervised-learning.md)** - Finding patterns in unlabeled data
- **[Reinforcement Learning](./02-learning-types/reinforcement-learning.md)** - Learning through interaction and feedback

### [03 - Models & Algorithms](./03-models-and-algorithms/)
Detailed coverage of machine learning models and algorithms.

- **[Neural Networks](./03-models-and-algorithms/neural-networks.md)** - Deep learning models and architectures
- **[Ensemble Methods](./03-models-and-algorithms/ensemble-methods.md)** - Combining multiple models for better performance
- **[Traditional Algorithms](./03-models-and-algorithms/traditional-algorithms.md)** - Classic ML algorithms and when to use them

### [04 - Advanced Topics](./04-advanced-topics/)
Cutting-edge techniques and specialized applications.

- **[RAG Systems](./04-advanced-topics/rag-systems.md)** - Retrieval-Augmented Generation
- **[Multi-Agent Systems](./04-advanced-topics/multi-agent-systems.md)** - Distributed AI systems
- **[RLHF](./04-advanced-topics/rlhf.md)** - Reinforcement Learning from Human Feedback

### [05 - Deployment](./05-deployment/)
Bringing machine learning models to production.

- **[MLOps](./05-deployment/mlops.md)** - Machine Learning Operations and best practices

### [06 - AI Types](./06-ai-types/)
Understanding different classifications of artificial intelligence.

- **[AI Classifications](./06-ai-types/ai-classifications.md)** - Types of AI based on capabilities and functionality

## Getting Started

If you're new to machine learning, we recommend following this learning path:

1. **Start with Fundamentals** - Read through the core concepts, terminology, and mathematical foundations
2. **Explore Learning Types** - Understand supervised, unsupervised, and reinforcement learning
3. **Dive into Algorithms** - Study traditional algorithms first, then explore neural networks and ensemble methods
4. **Advanced Topics** - Once comfortable with basics, explore specialized topics like RAG and multi-agent systems
5. **Deployment** - Learn about MLOps and bringing models to production

## How to Use This Repository

- Each section builds upon previous knowledge
- Use the terminology guide as a reference while reading other sections
- Examples and applications are provided throughout
- Cross-references link related concepts across sections

## Key Concepts Summary

**Machine Learning** is the process of training algorithms to make predictions or decisions based on data. The fundamental equation is:

**Model = Training (Algorithm + Data)**

The main types of learning are:
- **Supervised**: Learning from labeled examples
- **Unsupervised**: Finding patterns in unlabeled data  
- **Reinforcement**: Learning through trial and error with rewards

Common challenges include overfitting, underfitting, and the bias-variance tradeoff. Success depends on choosing the right algorithm, quality data, and proper evaluation methods.

## Quick Reference

### Algorithm Selection Guide
- **Small dataset**: Naive Bayes, KNN, Simple linear models
- **Large dataset**: Deep learning, ensemble methods
- **Interpretability needed**: Decision trees, linear regression
- **High accuracy required**: Ensemble methods, neural networks
- **Real-time predictions**: Linear models, simple tree models

### Performance Metrics
- **Classification**: Accuracy, Precision, Recall, F1-score
- **Regression**: MSE, RMSE, MAE, R²
- **Clustering**: Silhouette score, Davies-Bouldin index

---

*Last updated: July 2025*
- Stochastic Gradient Descent (SGD): SGD is a widely used optimization algorithm that updates the model's parameters in the direction of the steepest gradient. It performs parameter updates based on a small batch of randomly selected training examples at each iteration.
- Adam: Adam (Adaptive Moment Estimation) is an adaptive learning rate optimization algorithm that combines ideas from both momentum and RMSProp. It adapts the learning rate for each parameter based on the first and second moments of the gradients.
- RMSProp: RMSProp (Root Mean Square Propagation) is an optimization algorithm that adapts the learning rate based on the average of the squared gradients. It helps to mitigate the vanishing or exploding gradient problem.
- Adagrad: Adagrad (Adaptive Gradient) is an optimization algorithm that adapts the learning rate based on the sum of the historical squared gradients. It gives more weight to less frequently occurring features by decreasing the learning rate for frequently occurring features.
- AdamW: AdamW is an extension of Adam that incorporates weight decay regularization, which helps prevent overfitting by penalizing large parameter values.
  
These optimizers, and many others, provide different strategies for updating the model's parameters and adjusting the learning rate during the training process. The choice of optimizer depends on the specific problem, the characteristics of the data, and the model architecture. Experimenting with different optimizers can help improve the model's convergence and overall performance.
