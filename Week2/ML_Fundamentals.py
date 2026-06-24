Cell 1
# Week 2 - Machine Learning Basics

In this notebook, I explore fundamental Machine Learning concepts learned during Week 2 of the Summer of Code project.

----------------------------------------
Cell 2 
## What is Machine Learning?

Machine Learning is a branch of Artificial Intelligence that enables systems to learn patterns from data and make predictions without being explicitly programmed.

----------------------------------------
Cell 3
print("Machine Learning allows computers to learn from data.")

----------------------------------------
Cell 4
## Types of Machine Learning

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

----------------------------------------
Cell 5
learning_types = [
    "Supervised Learning",
    "Unsupervised Learning",
    "Reinforcement Learning"
]

for item in learning_types:
    print(item)

----------------------------------------
Cell 6
## Supervised Learning

In supervised learning, the model learns using labelled data.

Example:
Defect Images → Defect Category

----------------------------------------
Cell 7
products = ["Product A", "Product B", "Product C"]
labels = ["Pass", "Fail", "Pass"]

for product, label in zip(products, labels):
    print(product, ":", label)

----------------------------------------
Cell 8
## Unsupervised Learning

In unsupervised learning, data is not labelled.

The goal is to identify hidden patterns or groups.

----------------------------------------
Cell 9
inspection_scores = [92, 91, 95, 45, 48, 50]

print("Inspection Scores:")
print(inspection_scores)

----------------------------------------
Cell 10
## Overfitting vs Underfitting

Overfitting:
Model memorizes training data.

Underfitting:
Model fails to learn important patterns.

----------------------------------------
Cell 11
print("Overfitting -> High training accuracy, poor testing accuracy")
print("Underfitting -> Poor training accuracy and testing accuracy")

----------------------------------------
Cell 12
## Bagging

Bagging (Bootstrap Aggregating) combines predictions from multiple models to improve performance and reduce variance.

----------------------------------------
Cell 13
model_predictions = [1, 1, 0]

final_prediction = max(
    set(model_predictions),
    key=model_predictions.count
)

print("Final Prediction:", final_prediction)
