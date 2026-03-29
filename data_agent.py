import yfinance as yf
import streamlit as st

@st.cache_data(ttl=900)
def get_stock_data(ticker):
    return yf.Ticker(ticker).history(period="1y")