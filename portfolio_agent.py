from data_agent import get_stock_data
from prediction_agent import predict_price

def portfolio_advice(stocks):
    advice = []

    for s in stocks:
        data = get_stock_data(s)

        if data.empty:
            continue

        pred = predict_price(data)
        curr = data['Close'].iloc[-1]

        if pred < curr:
            advice.append(f"Consider exiting {s}")
        else:
            advice.append(f"{s} looks strong")

    return advice