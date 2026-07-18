# Week 7 & 8 - LLM Integration and Deployment

## Overview

This phase integrates:

- YOLOv8 defect detection
- Streamlit web application
- Ollama
- Llama 3.2

to create an AI-powered industrial quality assurance system.

---

## Workflow

1. Upload steel image
2. Run YOLOv8 detection
3. Identify defects
4. Send defects to Llama 3.2
5. Generate inspection report
6. Display results in Streamlit

---

## Technologies Used

- Python
- YOLOv8
- Streamlit
- Ollama
- Llama 3.2

---

## Features

### Defect Detection

Detected defects include:

- Patches
- Pitted Surface
- Scratches
- Inclusion
- Rolled-in Scale

---

### AI Inspection Report

The system automatically generates:

- Inspection Date
- Inspector Name
- Project Location
- Project ID
- Summary
- Severity Assessment
- Recommended Actions

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

---
## Workflow

The AI-Powered Industrial Quality Assurance System follows the workflow below:

### Step 1: User Inputs Inspection Details
The user enters:
- Inspector Name
- Project Location
- Project ID

These details are used to personalize the inspection report.

---

### Step 2: Upload Steel Surface Image
The user uploads a steel surface image through the Streamlit web application.

Supported image formats:
- JPG
- JPEG
- PNG

---

### Step 3: Defect Detection using YOLOv8
The uploaded image is processed by the trained YOLOv8 model (`best.pt`).

The model analyzes the steel surface and identifies defects such as:
- Pitted Surface
- Patches
- Scratches
- Inclusion
- Rolled-in Scale
- Crazing

The detected defect classes are extracted and displayed to the user.

---

### Step 4: Defect Information Processing
Duplicate detections are removed and a clean list of unique defects is prepared.

Example:

Detected Defects:
- Pitted Surface
- Patches

---

### Step 5: AI Report Generation using Llama 3.2
The detected defects along with the inspection details are sent to a locally running Large Language Model (Llama 3.2) through Ollama.

The model generates a professional inspection report containing:
- Inspection Date
- Inspector Name
- Project Location
- Project ID
- Detected Defects
- Summary
- Severity Assessment
- Recommended Actions

---

### Step 6: Results Display
The Streamlit application displays:
1. Uploaded Image
2. Detected Defects
3. AI-Generated Inspection Report

This allows inspectors and quality assurance teams to quickly review defects and take corrective actions.

---

## System Architecture

Steel Surface Image
↓
YOLOv8 Detection Model (best.pt)
↓
Defect Identification
↓
Llama 3.2 (Ollama)
↓
Inspection Report Generation
↓
Streamlit Web Application
↓
Final Output to User

---

## Example Output

Inspection Report

Inspection Date: 17 July 2026

Detected Defects:
- Pitted Surface
- Patches

Summary:
Surface defects were detected on the steel sheet. These defects may affect surface quality and should be inspected before further processing.

Severity:
Medium

Recommended Actions:
- Inspect affected regions manually
- Verify material quality
- Monitor production line for recurring defects
- Perform final quality verification before shipment
