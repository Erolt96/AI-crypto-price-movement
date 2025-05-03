import pandas as pd
import yfinance as yf
import joblib

# Load your trained model
model = joblib.load("crypto_model.joblib")

# Download today's BTC data
btc_today = yf.download('BTC-USD', period='1d', interval='1d')

# Prepare the feature DataFrame
latest_data = btc_today[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
latest_data.reset_index(drop=True, inplace=True)

# Predict using the model
prediction = model.predict(latest_data)

# Show result
if prediction[0] == 1:
    print("📈 Prediction: Price will go UP tomorrow.")
else:
    print("📉 Prediction: Price will go DOWN tomorrow.")

print("\nToday's data used for prediction:")
print(latest_data)
