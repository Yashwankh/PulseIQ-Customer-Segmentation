# 🚀 PulseIQ — Real-Time Business Intelligence Dashboard

## 📌 Project Overview

PulseIQ is a Business Intelligence and Machine Learning project designed to analyze customer behavior, predict churn, forecast revenue, and provide interactive visual insights through a dashboard.

This project integrates data engineering, exploratory data analysis (EDA), customer segmentation, machine learning models, forecasting, and dashboard visualization into one unified system.

The goal of PulseIQ is to help businesses make data-driven decisions by understanding customer patterns and predicting future outcomes.

---

## 🎯 Project Objectives

- Perform data cleaning and preprocessing
- Conduct exploratory data analysis (EDA)
- Segment customers using RFM analysis
- Predict customer churn using Machine Learning
- Forecast future revenue using time series models
- Build an interactive dashboard
- Provide actionable business insights

---

## 🧠 Project Workflow

Raw Data
↓
Data Cleaning
↓
EDA (Exploratory Data Analysis)
↓
Customer Segmentation
↓
Churn Prediction
↓
Revenue Forecasting
↓
Interactive Dashboard


---

## 📊 Modules in This Project

### 1️⃣ Data Engineering

- Cleaned raw dataset
- Removed duplicates and missing values
- Created derived features such as:
  - Recency
  - Frequency
  - Monetary
  - Total Amount
  - Churn Label

**Output:**
- `cleaned_data.csv`

---

### 2️⃣ Exploratory Data Analysis (EDA)

Performed data analysis to understand trends and relationships.

**Key Visualizations:**

- Monthly Revenue Trend
- Correlation Heatmap
- Churn Distribution
- Sales Distribution
- Frequency vs Monetary Analysis

**Output Files:**

visuals/eda/
├── monthly_revenue_trend.png
├── correlation_heatmap.png
├── churn_distribution.png
├── sales_distribution.png



---

### 3️⃣ Customer Segmentation (RFM + K-Means)

Customers were segmented using:

- Recency
- Frequency
- Monetary

**Steps Performed:**

- Feature Scaling
- Log Transformation
- Elbow Method
- K-Means Clustering

**Segments Created:**

- ⭐ High Value Customers
- 🟢 Regular Customers
- ⚠️ At Risk Customers

**Output Files:**
customer_segments.csv
segmentation_model.pkl
customer_segmentation.png





