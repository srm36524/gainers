import yfinance as yf
import pandas as pd
import streamlit as st

def get_stock_data(ticker, period):
    try:
        return yf.download(ticker, period=period)['Close']
    except Exception as e:
        st.error(f"Failed to retrieve stock data: {e}")
        return pd.Series()

def calculate_daily_change(stock_data):
    if stock_data.empty:
        return pd.Series()
    return stock_data.pct_change() * 100

def display_daily_changes(daily_change, num_days):
    if daily_change.empty:
        st.write("No data available for the specified period.")
    else:
        last_n_days = daily_change.tail(num_days)
        st.subheader(f"Daily Change (Last {num_days} Trading Days):")
        for date, change in last_n_days.items():
            if pd.notnull(change):
                st.write(f"{date}: {change:.2f}%")
            else:
                st.write(f"{date}: No data available")

        total_change = last_n_days.sum()
        st.write(f"Total Change in the last {num_days} trading days: {total_change:.2f}%")

def main():
    ticker = "KAUSHALYA.BO"
    period = "30d"
    num_days = 7

    st.title(f"Daily Percentage Change for {ticker}")
    stock_data = get_stock_data(ticker, period)
    daily_change = calculate_daily_change(stock_data).dropna()
    display_daily_changes(daily_change, num_days)

if __name__ == "__main__":
    main()
