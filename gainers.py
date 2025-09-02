import yfinance as yf
import pandas as pd
import streamlit as st

# Fetch only the closing price for Kaushalya Infrastructure (BSE: KAUSHALYA.BO)
ticker = "KAUSHALYA.BO"
stock_data = yf.download(ticker, period="7d", interval="1d")['Close']

# Calculate daily percentage change as (Today Close / Previous Close) - 1
daily_change = (stock_data / stock_data.shift(1) - 1) * 100

# Drop the first NaN value (since the first row doesn't have a previous close to compare)
daily_change = daily_change.dropna()

# Display title
st.title(f"Daily Percentage Change for {ticker}")

# Display daily change values without color coding
st.subheader("Daily Change:")

# Loop through each date and the corresponding change value using iteritems()
for date, change in daily_change.iteritems():
    if isinstance(change, (int, float)):  # Check if `change` is a scalar
        # Display the change without any color coding
        st.write(f"{date.date()}: {change:.2f}%")

# Calculate total change
total_change = daily_change.sum()
st.write(f"Total Change in the last 7 days: {total_change:.2f}%")
