import yfinance as yf
import pandas as pd

symbol = "SPY"  # Replace with the symbol you want to track
threshold = 1000  # Replace with your desired order flow threshold

def check_order_flow():
    data = yf.download(symbol, period="1d", interval="1m")
    volume_sum = data["Volume"].rolling(window=10).sum()  # Sum the volume over a 10-minute window
    bid_ask_imbalance = (data["Volume"] * (data["Close"] - data["Open"])) / volume_sum
    order_flow_imbalance = bid_ask_imbalance.cumsum()
    latest_imbalance = order_flow_imbalance.iloc[-1]
    if abs(latest_imbalance) > threshold:
        print(f"Order flow imbalance alert: {latest_imbalance}")

check_order_flow()  # Call the function to check for order flow imbalances


exit()