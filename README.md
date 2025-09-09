# Heart-Disease-Predictor
## Heart Disease Predictor
### Overview

This project focuses on building a machine learning model to predict the presence of heart disease in patients based on clinical and demographic data. The goal is to assist healthcare professionals in identifying potential heart disease cases early, thereby improving patient outcomes.

The dataset used contains a mix of categorical and numerical features, such as age, sex, chest pain type, resting blood pressure, cholesterol level, fasting blood sugar, ECG results, maximum heart rate, exercise-induced angina, and others. These features provide a comprehensive basis for predicting the likelihood of heart disease.

The final model achieved an accuracy of 85%, making it a reliable baseline tool for early detection of heart disease.

## Dataset

The dataset used is the Cleveland Heart Disease dataset, a widely known benchmark dataset in the medical machine learning community.

#### Key features include:

Age

Sex

Chest pain type

Resting blood pressure

Serum cholesterol

Fasting blood sugar

Resting electrocardiographic results

Maximum heart rate achieved

Exercise induced angina

Oldpeak (ST depression induced by exercise)

Slope of the peak exercise ST segment

Number of major vessels colored by fluoroscopy

Thalassemia

Target variable:

0 = No heart disease

1 = Presence of heart disease

## Approach

### Data Preprocessing

Handled missing values using imputation techniques.

Encoded categorical variables (e.g., chest pain type, thalassemia).

Scaled numerical features for consistent input to models.

### Exploratory Data Analysis

Visualized distributions of clinical features.

Compared feature importance against the target variable.

Identified correlations between predictors.

### Model Development


 models: Random Forest, XGBoost, SVM , Logistic Regression..

Used cross-validation for reliable evaluation.

Evaluation Metrics

Accuracy: 85%

Precision, recall, and F1-score were also computed to evaluate model .

Results

The model successfully predicted heart disease with 85% accuracy.

The project demonstrates that machine learning can provide meaningful decision support for medical practitioners.

Tools and Technologies

Python

Pandas, NumPy for data manipulation

Scikit-learn for machine learning models and preprocessing

Matplotlib, Seaborn for data visualization

XGBoost for gradient boosting models
