def find_opportunity(data, predicted_price, current_price):
    signals = []

    last_20_high = data['Close'][-20:].max()

    if current_price > last_20_high:
        signals.append("Breakout detected")

    if predicted_price > current_price * 1.05:
        signals.append("Strong upside potential (>5%)")

    if 'Volume' in data.columns:
        if data['Volume'].iloc[-1] > data['Volume'].mean():
            signals.append("High trading volume")

    if not signals:
        signals.append("No strong opportunity")

    return signals