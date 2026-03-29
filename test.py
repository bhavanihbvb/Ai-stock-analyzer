from data_agent import get_stock_data

data = get_stock_data("AAPL")
print(data.head())