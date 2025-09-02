import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Fetch the stock data for the last 7 days for 532925.BO
ticker = "532925.BO"
stock_data = yf.download(ticker, period="7d", interval="1d")

# Calculate daily change
stock_data['Change'] = stock_data['Close'].pct_change() * 100

# Calculate total change
total_change = stock_data['Change'].sum()

# Create a Streamlit app
st.title(f"Stock Daily Change for {ticker}")

# Display total change
st.write(f"Total Change in the last 7 days: {total_change:.2f}%")

# Display daily changes with colors (positive = green, negative = red)
st.subheader("Daily Change:")
for date, row in stock_data.iterrows():
    change = row['Change']
    if change > 0:
        color = "green"
    else:
        color = "red"
    
    st.markdown(f"<span style='color:{color};'>{date.date()}: {change:.2f}%</span>", unsafe_allow_html=True)

# Plot a simple bar chart showing daily changes
fig = go.Figure([go.Bar(x=stock_data.index.date, y=stock_data['Change'], marker=dict(color=stock_data['Change'].apply(lambda x: 'green' if x > 0 else 'red')))])

fig.update_layout(title=f"Daily Changes for {ticker}", xaxis_title="Date", yaxis_title="Change (%)")

# Display the plot in Streamlit
st.plotly_chart(fig)
