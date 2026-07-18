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

1. Upload steel surface image
2. YOLOv8 detects defects
3. Defects are extracted
4. Llama 3.2 generates inspection report
5. Results displayed in Streamlit

## Sample Detected Defects

- patches
- pitted_surface

## Author

Sameer Raj