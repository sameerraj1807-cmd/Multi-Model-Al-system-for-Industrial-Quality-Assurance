# AI-Powered Industrial Quality Assurance System

## Project Overview

This project detects steel surface defects using a YOLOv8 model and generates AI-powered inspection reports using Llama 3.2 through Ollama.

## Features

- Upload steel surface images
- Detect defects using YOLOv8
- Display detected defects
- Generate professional inspection reports using AI
- Streamlit web application

## Technologies Used

- Python
- YOLOv8
- Streamlit
- Ollama
- Llama 3.2

## Trained Model

Due to GitHub upload limitations, the trained YOLOv8 model is available at:

<[Google Drive link](https://drive.google.com/file/d/1hR8TxluBROBlZTDzHtPYSdjz8dyVhUmI/view?usp=sharing)>

neu_yolo_runs at:

<[Google Drive link](https://drive.google.com/drive/folders/17dQFv5ASZ23UY_d_vJTjL9T0maVzs0WQ?usp=sharing)>


## Project Structure

```text
Industrial-QA-System
│
├── app.py
├── best.pt
├── requirements.txt
└── README.md
```

## How To Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama run llama3.2
```

Run the application:

```bash
streamlit run app.py
```

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
