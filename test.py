import yfinance as yf

ticker = 'AAPL'
stock_name = yf.Ticker(ticker)
stock_info = stock_name.info
print(stock_info)