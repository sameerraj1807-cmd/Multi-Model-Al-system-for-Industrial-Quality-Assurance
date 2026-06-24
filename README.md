# Multi-Modal AI System for Industrial Quality Assurance
### Seasons of Code (SoC) - IIT Bombay | Midterm Progress Report

---

## 👤 About Me

- **Program:** Seasons of Code, IIT Bombay
- **Year:** Fresher (to-be Sophomore)
- **Project Title:** Multi-Modal AI System for Industrial Quality Assurance
- **Report Period:** Week 1 – Week 4 (Midterm)

---

## 🎯 Project Overview

This project aims to build a **Multi-Modal AI system** capable of performing **industrial quality assurance** - detecting defects, anomalies, and quality issues in manufactured products using a combination of **computer vision (CNNs)** and **language models (LLMs)**. The system will take image input (camera feeds from production lines) and textual/structured sensor data, process them through separate modalities, and fuse the outputs to make quality decisions.

The first four weeks are dedicated to building the foundational knowledge required to undertake this project - covering Python, Machine Learning, Deep Learning, CNNs, and Large Language Models.

---

## 📅 Weekly Progress Log

---

### Week 1 - Python Basics 🐍

**Goals Completed:**
- ✅ Set up Python development environment on Google Colab
- ✅ Learned core Python syntax: variables, data types, lists, dictionaries, loops, and functions
- ✅ Ran first Python scripts
- ✅ Covered Machine Learning theory as a primer

**Key Concepts Covered:**
- **Variables & Data Types:** integers, floats, strings, booleans
- **Data Structures:** lists (indexing, slicing, list comprehensions), dictionaries (key-value pairs, nested dicts), tuples, sets
- **Control Flow:** `if/elif/else`, `for` loops, `while` loops, `break/continue`
- **Functions:** defining functions, parameters, return values, default arguments, scope (local vs global)
- **ML Theory Primer:** what is ML, supervised vs unsupervised vs reinforcement learning, the concept of training/testing, overfitting vs underfitting

**Resources Used:**
- CodeWithHarry Python Video Lecture (till Chapter 8 - Functions)
- The Ultimate Python Handbook (PDF)
- futurecoder.io for interactive practice


---

### Week 2 - Machine Learning Basics 🤖

**Goals Completed:**
- ✅ Studied core ML algorithms and concepts up through Bagging (ensemble methods)
- ✅ Learned data manipulation using Pandas
- ✅ Built intuition for how models are trained and evaluated

**Key Concepts Covered:**
- **Supervised Learning Algorithms:** Linear Regression, Logistic Regression, K-Nearest Neighbours, Decision Trees, Support Vector Machines (SVMs)
- **Model Evaluation:** train-test split, cross-validation, accuracy, precision, recall, F1-score, confusion matrix
- **Ensemble Methods:** Bagging (Bootstrap Aggregating), Random Forests — how combining weak learners reduces variance
- **Pandas:** DataFrames, Series, reading CSVs, `.head()`, `.describe()`, `.groupby()`, handling missing values, filtering, sorting, merging datasets
- **Connection to Project:** In industrial QA, structured sensor data (temperature, pressure, vibration) can be fed into classical ML models alongside image data

**Resources Used:**
- CodeWithHarry ML Playlist (till Bagging)
- Pandas tutorial by Krish Naik


---

### Week 3 - Deep Learning & CNNs 🧠

**Goals Completed:**
- ✅ Understood the fundamentals of neural networks and deep learning
- ✅ Learned how Convolutional Neural Networks (CNNs) work
- ✅ Connected CNN concepts directly to visual defect detection in industrial settings

**Key Concepts Covered:**
- **Neural Networks:** neurons, layers, activation functions (ReLU, Sigmoid, Softmax), forward pass, backpropagation, gradient descent
- **Training Deep Networks:** loss functions (cross-entropy, MSE), optimizers (SGD, Adam), learning rate, epochs, batch size
- **Regularization:** dropout, batch normalization, L1/L2 regularization to prevent overfitting
- **Convolutional Neural Networks:**
  - Convolution operation — kernels/filters sliding over image to detect features
  - Pooling layers (Max Pooling, Average Pooling) — spatial downsampling
  - Fully connected layers — final classification
  - Classic architectures: LeNet, AlexNet, VGG, ResNet
- **Why CNNs for QA:** CNNs are spatially invariant — they can detect a scratch or crack regardless of where it appears in an image. This is critical for industrial inspection where defects can appear anywhere on a product surface.
- **Practical Implementation:** Built simple CNN in TensorFlow/Keras, trained on image classification tasks

**Resources Used:**
- Dswithbappy Deep Learning & CNN Playlist (Videos 1–32)


---

### Week 4 - Introduction to LLMs 💬

**Goals Completed:**
- ✅ Understood the architecture and training of Large Language Models
- ✅ Learned how LLMs are used in practice (prompting, APIs, fine-tuning)
- ✅ Connected LLM concepts to the multi-modal angle of the project

**Key Concepts Covered:**
- **Transformers Architecture:** attention mechanism, self-attention, multi-head attention, encoder-decoder structure, positional encoding
- **How LLMs Work:** pre-training on large text corpora (next-token prediction), the scale hypothesis, emergent capabilities
- **Key Models:** GPT family, BERT, LLaMA — differences in architecture (decoder-only vs encoder-only vs encoder-decoder)
- **Prompting:** zero-shot, few-shot, chain-of-thought prompting
- **Fine-tuning & RLHF:** how LLMs are aligned with human preferences
- **Multi-Modal LLMs:** models like GPT-4V, LLaVA that accept both image and text inputs - this is the **core architecture** our final project will build toward
- **Connection to Project:** In industrial QA, an LLM component can receive a description of detected anomalies from the vision module and generate a structured quality report, suggest root causes, or flag issues for human review

**Resources Used:**
- Andrej Karpathy's "Intro to LLMs" (1hr lecture)
- LLM Tutorial by Simplilearn / Krish Naik



---

## 🔑 Key Takeaways So Far

1. **Python is the backbone** of all ML/AI work - the first week's investment pays off in every subsequent notebook.
2. **Classical ML builds intuition** for understanding what neural networks are doing at a higher level of abstraction.
3. **CNNs are the natural choice** for image-based industrial inspection - their translational invariance and hierarchical feature learning map perfectly onto defect detection tasks.
4. **LLMs add the "intelligence layer"** that turns raw model outputs into actionable, human-readable quality reports - bridging the gap between AI predictions and real-world QA workflows.
5. **Multi-modal AI** is the frontier: combining vision + language in a single system is what makes this project novel and practically valuable for industry.

---

## 📁 Repository Structure

```
SOC/
├── README.md                          ← This file (Midterm Report)
├── Week1/
│   └── week1_python_basics.ipynb
├── Week2/
│   └── week2_ml_basics.ipynb
├── Week3/
│   └── week3_deep_learning_cnn.ipynb
└── Week4/
    └── week4_llm_intro.ipynb
```

---
edit 
