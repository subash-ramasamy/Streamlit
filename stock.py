import streamlit as st
st.title("Stock Analyzer!")

import yfinance as yf 
stock_name = st.text_input("Stock to be Analyzed")

ticker_data = yf.Ticker(stock_name)

ticker_df = ticker_data.history(period = "1d", start = "2024-12-01", end = "2024-12-11")

st.dataframe(ticker_df)

st.write("Hi")