from misc import *
import csv
from Order import Order

class UploadPage:

    def display_upload_page(self, portfolio):
        """Display the buy page with command options"""
        self.portfolio = portfolio

        # Initial Prompts
        print_stars()
        print("Welcome to the UPLOAD Page.\n")
        print("If you would likely to quickly populate a large portfolio, \n\
enter the path to a CSV file holding order history in the following format: \n")
        print("Order Type('Buy'/'Sell'), Ticker, Quantity, Purchase/Sale Price \n")
        print("An example row may look like this:")
        print("Buy, AAPL, 12, 230.45 \n")

        # Accept a valid file path
        file_path = input("Enter File Path Here:")

        # Prompt user with inputs
        print("Confirm/Cancel your request with the available commands: ")
        print("'Upload' : All orders in the CSV file at the specified path will now be reflected")
        print("'Home'   : Return to the home page without executing the upload")

        # Receive and validate a command
        command = input("Enter your desired command here: ")
        while command not in ('Upload', 'Home'):
            print('Invalid Command\n')
            command = input("Enter your desired command here: ")

        # Facilitate a command
        if command == 'Home':
            return ('Home', self.portfolio)
        
        if command == 'Upload':
            self.update_portfolio(file_path)
            return ('Home', self.portfolio)

    def update_portfolio(self, file_path):
        """Use the file path to buy / sell stocks."""

        try:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    order_type, ticker, quantity, price = row
                    order = Order(ticker, int(quantity), float(price))
                    if order_type == 'Buy':
                        self.execute_purchase(order)
                    elif order_type == 'Sell':
                        self.execute_sale(order)
                print("Upload Completed, returning you to the Home Page")
        except:
            print("\nError locating file. Returning Home.\n")
                
    def execute_purchase(self, order):
        """Purchase a single stock"""
        
        # If the stock exists in the portfolio
        found = False
        for stock in self.portfolio:
            if stock['Ticker'] == order.ticker:
                found = True
                stock['Total Cost'] = stock['Total Cost'] + order.quantity * order.price
                stock['Quantity'] += order.quantity
                stock['Average Purchase Price'] = stock['Total Cost'] / stock['Quantity']

        if not found:
            # If the stock does not exist in the portfolio
            new_stock = {"Ticker": order.ticker,
                        "Average Purchase Price": order.price,
                        "Quantity": order.quantity,
                        "Total Cost": order.price * order.quantity}
            self.portfolio.append(new_stock)

    def execute_sale(self, order):
        # If the stock exists in the portfolio
        found = False
        for stock in self.portfolio:
            if stock['Ticker'] == order.ticker:
                found = True
                # If the sale quantity is too large, skip this order
                if order.quantity > stock['Quantity']:
                    print(f'Failed to execute order for {order.ticker} at {order.price} \n')
                    break
                 # Remove the stock if it no longer is in the portfolio
                elif stock['Quantity'] - order.quantity == 0:
                    self.portfolio.remove(stock)
                    break
                # Otherwise subtract the quantity from the position
                stock['Quantity'] -= order.quantity
                stock['Total Cost'] = stock['Average Purchase Price'] * stock['Quantity']
            
        if not found:
            # If the stock does not exist in the portfolio
            print(f'Failed to execute order for {order.ticker} at {order.price}')

