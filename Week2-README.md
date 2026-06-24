# Week 2 Notes - Machine Learning Basics

## What is Machine Learning?

Machine Learning is a subset of Artificial Intelligence that enables computers to learn from data and improve performance without explicit programming.

---

## Types of Machine Learning

### 1. Supervised Learning

Uses labelled data.

Examples:

- Classification
- Regression

Industrial Example:

Predict whether a product passes inspection.

---

### 2. Unsupervised Learning

Uses unlabelled data.

Examples:

- Clustering
- Association

Industrial Example:

Grouping products with similar defect patterns.

---

### 3. Reinforcement Learning

An agent learns through rewards and penalties.

---

## Overfitting

Occurs when a model memorizes training data and performs poorly on unseen data.

---

## Underfitting

Occurs when a model fails to learn enough patterns from the data.

---

## Bagging

Bagging stands for Bootstrap Aggregating.

Multiple models are trained on different samples of data and their predictions are combined.

Benefits:

- Reduced variance
- Better generalization
- Improved stability

---

# Pandas

Pandas is a Python library used for data manipulation and analysis.

Common Operations:

- Reading data
- Filtering data
- Aggregation
- Statistics
- Data cleaning

Example:

```python
import pandas as pd

df = pd.DataFrame(data)
```
