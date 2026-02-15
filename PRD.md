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

**Supervisor**:
- Name: [Supervisor Name]
- Department: [Department]
- Email: [Supervisor Email]

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