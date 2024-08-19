from misc import *
import time
import json

class RiskPage:
    def display_risk_page(self, portfolio):
        self.portfolio = portfolio
        print_stars()
        print("Welcome to the Risk Page.\n")
        print('Here you can see the Risk of each of your holdings, as well as your portfolio.')
        print("The beta of a stock, or portfolio is an indicator of its risk compared to a benchmark (here the S&P 500).")
        print("A beta greater than one indicates price fluctuations greater than those of the index.")
        print("A beta lower than one indicates price fluctuations less than those of the index.")
        print("Often a large beta indicates greater returns, at the cost of added risk. Vice Versa for small betas.")
        print("Here is your portfolio's risk analysis: \n")

        self.send_risk_request(self.portfolio)
        print('\nLOADING\n')
        time.sleep(1)
        risk_data = self.risk_response()
        print(f"Your Portolio Beta for current holdings has been: {risk_data['Portfolio_Beta']} \n")
        print("Individual Holding Risk: \n")
        for key, value in risk_data['Holding Beta'].items():
            print(f"{key:<5}: Holding Beta: {value}")
        
        portfolio_message = self.get_portfolio_message(risk_data)
        print(f'\n{portfolio_message}')


        # Receive and Validate Command
        command = input("Please Enter 'Home' to return to the Home page: ")
        while command != 'Home':
            print('Invalid Command\n')
            command = input("Please Enter 'Home' to return to the Home page: ")
        return ('Home', self.portfolio)
    
    def send_risk_request(self, portfolio):
        with open('riskMicroservice/risk_request.json', 'w') as file:
            json.dump(portfolio, file, indent=4)

    def risk_response(self):
        with open('riskMicroservice/risk_response.json', 'r') as file:
            risk_data = json.load(file)
            return risk_data 

    def get_portfolio_message(self, risk_data):
        portfolio_risk = risk_data['Portfolio_Beta']
        if 0.8 <= portfolio_risk <= 1.2:
            return "Portfolio Risk is similar to the S&P500."
        elif 0.8 > portfolio_risk:
            return "Portfolio Risk is significantly lower than the S&P500."
        else:
            return "Portfolio Risk is significantly greater than the S&P500."
