from misc import *
from Order import Order
from tabulate import tabulate
import copy


class BuyPage:

    def display_buy_page(self, portfolio):
        self.portfolio = portfolio
        print_stars()
        print("Welcome to the BUY Page.\n")
        print("Please enter all of the relevant stock information below.\n")

        print("After entering all information, please enter one of three available commands:")
        print("'Confirm' : Confirm that you would like to continue with the purchase")
        print("'Preview' : View how your new portfolio will look before making this purchase")
        print("'Redo'    : Re-enter stock information to update one of the fields")
        print("'Home'    : Your entry will be discarded and immediately returned to the Home Page")

        print("Purchase Information\n")
        
        ticker = input("Ticker: ")
        quantity = int(input("Quantity Purchased: "))
        price = float(input("Purchase Price: "))
        date = input("Date Purchased (YYYY-MM-DD): ")
        order = Order(ticker, quantity, price,date)

        print("*** Note that all Purchases are final, and can only be reversed with a Sell Order ***")

        command = input("Enter your desired command here: ")

        while command not in ('Confirm', 'Preview', 'Redo', 'Home'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')

        if command == 'Confirm':
            return self.execute_purchase(order)
        
        elif command == 'Preview':
            return self.display_preview(order)

        elif command == 'Redo':
            self.display_buy_page(self.portfolio)
        
        else:
            return ('Home', self.portfolio) 
        
    def execute_purchase(self, order):
        # If the stock exists in the portfolio
        for stock in self.portfolio:
            if stock['Ticker'] == order.ticker:
                added_value = order.quantity * order.price
                stock['Total Value'] += added_value
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
        # If the stock exists in the portfolio
        mock_portfolio = copy.copy(self.portfolio)
        found = False
        for stock in mock_portfolio:
            if stock['Ticker'] == order.ticker:
                added_value = order.quantity * order.price
                stock['Total Value'] += added_value
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

        print_stars()

        print("Here your portfolio after implementing the current order:\n")

        self.print_table(mock_portfolio)

        print("\n Available Commands are: ")
        print("'Confirm': Execute the current order and return to the home page")
        print("'Cancel' : Discard this order and return to the buy/sell page")

        command = input("Enter your desired command here: ")

        while command not in ('Confirm', 'Cancel'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')

        if command == 'Confirm':
            return self.execute_purchase(order)

        elif command == 'Cancel':
            return self.display_buy_page(self.portfolio)

    def print_table(self, portfolio):
        headers = {'Ticker': "Ticker",
            "Average Purchase Price": "Average Purchase Price",
            "Quantity" : "Quantity",
            "Total Value" : "Total Value"}
        print(tabulate(portfolio, headers=headers))

        


  