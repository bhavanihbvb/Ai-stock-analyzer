import yfinance as yf
from textblob import TextBlob

def get_news_sentiment(ticker):
    news = yf.Ticker(ticker).news
    scores = []

    for n in news[:5]:
        scores.append(TextBlob(n['title']).sentiment.polarity)

    avg = sum(scores)/len(scores) if scores else 0

    if avg > 0: return "Positive"
    if avg < 0: return "Negative"
    return "Neutral"