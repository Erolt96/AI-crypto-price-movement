🧠 AI Crypto Price Movement Classifier
This project is a machine learning model that predicts whether the price of Bitcoin (BTC) will go up or down the next day using historical price data.
It uses a Random Forest Classifier trained on live BTC data fetched via yfinance.

🔍 What it does
Downloads real BTC-USD market data

Trains a model to classify next-day movement (Up = 1, Down = 0)

Saves the model with joblib

Predicts live price movement using today’s data

🛠 Technologies
Python

scikit-learn

yfinance

pandas

joblib

