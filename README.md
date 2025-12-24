📱 Mobile Price Range Prediction App

This project builds a machine learning application that predicts the price range of a mobile phone based on its hardware and feature specifications.
The output is a classification into one of four price categories: low, medium, high, or very high.

This is not a toy regression problem. It is a supervised multi-class classification task.

🚀 Objective

Predict the price range of a mobile phone using technical specifications such as battery power, RAM, camera quality, screen size, and connectivity features.

Target variable:

Price_range

0 Low cost

1 Medium cost

2 High cost

3 Very high cost

The dataset and problem definition come from the Mobile Price Prediction problem statement 

Predict Mobile Phone Pricing

.

📂 Dataset Overview

Each row represents a mobile phone.
Each column represents a measurable feature.

Input Features

Battery & Power

battery_power

talk_time

Performance

ram

clock_speed

n_cores

Memory

int_memory

Camera

fc Front camera (MP)

pc Primary camera (MP)

Display

px_height

px_width

sc_h

sc_w

Connectivity

blue Bluetooth

dual_sim

three_g

four_g

wifi

touch_screen

Physical

mobile_wt

m_deep

Target

Price_range

🧠 Approach

This project follows a standard ML pipeline. Skipping steps here means you do not understand ML.

Data Loading

Exploratory Data Analysis

Univariate

Bivariate

Multivariate

Feature Scaling

Required. RAM alone dominates otherwise.

Train-Test Split

Model Training

Logistic Regression

Random Forest

XGBoost (optional, but superior)

Evaluation

Accuracy

Confusion Matrix

Classification Report

Deployment

Streamlit / Flask app

🛠 Tech Stack

Language: Python

Libraries:

NumPy

Pandas

Matplotlib / Seaborn

Scikit-learn

Deployment:

Streamlit or Flask

Version Control:

Git + GitHub

🖥 Application Flow

User enters mobile specifications

Input is validated and scaled

Trained ML model predicts price range

Result is displayed instantly

This is a classification system, not a recommendation engine.

If your repository does not look like this, it is poorly organized.

📊 Expected Output

Model accuracy above 90%

Clear class separation

No data leakage

No hardcoded predictions

Anything less means your pipeline is broken.

🔮 Future Improvements

Hyperparameter tuning

Feature importance visualization

Model comparison dashboard

REST API for predictions

Do these only after the base model is solid.

📌 Conclusion

This project demonstrates:

Proper handling of structured data

Real-world classification modeling

End-to-end ML deployment

If you cannot explain why RAM dominates price, you do not understand the dataset.
