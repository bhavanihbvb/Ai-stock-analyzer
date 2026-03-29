from splash import show_splash
import streamlit as st
import sqlite3
import time

from auth import auth_page, logout
from data_agent import get_stock_data
from pattern_agent import detect_trend
from prediction_agent import predict_price
from decision_agent import make_decision
from explanation_agent import explain
from sentiment_agent import get_news_sentiment

from opportunity_agent import find_opportunity
from pattern_advanced import detect_patterns
from scanner import market_scanner
from assistant_agent import ai_answer
from portfolio_agent import portfolio_advice
from backtest import backtest

st.set_page_config(page_title="Smart Investor AI", layout="wide")

# Dynamic Theme Injection
if not st.session_state.get("logged_in", False):
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #FF6B6B 100%);
        color: white;
    }
    div.stButton > button {
        border-radius: 30px;
        background: linear-gradient(90deg, #F09819 0%, #EDDE5D 100%);
        color: #333;
        border: none;
        font-weight: bold;
        transition: transform 0.2s;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        color: #212529;
    }
    [data-testid="stSidebar"] {
        background-color: #1a252f;
    }
    [data-testid="stSidebar"] * {
        color: #ecf0f1;
    }
    div[data-testid="stMetricValue"] {
        color: #27ae60;
        font-size: 2.2rem;
        font-weight: bold;
    }
    div.stButton > button {
        background-color: #2980b9;
        color: white;
        border-radius: 8px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------- SPLASH CONTROL ----------
if "splash_done" not in st.session_state:
    st.session_state["splash_done"] = False

if not st.session_state["splash_done"]:
    show_splash()
    time.sleep(3.8)
    st.session_state["splash_done"] = True
    st.rerun()

# ---------- AUTH ----------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    auth_page()
    st.stop()

# ---------- DB ----------
conn = sqlite3.connect("portfolio.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS portfolio(username TEXT, stock TEXT, qty INT, price REAL)")

# ---------- SIDEBAR ----------
st.sidebar.image("logo.png", width=150)
menu = st.sidebar.selectbox("Navigation", ["Dashboard","Portfolio","News","Assistant"])

if st.sidebar.button("Logout"):
    logout()

username = st.session_state["username"]

# ---------- LIVE ALERTS ----------
st.sidebar.markdown("### Live AI Alerts")

stocks = ["RELIANCE.NS","TCS.NS","INFY.NS"]

alerts = market_scanner(stocks)
for a in alerts:
    st.sidebar.warning(a)

# ---------- DASHBOARD ----------
if menu == "Dashboard":
    st.title("Smart Investor AI")

    ticker_input = st.text_input("Stock Symbol", "TCS")

    # NSE FIX
    ticker = ticker_input.upper()
    if not ticker.endswith(".NS"):
        ticker += ".NS"

    if st.button("Analyze"):
        data = get_stock_data(ticker)

        if data.empty:
            st.error("Invalid stock")
        else:
            st.line_chart(data['Close'])

            trend = detect_trend(data)
            pred = predict_price(data)
            curr = data['Close'].iloc[-1]

            decision = make_decision(trend, pred, curr)
            acc = backtest(data)

            st.metric("Decision", decision)
            st.metric("Model Accuracy (%)", acc)

            st.write(explain(decision, trend, pred, curr))

            # Opportunity
            st.markdown("### Opportunity Radar")
            for s in find_opportunity(data, pred, curr):
                st.warning(s)

            # Patterns
            st.markdown("### Pattern Intelligence")
            for p in detect_patterns(data):
                st.info(p)

            # Portfolio
            rows = c.execute("SELECT stock FROM portfolio WHERE username=?", (username,)).fetchall()
            user_stocks = [r[0] for r in rows]

            st.markdown("### Portfolio Advice")
            for a in portfolio_advice(user_stocks):
                st.write(a)

# ---------- PORTFOLIO ----------
elif menu == "Portfolio":
    st.title("Portfolio")

    stock = st.text_input("Stock (e.g., TCS)")
    qty = st.number_input("Qty",1)
    price = st.number_input("Buy Price")

    if st.button("Add"):
        if not stock.endswith(".NS"):
            stock += ".NS"
        c.execute("INSERT INTO portfolio VALUES(?,?,?,?)",(username,stock,qty,price))
        conn.commit()
        st.success("Added")

    rows = c.execute("SELECT * FROM portfolio WHERE username=?",(username,)).fetchall()
    for r in rows:
        st.write(r)

# ---------- NEWS ----------
elif menu == "News":
    st.title("News Sentiment")

    ticker = st.text_input("Stock")

    if st.button("Check"):
        if not ticker.endswith(".NS"):
            ticker += ".NS"
        sentiment = get_news_sentiment(ticker)
        st.write("Sentiment:", sentiment)

# ---------- ASSISTANT ----------
elif menu == "Assistant":
    st.title("Market Assistant")

    query = st.text_input("Ask something")

    if query:
        word = query.split()[-1].upper()
        if not word.endswith(".NS"):
            ticker = word + ".NS"
        else:
            ticker = word

        data = get_stock_data(ticker)

        if data.empty:
            st.error("Invalid stock")
        else:
            trend = detect_trend(data)
            pred = predict_price(data)
            curr = data['Close'].iloc[-1]

            answer = ai_answer(query, ticker, trend, pred, curr)

            st.write(answer)

# ---------- VIDEO ----------
st.markdown("### AI Market Video")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")