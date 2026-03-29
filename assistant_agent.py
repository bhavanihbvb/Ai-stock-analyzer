def ai_answer(query, ticker, trend, pred, curr):
    q = query.lower()

    if "buy" in q:
        if pred > curr:
            return f"Yes, {ticker} shows upside potential based on prediction and trend"
        else:
            return f"No, {ticker} shows risk based on current analysis"

    elif "sell" in q:
        if pred < curr:
            return f"Yes, selling {ticker} may reduce risk"
        else:
            return f"Holding {ticker} is better"

    elif "trend" in q:
        return f"The current trend of {ticker} is {trend}"

    elif "why" in q:
        return f"Decision is based on trend={trend}, predicted={round(pred,2)}, current={round(curr,2)}"

    else:
        return "Ask about buy/sell/trend/why"