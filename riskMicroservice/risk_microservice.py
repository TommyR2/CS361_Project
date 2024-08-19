import time
import json
import yfinance as yf

class RiskMicroservice:

    def monitor_requests(self):
        with open('risk_request.json', 'r') as file:
            portfolio_data = json.load(file)
            if portfolio_data != {}:
                # Communicate Intention to Terminal
                print('Analyzing Portfolio Risk... ')

                risk_data = self.analyze_risk(portfolio_data)
                self.write_response_data(risk_data)
                return True

    def analyze_risk(self, portfolio_data):
        risk_data = {'Holding Beta' : {},}
        for stock in portfolio_data:
            risk_data['Holding Beta'][stock['Ticker']] = (self.get_stock_beta(stock['Ticker']))
        risk_data['Portfolio_Beta'] = self.get_portfolio_beta(portfolio_data, risk_data)
        return risk_data

    def get_stock_beta(self, ticker):
        stock_name = yf.Ticker(ticker)
        stock_info = stock_name.info
        beta = round(stock_info.get('beta', 1.0),2)
        return beta
    
    def get_portfolio_beta(self, portfolio_data, risk_data):
        portfolio_sum = 0
        for stock in portfolio_data:
            portfolio_sum += stock['Total Cost']
        
        portfolio_beta = 0
        # Now that the total is known
        for stock in portfolio_data:
            ticker = stock['Ticker']
            weight = stock['Total Cost'] / portfolio_sum
            beta = risk_data['Holding Beta'][ticker]
            portfolio_beta += weight * beta

        return round(portfolio_beta,2)

    def write_response_data(self, risk_data):
        with open('risk_response.json', 'w') as file:
                    json.dump(risk_data, file)

    def cleanup_data(self):
        time.sleep(2)
        with open('risk_request.json', 'w') as file:
            json.dump({}, file)

    def start(self):
        print('Starting Risk Microservice...')
        while True:
            action = self.monitor_requests()
            if action:
                self.cleanup_data()
            time.sleep(0.1)

if __name__ == '__main__':
    Service = RiskMicroservice()
    Service.start()
    