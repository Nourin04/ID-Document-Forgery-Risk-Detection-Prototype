

# ID Document Forgery Risk Detection Prototype

## Overview

This project implements a prototype system for analyzing uploaded ID document images and generating a structured forgery risk report. The goal of the system is not to achieve perfect fraud detection accuracy but to demonstrate a practical approach to document authenticity analysis by combining computer vision techniques, AI-based reasoning, and a simple risk scoring framework.

The system accepts an image of an ID document, performs a set of automated validation and analysis checks, and produces a structured report indicating whether the document appears genuine or suspicious. The prototype exposes its functionality through a FastAPI backend and a web interface built with HTML, CSS, and JavaScript.

This project was designed as a proof-of-concept to demonstrate the integration of multiple AI and computer vision tools in a document verification pipeline.

---

## Objectives

The primary objectives of this prototype are:

* Accept an uploaded ID document image
* Validate the image format
* Perform basic tampering and quality checks using computer vision techniques
* Integrate AI-based reasoning using a vision-language model
* Generate a structured fraud detection report
* Display the analysis results through a web interface

---

## Key Features

### Image Upload Service

The system accepts uploaded ID document images via a REST API endpoint and through the web interface.

Supported formats:

* JPEG
* PNG

The uploaded file is temporarily stored in a local uploads directory before analysis.

---

### Image Validation

The system validates the uploaded file type to ensure that only supported image formats are processed.

Validation checks include:

* File type verification
* Prevention of unsupported file uploads

---

### Computer Vision-Based Document Analysis

The system uses OpenCV-based analysis to detect possible indicators of tampering or poor image quality.

The following signals are extracted:

#### Blur Detection

Blur detection is performed using Laplacian variance analysis. Blurry images may indicate low-quality captures or attempts to obscure manipulated areas.

#### Resolution Analysis

Low-resolution images can indicate screenshots or manipulated images that have been resized or compressed.

#### Edge Artifact Detection

Edge detection is used to identify irregular edge patterns, which may appear when text or regions are edited or inserted.

These signals form the foundation for the fraud risk scoring process.

---

### AI-Based Image Reasoning

The system integrates a multimodal AI model through the Gemini Vision API to provide additional reasoning about the authenticity of the document.

The vision-language model is prompted to analyze the uploaded image for potential signs of tampering, including:

* Inconsistent fonts
* Edited regions
* Unusual artifacts
* Misaligned text or layout
* Suspicious document structure

The model generates a textual analysis describing potential issues in the document.

---

### Fraud Risk Scoring Engine

A rule-based risk scoring engine aggregates the signals extracted during the analysis stage.

Each signal contributes to a cumulative risk score.

Example signals include:

* Image blur
* Low resolution
* Edge artifacts

The system generates a structured report containing:

* Fraud risk score
* Risk classification verdict
* List of detected signals

Example output:

```
{
  "risk_score": 25,
  "verdict": "Likely Genuine",
  "signals": [
    "Low resolution image"
  ]
}
```

---

### Web-Based User Interface

The prototype includes a simple web interface for interacting with the system.

The interface allows users to:

* Upload ID images
* Preview the uploaded document
* Trigger analysis
* View fraud detection results

The results panel displays:

* Image analysis metrics
* Fraud risk score
* Verdict classification
* Detected signals

A progress bar visually represents the fraud risk score.

---

## System Architecture

The overall system pipeline follows a modular architecture:

```
User Uploads ID Document
        │
        ▼
File Validation
        │
        ▼
Image Processing (OpenCV)
  - Blur detection
  - Resolution analysis
  - Edge artifact detection
        │
        ▼
AI Vision Analysis (Gemini Vision API)
        │
        ▼
Fraud Risk Scoring Engine
        │
        ▼
Structured Fraud Report
        │
        ▼
Web Interface Display
```

---

## Project Structure

```
id-fraud-detector
│
├── app.py
├── image_utils.py
├── fraud_detector.py
├── report_generator.py
├── config.py
│
├── uploads/
│
├── templates/
│   └── index.html
│
└── requirements.txt
```

### File Descriptions

**app.py**
Main FastAPI application. Handles image upload, processing workflow, and API responses.

**image_utils.py**
Contains OpenCV-based functions for blur detection, resolution analysis, and edge artifact detection.

**fraud_detector.py**
Handles interaction with the Gemini Vision API for AI-based document analysis.

**report_generator.py**
Implements the rule-based fraud risk scoring engine.

**config.py**
Stores configuration values such as the Gemini API key and model configuration.

**templates/index.html**
Web interface for uploading and analyzing ID documents.

**uploads/**
Temporary storage directory for uploaded images.

---

## Installation

### Requirements

* Python 3.9 or higher
* pip

---

### Install Dependencies

```
pip install -r requirements.txt
```

Dependencies include:

* fastapi
* uvicorn
* opencv-python
* pillow
* python-multipart
* google-generativeai
* pytesseract
* jinja2

---

## Running the Application

Start the FastAPI server using:

```
uvicorn app:app --reload
```

Open the web interface in a browser:

```
http://127.0.0.1:8000
```

---

## API Endpoint

### Upload ID Document

Endpoint:

```
POST /upload-id
```

Request:
Multipart form-data with an image file.

Response example:

```
{
  "filename": "id.png",
  "blur_detected": false,
  "resolution": "Low",
  "edge_score": 3207399,
  "fraud_report": {
      "risk_score": 25,
      "verdict": "Likely Genuine",
      "signals": ["Low resolution image"]
  }
}
```

---

## Limitations

### Limitations of the Gemini Vision API

The Gemini API integration provides useful reasoning capabilities but introduces several limitations.

#### API Quotas

Free-tier API usage is limited by strict request and token quotas. When these limits are exceeded, requests fail with quota errors.

#### Rate Limits

The API enforces request-per-minute limits, which can restrict high-frequency analysis scenarios.


---



## Future Improvements

Potential improvements include:

* Training a deep learning model for forgery detection
* Integrating OCR to verify textual information
* Implementing document layout verification using object detection
* Adding template matching for known ID document formats
* Improving the fraud risk scoring model using machine learning
* Supporting additional document types
* Deploying the system as a scalable cloud service

---

## Conclusion

This project demonstrates a prototype document verification system that combines computer vision techniques, AI-based reasoning, and structured risk scoring. While the system is not designed for production deployment, it illustrates a realistic architecture for automated ID document analysis and fraud risk estimation.

The prototype highlights how multiple AI tools can be integrated into a cohesive pipeline for document authenticity analysis.
