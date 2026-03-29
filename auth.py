import streamlit as st
import sqlite3
import hashlib

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup():
    st.subheader("Create Account")
    user = st.text_input("Username", key="su_user")
    pwd = st.text_input("Password", type="password", key="su_pwd")

    if st.button("Sign Up"):
        if user and pwd:
            try:
                c.execute("INSERT INTO users VALUES (?, ?)", (user, hash_password(pwd)))
                conn.commit()
                st.success("Account created. Please login.")
            except:
                st.error("Username already exists")
        else:
            st.warning("Fill all fields")

def login():
    st.subheader("Login")
    user = st.text_input("Username", key="li_user")
    pwd = st.text_input("Password", type="password", key="li_pwd")

    if st.button("Login"):
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (user, hash_password(pwd)))
        if c.fetchone():
            st.session_state["logged_in"] = True
            st.session_state["username"] = user
            st.rerun()
        else:
            st.error("Invalid credentials")

def auth_page():
    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    st.title("Smart Investor AI")
    choice = st.radio("", ["Login", "Sign Up"])
    login() if choice == "Login" else signup()
    st.markdown('</div>', unsafe_allow_html=True)

def logout():
    st.session_state["logged_in"] = False
    st.rerun()