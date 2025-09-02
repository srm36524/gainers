import yfinance as yf
import pandas as pd
import streamlit as st

# Fetch data for Kaushalya Infrastructure (BSE: KAUSHALYA.BO)
ticker = "KAUSHALYA.BO"
stock_data = yf.download(ticker, period="7d", interval="1d")

# Calculate daily percentage change
stock_data['Change'] = stock_data['Close'].pct_change() * 100

# Clean NaN values (drop the first row or handle it based on context)
stock_data = stock_data.dropna(subset=['Change'])

# Display title
st.title(f"Stock Daily Change for {ticker}")

# Display daily change values with proper color
st.subheader("Daily Change:")
for date, row in stock_data.iterrows():
    change = row['Change']
    if pd.isna(change):  # Skip any NaN values (though we already dropped them)
        continue
    if change > 0:
        color = "green"
    else:
        color = "red"
    
    st.markdown(f"<span style='color:{color};'>{date.date()}: {change:.2f}%</span>", unsafe_allow_html=True)

# Calculate total change
total_change = stock_data['Change'].sum()
st.write(f"Total Change in the last 7 days: {total_change:.2f}%")
