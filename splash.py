import streamlit as st

def show_splash():

    st.markdown("""
    <style>
    .splash {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: radial-gradient(circle at center, #7a0c0c 0%, #3a0000 50%, #000000 100%);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }

    .title {
        font-size: 6rem;
        font-weight: bold;
        color: #f5e6dc;
    }

    .tagline {
        margin-top: 20px;
        font-size: 1.2rem;
        color: #e0cfc5;
    }

    .footer {
        position: absolute;
        bottom: 60px;
        font-size: 0.8rem;
        color: #c7b1a5;
    }
    </style>

    <div class="splash">
        <div class="title">StockZen</div>
        <div class="tagline">Stop Guessing. Start Investing Smart.</div>
        <div class="footer">INTELLIGENCE • ANALYSIS • DECISIONS</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Enter →"):
        st.session_state["splash_done"] = True