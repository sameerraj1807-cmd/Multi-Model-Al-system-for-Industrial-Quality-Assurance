# Multi-Modal AI System for Industrial Quality Assurance
### Seasons of Code (SoC) - IIT Bombay | Final Report

---

## 👤 About Me

- **Program:** Seasons of Code, IIT Bombay
- **Year:** Fresher (to-be Sophomore)
- **Project Title:** Multi-Modal AI System for Industrial Quality Assurance
- **Report Period:** Week 1 – Week 8 (Midterm & Endterm)

---

## 🎯 Project Overview

This project aims to build a **Multi-Modal AI system** capable of performing **industrial quality assurance** - detecting defects, anomalies, and quality issues in manufactured products using a combination of **computer vision (CNNs)** and **language models (LLMs)**. The system will take image input (camera feeds from production lines) and textual/structured sensor data, process them through separate modalities, and fuse the outputs to make quality decisions.

The first four weeks were dedicated to building the foundational knowledge required to undertake this project - covering Python, Machine Learning, Deep Learning, CNNs, and Large Language Models.

Building upon these foundations, Weeks 5–8 focused on the practical development and deployment of the system. A YOLOv8-based Computer Vision model was trained for steel surface defect detection using the NEU Surface Defect Dataset. The detected defects were then integrated with a locally deployed Llama 3.2 Large Language Model through Ollama to automatically generate professional inspection reports containing defect summaries, severity assessments, and recommended actions. Finally, the complete multi-modal pipeline was deployed as an interactive Streamlit web application, enabling users to upload steel surface images, detect defects in real time, and receive AI-generated inspection reports through a user-friendly interface.

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

### Week 5 - Exploratory Data Analysis (EDA) & Data Cleaning 📊

**Goals Completed:**
- ✅ Learned the fundamentals of Exploratory Data Analysis (EDA)
- ✅ Practiced data cleaning techniques using Python
- ✅ Understood the importance of data preprocessing before model training
- ✅ Gained familiarity with visualization and statistical analysis tools

**Key Concepts Covered:**
- **Exploratory Data Analysis (EDA):**
  - Understanding dataset structure
  - Identifying feature distributions
  - Detecting outliers and anomalies
  - Correlation analysis
  - Data visualization techniques
- **Data Cleaning:**
  - Handling missing values
  - Removing duplicates
  - Data formatting and transformation
  - Feature consistency checks
  - Noise reduction
- **Visualization Tools:**
  - Matplotlib
  - Pandas plotting utilities
  - Histograms
  - Scatter plots
  - Box plots
- **Connection to Project:**
  - Proper data analysis and cleaning are critical before training industrial defect detection models.
  - Understanding dataset quality directly impacts the performance of downstream Computer Vision systems.

**Resources Used:**
- Exploratory Data Analysis (EDA) Cheat Sheet
- Data Cleaning Colab Tutorial

---

### Week 6 - Computer Vision Model Development (YOLOv8) 👁️

**Goals Completed:**
- ✅ Trained a YOLOv8 model on the NEU Surface Defect Dataset
- ✅ Learned the object detection workflow
- ✅ Evaluated model performance using industry-standard metrics
- ✅ Generated prediction samples and confusion matrices
- ✅ Exported the final trained model (`best.pt`)

**Key Concepts Covered:**
- **Object Detection Fundamentals:**
  - Bounding Boxes
  - Class Labels
  - Confidence Scores
  - Intersection over Union (IoU)
- **YOLOv8 Architecture:**
  - One-stage object detection
  - Real-time inference
  - Detection head and feature extraction
- **Model Training Pipeline:**
  - Dataset preparation
  - Annotation formats
  - Training configuration
  - Hyperparameter selection
  - Validation and testing
- **Evaluation Metrics:**
  - Precision
  - Recall
  - mAP@50
  - mAP@50-95
  - Confusion Matrix Analysis
- **Practical Implementation:**
  - Trained YOLOv8 on steel surface defect images
  - Generated prediction samples
  - Exported final model weights (`best.pt`)
- **Connection to Project:**
  - The trained YOLOv8 model serves as the primary vision module responsible for identifying surface defects in steel products.

**Resources Used:**
- Ultralytics YOLOv8 Documentation
- NEU Surface Defect Dataset (Kaggle)

---

### Week 7 - LLM Integration & Report Generation 💬

**Goals Completed:**
- ✅ Installed and configured Ollama locally
- ✅ Integrated Llama 3.2 into the project workflow
- ✅ Connected Computer Vision outputs with a Large Language Model
- ✅ Generated automated inspection reports from detected defects

**Key Concepts Covered:**
- **Local LLM Deployment:**
  - Ollama installation and configuration
  - Running Llama 3.2 locally
  - Model management and inference
- **Prompt Engineering:**
  - Designing prompts for industrial reporting
  - Structured report generation
  - Context-aware response generation
- **Vision-Language Integration:**
  - Converting defect detections into textual descriptions
  - Passing defect information to LLMs
  - Generating actionable recommendations
- **Practical Implementation:**
  - Extracted detected defect classes from YOLOv8 outputs
  - Passed defect information to Llama 3.2
  - Generated professional inspection reports including:
    - Summary
    - Severity Assessment
    - Recommended Actions
- **Connection to Project:**
  - The LLM acts as the intelligence layer that transforms raw detections into human-readable industrial quality reports.

**Resources Used:**
- Ollama Documentation
- Llama 3.2 Model Documentation

---

### Week 8 - Deployment & Final Multi-Modal System 🚀

**Goals Completed:**
- ✅ Built a Streamlit web application
- ✅ Integrated YOLOv8 and Llama 3.2 into a single workflow
- ✅ Developed a complete AI-powered industrial quality assurance system
- ✅ Tested end-to-end functionality

**Key Concepts Covered:**
- **Streamlit Development:**
  - Interactive web interfaces
  - File upload components
  - Dynamic content rendering
  - Real-time user interaction
- **System Integration:**
  - Image upload
  - Defect detection
  - Defect processing
  - Report generation
  - User-facing output
- **Multi-Modal AI Workflow:**
  - Vision module (YOLOv8)
  - Language module (Llama 3.2)
  - Fusion of visual and textual information
- **Practical Implementation:**
  - Users enter inspection details
  - Upload steel surface images
  - YOLOv8 identifies defects
  - Llama 3.2 generates professional reports
  - Results displayed through Streamlit
- **Connection to Project:**
  - This completes the full Multi-Modal AI pipeline envisioned at the start of the project by combining Computer Vision and Language Models into a unified industrial quality assurance system.

**Resources Used:**
- Streamlit Documentation
- Ollama Documentation
- Ultralytics YOLOv8 Documentation

---

## 🔑 Key Takeaways (continued)

6. **Data quality directly impacts model performance** - effective exploratory data analysis and data cleaning are essential before training any AI model. Understanding dataset distributions, class balance, and annotation quality helps prevent poor model performance and unreliable predictions.

7. **Object detection extends beyond classification** - unlike traditional image classification, industrial inspection requires identifying the location and type of defects simultaneously. YOLOv8 proved highly effective for real-time defect detection through bounding box localization and multi-class classification.

8. **Model evaluation is as important as model training** - metrics such as precision, recall, mAP, confusion matrices, and validation predictions provide critical insights into model strengths, weaknesses, and real-world reliability.

9. **LLMs transform detections into actionable insights** - integrating Llama 3.2 with the defect detection pipeline demonstrated how language models can convert technical model outputs into structured inspection reports that are easier for engineers and quality assurance teams to interpret and act upon.

10. **End-to-end integration creates real-world value** - the combination of YOLOv8, Llama 3.2, Ollama, and Streamlit highlighted that successful AI systems require more than accurate models; they require seamless integration, usability, and deployment to solve practical industrial problems.

---

## 🏭 Final System Workflow

The completed system follows the workflow below:

1. User enters inspection details
   - Inspector Name
   - Project Location
   - Project ID

2. User uploads a steel surface image

3. YOLOv8 processes the image and detects defects

4. Detected defects are extracted and summarized

5. Defect information is passed to Llama 3.2 through Ollama

6. Llama generates a professional inspection report including:
   - Inspection Date
   - Detected Defects
   - Summary
   - Severity Assessment
   - Recommended Actions

7. Results are displayed through the Streamlit web interface

---

## 🎯 Final Project Outcome

Successfully developed a **Multi-Modal AI System for Industrial Quality Assurance** capable of:

- Detecting steel surface defects using Computer Vision (YOLOv8)
- Generating automated inspection reports using Large Language Models (Llama 3.2)
- Providing an interactive user interface through Streamlit
- Demonstrating practical integration of Vision AI and Generative AI for industrial applications

This project successfully combines the knowledge gained throughout all eight weeks into a complete end-to-end AI solution.


## 📁 Repository Structure

```
SOC/
│
├── README.md                                   ← Final Project Report (Week 1–8)
│
├── Week1_Python_Basics/
│   ├── Python_Basics.py
│   ├── Functions_Practice.py
│   └── Notes.md
│
├── Week2_ML_Basics/
│   ├── ML_Fundamentals.py
│   ├── Pandas_Practice.py
│   └── Notes.md
│
├── Week3_Deep_Learning_CNN/
│   ├── Neural_Network_Basics.py
│   ├── CNN_Concepts.py
│   └── Notes.md
│
├── Week4_LLM/
│   ├── Intro_to_LLM.py
│   ├── Prompt_Engineering.py
│   └── Notes.md
│
├── Week-5-6/
│   ├── README.md
│   ├── code.ipynb
│   ├── confusion_matrix.png
│   ├── confusion_matrix_normalized.png
│   ├── metrics.txt
│   ├── training_curves.png
│   ├── val_batch0_labels.jpg
│   └── val_batch0_pred.jpg
│
└── Week-7-8/
    ├── README.md
    ├── app.py
    ├── combined_test.py
    ├── report_test.py
    ├── requirements.txt
    ├── test_model.py
    └── train_batch0.jpg
```

### Folder Description

#### Week 5–6
Contains the Computer Vision development phase:
- Dataset exploration and preprocessing
- YOLOv8 training notebook
- Training metrics and evaluation results
- Confusion matrices
- Prediction samples
- Model performance analysis

#### Week 7–8
Contains the complete Multi-Modal AI system:
- YOLOv8 defect detection pipeline
- Llama 3.2 integration through Ollama
- AI-based inspection report generation
- Streamlit web application
- Testing scripts and deployment files

```
