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

## Example Output

The application detects defects and generates a professional inspection report using a local LLM.
