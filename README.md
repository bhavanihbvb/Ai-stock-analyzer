# StockZen / AI Stock Analyzer

An intelligent, AI-powered stock tracking and analysis dashboard built with Streamlit. StockZen uses a variety of AI agents to analyze market sentiment, detect trading patterns, and provide smart price predictions to help you manage your portfolio and make informed financial decisions.

## Features

- **Smart Investor Dashboard**: Real-time stock analysis, price prediction, and trend detection.
- **Pattern Intelligence**: Automatically detects advanced market patterns.
- **Market Sentiment Analysis**: Analyzes recent news to determine market sentiment for specific stocks.
- **Portfolio Management**: Add stocks to your portfolio and get AI-driven portfolio advice based on your holdings.
- **Market Assistant**: A chat assistant that you can ask about specific market trends or stock performances.
- **Decision Engine**: Generates automated buying/selling decisions based on backtested models.
- **Opportunity Radar**: Scans for potential trading opportunities automatically.

## AI Agents Used

- `data_agent.py` - Fetches and processes stock data.
- `pattern_agent.py` & `pattern_advanced.py` - Technical and chart pattern detection.
- `prediction_agent.py` - Price prediction modeling.
- `decision_agent.py` - Rules engine to determine buy/sell/hold decisions.
- `explanation_agent.py` - Generates natural language explanations for decisions.
- `sentiment_agent.py` - News scraper and sentiment analyzer.
- `portfolio_agent.py` - Portfolio composition advisor.
- `assistant_agent.py` - Natural language query interface.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bhavanihbvb/Ai-stock-analyzer.git
   cd Ai-stock-analyzer
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   The application is built using Streamlit. To start the local server, run:
   ```bash
   streamlit run app.py
   ```

## Disclaimer

This software is for educational and informational purposes only and does not constitute financial advice. Always do your own research before making any investment decisions.
