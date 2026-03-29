def explain(decision, trend, pred, curr):
    return f"""
Decision: {decision}

Trend: {trend}
Current Price: {round(curr,2)}
Predicted Price: {round(pred,2)}
"""