import time
from data_agent import get_stock_data
from prediction_agent import predict_price

def market_scanner(stocks):
    alerts = []

    for s in stocks:
        data = get_stock_data(s)

        if data.empty:
            continue

        pred = predict_price(data)
        curr = data['Close'].iloc[-1]

        if pred > curr * 1.05:
            alerts.append(f"{s} → Breakout Opportunity")

    return alerts