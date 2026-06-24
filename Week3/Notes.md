# Week 3 Notes - Deep Learning and CNN

## What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses Artificial Neural Networks with multiple layers to learn patterns from data.

It is particularly effective when working with:

- Images
- Audio
- Text
- Video

---

## Artificial Neural Networks (ANN)

Neural Networks are inspired by the human brain.

Basic structure:

1. Input Layer
2. Hidden Layer(s)
3. Output Layer

Each neuron receives inputs, processes them, and passes information to the next layer.

---

## Activation Functions

Activation functions introduce non-linearity into neural networks.

Common activation functions:

### ReLU

```python
max(0, x)
```

Advantages:

- Fast computation
- Most commonly used

### Sigmoid

```python
1 / (1 + e^-x)
```

Used for binary classification problems.

### Tanh

Produces values between -1 and 1.

---

## Forward Propagation

During forward propagation:

- Input data enters the network.
- Calculations are performed layer by layer.
- Predictions are generated.

---

## Backpropagation

Backpropagation is the process of updating network weights using prediction errors.

Purpose:

- Reduce loss
- Improve model accuracy

---

## Convolutional Neural Networks (CNN)

CNNs are specialized neural networks designed for image processing tasks.

Applications:

- Image Classification
- Object Detection
- Medical Imaging
- Industrial Inspection

---

## Components of CNN

### Convolution Layer

Extracts important features from images.

Examples:

- Edges
- Corners
- Shapes

---

### Pooling Layer

Reduces image dimensions while preserving important features.

Common type:

- Max Pooling

Benefits:

- Faster computation
- Reduced overfitting

---

### Flatten Layer

Converts feature maps into a one-dimensional vector.

---

### Dense Layer

Performs final classification using extracted features.

---

## Industrial Quality Assurance Applications

CNNs can be used for:

- Surface defect detection
- Crack identification
- Product classification
- Automated visual inspection

These applications help reduce manual inspection efforts and improve manufacturing efficiency.

---

## Key Learnings

During Week 3, I learned:

- Fundamentals of Deep Learning
- Neural Network Architecture
- Activation Functions
- Forward and Backpropagation
- CNN Architecture
- Applications of CNNs in image processing
