def backtest(data):
    correct = 0

    for i in range(1, len(data)-1):
        if data['Close'].iloc[i+1] > data['Close'].iloc[i]:
            correct += 1

    return round((correct / len(data)) * 100, 2)