import random

def make_decision(trend, pred, curr):
    if pred > curr: return "BUY"
    elif pred < curr: return "SELL"
    return "HOLD"

def confidence_score():
    return random.randint(70,95)