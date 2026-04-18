# Demand Forecasting Application

This project presents a machine learning-based demand forecasting system that predicts future sales using time-series feature engineering and an XGBoost regression model. The application is deployed using Streamlit to provide an interactive interface for real-time predictions.

---

## Overview

The objective of this project is to forecast product demand using historical sales data. The model leverages engineered time-based features to capture trends, seasonality, and recent sales behavior, resulting in improved prediction accuracy.

---

## Key Features

- Real-time demand prediction through an interactive web application  
- Time-series feature engineering including lag variables and rolling averages  
- XGBoost regression model for accurate forecasting  
- Baseline comparison demonstrating approximately 60% improvement  
- Visualization of predicted vs historical demand  

---

## Model Details

- Algorithm: XGBoost Regressor  
- Problem Type: Regression  
- Evaluation Metric: Mean Absolute Error (MAE)  
- Baseline Model: Lag-based prediction  
- Performance: ~60% improvement over baseline  

---

## Methodology

The model uses historical sales data and engineered features such as:

- Lag features (previous day, weekly, and monthly sales)  
- Rolling averages (7-day and 30-day windows)  
- Temporal features (weekday, month, and day)  

These features enable the model to capture both short-term variations and long-term demand patterns.

---

## Use Cases

- Retail demand forecasting  
- Inventory planning  
- Sales optimization  
- Promotion impact analysis  

---

## Author

Vishaal Jaladi
