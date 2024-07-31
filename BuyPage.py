from misc import *
from Order import Order
from tabulate import tabulate
import copy


class BuyPage:

    def display_buy_page(self, portfolio):
        """Display the buy page with command options"""
        self.portfolio = portfolio

        # Intitial prompts
        print_stars()
        print("Welcome to the BUY Page.\n")
        print("Please enter all of the relevant stock information below.\n")
        print("After entering all information, please enter one of three available commands:")
        print("'Confirm' : Confirm that you would like to continue with the purchase")
        print("'Preview' : View how your new portfolio will look before making this purchase")
        print("'Redo'    : Re-enter stock information to update one of the fields")
        print("'Home'    : Your entry will be discarded and immediately returned to the Home Page")
        print("Purchase Information\n")
        
        # Receive stock information
        ticker = self.enter_ticker()
        quantity = self.enter_quantity()
        price = self.enter_price()
        date = self.enter_date()
        order = Order(ticker, quantity, price,date)

        # User warning
        print("*** Note that all Purchases are final, and can only be reversed with a Sell Order ***")

        # Receive and validate command
        command = input("Enter your desired command here: ")
        while command not in ('Confirm', 'Preview', 'Redo', 'Home'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')

        # Facilitate a command
        if command == 'Confirm':
            return self.execute_purchase(order)
        
        elif command == 'Preview':
            return self.display_preview(order)

        elif command == 'Redo':
            self.display_buy_page(self.portfolio)
        
        else:
            return ('Home', self.portfolio) 
        
    def execute_purchase(self, order):
        """Purchase a single stock"""

        # If the stock exists in the portfolio
        for stock in self.portfolio:
            if stock['Ticker'] == order.ticker:
                added_value = order.quantity * order.price
                stock['Total Value'] = stock['Total Value'] + order.quantity * order.price
                stock['Quantity'] += order.quantity
                stock['Average Purchase Price'] = stock['Total Value'] / stock['Quantity']
                return ('Home', self.portfolio)

        # If the stock does not exist in the portfolio
        new_stock = {"Ticker": order.ticker,
                     "Average Purchase Price": order.price,
                     "Quantity": order.quantity,
                     "Total Value": order.price * order.quantity}
        self.portfolio.append(new_stock)
        return ('Home', self.portfolio)
    
    def display_preview(self, order):
        """Show how a stock purchase will impact a portfolio"""

        # Make the potential changes in a copied portfolio
        # If the stock exists in the portfolio
        mock_portfolio = copy.copy(self.portfolio)
        found = False
        for stock in mock_portfolio:
            if stock['Ticker'] == order.ticker:
                stock['Total Value'] = stock['Total Value'] + order.quantity * order.price
                stock['Quantity'] += order.quantity
                stock['Average Purchase Price'] = stock['Total Value'] / stock['Quantity']
                found = True

        # If the stock does not exist in the portfolio
        if not found:
            new_stock = {"Ticker": order.ticker,
                        "Average Purchase Price": order.price,
                        "Quantity": order.quantity,
                        "Total Value": order.price * order.quantity}
            mock_portfolio.append(new_stock)

        # Display the potential portfolio to the user and command options
        print_stars()
        print("Here is your portfolio after implementing the current order:\n")
        self.print_table(mock_portfolio)
        print("\n Available Commands are: ")
        print("'Confirm': Execute the current order and return to the home page")
        print("'Cancel' : Discard this order and return to the buy/sell page")

        # Receive and validate a command
        command = input("Enter your desired command here: ")
        while command not in ('Confirm', 'Cancel'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')

        # Facilitate a command
        if command == 'Confirm':
            self.portfolio = mock_portfolio
            return ('Home', self.portfolio)

        elif command == 'Cancel':
            return self.display_buy_page(self.portfolio)

    def print_table(self, portfolio):
        """Display a given portfolio."""

        headers = {'Ticker': "Ticker",
            "Average Purchase Price": "Average Purchase Price",
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

    def enter_date(self):
        """Ensure a valid date is entered."""

        while True:
            date = input('Date (YYYY-MM-DD): ')
            if date:
                return date
            else:
                print('\nInvalid Date\n')


  