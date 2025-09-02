import yfinance as yf
import pandas as pd
import streamlit as st

# Fetch only the closing price for Kaushalya Infrastructure (BSE: KAUSHALYA.BO)
ticker = "KAUSHALYA.BO"
stock_data = yf.download(ticker, period="7d", interval="1d")['Close']

# Calculate daily percentage change
stock_data = stock_data.pct_change() * 100  # Daily change in percentage

# Drop the first NaN value (because the first value won't have a previous day to compare)
stock_data = stock_data.dropna()

# Display title
st.title(f"Daily Percentage Change for {ticker}")

# Display daily change values with proper color
st.subheader("Daily Change:")
for date, change in stock_data.items():
    if change > 0:
        color = "green"
    elif change < 0:
        color = "red"
    else:
        color = "black"
    
    # Display the change with the correct color
    st.markdown(f"<span style='color:{color};'>{date.date()}: {change:.2f}%</span>", unsafe_allow_html=True)

# Calculate total change
total_change = stock_data.sum()
st.write(f"Total Change in the last 7 days: {total_change:.2f}%")
