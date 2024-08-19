from misc import *
import time
import json

class ResearchPage:

    def display_research_page(self, portfolio):
        self.portfolio = portfolio
        print_stars()
        print("Welcome to the Research Page.\n")
        print("Enter a Stock Ticker to See Summary Information.\n")
        print("An Empty Ticker will return you to the Home page \n")
        ticker = input("Ticker: ")
        if not ticker:
            return ('Home', self.portfolio) 
        
        self.update_ticker(ticker)
        print('\nLOADING\n')
        time.sleep(1)
        data = self.read_stock_summary()
        
        print("Stock Information")
        print(f"Ticker : {data['ticker']}")
        print(f"Company Name : {data['company_name']}")
        print(f"Last Price : {data['trading_price']}")
        print(f"Average Volume : {data['volume']} \n")

        print("Please enter one of the following commands:")
        print("'New' : Continue Researching More Tickers")
        print("'Home' : Return to the Home Page")
        command = input("Enter your desired command here: ")
        while command not in ('New', 'Home'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')
        if command == 'Home':
            return ('Home', self.portfolio) 
        elif command == 'New':
            return ('Research', self.portfolio)

    def update_ticker(self, ticker):
        with open('stockMicroservice/ticker.txt', 'w') as file:
            file.write(ticker)

    # Function to read the stock summary
    def read_stock_summary(self):
        with open('stockMicroservice/stock_summary.json', 'r') as file:
            stock_data = json.load(file)
            return stock_data