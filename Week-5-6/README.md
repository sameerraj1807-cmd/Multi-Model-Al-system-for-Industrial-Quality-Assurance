# Week 5 & 6 - Exploratory Data Analysis and Computer Vision Model

## Overview

This phase focused on:

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Training a YOLOv8 model for steel defect detection

---

## Dataset

NEU Surface Defect Dataset

Defect Classes:

- Patches
- Pitted Surface
- Scratches
- Inclusion
- Rolled-in Scale
- Crazing

---

## Model

YOLOv8 Medium (YOLOv8m)

The model was trained on the NEU dataset and exported as:

best.pt

---

## Performance Metrics

| Metric | Value |
|----------|----------|
| Precision | 0.75 |
| Recall | 0.76 |
| mAP@50 | 0.75 |
| mAP@50-95 | 0.44 |

---

## Results

Training curves, confusion matrix and prediction samples are included.

Files:

- confusion_matrix.png
- val_batch0_pred.jpg
- training curves.png
---

## Output

The trained model successfully detects steel surface defects and is used in the deployment phase.

## Trained Model

Due to GitHub upload limitations, the trained YOLOv8 model is available at:

<[Google Drive link](https://drive.google.com/file/d/1hR8TxluBROBlZTDzHtPYSdjz8dyVhUmI/view?usp=sharing)>

neu_yolo_runs at:

<[Google Drive link](https://drive.google.com/drive/folders/17dQFv5ASZ23UY_d_vJTjL9T0maVzs0WQ?usp=sharing)>
