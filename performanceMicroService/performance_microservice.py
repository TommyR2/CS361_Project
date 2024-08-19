import time
import json
import yfinance as yf

class PerformanceMicroservice:

    def monitor_requests(self):
        with open('performance_request.json', 'r') as file:
            portfolio_data = json.load(file)
            if portfolio_data != {}:
                performance_data = self.analyze_performance(portfolio_data)
                self.write_response_data(performance_data)
                return True

    def analyze_performance(self, portfolio_data):
        performance_data = {'Holding Performance' : {},}
        for stock in portfolio_data:
            purchase_price = stock['Average Purchase Price']
            current_price = self.get_stock_price(stock['Ticker'])
            profit = str(round((((current_price / purchase_price) - 1) * 100), 2)) + ' %'
            performance_data['Holding Performance'][stock['Ticker']] = (purchase_price, current_price, profit)
        performance_data['Portfolio_Performance'] = self.get_portfolio_performance(portfolio_data, performance_data)
        return performance_data

    def get_stock_price(self, ticker):
        stock_name = yf.Ticker(ticker)
        stock_info = stock_name.info
        trading_price = stock_info.get('regularMarketPrice', 'N/A')
        if trading_price == 'N/A':  
            trading_price = stock_name.history(period='1mo').iloc[0]['Close']
        return round(trading_price, 2)
    
    def get_portfolio_performance(self, portfolio_data, performance_data):
        starting_value = 0
        ending_value = 0
        for stock in portfolio_data:
            starting_value += stock['Total Cost'] 
            ending_value += stock['Quantity'] * performance_data['Holding Performance'][stock['Ticker']][1]
         
        return str(round((((ending_value / starting_value) - 1) * 100), 2)) + ' %'

    def write_response_data(self, performance_data):
        with open('performance_response.json', 'w') as file:
                    json.dump(performance_data, file)

    def cleanup_data(self):
        time.sleep(1)
        with open('performance_request.json', 'w') as file:
            json.dump({}, file)

    def start(self):
        while True:
            action = self.monitor_requests()
            if action:
                self.cleanup_data()
            time.sleep(0.1)

if __name__ == '__main__':
    Service = PerformanceMicroservice()
    Service.start()
    