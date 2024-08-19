import yfinance as yf
import json
import time

#function to read the ticker file.
def read_ticker_file(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()

#function to write the stock summary in the json file.
def write_stock_summary(file_path, stock_data):
    with open(file_path, 'w') as file:
        json.dump(stock_data, file, indent=4)

#function to fetch all the stock statistics.
def fetch_stock_data(ticker):
    try:
        stock_name = yf.Ticker(ticker)
        stock_info = stock_name.info
        trading_price = stock_info.get('regularMarketPrice', 'N/A')
        if trading_price == 'N/A':  
            trading_price = stock_name.history(period='1mo').iloc[0]['Close']
        
        stock_data = {
            "ticker": ticker,
            "company_name": stock_info.get('longName', 'N/A'),
            "trading_price": trading_price,
            "volume": stock_info.get('volume', 'N/A')
        }
        return stock_data
    except Exception as e:
        print(f"Error fetching data for ticker {ticker}: {e}")
        return {
            "ticker": ticker,
            "company_name": "N/A",
            "trading_price": "N/A",
            "volume": "N/A"
        }

#function to run the microservice.
def run_microservice(ticker_file, output_file):
    last_ticker = None
    while True:
        ticker = read_ticker_file(ticker_file)
        if ticker and ticker != last_ticker and ticker != "None":
            print(f"Processing ticker: {ticker}")
            stock_data = fetch_stock_data(ticker)
            write_stock_summary(output_file, stock_data)
            last_ticker = ticker
        time.sleep(0.1) 

if __name__ == "__main__":
    ticker_file_path = 'ticker.txt'
    output_file_path = 'stock_summary.json'
    run_microservice(ticker_file_path, output_file_path)