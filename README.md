# 💹 AI Crypto Price Movement Classifier

A machine learning model that predicts whether **Bitcoin (BTC)** will go **up 📈 or down 📉** the next day based on historical market data.

---

## 🧠 Overview

This project uses a **Random Forest Classifier** trained on real BTC price data to forecast the next day’s movement.  
The model is trained and tested using data from `yfinance`, and predictions can be made in real time using today's live data.

---

## 🚀 Features

✅ Downloads historical BTC-USD price data  
✅ Cleans and prepares the dataset  
✅ Trains a classification model  
✅ Predicts if tomorrow's price will go **UP** or **DOWN**  
✅ Can fetch **live daily data** and run the prediction instantly

---

## 🔧 Tech Stack

- **Python 3**
- **scikit-learn** (ML model)
- **pandas** (data handling)
- **yfinance** (fetching crypto data)
- **joblib** (model persistence)

---

## 📦 Project Structure
AI-crypto-price-movement/
├── crypto_classifier.ipynb # Jupyter notebook used for training
├── predict_today.py # Script for live prediction
├── .gitignore # Excludes model file
├── requirements.txt # Dependencies
└── README.md # You're reading it!


🛑 Model file `crypto_model.joblib` is intentionally excluded for security and size — but you can easily retrain it.

---

## 🧪 How to Use

### 1. Clone the repository
```bash
git clone https://github.com/Erolt96/AI-crypto-price-movement.git
cd AI-crypto-price-movement

2.Install dependencies
pip install -r requirements.txt


3. Run live prediction
python predition.py


