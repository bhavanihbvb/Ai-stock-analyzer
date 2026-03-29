def detect_trend(data):
    return "UPTREND" if data['Close'].iloc[-1] > data['Close'].mean() else "DOWNTREND"