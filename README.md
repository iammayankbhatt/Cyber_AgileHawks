#  Cyber Threat Detection — Agile Hawks



##  Team

| Name | Role |
|------|------|
| Mayank Bhatt | Team Member |
| Ansh Karki | Team Member |

---

##  Overview

This project focuses on **cyber threat detection** using machine learning on a large-scale, highly imbalanced dataset. The solution involves a complete end-to-end pipeline:

-  Exploratory Data Analysis (EDA)
-  Data Cleaning and Preprocessing
-  Feature Engineering
-  Model Training using XGBoost
-  Deployment via Streamlit

**Primary Goal:
 Build an AI-powered threat detection system capable of identifying complex cyberattacks : including botnets, DDoS attacks, and web-based exploits - by distinguishing legitimate user traffic from malicious or bot-driven activity, even under conditions of extreme class imbalance and noisy real-world labels.
---

##  Repository Structure

```
├── eda.ipynb                  # Exploratory Data Analysis
├── preprocessing.ipynb        # Data cleaning & preprocessing
├── model_training.ipynb       # Model training pipeline
├── app.py                     # Streamlit application
├── requirements.txt           # Dependencies
└── README.md
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo-link>
cd <repo-folder>
```

### 2. Download the Trained Model

 [Download Model from Google Drive](https://drive.google.com/file/d/1OG4n-6pX81fsfoWUzyTOu14-MCbaMzBA/view?usp=drive_link)

> Place the model file in the **project root directory**.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

##  Dataset

🔗 [Engineered Dataset on Kaggle](https://www.kaggle.com/datasets/anshkarki/engineered-dataset-1)

**Files:**
- `engineered_dataset.csv`
- `label_map.csv`

---

##  Exploratory Data Analysis (EDA)

### Dataset Summary

| Metric | Value |
|--------|-------|
| Total Rows | 1,775,435 |
| Total Features | 79 |
| Numeric Features | 70 |
| Missing Value Columns | 14 |
| Duplicate Rows | 1,445 |
| Inf-Value Columns | 2 |
| Zero-Variance Features | 0 |
| Near-Zero-Variance Features | 6 |
| High-Correlation Pairs (> 0.9) | 20 |
| Unique Labels | 1,588 |
| Class Imbalance Ratio | 1,180,520× |

###  Key Observations

- The dataset is **extremely imbalanced**, making evaluation challenging
- Significant **label noise and duplication** exist across classes
- High correlation among features required **dimensionality reduction**
- Missing and infinite values required **careful preprocessing**
- **Multi-class problem** with a very large number of categories

---

##  Feature Engineering

### Final Processed Dataset

| Metric | Value |
|--------|-------|
| Final Rows | 1,768,131 |
| Final Features | 85 |
| Label Classes | 1,589 |
| Saved To | `engineered_dataset.csv` |
| Label Map | `label_map.csv` |

### Steps Performed

1. Removed missing and infinite values
2. Eliminated duplicate entries
3. Reduced highly correlated features
4. Removed near-zero variance features
5. Created additional meaningful features
6. Encoded labels and saved mapping for reproducibility

---

##  Modeling Approach

> Detailed in `model_training.ipynb`

### Pipeline Overview

```
Load Engineered Dataset
        ↓
Stratified Train-Test Split
        ↓
Handle Imbalance (SMOTE on train set only)
        ↓
Train XGBoost Model
        ↓
Evaluate with Weighted Metrics
```

### Model Used

- **Primary Model:** XGBoost

###  Important Evaluation Note

Due to extreme class imbalance:
-  **Weighted metrics** are used for evaluation
-  **Macro scores** are intentionally ignored — they do not reflect real performance in this scenario

---

##  Key Challenges

| Challenge | Details |
|-----------|---------|
| Extreme class imbalance | ~1,000,000 : 1 ratio |
| Noisy & inconsistent labels | ~1,589 unique classes |
| Memory constraints | Dataset size ~2 GB |
| Feature redundancy | High correlation among features |

---

##  Deployment

A lightweight **Streamlit application** is provided to:

- Input feature values
- Generate predictions using the trained model
- Display predicted cyber threat category

---

##  Future Improvements

- [ ] Label consolidation to reduce noise (grouping similar classes)
- [ ] Advanced ensemble models (XGBoost + LightGBM + CatBoost)
- [ ] Hyperparameter tuning using Optuna or FLAML
- [ ] Model calibration and threshold optimization
- [ ] Real-time streaming data integration

---

##  Notes

> - The dataset is preprocessed and engineered before training
> - Label mapping is preserved for reproducibility
> - Model file must be downloaded separately due to size constraints
