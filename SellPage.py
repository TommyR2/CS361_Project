from misc import *
from Order import Order
from tabulate import tabulate
import copy


class SellPage:

    def display_sell_page(self, portfolio):
        """Display the sell page with command options"""

        # Intitial prompts
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
        
        # Receive stock information
        ticker = self.enter_ticker()
        quantity = self.enter_quantity()
        price = self.enter_price()
        order = Order(ticker, quantity, price)

        # User warning
        print("*** Note that all sales are final, and can only be reversed with a Purchase Order ***")

        # Receive and validate command
        command = input("Enter your desired command here: ")
        while command not in ('Confirm', 'Preview', 'Redo', 'Home'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')

         # Facilitate a command
        if command == 'Confirm':
            return self.execute_sale(order)
        
        elif command == 'Preview':
            return self.display_preview(order)

        elif command == 'Redo':
            return self.display_sell_page(self.portfolio)
        
        else:
            return ('Home', self.portfolio) 
        
    def execute_sale(self, order):
        """Sell a single stock"""

        # If the stock exists in the portfolio
        previous_portfolio = copy.copy(self.portfolio)
        for stock in self.portfolio:
            if stock['Ticker'] == order.ticker:
                # If the sale quantity is too large, return with the previous portfolio
                if stock['Quantity'] - order.quantity < 0:
                    print('\n****Sale quantity too large. Returning to Sale Page.****')
                    return self.display_sell_page(previous_portfolio)

                # Remove the stock if it no longer is in the portfolio
                if stock['Quantity'] - order.quantity == 0:
                    self.portfolio.remove(stock)
                    return ('Home', self.portfolio)
                
                # Otherwise subtract the quantity from the position
                stock['Total Value'] = stock['Total Value'] - order.quantity * order.price
                stock['Quantity'] -= order.quantity
                stock['Average Purchase Price'] = stock['Total Value'] / stock['Quantity']
                return ('Home', self.portfolio)
            
        # If the stock does not exist in the portfolio
        print('\n****Stock Not Owned. Returning to Sale Page.****')
        return self.display_sell_page(previous_portfolio)
    
    def display_preview(self, order):
        """Show how a stock sale will impact a portfolio"""

        # If the stock exists in the portfolio
        mock_portfolio = copy.copy(self.portfolio)
        found = False
        for stock in mock_portfolio:
            if stock['Ticker'] == order.ticker:
                
                if stock['Quantity'] - order.quantity == 0:
                    # If the stock is fully sold, remove it
                    mock_portfolio.remove(stock)
                    found = True
                else:
                    # Otherwise subtract the quantity from the position
                    stock['Total Value'] = stock['Total Value'] - order.quantity * order.price
                    stock['Quantity'] -= order.quantity
                    stock['Average sale Price'] = stock['Total Value'] / stock['Quantity']
                    found = True
                    if stock['Quantity'] < 0:
                        # If the sale quantity is too large, return with the mock portfolio
                        print(f"\n****Sale quantity too large.{stock['Quantity']} Returning to Sale Page.****")
                        return self.display_sell_page(mock_portfolio)

        # If the stock does not exist in the portfolio
        if not found:
            print('\n****Stock Not Owned. Returning to Sale Page.****')
            return self.display_sell_page(mock_portfolio)

        # Display the potential portfolio to the user and command options
        print_stars()
        print("Here your portfolio after implementing the current order:\n")
        self.print_table(mock_portfolio)
        print("\n Available Commands are: ")
        print("'Confirm': Execute the current order and return to the home page")
        print("'Cancel' : Discard this order and return to the sell/sell page")

        # Receive and validate a command
        command = input("Enter your desired command here: ")
        while command not in ('Confirm', 'Cancel'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')

        # Facilitate a Command
        if command == 'Confirm':
            self.portfolio = mock_portfolio
            return ('Home', self.portfolio)

        elif command == 'Cancel':
            return self.display_sell_page(self.portfolio)

    def print_table(self, portfolio):
        """Display a given portfolio."""
        
        headers = {'Ticker': "Ticker",
            "Average sale Price": "Average sale Price",
            "Quantity" : "Quantity",
            "Total Value" : "Total Value"}
        print(tabulate(portfolio, headers=headers))

    def enter_ticker(self):
        """Ensure a valid ticker is entered."""

        while True:
            ticker = input('Ticker: ')
            if ticker:
                return ticker
            else:
                print('\nInvalid Ticker\n')

    def enter_quantity(self):
        """Ensure a valid quantity is entered."""
        while True:
            try:
                quantity = int(input('Quantity: '))
                return quantity
            except:
                print('\nInvalid Quantity. Must be an integer\n')

    def enter_price(self):
        """Ensure a valid price is entered."""
        while True:
            try:
                price = float(input('Price: '))
                return price
            except:
                print('\nInvalid Quantity. Must be a float\n')

