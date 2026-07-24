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
Label Encoding
            │
            ▼
Train-Test Split
            │
            ▼
Random Forest & XGBoost Training
            │
            ▼
Model Evaluation
            │
            ▼
Save Model (.pkl)
            │
            ▼
Flask Backend
            │
            ▼
User Input
            │
            ▼
Crop Prediction
            │
            ▼
Confidence Score
            │
            ▼
Fertilizer Recommendation
            │
            ▼
Analytics Dashboard
```

---

## 🧠 Machine Learning Models

### Random Forest

- High prediction accuracy
- Handles multiclass classification
- Reduces overfitting
- Used as the final deployed model

### XGBoost

- Used for model comparison
- Gradient boosting algorithm
- High performance on structured datasets

---

## 💻 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Agriculture-Crop-Recommendation-System.git
```

### Navigate to Project

```bash
cd Smart-Agriculture-Crop-Recommendation-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Application Modules

- Home Page
- Crop Prediction
- Confidence Score
- Fertilizer Recommendation
- Analytics Dashboard

---

## 🎯 Results

The developed system successfully predicts the most suitable crop based on soil nutrients and weather conditions.

The application also:

- Displays prediction confidence
- Provides fertilizer suggestions
- Visualizes agricultural data using charts
- Offers an easy-to-use interface

---

## 🔮 Future Enhancements

- Live Weather API Integration
- IoT Soil Sensor Integration
- Crop Disease Detection
- Mobile Application
- Cloud Deployment
- Multilingual Support
- User Authentication

---

## 📚 References

- Kaggle Crop Recommendation Dataset
- Scikit-learn Documentation
- Flask Documentation
- XGBoost Documentation
- Pandas Documentation
- NumPy Documentation

---

## 👩‍💻 Author

**Malavika B.S**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

Capstone Project | Machine Learning | Flask | Data Science

---

⭐ If you found this project useful, please consider giving it a Star on GitHub.
