import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor

import streamlit as st

@st.cache_data(show_spinner=False)
def predict_price(data):
    prices = data['Close'].values.reshape(-1,1)
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(prices)

    X = [scaled[i-60:i] for i in range(60, len(scaled))]
    X = np.array(X)

    # Simple RandomForest regression model (no TensorFlow)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    # reshape X for sklearn (samples, features)
    X_flat = X.reshape(X.shape[0], -1)
    y = scaled[60:].ravel()
    model.fit(X_flat, y)
    # Predict next price using the last 60 days
    last_flat = scaled[-60:].reshape(1, -1)
    pred_scaled = model.predict(last_flat)
    pred = scaler.inverse_transform(pred_scaled.reshape(-1, 1))

    return float(pred[0][0])