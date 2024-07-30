from misc import *
from Order import Order
from tabulate import tabulate
import copy


class SellPage:

    def display_sell_page(self, portfolio):
        self.portfolio = portfolio
        print_stars()
        print("Welcome to the SELL Page.\n")
        print("Please enter all of the relevant stock information below.\n")

        print("After entering all information, please enter one of three available commands:")
        print("'Confirm' : Confirm that you would like to continue with the sale")
        print("'Preview' : View how your new portfolio will look before making this sale")
        print("'Redo'    : Re-enter stock information to update one of the fields")
        print("'Home'    : Your entry will be discarded and immediately returned to the Home Page")

        print("sale Information\n")
        
        ticker = input("Ticker: ")
        quantity = int(input("Quantity sold: "))
        price = float(input("Sale Price: "))
        date = input("Date Sold (YYYY-MM-DD): ")
        order = Order(ticker, quantity, price,date)

        print("*** Note that all sales are final, and can only be reversed with a Purchase Order ***")

        command = input("Enter your desired command here: ")

        while command not in ('Confirm', 'Preview', 'Redo', 'Home'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')

        if command == 'Confirm':
            return self.execute_sale(order)
        
        elif command == 'Preview':
            return self.display_preview(order)

        elif command == 'Redo':
            self.display_sell_page(self.portfolio)
        
        else:
            return ('Home', self.portfolio) 
        
    def execute_sale(self, order):
        # If the stock exists in the portfolio
        for stock in self.portfolio:
            if stock['Ticker'] == order.ticker:
                if stock['Quantity'] - order.quantity < 0:
                    print('\n****Sale quantity too large. Returning to Sale Page.****')
                    return self.display_sell_page(self.portfolio)

                # Remove the stock if it no longer is in the portfolio
                if stock['Quantity'] - order.quantity == 0:
                    self.portfolio.remove(stock)
                    return ('Home', self.portfolio)
                
                lost_value = order.quantity * order.price
                stock['Total Value'] -= lost_value
                stock['Quantity'] -= order.quantity
                stock['Average Purchase Price'] = stock['Total Value'] / stock['Quantity']
                return ('Home', self.portfolio)
            
        # If the stock does not exist in the portfolio
        print('\n****Stock Not Owned. Returning to Sale Page.****')
        return self.display_sell_page(self.portfolio)
    
    def display_preview(self, order):
        # If the stock exists in the portfolio
        mock_portfolio = copy.copy(self.portfolio)
        found = False
        for stock in mock_portfolio:
            if stock['Ticker'] == order.ticker:
                if stock['Quantity'] - order.quantity == 0:
                    mock_portfolio.remove(stock)
                    found = True
                else:
                    added_value = order.quantity * order.price
                    stock['Total Value'] -= added_value
                    stock['Quantity'] -= order.quantity
                    stock['Average sale Price'] = stock['Total Value'] / stock['Quantity']
                    found = True
                    if stock['Quantity'] < 0:
                        print(f"\n****Sale quantity too large.{stock['Quantity']} Returning to Sale Page.****")
                        return self.display_sell_page(self.portfolio)

        # If the stock does not exist in the portfolio
        if not found:
            print('\n****Stock Not Owned. Returning to Sale Page.****')
            return self.display_sell_page(self.portfolio)

        print_stars()

        print("Here your portfolio after implementing the current order:\n")

        self.print_table(mock_portfolio)

        print("\n Available Commands are: ")
        print("'Confirm': Execute the current order and return to the home page")
        print("'Cancel' : Discard this order and return to the sell/sell page")

        command = input("Enter your desired command here: ")

        while command not in ('Confirm', 'Cancel'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')

        if command == 'Confirm':
            return self.execute_sale(order)

        elif command == 'Cancel':
            return self.display_sell_page(self.portfolio)

    def print_table(self, portfolio):
        headers = {'Ticker': "Ticker",
            "Average sale Price": "Average sale Price",
            "Quantity" : "Quantity",
            "Total Value" : "Total Value"}
        print(tabulate(portfolio, headers=headers))
