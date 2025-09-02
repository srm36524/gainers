import yfinance as yf
import pandas as pd
import streamlit as st

# Fetch closing prices for Kaushalya Infrastructure (BSE: KAUSHALYA.BO) over the last 8 days
ticker = "KAUSHALYA.BO"
stock_data = yf.download(ticker, period="8d", interval="1d")['Close']

if stock_data.empty:
    st.write("No data available for the specified period.")
else:
    # Calculate daily percentage change as (Today Close / Previous Close) - 1
    daily_change = (stock_data / stock_data.shift(1) - 1) * 100

    # Drop the first NaN value (since the first row doesn't have a previous close to compare)
    daily_change = daily_change.dropna()

    # Display the title
    st.title(f"Daily Percentage Change for {ticker}")

    # Display the daily percentage change for today and the past 7 days
    st.subheader("Daily Change (Today and Past 7 Days):")

    # Loop through the last 7 days of changes and display them using `.items()` for a Series
    if len(daily_change) < 7:
        st.write("Not enough data to display changes for the last 7 days.")
    else:
        for date, change in daily_change.tail(7).items():
            if pd.isnull(change):
                st.write(f"{date}: No data available")
            else:
                st.write(f"{date}: {change:.2f}%")

        # Calculate the total change for the last 7 days
        total_change = daily_change.tail(7).sum()
        st.write(f"Total Change in the last 7 days: {total_change:.2f}%")
