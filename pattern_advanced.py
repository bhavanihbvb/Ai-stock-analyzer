from ta.momentum import RSIIndicator

def detect_patterns(data):
    patterns = []

    rsi = RSIIndicator(close=data['Close']).rsi()

    if rsi.iloc[-1] > 70:
        patterns.append("Overbought (RSI)")

    elif rsi.iloc[-1] < 30:
        patterns.append("Oversold (RSI)")

    # Support / Resistance
    support = data['Close'][-20:].min()
    resistance = data['Close'][-20:].max()
    current = data['Close'].iloc[-1]

    if current >= resistance:
        patterns.append("Resistance Breakout")

    elif current <= support:
        patterns.append("Support Level")

    if not patterns:
        patterns.append("No strong pattern")

    return patterns