import yfinance as yf
import pandas as pd
import streamlit as st

# Fetch closing prices for Kaushalya Infrastructure (BSE: KAUSHALYA.BO) over the last 30 days
ticker = "KAUSHALYA.BO"
stock_data = yf.download(ticker, period="30d", interval="1d")['Close']

if stock_data.empty:
    st.write("No data available for the specified period.")
else:
    # Calculate daily percentage change as (Today Close / Previous Close) - 1
    daily_change = (stock_data / stock_data.shift(1) - 1) * 100

    # Drop the first NaN value (since the first row doesn't have a previous close to compare)
    daily_change = daily_change.dropna()

    # Display the title
    st.title(f"Daily Percentage Change for {ticker}")

    # Display the daily percentage change for the last available trading days
    st.subheader("Daily Change (Last 7 Trading Days):")

    # Loop through the last 7 trading days of changes and display them
    last_7_days = daily_change.tail(7)
    for date, change in last_7_days.items():
        if pd.isnull(change):
            st.write(f"{date}: No data available")
        else:
            st.write(f"{date}: {change:.2f}%")

    # Calculate the total change for the last 7 trading days
    total_change = last_7_days.sum()
    st.write(f"Total Change in the last 7 trading days: {total_change:.2f}%")
