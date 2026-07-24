# Smart-Agriculture-Crop-Recommendation-System
 AI-powered crop recommendation system using Machine Learning, Flask, Random Forest, XGBoost, and an interactive dashboard.
# 🌱 Smart Agriculture Crop Recommendation System using Machine Learning

## 📌 Project Overview

The Smart Agriculture Crop Recommendation System is a Machine Learning-based web application that recommends the most suitable crop based on soil nutrients and environmental conditions. The system uses a trained Random Forest model to predict the best crop and also provides fertilizer recommendations along with an interactive dashboard for data visualization.

This project was developed as a Capstone Project using Python, Flask, Machine Learning, HTML, CSS, JavaScript, and Chart.js.

---

## 🚀 Features

- 🌾 Crop Recommendation using Machine Learning
- 🤖 Random Forest & XGBoost Model Training
- 🌱 Fertilizer Recommendation
- 📊 Interactive Analytics Dashboard
- 📈 Prediction Confidence Score
- 💻 Responsive Web Interface
- ⚡ Flask Backend
- 📂 Organized Project Structure

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Flask

### Machine Learning
- Random Forest Classifier
- XGBoost Classifier
- Scikit-learn

### Libraries
- Pandas
- NumPy
- Joblib
- Matplotlib
- Chart.js

### Development Tools
- Visual Studio Code
- Google Colab

### Dataset
- Crop Recommendation Dataset (Kaggle)

---

## 📂 Project Structure

```
Smart-Agriculture-Crop-Recommendation-System/

│── app.py
│── fertilizer_recommendation.py
│── model_info.py
│── requirements.txt

├── dataset/
│      Crop_recommendation.csv

├── models/
│      crop_model.pkl
│      label_encoder.pkl

├── src/
│      train_model.py
│      predict_crop.py

├── templates/
│      index.html
│      dashboard.html

├── static/
│      style.css

└── README.md
```

---

## 📊 Dataset Information

The project uses the **Crop Recommendation Dataset** from Kaggle.

### Input Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

### Output

Recommended Crop

Examples:

- Rice
- Maize
- Cotton
- Coffee
- Apple
- Mango
- Papaya
- Banana
- Watermelon

---

## ⚙️ Project Workflow

```
Crop Recommendation Dataset
            │
            ▼
Data Preprocessing
            │
            ▼
