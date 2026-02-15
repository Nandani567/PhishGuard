# Product Requirements Document (PRD)
## ML-Based Phishing URL Detection System

---

**Document Version:** 1.0  
**Author:** [Your Name]  
**Date:** February 15, 2026  
**Project Type:** Final Year Major Project  
**Status:** Draft

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Problem Statement](#problem-statement)
3. [Objectives](#objectives)
4. [Scope](#scope)
5. [Stakeholders](#stakeholders)
6. [System Architecture](#system-architecture)
7. [Functional Requirements](#functional-requirements)
8. [Non-Functional Requirements](#non-functional-requirements)
9. [Technical Specifications](#technical-specifications)
10. [User Interface Requirements](#user-interface-requirements)
11. [Data Requirements](#data-requirements)
12. [Security & Privacy](#security-privacy)
13. [Testing Strategy](#testing-strategy)
14. [Timeline & Milestones](#timeline-milestones)
15. [Success Metrics](#success-metrics)
16. [Risks & Mitigation](#risks-mitigation)
17. [Future Enhancements](#future-enhancements)

---

## 1. Executive Summary

This document outlines the requirements for developing an ML-based Phishing URL Detection System designed to protect users from malicious phishing attacks in real-time. The system leverages machine learning algorithms to analyze URLs and identify potential phishing threats before users interact with suspicious websites.

The solution consists of three core components:
- **Machine Learning Backend**: A FastAPI-based Python service that hosts trained ML models for URL classification
- **Detection Engine**: Utilizes ensemble methods (XGBoost/Random Forest) to achieve high accuracy in phishing detection
- **Chrome Extension Frontend**: A lightweight browser extension providing real-time protection with minimal user interaction

The system aims to provide an accessible, fast, and accurate phishing detection solution for everyday internet users, reducing the risk of credential theft, financial fraud, and malware infection through proactive URL screening.

---

## 2. Problem Statement

### 2.1 Background

Phishing attacks remain one of the most prevalent and effective cyber threats, with millions of users falling victim annually. According to recent cybersecurity reports, phishing attacks have increased by 150% since 2020, with attackers employing increasingly sophisticated techniques to bypass traditional security measures.

### 2.2 Current Limitations

Existing phishing detection solutions face several challenges:

- **Blacklist-Based Approaches**: Traditional blacklist methods are reactive, requiring known phishing sites to be catalogued before detection
- **Delayed Updates**: Blacklists often lag behind new phishing campaigns by hours or days
- **High False Positive Rates**: Legacy rule-based systems generate excessive false alarms, leading to user fatigue
- **Limited Real-Time Protection**: Many solutions lack seamless integration with browsing workflows
- **Resource Intensive**: Server-side solutions may introduce latency and privacy concerns

### 2.3 Target Problem

Users need a proactive, intelligent, and privacy-respecting solution that can:
- Identify phishing URLs in real-time before page load
- Distinguish between legitimate and malicious sites with high accuracy
- Operate with minimal performance impact on browsing experience
- Function without sending complete browsing history to external servers

---

## 3. Objectives

### 3.1 Primary Objectives

1. **Develop a Machine Learning Model** capable of detecting phishing URLs with ≥95% accuracy and ≤5% false positive rate

2. **Build a FastAPI Backend Service** that:
   - Serves ML model predictions via RESTful API
   - Processes URL classification requests in <200ms
   - Handles concurrent requests efficiently

3. **Create a Chrome Extension** that:
   - Intercepts navigation events before page load
   - Displays clear warnings for suspected phishing sites
   - Provides intuitive user controls and settings

4. **Ensure Real-Time Performance** with end-to-end response time under 500ms for typical URL checks

### 3.2 Secondary Objectives

1. **Educational Component**: Provide users with information about detected phishing indicators to improve security awareness

2. **Whitelist Management**: Allow users to manually approve trusted sites to reduce false positive impact

3. **Analytics Dashboard**: Generate usage statistics and threat detection reports for system monitoring

4. **Model Versioning**: Implement infrastructure for continuous model improvement and deployment

5. **Cross-Platform Foundation**: Design architecture extensible to Firefox and Edge extensions in future iterations

---

## 4. Scope

### 4.1 In Scope

#### Phase 1: Core Development
- Data collection and preprocessing pipeline for phishing/legitimate URL datasets
- Feature engineering from URL strings (lexical, host-based, and content-based features)
- Training and evaluation of ML models (XGBoost, Random Forest, ensemble methods)
- FastAPI backend implementation with model serving endpoints
- Chrome extension development with core detection functionality
- Real-time URL interception and classification
- User notification system for phishing warnings
- Basic whitelist/blacklist management

#### Phase 2: Enhancement & Testing
- Model optimization and hyperparameter tuning
- Extension UI/UX refinement
- Performance benchmarking and optimization
- Security testing and vulnerability assessment
- User acceptance testing with target demographic
- Documentation and deployment guides

### 4.2 Out of Scope

The following features are explicitly excluded from the current project scope:

- **Multi-Browser Support**: Firefox, Safari, Edge extensions (future roadmap)
- **Mobile Applications**: iOS/Android native apps
- **Email Phishing Detection**: Analysis of email content or attachments
- **SMS/Text Message Phishing**: Detection of smishing attacks
- **Social Media Phishing**: Platform-specific social engineering attacks
- **Advanced Threat Analysis**: Deep packet inspection, malware analysis
- **Enterprise Features**: Centralized management, SIEM integration, compliance reporting
- **Blockchain Integration**: Decentralized threat intelligence sharing
- **AI-Powered Content Analysis**: Deep learning models for webpage visual analysis
- **Automated Takedown**: Reporting to authorities or registrars
- **VPN/Network Security**: Network-level protection mechanisms

---

## 5. Stakeholders

### 5.1 Primary Stakeholders

| Stakeholder | Role | Responsibilities |
|-------------|------|------------------|
| Project Developer(s) | System Architect & Developer | Design, development, testing, documentation |
| Project Supervisor | Academic Advisor | Guidance, progress review, evaluation |
| End Users | General Browser Users | System usage, feedback, acceptance testing |

### 5.2 Secondary Stakeholders

| Stakeholder | Interest | Involvement |
|-------------|----------|-------------|
| Academic Institution | Educational Outcomes | Project evaluation, grade assignment |
| Potential Employers | Technical Capability Assessment | Portfolio review, skill evaluation |
| Open Source Community | Code Reusability | Potential contributors, users (if open-sourced) |
| Cybersecurity Researchers | Methodology Validation | Technical feedback, academic citation |

---

## 6. System Architecture

### 6.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Chrome Browser                          │
│  ┌───────────────────────────────────────────────────────┐  │
│  │           Chrome Extension (Frontend)                  │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐ │  │
│  │  │  Content     │  │  Background  │  │   Popup     │ │  │
│  │  │  Script      │  │  Service     │  │   UI        │ │  │
│  │  └──────────────┘  └──────────────┘  └─────────────┘ │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTPS/REST API
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend (Python)                 │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                  API Layer                            │  │
│  │  • /predict endpoint                                  │  │
│  │  • /health endpoint                                   │  │
│  │  • /feedback endpoint                                 │  │
│  └───────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Feature Extraction Module                │  │
│  │  • URL parsing and tokenization                       │  │
│  │  • Feature computation                                │  │
│  └───────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │               ML Model Layer                          │  │
│  │  • XGBoost/Random Forest models                       │  │
│  │  • Ensemble prediction                                │  │
│  │  • Confidence scoring                                 │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   Data & Model Storage                      │
│  • Trained model artifacts (.pkl, .joblib)                  │
│  • Feature vectorizers                                      │
│  • Configuration files                                      │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Component Descriptions

#### 6.2.1 Chrome Extension (Frontend)
- **Content Script**: Intercepts navigation events, extracts URLs from page
- **Background Service**: Manages API communication, caching, state management
- **Popup UI**: Provides user settings, whitelist management, statistics display

#### 6.2.2 FastAPI Backend
- **API Gateway**: Handles HTTP requests, authentication, rate limiting
- **Feature Extractor**: Processes URLs to generate ML model input features
- **ML Inference Engine**: Loads models, performs prediction, calculates confidence scores
- **Response Formatter**: Structures API responses with detection results

#### 6.2.3 Data Pipeline (Development)
- **Dataset Collection**: Aggregation of phishing and legitimate URL datasets
- **Preprocessing**: Data cleaning, normalization, train-test splitting
- **Feature Engineering**: Extraction of lexical, host-based, and statistical features
- **Model Training**: Algorithm selection, training, validation, serialization

---

## 6.3 System Overview

### 6.3.1 System Purpose

The ML-Based Phishing URL Detection System is a distributed cybersecurity solution designed to provide real-time protection against phishing attacks through intelligent URL analysis. The system operates as a client-server architecture where lightweight browser-based clients leverage a centralized machine learning inference engine to classify URLs before users interact with potentially malicious websites.

### 6.3.2 Operational Workflow

```
User Navigation Event
        ↓
[1] Extension intercepts URL
        ↓
[2] Local cache check (24hr TTL)
        ↓
    Cache Hit? ──Yes──→ [3a] Return cached result
        │                      ↓
       No                [9] Display result to user
        ↓
[3b] Extract URL from request
        ↓
[4] Send HTTPS POST to /predict endpoint
        ↓
[5] Backend: Extract features from URL
        ↓
[6] Backend: ML model inference
        ↓
[7] Backend: Generate confidence score
        ↓
[8] Return classification + confidence
        ↓
[9] Extension: Cache result locally
        ↓
[10] Risk assessment (confidence threshold)
        ↓
    High Risk (>80%)? ──Yes──→ [11a] Block page + warning
        │                              ↓
       No                        User can override
        ↓
    Medium Risk (60-80%)? ──Yes──→ [11b] Warning banner
        │                              ↓
       No                        User can proceed
        ↓
[11c] Allow navigation (Low Risk <60%)
        ↓
[12] Log detection event (optional analytics)
```

### 6.3.3 Data Flow Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                           │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │              CHROME EXTENSION LAYER                      │ │
│  │                                                          │ │
│  │  Input: Navigation Event (URL)                          │ │
│  │  Processing: Local cache lookup, API communication      │ │
│  │  Output: User warning/allow decision                    │ │
│  │                                                          │ │
│  │  Cache: Local Storage (24hr)                            │ │
│  │  - URL hash → Classification result                     │ │
│  │  - Whitelist domains                                    │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
                              ↓ ↑
                         HTTPS REST API
                              ↓ ↑
┌────────────────────────────────────────────────────────────────┐
│                      BACKEND SERVER                            │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                   API GATEWAY LAYER                      │ │
│  │                                                          │ │
│  │  Input: HTTP POST /predict {url: string}                │ │
│  │  Processing: Validation, rate limiting, routing         │ │
│  │  Output: HTTP 200 {prediction, confidence}              │ │
│  │                                                          │ │
│  │  Middleware: CORS, logging, error handling              │ │
│  └──────────────────────────────────────────────────────────┘ │
│                              ↓                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │            FEATURE EXTRACTION MODULE                     │ │
│  │                                                          │ │
│  │  Input: Raw URL string                                  │ │
│  │  Processing:                                            │ │
│  │    • URL parsing (scheme, domain, path, query)          │ │
│  │    • Lexical feature computation (length, char counts)  │ │
│  │    • Host-based features (domain age, SSL status)       │ │
│  │    • Statistical features (entropy, token patterns)     │ │
│  │  Output: Feature vector (30-50 dimensions)              │ │
│  │                                                          │ │
│  │  Dependencies: urllib.parse, tldextract, re             │ │
│  └──────────────────────────────────────────────────────────┘ │
│                              ↓                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │              ML INFERENCE ENGINE                         │ │
│  │                                                          │ │
│  │  Input: Feature vector (numpy array)                    │ │
│  │  Processing:                                            │ │
│  │    • Feature scaling/normalization                      │ │
│  │    • Model prediction (XGBoost/Random Forest)           │ │
│  │    • Probability calibration                            │ │
│  │    • Ensemble voting (if multiple models)               │ │
│  │  Output: Binary classification + confidence [0-1]       │ │
│  │                                                          │ │
│  │  Loaded Models: XGBoost (.pkl), Scaler (.joblib)        │ │
│  └──────────────────────────────────────────────────────────┘ │
│                              ↓                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │              RESPONSE FORMATTER                          │ │
│  │                                                          │ │
│  │  Input: Prediction, confidence, features                │ │
│  │  Processing:                                            │ │
│  │    • Risk level categorization                          │ │
│  │    • Response JSON serialization                        │ │
│  │    • Logging and metrics collection                     │ │
│  │  Output: Structured API response                        │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────┐
│                    PERSISTENT STORAGE                          │
│                                                                │
│  • Trained ML models (.pkl, .joblib)                          │
│  • Feature transformers (scalers, encoders)                   │
│  • Configuration files (config.yaml)                          │
│  • Model metadata (version, metrics, timestamp)               │
│  • Request logs (optional, anonymized)                        │
└────────────────────────────────────────────────────────────────┘
```

### 6.3.4 Deployment Architecture

```
Development Environment:
┌─────────────────────────────────────────┐
│  Developer Workstation                  │
│  • Python 3.10+ (Backend development)   │
│  • Node.js/npm (Extension build tools)  │
│  • Jupyter Notebook (ML experiments)    │
│  • Git (Version control)                │
│  • Chrome Browser (Testing)             │
└─────────────────────────────────────────┘

Testing/Staging Environment:
┌─────────────────────────────────────────┐
│  Local Server / VM                      │
│  • FastAPI backend (uvicorn)            │
│  • Localhost:8000 API endpoint          │
│  • Unpacked extension (Developer mode)  │
│  • Test datasets for validation         │
└─────────────────────────────────────────┘

Production Environment (Post-Project):
┌─────────────────────────────────────────┐
│  Cloud Platform (AWS/Azure/GCP)         │
│  • Backend: Container (Docker)          │
│  • Load Balancer (Optional)             │
│  • HTTPS/TLS Certificate                │
│  • Extension: Chrome Web Store          │
│  • Monitoring: CloudWatch/Prometheus    │
└─────────────────────────────────────────┘
```

---

## 6.4 Detailed Component Breakdown

### 6.4.1 Machine Learning Layer

#### **Purpose and Responsibilities**

The Machine Learning Layer serves as the intelligent core of the phishing detection system, responsible for analyzing URL characteristics and determining the likelihood of malicious intent. This layer encompasses the entire ML pipeline from training to inference.

#### **Sub-Components**

##### A. Training Pipeline (Offline Component)

**Responsibilities:**
- Ingest and preprocess raw URL datasets from multiple sources
- Perform exploratory data analysis to identify relevant features
- Engineer discriminative features from URL strings
- Handle class imbalance through sampling techniques
- Train multiple candidate models (XGBoost, Random Forest, Gradient Boosting)
- Optimize hyperparameters using grid search or Bayesian optimization
- Evaluate model performance using cross-validation
- Select best-performing model based on evaluation metrics
- Serialize trained models for deployment

**Inputs:**
- Raw URL datasets (CSV/JSON format)
  - Phishing URLs: PhishTank, OpenPhish (~50,000 samples)
  - Legitimate URLs: Alexa Top 1M, Common Crawl (~50,000 samples)
- Feature engineering specifications (Python scripts)
- Training configuration (hyperparameters, validation strategy)

**Outputs:**
- Trained model file: `phishing_model_v1.0.pkl` (XGBoost model)
- Feature scaler: `feature_scaler.joblib` (StandardScaler/MinMaxScaler)
- Feature extractor: `feature_extractor.pkl` (custom feature engineering pipeline)
- Model metadata: `model_metadata.json` (accuracy, precision, recall, feature importance)
- Training report: `training_report.pdf` (performance plots, confusion matrix)

**Dependencies:**
- **Libraries:**
  - scikit-learn (v1.3+): Model training, preprocessing, evaluation
  - XGBoost (v2.0+): Gradient boosting algorithm
  - pandas (v2.0+): Data manipulation
  - numpy (v1.24+): Numerical computations
  - matplotlib/seaborn: Visualization
  - joblib: Model serialization
- **Data Sources:**
  - PhishTank API
  - OpenPhish feed
  - Alexa Top Sites
- **Hardware:**
  - Minimum: 8GB RAM, 4-core CPU
  - Recommended: 16GB RAM, GPU (optional for deep learning experiments)

**Key Algorithms:**
```
Primary Model: XGBoost Classifier
- n_estimators: 100-300
- max_depth: 5-10
- learning_rate: 0.01-0.1
- subsample: 0.8
- colsample_bytree: 0.8
- objective: binary:logistic
- eval_metric: logloss, auc

Alternative Model: Random Forest Classifier
- n_estimators: 100-200
- max_depth: 10-20
- min_samples_split: 2-5
- min_samples_leaf: 1-2
- class_weight: balanced

Ensemble: Voting Classifier (Soft voting)
- Combines XGBoost + Random Forest predictions
- Weights: [0.6, 0.4] (tuned based on validation performance)
```

##### B. Feature Extraction Module

**Responsibilities:**
- Parse raw URL strings into structured components
- Compute lexical features (character statistics, special symbol counts)
- Extract host-based features (domain properties, TLD analysis)
- Generate derived features (entropy, n-gram patterns)
- Handle missing or malformed URLs gracefully
- Transform features to model-compatible format

**Inputs:**
- Raw URL string (e.g., `"https://secure-login.paypal-verify.tk/signin"`)

**Outputs:**
- Feature vector (numpy array or dictionary), example:
```python
{
    "url_length": 55,
    "num_dots": 4,
    "num_hyphens": 3,
    "num_underscores": 0,
    "num_slashes": 3,
    "num_questionmarks": 0,
    "num_equals": 0,
    "num_at": 0,
    "num_ampersands": 0,
    "num_digits": 0,
    "num_subdomains": 3,
    "domain_length": 24,
    "path_length": 7,
    "has_ip_address": 0,
    "is_https": 1,
    "suspicious_tld": 1,  # .tk domain
    "url_entropy": 4.23,
    "vowel_consonant_ratio": 0.67,
    "digit_letter_ratio": 0.0,
    "has_shortening_service": 0,
    "subdomain_depth": 3,
    "path_depth": 1,
    "domain_token_count": 3,
    "avg_domain_token_length": 8.0,
    "longest_subdomain": 14,
    "domain_has_hyphen": 1,
    "path_has_hyphen": 0,
    # ... (30+ total features)
}
```

**Dependencies:**
- **Libraries:**
  - `urllib.parse`: URL parsing
  - `tldextract`: Domain extraction
  - `re`: Regular expressions
  - `math`: Entropy calculation
  - `numpy`: Array operations
- **External APIs (Optional):**
  - WHOIS service (domain age)
  - Google Safe Browsing API (reputation check)

**Feature Categories:**

| Category | Features | Example |
|----------|----------|---------|
| **Lexical** | URL length, character counts, symbol frequency | 55 chars, 4 dots, 3 hyphens |
| **Host-based** | Domain length, subdomain count, TLD type | 24 chars, 3 subdomains, .tk TLD |
| **Statistical** | Entropy, token statistics, ratios | 4.23 entropy, 0.67 vowel ratio |
| **Binary Flags** | IP address presence, HTTPS, URL shortener | has_ip=0, is_https=1 |
| **Derived** | Path depth, longest token, special patterns | depth=1, longest=14 |

##### C. Inference Engine

**Responsibilities:**
- Load pre-trained ML models into memory at startup
- Accept feature vectors from API layer
- Perform model prediction (classification)
- Generate probability scores for phishing/legitimate classes
- Apply ensemble voting if multiple models are used
- Return binary classification and confidence score
- Optimize for low-latency inference (<50ms)

**Inputs:**
- Feature vector: numpy array shape (1, n_features) where n_features ≈ 30-50
- Model version (optional): Specify which model to use for A/B testing

**Outputs:**
- Classification: `0` (legitimate) or `1` (phishing)
- Confidence score: Float [0.0-1.0] representing probability of phishing
- Prediction metadata:
```python
{
    "prediction": 1,  # Phishing
    "confidence": 0.92,
    "probabilities": {
        "legitimate": 0.08,
        "phishing": 0.92
    },
    "model_version": "v1.0",
    "inference_time_ms": 23
}
```

**Dependencies:**
- **Loaded Models:**
  - XGBoost model object
  - Feature scaler (StandardScaler)
  - Feature name mapping (for correct ordering)
- **Libraries:**
  - xgboost: Model inference
  - joblib: Model loading
  - numpy: Array operations

**Performance Optimizations:**
- **Model Loading**: Load models once at startup (not per request)
- **Batch Prediction**: Support batch inference for multiple URLs (future)
- **Model Quantization**: Reduce model size using post-training quantization
- **Caching**: Cache predictions for identical URLs (application layer)

##### D. Model Evaluation Module (Offline)

**Responsibilities:**
- Compute standard ML metrics (accuracy, precision, recall, F1, AUC)
- Generate confusion matrix and classification report
- Analyze per-class performance
- Identify feature importance rankings
- Detect potential bias or overfitting
- Create visualization of model performance
- Compare multiple model candidates

**Inputs:**
- Trained model object
- Test dataset (features + labels)
- Validation configuration

**Outputs:**
- Evaluation metrics report:
```
Accuracy: 0.9623
Precision: 0.9456
Recall: 0.9701
F1-Score: 0.9577
ROC-AUC: 0.9845

Confusion Matrix:
                 Predicted Negative  Predicted Positive
Actual Negative         4,782                243
Actual Positive           149              4,826

False Positive Rate: 0.0484
False Negative Rate: 0.0300
```
- Feature importance plot (top 20 features)
- ROC curve and Precision-Recall curve
- Learning curves (training vs. validation performance)

**Dependencies:**
- scikit-learn: metrics module
- matplotlib/seaborn: Plotting
- pandas: Data handling

---

### 6.4.2 Backend API Layer

#### **Purpose and Responsibilities**

The Backend API Layer provides a RESTful interface for URL classification requests, orchestrates communication between the browser extension and ML inference engine, and ensures secure, scalable, and performant operation.

#### **Sub-Components**

##### A. FastAPI Application Core

**Responsibilities:**
- Expose HTTP endpoints for URL classification
- Handle concurrent requests asynchronously
- Implement request/response validation using Pydantic models
- Manage application lifecycle (startup, shutdown)
- Provide automatic API documentation (Swagger/OpenAPI)
- Configure CORS policies for browser extension access

**Inputs:**
- HTTP POST requests to `/predict` endpoint:
```json
{
    "url": "https://suspicious-bank-login.tk/verify",
    "user_id": "anonymous",  # Optional
    "include_features": false  # Optional: return feature vector
}
```

**Outputs:**
- HTTP 200 response:
```json
{
    "status": "success",
    "url": "https://suspicious-bank-login.tk/verify",
    "prediction": "phishing",
    "confidence": 0.92,
    "risk_level": "high",
    "timestamp": "2026-02-15T10:30:45.123Z",
    "model_version": "v1.0",
    "features": {  # If include_features=true
        "url_length": 45,
        "num_dots": 3,
        ...
    }
}
```
- HTTP error responses (400, 429, 500)

**Dependencies:**
- **Framework:** FastAPI (v0.100+)
- **ASGI Server:** Uvicorn (v0.23+)
- **Validation:** Pydantic (v2.0+)
- **Async Runtime:** asyncio
- **HTTP Client:** httpx (for external API calls)

**Key Endpoints:**

| Endpoint | Method | Purpose | Rate Limit |
|----------|--------|---------|------------|
| `/predict` | POST | Classify URL | 100/min per IP |
| `/health` | GET | Health check | Unlimited |
| `/metrics` | GET | System metrics | Admin only |
| `/feedback` | POST | User feedback | 20/min per IP |
| `/docs` | GET | API documentation | Unlimited |

##### B. Request Validation & Preprocessing

**Responsibilities:**
- Validate URL format and structure
- Sanitize input to prevent injection attacks
- Normalize URLs (lowercase, remove trailing slash)
- Extract domain and path components
- Reject malformed or dangerous URLs
- Apply rate limiting per IP address
- Log incoming requests for monitoring

**Inputs:**
- Raw HTTP request body (JSON)
- Request headers (User-Agent, Origin)
- Client IP address

**Outputs:**
- Validated and normalized URL string
- HTTP 400 error for invalid requests
- HTTP 429 error for rate limit violations

**Dependencies:**
- Pydantic: Data validation
- validators library: URL validation
- slowapi: Rate limiting middleware
- fastapi.Request: Access client information

**Validation Rules:**
```python
class URLPredictRequest(BaseModel):
    url: HttpUrl  # Pydantic URL validation
    user_id: Optional[str] = "anonymous"
    include_features: bool = False
    
    @validator('url')
    def validate_url(cls, v):
        # Additional custom validation
        if len(str(v)) > 2048:
            raise ValueError("URL too long (max 2048 chars)")
        if not v.scheme in ['http', 'https']:
            raise ValueError("Only HTTP/HTTPS URLs supported")
        return v
```

##### C. Feature Extraction Service

**Responsibilities:**
- Interface with ML Feature Extraction Module
- Call feature extraction functions on validated URLs
- Handle extraction errors gracefully
- Cache computed features (optional optimization)
- Transform features to model input format

**Inputs:**
- Validated URL string: `"https://suspicious-site.tk/login"`

**Outputs:**
- Feature vector ready for model inference
- Error message if extraction fails

**Dependencies:**
- Feature extraction module (from ML layer)
- Custom feature engineering functions
- numpy: Array formatting

**Integration:**
```python
from ml.feature_extractor import FeatureExtractor

extractor = FeatureExtractor()

async def extract_features(url: str):
    try:
        features = extractor.extract(url)
        return features
    except Exception as e:
        logger.error(f"Feature extraction failed: {e}")
        raise HTTPException(status_code=500, 
                          detail="Feature extraction error")
```

##### D. ML Model Interface

**Responsibilities:**
- Load ML models during application startup
- Maintain model objects in memory
- Route feature vectors to appropriate model
- Retrieve predictions and confidence scores
- Handle model errors and fallbacks
- Support A/B testing with multiple model versions

**Inputs:**
- Feature vector from Feature Extraction Service
- Model version identifier (optional)

**Outputs:**
- Prediction: integer (0=legitimate, 1=phishing)
- Confidence: float [0-1]
- Model metadata: version, inference time

**Dependencies:**
- Trained model files (.pkl, .joblib)
- xgboost/sklearn libraries
- numpy

**Model Loading Strategy:**
```python
from joblib import load
import xgboost as xgb

class ModelManager:
    def __init__(self):
        self.models = {}
        self.scalers = {}
    
    def load_models(self):
        # Load at startup, not per request
        self.models['v1.0'] = load('models/xgboost_v1.0.pkl')
        self.scalers['v1.0'] = load('models/scaler_v1.0.joblib')
        logger.info("Models loaded successfully")
    
    async def predict(self, features, version='v1.0'):
        scaled_features = self.scalers[version].transform([features])
        prediction = self.models[version].predict(scaled_features)[0]
        confidence = self.models[version].predict_proba(scaled_features)[0]
        return prediction, max(confidence)
```

##### E. Response Formatting Service

**Responsibilities:**
- Transform raw model outputs into structured API responses
- Categorize risk levels based on confidence thresholds
- Add timestamps and metadata
- Format JSON responses according to API specification
- Include optional debug information

**Inputs:**
- Model prediction (0 or 1)
- Confidence score (0.0-1.0)
- Original URL
- Feature vector (optional)

**Outputs:**
- Structured JSON response conforming to API schema

**Dependencies:**
- Pydantic: Response models
- datetime: Timestamp generation

**Risk Level Categorization:**
```python
def categorize_risk(confidence: float, prediction: int) -> str:
    if prediction == 0:  # Legitimate
        return "safe"
    elif confidence >= 0.80:
        return "high"
    elif confidence >= 0.60:
        return "medium"
    else:
        return "low"
```

##### F. Logging & Monitoring Service

**Responsibilities:**
- Log all API requests (URL hash, not full URL for privacy)
- Record prediction results for analysis
- Track performance metrics (latency, throughput)
- Monitor error rates and types
- Generate health status reports
- Alert on anomalies or failures

**Inputs:**
- Request metadata (timestamp, IP, endpoint)
- Response data (prediction, latency)
- Error messages and stack traces

**Outputs:**
- Structured log entries (JSON format)
- Performance metrics for dashboards
- Health status (healthy/degraded/unhealthy)

**Dependencies:**
- logging: Python standard library
- prometheus_client: Metrics export (optional)
- Custom logger configuration

**Log Format:**
```json
{
    "timestamp": "2026-02-15T10:30:45.123Z",
    "level": "INFO",
    "endpoint": "/predict",
    "method": "POST",
    "url_hash": "sha256:abc123...",
    "prediction": "phishing",
    "confidence": 0.92,
    "latency_ms": 87,
    "status_code": 200,
    "client_ip": "192.168.1.100",
    "user_agent": "Chrome Extension/1.0"
}
```

##### G. Error Handling & Recovery

**Responsibilities:**
- Catch and handle exceptions gracefully
- Return appropriate HTTP status codes
- Provide meaningful error messages
- Implement retry logic for transient failures
- Log errors for debugging
- Prevent information leakage in error messages

**Error Responses:**
```python
# 400 Bad Request
{
    "status": "error",
    "error_code": "INVALID_URL",
    "message": "URL format is invalid",
    "details": "Missing scheme (http/https)"
}

# 429 Too Many Requests
{
    "status": "error",
    "error_code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests",
    "retry_after": 60
}

# 500 Internal Server Error
{
    "status": "error",
    "error_code": "INTERNAL_ERROR",
    "message": "An unexpected error occurred",
    "request_id": "req_abc123"
}
```

---

### 6.4.3 Browser Extension Layer

#### **Purpose and Responsibilities**

The Browser Extension Layer provides the user-facing interface for the phishing detection system, running directly in the user's Chrome browser to intercept navigation events, communicate with the backend API, and display warnings or allow safe browsing.

#### **Sub-Components**

##### A. Background Service Worker (Manifest V3)

**Responsibilities:**
- Listen for navigation events across all tabs
- Intercept URL requests before page load
- Manage communication with backend API
- Coordinate between content scripts and popup UI
- Handle extension lifecycle events
- Maintain extension state and cache
- Process alarm events for cache cleanup

**Inputs:**
- `chrome.webNavigation.onBeforeNavigate` events
- Messages from content scripts and popup
- User settings from storage
- API responses from backend

**Outputs:**
- API calls to backend `/predict` endpoint
- Messages to content scripts (display warnings)
- Storage updates (cache, whitelist, settings)
- Navigation blocking decisions (redirect to warning page)

**Dependencies:**
- **Chrome APIs:**
  - `chrome.webNavigation`: URL interception
  - `chrome.storage.local`: Persistent storage
  - `chrome.runtime`: Messaging
  - `chrome.alarms`: Scheduled tasks
  - `chrome.tabs`: Tab management
- **Permissions:**
  - `webNavigation`, `storage`, `alarms`, `activeTab`
  - Host permission: `<all_urls>`

**Key Functions:**
```javascript
// Main navigation listener
chrome.webNavigation.onBeforeNavigate.addListener(
    async (details) => {
        if (details.frameId !== 0) return; // Main frame only
        
        const url = details.url;
        
        // Check whitelist
        if (await isWhitelisted(url)) return;
        
        // Check cache
        const cached = await getCachedResult(url);
        if (cached) {
            handlePrediction(cached, details.tabId);
            return;
        }
        
        // Call API
        const result = await classifyURL(url);
        await cacheResult(url, result);
        handlePrediction(result, details.tabId);
    }
);
```

##### B. Content Script

**Responsibilities:**
- Inject warning UI into web pages
- Display advisory banners for suspicious URLs
- Handle user interactions (proceed/go back buttons)
- Extract page URLs for analysis
- Listen for messages from background script
- Modify DOM to show warnings

**Inputs:**
- Messages from background service worker
- Page URL and DOM
- User click events on warning UI elements

**Outputs:**
- Rendered warning UI elements
- User feedback messages to background script
- Page navigation control (allow/block)

**Dependencies:**
- **Chrome APIs:**
  - `chrome.runtime.onMessage`: Receive commands
  - `chrome.runtime.sendMessage`: Send responses
- **Web APIs:**
  - DOM manipulation
  - Event listeners

**Warning UI Injection:**
```javascript
function injectWarningBanner(predictionData) {
    const banner = document.createElement('div');
    banner.id = 'phishing-warning-banner';
    banner.innerHTML = `
        <div class="warning-content">
            <span class="warning-icon">⚠️</span>
            <span class="warning-text">
                Suspicious website detected (${Math.round(predictionData.confidence * 100)}% confidence)
            </span>
            <button id="trust-site-btn">Trust This Site</button>
            <button id="go-back-btn">Go Back</button>
        </div>
    `;
    banner.style.cssText = `
        position: fixed; top: 0; width: 100%; 
        background: #FFC107; color: #000; 
        padding: 15px; z-index: 999999;
    `;
    document.body.insertBefore(banner, document.body.firstChild);
    
    // Attach event listeners
    document.getElementById('trust-site-btn').addEventListener('click', () => {
        chrome.runtime.sendMessage({action: 'whitelist', url: window.location.href});
        banner.remove();
    });
}
```

##### C. Blocking Warning Page

**Responsibilities:**
- Display full-page warning for high-risk URLs
- Provide clear information about the threat
- Show confidence score and detection details
- Offer "Go Back" and "Continue Anyway" options
- Report false positives to backend
- Educate users about phishing risks

**Inputs:**
- URL that triggered the warning
- Confidence score from backend
- Detection timestamp

**Outputs:**
- Full-page warning HTML
- User decision (go back / continue / report)
- Whitelist addition if user trusts site

**Dependencies:**
- HTML/CSS for warning page
- JavaScript for interaction handling

**Warning Page Structure:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Phishing Warning</title>
    <link rel="stylesheet" href="warning.css">
</head>
<body>
    <div class="warning-container">
        <div class="warning-icon-large">🛡️</div>
        <h1>Phishing Threat Detected</h1>
        <p class="url-display">Suspicious URL: <code id="url-text"></code></p>
        <p class="confidence">Detection Confidence: <strong id="confidence-text"></strong></p>
        
        <div class="threat-info">
            <h3>What is phishing?</h3>
            <p>Phishing sites attempt to steal your passwords, credit card numbers, 
               or other sensitive information by impersonating legitimate websites.</p>
        </div>
        
        <div class="action-buttons">
            <button id="go-back-btn" class="btn-primary">
                ← Go Back to Safety
            </button>
            <button id="continue-btn" class="btn-secondary">
                Continue Anyway (Not Recommended)
            </button>
        </div>
        
        <div class="feedback-section">
            <a href="#" id="report-false-positive">Report False Positive</a>
        </div>
    </div>
    <script src="warning.js"></script>
</body>
</html>
```

##### D. Popup UI

**Responsibilities:**
- Display extension status and statistics
- Provide settings interface
- Show recent detections log
- Allow whitelist management
- Toggle protection on/off
- Display current tab risk status

**Inputs:**
- Extension storage data (settings, statistics, whitelist)
- Current tab URL
- User interactions

**Outputs:**
- Updated settings saved to storage
- Whitelist additions/removals
- User preference changes

**Dependencies:**
- **Chrome APIs:**
  - `chrome.storage.local`: Read/write settings
  - `chrome.tabs.query`: Get active tab
- **HTML/CSS:** Popup UI structure
- **JavaScript:** UI logic and event handling

**Popup Components:**
```
┌────────────────────────────────────┐
│  Phishing Detector     [Settings]  │
├────────────────────────────────────┤
│  🛡️ Protection: ON                 │
│                                    │
│  Today's Statistics:               │
│  ✓ URLs Checked: 127               │
│  ⚠️ Threats Blocked: 3             │
│  ℹ️ Warnings Shown: 8               │
│                                    │
│  Current Tab: ✓ Safe               │
│  example.com                       │
│                                    │
│  [Whitelist Manager]               │
│  [View Recent Detections]          │
└────────────────────────────────────┘
```

##### E. Local Cache Manager

**Responsibilities:**
- Store recent URL classifications locally
- Implement 24-hour TTL (time-to-live) for cached entries
- Reduce API calls for frequently visited sites
- Invalidate cache entries on user request
- Manage cache size limits
- Clean up expired entries automatically

**Inputs:**
- URL and classification result from API
- Current timestamp
- Cache size limit configuration

**Outputs:**
- Cached results for URL lookups
- Cache hit/miss statistics

**Dependencies:**
- `chrome.storage.local`: Persistent storage (max 10MB)
- `chrome.alarms`: Periodic cache cleanup

**Cache Structure:**
```javascript
{
    "cache": {
        "sha256_hash_of_url_1": {
            "prediction": "legitimate",
            "confidence": 0.12,
            "risk_level": "safe",
            "timestamp": 1708000000000,
            "expires": 1708086400000  // 24 hours later
        },
        "sha256_hash_of_url_2": {
            "prediction": "phishing",
            "confidence": 0.89,
            "risk_level": "high",
            "timestamp": 1708010000000,
            "expires": 1708096400000
        }
    },
    "whitelist": [
        "google.com",
        "github.com",
        "stackoverflow.com"
    ],
    "statistics": {
        "urls_checked": 1247,
        "threats_blocked": 32,
        "warnings_shown": 78,
        "false_positives_reported": 2
    }
}
```

##### F. Whitelist Management

**Responsibilities:**
- Maintain list of user-trusted domains
- Check URLs against whitelist before API call
- Provide UI for adding/removing trusted sites
- Export/import whitelist for backup
- Sync whitelist across devices (optional with chrome.storage.sync)

**Inputs:**
- User requests to trust/untrust domains
- Whitelist data from storage

**Outputs:**
- Updated whitelist in storage
- Bypass decisions for whitelisted domains

**Dependencies:**
- `chrome.storage.local` or `chrome.storage.sync`

**Whitelist Operations:**
```javascript
async function addToWhitelist(url) {
    const domain = extractDomain(url);
    const whitelist = await getWhitelist();
    if (!whitelist.includes(domain)) {
        whitelist.push(domain);
        await chrome.storage.local.set({ whitelist });
        console.log(`Added ${domain} to whitelist`);
    }
}

async function isWhitelisted(url) {
    const domain = extractDomain(url);
    const whitelist = await getWhitelist();
    return whitelist.includes(domain);
}
```

##### G. Settings Manager

**Responsibilities:**
- Store and retrieve user preferences
- Provide default settings on first install
- Validate settings inputs
- Apply settings changes immediately
- Export/import settings for backup

**Settings Schema:**
```javascript
{
    "settings": {
        "protection_enabled": true,
        "sensitivity": "medium",  // low, medium, high
        "show_notifications": true,
        "cache_enabled": true,
        "cache_duration_hours": 24,
        "anonymous_analytics": false,
        "api_endpoint": "https://api.example.com",
        "confidence_threshold_block": 0.80,
        "confidence_threshold_warn": 0.60,
        "auto_whitelist_common_sites": true
    }
}
```

---

### 6.4.4 Adversarial Testing Module

#### **Purpose and Responsibilities**

The Adversarial Testing Module evaluates the robustness of the phishing detection system against sophisticated evasion techniques, adversarial examples, and edge cases. This module is crucial for identifying vulnerabilities before deployment and improving model resilience.

#### **Sub-Components**

##### A. URL Obfuscation Generator

**Responsibilities:**
- Generate adversarial URL variants through obfuscation techniques
- Test model robustness against evasion strategies
- Simulate attacker behavior patterns
- Identify blind spots in feature extraction
- Create challenging test cases for model hardening

**Inputs:**
- Known phishing URLs from test dataset
- Obfuscation technique specifications
- Attack strategy parameters

**Outputs:**
- Adversarial URL examples
- Detection evasion success rate
- Feature vector perturbations
- Vulnerability report

**Dependencies:**
- urllib.parse: URL manipulation
- Custom obfuscation libraries
- Test dataset

**Obfuscation Techniques:**

| Technique | Description | Example |
|-----------|-------------|---------|
| **Homograph Attack** | Replace characters with visually similar Unicode | `paypal.com` → `pаypal.com` (Cyrillic 'а') |
| **Subdomain Manipulation** | Add legitimate-looking subdomains | `paypal.com` → `login.paypal.secure-verification.tk` |
| **URL Encoding** | Percent-encode URL components | `/login` → `/%6C%6F%67%69%6E` |
| **IP Address Obfuscation** | Use IP instead of domain | `paypal.com` → `64.4.250.36` |
| **Decimal/Hex IP** | Convert IP to different formats | `64.4.250.36` → `http://1074660900/` (decimal) |
| **Path Confusion** | Add legitimate domain in path | `evil.tk/paypal.com/login` |
| **URL Shortening** | Hide destination behind shortener | `bit.ly/xyz123` → `malicious-phishing-site.tk` |
| **Typosquatting** | Slight misspellings | `paypal.com` → `paypa1.com`, `paypai.com` |
| **Double Encoding** | Encode twice | `/login` → `/%25%36%43%25%36%46%25%67%36%39%25%36%45` |
| **Fragment Abuse** | Use URL fragments to deceive | `evil.tk#paypal.com/login` |

**Test Suite:**
```python
class AdversarialURLGenerator:
    def generate_obfuscated_urls(self, original_url, techniques):
        """
        Generate adversarial variants of a URL
        
        Args:
            original_url: Base phishing URL
            techniques: List of obfuscation methods to apply
        
        Returns:
            List of obfuscated URLs with metadata
        """
        variants = []
        
        for technique in techniques:
            if technique == 'homograph':
                variants.append(self._homograph_attack(original_url))
            elif technique == 'subdomain':
                variants.append(self._subdomain_manipulation(original_url))
            elif technique == 'encoding':
                variants.append(self._url_encoding(original_url))
            # ... more techniques
        
        return variants
    
    def _homograph_attack(self, url):
        """Replace ASCII chars with visually similar Unicode"""
        replacements = {
            'a': 'а',  # Cyrillic a (U+0430)
            'e': 'е',  # Cyrillic e (U+0435)
            'o': 'о',  # Cyrillic o (U+043E)
            # ... more replacements
        }
        obfuscated = url
        for ascii_char, unicode_char in replacements.items():
            obfuscated = obfuscated.replace(ascii_char, unicode_char)
        return obfuscated
```

##### B. Model Robustness Tester

**Responsibilities:**
- Test model against adversarial examples
- Measure detection rate for obfuscated URLs
- Identify feature importance under attack
- Calculate adversarial robustness metrics
- Generate adversarial training data
- Benchmark against baseline defenses

**Inputs:**
- Trained ML model
- Set of adversarial URLs
- Original (non-obfuscated) URLs
- Ground truth labels

**Outputs:**
- Adversarial evaluation metrics:
  - Detection rate on adversarial examples
  - Average confidence drop under attack
  - Most effective evasion techniques
  - Feature sensitivity analysis
- Adversarial training dataset (for model improvement)

**Dependencies:**
- Trained model
- Feature extraction module
- Adversarial URL generator
- Evaluation metrics library

**Evaluation Metrics:**
```python
class AdversarialEvaluator:
    def evaluate_robustness(self, model, original_urls, adversarial_urls):
        """
        Evaluate model robustness against adversarial attacks
        
        Returns:
            Dictionary of robustness metrics
        """
        results = {
            'original_detection_rate': 0.0,
            'adversarial_detection_rate': 0.0,
            'evasion_success_rate': 0.0,
            'avg_confidence_drop': 0.0,
            'by_technique': {}
        }
        
        # Test on original URLs
        original_preds = [model.predict(url) for url in original_urls]
        results['original_detection_rate'] = sum(original_preds) / len(original_preds)
        
        # Test on adversarial URLs
        adv_preds = [model.predict(url) for url in adversarial_urls]
        results['adversarial_detection_rate'] = sum(adv_preds) / len(adv_preds)
        
        # Calculate evasion success (how many phishing URLs now classified as legitimate)
        results['evasion_success_rate'] = 1 - results['adversarial_detection_rate']
        
        return results
```

**Target Metrics:**
- Adversarial Detection Rate: >85% (target: maintain high detection despite obfuscation)
- Confidence Drop: <20% (robustness to perturbations)
- Evasion Success Rate: <15% (attacker difficulty)

##### C. Edge Case Tester

**Responsibilities:**
- Test boundary conditions and unusual inputs
- Evaluate handling of malformed URLs
- Test internationalized domain names (IDN)
- Verify behavior on edge network conditions
- Identify unexpected model behavior
- Document corner cases for model improvement

**Test Cases:**

| Category | Test Case | Expected Behavior |
|----------|-----------|-------------------|
| **Malformed URLs** | `http://` (no domain) | Graceful error handling |
| **Very Long URLs** | 5000+ character URL | Truncation or rejection |
| **Special Characters** | URLs with emoji, RTL marks | Proper parsing or rejection |
| **IDN Domains** | `münchen.de` (punycode) | Correct normalization |
| **Uncommon Schemes** | `ftp://`, `file://` | Rejection or classification |
| **IPv6 Addresses** | `http://[2001:db8::1]/` | Proper feature extraction |
| **Multiple Redirects** | URL chain with 5+ hops | Follow or timeout |
| **Empty Query Params** | `example.com?&&&` | Normalize correctly |

**Implementation:**
```python
class EdgeCaseTester:
    def run_edge_case_tests(self, system):
        """Run comprehensive edge case test suite"""
        test_results = []
        
        edge_cases = [
            ("Empty URL", "", "should_reject"),
            ("Only scheme", "https://", "should_reject"),
            ("Very long domain", "a" * 2000 + ".com", "should_handle"),
            ("IDN homograph", "pаypal.com", "should_detect"),
            ("Multiple dots", "www...example..com", "should_normalize"),
            # ... more cases
        ]
        
        for test_name, test_url, expected in edge_cases:
            try:
                result = system.classify(test_url)
                status = self._evaluate_result(result, expected)
                test_results.append({
                    'test': test_name,
                    'url': test_url,
                    'status': status,
                    'result': result
                })
            except Exception as e:
                test_results.append({
                    'test': test_name,
                    'url': test_url,
                    'status': 'exception',
                    'error': str(e)
                })
        
        return self._generate_report(test_results)
```

##### D. Performance Stress Tester

**Responsibilities:**
- Simulate high-load conditions
- Measure system performance under stress
- Identify bottlenecks and resource limits
- Test concurrent request handling
- Evaluate cache effectiveness
- Monitor memory leaks and resource exhaustion

**Test Scenarios:**

| Scenario | Load Profile | Success Criteria |
|----------|--------------|------------------|
| **Baseline** | 10 requests/sec | <200ms latency, 0% errors |
| **Normal Load** | 50 requests/sec | <250ms latency, <1% errors |
| **Peak Load** | 100 requests/sec | <500ms latency, <5% errors |
| **Stress Test** | 200 requests/sec | Graceful degradation |
| **Spike Test** | 0→150→0 in 10sec | Quick recovery |
| **Sustained** | 50 req/s for 1 hour | No memory leaks |

**Implementation:**
```python
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

class StressTester:
    async def run_load_test(self, target_url, requests_per_second, duration_seconds):
        """
        Execute load test against API endpoint
        
        Returns:
            Performance metrics (latency, throughput, error rate)
        """
        total_requests = requests_per_second * duration_seconds
        interval = 1.0 / requests_per_second
        
        results = []
        start_time = time.time()
        
        async def send_request():
            req_start = time.time()
            try:
                response = await self._api_call(target_url)
                latency = (time.time() - req_start) * 1000  # ms
                results.append({
                    'latency': latency,
                    'success': response.status == 200
                })
            except Exception as e:
                results.append({
                    'latency': None,
                    'success': False,
                    'error': str(e)
                })
        
        # Schedule requests at target rate
        tasks = []
        for i in range(total_requests):
            tasks.append(send_request())
            await asyncio.sleep(interval)
        
        await asyncio.gather(*tasks)
        
        return self._analyze_results(results, time.time() - start_time)
```

##### E. Security Vulnerability Scanner

**Responsibilities:**
- Test for common web vulnerabilities (OWASP Top 10)
- Attempt injection attacks (SQL, XSS, command injection)
- Test API authentication and authorization
- Verify input sanitization effectiveness
- Check for information disclosure
- Test CORS and HTTPS configuration

**Security Tests:**

| Vulnerability | Test Method | Mitigation Verification |
|---------------|-------------|------------------------|
| **SQL Injection** | Submit URLs with SQL payloads | Input validation, parameterized queries |
| **XSS** | URLs with `<script>` tags | Output encoding, CSP headers |
| **Command Injection** | URLs with shell metacharacters | Input sanitization |
| **Path Traversal** | URLs with `../../../etc/passwd` | Path normalization |
| **XML Injection** | URLs with XML entities | XML parser configuration |
| **SSRF** | URLs pointing to internal IPs | URL whitelist/blacklist |
| **Rate Limit Bypass** | Distributed requests | IP-based rate limiting |
| **Auth Bypass** | Requests without tokens | Auth middleware verification |

**Dependencies:**
- requests library: HTTP testing
- Security testing frameworks (e.g., OWASP ZAP API)
- Custom payload generators

---

## 6.5 Backend Requirements

### 6.5.1 Backend Overview

The backend service is the core processing engine of the phishing detection system, responsible for receiving URL classification requests from browser extensions, extracting relevant features, performing machine learning inference, and returning classification results. Built with FastAPI, the backend is designed for high performance, scalability, and ease of deployment.

#### Architecture Philosophy

The backend follows a **layered architecture** pattern:

```
┌─────────────────────────────────────────────────────────┐
│                    API Gateway Layer                    │
│  (Request routing, validation, authentication)          │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                   Business Logic Layer                  │
│  (Feature extraction, model inference, result formatting)│
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                   Data Access Layer                     │
│  (Model loading, configuration, logging)                │
└─────────────────────────────────────────────────────────┘
```

#### Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Web Framework** | FastAPI | 0.104+ | Async API framework with automatic docs |
| **ASGI Server** | Uvicorn | 0.24+ | Production-grade ASGI server |
| **ML Framework** | XGBoost | 2.0+ | Gradient boosting for classification |
| **Data Processing** | Pandas | 2.1+ | Data manipulation and feature engineering |
| **Numerical Computing** | NumPy | 1.26+ | Array operations and mathematical functions |
| **Model Serialization** | Joblib | 1.3+ | Efficient model persistence |
| **Validation** | Pydantic | 2.5+ | Request/response validation |
| **HTTP Client** | HTTPX | 0.25+ | Async HTTP requests (external APIs) |
| **Logging** | Python logging | 3.10+ | Structured application logging |
| **Testing** | Pytest | 7.4+ | Unit and integration testing |
| **API Documentation** | OpenAPI/Swagger | Built-in | Automatic interactive API docs |

#### Design Principles

1. **Stateless Design**: Each request is independent; no session state stored
2. **Fail Fast**: Input validation at API boundary; reject invalid requests immediately
3. **Graceful Degradation**: Return cached results or default safe behavior on failures
4. **Observable**: Comprehensive logging and metrics for monitoring
5. **Secure by Default**: HTTPS only, input sanitization, rate limiting
6. **Performance First**: Async operations, model preloading, efficient feature extraction

---

### 6.5.2 Backend Functional Requirements

#### Core API Endpoints

| Req ID | Requirement | Priority | Acceptance Criteria |
|--------|-------------|----------|---------------------|
| **FR-B001** | URL Classification Endpoint | Critical | System shall expose POST /predict endpoint that accepts URL and returns classification |
| **FR-B002** | Health Check Endpoint | Critical | System shall expose GET /health endpoint returning service status |
| **FR-B003** | Metrics Endpoint | High | System shall expose GET /metrics endpoint returning performance statistics |
| **FR-B004** | API Documentation | High | System shall auto-generate OpenAPI docs at /docs endpoint |
| **FR-B005** | Version Endpoint | Medium | System shall expose GET /version endpoint returning API and model versions |
| **FR-B006** | Feedback Endpoint | Low | System shall expose POST /feedback for user feedback collection |

#### Input Processing

| Req ID | Requirement | Priority | Acceptance Criteria |
|--------|-------------|----------|---------------------|
| **FR-B007** | URL Validation | Critical | System shall validate URL format using regex and reject malformed URLs |
| **FR-B008** | URL Normalization | High | System shall normalize URLs (lowercase domain, remove trailing slash, decode percent encoding) |
| **FR-B009** | Request Size Limit | High | System shall reject requests with URL length >2048 characters |
| **FR-B010** | Content-Type Validation | High | System shall only accept application/json content type |
| **FR-B011** | Scheme Validation | High | System shall only accept http:// and https:// URL schemes |
| **FR-B012** | Input Sanitization | Critical | System shall sanitize all inputs to prevent injection attacks |

#### Feature Extraction

| Req ID | Requirement | Priority | Acceptance Criteria |
|--------|-------------|----------|---------------------|
| **FR-B013** | Lexical Feature Extraction | Critical | System shall extract 15+ lexical features (length, character counts, special symbols) |
| **FR-B014** | Host-Based Feature Extraction | Critical | System shall extract 10+ host-based features (domain structure, TLD, subdomains) |
| **FR-B015** | Statistical Feature Extraction | High | System shall compute statistical features (entropy, token statistics) |
| **FR-B016** | Feature Vector Generation | Critical | System shall generate standardized feature vector for model input |
| **FR-B017** | Feature Scaling | High | System shall apply trained scaler to normalize feature values |
| **FR-B018** | Missing Feature Handling | High | System shall handle missing features using default values or imputation |

#### Model Inference

| Req ID | Requirement | Priority | Acceptance Criteria |
|--------|-------------|----------|---------------------|
| **FR-B019** | Model Loading | Critical | System shall load trained ML model(s) during startup |
| **FR-B020** | Prediction Generation | Critical | System shall classify URL as phishing (1) or legitimate (0) |
| **FR-B021** | Confidence Score | Critical | System shall return confidence score [0.0-1.0] with prediction |
| **FR-B022** | Inference Timeout | High | System shall timeout model inference after 5 seconds |
| **FR-B023** | Model Versioning | Medium | System shall support loading multiple model versions |
| **FR-B024** | Ensemble Prediction | Low | System shall optionally combine predictions from multiple models |

#### Response Formatting

| Req ID | Requirement | Priority | Acceptance Criteria |
|--------|-------------|----------|---------------------|
| **FR-B025** | Structured Response | Critical | System shall return JSON response with prediction, confidence, timestamp |
| **FR-B026** | Risk Level Categorization | High | System shall categorize risk as high/medium/low based on confidence |
| **FR-B027** | Feature Return (Optional) | Low | System shall optionally include extracted features in response |
| **FR-B028** | Error Response Format | High | System shall return consistent error format with code and message |
| **FR-B029** | Response Metadata | Medium | System shall include model version and inference time in response |

#### Error Handling

| Req ID | Requirement | Priority | Acceptance Criteria |
|--------|-------------|----------|---------------------|
| **FR-B030** | Input Validation Errors | Critical | System shall return 400 Bad Request for invalid inputs |
| **FR-B031** | Rate Limit Errors | High | System shall return 429 Too Many Requests when limit exceeded |
| **FR-B032** | Server Errors | Critical | System shall return 500 Internal Server Error for unexpected failures |
| **FR-B033** | Model Loading Errors | Critical | System shall fail to start if models cannot be loaded |
| **FR-B034** | Graceful Degradation | High | System shall return safe default (block) on inference failures |
| **FR-B035** | Error Logging | High | System shall log all errors with stack traces for debugging |

#### Logging & Monitoring

| Req ID | Requirement | Priority | Acceptance Criteria |
|--------|-------------|----------|---------------------|
| **FR-B036** | Request Logging | High | System shall log all incoming requests with timestamp, IP, endpoint |
| **FR-B037** | Performance Logging | High | System shall log inference time for each request |
| **FR-B038** | Error Logging | Critical | System shall log all errors with severity level and context |
| **FR-B039** | Privacy-Preserving Logs | Critical | System shall log URL hash (SHA-256), not full URL |
| **FR-B040** | Structured Logging | Medium | System shall use JSON format for logs |
| **FR-B041** | Log Rotation | Medium | System shall rotate logs daily and retain for 30 days |

---

### 6.5.3 API Specification

#### 6.5.3.1 POST /predict - URL Classification

**Endpoint**: `/predict`  
**Method**: `POST`  
**Content-Type**: `application/json`  
**Authentication**: None (public endpoint with rate limiting)

##### Request Schema

```json
{
  "url": "string (required)",
  "user_id": "string (optional)",
  "include_features": "boolean (optional, default: false)",
  "model_version": "string (optional, default: 'latest')"
}
```

##### Request Field Specifications

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `url` | string | Yes | 1-2048 chars, valid URL format | The URL to classify |
| `user_id` | string | No | Max 64 chars | Anonymous user identifier for analytics |
| `include_features` | boolean | No | true/false | Whether to return extracted features |
| `model_version` | string | No | Max 16 chars | Model version to use (e.g., 'v1.0', 'latest') |

##### Request Example

```json
{
  "url": "https://secure-login.paypal-verify.tk/signin?next=account",
  "user_id": "anon_user_12345",
  "include_features": false,
  "model_version": "v1.0"
}
```

##### Response Schema (Success - 200 OK)

```json
{
  "status": "success",
  "request_id": "string",
  "timestamp": "string (ISO 8601)",
  "url": "string",
  "prediction": "string (enum: 'phishing', 'legitimate')",
  "confidence": "number (0.0-1.0)",
  "risk_level": "string (enum: 'safe', 'low', 'medium', 'high')",
  "model_version": "string",
  "inference_time_ms": "number",
  "features": "object (optional)"
}
```

##### Response Field Specifications

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Request status: "success" or "error" |
| `request_id` | string | Unique identifier for request tracing |
| `timestamp` | string | ISO 8601 timestamp of response generation |
| `url` | string | The URL that was classified (normalized) |
| `prediction` | string | Classification result: "phishing" or "legitimate" |
| `confidence` | float | Model confidence score (0.0 = certain legitimate, 1.0 = certain phishing) |
| `risk_level` | string | Risk categorization: "safe" (<0.3), "low" (0.3-0.6), "medium" (0.6-0.8), "high" (>0.8) |
| `model_version` | string | Version of model used for prediction |
| `inference_time_ms` | float | Time taken for model inference in milliseconds |
| `features` | object | Extracted feature vector (only if include_features=true) |

##### Response Example (Phishing Detected)

```json
{
  "status": "success",
  "request_id": "req_8f3d9a2b1c4e",
  "timestamp": "2026-02-15T10:30:45.123Z",
  "url": "https://secure-login.paypal-verify.tk/signin",
  "prediction": "phishing",
  "confidence": 0.92,
  "risk_level": "high",
  "model_version": "v1.0",
  "inference_time_ms": 23.5,
  "features": {
    "url_length": 45,
    "num_dots": 4,
    "num_hyphens": 3,
    "num_subdomains": 3,
    "suspicious_tld": 1,
    "url_entropy": 4.23,
    "has_ip_address": 0,
    "is_https": 1
  }
}
```

##### Response Example (Legitimate URL)

```json
{
  "status": "success",
  "request_id": "req_7a2c8b9d5f1e",
  "timestamp": "2026-02-15T10:31:12.456Z",
  "url": "https://www.google.com/search",
  "prediction": "legitimate",
  "confidence": 0.08,
  "risk_level": "safe",
  "model_version": "v1.0",
  "inference_time_ms": 18.2
}
```

##### Error Responses

**400 Bad Request - Invalid URL Format**

```json
{
  "status": "error",
  "error_code": "INVALID_URL",
  "message": "URL format is invalid",
  "details": "URL must include scheme (http:// or https://)",
  "request_id": "req_9e4f2a8b3d7c",
  "timestamp": "2026-02-15T10:32:00.789Z"
}
```

**400 Bad Request - URL Too Long**

```json
{
  "status": "error",
  "error_code": "URL_TOO_LONG",
  "message": "URL exceeds maximum length",
  "details": "Maximum URL length is 2048 characters. Received 3500 characters.",
  "request_id": "req_3c7d9f2e8a1b",
  "timestamp": "2026-02-15T10:33:15.234Z"
}
```

**400 Bad Request - Invalid Scheme**

```json
{
  "status": "error",
  "error_code": "INVALID_SCHEME",
  "message": "Unsupported URL scheme",
  "details": "Only http:// and https:// schemes are supported. Received: ftp://",
  "request_id": "req_5a8e2c9f7d3b",
  "timestamp": "2026-02-15T10:34:20.567Z"
}
```

**422 Unprocessable Entity - Validation Error**

```json
{
  "status": "error",
  "error_code": "VALIDATION_ERROR",
  "message": "Request validation failed",
  "details": [
    {
      "field": "url",
      "error": "field required",
      "type": "value_error.missing"
    }
  ],
  "request_id": "req_2d9f8c3a7e6b",
  "timestamp": "2026-02-15T10:35:30.890Z"
}
```

**429 Too Many Requests - Rate Limit Exceeded**

```json
{
  "status": "error",
  "error_code": "RATE_LIMIT_EXCEEDED",
  "message": "Too many requests",
  "details": "Rate limit: 100 requests per minute. Try again in 45 seconds.",
  "retry_after": 45,
  "request_id": "req_6b2e9d8f4c1a",
  "timestamp": "2026-02-15T10:36:45.123Z"
}
```

**500 Internal Server Error - Model Inference Failure**

```json
{
  "status": "error",
  "error_code": "INFERENCE_ERROR",
  "message": "Model inference failed",
  "details": "An unexpected error occurred during URL classification. The issue has been logged.",
  "request_id": "req_4f9c7e2a8d3b",
  "timestamp": "2026-02-15T10:37:50.456Z"
}
```

**503 Service Unavailable - Model Not Loaded**

```json
{
  "status": "error",
  "error_code": "SERVICE_UNAVAILABLE",
  "message": "Service is temporarily unavailable",
  "details": "ML model is not loaded. Please try again in a few moments.",
  "request_id": "req_8e3d9c2f7a1b",
  "timestamp": "2026-02-15T10:38:55.789Z"
}
```

##### Status Code Summary

| Status Code | Description | Use Case |
|-------------|-------------|----------|
| **200 OK** | Successful classification | Valid request processed successfully |
| **400 Bad Request** | Invalid request data | Malformed URL, invalid parameters |
| **422 Unprocessable Entity** | Validation failed | Missing required fields, type errors |
| **429 Too Many Requests** | Rate limit exceeded | Too many requests from same IP |
| **500 Internal Server Error** | Server error | Unexpected errors, model failures |
| **503 Service Unavailable** | Service not ready | Model not loaded, maintenance mode |

##### cURL Examples

**Basic Request**

```bash
curl -X POST https://api.phishing-detector.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://suspicious-site.tk/login"
  }'
```

**Request with Optional Parameters**

```bash
curl -X POST https://api.phishing-detector.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://secure-banking.example.tk/verify",
    "user_id": "test_user_001",
    "include_features": true,
    "model_version": "v1.0"
  }'
```

**Python Requests Example**

```python
import requests

url = "https://api.phishing-detector.com/predict"
payload = {
    "url": "https://paypal-verify.suspicious.tk/login",
    "include_features": False
}

response = requests.post(url, json=payload)
result = response.json()

if result['status'] == 'success':
    print(f"Prediction: {result['prediction']}")
    print(f"Confidence: {result['confidence']:.2%}")
    print(f"Risk Level: {result['risk_level']}")
else:
    print(f"Error: {result['message']}")
```

**JavaScript Fetch Example**

```javascript
const url = 'https://api.phishing-detector.com/predict';
const payload = {
  url: 'https://suspicious-login.tk/account',
  include_features: false
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(payload)
})
  .then(response => response.json())
  .then(data => {
    if (data.status === 'success') {
      console.log(`Prediction: ${data.prediction}`);
      console.log(`Confidence: ${(data.confidence * 100).toFixed(1)}%`);
      console.log(`Risk Level: ${data.risk_level}`);
    } else {
      console.error(`Error: ${data.message}`);
    }
  })
  .catch(error => console.error('Request failed:', error));
```

---

#### 6.5.3.2 GET /health - Health Check

**Endpoint**: `/health`  
**Method**: `GET`  
**Authentication**: None

##### Response Schema (200 OK)

```json
{
  "status": "healthy",
  "timestamp": "2026-02-15T10:40:00.123Z",
  "version": "1.0.0",
  "uptime_seconds": 86400,
  "model_loaded": true,
  "model_version": "v1.0",
  "dependencies": {
    "database": "n/a",
    "external_apis": "n/a"
  }
}
```

##### Response Example (Degraded)

```json
{
  "status": "degraded",
  "timestamp": "2026-02-15T10:41:00.456Z",
  "version": "1.0.0",
  "uptime_seconds": 3600,
  "model_loaded": true,
  "model_version": "v1.0",
  "issues": [
    "High memory usage (85%)",
    "Average inference time above threshold"
  ]
}
```

---

#### 6.5.3.3 GET /metrics - Performance Metrics

**Endpoint**: `/metrics`  
**Method**: `GET`  
**Authentication**: Optional (admin only in production)

##### Response Schema (200 OK)

```json
{
  "timestamp": "2026-02-15T10:42:00.789Z",
  "requests": {
    "total": 125847,
    "success": 124532,
    "errors": 1315,
    "rate_limited": 245
  },
  "predictions": {
    "phishing": 3847,
    "legitimate": 120685
  },
  "performance": {
    "avg_inference_time_ms": 24.5,
    "p50_inference_time_ms": 22.0,
    "p95_inference_time_ms": 45.0,
    "p99_inference_time_ms": 78.0
  },
  "system": {
    "cpu_usage_percent": 15.2,
    "memory_usage_mb": 342,
    "uptime_seconds": 86400
  }
}
```

---

#### 6.5.3.4 POST /feedback - User Feedback

**Endpoint**: `/feedback`  
**Method**: `POST`  
**Content-Type**: `application/json`

##### Request Schema

```json
{
  "request_id": "string (required)",
  "feedback_type": "string (enum: 'false_positive', 'false_negative', 'correct')",
  "url": "string (required)",
  "user_comment": "string (optional)",
  "timestamp": "string (ISO 8601)"
}
```

##### Response Schema (200 OK)

```json
{
  "status": "success",
  "message": "Feedback received. Thank you for helping improve the system.",
  "feedback_id": "fb_9d8e7c6b5a4f"
}
```

---

### 6.5.4 Non-Functional Requirements

#### 6.5.4.1 Performance Requirements

| Req ID | Requirement | Target Metric | Priority | Measurement Method |
|--------|-------------|---------------|----------|-------------------|
| **NFR-B001** | API Response Time | <200ms (95th percentile) | Critical | Request duration logging |
| **NFR-B002** | Model Inference Time | <50ms per prediction | Critical | Inference timer |
| **NFR-B003** | Throughput | ≥100 requests/second | High | Load testing |
| **NFR-B004** | Cold Start Time | <5 seconds | Medium | Startup timer |
| **NFR-B005** | Model Load Time | <3 seconds | High | Startup profiling |
| **NFR-B006** | Feature Extraction Time | <20ms per URL | High | Feature extraction timer |
| **NFR-B007** | Memory Footprint | <512MB RAM | Medium | Process monitoring |
| **NFR-B008** | CPU Utilization | <50% under normal load | Medium | System monitoring |
| **NFR-B009** | Concurrent Connections | Support 1000+ simultaneous | Medium | Connection pooling |
| **NFR-B010** | Request Queue Depth | Handle 500+ queued requests | Low | Queue monitoring |

**Performance Benchmarks:**

| Scenario | Target Latency | Target Throughput | Acceptance |
|----------|---------------|-------------------|------------|
| Single request (idle) | <100ms | N/A | P95 < 200ms |
| Normal load (50 req/s) | <200ms | 50 req/s | P95 < 300ms |
| Peak load (100 req/s) | <500ms | 100 req/s | P95 < 800ms |
| Stress test (200 req/s) | <1000ms | Graceful degradation | No crashes |

**Optimization Strategies:**

```python
# 1. Model Preloading
class ModelManager:
    def __init__(self):
        self.model = None
        self.scaler = None
    
    async def load_models(self):
        """Load models during startup, not per request"""
        self.model = joblib.load('models/xgboost_v1.0.pkl')
        self.scaler = joblib.load('models/scaler_v1.0.joblib')

# 2. Async Operations
@app.post("/predict")
async def predict(request: URLPredictRequest):
    """Use async for I/O-bound operations"""
    features = await extract_features_async(request.url)
    prediction = await model_manager.predict(features)
    return format_response(prediction)

# 3. Feature Extraction Caching
from functools import lru_cache

@lru_cache(maxsize=1000)
def extract_domain_features(domain: str):
    """Cache domain feature extraction results"""
    return compute_domain_features(domain)

# 4. Connection Pooling
import httpx

http_client = httpx.AsyncClient(
    timeout=10.0,
    limits=httpx.Limits(max_connections=100)
)
```

---

#### 6.5.4.2 Security Requirements

| Req ID | Requirement | Implementation | Priority |
|--------|-------------|----------------|----------|
| **NFR-B011** | HTTPS Only | Enforce TLS 1.3, redirect HTTP to HTTPS | Critical |
| **NFR-B012** | Input Validation | Validate all inputs using Pydantic schemas | Critical |
| **NFR-B013** | Input Sanitization | Strip malicious characters, prevent injection | Critical |
| **NFR-B014** | Rate Limiting | 100 requests/minute per IP | High |
| **NFR-B015** | CORS Policy | Restrict origins to extension domain | High |
| **NFR-B016** | No PII Logging | Log URL hash (SHA-256), not full URL | Critical |
| **NFR-B017** | SQL Injection Prevention | Use parameterized queries (if DB added) | High |
| **NFR-B018** | XSS Prevention | Escape all user input in responses | High |
| **NFR-B019** | DDoS Protection | Implement request throttling and backoff | Medium |
| **NFR-B020** | Security Headers | Set CSP, X-Frame-Options, HSTS | Medium |
| **NFR-B021** | API Key Support | Optional API key authentication (future) | Low |
| **NFR-B022** | Secrets Management | Store secrets in environment variables | High |

**Security Implementation:**

```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import hashlib

app = FastAPI()

# Rate Limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "chrome-extension://your-extension-id",
        "https://your-frontend-domain.com"
    ],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Security Headers
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

# Privacy-Preserving Logging
def log_request(url: str):
    url_hash = hashlib.sha256(url.encode()).hexdigest()
    logger.info(f"URL Hash: {url_hash}")  # Log hash, not full URL

# Rate Limiting on Endpoint
@app.post("/predict")
@limiter.limit("100/minute")
async def predict(request: Request, url_request: URLPredictRequest):
    # Process request
    pass
```

---

#### 6.5.4.3 Reliability Requirements

| Req ID | Requirement | Target | Priority | Measurement |
|--------|-------------|--------|----------|-------------|
| **NFR-B023** | API Uptime | 99.5% availability | High | Uptime monitoring |
| **NFR-B024** | Error Rate | <1% of requests | High | Error tracking |
| **NFR-B025** | Mean Time Between Failures (MTBF) | >720 hours (30 days) | Medium | Incident tracking |
| **NFR-B026** | Mean Time To Recovery (MTTR) | <15 minutes | Medium | Incident response time |
| **NFR-B027** | Graceful Degradation | Function without external APIs | High | Fallback testing |
| **NFR-B028** | Data Integrity | 100% prediction accuracy in logging | High | Log validation |
| **NFR-B029** | Crash Recovery | Auto-restart on failure | High | Process manager config |
| **NFR-B030** | Model Fallback | Use backup model on primary failure | Medium | Failover testing |

**Reliability Implementation:**

```python
from fastapi import FastAPI, HTTPException
import logging
from typing import Optional

app = FastAPI()

# Comprehensive Error Handling
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "error_code": "INTERNAL_ERROR",
            "message": "An unexpected error occurred",
            "request_id": generate_request_id()
        }
    )

# Graceful Degradation
class PredictionService:
    def __init__(self):
        self.primary_model = None
        self.fallback_model = None
    
    async def predict(self, features):
        try:
            # Try primary model
            return await self._predict_with_model(self.primary_model, features)
        except Exception as e:
            logger.warning(f"Primary model failed: {e}. Using fallback.")
            try:
                # Fallback to secondary model
                return await self._predict_with_model(self.fallback_model, features)
            except Exception as e2:
                logger.error(f"Fallback model also failed: {e2}")
                # Return safe default (block)
                return {"prediction": "phishing", "confidence": 0.5, "fallback": True}

# Health Checks
@app.get("/health")
async def health_check():
    checks = {
        "model_loaded": model_manager.is_loaded(),
        "disk_space": check_disk_space(),
        "memory": check_memory_usage()
    }
    
    if all(checks.values()):
        return {"status": "healthy", **checks}
    else:
        return {"status": "degraded", **checks}
```

---

#### 6.5.4.4 Scalability Requirements

| Req ID | Requirement | Target | Priority | Approach |
|--------|-------------|--------|----------|----------|
| **NFR-B031** | Horizontal Scaling | Support 10+ instances | Medium | Stateless design |
| **NFR-B032** | Load Balancing | Distribute across instances | Medium | Load balancer (nginx/ALB) |
| **NFR-B033** | Database Scaling | N/A (stateless) | N/A | No database required |
| **NFR-B034** | Model Replication | Duplicate models across instances | Medium | Shared model storage |
| **NFR-B035** | Cache Scaling | Distributed cache (optional) | Low | Redis/Memcached |
| **NFR-B036** | Request Queueing | Queue overflow requests | Low | Message queue (RabbitMQ) |
| **NFR-B037** | Auto-Scaling | Scale based on CPU/requests | Low | Cloud auto-scaling |

**Scalability Architecture:**

```
┌─────────────────────────────────────────────────────────┐
│                    Load Balancer                        │
│                  (nginx / AWS ALB)                      │
└─────────────────────────────────────────────────────────┘
            │              │              │
            ▼              ▼              ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Backend     │  │  Backend     │  │  Backend     │
│  Instance 1  │  │  Instance 2  │  │  Instance N  │
│  (Uvicorn)   │  │  (Uvicorn)   │  │  (Uvicorn)   │
└──────────────┘  └──────────────┘  └──────────────┘
            │              │              │
            ▼              ▼              ▼
┌─────────────────────────────────────────────────────────┐
│              Shared Model Storage (S3/NFS)              │
└─────────────────────────────────────────────────────────┘
```

**Docker Compose for Multi-Instance:**

```yaml
version: '3.8'

services:
  backend-1:
    image: phishing-detector-api:latest
    ports:
      - "8001:8000"
    environment:
      - MODEL_PATH=/models/xgboost_v1.0.pkl
    volumes:
      - ./models:/models:ro
    restart: always

  backend-2:
    image: phishing-detector-api:latest
    ports:
      - "8002:8000"
    environment:
      - MODEL_PATH=/models/xgboost_v1.0.pkl
    volumes:
      - ./models:/models:ro
    restart: always

  load-balancer:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - backend-1
      - backend-2
```

---

#### 6.5.4.5 Maintainability Requirements

| Req ID | Requirement | Target | Priority |
|--------|-------------|--------|----------|
| **NFR-B038** | Code Documentation | 100% function docstrings | High |
| **NFR-B039** | Code Coverage | ≥80% test coverage | High |
| **NFR-B040** | Code Quality | Pass linting (Pylint score ≥8.0) | Medium |
| **NFR-B041** | API Documentation | Auto-generated OpenAPI docs | High |
| **NFR-B042** | Logging Standard | Structured JSON logs | High |
| **NFR-B043** | Configuration Management | Environment-based config | High |
| **NFR-B044** | Version Control | Git with semantic versioning | Critical |
| **NFR-B045** | Monitoring Hooks | Prometheus/CloudWatch metrics | Low |

**Code Quality Standards:**

```python
"""
URL Phishing Detection API
===========================

This module provides FastAPI endpoints for real-time phishing URL classification.

Author: [Your Name]
Version: 1.0.0
"""

from typing import Dict, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl, validator
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class URLPredictRequest(BaseModel):
    """
    Request model for URL classification.
    
    Attributes:
        url (HttpUrl): The URL to classify
        user_id (Optional[str]): Anonymous user identifier
        include_features (bool): Whether to include features in response
    """
    url: HttpUrl
    user_id: Optional[str] = "anonymous"
    include_features: bool = False
    
    @validator('url')
    def validate_url_length(cls, v):
        """
        Validate URL length does not exceed maximum.
        
        Args:
            v: URL string to validate
            
        Returns:
            Validated URL
            
        Raises:
            ValueError: If URL exceeds 2048 characters
        """
        if len(str(v)) > 2048:
            raise ValueError("URL exceeds maximum length of 2048 characters")
        return v


async def predict_url(url: str) -> Dict:
    """
    Classify a URL as phishing or legitimate.
    
    Args:
        url (str): URL to classify
        
    Returns:
        Dict: Prediction result with confidence score
        
    Raises:
        HTTPException: If prediction fails
        
    Example:
        >>> result = await predict_url("https://suspicious-site.tk")
        >>> print(result['prediction'])
        'phishing'
    """
    try:
        features = extract_features(url)
        prediction = model.predict(features)
        return format_prediction(prediction)
    except Exception as e:
        logger.error(f"Prediction failed for URL: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")
```

---

### 6.5.5 Deployment Considerations

#### 6.5.5.1 Development Environment

**Local Development Setup:**

```bash
# 1. Clone repository
git clone https://github.com/your-username/phishing-detector-api.git
cd phishing-detector-api

# 2. Create virtual environment
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Place trained models
mkdir models
cp /path/to/trained/xgboost_v1.0.pkl models/
cp /path/to/trained/scaler_v1.0.joblib models/

# 5. Run development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 6. Access API documentation
# Open browser: http://localhost:8000/docs
```

**requirements.txt:**

```
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
xgboost==2.0.3
scikit-learn==1.3.2
pandas==2.1.4
numpy==1.26.2
joblib==1.3.2
python-multipart==0.0.6
httpx==0.25.2
slowapi==0.1.9
python-dotenv==1.0.0
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
```

---

#### 6.5.5.2 Production Deployment

**Docker Deployment:**

**Dockerfile:**

```dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy trained models
COPY models/ /app/models/

# Expose port
EXPOSE 8000

# Set environment variables
ENV MODEL_PATH=/app/models/xgboost_v1.0.pkl
ENV SCALER_PATH=/app/models/scaler_v1.0.joblib
ENV LOG_LEVEL=INFO

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

**Build and Run:**

```bash
# Build Docker image
docker build -t phishing-detector-api:1.0 .

# Run container
docker run -d \
  --name phishing-api \
  -p 8000:8000 \
  -e MODEL_PATH=/app/models/xgboost_v1.0.pkl \
  -e LOG_LEVEL=INFO \
  --restart unless-stopped \
  phishing-detector-api:1.0

# Check logs
docker logs -f phishing-api

# Stop container
docker stop phishing-api
```

---

#### 6.5.5.3 Cloud Deployment Options

**Option 1: AWS EC2**

```bash
# 1. Launch EC2 instance (Ubuntu 22.04, t3.medium)
# 2. SSH into instance
ssh -i your-key.pem ubuntu@ec2-xx-xx-xx-xx.compute.amazonaws.com

# 3. Install Docker
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker

# 4. Clone and deploy
git clone https://github.com/your-repo/phishing-detector-api.git
cd phishing-detector-api
sudo docker-compose up -d

# 5. Configure nginx reverse proxy
sudo apt install nginx
sudo nano /etc/nginx/sites-available/phishing-api
```

**Nginx Configuration:**

```nginx
server {
    listen 80;
    server_name api.phishing-detector.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Option 2: AWS Elastic Beanstalk**

```bash
# 1. Install EB CLI
pip install awsebcli

# 2. Initialize EB application
eb init -p python-3.10 phishing-detector-api

# 3. Create environment
eb create phishing-api-prod --instance-type t3.medium

# 4. Deploy
eb deploy

# 5. Open application
eb open
```

**Option 3: Google Cloud Run (Serverless)**

```bash
# 1. Build and push to Container Registry
gcloud builds submit --tag gcr.io/your-project/phishing-api

# 2. Deploy to Cloud Run
gcloud run deploy phishing-api \
  --image gcr.io/your-project/phishing-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 2 \
  --max-instances 10
```

---

#### 6.5.5.4 Environment Configuration

**.env file:**

```ini
# Application Settings
APP_NAME=Phishing Detection API
APP_VERSION=1.0.0
DEBUG=false
LOG_LEVEL=INFO

# Server Settings
HOST=0.0.0.0
PORT=8000
WORKERS=4
RELOAD=false

# Model Configuration
MODEL_PATH=models/xgboost_v1.0.pkl
SCALER_PATH=models/scaler_v1.0.joblib
MODEL_VERSION=v1.0

# Security Settings
ALLOWED_ORIGINS=chrome-extension://your-extension-id,https://your-domain.com
RATE_LIMIT=100/minute
CORS_ENABLED=true

# Performance Settings
REQUEST_TIMEOUT=10
INFERENCE_TIMEOUT=5
MAX_WORKERS=4

# Monitoring (Optional)
SENTRY_DSN=https://your-sentry-dsn
PROMETHEUS_ENABLED=false
```

**Load Configuration:**

```python
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Application configuration settings"""
    
    # Application
    app_name: str = "Phishing Detection API"
    app_version: str = "1.0.0"
    debug: bool = False
    log_level: str = "INFO"
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    
    # Model
    model_path: str = "models/xgboost_v1.0.pkl"
    scaler_path: str = "models/scaler_v1.0.joblib"
    
    # Security
    allowed_origins: List[str] = ["*"]
    rate_limit: str = "100/minute"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

---

#### 6.5.5.5 Monitoring and Logging

**Structured Logging:**

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    """Format logs as JSON"""
    
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_data)

# Configure logger
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

**Prometheus Metrics (Optional):**

```python
from prometheus_client import Counter, Histogram, generate_latest

# Define metrics
request_count = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
request_duration = Histogram('http_request_duration_seconds', 'HTTP request duration')
prediction_count = Counter('predictions_total', 'Total predictions', ['prediction'])

@app.get("/metrics")
async def metrics():
    """Expose Prometheus metrics"""
    return Response(generate_latest(), media_type="text/plain")
```

---

## 6.5 Backend Requirements Specification

### 6.5.1 Backend Overview

The backend service is built using FastAPI, a modern, high-performance Python web framework optimized for building APIs with automatic validation, documentation, and async support. The backend serves as the intelligence layer of the phishing detection system, hosting the trained machine learning models and providing RESTful endpoints for URL classification.

#### Architecture Philosophy

**Stateless Design**: The backend operates as a stateless service, enabling horizontal scaling and simplified deployment. All user-specific data (whitelist, settings) is stored client-side in the browser extension.

**Microservice-Ready**: While deployed as a monolithic application for this academic project, the architecture is designed with clear separation of concerns to facilitate future microservice decomposition if needed.

**API-First Approach**: The backend exposes a well-defined REST API that can be consumed by various clients (browser extensions, mobile apps, third-party services) without modification.

#### Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Web Framework** | FastAPI | 0.104+ | High-performance async API framework |
| **ASGI Server** | Uvicorn | 0.24+ | Production-grade ASGI server |
| **Data Validation** | Pydantic | 2.5+ | Request/response validation and serialization |
| **ML Framework** | scikit-learn | 1.3+ | Model interface and preprocessing |
| **Gradient Boosting** | XGBoost | 2.0+ | Primary classification algorithm |
| **Numerical Computing** | NumPy | 1.26+ | Array operations and computations |
| **Data Processing** | Pandas | 2.1+ | Data manipulation (training phase) |
| **HTTP Client** | httpx | 0.25+ | Async HTTP requests for external APIs |
| **Testing** | Pytest | 7.4+ | Unit and integration testing |
| **Logging** | Python logging | stdlib | Structured logging |
| **Environment Management** | python-dotenv | 1.0+ | Configuration management |
| **Rate Limiting** | slowapi | 0.1.9+ | Request rate limiting |
| **CORS Handling** | FastAPI CORS | built-in | Cross-origin resource sharing |
| **Model Serialization** | joblib | 1.3+ | Efficient model persistence |

#### Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py               # Configuration settings
│   ├── models/
│   │   ├── __init__.py
│   │   ├── schemas.py          # Pydantic models for request/response
│   │   └── ml_model.py         # ML model wrapper class
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py           # API route definitions
│   │   └── dependencies.py     # Dependency injection
│   ├── core/
│   │   ├── __init__.py
│   │   ├── feature_extractor.py  # URL feature engineering
│   │   ├── model_manager.py      # Model loading and inference
│   │   └── exceptions.py         # Custom exception classes
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py       # Input validation utilities
│   │   └── logger.py           # Logging configuration
│   └── middleware/
│       ├── __init__.py
│       ├── rate_limiter.py     # Rate limiting middleware
│       └── error_handler.py    # Global error handling
├── models/
│   ├── xgboost_v1.0.pkl        # Trained XGBoost model
│   ├── scaler_v1.0.joblib      # Feature scaler
│   └── metadata.json           # Model metadata
├── tests/
│   ├── __init__.py
│   ├── test_api.py             # API endpoint tests
│   ├── test_features.py        # Feature extraction tests
│   └── test_model.py           # Model inference tests
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variable template
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Multi-container orchestration
└── README.md                   # Backend documentation
```

---

### 6.5.2 Functional Requirements

#### Core API Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-B01** | URL Classification Endpoint | Critical | Provide POST /predict endpoint that accepts URL and returns phishing classification | Endpoint returns 200 with valid JSON containing prediction and confidence |
| **FR-B02** | Request Validation | Critical | Validate incoming URL format and reject malformed requests | Invalid URLs return 400 with descriptive error message |
| **FR-B03** | Feature Extraction | Critical | Extract 30+ features from URL string for model input | Features extracted successfully for all valid URLs |
| **FR-B04** | Model Inference | Critical | Load ML model at startup and perform predictions on demand | Model loads successfully, predictions complete in <50ms |
| **FR-B05** | Confidence Scoring | Critical | Return confidence score (0-1) with each prediction | Confidence score reflects model probability, properly calibrated |
| **FR-B06** | Risk Categorization | High | Categorize URLs as high/medium/low risk based on confidence | Risk levels assigned according to defined thresholds |
| **FR-B07** | Health Check Endpoint | High | Provide GET /health for service monitoring | Returns 200 with service status and model loaded indicator |
| **FR-B08** | API Documentation | High | Auto-generate OpenAPI/Swagger documentation | Interactive docs available at /docs endpoint |
| **FR-B09** | CORS Configuration | High | Allow cross-origin requests from browser extension | CORS headers properly configured for extension origin |
| **FR-B10** | Rate Limiting | High | Limit requests to prevent abuse (100 req/min per IP) | Rate limiter returns 429 when threshold exceeded |
| **FR-B11** | Request Logging | Medium | Log all requests with timestamp, URL hash, and result | Structured logs written for monitoring and debugging |
| **FR-B12** | Error Response Standardization | Medium | Return consistent error format across all endpoints | All errors follow standard schema with error_code and message |
| **FR-B13** | Batch Prediction | Low | Support batch URL classification in single request | Accept array of URLs and return array of predictions |
| **FR-B14** | Model Versioning | Low | Support multiple model versions via query parameter | Endpoint accepts model_version parameter for A/B testing |
| **FR-B15** | Feedback Collection | Low | Provide POST /feedback for user-reported false positives | Feedback stored for model improvement analysis |

#### Feature Extraction Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-B16** | Lexical Feature Extraction | Critical | Extract character-based features (length, symbol counts, entropy) | All 15+ lexical features computed correctly |
| **FR-B17** | Host-Based Feature Extraction | Critical | Extract domain features (TLD, subdomain count, domain length) | Domain parsing handles edge cases correctly |
| **FR-B18** | URL Parsing | Critical | Parse URL into scheme, domain, path, query components | Parsing handles malformed URLs gracefully |
| **FR-B19** | Special Character Detection | High | Identify suspicious characters (%, @, IP addresses) | Special patterns detected with 100% accuracy |
| **FR-B20** | Feature Normalization | High | Scale features to model-compatible range | Features normalized using trained scaler |
| **FR-B21** | Missing Feature Handling | Medium | Handle URLs where certain features cannot be extracted | Default values used for missing features |
| **FR-B22** | Unicode Normalization | Medium | Normalize internationalized domain names (IDN) | Punycode conversion performed correctly |
| **FR-B23** | Feature Vector Caching | Low | Cache computed features for identical URLs | Cache reduces redundant computation |

#### Model Management Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-B24** | Model Loading at Startup | Critical | Load trained model into memory during application initialization | Model loaded successfully, startup time <10 seconds |
| **FR-B25** | Model Persistence | Critical | Load model from persistent storage (.pkl files) | Model deserialization handles file I/O errors |
| **FR-B26** | Prediction Pipeline | Critical | Apply feature scaling → model inference → post-processing | Pipeline produces consistent results |
| **FR-B27** | Model Validation | High | Verify model integrity on load (checksum, version) | Invalid models rejected with clear error |
| **FR-B28** | Graceful Model Failure | High | Handle model inference errors without crashing | Errors logged, 500 returned with generic message |
| **FR-B29** | Model Hot-Reload | Low | Support reloading model without server restart | Model reloaded via admin endpoint |
| **FR-B30** | Multiple Model Support | Low | Load and serve predictions from multiple model versions | Model routing based on version parameter |

---

### 6.5.3 API Specification

#### Endpoint: POST /predict

**Description**: Classify a URL as phishing or legitimate using the trained machine learning model.

**URL**: `/api/v1/predict`

**Method**: `POST`

**Authentication**: None (public endpoint with rate limiting)

**Rate Limit**: 100 requests per minute per IP address

---

#### Request Specification

**Headers**:
```http
Content-Type: application/json
Accept: application/json
User-Agent: PhishingDetector-Extension/1.0
```

**Request Body Schema**:

```json
{
  "url": "string (required, 1-2048 characters)",
  "user_id": "string (optional, for analytics)",
  "include_features": "boolean (optional, default: false)",
  "model_version": "string (optional, default: 'v1.0')"
}
```

**Field Descriptions**:

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `url` | string | Yes | Valid URL format, 1-2048 chars, HTTP/HTTPS only | The URL to classify |
| `user_id` | string | No | Max 64 chars | Anonymous user identifier for analytics (not PII) |
| `include_features` | boolean | No | Default: false | Return extracted features in response |
| `model_version` | string | No | Must match available version | Specify model version for A/B testing |

**Request Examples**:

**Example 1: Basic Request**
```json
{
  "url": "https://secure-login.paypal-verify.tk/signin"
}
```

**Example 2: Request with Optional Fields**
```json
{
  "url": "https://github.com/openai/gpt-3",
  "user_id": "anonymous_user_12345",
  "include_features": true,
  "model_version": "v1.0"
}
```

**Example 3: Suspicious URL**
```json
{
  "url": "http://bit.ly.account-verify.suspicious-domain.xyz/update?user=victim"
}
```

---

#### Response Specification

**Success Response (HTTP 200)**

**Response Schema**:
```json
{
  "status": "success",
  "data": {
    "url": "string",
    "prediction": "string (phishing|legitimate)",
    "confidence": "float (0.0-1.0)",
    "risk_level": "string (safe|low|medium|high)",
    "timestamp": "string (ISO 8601)",
    "model_version": "string",
    "features": "object (optional)"
  },
  "metadata": {
    "request_id": "string",
    "processing_time_ms": "integer"
  }
}
```

**Field Descriptions**:

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Always "success" for 200 responses |
| `data.url` | string | The URL that was classified (may be normalized) |
| `data.prediction` | string | Classification result: "phishing" or "legitimate" |
| `data.confidence` | float | Model confidence score between 0.0 and 1.0 |
| `data.risk_level` | string | Risk categorization: "safe", "low", "medium", or "high" |
| `data.timestamp` | string | ISO 8601 timestamp of prediction |
| `data.model_version` | string | Version of model used for prediction |
| `data.features` | object | Feature vector (only if include_features=true) |
| `metadata.request_id` | string | Unique identifier for this request |
| `metadata.processing_time_ms` | integer | Server-side processing time in milliseconds |

**Risk Level Thresholds**:
- **safe**: prediction = "legitimate" (confidence < 0.60 for phishing class)
- **low**: prediction = "phishing" AND confidence 0.60-0.69
- **medium**: prediction = "phishing" AND confidence 0.70-0.79
- **high**: prediction = "phishing" AND confidence ≥ 0.80

**Response Examples**:

**Example 1: Legitimate URL Detected**
```json
{
  "status": "success",
  "data": {
    "url": "https://github.com/openai/gpt-3",
    "prediction": "legitimate",
    "confidence": 0.05,
    "risk_level": "safe",
    "timestamp": "2026-02-15T14:23:45.123Z",
    "model_version": "v1.0"
  },
  "metadata": {
    "request_id": "req_8f3a4b2c9d1e",
    "processing_time_ms": 87
  }
}
```

**Example 2: Phishing URL Detected (High Risk)**
```json
{
  "status": "success",
  "data": {
    "url": "https://secure-login.paypal-verify.tk/signin",
    "prediction": "phishing",
    "confidence": 0.94,
    "risk_level": "high",
    "timestamp": "2026-02-15T14:24:12.456Z",
    "model_version": "v1.0"
  },
  "metadata": {
    "request_id": "req_7e2d5a1f8c3b",
    "processing_time_ms": 92
  }
}
```

**Example 3: With Feature Vector**
```json
{
  "status": "success",
  "data": {
    "url": "http://account-verify.suspicious.xyz/login",
    "prediction": "phishing",
    "confidence": 0.87,
    "risk_level": "high",
    "timestamp": "2026-02-15T14:25:33.789Z",
    "model_version": "v1.0",
    "features": {
      "url_length": 48,
      "num_dots": 3,
      "num_hyphens": 2,
      "num_subdomains": 2,
      "domain_length": 27,
      "has_ip_address": 0,
      "is_https": 0,
      "suspicious_tld": 1,
      "url_entropy": 4.12,
      "digit_letter_ratio": 0.0,
      "vowel_consonant_ratio": 0.58,
      "path_length": 6,
      "longest_subdomain": 15
      // ... 20+ more features
    }
  },
  "metadata": {
    "request_id": "req_9a4c7b2e5d1f",
    "processing_time_ms": 94
  }
}
```

**Example 4: Medium Risk (Suspicious but Lower Confidence)**
```json
{
  "status": "success",
  "data": {
    "url": "https://login-secure.example-bank.com/verify",
    "prediction": "phishing",
    "confidence": 0.72,
    "risk_level": "medium",
    "timestamp": "2026-02-15T14:26:01.234Z",
    "model_version": "v1.0"
  },
  "metadata": {
    "request_id": "req_3f7a9c1b8e2d",
    "processing_time_ms": 89
  }
}
```

---

#### Error Response Specification

All error responses follow a consistent schema for easier client-side handling.

**Error Response Schema**:
```json
{
  "status": "error",
  "error": {
    "code": "string (ERROR_CODE_CONSTANT)",
    "message": "string (human-readable error description)",
    "details": "string or object (optional, additional context)",
    "timestamp": "string (ISO 8601)"
  },
  "metadata": {
    "request_id": "string"
  }
}
```

---

#### Error Codes and Responses

**1. HTTP 400 - Bad Request**

**Scenario**: Invalid URL format

```json
{
  "status": "error",
  "error": {
    "code": "INVALID_URL_FORMAT",
    "message": "The provided URL is not valid",
    "details": "URL must include a valid scheme (http or https) and domain",
    "timestamp": "2026-02-15T14:30:00.123Z"
  },
  "metadata": {
    "request_id": "req_1a2b3c4d5e6f"
  }
}
```

**Scenario**: Missing required field

```json
{
  "status": "error",
  "error": {
    "code": "MISSING_REQUIRED_FIELD",
    "message": "Required field 'url' is missing from request body",
    "details": {
      "field": "url",
      "type": "string",
      "required": true
    },
    "timestamp": "2026-02-15T14:30:15.456Z"
  },
  "metadata": {
    "request_id": "req_2b3c4d5e6f7g"
  }
}
```

**Scenario**: URL too long

```json
{
  "status": "error",
  "error": {
    "code": "URL_TOO_LONG",
    "message": "URL exceeds maximum allowed length",
    "details": "Maximum URL length is 2048 characters, received 3521",
    "timestamp": "2026-02-15T14:31:22.789Z"
  },
  "metadata": {
    "request_id": "req_3c4d5e6f7g8h"
  }
}
```

**Scenario**: Unsupported URL scheme

```json
{
  "status": "error",
  "error": {
    "code": "UNSUPPORTED_SCHEME",
    "message": "URL scheme not supported",
    "details": "Only HTTP and HTTPS schemes are supported. Received: ftp",
    "timestamp": "2026-02-15T14:32:45.012Z"
  },
  "metadata": {
    "request_id": "req_4d5e6f7g8h9i"
  }
}
```

---

**2. HTTP 422 - Unprocessable Entity**

**Scenario**: Pydantic validation error

```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "loc": ["body", "url"],
        "msg": "invalid or missing URL scheme",
        "type": "value_error.url.scheme"
      }
    ],
    "timestamp": "2026-02-15T14:33:10.345Z"
  },
  "metadata": {
    "request_id": "req_5e6f7g8h9i0j"
  }
}
```

---

**3. HTTP 429 - Too Many Requests**

**Scenario**: Rate limit exceeded

```json
{
  "status": "error",
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Please try again later",
    "details": "Rate limit: 100 requests per minute. Retry after 45 seconds",
    "timestamp": "2026-02-15T14:34:00.678Z"
  },
  "metadata": {
    "request_id": "req_6f7g8h9i0j1k",
    "retry_after": 45,
    "limit": 100,
    "window": "1 minute"
  }
}
```

---

**4. HTTP 500 - Internal Server Error**

**Scenario**: Model inference failure

```json
{
  "status": "error",
  "error": {
    "code": "MODEL_INFERENCE_ERROR",
    "message": "An error occurred during URL classification",
    "details": "The model encountered an unexpected error. Please try again",
    "timestamp": "2026-02-15T14:35:22.901Z"
  },
  "metadata": {
    "request_id": "req_7g8h9i0j1k2l"
  }
}
```

**Scenario**: Feature extraction failure

```json
{
  "status": "error",
  "error": {
    "code": "FEATURE_EXTRACTION_ERROR",
    "message": "Failed to extract features from URL",
    "details": "Unable to parse URL structure for feature computation",
    "timestamp": "2026-02-15T14:36:45.234Z"
  },
  "metadata": {
    "request_id": "req_8h9i0j1k2l3m"
  }
}
```

**Scenario**: Generic server error

```json
{
  "status": "error",
  "error": {
    "code": "INTERNAL_SERVER_ERROR",
    "message": "An unexpected error occurred",
    "details": "The server encountered an internal error. Our team has been notified",
    "timestamp": "2026-02-15T14:37:30.567Z"
  },
  "metadata": {
    "request_id": "req_9i0j1k2l3m4n"
  }
}
```

---

**5. HTTP 503 - Service Unavailable**

**Scenario**: Model not loaded

```json
{
  "status": "error",
  "error": {
    "code": "SERVICE_UNAVAILABLE",
    "message": "Service is temporarily unavailable",
    "details": "ML model is not loaded. Please wait for service initialization",
    "timestamp": "2026-02-15T14:38:15.890Z"
  },
  "metadata": {
    "request_id": "req_0j1k2l3m4n5o",
    "retry_after": 10
  }
}
```

---

#### Additional Endpoints

**Endpoint: GET /health**

**Description**: Health check endpoint for monitoring service status

**Response (HTTP 200)**:
```json
{
  "status": "healthy",
  "service": "phishing-detection-api",
  "version": "1.0.0",
  "model_loaded": true,
  "model_version": "v1.0",
  "uptime_seconds": 86400,
  "timestamp": "2026-02-15T14:40:00.123Z"
}
```

**Response (HTTP 503)** - When model not loaded:
```json
{
  "status": "unhealthy",
  "service": "phishing-detection-api",
  "version": "1.0.0",
  "model_loaded": false,
  "error": "Model not initialized",
  "timestamp": "2026-02-15T14:40:30.456Z"
}
```

---

**Endpoint: POST /feedback**

**Description**: Collect user feedback on false positives/negatives

**Request**:
```json
{
  "url": "https://example.com",
  "prediction": "phishing",
  "confidence": 0.85,
  "user_feedback": "false_positive",
  "user_comment": "This is a legitimate site I use daily",
  "request_id": "req_abc123"
}
```

**Response (HTTP 200)**:
```json
{
  "status": "success",
  "message": "Feedback recorded. Thank you for helping improve our model",
  "feedback_id": "fb_xyz789",
  "timestamp": "2026-02-15T14:42:00.789Z"
}
```

---

### 6.5.4 Non-Functional Requirements

#### Performance Requirements

| ID | Requirement | Target Metric | Priority | Measurement Method |
|----|-------------|---------------|----------|-------------------|
| **NFR-B01** | API Response Time | <200ms (p95) | Critical | Prometheus metrics, request timing |
| **NFR-B02** | Model Inference Latency | <50ms per prediction | Critical | Internal timing instrumentation |
| **NFR-B03** | Feature Extraction Time | <30ms per URL | High | Profiling with cProfile |
| **NFR-B04** | Concurrent Request Handling | 100+ simultaneous requests | High | Load testing with Locust/JMeter |
| **NFR-B05** | Request Throughput | 50 requests/second sustained | Medium | Load testing over 1-hour duration |
| **NFR-B06** | Cold Start Time | <10 seconds | Medium | Application startup measurement |
| **NFR-B07** | Memory Usage | <512MB RAM under load | Medium | Memory profiling, Docker stats |
| **NFR-B08** | CPU Utilization | <50% under typical load | Low | System monitoring (htop, Docker stats) |
| **NFR-B09** | Model Loading Time | <5 seconds | Low | Startup logs timing |
| **NFR-B10** | Database Query Time | <20ms (if database added) | Low | Query profiling |

**Performance Benchmarking Strategy**:
```python
# Example performance test
import time
import statistics

def benchmark_endpoint(url, num_requests=100):
    latencies = []
    for _ in range(num_requests):
        start = time.time()
        response = requests.post(API_URL, json={"url": url})
        latency = (time.time() - start) * 1000  # ms
        latencies.append(latency)
    
    return {
        "mean": statistics.mean(latencies),
        "median": statistics.median(latencies),
        "p95": statistics.quantiles(latencies, n=20)[18],  # 95th percentile
        "p99": statistics.quantiles(latencies, n=100)[98],
        "min": min(latencies),
        "max": max(latencies)
    }
```

---

#### Security Requirements

| ID | Requirement | Implementation | Priority | Verification Method |
|----|-------------|----------------|----------|---------------------|
| **NFR-B11** | HTTPS Encryption | TLS 1.3 for all API traffic | Critical | SSL Labs scan, certificate verification |
| **NFR-B12** | Input Sanitization | Validate and sanitize all inputs | Critical | Security testing, fuzzing |
| **NFR-B13** | No PII Collection | Avoid logging full URLs or user data | Critical | Code review, log inspection |
| **NFR-B14** | SQL Injection Prevention | Use parameterized queries (if DB used) | Critical | OWASP ZAP scanning |
| **NFR-B15** | XSS Prevention | Escape output, set CSP headers | High | Penetration testing |
| **NFR-B16** | CORS Configuration | Whitelist extension origins only | High | Browser DevTools verification |
| **NFR-B17** | Rate Limiting | IP-based throttling | High | Load testing with rate limit bypass attempts |
| **NFR-B18** | Authentication (Future) | JWT or API key authentication | Medium | N/A (not implemented in v1.0) |
| **NFR-B19** | Secrets Management | Use environment variables for secrets | Medium | Code review |
| **NFR-B20** | Dependency Scanning | Regular security audits of packages | Medium | pip-audit, safety check |
| **NFR-B21** | DoS Protection | Request size limits, timeout configs | Medium | Stress testing |
| **NFR-B22** | Error Message Security | No stack traces in production errors | Low | Manual testing |

**Security Headers**:
```python
# Example FastAPI security headers middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://extension-id-here"],
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)

# Additional security headers
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000"
    return response
```

---

#### Reliability Requirements

| ID | Requirement | Target | Priority | Implementation |
|----|-------------|--------|----------|----------------|
| **NFR-B23** | API Uptime | 99.5% availability | High | Health checks, auto-restart on failure |
| **NFR-B24** | Graceful Error Handling | No unhandled exceptions | Critical | Try-catch blocks, global exception handler |
| **NFR-B25** | Model Fallback | Use cached results if model fails | Medium | Implement fallback mechanism |
| **NFR-B26** | Request Retry Logic | Client-side exponential backoff | Medium | Extension implementation |
| **NFR-B27** | Logging Reliability | All errors logged with context | High | Structured logging to file/stdout |
| **NFR-B28** | Graceful Degradation | Partial functionality on subsystem failure | Medium | Circuit breaker pattern |
| **NFR-B29** | Data Validation | Reject invalid inputs early | Critical | Pydantic validators |
| **NFR-B30** | Timeout Configuration | Set timeouts for all operations | High | FastAPI timeout middleware |

**Error Handling Example**:
```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for unhandled errors"""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "An unexpected error occurred",
                "details": "Please contact support with request ID",
                "timestamp": datetime.utcnow().isoformat() + "Z"
            },
            "metadata": {
                "request_id": generate_request_id()
            }
        }
    )
```

---

#### Scalability Requirements

| ID | Requirement | Target | Priority | Implementation Strategy |
|----|-------------|--------|----------|------------------------|
| **NFR-B31** | Horizontal Scalability | Support multiple instances behind load balancer | Medium | Stateless design, session-free |
| **NFR-B32** | Stateless Architecture | No server-side session state | High | Store all state client-side |
| **NFR-B33** | Model Replication | Each instance loads its own model | Medium | File-based model distribution |
| **NFR-B34** | Connection Pooling | Efficient resource management | Low | Uvicorn worker configuration |
| **NFR-B35** | Asynchronous Processing | Non-blocking I/O for API calls | High | FastAPI async/await |
| **NFR-B36** | Caching Strategy | Cache frequent URL classifications | Low | Redis cache (future enhancement) |
| **NFR-B37** | Database Scaling | Use connection pooling if DB added | Low | SQLAlchemy pooling |
| **NFR-B38** | Auto-scaling | Scale instances based on load | Low | Kubernetes HPA (future) |

**Deployment Scaling Architecture**:
```
                    ┌─────────────────┐
                    │  Load Balancer  │
                    │   (NGINX/ALB)   │
                    └────────┬────────┘
                             │
             ┌───────────────┼───────────────┐
             ▼               ▼               ▼
    ┌────────────┐  ┌────────────┐  ┌────────────┐
    │  Backend   │  │  Backend   │  │  Backend   │
    │ Instance 1 │  │ Instance 2 │  │ Instance N │
    └────────────┘  └────────────┘  └────────────┘
         │               │               │
         └───────────────┴───────────────┘
                         │
                    ┌────▼────┐
                    │ Shared  │
                    │ Storage │
                    │ (Model) │
                    └─────────┘
```

---

#### Maintainability Requirements

| ID | Requirement | Standard | Priority | Verification |
|----|-------------|----------|----------|--------------|
| **NFR-B39** | Code Documentation | Docstrings for all functions/classes | High | Code review, documentation coverage |
| **NFR-B40** | API Documentation | Auto-generated Swagger/OpenAPI docs | High | /docs endpoint functional |
| **NFR-B41** | Code Style | Follow PEP 8 guidelines | Medium | Linting with flake8/black |
| **NFR-B42** | Type Hints | Use Python type annotations | Medium | mypy static type checking |
| **NFR-B43** | Unit Test Coverage | ≥80% code coverage | Medium | pytest-cov measurement |
| **NFR-B44** | Logging Standards | Structured JSON logging | Medium | Log format validation |
| **NFR-B45** | Configuration Management | Environment-based config | High | .env file usage |
| **NFR-B46** | Version Control | Git with meaningful commit messages | Critical | Repository inspection |
| **NFR-B47** | Dependency Management | requirements.txt with pinned versions | High | File review |
| **NFR-B48** | README Documentation | Comprehensive setup instructions | Medium | Documentation completeness |

**Code Quality Standards**:
```python
# Example well-documented function
from typing import Dict, List, Optional
import numpy as np

def extract_url_features(
    url: str,
    include_optional: bool = False
) -> Dict[str, float]:
    """
    Extract numerical features from a URL string for ML model input.
    
    This function parses the URL and computes lexical, host-based, and
    statistical features used by the phishing detection model.
    
    Args:
        url: The URL string to analyze (must be valid HTTP/HTTPS URL)
        include_optional: Whether to include computationally expensive
            features like WHOIS lookup (default: False)
    
    Returns:
        Dictionary mapping feature names to numerical values. Returns
        30+ features including url_length, num_dots, entropy, etc.
    
    Raises:
        ValueError: If URL format is invalid
        URLParsingError: If URL cannot be parsed into components
    
    Example:
        >>> features = extract_url_features("https://example.com/path")
        >>> features['url_length']
        26
        >>> features['num_dots']
        1
    
    Note:
        Features are not normalized. Use the trained scaler before
        passing to the model.
    """
    # Implementation...
```

---

### 6.5.5 Deployment Considerations

#### Development Environment Setup

**Prerequisites**:
- Python 3.10 or higher
- pip package manager
- Virtual environment (venv or conda)
- Git for version control

**Installation Steps**:

```bash
# 1. Clone repository
git clone https://github.com/your-repo/phishing-detection-backend.git
cd phishing-detection-backend

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# 5. Download or train ML model
python scripts/train_model.py  # Or download pre-trained model
mv model.pkl models/xgboost_v1.0.pkl

# 6. Run development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Environment Variables** (`.env` file):
```bash
# Application Settings
APP_NAME=PhishingDetectionAPI
APP_VERSION=1.0.0
DEBUG_MODE=True
LOG_LEVEL=INFO

# Server Configuration
HOST=0.0.0.0
PORT=8000
WORKERS=4
RELOAD=True

# Model Configuration
MODEL_PATH=models/xgboost_v1.0.pkl
SCALER_PATH=models/scaler_v1.0.joblib
MODEL_VERSION=v1.0

# Rate Limiting
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=60  # seconds

# CORS Configuration
CORS_ORIGINS=["chrome-extension://your-extension-id"]

# Security
SECRET_KEY=your-secret-key-here
API_KEY_ENABLED=False

# Logging
LOG_FILE=logs/app.log
LOG_MAX_SIZE=10485760  # 10MB
LOG_BACKUP_COUNT=5
```

---

#### Local Testing Environment

**Running Tests**:
```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/test_api.py -v

# Run with timing information
pytest tests/ --durations=10
```

**Manual API Testing with cURL**:
```bash
# Test /predict endpoint
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "https://suspicious-site.tk/login"}'

# Test /health endpoint
curl http://localhost:8000/health

# Test with verbose output
curl -v -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com", "include_features": true}'
```

---

#### Production Deployment Options

**Option 1: Docker Containerization (Recommended)**

**Dockerfile**:
```dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ app/
COPY models/ models/

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

**docker-compose.yml** (for local multi-container setup):
```yaml
version: '3.8'

services:
  api:
    build: .
    container_name: phishing-api
    ports:
      - "8000:8000"
    environment:
      - DEBUG_MODE=False
      - LOG_LEVEL=INFO
      - WORKERS=4
    volumes:
      - ./models:/app/models:ro
      - ./logs:/app/logs
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 10s

  # Optional: Add Redis for caching
  redis:
    image: redis:7-alpine
    container_name: phishing-cache
    ports:
      - "6379:6379"
    restart: unless-stopped
```

**Build and Run**:
```bash
# Build Docker image
docker build -t phishing-detection-api:v1.0 .

# Run container
docker run -d \
  --name phishing-api \
  -p 8000:8000 \
  -v $(pwd)/models:/app/models:ro \
  phishing-detection-api:v1.0

# Or use docker-compose
docker-compose up -d
```

---

**Option 2: Cloud Platform Deployment**

**AWS Elastic Beanstalk**:
```yaml
# .ebextensions/01_app.config
option_settings:
  aws:elasticbeanstalk:application:environment:
    PYTHONPATH: "/var/app/current:$PYTHONPATH"
  aws:elasticbeanstalk:container:python:
    WSGIPath: app.main:app
  aws:autoscaling:launchconfiguration:
    InstanceType: t3.small
    RootVolumeSize: 20
```

**Google Cloud Run** (serverless):
```bash
# Deploy to Cloud Run
gcloud run deploy phishing-api \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1
```

**Heroku**:
```bash
# Procfile
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT

# Deploy
heroku create phishing-detection-api
git push heroku main
```

---

#### Monitoring and Observability

**Logging Configuration**:
```python
# app/utils/logger.py
import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("phishing-api")
    logger.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    
    # JSON formatter for structured logging
    formatter = logging.Formatter(
        '{"timestamp": "%(asctime)s", "level": "%(levelname)s", '
        '"logger": "%(name)s", "message": "%(message)s"}'
    )
    
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger
```

**Health Monitoring**:
- Implement `/health` endpoint for liveness probes
- Use `/metrics` endpoint for Prometheus metrics (optional)
- Set up alerting for error rates, latency spikes
- Monitor resource usage (CPU, memory, disk)

---

#### CI/CD Pipeline

**GitHub Actions Workflow** (`.github/workflows/ci.yml`):
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      
      - name: Run tests
        run: pytest tests/ --cov=app --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
  
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Lint with flake8
        run: |
          pip install flake8
          flake8 app/ --max-line-length=100
  
  deploy:
    needs: [test, lint]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to production
        run: |
          # Add deployment script here
          echo "Deploying to production..."
```

---

#### Backup and Recovery

**Model Versioning**:
- Store multiple model versions with timestamps
- Maintain model metadata (accuracy, training date)
- Implement rollback mechanism for model updates

**Data Backup**:
- Regular backups of feedback data (if stored)
- Configuration backups
- Log archival and retention policy

---

#### Performance Optimization

**Caching Strategies**:
```python
# Example: In-memory LRU cache for predictions
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_cached_prediction(url_hash: str):
    """Cache recent predictions to reduce redundant computations"""
    # This would be implemented in the actual service
    pass
```

**Load Balancing**:
- Use NGINX or HAProxy for multiple backend instances
- Implement round-robin or least-connections algorithm
- Health checks for automatic failover

**Database Optimization** (if database added):
- Index frequently queried fields
- Use connection pooling
- Implement read replicas for scalability

### 6.6 System Overview

The ML-Based Phishing URL Detection System is designed as a modular, scalable architecture that separates concerns across distinct operational layers. The system follows a client-server model where the browser extension acts as a lightweight client, performing minimal processing while delegating complex machine learning inference to a centralized backend service.

#### 6.6.1 Operational Flow

The system operates through the following sequential workflow:

1. **URL Capture**: When a user attempts to navigate to a URL, the Chrome extension intercepts the navigation event before the page loads
2. **Preprocessing**: The extension performs basic URL normalization and checks local cache for recent classifications
3. **API Request**: If not cached, the extension sends an HTTPS POST request to the FastAPI backend containing the URL
4. **Feature Extraction**: The backend parses the URL and extracts 30+ features including lexical, structural, and host-based characteristics
5. **ML Inference**: The extracted features are passed to the trained machine learning model (XGBoost/Random Forest) for classification
6. **Confidence Scoring**: The model returns a prediction (phishing/legitimate) with an associated confidence score (0-100%)
7. **Response Formatting**: The API packages the prediction, confidence, risk level, and metadata into a JSON response
8. **Client-Side Decision**: The extension interprets the response and determines the appropriate user intervention
9. **User Notification**: Based on risk level, the system either blocks access, displays a warning, or allows seamless navigation
10. **Feedback Loop**: User actions (proceed/block/report) are optionally logged for model improvement

#### 6.6.2 Design Principles

The architecture adheres to the following design principles:

- **Separation of Concerns**: Clear boundaries between presentation (extension), business logic (API), and ML inference (model layer)
- **Statelessness**: API endpoints are stateless, enabling horizontal scalability
- **Privacy-by-Design**: Minimal data collection with no user tracking or PII storage
- **Performance Optimization**: Caching, async operations, and efficient feature extraction minimize latency
- **Graceful Degradation**: System functions in reduced capacity if backend is unavailable
- **Modularity**: Components can be independently updated, tested, and deployed
- **Security-First**: All communications encrypted, input validation at every layer

#### 6.6.3 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                          USER INTERACTION                           │
│                    (Clicks link / Enters URL)                       │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      CHROME BROWSER LAYER                           │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  Navigation Event Triggered                                   │  │
│  │  • webNavigation.onBeforeNavigate                             │  │
│  │  • webRequest.onBeforeRequest                                 │  │
│  └───────────────────────────┬───────────────────────────────────┘  │
└────────────────────────────────┼────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   CHROME EXTENSION (Frontend)                       │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  STEP 1: URL Extraction & Normalization                      │  │
│  │  • Parse URL from navigation event                            │  │
│  │  • Remove fragments, normalize encoding                       │  │
│  │  • Extract domain, protocol, path                             │  │
│  └───────────────────────────┬───────────────────────────────────┘  │
│                               │                                      │
│  ┌───────────────────────────▼───────────────────────────────────┐  │
│  │  STEP 2: Local Cache Check                                    │  │
│  │  • Query chrome.storage.local                                 │  │
│  │  • Key: hashed URL, Value: {classification, timestamp}        │  │
│  │  • Cache TTL: 24 hours                                        │  │
│  └───────────────────────────┬───────────────────────────────────┘  │
│                               │                                      │
│                    ┌──────────┴───────────┐                          │
│                    │                      │                          │
│              Cache Hit?              Cache Miss?                     │
│                    │                      │                          │
│        ┌───────────▼──────────┐   ┌──────▼──────────────┐           │
│        │  Use Cached Result   │   │  Prepare API Request│           │
│        └───────────┬──────────┘   └──────┬──────────────┘           │
│                    │                      │                          │
│                    │              ┌───────▼───────────────────────┐  │
│                    │              │ STEP 3: HTTP Request          │  │
│                    │              │ POST /predict                 │  │
│                    │              │ Headers: Content-Type, API-Key│  │
│                    │              │ Body: {"url": "..."}          │  │
│                    │              └───────┬───────────────────────┘  │
└────────────────────┼──────────────────────┼──────────────────────────┘
                     │                      │
                     │                      │ HTTPS (TLS 1.3)
                     │                      ▼
                     │      ┌─────────────────────────────────────────┐
                     │      │      NETWORK LAYER (Internet)           │
                     │      │  • Encrypted communication              │
                     │      │  • DNS resolution                       │
                     │      │  • Load balancing (if deployed)         │
                     │      └─────────────┬───────────────────────────┘
                     │                    │
                     │                    ▼
                     │      ┌─────────────────────────────────────────┐
                     │      │      FASTAPI BACKEND SERVER             │
                     │      │  ┌────────────────────────────────────┐ │
                     │      │  │  STEP 4: Request Handling          │ │
                     │      │  │  • Validate request format         │ │
                     │      │  │  • Rate limiting check             │ │
                     │      │  │  • Authentication (if enabled)     │ │
                     │      │  │  • Logging & monitoring            │ │
                     │      │  └────────────┬───────────────────────┘ │
                     │      │               │                          │
                     │      │  ┌────────────▼───────────────────────┐ │
                     │      │  │  STEP 5: Feature Extraction        │ │
                     │      │  │  • Parse URL structure             │ │
                     │      │  │  • Compute lexical features        │ │
                     │      │  │  • Extract host-based features     │ │
                     │      │  │  • Generate feature vector         │ │
                     │      │  │  Output: X = [f1, f2, ..., f30]    │ │
                     │      │  └────────────┬───────────────────────┘ │
                     │      │               │                          │
                     │      │  ┌────────────▼───────────────────────┐ │
                     │      │  │  STEP 6: ML Model Inference        │ │
                     │      │  │  • Load model from memory          │ │
                     │      │  │  • model.predict(X)                │ │
                     │      │  │  • model.predict_proba(X)          │ │
                     │      │  │  Output: class, probability        │ │
                     │      │  └────────────┬───────────────────────┘ │
                     │      │               │                          │
                     │      │  ┌────────────▼───────────────────────┐ │
                     │      │  │  STEP 7: Post-Processing           │ │
                     │      │  │  • Map class to label              │ │
                     │      │  │  • Calculate confidence score      │ │
                     │      │  │  • Determine risk level            │ │
                     │      │  │  • Format JSON response            │ │
                     │      │  └────────────┬───────────────────────┘ │
                     │      └────────────────┼────────────────────────┘
                     │                       │
                     │                       │ HTTP 200 Response
                     │      ┌────────────────▼────────────────────────┐
                     │      │  Response: {                            │
                     │      │    "prediction": "phishing",            │
                     │      │    "confidence": 0.89,                  │
                     │      │    "risk_level": "high"                 │
                     │      │  }                                      │
                     │      └────────────────┬────────────────────────┘
                     │                       │
┌────────────────────┼───────────────────────┼──────────────────────────┐
│                    │                       │                          │
│  ┌─────────────────▼───────────────────────▼────────────────────────┐│
│  │  STEP 8: Response Processing & Decision Logic                    ││
│  │  • Parse API response                                             ││
│  │  • Update local cache                                             ││
│  │  • Apply decision rules:                                          ││
│  │    - confidence > 80% → Block page                                ││
│  │    - confidence 60-80% → Show warning banner                      ││
│  │    - confidence < 60% → Allow with silent logging                 ││
│  └───────────────────────────┬───────────────────────────────────────┘│
│                               │                                        │
│  ┌────────────────────────────▼──────────────────────────────────────┐│
│  │  STEP 9: User Interface Rendering                                 ││
│  │  High Risk: Display blocking page with warning                    ││
│  │  Medium Risk: Inject warning banner at page top                   ││
│  │  Low Risk: Allow navigation, log silently                         ││
│  └───────────────────────────┬───────────────────────────────────────┘│
└────────────────────────────────┼────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          USER NOTIFICATION                          │
│  • Blocking page: "Phishing Threat Detected"                        │
│  • Warning banner: "This site may be suspicious"                    │
│  • Seamless navigation: (No interruption)                           │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      USER DECISION                                  │
│  • Go back to safety                                                │
│  • Proceed anyway (with consent)                                    │
│  • Add to whitelist                                                 │
│  • Report false positive                                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 6.7 Component Breakdown

This section provides an in-depth analysis of each system component, detailing their responsibilities, interfaces, and interdependencies.

### 6.7.1 Machine Learning Layer

The Machine Learning Layer is the core intelligence component responsible for distinguishing phishing URLs from legitimate ones through supervised learning techniques.

#### 6.7.1.1 Responsibilities

1. **Feature Engineering**
   - Extract meaningful patterns from raw URL strings
   - Transform unstructured URL data into structured numerical features
   - Implement domain-specific feature extraction logic
   - Handle missing or malformed URL components

2. **Model Training**
   - Train classification models on labeled phishing/legitimate datasets
   - Perform hyperparameter optimization for model tuning
   - Implement cross-validation for robust performance estimation
   - Handle class imbalance through sampling or weighting techniques

3. **Model Evaluation**
   - Compute standard classification metrics (accuracy, precision, recall, F1)
   - Generate confusion matrices and ROC curves
   - Perform error analysis on misclassified samples
   - Validate model generalization on holdout test sets

4. **Model Serialization**
   - Save trained models in production-ready formats
   - Version control for model artifacts
   - Compress models for efficient storage and loading
   - Document model metadata (features, performance, training date)

5. **Inference**
   - Load pre-trained models efficiently at runtime
   - Process feature vectors and generate predictions
   - Compute prediction confidence scores
   - Optimize inference speed for real-time requirements

#### 6.7.1.2 Inputs

| Input Type | Source | Format | Description |
|------------|--------|--------|-------------|
| Training Data | PhishTank, OpenPhish, Alexa | CSV/JSON | Labeled URL dataset with binary labels |
| URL String | Backend API | String | Raw URL to be classified |
| Feature Vector | Feature Extractor | NumPy Array | Numerical representation of URL (shape: [1, n_features]) |
| Model Parameters | Training Script | Dict/Config | Hyperparameters for model training |
| Historical Data | Feedback System | JSON | User-reported false positives/negatives |

#### 6.7.1.3 Outputs

| Output Type | Destination | Format | Description |
|-------------|-------------|--------|-------------|
| Trained Model | Model Repository | .pkl/.joblib | Serialized XGBoost/Random Forest model |
| Prediction | Backend API | Integer | Binary classification (0=legitimate, 1=phishing) |
| Confidence Score | Backend API | Float | Probability estimate [0.0, 1.0] |
| Feature Importance | Documentation | DataFrame | Ranking of features by predictive power |
| Evaluation Metrics | Project Report | JSON/Dict | Performance statistics on test set |
| Feature Vector | Model Inference | NumPy Array | Extracted features from input URL |

#### 6.7.1.4 Dependencies

**Python Libraries:**
- `scikit-learn` (>=1.3.0): Core ML algorithms, preprocessing, metrics
- `xgboost` (>=2.0.0): Gradient boosting implementation
- `pandas` (>=2.0.0): Data manipulation and feature engineering
- `numpy` (>=1.24.0): Numerical computing and array operations
- `joblib` (>=1.3.0): Efficient model serialization
- `imbalanced-learn` (optional): SMOTE for class balancing

**Data Sources:**
- PhishTank API for phishing URLs
- Alexa Top 1M for legitimate URLs
- UCI ML Repository datasets

**Hardware Requirements:**
- Training: Multi-core CPU or GPU for faster training
- Inference: Minimal CPU (single-core sufficient)
- Memory: 4-8 GB RAM for training, <512 MB for inference

#### 6.7.1.5 Feature Extraction Details

The ML layer extracts the following feature categories:

**Lexical Features (String-based):**
```python
features = {
    'url_length': len(url),
    'num_dots': url.count('.'),
    'num_hyphens': url.count('-'),
    'num_underscores': url.count('_'),
    'num_slashes': url.count('/'),
    'num_question_marks': url.count('?'),
    'num_equals': url.count('='),
    'num_at_symbols': url.count('@'),
    'num_ampersands': url.count('&'),
    'num_digits': sum(c.isdigit() for c in url),
    'num_special_chars': sum(c in string.punctuation for c in url),
}
```

**Host-based Features:**
```python
features = {
    'hostname_length': len(hostname),
    'num_subdomains': hostname.count('.'),
    'has_ip_address': bool(re.match(r'\d+\.\d+\.\d+\.\d+', hostname)),
    'suspicious_tld': tld in ['.xyz', '.tk', '.ml', '.ga', '.cf'],
    'port_present': bool(parsed_url.port),
}
```

**Structural Features:**
```python
features = {
    'path_length': len(parsed_url.path),
    'query_length': len(parsed_url.query),
    'fragment_length': len(parsed_url.fragment),
    'has_https': parsed_url.scheme == 'https',
    'entropy': calculate_shannon_entropy(url),
}
```

#### 6.7.1.6 Model Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    ML Training Pipeline                     │
│                                                             │
│  ┌─────────────┐      ┌──────────────┐     ┌────────────┐ │
│  │   Raw       │      │  Feature     │     │  Labeled   │ │
│  │   URLs      │─────▶│  Extraction  │────▶│  Feature   │ │
│  │  (100K)     │      │              │     │  Vectors   │ │
│  └─────────────┘      └──────────────┘     └────────────┘ │
│                                                   │         │
│                                                   ▼         │
│                            ┌─────────────────────────────┐ │
│                            │  Train/Test Split (70/30)  │ │
│                            └────────────┬────────────────┘ │
│                                         │                  │
│                    ┌────────────────────┴───────┐          │
│                    ▼                            ▼          │
│           ┌─────────────────┐         ┌──────────────────┐│
│           │  Training Set   │         │   Test Set       ││
│           │    (70K)        │         │   (30K)          ││
│           └────────┬────────┘         └────────┬─────────┘│
│                    │                            │          │
│                    ▼                            │          │
│    ┌───────────────────────────────┐           │          │
│    │  Model Training & Tuning      │           │          │
│    │  • XGBoost                    │           │          │
│    │  • Random Forest              │           │          │
│    │  • 5-Fold Cross-Validation    │           │          │
│    │  • Grid Search                │           │          │
│    └───────────────┬───────────────┘           │          │
│                    │                            │          │
│                    ▼                            │          │
│           ┌─────────────────┐                  │          │
│           │  Trained Model  │                  │          │
│           │   (Best Params) │                  │          │
│           └────────┬────────┘                  │          │
│                    │                            │          │
│                    └────────────────────────────┘          │
│                                 │                          │
│                                 ▼                          │
│                    ┌─────────────────────────┐            │
│                    │  Model Evaluation       │            │
│                    │  • Accuracy: 96.3%      │            │
│                    │  • Precision: 94.8%     │            │
│                    │  • Recall: 97.1%        │            │
│                    │  • F1-Score: 95.9%      │            │
│                    │  • ROC-AUC: 0.982       │            │
│                    └─────────────────────────┘            │
│                                 │                          │
│                                 ▼                          │
│                    ┌─────────────────────────┐            │
│                    │  Model Serialization    │            │
│                    │  phishing_model_v1.pkl  │            │
│                    └─────────────────────────┘            │
└─────────────────────────────────────────────────────────────┘
```

---

### 6.7.2 Backend API Layer

The Backend API Layer serves as the bridge between the browser extension and the machine learning model, providing RESTful endpoints for URL classification.

#### 6.7.2.1 Responsibilities

1. **API Gateway Management**
   - Expose RESTful endpoints for client communication
   - Handle HTTP request routing and method validation
   - Implement request/response serialization
   - Provide automatic API documentation (Swagger/OpenAPI)

2. **Request Processing**
   - Validate incoming URL format and structure
   - Sanitize inputs to prevent injection attacks
   - Implement rate limiting to prevent abuse
   - Log requests for monitoring and debugging

3. **Feature Extraction Orchestration**
   - Parse URLs into constituent components
   - Invoke feature extraction functions
   - Aggregate features into model input format
   - Handle extraction errors gracefully

4. **Model Serving**
   - Load ML models into memory at startup
   - Manage model lifecycle and versioning
   - Route requests to appropriate model version
   - Cache model predictions for frequent URLs

5. **Response Formation**
   - Format predictions into standardized JSON responses
   - Include metadata (timestamp, version, confidence)
   - Implement error responses with appropriate status codes
   - Compress responses for bandwidth efficiency

6. **System Health Monitoring**
   - Provide health check endpoints for uptime monitoring
   - Track API performance metrics (latency, throughput)
   - Log errors and exceptions for debugging
   - Support graceful shutdown and restart

#### 6.7.2.2 Inputs

| Input Type | Source | Format | Description |
|------------|--------|--------|-------------|
| HTTP Request | Chrome Extension | JSON | POST request with URL to classify |
| URL String | Request Body | String | Target URL for phishing detection |
| API Key | Request Header | String | Authentication token (optional) |
| User Feedback | Feedback Endpoint | JSON | False positive/negative reports |
| Configuration | Config File | YAML/JSON | API settings, model paths, thresholds |

**Example API Request:**
```json
POST /api/v1/predict
Content-Type: application/json

{
  "url": "http://paypal-verify.suspicious-site.xyz/login",
  "user_id": "anonymous",
  "client_version": "1.0.0"
}
```

#### 6.7.2.3 Outputs

| Output Type | Destination | Format | Description |
|-------------|-------------|--------|-------------|
| Classification Result | Chrome Extension | JSON | Prediction with confidence and metadata |
| HTTP Status Code | Client | Integer | 200 (success), 400 (bad request), 500 (error) |
| Error Message | Client | JSON | Detailed error description for failures |
| Log Entries | Log File | Text | Request logs for monitoring and analytics |
| Metrics | Monitoring System | JSON | Performance metrics (response time, throughput) |

**Example API Response:**
```json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "url": "http://paypal-verify.suspicious-site.xyz/login",
  "prediction": "phishing",
  "confidence": 0.89,
  "risk_level": "high",
  "features": {
    "url_length": 52,
    "num_dots": 3,
    "suspicious_tld": true,
    "has_brand_keyword": true
  },
  "model_version": "v1.0",
  "timestamp": "2026-02-15T10:30:45Z",
  "processing_time_ms": 127
}
```

#### 6.7.2.4 Dependencies

**Python Libraries:**
- `fastapi` (>=0.100.0): Modern web framework for API development
- `uvicorn` (>=0.23.0): ASGI server for production deployment
- `pydantic` (>=2.0.0): Data validation using Python type annotations
- `python-dotenv`: Environment variable management
- `aiofiles`: Async file operations
- `httpx`: Async HTTP client for external requests

**System Dependencies:**
- Python 3.10+ runtime
- Trained ML model files (.pkl)
- SSL/TLS certificates for HTTPS
- Configuration files (API keys, model paths)

**External Services (Optional):**
- WHOIS API for domain age lookup
- VirusTotal API for additional threat intelligence
- Logging service (e.g., Sentry) for error tracking

#### 6.7.2.5 API Endpoint Specifications

##### Endpoint 1: URL Classification

```python
@app.post("/api/v1/predict")
async def predict_url(request: URLPredictionRequest) -> URLPredictionResponse:
    """
    Classify a URL as phishing or legitimate.
    
    Args:
        request: URLPredictionRequest containing URL and optional metadata
        
    Returns:
        URLPredictionResponse with classification, confidence, and risk level
        
    Raises:
        HTTPException 400: Invalid URL format
        HTTPException 429: Rate limit exceeded
        HTTPException 500: Internal server error
    """
```

**Request Schema (Pydantic):**
```python
class URLPredictionRequest(BaseModel):
    url: HttpUrl  # Validates URL format
    user_id: Optional[str] = "anonymous"
    client_version: Optional[str] = None
    
    @validator('url')
    def validate_url(cls, v):
        if len(v) > 2048:
            raise ValueError("URL exceeds maximum length")
        return v
```

**Response Schema:**
```python
class URLPredictionResponse(BaseModel):
    url: str
    prediction: Literal["phishing", "legitimate"]
    confidence: float = Field(ge=0.0, le=1.0)
    risk_level: Literal["high", "medium", "low"]
    features: Dict[str, Union[int, float, bool]]
    model_version: str
    timestamp: datetime
    processing_time_ms: int
```

##### Endpoint 2: Health Check

```python
@app.get("/api/v1/health")
async def health_check() -> HealthCheckResponse:
    """
    Health check endpoint for monitoring system status.
    
    Returns:
        HealthCheckResponse with system status and metrics
    """
```

**Response Example:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_version": "v1.0",
  "uptime_seconds": 3600,
  "total_requests": 1523,
  "avg_response_time_ms": 145,
  "timestamp": "2026-02-15T10:30:45Z"
}
```

##### Endpoint 3: Feedback Collection

```python
@app.post("/api/v1/feedback")
async def submit_feedback(feedback: FeedbackRequest) -> FeedbackResponse:
    """
    Collect user feedback on classification accuracy.
    
    Args:
        feedback: User-reported correction or validation
        
    Returns:
        Acknowledgment of feedback receipt
    """
```

#### 6.7.2.6 Backend Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                    FastAPI Backend Server                        │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                    API Gateway Layer                       │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐  │ │
│  │  │   Routing    │  │   CORS       │  │  Rate Limiter  │  │ │
│  │  │   Handler    │  │  Middleware  │  │                │  │ │
│  │  └──────────────┘  └──────────────┘  └────────────────┘  │ │
│  └─────────────────────────────┬──────────────────────────────┘ │
│                                │                                │
│  ┌─────────────────────────────▼──────────────────────────────┐ │
│  │                  Request Validation Layer                  │ │
│  │  • Pydantic Models                                         │ │
│  │  • URL Format Validation                                   │ │
│  │  • Input Sanitization                                      │ │
│  └─────────────────────────────┬──────────────────────────────┘ │
│                                │                                │
│  ┌─────────────────────────────▼──────────────────────────────┐ │
│  │                   Business Logic Layer                     │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │         Feature Extraction Service                   │ │ │
│  │  │  • URL Parser                                        │ │ │
│  │  │  • Lexical Feature Computer                          │ │ │
│  │  │  • Host Feature Extractor                            │ │ │
│  │  │  • Feature Vector Builder                            │ │ │
│  │  └──────────────────────────┬───────────────────────────┘ │ │
│  │                             │                              │ │
│  │  ┌──────────────────────────▼───────────────────────────┐ │ │
│  │  │         Model Inference Service                      │ │ │
│  │  │  • Model Loader (Singleton)                          │ │ │
│  │  │  • Prediction Engine                                 │ │ │
│  │  │  • Confidence Calculator                             │ │ │
│  │  │  • Result Interpreter                                │ │ │
│  │  └──────────────────────────┬───────────────────────────┘ │ │
│  │                             │                              │ │
│  │  ┌──────────────────────────▼───────────────────────────┐ │ │
│  │  │         Response Formatting Service                  │ │ │
│  │  │  • JSON Serializer                                   │ │ │
│  │  │  • Metadata Enrichment                               │ │ │
│  │  │  • Error Handler                                     │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                      Support Services                      │ │
│  │  ┌────────────┐  ┌──────────────┐  ┌──────────────────┐  │ │
│  │  │   Logger   │  │  Cache       │  │  Monitoring      │  │ │
│  │  │            │  │  (Redis)     │  │  (Prometheus)    │  │ │
│  │  └────────────┘  └──────────────┘  └──────────────────┘  │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                     Data Access Layer                      │ │
│  │  ┌────────────┐  ┌──────────────┐  ┌──────────────────┐  │ │
│  │  │   Model    │  │   Feature    │  │   Feedback       │  │ │
│  │  │   Store    │  │   Config     │  │   Database       │  │ │
│  │  └────────────┘  └──────────────┘  └──────────────────┘  │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

---

### 6.7.3 Browser Extension Layer

The Browser Extension Layer provides the user-facing interface and real-time URL interception capabilities within the Chrome browser.

#### 6.7.3.1 Responsibilities

1. **Navigation Interception**
   - Monitor all navigation events before page load
   - Capture URL changes from address bar, links, and redirects
   - Distinguish between user-initiated and automatic navigation
   - Support multiple navigation types (typed, link click, form submission)

2. **Local Decision Making**
   - Check local cache for recent URL classifications
   - Apply caching logic with time-based expiration
   - Manage whitelist of user-approved domains
   - Implement offline fallback behavior

3. **API Communication**
   - Construct and send HTTPS requests to backend API
   - Handle API responses asynchronously
   - Implement retry logic with exponential backoff
   - Manage timeout and error scenarios

4. **User Interface Management**
   - Display blocking pages for high-risk phishing URLs
   - Inject warning banners for medium-risk URLs
   - Render popup interface for settings and statistics
   - Provide intuitive controls for user actions

5. **Data Management**
   - Store user preferences using chrome.storage.local
   - Maintain whitelist and blacklist
   - Cache URL classifications with TTL
   - Track usage statistics (threats blocked, URLs checked)

6. **Security Enforcement**
   - Prevent navigation to blocked URLs
   - Implement Content Security Policy (CSP)
   - Validate API responses for tampering
   - Ensure secure communication channels

#### 6.7.3.2 Inputs

| Input Type | Source | Format | Description |
|------------|--------|--------|-------------|
| Navigation Event | Chrome Browser | Event Object | User navigation to new URL |
| User Action | Browser UI | Click/Input Event | User interaction with warnings or settings |
| API Response | Backend | JSON | Classification result from API |
| Cached Data | chrome.storage.local | JSON | Previously stored classifications and preferences |
| Configuration | User Settings | JSON | User-defined preferences and whitelists |

**Navigation Event Example:**
```javascript
chrome.webNavigation.onBeforeNavigate.addListener((details) => {
  // details.url: "http://suspicious-site.com"
  // details.tabId: 12345
  // details.frameId: 0
  // details.timeStamp: 1708001445000
});
```

#### 6.7.3.3 Outputs

| Output Type | Destination | Format | Description |
|-------------|-------------|--------|-------------|
| API Request | Backend Server | HTTPS/JSON | URL classification request |
| Warning UI | Browser Tab | HTML/CSS | Visual warning for phishing threats |
| Statistics | Popup UI | HTML | Threats blocked, URLs scanned count |
| Cache Update | chrome.storage.local | JSON | Updated classification cache |
| User Feedback | Backend API | JSON | False positive/negative reports |

**Warning Page HTML Structure:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Phishing Threat Detected</title>
  <style>
    /* Critical warning styles */
  </style>
</head>
<body>
  <div class="warning-container">
    <div class="warning-icon">⚠️</div>
    <h1>Phishing Threat Detected</h1>
    <p>The site you're trying to visit has been identified as a phishing threat.</p>
    <div class="url-display">http://malicious-site.com</div>
    <div class="confidence">Confidence: 89%</div>
    <button class="primary-action">Go Back to Safety</button>
    <a class="secondary-action">Continue Anyway (Not Recommended)</a>
  </div>
</body>
</html>
```

#### 6.7.3.4 Dependencies

**Chrome Extension APIs:**
- `chrome.webNavigation`: Intercept navigation events
- `chrome.webRequest`: Monitor and modify network requests
- `chrome.tabs`: Manage browser tabs and navigation
- `chrome.storage.local`: Persistent local data storage
- `chrome.runtime`: Extension lifecycle and messaging
- `chrome.declarativeContent`: Page-specific actions

**Web Technologies:**
- JavaScript ES6+: Core extension logic
- HTML5: User interface markup
- CSS3: Styling and animations
- Fetch API: HTTP communication
- LocalStorage API: Fallback storage

**Chrome Extension Platform:**
- Manifest V3: Latest extension architecture
- Service Workers: Background script execution
- Content Scripts: Page context injection

#### 6.7.3.5 Extension Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                Chrome Extension Components                       │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │               Background Service Worker                    │ │
│  │  (Persistent background script, Manifest V3)               │ │
│  │                                                            │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │         Navigation Event Listener                    │ │ │
│  │  │  chrome.webNavigation.onBeforeNavigate               │ │ │
│  │  │  • Capture URL before page load                      │ │ │
│  │  │  • Extract target URL                                │ │ │
│  │  │  • Check if user-initiated navigation                │ │ │
│  │  └────────────────────┬─────────────────────────────────┘ │ │
│  │                       │                                    │ │
│  │  ┌────────────────────▼─────────────────────────────────┐ │ │
│  │  │         Cache & Whitelist Checker                    │ │ │
│  │  │  • Query chrome.storage.local                        │ │ │
│  │  │  • Check whitelist (user-approved domains)           │ │ │
│  │  │  • Check cache (24hr TTL)                            │ │ │
│  │  │  • Return cached result if available                 │ │ │
│  │  └────────────────────┬─────────────────────────────────┘ │ │
│  │                       │                                    │ │
│  │            Cache Hit? │ Cache Miss?                        │ │
│  │                       │                                    │ │
│  │  ┌────────────────────▼─────────────────────────────────┐ │ │
│  │  │         API Communication Module                     │ │ │
│  │  │  • Construct API request                             │ │ │
│  │  │  • Send HTTPS POST to backend                        │ │ │
│  │  │  • Handle response/timeout/errors                    │ │ │
│  │  │  • Implement retry with backoff                      │ │ │
│  │  └────────────────────┬─────────────────────────────────┘ │ │
│  │                       │                                    │ │
│  │  ┌────────────────────▼─────────────────────────────────┐ │ │
│  │  │         Decision Engine                              │ │ │
│  │  │  • Parse API response                                │ │ │
│  │  │  • Apply risk thresholds                             │ │ │
│  │  │    - confidence > 80% → Block                        │ │ │
│  │  │    - confidence 60-80% → Warn                        │ │ │
│  │  │    - confidence < 60% → Allow                        │ │ │
│  │  │  • Update cache with result                          │ │ │
│  │  └────────────────────┬─────────────────────────────────┘ │ │
│  │                       │                                    │ │
│  │  ┌────────────────────▼─────────────────────────────────┐ │ │
│  │  │         Action Dispatcher                            │ │ │
│  │  │  • Block: Redirect to warning page                   │ │ │
│  │  │  • Warn: Send message to content script              │ │ │
│  │  │  • Allow: Continue navigation                        │ │ │
│  │  │  • Update statistics                                 │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                    Content Scripts                         │ │
│  │  (Injected into web pages)                                 │ │
│  │                                                            │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │         Warning Banner Injector                      │ │ │
│  │  │  • Receive message from background script            │ │ │
│  │  │  • Create warning banner DOM element                 │ │ │
│  │  │  • Inject at top of page                             │ │ │
│  │  │  • Handle user interactions                          │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  │                                                            │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │         Page Context Monitor                         │ │ │
│  │  │  • Detect dynamic URL changes                        │ │ │
│  │  │  • Monitor AJAX navigation (SPA)                     │ │ │
│  │  │  • Report to background script                       │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                     Popup Interface                        │ │
│  │  (popup.html, popup.js)                                    │ │
│  │                                                            │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │         Statistics Display                           │ │ │
│  │  │  • Total URLs checked                                │ │ │
│  │  │  • Threats blocked (today/total)                     │ │ │
│  │  │  • False positives reported                          │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  │                                                            │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │         Settings Panel                               │ │ │
│  │  │  • Enable/disable protection toggle                  │ │ │
│  │  │  • Sensitivity slider                                │ │ │
│  │  │  • Whitelist management UI                           │ │ │
│  │  │  • Clear cache button                                │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                    Warning Page                            │ │
│  │  (warning.html, warning.js)                                │ │
│  │                                                            │ │
│  │  • Full-page blocking interface                           │ │
│  │  • Large warning icon and message                         │ │
│  │  • URL display with confidence score                      │ │
│  │  • "Go Back" and "Proceed Anyway" buttons                 │ │
│  │  • Report false positive option                           │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                   Storage Manager                          │ │
│  │                                                            │ │
│  │  ┌─────────────────┐  ┌─────────────────┐                │ │
│  │  │   Cache         │  │   Whitelist     │                │ │
│  │  │   {url: result} │  │   [domains]     │                │ │
│  │  └─────────────────┘  └─────────────────┘                │ │
│  │  ┌─────────────────┐  ┌─────────────────┐                │ │
│  │  │   Statistics    │  │   Preferences   │                │ │
│  │  │   {count, date} │  │   {enabled,...} │                │ │
│  │  └─────────────────┘  └─────────────────┘                │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

#### 6.7.3.6 Extension Manifest (V3)

```json
{
  "manifest_version": 3,
  "name": "Phishing URL Detector",
  "version": "1.0.0",
  "description": "Real-time ML-based phishing detection",
  
  "permissions": [
    "webNavigation",
    "webRequest",
    "storage",
    "tabs",
    "activeTab"
  ],
  
  "host_permissions": [
    "<all_urls>"
  ],
  
  "background": {
    "service_worker": "background.js",
    "type": "module"
  },
  
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["content.js"],
    "css": ["content.css"],
    "run_at": "document_start"
  }],
  
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  
  "web_accessible_resources": [{
    "resources": ["warning.html", "icons/*"],
    "matches": ["<all_urls>"]
  }],
  
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self'"
  }
}
```

---

### 6.7.4 Adversarial Testing Module

The Adversarial Testing Module evaluates system robustness against sophisticated phishing techniques and edge cases that may evade detection.

#### 6.7.4.1 Responsibilities

1. **Attack Simulation**
   - Generate synthetic phishing URLs with obfuscation techniques
   - Simulate zero-day phishing campaigns
   - Test homograph attacks (IDN homographs)
   - Evaluate URL shortener redirection chains

2. **Robustness Testing**
   - Test model performance on adversarial examples
   - Evaluate decision boundaries and confidence thresholds
   - Identify failure modes and edge cases
   - Measure model uncertainty on ambiguous URLs

3. **Evasion Technique Testing**
   - Test character substitution (0 vs O, 1 vs l)
   - Evaluate subdomain manipulation
   - Test URL encoding obfuscation (%20, %2F)
   - Assess IP address-based phishing

4. **Performance Under Attack**
   - Measure degradation under adversarial inputs
   - Test rate limiting and API abuse scenarios
   - Evaluate system behavior under load
   - Assess recovery from malicious inputs

5. **Red Team Testing**
   - Manual penetration testing of API endpoints
   - Test for injection vulnerabilities
   - Evaluate XSS resistance in extension UI
   - Test authentication bypass attempts

#### 6.7.4.2 Inputs

| Input Type | Source | Format | Description |
|------------|--------|--------|-------------|
| Adversarial URLs | Synthetic Generator | List[str] | Crafted phishing URLs with obfuscation |
| Zero-Day Phishing | PhishTank Recent | CSV | Recently reported phishing URLs |
| Benign Variations | URL Mutator | List[str] | Legitimate URLs with minor modifications |
| Attack Patterns | Security Research | JSON | Known phishing techniques |
| Test Specifications | Test Plan | YAML | Test cases and expected outcomes |

**Example Adversarial Test Cases:**
```python
adversarial_tests = {
    "homograph_attack": [
        "https://pаypal.com",  # Cyrillic 'а' instead of Latin 'a'
        "https://gооgle.com",  # Cyrillic 'о' instead of Latin 'o'
    ],
    "subdomain_spoofing": [
        "https://paypal.com.verify-account.xyz",
        "https://secure-facebook-login.attacker.com",
    ],
    "url_obfuscation": [
        "https://example.com%2f@attacker.com",
        "https://attacker.com%252f%252fexample.com",
    ],
    "ip_based_phishing": [
        "https://192.168.1.100/paypal-login",
        "https://127.0.0.1:8080/bank-verify",
    ],
    "shortener_chains": [
        "https://bit.ly/3xyz → https://tinyurl.com/abc → phishing-site",
    ]
}
```

#### 6.7.4.3 Outputs

| Output Type | Destination | Format | Description |
|-------------|-------------|--------|-------------|
| Test Report | Documentation | PDF/HTML | Comprehensive adversarial testing results |
| Failure Cases | Development Team | CSV | URLs where model failed |
| Robustness Metrics | Project Report | JSON | Attack success rates, evasion rates |
| Recommendations | System Improvement | Markdown | Suggested defenses and model improvements |
| Security Audit | Stakeholders | PDF | Overall security posture assessment |

**Adversarial Testing Report Structure:**
```markdown
# Adversarial Testing Report

## Executive Summary
- Total test cases: 500
- Attack success rate: 12%
- Zero-day detection rate: 88%
- Critical vulnerabilities: 2

## Attack Category Results

### Homograph Attacks
- Test cases: 50
- Detected: 38 (76%)
- Missed: 12 (24%)
- Recommendation: Add Unicode normalization

### Subdomain Spoofing
- Test cases: 100
- Detected: 92 (92%)
- Missed: 8 (8%)
- Status: Good performance

### URL Obfuscation
- Test cases: 75
- Detected: 60 (80%)
- Missed: 15 (20%)
- Recommendation: Enhance encoding detection
```

#### 6.7.4.4 Dependencies

**Testing Libraries:**
- `pytest`: Test framework and fixtures
- `hypothesis`: Property-based testing
- `faker`: Synthetic data generation
- `requests`: API testing
- `selenium`: Browser automation for extension testing

**Security Tools:**
- `OWASP ZAP`: API security testing
- `Burp Suite`: Manual penetration testing
- `sqlmap`: SQL injection testing (if database added)

**Analysis Tools:**
- `matplotlib`: Visualization of attack patterns
- `pandas`: Test result analysis
- `scikit-learn`: Adversarial robustness metrics

#### 6.7.4.5 Testing Methodology

```
┌──────────────────────────────────────────────────────────────────┐
│              Adversarial Testing Pipeline                        │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  PHASE 1: Test Case Generation                            │ │
│  │                                                            │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐  │ │
│  │  │  Synthetic   │  │  Zero-Day    │  │  Real-World    │  │ │
│  │  │  Adversarial │  │  Phishing    │  │  Edge Cases    │  │ │
│  │  │  Generator   │  │  URLs        │  │  Collection    │  │ │
│  │  └──────┬───────┘  └──────┬───────┘  └────────┬───────┘  │ │
│  │         │                 │                    │          │ │
│  │         └─────────────────┴────────────────────┘          │ │
│  │                           │                                │ │
│  │                           ▼                                │ │
│  │              ┌─────────────────────────┐                  │ │
│  │              │  Combined Test Suite   │                  │ │
│  │              │  (500+ test cases)     │                  │ │
│  │              └────────────┬────────────┘                  │ │
│  └─────────────────────────────┼──────────────────────────────┘ │
│                                │                                │
│  ┌─────────────────────────────▼──────────────────────────────┐ │
│  │  PHASE 2: Automated Testing                              │ │
│  │                                                            │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │  For each test case:                                 │ │ │
│  │  │  1. Send to API endpoint                             │ │ │
│  │  │  2. Record prediction & confidence                   │ │ │
│  │  │  3. Compare with expected label                      │ │ │
│  │  │  4. Classify as: TP, TN, FP, FN                      │ │ │
│  │  └──────────────────────────┬───────────────────────────┘ │ │
│  │                             │                              │ │
│  │  ┌──────────────────────────▼───────────────────────────┐ │ │
│  │  │  Collect Results:                                    │ │ │
│  │  │  • Attack success rate                               │ │ │
│  │  │  • False negative rate on adversarial               │ │ │
│  │  │  • Confidence score distribution                     │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  PHASE 3: Manual Penetration Testing                      │ │
│  │                                                            │ │
│  │  • API endpoint fuzzing                                   │ │
│  │  • Input validation bypass attempts                       │ │
│  │  • Extension XSS testing                                  │ │
│  │  • CSRF vulnerability checks                              │ │
│  │  • Rate limiting evasion                                  │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                │                                │
│  ┌─────────────────────────────▼──────────────────────────────┐ │
│  │  PHASE 4: Analysis & Reporting                            │ │
│  │                                                            │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │  Failure Case Analysis:                              │ │ │
│  │  │  • Identify patterns in missed phishing              │ │ │
│  │  │  • Analyze confidence scores of failures             │ │ │
│  │  │  • Categorize attack techniques                      │ │ │
│  │  └──────────────────────────┬───────────────────────────┘ │ │
│  │                             │                              │ │
│  │  ┌──────────────────────────▼───────────────────────────┐ │ │
│  │  │  Generate Recommendations:                           │ │ │
│  │  │  • Model improvements                                │ │ │
│  │  │  • Feature engineering suggestions                   │ │ │
│  │  │  • Security hardening measures                       │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

#### 6.7.4.6 Key Adversarial Test Categories

**1. Encoding & Obfuscation Attacks:**
- URL encoding: `%2F%2Fpaypal.com`
- Double encoding: `%252F%252F`
- Mixed encoding: `http://example%2Ecom`
- Unicode normalization bypass

**2. Homograph & Typosquatting:**
- IDN homographs: Cyrillic/Greek characters
- Visual similarity: `rn` vs `m`
- Character substitution: `0` vs `O`
- Missing characters: `gogle.com`

**3. Subdomain Manipulation:**
- Trusted domain in subdomain: `paypal.attacker.com`
- Long subdomain chains: `a.b.c.d.e.attacker.com`
- Hyphen tricks: `pay-pal-secure.com`

**4. Structural Attacks:**
- IP address URLs: `http://192.168.1.1/login`
- Port obfuscation: `:8080`, `:443`
- Fragment manipulation: `#@trusted.com`
- Username in URL: `http://user@attacker.com`

**5. Redirection Chains:**
- URL shortener abuse
- Multiple 302 redirects
- JavaScript-based redirects
- Meta refresh redirects

---

## 6.6 Machine Learning Requirements Specification

### 6.6.1 ML System Overview

The machine learning component forms the core intelligence of the phishing detection system. This section defines the requirements for model selection, feature engineering, training procedures, evaluation metrics, and deployment strategies to ensure a robust, accurate, and maintainable ML pipeline.

#### ML Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    OFFLINE TRAINING PIPELINE                    │
└─────────────────────────────────────────────────────────────────┘

[1] Data Collection
    ├── Phishing URLs: PhishTank, OpenPhish
    ├── Legitimate URLs: Alexa Top 1M, Common Crawl
    └── Dataset size: 100,000+ URLs (50k phishing, 50k legitimate)
              ↓
[2] Data Preprocessing
    ├── Remove duplicates
    ├── URL normalization (lowercase, remove trailing slash)
    ├── Handle missing/malformed URLs
    ├── Label validation
    └── Train-test split (70-15-15)
              ↓
[3] Feature Engineering
    ├── Lexical features (15+ features)
    ├── Domain-based features (10+ features)
    ├── Statistical features (5+ features)
    └── Binary flags (5+ features)
              ↓
[4] Feature Scaling & Transformation
    ├── StandardScaler or MinMaxScaler
    ├── Handle feature distributions
    └── Save scaler object for deployment
              ↓
[5] Model Training
    ├── Algorithm: XGBoost, Random Forest
    ├── Cross-validation: 5-fold stratified
    ├── Hyperparameter tuning: Grid/Random search
    └── Handle class imbalance: SMOTE or class weights
              ↓
[6] Model Evaluation
    ├── Metrics: Accuracy, Precision, Recall, F1, ROC-AUC
    ├── Confusion matrix analysis
    ├── Feature importance ranking
    └── Error analysis
              ↓
[7] Model Serialization
    ├── Save trained model (.pkl)
    ├── Save scaler (.joblib)
    ├── Save feature metadata (JSON)
    └── Version tagging (v1.0, v1.1, etc.)

┌─────────────────────────────────────────────────────────────────┐
│                   ONLINE INFERENCE PIPELINE                      │
└─────────────────────────────────────────────────────────────────┘

[1] Model Loading (at startup)
    ├── Load trained model from disk
    ├── Load scaler object
    ├── Verify model integrity
    └── Warm-up inference
              ↓
[2] Feature Extraction (per request)
    ├── Parse URL string
    ├── Compute features (same as training)
    └── Return feature vector
              ↓
[3] Feature Scaling
    ├── Apply loaded scaler
    └── Transform to model input format
              ↓
[4] Model Prediction
    ├── Binary classification (0=legitimate, 1=phishing)
    ├── Probability scores [P(legitimate), P(phishing)]
    └── Confidence = max(probabilities)
              ↓
[5] Post-processing
    ├── Risk categorization (safe/low/medium/high)
    ├── Response formatting
    └── Logging (for monitoring)
```

---

### 6.6.2 Model Selection Strategy

#### Requirements for Algorithm Selection

| Criterion | Requirement | Priority | Rationale |
|-----------|-------------|----------|-----------|
| **Accuracy** | ≥95% on test set | Critical | Minimize false negatives (missed phishing sites) |
| **Precision** | ≥93% | Critical | Minimize false positives (legitimate sites blocked) |
| **Inference Speed** | <50ms per prediction | Critical | Real-time requirement for browser extension |
| **Interpretability** | Medium to high | High | Enable feature importance analysis and debugging |
| **Training Time** | <2 hours on standard hardware | Medium | Enable rapid experimentation and iteration |
| **Model Size** | <100MB serialized | Medium | Deployment efficiency and memory constraints |
| **Robustness** | Resilient to adversarial examples | High | Resist URL obfuscation techniques |
| **Scalability** | Handle 100k+ training samples | Medium | Support large dataset training |

#### Candidate Algorithms Evaluation

| Algorithm | Pros | Cons | Expected Performance | Recommendation |
|-----------|------|------|---------------------|----------------|
| **XGBoost** | • Excellent accuracy on tabular data<br>• Fast inference<br>• Built-in feature importance<br>• Handles missing values<br>• Regularization to prevent overfitting | • Black-box nature<br>• Requires hyperparameter tuning<br>• Moderate training time | Accuracy: 96-98%<br>F1-Score: 95-97%<br>Inference: 10-30ms | **Primary Choice** |
| **Random Forest** | • Good accuracy<br>• Robust to overfitting<br>• Easily interpretable<br>• No feature scaling needed<br>• Parallel training | • Larger model size<br>• Slower inference than XGBoost<br>• Can be memory intensive | Accuracy: 94-96%<br>F1-Score: 93-95%<br>Inference: 20-50ms | **Secondary/Ensemble** |
| **Logistic Regression** | • Very fast inference<br>• Highly interpretable<br>• Small model size<br>• Easy to deploy | • Lower accuracy on complex patterns<br>• Requires feature engineering<br>• Linear decision boundary | Accuracy: 88-92%<br>F1-Score: 87-90%<br>Inference: 1-5ms | Baseline only |
| **Neural Networks (MLP)** | • Can learn complex patterns<br>• High potential accuracy | • Requires more data<br>• Longer training time<br>• Less interpretable<br>• Slower inference | Accuracy: 95-97%<br>F1-Score: 94-96%<br>Inference: 30-100ms | Future consideration |
| **Naive Bayes** | • Very fast training/inference<br>• Simple implementation | • Strong independence assumption<br>• Lower accuracy | Accuracy: 85-88%<br>F1-Score: 83-86%<br>Inference: 1-5ms | Not recommended |

#### Selected Algorithm: XGBoost

**Justification**:
1. **Superior Performance**: XGBoost consistently achieves state-of-the-art results on tabular data, with expected accuracy >95%
2. **Inference Speed**: Optimized C++ implementation provides <50ms inference, meeting real-time requirements
3. **Built-in Regularization**: L1 (Lasso) and L2 (Ridge) regularization prevent overfitting
4. **Feature Importance**: Native support for feature importance analysis aids debugging and explainability
5. **Robustness**: Tree-based models are less sensitive to feature scaling and outliers
6. **Industry Adoption**: Widely used in production systems with proven reliability

**Ensemble Strategy** (Optional Enhancement):
- Combine XGBoost with Random Forest using soft voting
- Weights: 60% XGBoost, 40% Random Forest (tuned on validation set)
- Improves robustness and reduces overfitting
- Trade-off: Slightly slower inference (~50-80ms)

#### Hyperparameter Search Space

**XGBoost Hyperparameters**:

| Parameter | Search Space | Default | Purpose |
|-----------|--------------|---------|---------|
| `n_estimators` | [100, 200, 300] | 200 | Number of boosting rounds |
| `max_depth` | [5, 7, 10, 15] | 7 | Maximum tree depth (controls complexity) |
| `learning_rate` | [0.01, 0.05, 0.1, 0.2] | 0.1 | Step size shrinkage (prevents overfitting) |
| `subsample` | [0.7, 0.8, 0.9, 1.0] | 0.8 | Fraction of samples per tree |
| `colsample_bytree` | [0.7, 0.8, 0.9, 1.0] | 0.8 | Fraction of features per tree |
| `min_child_weight` | [1, 3, 5] | 1 | Minimum sum of instance weight in child |
| `gamma` | [0, 0.1, 0.2] | 0 | Minimum loss reduction for split |
| `reg_alpha` | [0, 0.1, 1] | 0 | L1 regularization term |
| `reg_lambda` | [1, 2, 3] | 1 | L2 regularization term |
| `scale_pos_weight` | [1, 1.5, 2] | 1 | Balance of positive/negative weights |

**Optimization Method**:
- **Grid Search**: Exhaustive search over discrete parameter grid
- **Random Search**: Sample random combinations (faster, often sufficient)
- **Bayesian Optimization**: Intelligent search using Gaussian processes (most efficient)

**Recommendation**: Use Randomized Search (50-100 iterations) followed by fine-tuning with Grid Search

---

### 6.6.3 Feature Engineering Requirements

Feature engineering is critical for model performance. This section defines the comprehensive feature set extracted from URL strings.

#### Feature Categories Overview

| Category | Number of Features | Computational Cost | Importance |
|----------|-------------------|-------------------|------------|
| **Lexical Features** | 15-20 | Low | High |
| **Domain-Based Features** | 10-15 | Medium | Very High |
| **Statistical Features** | 5-10 | Medium | Medium |
| **Binary Flags** | 5-10 | Low | High |
| **Optional/External** | 5+ | High (API calls) | Medium |
| **Total** | **35-50+** | - | - |

---

#### 6.6.3.1 Lexical Features

Lexical features analyze the character-level composition of the URL string.

| Feature ID | Feature Name | Description | Example | Computation |
|------------|--------------|-------------|---------|-------------|
| **LEX-01** | `url_length` | Total character count of URL | `https://example.com/path` → 26 | `len(url)` |
| **LEX-02** | `domain_length` | Character count of domain only | `example.com` → 11 | `len(domain)` |
| **LEX-03** | `path_length` | Character count of path component | `/path/to/page` → 13 | `len(path)` |
| **LEX-04** | `num_dots` | Count of '.' characters | `sub.example.co.uk` → 3 | `url.count('.')` |
| **LEX-05** | `num_hyphens` | Count of '-' characters | `my-secure-bank.com` → 2 | `url.count('-')` |
| **LEX-06** | `num_underscores` | Count of '_' characters | `user_login.php` → 1 | `url.count('_')` |
| **LEX-07** | `num_slashes` | Count of '/' characters | `https://a.com/b/c` → 3 | `url.count('/')` |
| **LEX-08** | `num_questionmarks` | Count of '?' characters | Query parameters indicator | `url.count('?')` |
| **LEX-09** | `num_equals` | Count of '=' characters | Query parameter assignments | `url.count('=')` |
| **LEX-10** | `num_at` | Count of '@' characters | Credential obfuscation | `url.count('@')` |
| **LEX-11** | `num_ampersands` | Count of '&' characters | Multiple query parameters | `url.count('&')` |
| **LEX-12** | `num_digits` | Count of numeric characters | `bank123.com` → 3 | `sum(c.isdigit() for c in url)` |
| **LEX-13** | `num_letters` | Count of alphabetic characters | Character distribution | `sum(c.isalpha() for c in url)` |
| **LEX-14** | `num_special_chars` | Count of special symbols | `%`, `#`, `$`, etc. | Custom function |
| **LEX-15** | `url_entropy` | Shannon entropy of URL string | Measures randomness | `-Σ(p(x) * log2(p(x)))` |
| **LEX-16** | `digit_letter_ratio` | Ratio of digits to letters | Suspicious if high | `num_digits / num_letters` |
| **LEX-17** | `vowel_consonant_ratio` | Ratio of vowels to consonants | Natural language check | `vowels / consonants` |
| **LEX-18** | `uppercase_ratio` | Ratio of uppercase letters | Abnormal patterns | `uppercase / total_letters` |
| **LEX-19** | `longest_word_length` | Max length of tokens in URL | Abnormally long tokens | `max(len(token))` |
| **LEX-20** | `avg_token_length` | Average token length | Token distribution | `mean(len(tokens))` |

**Feature Implementation Example**:
```python
import math
from collections import Counter
from urllib.parse import urlparse

def extract_lexical_features(url: str) -> dict:
    """Extract lexical features from URL string"""
    features = {}
    
    # Basic counts
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['num_underscores'] = url.count('_')
    features['num_slashes'] = url.count('/')
    features['num_questionmarks'] = url.count('?')
    features['num_equals'] = url.count('=')
    features['num_at'] = url.count('@')
    features['num_ampersands'] = url.count('&')
    
    # Character type counts
    features['num_digits'] = sum(c.isdigit() for c in url)
    features['num_letters'] = sum(c.isalpha() for c in url)
    features['num_special_chars'] = sum(not c.isalnum() for c in url)
    
    # Ratios
    if features['num_letters'] > 0:
        features['digit_letter_ratio'] = features['num_digits'] / features['num_letters']
    else:
        features['digit_letter_ratio'] = 0
    
    # Shannon entropy
    char_freq = Counter(url)
    length = len(url)
    entropy = -sum((count/length) * math.log2(count/length) 
                   for count in char_freq.values())
    features['url_entropy'] = entropy
    
    # Parse components
    parsed = urlparse(url)
    features['domain_length'] = len(parsed.netloc)
    features['path_length'] = len(parsed.path)
    
    return features
```

---

#### 6.6.3.2 Domain-Based Features

Domain-based features analyze the hostname/domain characteristics.

| Feature ID | Feature Name | Description | Example | Phishing Indicator |
|------------|--------------|-------------|---------|-------------------|
| **DOM-01** | `num_subdomains` | Count of subdomain levels | `a.b.example.com` → 2 | High count suspicious |
| **DOM-02** | `subdomain_depth` | Maximum subdomain nesting | `secure.login.paypal.verify.tk` → 4 | >3 is suspicious |
| **DOM-03** | `domain_token_count` | Number of tokens in domain | `my-secure-bank` → 3 | Many tokens suspicious |
| **DOM-04** | `longest_subdomain` | Length of longest subdomain | `verylongsubdomain.ex.com` → 17 | >15 suspicious |
| **DOM-05** | `avg_subdomain_length` | Average subdomain length | Statistical measure | Abnormal if very high/low |
| **DOM-06** | `has_ip_address` | Domain is IP (not domain name) | `192.168.1.1` → 1 | Binary: 1=IP, 0=domain |
| **DOM-07** | `is_https` | URL uses HTTPS | `https://` → 1, `http://` → 0 | HTTPS is more legitimate |
| **DOM-08** | `suspicious_tld` | TLD in suspicious list | `.tk`, `.ml`, `.ga`, `.cf` | Binary flag |
| **DOM-09** | `tld_length` | Length of TLD | `.com` → 3, `.museum` → 6 | Unusual lengths suspicious |
| **DOM-10** | `domain_has_hyphen` | Domain contains hyphen | `my-bank.com` → 1 | Often used in phishing |
| **DOM-11** | `domain_has_digit` | Domain contains digit | `bank123.com` → 1 | Suspicious for brands |
| **DOM-12** | `port_number_present` | Non-standard port in URL | `:8080` → 1 | Non-80/443 suspicious |
| **DOM-13** | `is_shortening_service` | URL uses shortener | `bit.ly`, `tinyurl.com` | Binary flag |
| **DOM-14** | `contains_brand_name` | Common brand in subdomain | `paypal` in subdomain | Brand spoofing |
| **DOM-15** | `punycode_domain` | IDN with punycode encoding | `xn--...` domains | Homograph attack |

**Suspicious TLD List**:
```python
SUSPICIOUS_TLDS = {
    '.tk', '.ml', '.ga', '.cf', '.gq',  # Free TLDs (common in phishing)
    '.xyz', '.top', '.work', '.click',   # Cheap TLDs
    '.info', '.biz',                      # Often abused
    '.club', '.online', '.site'           # New generic TLDs
}
```

**URL Shortening Services**:
```python
SHORTENING_SERVICES = {
    'bit.ly', 'tinyurl.com', 'goo.gl', 't.co',
    'ow.ly', 'buff.ly', 'adf.ly', 'short.link'
}
```

**Common Brand Keywords** (for spoofing detection):
```python
BRAND_KEYWORDS = [
    'paypal', 'amazon', 'google', 'facebook', 'apple',
    'microsoft', 'netflix', 'ebay', 'instagram', 'twitter',
    'bank', 'signin', 'login', 'verify', 'account',
    'secure', 'update', 'confirm', 'wallet'
]
```

**Domain Feature Implementation**:
```python
import tldextract
import re

def extract_domain_features(url: str) -> dict:
    """Extract domain-based features from URL"""
    features = {}
    parsed = urlparse(url)
    domain = parsed.netloc
    
    # Extract TLD using tldextract
    ext = tldextract.extract(url)
    subdomain = ext.subdomain
    domain_name = ext.domain
    tld = ext.suffix
    
    # Subdomain analysis
    if subdomain:
        subdomains = subdomain.split('.')
        features['num_subdomains'] = len(subdomains)
        features['subdomain_depth'] = len(subdomains)
        features['longest_subdomain'] = max(len(s) for s in subdomains)
        features['avg_subdomain_length'] = sum(len(s) for s in subdomains) / len(subdomains)
    else:
        features['num_subdomains'] = 0
        features['subdomain_depth'] = 0
        features['longest_subdomain'] = 0
        features['avg_subdomain_length'] = 0
    
    # Domain token analysis
    domain_tokens = re.split(r'[-_.]', domain_name)
    features['domain_token_count'] = len(domain_tokens)
    
    # Binary flags
    features['has_ip_address'] = 1 if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', domain) else 0
    features['is_https'] = 1 if parsed.scheme == 'https' else 0
    features['suspicious_tld'] = 1 if ('.' + tld) in SUSPICIOUS_TLDS else 0
    features['tld_length'] = len(tld)
    features['domain_has_hyphen'] = 1 if '-' in domain_name else 0
    features['domain_has_digit'] = 1 if any(c.isdigit() for c in domain_name) else 0
    features['port_number_present'] = 1 if parsed.port else 0
    features['is_shortening_service'] = 1 if domain in SHORTENING_SERVICES else 0
    
    # Brand name detection (case-insensitive)
    domain_lower = domain.lower()
    features['contains_brand_name'] = 1 if any(brand in domain_lower for brand in BRAND_KEYWORDS) else 0
    
    # Punycode detection
    features['punycode_domain'] = 1 if 'xn--' in domain else 0
    
    return features
```

---

#### 6.6.3.3 Statistical Features

Statistical features capture distributional properties and patterns.

| Feature ID | Feature Name | Description | Formula | Interpretation |
|------------|--------------|-------------|---------|----------------|
| **STAT-01** | `url_entropy` | Shannon entropy of character distribution | H = -Σ p(x) log₂ p(x) | Higher = more random |
| **STAT-02** | `consonant_vowel_ratio` | Ratio of consonants to vowels | consonants / vowels | Natural language check |
| **STAT-03** | `digit_concentration` | Digits clustered or distributed | Std dev of digit positions | Clustering suspicious |
| **STAT-04** | `special_char_concentration` | Special chars clustered | Std dev of special positions | Clustering suspicious |
| **STAT-05** | `path_token_count` | Number of path segments | `/a/b/c` → 3 | Many segments suspicious |
| **STAT-06** | `query_param_count` | Number of query parameters | `?a=1&b=2` → 2 | Many params suspicious |
| **STAT-07** | `avg_word_length` | Average token length across URL | mean(token lengths) | Statistical baseline |
| **STAT-08** | `std_word_length` | Std deviation of token lengths | std(token lengths) | High variance suspicious |
| **STAT-09** | `char_diversity` | Unique chars / total chars | len(set(url)) / len(url) | Low diversity suspicious |
| **STAT-10** | `hex_encoding_ratio` | Percentage of URL that is hex-encoded | `%XX` sequences | High ratio suspicious |

**Statistical Feature Implementation**:
```python
import numpy as np
from collections import Counter

def extract_statistical_features(url: str) -> dict:
    """Extract statistical features from URL"""
    features = {}
    
    # Shannon entropy (already in lexical)
    char_freq = Counter(url)
    length = len(url)
    entropy = -sum((count/length) * np.log2(count/length) 
                   for count in char_freq.values())
    features['url_entropy'] = entropy
    
    # Character diversity
    features['char_diversity'] = len(set(url)) / len(url) if len(url) > 0 else 0
    
    # Vowel/consonant analysis
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel_count = sum(c in vowels for c in url)
    consonant_count = sum(c in consonants for c in url)
    features['consonant_vowel_ratio'] = consonant_count / vowel_count if vowel_count > 0 else 0
    
    # Parse URL components
    parsed = urlparse(url)
    
    # Path analysis
    path_tokens = [t for t in parsed.path.split('/') if t]
    features['path_token_count'] = len(path_tokens)
    
    # Query parameter analysis
    query_params = parsed.query.split('&') if parsed.query else []
    features['query_param_count'] = len(query_params)
    
    # Token length statistics
    tokens = re.findall(r'\w+', url)
    if tokens:
        token_lengths = [len(t) for t in tokens]
        features['avg_word_length'] = np.mean(token_lengths)
        features['std_word_length'] = np.std(token_lengths)
    else:
        features['avg_word_length'] = 0
        features['std_word_length'] = 0
    
    # Hex encoding detection
    hex_pattern = r'%[0-9A-Fa-f]{2}'
    hex_matches = re.findall(hex_pattern, url)
    features['hex_encoding_ratio'] = len(hex_matches) * 3 / len(url) if len(url) > 0 else 0
    
    return features
```

---

#### 6.6.3.4 Binary Flag Features

Binary features indicate presence/absence of specific patterns.

| Feature ID | Feature Name | Condition | Phishing Indicator |
|------------|--------------|-----------|-------------------|
| **FLAG-01** | `has_ip_address` | Domain is numeric IP | 1 = suspicious |
| **FLAG-02** | `is_https` | URL uses HTTPS | 0 = suspicious |
| **FLAG-03** | `has_at_symbol` | '@' in URL | 1 = suspicious (credential obfuscation) |
| **FLAG-04** | `has_double_slash_redirect` | '//' in path (not scheme) | 1 = suspicious |
| **FLAG-05** | `has_prefix_suffix` | '-' in domain name | 1 = suspicious (e.g., paypal-verify) |
| **FLAG-06** | `uses_shortening_service` | Domain is URL shortener | 1 = suspicious (hides destination) |
| **FLAG-07** | `suspicious_tld` | TLD in suspicious list | 1 = suspicious |
| **FLAG-08** | `contains_suspicious_keywords` | 'verify', 'account', 'secure' | 1 = possible social engineering |
| **FLAG-09** | `abnormal_port` | Non-standard port (not 80/443) | 1 = suspicious |
| **FLAG-10** | `punycode_encoding` | Contains 'xn--' (IDN) | 1 = possible homograph attack |

---

#### 6.6.3.5 Optional External Features

These features require external API calls or lookups (computationally expensive).

| Feature ID | Feature Name | Data Source | Computation Cost | Implementation Priority |
|------------|--------------|-------------|------------------|----------------------|
| **EXT-01** | `domain_age_days` | WHOIS lookup | High (API call) | Low (optional) |
| **EXT-02** | `domain_registration_length` | WHOIS lookup | High (API call) | Low (optional) |
| **EXT-03** | `page_rank` | Google PageRank (deprecated) | High | Not recommended |
| **EXT-04** | `alexa_rank` | Alexa ranking service | Medium (API call) | Low (optional) |
| **EXT-05** | `dns_record_count` | DNS lookup | Medium | Low (optional) |
| **EXT-06** | `ssl_certificate_age` | SSL certificate check | Medium (HTTPS request) | Medium |
| **EXT-07** | `ssl_certificate_issuer` | Certificate authority | Medium | Medium |
| **EXT-08** | `google_safe_browsing` | Google Safe Browsing API | High (API call) | Low (rate limits) |

**Note**: External features are **NOT RECOMMENDED** for the v1.0 academic project due to:
- API rate limits and costs
- Increased latency (violates <200ms requirement)
- External dependency risks
- Privacy concerns (sending URLs to third parties)

---

#### 6.6.3.6 Feature Scaling and Normalization

**Requirement**: All features must be scaled to consistent ranges before model training.

**Scaling Methods**:

1. **StandardScaler** (Z-score normalization):
   ```
   X_scaled = (X - μ) / σ
   where μ = mean, σ = standard deviation
   ```
   - **Use case**: Features follow normal distribution
   - **Advantage**: Preserves outlier information
   - **Disadvantage**: Sensitive to outliers

2. **MinMaxScaler** (Range normalization):
   ```
   X_scaled = (X - X_min) / (X_max - X_min)
   ```
   - **Use case**: Features should be in [0, 1] range
   - **Advantage**: Bounded output range
   - **Disadvantage**: Sensitive to outliers

3. **RobustScaler** (Median-based):
   ```
   X_scaled = (X - median) / IQR
   where IQR = Q3 - Q1 (interquartile range)
   ```
   - **Use case**: Features contain outliers
   - **Advantage**: Robust to outliers
   - **Disadvantage**: Less interpretable

**Recommendation**: Use **StandardScaler** for most features, **MinMaxScaler** for binary flags (already in [0,1])

**Implementation**:
```python
from sklearn.preprocessing import StandardScaler
import joblib

# Fit scaler on training data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Save scaler for deployment
joblib.dump(scaler, 'models/feature_scaler.joblib')

# In production: load and apply scaler
scaler = joblib.load('models/feature_scaler.joblib')
X_new_scaled = scaler.transform(X_new)
```

---

### 6.6.4 Training Requirements

#### 6.6.4.1 Dataset Requirements

| Requirement | Specification | Rationale |
|-------------|---------------|-----------|
| **Minimum Dataset Size** | 50,000 URLs (25k phishing, 25k legitimate) | Sufficient for generalization |
| **Target Dataset Size** | 100,000+ URLs | Better model robustness |
| **Class Balance** | 50/50 or 40/60 (phishing/legitimate) | Prevent bias toward majority class |
| **Data Recency** | URLs from last 6-12 months | Capture current phishing trends |
| **Data Diversity** | Multiple phishing campaigns and legitimate domains | Prevent overfitting to specific patterns |
| **Label Quality** | Verified labels from trusted sources | Minimize label noise |
| **Duplicate Removal** | No duplicate URLs in dataset | Prevent data leakage |

#### Dataset Sources

| Source | Type | Approximate Size | Quality | Access Method |
|--------|------|------------------|---------|---------------|
| **PhishTank** | Phishing URLs | 100k+ verified phishing | High (community verified) | Public API / CSV download |
| **OpenPhish** | Phishing URLs | 50k+ active phishing | High (automated+manual) | Free feed / Premium API |
| **Alexa Top 1M** | Legitimate URLs | 1M popular sites | High (trusted sites) | Public download |
| **Common Crawl** | Legitimate URLs | Billions of pages | Medium (sampling needed) | Public S3 bucket |
| **UCI ML Repository** | Phishing dataset | 11,055 URLs (2016) | Medium (older data) | Public download |
| **APWG eCrime Exchange** | Phishing feeds | Variable | High | Membership required |

#### Data Split Strategy

```
Total Dataset (100,000 URLs)
        │
        ├── Training Set (70,000 URLs) ────► Model training
        │      - 35,000 phishing
        │      - 35,000 legitimate
        │
        ├── Validation Set (15,000 URLs) ──► Hyperparameter tuning
        │      - 7,500 phishing
        │      - 7,500 legitimate
        │
        └── Test Set (15,000 URLs) ────────► Final evaluation
               - 7,500 phishing
               - 7,500 legitimate

Stratified Splitting: Maintain class balance across all sets
```

---

#### 6.6.4.2 Data Preprocessing Pipeline

```python
import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_dataset(phishing_urls, legitimate_urls):
    """
    Preprocess URL dataset for model training
    
    Steps:
    1. Combine datasets with labels
    2. Remove duplicates
    3. Normalize URLs
    4. Handle missing values
    5. Validate URL format
    6. Split into train/val/test
    """
    # Combine datasets
    phishing_df = pd.DataFrame({
        'url': phishing_urls,
        'label': 1  # Phishing
    })
    legitimate_df = pd.DataFrame({
        'url': legitimate_urls,
        'label': 0  # Legitimate
    })
    df = pd.concat([phishing_df, legitimate_df], ignore_index=True)
    
    # Remove duplicates
    df = df.drop_duplicates(subset='url')
    print(f"Dataset size after deduplication: {len(df)}")
    
    # URL normalization
    df['url'] = df['url'].str.lower()
    df['url'] = df['url'].str.rstrip('/')
    
    # Remove malformed URLs
    df = df[df['url'].str.contains(r'^https?://', regex=True)]
    
    # Shuffle dataset
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Split dataset: 70-15-15
    train_df, temp_df = train_test_split(
        df, test_size=0.3, random_state=42, stratify=df['label']
    )
    val_df, test_df = train_test_split(
        temp_df, test_size=0.5, random_state=42, stratify=temp_df['label']
    )
    
    print(f"Training set: {len(train_df)} URLs")
    print(f"Validation set: {len(val_df)} URLs")
    print(f"Test set: {len(test_df)} URLs")
    
    return train_df, val_df, test_df
```

---

#### 6.6.4.3 Class Imbalance Handling

**Problem**: Real-world datasets may have imbalanced classes (e.g., 60% legitimate, 40% phishing)

**Solutions**:

| Technique | Method | Pros | Cons | Recommendation |
|-----------|--------|------|------|----------------|
| **SMOTE** | Synthetic Minority Oversampling | Creates realistic synthetic samples | May introduce noise | Use if imbalance >60/40 |
| **Random Undersampling** | Remove majority class samples | Simple, fast | Loses information | Not recommended |
| **Random Oversampling** | Duplicate minority samples | Simple | May cause overfitting | Not recommended |
| **Class Weights** | Adjust loss function | No data modification | Model-dependent | **Recommended** |
| **Ensemble Methods** | Balanced random forests | Built-in handling | More complex | Good for Random Forest |

**Recommended Approach: Class Weights in XGBoost**

```python
import xgboost as xgb
from sklearn.utils.class_weight import compute_sample_weight

# Calculate class weights
y_train = train_df['label']
sample_weights = compute_sample_weight(class_weight='balanced', y=y_train)

# Or manually:
n_samples = len(y_train)
n_positive = sum(y_train == 1)
n_negative = sum(y_train == 0)
scale_pos_weight = n_negative / n_positive

# Train with class weights
model = xgb.XGBClassifier(scale_pos_weight=scale_pos_weight)
model.fit(X_train, y_train)
```

---

#### 6.6.4.4 Cross-Validation Strategy

**Requirement**: Use k-fold stratified cross-validation to ensure robust model evaluation.

**Configuration**:
- **k = 5** (5-fold cross-validation)
- **Stratified**: Maintain class distribution in each fold
- **Shuffle**: Randomize data before splitting
- **Random State**: Set seed for reproducibility

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Define cross-validation strategy
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Evaluate model with cross-validation
scores = cross_val_score(
    model, X_train, y_train,
    cv=cv,
    scoring='f1',
    n_jobs=-1
)

print(f"Cross-validation F1 scores: {scores}")
print(f"Mean F1: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")
```

---

#### 6.6.4.5 Hyperparameter Optimization

**Method**: Randomized Search followed by Grid Search

**Step 1: Randomized Search (Broad Exploration)**
```python
from sklearn.model_selection import RandomizedSearchCV
import xgboost as xgb
from scipy.stats import randint, uniform

# Define parameter distributions
param_dist = {
    'n_estimators': randint(100, 300),
    'max_depth': randint(5, 15),
    'learning_rate': uniform(0.01, 0.2),
    'subsample': uniform(0.7, 0.3),
    'colsample_bytree': uniform(0.7, 0.3),
    'min_child_weight': randint(1, 5),
    'gamma': uniform(0, 0.2),
    'reg_alpha': uniform(0, 1),
    'reg_lambda': randint(1, 3)
}

# Randomized search
random_search = RandomizedSearchCV(
    xgb.XGBClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=50,
    scoring='f1',
    cv=5,
    random_state=42,
    n_jobs=-1,
    verbose=2
)

random_search.fit(X_train, y_train)
print(f"Best parameters: {random_search.best_params_}")
print(f"Best F1 score: {random_search.best_score_:.4f}")
```

**Step 2: Grid Search (Fine-tuning)**
```python
from sklearn.model_selection import GridSearchCV

# Define narrow parameter grid around best random search results
param_grid = {
    'n_estimators': [180, 200, 220],
    'max_depth': [6, 7, 8],
    'learning_rate': [0.08, 0.1, 0.12],
    'subsample': [0.75, 0.8, 0.85],
    'colsample_bytree': [0.75, 0.8, 0.85]
}

grid_search = GridSearchCV(
    xgb.XGBClassifier(random_state=42),
    param_grid=param_grid,
    scoring='f1',
    cv=5,
    n_jobs=-1,
    verbose=2
)

grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
```

---

### 6.6.5 Evaluation Metrics and Acceptance Criteria

#### 6.6.5.1 Primary Metrics

**Confusion Matrix**:
```
                  Predicted
                 Negative  Positive
Actual Negative    TN        FP
Actual Positive    FN        TP

Where:
- TN (True Negative): Correctly classified legitimate URLs
- FP (False Positive): Legitimate URLs incorrectly flagged as phishing
- FN (False Negative): Phishing URLs missed by the model
- TP (True Positive): Correctly detected phishing URLs
```

---

**Metric 1: Accuracy**

**Definition**: Overall correctness of the model

**Formula**:
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

**Target**: ≥ 95%

**Interpretation**:
- 95% accuracy means 95 out of 100 URLs are correctly classified
- Good general metric but can be misleading with imbalanced data

**Python Implementation**:
```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
```

---

**Metric 2: Precision**

**Definition**: Of all URLs predicted as phishing, how many are actually phishing?

**Formula**:
```
Precision = TP / (TP + FP)
```

**Target**: ≥ 93%

**Interpretation**:
- High precision means low false positive rate
- Critical for user experience (don't block legitimate sites)
- 93% precision means 7% of blocked sites are false positives

**Python Implementation**:
```python
from sklearn.metrics import precision_score

precision = precision_score(y_test, y_pred)
print(f"Precision: {precision:.4f}")
```

---

**Metric 3: Recall (Sensitivity, True Positive Rate)**

**Definition**: Of all actual phishing URLs, how many does the model detect?

**Formula**:
```
Recall = TP / (TP + FN)
```

**Target**: ≥ 95%

**Interpretation**:
- High recall means low false negative rate
- Critical for security (catch phishing sites)
- 95% recall means 5% of phishing sites slip through

**Python Implementation**:
```python
from sklearn.metrics import recall_score

recall = recall_score(y_test, y_pred)
print(f"Recall: {recall:.4f}")
```

---

**Metric 4: F1-Score**

**Definition**: Harmonic mean of precision and recall (balanced metric)

**Formula**:
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

**Target**: ≥ 94%

**Interpretation**:
- Balances precision and recall
- Good single metric for model selection
- More informative than accuracy for imbalanced data

**Python Implementation**:
```python
from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred)
print(f"F1-Score: {f1:.4f}")
```

---

**Metric 5: ROC-AUC (Area Under Receiver Operating Characteristic Curve)**

**Definition**: Measures the model's ability to distinguish between classes across all thresholds

**Formula**:
```
AUC = ∫ TPR d(FPR)

where:
TPR (True Positive Rate) = Recall = TP / (TP + FN)
FPR (False Positive Rate) = FP / (FP + TN)
```

**Target**: ≥ 0.97

**Interpretation**:
- AUC = 1.0: Perfect classifier
- AUC = 0.5: Random classifier
- AUC > 0.97: Excellent discrimination

**Python Implementation**:
```python
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Calculate AUC
y_proba = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_proba)
print(f"ROC-AUC: {auc:.4f}")

# Plot ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
plt.plot(fpr, tpr, label=f'XGBoost (AUC = {auc:.3f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.savefig('roc_curve.png')
```

---

#### 6.6.5.2 Evaluation Metrics Summary Table

| Metric | Formula | Target | Priority | Interpretation |
|--------|---------|--------|----------|----------------|
| **Accuracy** | (TP+TN)/(TP+TN+FP+FN) | ≥95% | High | Overall correctness |
| **Precision** | TP/(TP+FP) | ≥93% | Critical | Minimize false alarms |
| **Recall** | TP/(TP+FN) | ≥95% | Critical | Catch phishing sites |
| **F1-Score** | 2PR/(P+R) | ≥94% | Critical | Balanced metric |
| **ROC-AUC** | Area under ROC | ≥0.97 | High | Discrimination ability |
| **Specificity** | TN/(TN+FP) | ≥93% | Medium | True negative rate |
| **FPR** | FP/(FP+TN) | ≤7% | High | False positive rate |
| **FNR** | FN/(FN+TP) | ≤5% | Critical | False negative rate |

**Business Impact**:
- **False Positives** (FP): Frustrate users, reduce trust, productivity loss
- **False Negatives** (FN): Security risk, potential data breach, financial loss

**Balanced Trade-off**:
- Slightly favor **Recall over Precision** (better to warn unnecessarily than miss phishing)
- Target: Precision ≥93%, Recall ≥95%

---

#### 6.6.5.3 Comprehensive Evaluation Report

```python
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

def evaluate_model(model, X_test, y_test):
    """Generate comprehensive evaluation report"""
    
    # Predictions
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    # Classification report
    print("="*60)
    print("CLASSIFICATION REPORT")
    print("="*60)
    print(classification_report(y_test, y_pred, 
                                target_names=['Legitimate', 'Phishing']))
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("\n" + "="*60)
    print("CONFUSION MATRIX")
    print("="*60)
    print(cm)
    
    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Legitimate', 'Phishing'],
                yticklabels=['Legitimate', 'Phishing'])
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Confusion Matrix')
    plt.savefig('confusion_matrix.png')
    
    # Calculate metrics
    tn, fp, fn, tp = cm.ravel()
    
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    specificity = tn / (tn + fp)
    fpr = fp / (fp + tn)
    fnr = fn / (fn + tp)
    auc = roc_auc_score(y_test, y_proba)
    
    # Print metrics
    print("\n" + "="*60)
    print("PERFORMANCE METRICS")
    print("="*60)
    print(f"Accuracy:      {accuracy:.4f} (Target: ≥0.9500)")
    print(f"Precision:     {precision:.4f} (Target: ≥0.9300)")
    print(f"Recall:        {recall:.4f} (Target: ≥0.9500)")
    print(f"F1-Score:      {f1:.4f} (Target: ≥0.9400)")
    print(f"Specificity:   {specificity:.4f}")
    print(f"ROC-AUC:       {auc:.4f} (Target: ≥0.9700)")
    print(f"FPR:           {fpr:.4f} (Target: ≤0.0700)")
    print(f"FNR:           {fnr:.4f} (Target: ≤0.0500)")
    
    # Acceptance criteria check
    print("\n" + "="*60)
    print("ACCEPTANCE CRITERIA")
    print("="*60)
    print(f"✓ Accuracy ≥ 95%:    {'PASS' if accuracy >= 0.95 else 'FAIL'}")
    print(f"✓ Precision ≥ 93%:   {'PASS' if precision >= 0.93 else 'FAIL'}")
    print(f"✓ Recall ≥ 95%:      {'PASS' if recall >= 0.95 else 'FAIL'}")
    print(f"✓ F1-Score ≥ 94%:    {'PASS' if f1 >= 0.94 else 'FAIL'}")
    print(f"✓ ROC-AUC ≥ 0.97:    {'PASS' if auc >= 0.97 else 'FAIL'}")
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'auc': auc
    }
```

---

### 6.6.6 Model Explainability Requirements

Model explainability is critical for debugging, trust, and regulatory compliance.

#### 6.6.6.1 Feature Importance Analysis

**Requirement**: Identify which features contribute most to predictions.

**Method 1: XGBoost Built-in Feature Importance**

```python
import matplotlib.pyplot as plt

# Get feature importance
feature_importance = model.get_booster().get_score(importance_type='gain')

# Sort by importance
sorted_features = sorted(feature_importance.items(), 
                        key=lambda x: x[1], reverse=True)

# Plot top 20 features
features = [f[0] for f in sorted_features[:20]]
scores = [f[1] for f in sorted_features[:20]]

plt.figure(figsize=(10, 8))
plt.barh(features, scores)
plt.xlabel('Importance Score (Gain)')
plt.title('Top 20 Most Important Features')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('feature_importance.png')
```

**Importance Types**:
- **gain**: Average gain across all splits using the feature
- **weight**: Number of times feature is used in trees
- **cover**: Average coverage (number of samples affected)

---

**Method 2: SHAP (SHapley Additive exPlanations)**

**Requirement**: Provide instance-level explanations for individual predictions.

**SHAP Overview**:
- Based on game theory (Shapley values)
- Explains each prediction by attributing contribution to each feature
- Model-agnostic but optimized for tree-based models

**Implementation**:
```python
import shap

# Create SHAP explainer
explainer = shap.TreeExplainer(model)

# Calculate SHAP values for test set
shap_values = explainer.shap_values(X_test)

# Summary plot (global feature importance)
shap.summary_plot(shap_values, X_test, 
                  feature_names=feature_names,
                  max_display=20,
                  show=False)
plt.savefig('shap_summary.png', bbox_inches='tight')

# Force plot (individual prediction explanation)
shap.initjs()
shap.force_plot(explainer.expected_value, 
                shap_values[0], 
                X_test.iloc[0],
                feature_names=feature_names)
```

**SHAP Visualizations**:

1. **Summary Plot**: Shows feature importance and impact distribution
2. **Force Plot**: Explains individual prediction (feature contributions)
3. **Waterfall Plot**: Shows cumulative feature contributions
4. **Dependence Plot**: Shows relationship between feature value and SHAP value

**Example Interpretation**:
```
URL: https://secure-login.paypal-verify.tk/signin
Prediction: Phishing (Confidence: 0.94)

Top Contributing Features:
1. suspicious_tld (+0.45)        ← .tk domain is highly suspicious
2. domain_length (+0.22)         ← Long domain name
3. num_hyphens (+0.18)           ← Multiple hyphens in domain
4. contains_brand_name (+0.15)   ← "paypal" in suspicious context
5. subdomain_depth (+0.12)       ← Deep subdomain nesting
```

---

#### 6.6.6.2 Error Analysis

**Requirement**: Analyze misclassified examples to improve model.

```python
def analyze_errors(model, X_test, y_test, feature_names):
    """Analyze false positives and false negatives"""
    
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    # False positives (legitimate flagged as phishing)
    fp_indices = (y_pred == 1) & (y_test == 0)
    false_positives = X_test[fp_indices]
    fp_confidence = y_proba[fp_indices]
    
    print("="*60)
    print(f"FALSE POSITIVES: {len(false_positives)} cases")
    print("="*60)
    
    for i, (idx, conf) in enumerate(zip(false_positives.index[:5], fp_confidence[:5])):
        url = test_df.loc[idx, 'url']
        print(f"\n{i+1}. URL: {url}")
        print(f"   Confidence: {conf:.3f}")
        print(f"   Top features:")
        for feat, val in X_test.loc[idx].nlargest(5).items():
            print(f"     - {feat}: {val:.3f}")
    
    # False negatives (phishing missed)
    fn_indices = (y_pred == 0) & (y_test == 1)
    false_negatives = X_test[fn_indices]
    fn_confidence = 1 - y_proba[fn_indices]
    
    print("\n" + "="*60)
    print(f"FALSE NEGATIVES: {len(false_negatives)} cases")
    print("="*60)
    
    for i, (idx, conf) in enumerate(zip(false_negatives.index[:5], fn_confidence[:5])):
        url = test_df.loc[idx, 'url']
        print(f"\n{i+1}. URL: {url}")
        print(f"   Confidence (legitimate): {conf:.3f}")
        print(f"   Why missed: Likely has legitimate-looking features")
```

---

### 6.6.7 Model Persistence and Loading Strategy

#### 6.6.7.1 Model Serialization Requirements

**Requirement**: Trained models must be saved efficiently for deployment.

**Serialization Format**: **Joblib** (recommended for scikit-learn/XGBoost)

**Alternative**: Pickle (Python standard library, less efficient for large arrays)

**Files to Serialize**:
1. Trained model object
2. Feature scaler
3. Feature names (ordered list)
4. Model metadata (version, metrics, training date)

---

#### 6.6.7.2 Model Saving Implementation

```python
import joblib
import json
from datetime import datetime

def save_model_artifacts(model, scaler, feature_names, metrics, version='v1.0'):
    """
    Save all model artifacts for deployment
    
    Args:
        model: Trained XGBoost model
        scaler: Fitted StandardScaler
        feature_names: List of feature names (in order)
        metrics: Dictionary of evaluation metrics
        version: Model version string
    """
    
    # Create models directory
    import os
    os.makedirs('models', exist_ok=True)
    
    # Save model
    model_path = f'models/xgboost_{version}.pkl'
    joblib.dump(model, model_path)
    print(f"Model saved: {model_path}")
    
    # Save scaler
    scaler_path = f'models/scaler_{version}.joblib'
    joblib.dump(scaler, scaler_path)
    print(f"Scaler saved: {scaler_path}")
    
    # Save feature names
    features_path = f'models/features_{version}.json'
    with open(features_path, 'w') as f:
        json.dump({'features': feature_names}, f, indent=2)
    print(f"Features saved: {features_path}")
    
    # Save metadata
    metadata = {
        'version': version,
        'training_date': datetime.now().isoformat(),
        'model_type': 'XGBoost',
        'num_features': len(feature_names),
        'metrics': {
            'accuracy': float(metrics['accuracy']),
            'precision': float(metrics['precision']),
            'recall': float(metrics['recall']),
            'f1_score': float(metrics['f1']),
            'roc_auc': float(metrics['auc'])
        },
        'hyperparameters': model.get_params(),
        'feature_names': feature_names
    }
    
    metadata_path = f'models/metadata_{version}.json'
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"Metadata saved: {metadata_path}")
    
    # File size report
    model_size_mb = os.path.getsize(model_path) / (1024 * 1024)
    print(f"\nModel size: {model_size_mb:.2f} MB")
```

---

#### 6.6.7.3 Model Loading Implementation

```python
def load_model_artifacts(version='v1.0'):
    """
    Load all model artifacts for inference
    
    Returns:
        Dictionary containing model, scaler, features, metadata
    """
    
    # Load model
    model_path = f'models/xgboost_{version}.pkl'
    model = joblib.load(model_path)
    print(f"Model loaded: {model_path}")
    
    # Load scaler
    scaler_path = f'models/scaler_{version}.joblib'
    scaler = joblib.load(scaler_path)
    print(f"Scaler loaded: {scaler_path}")
    
    # Load feature names
    features_path = f'models/features_{version}.json'
    with open(features_path, 'r') as f:
        feature_data = json.load(f)
        feature_names = feature_data['features']
    print(f"Features loaded: {len(feature_names)} features")
    
    # Load metadata
    metadata_path = f'models/metadata_{version}.json'
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    print(f"Metadata loaded: {metadata_path}")
    print(f"Model metrics: Accuracy={metadata['metrics']['accuracy']:.4f}, "
          f"F1={metadata['metrics']['f1_score']:.4f}")
    
    return {
        'model': model,
        'scaler': scaler,
        'feature_names': feature_names,
        'metadata': metadata
    }
```

---

#### 6.6.7.4 Model Versioning Strategy

**Versioning Scheme**: Semantic Versioning (MAJOR.MINOR.PATCH)

- **MAJOR**: Breaking changes (different feature set, algorithm change)
- **MINOR**: Backward-compatible improvements (retrained model, hyperparameter tuning)
- **PATCH**: Bug fixes (no model change)

**Example Versions**:
- `v1.0.0`: Initial production model
- `v1.1.0`: Retrained with more data (same features)
- `v1.2.0`: Improved hyperparameters
- `v2.0.0`: New feature set or algorithm

**Version Storage Structure**:
```
models/
├── v1.0/
│   ├── xgboost_v1.0.pkl
│   ├── scaler_v1.0.joblib
│   ├── features_v1.0.json
│   └── metadata_v1.0.json
├── v1.1/
│   ├── xgboost_v1.1.pkl
│   ├── scaler_v1.1.joblib
│   ├── features_v1.1.json
│   └── metadata_v1.1.json
└── current -> v1.1/  (symlink to active version)
```

---

#### 6.6.7.5 Model Validation on Load

**Requirement**: Verify model integrity when loading.

```python
import hashlib

def validate_model(model_path, expected_checksum=None):
    """
    Validate model file integrity
    
    Args:
        model_path: Path to model file
        expected_checksum: Optional SHA256 checksum
    
    Returns:
        Boolean indicating if model is valid
    """
    
    # Check file exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    # Verify checksum if provided
    if expected_checksum:
        with open(model_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        
        if file_hash != expected_checksum:
            raise ValueError(f"Model checksum mismatch. "
                           f"Expected: {expected_checksum}, Got: {file_hash}")
    
    # Try loading model
    try:
        model = joblib.load(model_path)
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")
    
    # Verify model has required methods
    if not hasattr(model, 'predict') or not hasattr(model, 'predict_proba'):
        raise ValueError("Loaded object is not a valid classifier")
    
    print(f"✓ Model validation passed: {model_path}")
    return True
```

---

#### 6.6.7.6 Production Model Loading (FastAPI Integration)

```python
from fastapi import FastAPI
from contextlib import asynccontextmanager

# Global model storage
ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load model on startup, cleanup on shutdown"""
    
    # Startup: Load model
    print("Loading ML model...")
    try:
        artifacts = load_model_artifacts(version='v1.0')
        ml_models['model'] = artifacts['model']
        ml_models['scaler'] = artifacts['scaler']
        ml_models['feature_names'] = artifacts['feature_names']
        ml_models['metadata'] = artifacts['metadata']
        print("✓ Model loaded successfully")
    except Exception as e:
        print(f"✗ Failed to load model: {e}")
        raise
    
    yield  # Application runs
    
    # Shutdown: Cleanup
    ml_models.clear()
    print("Model unloaded")

app = FastAPI(lifespan=lifespan)

# Access model in endpoints
@app.post("/predict")
async def predict(request: URLRequest):
    model = ml_models['model']
    scaler = ml_models['scaler']
    # ... inference logic
```

---

### 6.6.8 Model Retraining Strategy

**Requirement**: Define process for periodic model updates.

**Retraining Triggers**:
1. **Performance Degradation**: Accuracy drops below 94%
2. **Time-Based**: Every 3-6 months to capture new phishing trends
3. **Data-Based**: New dataset with 10,000+ labeled URLs
4. **Feedback-Based**: 1,000+ user-reported false positives/negatives

**Retraining Pipeline**:
```
[1] Collect new data (phishing feeds, feedback)
[2] Merge with existing training data
[3] Preprocess and validate data quality
[4] Retrain model with updated dataset
[5] Evaluate on holdout test set
[6] Compare metrics with current production model
[7] If improved: Deploy new model
[8] If not: Analyze and iterate
```

---

## 6.7 Frontend Requirements Specification (Chrome Extension)

### 6.7.1 Frontend Overview

The frontend component is a Chrome browser extension built using Manifest V3, providing real-time phishing detection directly in the user's browsing experience. The extension acts as a lightweight client that intercepts navigation events, communicates with the backend API, and displays security warnings when necessary.

#### Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Extension Platform** | Chrome Extension API | Manifest V3 | Browser extension framework |
| **Programming Language** | JavaScript | ES6+ | Core extension logic |
| **Markup** | HTML5 | - | UI structure (popup, warning pages) |
| **Styling** | CSS3 | - | UI styling and animations |
| **Storage** | chrome.storage.local | Native API | Local data persistence |
| **Navigation** | chrome.webNavigation | Native API | URL interception |
| **HTTP Client** | Fetch API | Native | Backend API communication |
| **Async Operations** | Promises/Async-Await | ES6+ | Asynchronous programming |
| **Build Tools** | None (vanilla JS) | - | Simplicity for academic project |

#### Extension Architecture

```
Chrome Browser Process
├── Background Service Worker (persistent)
│   ├── Navigation event listeners
│   ├── API communication manager
│   ├── Cache management
│   └── Message routing
│
├── Content Scripts (injected per page)
│   ├── Warning banner injection
│   ├── DOM manipulation
│   └── User interaction handling
│
├── Popup Interface (on-demand)
│   ├── Statistics display
│   ├── Settings management
│   └── Whitelist editor
│
└── Warning Page (full page)
    ├── Phishing alert display
    ├── User decision interface
    └── Feedback collection
```

#### File Structure

```
chrome-extension/
├── manifest.json                # Extension configuration
├── background.js                # Service worker (main logic)
├── content-script.js            # Injected page scripts
├── popup/
│   ├── popup.html              # Popup interface
│   ├── popup.js                # Popup logic
│   └── popup.css               # Popup styling
├── warning/
│   ├── warning.html            # Full-page warning
│   ├── warning.js              # Warning page logic
│   └── warning.css             # Warning page styling
├── settings/
│   ├── settings.html           # Settings page
│   ├── settings.js             # Settings logic
│   └── settings.css            # Settings styling
├── assets/
│   ├── icon-16.png            # Extension icon (16x16)
│   ├── icon-48.png            # Extension icon (48x48)
│   ├── icon-128.png           # Extension icon (128x128)
│   ├── shield.svg             # Security shield icon
│   └── warning.svg            # Warning icon
├── utils/
│   ├── api-client.js          # Backend API wrapper
│   ├── cache-manager.js       # Local cache operations
│   └── constants.js           # Shared constants
└── README.md                   # Development documentation
```

---

### 6.7.2 User Flow Diagrams

#### 6.7.2.1 Primary User Flow: URL Navigation

```
┌─────────────────────────────────────────────────────────────────┐
│  USER ACTION: Navigates to URL (clicks link, types address)    │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│  EXTENSION: Background script intercepts navigation event       │
│  chrome.webNavigation.onBeforeNavigate                          │
└─────────────────────────────────────────────────────────────────┘
                            ↓
                    ┌───────┴───────┐
                    │  Is main frame? │ ──No──→ [Allow navigation]
                    └───────┬───────┘
                          Yes
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│  CHECK 1: Is URL whitelisted?                                   │
│  (User-added trusted domains)                                   │
└─────────────────────────────────────────────────────────────────┘
                            ↓
                    ┌───────┴───────┐
                    │  Whitelisted?   │ ──Yes──→ [Allow navigation]
                    └───────┬───────┘
                          No
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│  CHECK 2: Is result cached?                                     │
│  (Check local storage for recent classification)                │
└─────────────────────────────────────────────────────────────────┘
                            ↓
                    ┌───────┴───────┐
                    │  Cache hit?     │ ──Yes──→ [Use cached result]
                    └───────┬───────┘              ↓
                          No                       └─────┐
                            ↓                            │
┌─────────────────────────────────────────────────────────────────┐
│  API CALL: Send URL to backend /predict endpoint                │
│  POST /predict { "url": "..." }                                 │
└─────────────────────────────────────────────────────────────────┘
                            ↓
                    ┌───────┴───────┐
                    │  API Success?   │ ──No──→ [Handle error, allow with warning]
                    └───────┬───────┘
                          Yes
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│  CACHE: Store result locally (24hr TTL)                         │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│  DECISION: Determine action based on risk level                 │
└─────────────────────────────────────────────────────────────────┘
                            ↓
            ┌───────────────┴───────────────┐
            ↓                               ↓
    ┌──────────────┐              ┌──────────────┐
    │ HIGH RISK    │              │ MEDIUM RISK  │
    │ (conf≥80%)   │              │ (60-79%)     │
    └──────┬───────┘              └──────┬───────┘
           ↓                              ↓
┌──────────────────────┐      ┌──────────────────────┐
│ Block navigation     │      │ Allow with banner    │
│ Redirect to warning  │      │ Inject warning banner│
│ page                 │      │ into page            │
└──────────────────────┘      └──────────────────────┘
           ↓                              ↓
  ┌────────────────┐            ┌────────────────┐
  │ User sees full │            │ User sees      │
  │ page warning   │            │ top banner     │
  └────────┬───────┘            └────────┬───────┘
           ↓                              ↓
    ┌─────┴─────┐                  ┌─────┴─────┐
    │ Go Back   │                  │ Continue  │
    │ (default) │                  │ Browsing  │
    └───────────┘                  └───────────┘
           ↓
    ┌─────┴─────┐
    │ Continue  │
    │ Anyway    │
    │ (override)│
    └───────────┘
```

#### 6.7.2.2 User Flow: Extension Popup Interaction

```
USER: Clicks extension icon in toolbar
              ↓
┌─────────────────────────────────┐
│ Display popup.html              │
│ - Load statistics from storage  │
│ - Get current tab URL           │
│ - Check protection status       │
└─────────────────────────────────┘
              ↓
┌─────────────────────────────────┐
│ Popup Interface Displayed       │
│ ┌─────────────────────────────┐ │
│ │ Phishing Detector    ⚙️     │ │
│ ├─────────────────────────────┤ │
│ │ 🛡️ Protection: ON           │ │
│ │                             │ │
│ │ Today's Statistics:         │ │
│ │ ✓ URLs Checked: 127         │ │
│ │ ⚠️ Threats Blocked: 3       │ │
│ │ ℹ️ Warnings: 8              │ │
│ │                             │ │
│ │ Current Tab: ✓ Safe         │ │
│ │ example.com                 │ │
│ │                             │ │
│ │ [Whitelist Manager]         │ │
│ │ [Settings]                  │ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
              ↓
      ┌───────┴────────┐
      │ User Action?    │
      └───────┬────────┘
              ↓
    ┌─────────┼─────────────┐
    ↓         ↓             ↓
[Toggle   [Whitelist]  [Settings]
 Protection]
    ↓         ↓             ↓
 Update    Open          Open
 Setting   Whitelist     Settings
           Manager       Page
```

#### 6.7.2.3 User Flow: Whitelist Management

```
USER: Wants to trust a site flagged as phishing
              ↓
      ┌───────┴────────┐
      │ Entry Point?    │
      └───────┬────────┘
              ↓
    ┌─────────┼─────────────┐
    ↓                       ↓
[Warning Page]         [Popup Menu]
"Trust this site"      "Whitelist Manager"
    ↓                       ↓
    └───────────┬───────────┘
                ↓
┌─────────────────────────────────┐
│ Extract domain from URL         │
│ example.com                     │
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│ Show confirmation dialog        │
│ "Add example.com to whitelist?"│
└─────────────────────────────────┘
                ↓
        ┌───────┴────────┐
        │ User confirms?  │
        └───────┬────────┘
               Yes
                ↓
┌─────────────────────────────────┐
│ Add domain to whitelist         │
│ Save to chrome.storage.local    │
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│ Show success notification       │
│ "example.com added to whitelist"│
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│ Remove warning/allow navigation │
└─────────────────────────────────┘
```

---

### 6.7.3 Functional Requirements

#### 6.7.3.1 Core Detection Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-F01** | URL Interception | Critical | Extension shall intercept all navigation events before page load | Navigation events captured with <10ms overhead |
| **FR-F02** | Main Frame Detection | Critical | Extension shall only process main frame navigations, not iframes | Sub-frames ignored to prevent excessive API calls |
| **FR-F03** | Whitelist Check | Critical | Extension shall check URLs against user whitelist before API call | Whitelisted domains bypass all checks instantly |
| **FR-F04** | Cache Lookup | High | Extension shall check local cache for recent classifications | Cache lookup completes in <5ms |
| **FR-F05** | API Communication | Critical | Extension shall send URL to backend API when no cache hit | API call made within 50ms of navigation event |
| **FR-F06** | Response Parsing | Critical | Extension shall correctly parse API response (prediction, confidence) | All response fields extracted without errors |
| **FR-F07** | Risk Categorization | Critical | Extension shall determine action based on confidence threshold | High (≥80%), Medium (60-79%), Low (<60%) |
| **FR-F08** | Navigation Blocking | Critical | Extension shall block navigation to high-risk URLs | Page load prevented until user override |
| **FR-F09** | Warning Display | Critical | Extension shall display appropriate warnings based on risk level | Full-page for high risk, banner for medium risk |
| **FR-F10** | User Override | High | Users shall be able to proceed to blocked sites after warning | "Continue Anyway" button functional |

#### 6.7.3.2 User Interface Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-F11** | Extension Icon | High | Extension icon shall be visible in Chrome toolbar | Icon displayed in all browser windows |
| **FR-F12** | Popup Display | High | Clicking icon shall open popup with statistics and controls | Popup appears within 100ms of click |
| **FR-F13** | Statistics Tracking | Medium | Extension shall track and display URLs checked, threats blocked | Statistics persist across sessions |
| **FR-F14** | Current Tab Status | Medium | Popup shall show safety status of current tab | Real-time status indicator |
| **FR-F15** | Settings Access | Medium | Popup shall provide access to settings page | Settings page opens in new tab |
| **FR-F16** | Warning Page Design | Critical | Full-page warning shall be clear and professional | Meets WCAG 2.1 accessibility standards |
| **FR-F17** | Banner Injection | High | Medium-risk warnings shall appear as non-intrusive banner | Banner at top of page, easily dismissible |
| **FR-F18** | Action Buttons | Critical | All user actions shall have clearly labeled buttons | Button text unambiguous (e.g., "Go Back to Safety") |
| **FR-F19** | Visual Feedback | Medium | Extension shall provide visual feedback for all actions | Loading spinners, success/error messages |
| **FR-F20** | Responsive Design | Low | UI shall adapt to different window sizes | Popup usable from 300px width |

#### 6.7.3.3 Cache Management Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-F21** | Cache Storage | High | Extension shall cache URL classifications locally | Cached entries stored in chrome.storage.local |
| **FR-F22** | Cache TTL | High | Cached entries shall expire after 24 hours | Entries automatically invalidated after TTL |
| **FR-F23** | Cache Size Limit | Medium | Cache shall not exceed 5MB storage | Old entries purged when limit approached |
| **FR-F24** | Cache Lookup Speed | High | Cache lookups shall complete in <5ms | No noticeable delay in navigation |
| **FR-F25** | Cache Invalidation | Medium | Users shall be able to manually clear cache | "Clear Cache" button in settings |
| **FR-F26** | URL Hashing | High | URLs shall be hashed before caching (privacy) | SHA-256 hash used, not full URL |
| **FR-F27** | Cache Persistence | Medium | Cache shall persist across browser restarts | Storage survives extension updates |
| **FR-F28** | Cache Statistics | Low | Extension shall track cache hit rate | Hit rate displayed in settings (optional) |

#### 6.7.3.4 Whitelist Management Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-F29** | Whitelist Storage | Critical | Extension shall maintain list of trusted domains | Whitelist persists in chrome.storage.local |
| **FR-F30** | Add to Whitelist | High | Users shall be able to add domains to whitelist | "Trust This Site" button on warning page |
| **FR-F31** | Remove from Whitelist | Medium | Users shall be able to remove domains from whitelist | Whitelist manager UI with delete buttons |
| **FR-F32** | Whitelist UI | Medium | Popup shall provide access to whitelist manager | List of whitelisted domains with actions |
| **FR-F33** | Domain Extraction | High | Extension shall extract root domain from URLs | `subdomain.example.com` → `example.com` |
| **FR-F34** | Subdomain Handling | Medium | Whitelist shall apply to all subdomains | `example.com` whitelist includes `www.example.com` |
| **FR-F35** | Import/Export | Low | Users shall be able to import/export whitelist | JSON export/import functionality |
| **FR-F36** | Whitelist Validation | Medium | Extension shall validate domains before adding | Invalid domains rejected with error message |

#### 6.7.3.5 Settings Management Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-F37** | Protection Toggle | High | Users shall be able to enable/disable protection | Toggle in popup updates immediately |
| **FR-F38** | Sensitivity Settings | Medium | Users shall be able to adjust detection sensitivity | Low/Medium/High options (adjusts thresholds) |
| **FR-F39** | Notification Settings | Low | Users shall be able to enable/disable notifications | Chrome notification preferences |
| **FR-F40** | API Endpoint Config | Low | Users shall be able to change API endpoint (for self-hosting) | Custom URL input in advanced settings |
| **FR-F41** | Default Settings | High | Extension shall have sensible defaults on first install | Protection ON, Medium sensitivity |
| **FR-F42** | Settings Persistence | High | Settings shall persist across browser restarts | Stored in chrome.storage.sync |
| **FR-F43** | Settings Export | Low | Users shall be able to export settings | JSON export for backup |
| **FR-F44** | Settings Reset | Low | Users shall be able to reset to defaults | "Reset to Default" button |

#### 6.7.3.6 Error Handling Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-F45** | Network Error Handling | Critical | Extension shall handle API unavailability gracefully | Allow navigation with warning banner |
| **FR-F46** | Timeout Handling | High | Extension shall timeout API calls after 5 seconds | Navigation not blocked indefinitely |
| **FR-F47** | Invalid Response Handling | High | Extension shall handle malformed API responses | Error logged, user allowed to proceed |
| **FR-F48** | Rate Limit Handling | Medium | Extension shall detect and handle 429 responses | Show "Service busy" message, use cache |
| **FR-F49** | Error Notifications | Medium | Extension shall notify users of errors | Non-intrusive error messages |
| **FR-F50** | Offline Mode | Medium | Extension shall function in degraded mode when offline | Use cached results, whitelist only |
| **FR-F51** | Error Logging | Low | Extension shall log errors for debugging | Console.log with structured format |
| **FR-F52** | Retry Logic | Medium | Extension shall retry failed API calls once | Exponential backoff before retry |

#### 6.7.3.7 Performance Requirements

| ID | Requirement | Priority | Description | Acceptance Criteria |
|----|-------------|----------|-------------|---------------------|
| **FR-F53** | Load Time Impact | Critical | Extension shall not noticeably slow page loads | <100ms overhead for legitimate sites |
| **FR-F54** | Memory Usage | High | Extension shall use <50MB RAM | Memory measured via Chrome Task Manager |
| **FR-F55** | CPU Usage | Medium | Extension shall use minimal CPU when idle | <1% CPU when not processing requests |
| **FR-F56** | Storage Usage | Medium | Extension shall use <10MB disk space | Includes cache, settings, whitelist |
| **FR-F57** | Popup Load Time | High | Popup shall open in <100ms | Measured from click to display |
| **FR-F58** | API Call Optimization | High | Extension shall minimize redundant API calls | Cache hit rate >80% for repeat visits |
| **FR-F59** | Background Worker | High | Service worker shall not impact browser performance | No memory leaks, efficient event handling |
| **FR-F60** | Batch Operations | Low | Extension shall batch multiple operations when possible | e.g., batch cache cleanup |

---

### 6.7.4 UI/UX Requirements

#### 6.7.4.1 Design Principles

| Principle | Description | Implementation |
|-----------|-------------|----------------|
| **Clarity** | Information should be immediately understandable | Clear language, no jargon, prominent headings |
| **Safety-First** | Default actions should prioritize user security | "Go Back" as primary button, "Continue" as secondary |
| **Non-Intrusive** | Warnings should not disrupt legitimate browsing | Medium-risk sites use subtle banners |
| **Accessibility** | UI should be usable by all users | WCAG 2.1 AA compliance, keyboard navigation |
| **Consistency** | Design patterns consistent across all screens | Uniform color scheme, typography, button styles |
| **Performance** | UI should respond instantly to user actions | <100ms response time for all interactions |

#### 6.7.4.2 Color Scheme

| Color | Hex Code | Usage | Meaning |
|-------|----------|-------|---------|
| **Primary (Blue)** | `#2563EB` | Extension icon, primary actions | Trust, security |
| **Success (Green)** | `#10B981` | Safe status indicators, success messages | Safe, legitimate |
| **Warning (Yellow)** | `#F59E0B` | Medium-risk warnings, cautionary messages | Caution, attention |
| **Danger (Red)** | `#DC2626` | High-risk warnings, error messages | Danger, threat |
| **Neutral (Gray)** | `#6B7280` | Secondary text, borders, disabled states | Neutral, inactive |
| **Background** | `#FFFFFF` | Page backgrounds, popup background | Clean, professional |
| **Text** | `#1F2937` | Primary text color | Readable, high contrast |

**Accessibility Requirements**:
- All color combinations must meet WCAG 2.1 AA contrast ratio (4.5:1 for normal text)
- Color should not be the only means of conveying information (use icons + text)

#### 6.7.4.3 Typography

| Element | Font | Size | Weight | Usage |
|---------|------|------|--------|-------|
| **Heading 1** | System font stack | 24px | 700 (Bold) | Page titles |
| **Heading 2** | System font stack | 20px | 600 (Semi-bold) | Section headers |
| **Heading 3** | System font stack | 18px | 600 (Semi-bold) | Sub-sections |
| **Body Text** | System font stack | 14px | 400 (Regular) | General content |
| **Small Text** | System font stack | 12px | 400 (Regular) | Captions, metadata |
| **Button Text** | System font stack | 14px | 600 (Semi-bold) | Action buttons |
| **Monospace** | Consolas, Monaco | 13px | 400 (Regular) | URLs, code |

**System Font Stack**:
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, 
             "Helvetica Neue", Arial, sans-serif;
```

#### 6.7.4.4 Extension Popup UI Specification

**Dimensions**: 320px width × 480px height

**Layout Structure**:
```
┌─────────────────────────────────────────┐
│ Header (60px)                           │
│ ┌─────────┐  Phishing Detector   ⚙️    │
│ │ 🛡️ Icon │                             │
│ └─────────┘                             │
├─────────────────────────────────────────┤
│ Protection Status (80px)                │
│ ┌─────────────────────────────────────┐ │
│ │ 🛡️ Protection: ON    [Toggle]       │ │
│ │ Real-time phishing detection active │ │
│ └─────────────────────────────────────┘ │
├─────────────────────────────────────────┤
│ Statistics Section (120px)              │
│ Today's Activity:                       │
│ ✓ URLs Checked: 127                     │
│ ⚠️ Threats Blocked: 3                    │
│ ℹ️ Warnings Shown: 8                     │
│ 📊 Cache Hit Rate: 84%                   │
├─────────────────────────────────────────┤
│ Current Tab Status (100px)              │
│ ┌─────────────────────────────────────┐ │
│ │ Current Page:                       │ │
│ │ ✓ Safe                              │ │
│ │ https://example.com                 │ │
│ │ Last checked: 2 minutes ago         │ │
│ └─────────────────────────────────────┘ │
├─────────────────────────────────────────┤
│ Quick Actions (100px)                   │
│ [📋 Whitelist Manager]                  │
│ [🔧 Settings]                           │
│ [🗑️ Clear Cache]                        │
├─────────────────────────────────────────┤
│ Footer (40px)                           │
│ Version 1.0 | Report Issue              │
└─────────────────────────────────────────┘
```

**Interactive Elements**:
- **Protection Toggle**: Switch component (ON/OFF)
- **Statistics**: Display-only, updates in real-time
- **Quick Action Buttons**: Hover effect, click to navigate
- **Settings Icon**: Opens settings in new tab

#### 6.7.4.5 Warning Page UI Specification

**Full-Page Warning (High Risk)**:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                         🛡️                              │
│                                                         │
│              PHISHING THREAT DETECTED                   │
│                                                         │
│   This site has been identified as a phishing attempt  │
│   and may steal your personal information.              │
│                                                         │
│   ┌───────────────────────────────────────────────┐   │
│   │ Suspicious URL:                               │   │
│   │ https://secure-login.paypal-verify.tk/signin  │   │
│   │                                               │   │
│   │ Detection Confidence: 94%                     │   │
│   │ Risk Level: HIGH                              │   │
│   └───────────────────────────────────────────────┘   │
│                                                         │
│   ┌───────────────────────────────────────────────┐   │
│   │ Why is this dangerous?                        │   │
│   │                                               │   │
│   │ • Domain uses suspicious TLD (.tk)            │   │
│   │ • Contains brand name in subdomain            │   │
│   │ • Multiple hyphens in domain name             │   │
│   │ • No HTTPS encryption                         │   │
│   └───────────────────────────────────────────────┘   │
│                                                         │
│           ┌──────────────────────────────┐            │
│           │   ← Go Back to Safety        │            │
│           │      (Recommended)           │            │
│           └──────────────────────────────┘            │
│                                                         │
│               Continue Anyway                          │
│            (Not Recommended)                           │
│                                                         │
│         [✓] Trust this site (Add to whitelist)        │
│         [⚠️] Report False Positive                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Design Specifications**:
- **Background**: White (`#FFFFFF`)
- **Icon**: Large red shield (96px × 96px)
- **Heading**: 32px, bold, red (`#DC2626`)
- **Body Text**: 16px, gray (`#6B7280`)
- **URL Display**: Monospace font, light gray background
- **Primary Button**: Green, large (200px × 50px)
- **Secondary Link**: Gray text, underlined
- **Checkboxes**: Standard Chrome checkboxes

#### 6.7.4.6 Warning Banner UI Specification

**In-Page Banner (Medium Risk)**:

```
┌──────────────────────────────────────────────────────────┐
│ ⚠️  This site may be suspicious (Confidence: 72%)        │
│     Proceed with caution. Avoid entering passwords.      │
│     [Trust This Site] [Learn More] [×]                   │
└──────────────────────────────────────────────────────────┘
```

**Design Specifications**:
- **Position**: Fixed at top of page (`position: fixed; top: 0;`)
- **Width**: 100% viewport width
- **Height**: 60px
- **Background**: Yellow (`#FEF3C7`)
- **Border**: Bottom border, orange (`#F59E0B`)
- **Z-index**: 999999 (above all page content)
- **Text**: 14px, dark gray (`#78350F`)
- **Buttons**: Small, inline, subtle styling
- **Close Button**: Top-right corner (× icon)

**Behavior**:
- Slides down from top with animation (300ms ease-in-out)
- Dismissible by clicking (×) button
- Persists until user action or page navigation

#### 6.7.4.7 Settings Page UI Specification

**Layout**:
```
┌─────────────────────────────────────────────────┐
│ ⚙️ Phishing Detector Settings                   │
├─────────────────────────────────────────────────┤
│                                                 │
│ General Settings                                │
│ ┌─────────────────────────────────────────────┐│
│ │ [✓] Enable real-time protection             ││
│ │ [✓] Show notifications                      ││
│ │ [ ] Send anonymous usage statistics         ││
│ └─────────────────────────────────────────────┘│
│                                                 │
│ Detection Sensitivity                           │
│ ┌─────────────────────────────────────────────┐│
│ │ ( ) Low    (•) Medium    ( ) High           ││
│ │                                             ││
│ │ Medium: Balanced protection (recommended)   ││
│ └─────────────────────────────────────────────┘│
│                                                 │
│ Cache Settings                                  │
│ ┌─────────────────────────────────────────────┐│
│ │ [✓] Enable cache (faster, less API calls)   ││
│ │ Cache duration: [24] hours                  ││
│ │ Cache size: 2.3 MB / 5 MB                   ││
│ │ [Clear Cache]                               ││
│ └─────────────────────────────────────────────┘│
│                                                 │
│ Advanced Settings                               │
│ ┌─────────────────────────────────────────────┐│
│ │ API Endpoint:                               ││
│ │ [https://api.phishingdetector.com/v1]      ││
│ │                                             ││
│ │ Confidence Thresholds:                      ││
│ │ Block (High Risk): [80]%                    ││
│ │ Warn (Medium Risk): [60]%                   ││
│ └─────────────────────────────────────────────┘│
│                                                 │
│ [Save Changes]  [Reset to Defaults]            │
└─────────────────────────────────────────────────┘
```

---

### 6.7.5 API Integration Details

#### 6.7.5.1 API Client Architecture

**File**: `utils/api-client.js`

```javascript
/**
 * API Client for backend communication
 * Handles request formation, error handling, and response parsing
 */

class PhishingAPIClient {
    constructor(baseURL = 'https://api.phishingdetector.com/v1') {
        this.baseURL = baseURL;
        this.timeout = 5000; // 5 seconds
    }

    /**
     * Classify a URL using the backend API
     * @param {string} url - URL to classify
     * @returns {Promise<Object>} Classification result
     */
    async classifyURL(url) {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), this.timeout);

        try {
            const response = await fetch(`${this.baseURL}/predict`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'User-Agent': 'PhishingDetector-Extension/1.0'
                },
                body: JSON.stringify({
                    url: url,
                    include_features: false
                }),
                signal: controller.signal
            });

            clearTimeout(timeoutId);

            // Handle different status codes
            if (response.status === 429) {
                throw new APIRateLimitError('Rate limit exceeded');
            }

            if (!response.ok) {
                const errorData = await response.json();
                throw new APIError(
                    errorData.error?.message || 'API request failed',
                    response.status
                );
            }

            const data = await response.json();
            return this.parseResponse(data);

        } catch (error) {
            if (error.name === 'AbortError') {
                throw new APITimeoutError('Request timeout');
            }
            throw error;
        }
    }

    /**
     * Parse API response into standard format
     */
    parseResponse(data) {
        return {
            url: data.data.url,
            prediction: data.data.prediction, // 'phishing' or 'legitimate'
            confidence: data.data.confidence, // 0.0 - 1.0
            riskLevel: data.data.risk_level,  // 'safe', 'low', 'medium', 'high'
            timestamp: data.data.timestamp,
            modelVersion: data.data.model_version
        };
    }

    /**
     * Check API health
     */
    async healthCheck() {
        try {
            const response = await fetch(`${this.baseURL}/health`, {
                method: 'GET',
                timeout: 3000
            });
            return response.ok;
        } catch {
            return false;
        }
    }
}

// Custom error classes
class APIError extends Error {
    constructor(message, statusCode) {
        super(message);
        this.name = 'APIError';
        this.statusCode = statusCode;
    }
}

class APITimeoutError extends Error {
    constructor(message) {
        super(message);
        this.name = 'APITimeoutError';
    }
}

class APIRateLimitError extends Error {
    constructor(message) {
        super(message);
        this.name = 'APIRateLimitError';
    }
}

export { PhishingAPIClient, APIError, APITimeoutError, APIRateLimitError };
```

#### 6.7.5.2 Request Flow with Retry Logic

```javascript
/**
 * Make API request with retry logic
 */
async function classifyWithRetry(url, maxRetries = 1) {
    let lastError;
    
    for (let attempt = 0; attempt <= maxRetries; attempt++) {
        try {
            const result = await apiClient.classifyURL(url);
            return result;
            
        } catch (error) {
            lastError = error;
            
            // Don't retry on rate limit or client errors
            if (error instanceof APIRateLimitError || 
                (error.statusCode && error.statusCode < 500)) {
                throw error;
            }
            
            // Wait before retry (exponential backoff)
            if (attempt < maxRetries) {
                const delay = Math.pow(2, attempt) * 1000; // 1s, 2s, 4s...
                await new Promise(resolve => setTimeout(resolve, delay));
            }
        }
    }
    
    // All retries failed
    throw lastError;
}
```

#### 6.7.5.3 API Configuration Management

```javascript
/**
 * Load API configuration from storage
 */
async function getAPIConfig() {
    const defaults = {
        endpoint: 'https://api.phishingdetector.com/v1',
        timeout: 5000,
        retries: 1
    };
    
    const stored = await chrome.storage.local.get('apiConfig');
    return { ...defaults, ...stored.apiConfig };
}

/**
 * Update API configuration
 */
async function updateAPIConfig(config) {
    await chrome.storage.local.set({ apiConfig: config });
}
```

---

### 6.7.6 Error Handling Behavior

#### 6.7.6.1 Error Handling Strategy

| Error Type | User Impact | Extension Behavior | User Message |
|------------|-------------|-------------------|--------------|
| **API Unavailable** | Low | Allow navigation, show warning banner | "Protection temporarily unavailable. Proceed with caution." |
| **Network Timeout** | Low | Allow navigation, log error | "Unable to verify URL. Please check your connection." |
| **Rate Limit (429)** | Medium | Use cache if available, else allow | "Service busy. Verification skipped for this request." |
| **Invalid Response** | Low | Allow navigation, log error | "Verification error occurred. Navigation allowed." |
| **Malformed URL** | None | Skip processing | No message (invalid URLs ignored) |
| **Storage Error** | Low | Function without cache | "Cache unavailable. Performance may be affected." |
| **Permission Denied** | High | Warn user, degrade functionality | "Extension permissions required. Please reinstall." |

#### 6.7.6.2 Error Handling Implementation

```javascript
/**
 * Central error handler for background script
 */
function handleClassificationError(error, url, tabId) {
    console.error('[Phishing Detector] Error:', error.message, error);
    
    // Log to analytics (if enabled)
    logError(error.name, error.message);
    
    // Determine user-facing behavior
    switch (error.name) {
        case 'APITimeoutError':
            showWarningBanner(tabId, {
                message: 'Unable to verify this site. Connection timeout.',
                severity: 'warning',
                action: 'proceed-caution'
            });
            allowNavigation(tabId);
            break;
            
        case 'APIRateLimitError':
            // Check if we have cached result
            const cached = await checkCache(url);
            if (cached) {
                handleCachedResult(cached, tabId);
            } else {
                showWarningBanner(tabId, {
                    message: 'Protection service busy. Verification skipped.',
                    severity: 'info',
                    action: 'proceed-caution'
                });
                allowNavigation(tabId);
            }
            break;
            
        case 'APIError':
            if (error.statusCode >= 500) {
                // Server error - allow with warning
                showWarningBanner(tabId, {
                    message: 'Verification service error. Proceed with caution.',
                    severity: 'warning'
                });
            }
            allowNavigation(tabId);
            break;
            
        default:
            // Unknown error - fail open (allow navigation)
            allowNavigation(tabId);
            break;
    }
}

/**
 * Error logging for debugging
 */
function logError(errorType, message) {
    const errorLog = {
        timestamp: new Date().toISOString(),
        type: errorType,
        message: message,
        userAgent: navigator.userAgent
    };
    
    // Store in local storage (up to last 100 errors)
    chrome.storage.local.get('errorLog', (data) => {
        const log = data.errorLog || [];
        log.push(errorLog);
        if (log.length > 100) log.shift(); // Keep only last 100
        chrome.storage.local.set({ errorLog: log });
    });
}
```

#### 6.7.6.3 User-Facing Error Messages

**Design Guidelines**:
- **Clear Language**: Avoid technical jargon
- **Actionable**: Tell users what to do next
- **Non-Alarming**: Don't cause panic for minor errors
- **Consistent Tone**: Professional but friendly

**Examples**:

```javascript
const ERROR_MESSAGES = {
    network: {
        title: 'Connection Issue',
        message: 'Unable to verify this site due to network problems.',
        action: 'You can proceed, but be cautious about entering sensitive information.',
        icon: '⚠️'
    },
    
    timeout: {
        title: 'Verification Timeout',
        message: 'The security check took too long to complete.',
        action: 'The site has been allowed. If you\'re unsure, close this tab.',
        icon: 'ℹ️'
    },
    
    rateLimit: {
        title: 'Service Busy',
        message: 'Too many verification requests at this time.',
        action: 'Protection temporarily limited. Avoid suspicious sites.',
        icon: '⏳'
    },
    
    serverError: {
        title: 'Service Error',
        message: 'The verification service encountered an error.',
        action: 'Protection temporarily unavailable. Exercise caution.',
        icon: '⚠️'
    },
    
    invalidResponse: {
        title: 'Unexpected Response',
        message: 'Received invalid data from verification service.',
        action: 'Site allowed by default. Report this issue if it persists.',
        icon: '⚠️'
    }
};
```

---

### 6.7.7 Performance Requirements

#### 6.7.7.1 Performance Metrics and Targets

| Metric | Target | Priority | Measurement Method |
|--------|--------|----------|-------------------|
| **Navigation Overhead** | <100ms | Critical | Time from event to API call |
| **Cache Lookup Time** | <5ms | High | Storage retrieval duration |
| **Popup Load Time** | <100ms | High | Click to visible UI |
| **Warning Page Load** | <200ms | Medium | Redirect to full display |
| **Memory Usage (Idle)** | <20MB | Medium | Chrome Task Manager |
| **Memory Usage (Active)** | <50MB | High | Chrome Task Manager |
| **CPU Usage (Idle)** | <1% | Medium | Chrome Task Manager |
| **CPU Usage (Active)** | <5% | Medium | During API calls |
| **Storage Usage** | <10MB | Low | chrome.storage.local.getBytesInUse() |
| **API Call Frequency** | <10/min | High | Request counter |

#### 6.7.7.2 Performance Optimization Strategies

**1. Cache Optimization**
```javascript
/**
 * Efficient cache implementation with TTL
 */
class URLCache {
    constructor(ttlHours = 24) {
        this.ttl = ttlHours * 60 * 60 * 1000; // Convert to milliseconds
        this.maxSize = 1000; // Maximum cached entries
    }

    /**
     * Get cached result with TTL check
     */
    async get(url) {
        const hash = await this.hashURL(url);
        const data = await chrome.storage.local.get(`cache_${hash}`);
        
        if (!data[`cache_${hash}`]) return null;
        
        const cached = data[`cache_${hash}`];
        const age = Date.now() - cached.timestamp;
        
        // Check if expired
        if (age > this.ttl) {
            await this.remove(url);
            return null;
        }
        
        return cached.result;
    }

    /**
     * Store result in cache
     */
    async set(url, result) {
        const hash = await this.hashURL(url);
        const entry = {
            result: result,
            timestamp: Date.now()
        };
        
        await chrome.storage.local.set({ [`cache_${hash}`]: entry });
        
        // Check cache size and cleanup if needed
        await this.cleanupIfNeeded();
    }

    /**
     * Hash URL for privacy (don't store full URLs)
     */
    async hashURL(url) {
        const encoder = new TextEncoder();
        const data = encoder.encode(url);
        const hashBuffer = await crypto.subtle.digest('SHA-256', data);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }

    /**
     * Cleanup old entries if cache too large
     */
    async cleanupIfNeeded() {
        const storage = await chrome.storage.local.get(null);
        const cacheKeys = Object.keys(storage).filter(k => k.startsWith('cache_'));
        
        if (cacheKeys.length > this.maxSize) {
            // Remove oldest 20% of entries
            const toRemove = Math.floor(cacheKeys.length * 0.2);
            const entries = await Promise.all(
                cacheKeys.map(async key => ({
                    key,
                    timestamp: storage[key].timestamp
                }))
            );
            
            entries.sort((a, b) => a.timestamp - b.timestamp);
            const keysToRemove = entries.slice(0, toRemove).map(e => e.key);
            
            await chrome.storage.local.remove(keysToRemove);
        }
    }
}
```

**2. Debouncing and Throttling**
```javascript
/**
 * Debounce function to limit rapid-fire events
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Throttle API calls to prevent rate limiting
 */
class APIThrottler {
    constructor(maxCallsPerMinute = 100) {
        this.maxCalls = maxCallsPerMinute;
        this.calls = [];
    }

    async canMakeCall() {
        const now = Date.now();
        const oneMinuteAgo = now - 60000;
        
        // Remove calls older than 1 minute
        this.calls = this.calls.filter(time => time > oneMinuteAgo);
        
        if (this.calls.length >= this.maxCalls) {
            return false;
        }
        
        this.calls.push(now);
        return true;
    }
}
```

**3. Lazy Loading**
```javascript
/**
 * Lazy load non-critical components
 */
async function initializeExtension() {
    // Load critical components immediately
    await loadCache();
    await loadWhitelist();
    await loadSettings();
    
    // Defer non-critical loads
    setTimeout(() => {
        loadStatistics();
        cleanupOldLogs();
    }, 5000);
}
```

**4. Efficient DOM Manipulation**
```javascript
/**
 * Inject warning banner efficiently
 */
function injectWarningBanner(message, severity) {
    // Create banner element once
    const banner = document.createElement('div');
    banner.id = 'phishing-detector-banner';
    banner.className = `pd-banner pd-banner-${severity}`;
    
    // Use template literal for faster rendering
    banner.innerHTML = `
        <div class="pd-banner-content">
            <span class="pd-icon">${severityIcon(severity)}</span>
            <span class="pd-message">${escapeHTML(message)}</span>
            <button class="pd-close" aria-label="Close">×</button>
        </div>
    `;
    
    // Inject at top of body (single DOM operation)
    document.body.insertAdjacentElement('afterbegin', banner);
    
    // Attach event listener
    banner.querySelector('.pd-close').addEventListener('click', () => {
        banner.remove();
    });
}
```

#### 6.7.7.3 Performance Monitoring

```javascript
/**
 * Performance monitoring utility
 */
class PerformanceMonitor {
    constructor() {
        this.metrics = {
            apiCalls: [],
            cacheHits: 0,
            cacheMisses: 0,
            navigationOverhead: []
        };
    }

    /**
     * Record API call duration
     */
    recordAPICall(duration) {
        this.metrics.apiCalls.push(duration);
        if (this.metrics.apiCalls.length > 100) {
            this.metrics.apiCalls.shift();
        }
    }

    /**
     * Record cache performance
     */
    recordCacheHit() {
        this.metrics.cacheHits++;
    }

    recordCacheMiss() {
        this.metrics.cacheMisses++;
    }

    /**
     * Get performance statistics
     */
    getStats() {
        const avgAPITime = this.metrics.apiCalls.length > 0
            ? this.metrics.apiCalls.reduce((a, b) => a + b, 0) / this.metrics.apiCalls.length
            : 0;
        
        const cacheHitRate = (this.metrics.cacheHits + this.metrics.cacheMisses) > 0
            ? (this.metrics.cacheHits / (this.metrics.cacheHits + this.metrics.cacheMisses)) * 100
            : 0;
        
        return {
            avgAPICallTime: Math.round(avgAPITime),
            cacheHitRate: Math.round(cacheHitRate),
            totalAPICalls: this.metrics.apiCalls.length
        };
    }
}
```

---

## 7. Functional Requirements

### 7.1 Chrome Extension Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| FR-EXT-001 | URL Interception | Critical | Extension shall intercept all navigation events before page load |
| FR-EXT-002 | API Communication | Critical | Extension shall send URL to backend API and receive classification |
| FR-EXT-003 | Warning Display | Critical | Extension shall display blocking page for phishing URLs (confidence >80%) |
| FR-EXT-004 | Advisory Display | High | Extension shall show warning banner for suspicious URLs (confidence 60-80%) |
| FR-EXT-005 | User Override | High | Users shall be able to proceed despite warning (informed consent) |
| FR-EXT-006 | Whitelist Management | Medium | Users shall be able to add/remove trusted domains |
| FR-EXT-007 | Settings Interface | Medium | Extension shall provide settings page for configuration |
| FR-EXT-008 | Statistics Display | Low | Extension shall show detection statistics in popup |
| FR-EXT-009 | Cache Management | High | Extension shall cache recent classifications for 24 hours |
| FR-EXT-010 | Offline Mode | Medium | Extension shall function in degraded mode without API access |

### 7.2 Backend API Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| FR-API-001 | URL Classification | Critical | API shall accept URL and return classification (phishing/legitimate) |
| FR-API-002 | Confidence Scoring | Critical | API shall return confidence score (0-100%) with classification |
| FR-API-003 | Feature Extraction | Critical | API shall extract 30+ features from URL string |
| FR-API-004 | Model Loading | Critical | API shall load pre-trained ML model on startup |
| FR-API-005 | Health Check | High | API shall provide /health endpoint for monitoring |
| FR-API-006 | Request Validation | High | API shall validate input URLs and reject malformed requests |
| FR-API-007 | Error Handling | High | API shall return meaningful error messages for failures |
| FR-API-008 | Logging | Medium | API shall log all requests for monitoring and debugging |
| FR-API-009 | Model Versioning | Low | API shall support multiple model versions |
| FR-API-010 | Feedback Collection | Low | API shall accept user feedback on classifications |

### 7.3 Machine Learning Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| FR-ML-001 | Model Accuracy | Critical | Model shall achieve ≥95% accuracy on test dataset |
| FR-ML-002 | False Positive Rate | Critical | Model shall maintain ≤5% false positive rate |
| FR-ML-003 | Feature Engineering | Critical | System shall extract lexical, host-based, and URL structure features |
| FR-ML-004 | Model Training | High | Training pipeline shall support XGBoost and Random Forest algorithms |
| FR-ML-005 | Model Evaluation | High | System shall provide precision, recall, F1-score, ROC-AUC metrics |
| FR-ML-006 | Cross-Validation | High | Training shall use k-fold cross-validation (k=5) |
| FR-ML-007 | Model Serialization | High | Trained models shall be serialized for deployment |
| FR-ML-008 | Imbalanced Data Handling | Medium | Training shall handle class imbalance using appropriate techniques |
| FR-ML-009 | Hyperparameter Tuning | Medium | System shall support automated hyperparameter optimization |
| FR-ML-010 | Model Interpretability | Low | System should provide feature importance analysis |

---

## 8. Non-Functional Requirements

### 8.1 Performance Requirements

| ID | Requirement | Target Metric | Priority |
|----|-------------|---------------|----------|
| NFR-PERF-001 | API Response Time | <200ms (95th percentile) | Critical |
| NFR-PERF-002 | End-to-End Latency | <500ms (extension + API) | Critical |
| NFR-PERF-003 | Extension Load Time | <100ms | High |
| NFR-PERF-004 | Model Inference Time | <50ms per prediction | High |
| NFR-PERF-005 | Concurrent Requests | Support 100+ simultaneous requests | Medium |
| NFR-PERF-006 | Memory Usage (Extension) | <50MB RAM | Medium |
| NFR-PERF-007 | Memory Usage (API) | <512MB RAM | Medium |
| NFR-PERF-008 | CPU Usage | <10% idle, <50% under load | Low |

### 8.2 Reliability Requirements

| ID | Requirement | Target | Priority |
|----|-------------|--------|----------|
| NFR-REL-001 | API Uptime | 99.5% availability | High |
| NFR-REL-002 | Extension Stability | No crashes during normal operation | Critical |
| NFR-REL-003 | Graceful Degradation | Function in offline mode | High |
| NFR-REL-004 | Error Recovery | Automatic retry with exponential backoff | Medium |

### 8.3 Scalability Requirements

| ID | Requirement | Target | Priority |
|----|-------------|--------|----------|
| NFR-SCALE-001 | User Base | Support up to 1000 concurrent users | Medium |
| NFR-SCALE-002 | Request Throughput | Handle 100 requests/second | Medium |
| NFR-SCALE-003 | Model Retraining | Support monthly model updates | Low |

### 8.4 Usability Requirements

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| NFR-USE-001 | Intuitive Interface | Extension UI shall require no training | High |
| NFR-USE-002 | Clear Warnings | Phishing warnings shall be unambiguous | Critical |
| NFR-USE-003 | Minimal Disruption | Legitimate sites shall load without delay | Critical |
| NFR-USE-004 | Accessibility | Interface shall follow WCAG 2.1 Level AA | Low |

### 8.5 Security Requirements

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| NFR-SEC-001 | HTTPS Communication | All API calls shall use TLS 1.3 | Critical |
| NFR-SEC-002 | Input Sanitization | API shall sanitize all input to prevent injection | Critical |
| NFR-SEC-003 | No PII Collection | System shall not collect personally identifiable information | Critical |
| NFR-SEC-004 | Secure Storage | Extension shall use chrome.storage.local for sensitive data | High |

### 8.6 Maintainability Requirements

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| NFR-MAINT-001 | Code Documentation | All functions shall have docstrings | High |
| NFR-MAINT-002 | Code Quality | Code shall pass linting (PEP 8 for Python) | Medium |
| NFR-MAINT-003 | Version Control | All code shall be managed via Git | Critical |
| NFR-MAINT-004 | Automated Testing | Unit test coverage ≥80% | Medium |

---

## 9. Technical Specifications

### 9.1 Backend Technology Stack

| Component | Technology | Version | Justification |
|-----------|-----------|---------|---------------|
| Programming Language | Python | 3.10+ | ML library support, rapid development |
| Web Framework | FastAPI | 0.100+ | High performance, async support, automatic docs |
| ML Framework | Scikit-learn | 1.3+ | Comprehensive ML algorithms |
| Model (Primary) | XGBoost | 2.0+ | Superior performance for tabular data |
| Model (Alternative) | Random Forest | via scikit-learn | Ensemble method, interpretability |
| Data Processing | Pandas | 2.0+ | Data manipulation and analysis |
| Numerical Computing | NumPy | 1.24+ | Array operations, numerical computations |
| Model Serialization | Joblib | 1.3+ | Efficient model persistence |
| API Validation | Pydantic | 2.0+ | Data validation and settings management |
| Testing Framework | Pytest | 7.4+ | Comprehensive testing capabilities |
| ASGI Server | Uvicorn | 0.23+ | Production ASGI server |

### 9.2 Frontend Technology Stack

| Component | Technology | Version | Justification |
|-----------|-----------|---------|---------------|
| Extension Platform | Chrome Extension API | Manifest V3 | Latest Chrome extension standard |
| Programming Language | JavaScript | ES6+ | Native browser support |
| UI Framework | Vanilla JS | N/A | Minimal dependencies, fast load |
| HTTP Client | Fetch API | Native | Modern, promise-based HTTP requests |
| Storage | chrome.storage.local | Native | Secure extension storage |
| Styling | CSS3 | N/A | Custom lightweight styling |

### 9.3 Development Tools

| Tool | Purpose |
|------|---------|
| Git/GitHub | Version control and collaboration |
| Visual Studio Code | Primary IDE |
| Postman | API testing and documentation |
| Jupyter Notebook | Data exploration and model experimentation |
| Chrome DevTools | Extension debugging and profiling |
| Docker | Containerization (optional deployment) |

### 9.4 ML Feature Set

#### 9.4.1 Lexical Features (URL String Analysis)
- URL length
- Number of dots
- Number of hyphens
- Number of underscores
- Number of slashes
- Number of question marks
- Number of equal signs
- Number of at symbols
- Number of ampersands
- Presence of IP address
- Presence of shortened URL service
- Number of subdomains
- Length of hostname
- Presence of suspicious TLD (.xyz, .tk, .ml, etc.)

#### 9.4.2 Host-Based Features
- Domain age (via WHOIS when available)
- SSL certificate validity
- Page rank estimation
- DNS record anomalies
- Domain registrar reputation

#### 9.4.3 Content-Based Features (Optional Enhancement)
- Presence of login forms
- External resource count
- Favicon analysis
- HTML form analysis

### 9.5 API Specification

#### 9.5.1 POST /predict
**Description**: Classify a URL as phishing or legitimate

**Request**:
```json
{
  "url": "string",
  "user_id": "string (optional)"
}
```

**Response**:
```json
{
  "url": "string",
  "prediction": "phishing" | "legitimate",
  "confidence": 0.0-1.0,
  "risk_level": "high" | "medium" | "low",
  "features": {
    "url_length": 45,
    "num_dots": 3,
    ...
  },
  "timestamp": "ISO 8601 datetime"
}
```

**Status Codes**:
- 200: Successful classification
- 400: Invalid URL format
- 429: Rate limit exceeded
- 500: Internal server error

#### 9.5.2 GET /health
**Description**: Health check endpoint

**Response**:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "version": "1.0.0",
  "uptime": 3600
}
```

---

## 10. User Interface Requirements

### 10.1 Extension Popup

**Layout**: 
- Header: Extension logo and name
- Statistics section: Total URLs checked, threats blocked today
- Quick actions: Enable/disable protection, settings button
- Footer: Version info

**Dimensions**: 300px × 400px

### 10.2 Warning Page (Phishing Detected)

**Elements**:
- Large warning icon (red shield)
- Clear headline: "Phishing Threat Detected"
- Explanation: Brief description of the threat
- URL display: Show the suspicious URL
- Primary action: "Go Back to Safety" (green button)
- Secondary action: "Continue Anyway (Not Recommended)" (text link)
- Feedback option: "Report False Positive"

**Color Scheme**: Red (#DC3545) for danger, white background

### 10.3 Advisory Banner (Suspicious URL)

**Elements**:
- Yellow warning icon
- Message: "This site may be suspicious. Proceed with caution."
- Confidence score: "Confidence: 65%"
- Actions: "Trust this site" | "Block permanently" | "Learn more"

**Style**: Non-intrusive banner at top of page

### 10.4 Settings Page

**Sections**:
1. Protection Settings
   - Toggle: Enable/disable real-time protection
   - Sensitivity slider: Low/Medium/High
   
2. Whitelist Management
   - List of trusted domains
   - Add/Remove buttons
   
3. Privacy Settings
   - Toggle: Send anonymous usage statistics
   - Toggle: Enable cache
   
4. Advanced
   - API endpoint configuration (for self-hosted)
   - Debug mode toggle

---

## 11. Data Requirements

### 11.1 Training Dataset

**Sources**:
- PhishTank (verified phishing URLs)
- OpenPhish (community-reported phishing)
- Alexa Top 1M (legitimate URLs)
- Common Crawl (legitimate URL samples)
- UCI Machine Learning Repository (phishing datasets)

**Dataset Size**:
- Minimum: 50,000 URLs (25,000 phishing, 25,000 legitimate)
- Target: 100,000+ URLs for robust training
- Split: 70% training, 15% validation, 15% test

**Data Quality**:
- Remove duplicate URLs
- Validate URL format
- Remove dead/unreachable URLs (optional)
- Balance class distribution or apply SMOTE/class weights

### 11.2 Feature Storage

**Format**: 
- Feature vectors: NumPy arrays or Pandas DataFrames
- Serialized format: CSV for raw data, .pkl for processed features

### 11.3 Model Artifacts

**Storage Requirements**:
- Trained model file: ~10-50 MB (XGBoost/Random Forest)
- Feature vectorizer: ~1-5 MB
- Scaler objects: <1 MB
- Metadata: JSON config file

**Versioning**: 
- Model version naming: `phishing_model_v1.0.pkl`
- Store multiple versions for rollback capability

---

## 12. Security & Privacy

### 12.1 Privacy Considerations

| Aspect | Implementation | Rationale |
|--------|---------------|-----------|
| URL Logging | Log only domain (not full URL) | Prevent collection of sensitive query parameters |
| User Identification | No user tracking or identification | Respect user anonymity |
| Data Transmission | HTTPS only | Protect data in transit |
| Local Storage | Store whitelist locally | Avoid server-side user profile creation |
| Analytics | Optional, anonymized | User control over data sharing |

### 12.2 Security Measures

| Layer | Measure | Implementation |
|-------|---------|----------------|
| API | Rate Limiting | 100 requests/minute per IP |
| API | Input Validation | Pydantic models, URL regex validation |
| API | CORS Policy | Restrict to extension origin |
| Extension | Content Security Policy | Manifest V3 CSP directives |
| Extension | Secure Communication | Validate API responses |
| Data | No Sensitive Data | Avoid collecting PII |

### 12.3 Compliance

- **GDPR**: No personal data collection, no user consent required
- **Chrome Web Store Policies**: Comply with extension privacy requirements
- **Data Retention**: Cache cleared after 24 hours

---

## 13. Testing Strategy

### 13.1 Unit Testing

**Backend**:
- Test feature extraction functions
- Test model prediction logic
- Test API endpoint handlers
- Target: 80% code coverage

**Extension**:
- Test URL interception logic
- Test storage operations
- Test UI rendering

### 13.2 Integration Testing

- End-to-end flow: Extension → API → Response → UI
- API contract testing (request/response validation)
- Extension-backend communication

### 13.3 Model Evaluation

| Metric | Target | Measurement |
|--------|--------|-------------|
| Accuracy | ≥95% | Correct predictions / Total predictions |
| Precision | ≥93% | True Positives / (True Positives + False Positives) |
| Recall | ≥95% | True Positives / (True Positives + False Negatives) |
| F1-Score | ≥94% | Harmonic mean of precision and recall |
| ROC-AUC | ≥0.97 | Area under ROC curve |
| False Positive Rate | ≤5% | False Positives / (False Positives + True Negatives) |

**Testing Datasets**:
- Holdout test set (15% of data)
- Zero-day phishing URLs (newly discovered threats)
- Edge cases (IDN homograph attacks, URL obfuscation)

### 13.4 User Acceptance Testing

**Test Scenarios**:
1. Browse legitimate sites (Google, Facebook, Amazon) - no warnings
2. Visit known phishing site - warning displayed
3. Add site to whitelist - subsequent visits allowed
4. Disable protection - warnings stopped
5. Check statistics - correct counts displayed

**Test Users**: 10-15 volunteers from target demographic

### 13.5 Performance Testing

- Load testing: Simulate 100+ concurrent API requests
- Stress testing: Maximum throughput identification
- Extension performance: Page load time impact measurement
- Memory leak detection: Extended usage monitoring

### 13.6 Security Testing

- Input fuzzing: Malformed URL testing
- SQL injection attempts (if database added)
- XSS testing in extension UI
- API authentication bypass attempts

---

## 14. Timeline & Milestones

### 14.1 Project Phases

| Phase | Duration | Activities | Deliverables |
|-------|----------|------------|--------------|
| **Phase 1: Research & Planning** | Weeks 1-2 | Literature review, dataset identification, architecture design | PRD, Architecture document |
| **Phase 2: Data Collection & Preprocessing** | Weeks 3-4 | Dataset aggregation, cleaning, feature engineering | Training dataset, feature extraction pipeline |
| **Phase 3: Model Development** | Weeks 5-7 | Model training, hyperparameter tuning, evaluation | Trained ML model, evaluation report |
| **Phase 4: Backend Development** | Weeks 8-10 | FastAPI implementation, API endpoints, testing | Functional backend API |
| **Phase 5: Frontend Development** | Weeks 11-13 | Chrome extension development, UI design, integration | Functional Chrome extension |
| **Phase 6: Integration & Testing** | Weeks 14-15 | End-to-end testing, bug fixing, optimization | Integrated system, test reports |
| **Phase 7: Evaluation & Documentation** | Weeks 16-17 | UAT, performance benchmarking, documentation | Final report, user manual, presentation |
| **Phase 8: Deployment & Presentation** | Week 18 | Deployment, final presentation preparation | Deployed system, project presentation |

### 14.2 Key Milestones

| Milestone | Target Date | Success Criteria |
|-----------|-------------|------------------|
| M1: Project Kickoff | Week 1 | PRD approved, team formed |
| M2: Dataset Ready | Week 4 | 100K URLs collected, preprocessed |
| M3: Model Trained | Week 7 | Model achieves ≥95% accuracy |
| M4: API Functional | Week 10 | API passes all unit tests |
| M5: Extension Alpha | Week 13 | Basic extension functionality complete |
| M6: Integration Complete | Week 15 | End-to-end system operational |
| M7: UAT Complete | Week 16 | Positive user feedback received |
| M8: Project Delivery | Week 18 | All deliverables submitted |

---

## 15. Success Metrics

### 15.1 Technical Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Model Accuracy | ≥95% | Test set evaluation |
| False Positive Rate | ≤5% | Legitimate URLs incorrectly flagged |
| API Response Time | <200ms | Percentile (95th) measurement |
| Extension Load Time | <100ms | Chrome DevTools profiling |
| System Uptime | ≥99% | Monitoring logs |
| Bug Density | <2 bugs/KLOC | Static analysis, testing |

### 15.2 User Experience Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| User Satisfaction | ≥4/5 | Post-UAT survey |
| False Positive User Impact | <10% | User feedback, whitelist additions |
| Installation Success Rate | ≥95% | Installation tracking |
| Extension Uninstall Rate | <5% | Chrome Web Store metrics (if published) |

### 15.3 Academic Success Criteria

| Criterion | Description |
|-----------|-------------|
| Technical Innovation | Novel application of ML to phishing detection |
| Implementation Quality | Clean, well-documented, maintainable code |
| Evaluation Rigor | Comprehensive testing and analysis |
| Documentation | Complete PRD, user manual, technical report |
| Presentation | Clear communication of problem, solution, results |

---

## 16. Risks & Mitigation

### 16.1 Technical Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| Model underfitting/poor performance | Medium | High | Use multiple algorithms, ensemble methods, extensive feature engineering |
| Dataset quality issues | Medium | High | Multiple data sources, thorough data validation, manual review sample |
| API performance bottleneck | Low | Medium | Optimize model inference, implement caching, use async operations |
| Extension compatibility issues | Low | Medium | Thorough testing across Chrome versions, follow Manifest V3 best practices |
| Chrome Web Store rejection | Low | Medium | Comply with all policies, review guidelines before submission |
| HTTPS/CORS issues | Low | Low | Proper CORS configuration, HTTPS certificate setup |

### 16.2 Project Management Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| Scope creep | High | High | Strict adherence to defined scope, change control process |
| Timeline delays | Medium | High | Buffer time in schedule, prioritize critical features |
| Resource constraints | Medium | Medium | Identify requirements early, leverage free/open-source tools |
| Technical knowledge gaps | Medium | Medium | Early learning phase, leverage online resources, seek mentor guidance |

### 16.3 Data Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| Dataset unavailability | Low | High | Multiple backup data sources identified |
| Imbalanced dataset | Medium | High | SMOTE, class weighting, stratified sampling |
| Label noise (incorrect labels) | Medium | Medium | Cross-validation, manual review of high-confidence errors |
| Dataset obsolescence | Low | Low | Use recent datasets, consider incremental learning |

---

## 17. Future Enhancements

### 17.1 Short-Term Enhancements (Post-Project)

1. **Multi-Browser Support**: Firefox, Edge, Safari extensions
2. **Advanced ML Models**: Deep learning (LSTM, CNN) for URL sequence analysis
3. **Real-Time Model Updates**: Continuous learning from user feedback
4. **Visual Similarity Detection**: Screenshot comparison for spoofed sites
5. **Enhanced Whitelist**: Automatic whitelist suggestions based on browsing patterns

### 17.2 Medium-Term Enhancements

1. **Enterprise Features**: Centralized dashboard, admin controls, reporting
2. **Mobile Support**: Android/iOS apps or mobile browser integration
3. **Email Integration**: Outlook/Gmail plugin for email link scanning
4. **API Marketplace**: Public API for third-party integration
5. **Threat Intelligence Sharing**: Community-driven threat database

### 17.3 Long-Term Vision

1. **AI-Powered Content Analysis**: Deep learning for webpage visual inspection
2. **Behavioral Analysis**: User interaction pattern anomaly detection
3. **Blockchain Integration**: Decentralized reputation system
4. **Automated Remediation**: Partnership with registrars for takedown
5. **Educational Platform**: Phishing awareness training integrated into extension

---

## 18. Appendices

### Appendix A: Glossary

| Term | Definition |
|------|------------|
| Phishing | Fraudulent attempt to obtain sensitive information by disguising as trustworthy entity |
| False Positive | Legitimate URL incorrectly classified as phishing |
| False Negative | Phishing URL incorrectly classified as legitimate |
| XGBoost | Extreme Gradient Boosting, an ensemble ML algorithm |
| Manifest V3 | Latest Chrome extension platform version |
| WHOIS | Protocol for querying domain registration information |
| TLD | Top-Level Domain (e.g., .com, .org) |
| ROC-AUC | Receiver Operating Characteristic - Area Under Curve |

### Appendix B: References

1. **Academic Papers**:
   - Mohammad, R., Thabtah, F., & McCluskey, L. (2014). "Predicting phishing websites based on self-structuring neural network"
   - Jain, A. K., & Gupta, B. B. (2016). "Phishing detection: Analysis of visual similarity based approaches"

2. **Datasets**:
   - PhishTank: https://phishtank.org/
   - UCI ML Repository: https://archive.ics.uci.edu/ml/datasets/phishing+websites

3. **Technical Documentation**:
   - Chrome Extension Developer Guide: https://developer.chrome.com/docs/extensions/
   - FastAPI Documentation: https://fastapi.tiangolo.com/
   - XGBoost Documentation: https://xgboost.readthedocs.io/

### Appendix C: Contact Information

**Project Team**:
- Developer: [Your Name]
- Email: [Your Email]
- GitHub: [Your GitHub Profile]
---

**Document Change Log**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Feb 15, 2026 | [Your Name] | Initial PRD creation |

---

**Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Developer | [Your Name] | _________ | _______ |
| Project Supervisor | [Supervisor Name] | _________ | _______ |

---

*End of Document*