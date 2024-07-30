from misc import *
import csv
from Order import Order

class UploadPage:

    def display_upload_page(self, portfolio):
        self.portfolio = portfolio
        print_stars()
        print("Welcome to the UPLOAD Page.\n")
        print("If you would likely to quickly populate a large portfolio, \n\
enter the path to a CSV file holding order history in the following format: \n")
        print("Order Type('Buy'/'Sell'), Ticker, Quantity, Purchase/Sale Price, Date(YYYY-MM-DD) \n")
        print("An example row may look like this:")
        print("Buy, AAPL, 12, 230.45, 2024-08-01 \n")

        file_path = input("Enter File Path Here:")

        print("Confirm/Cancel your request with the available commands: ")
        print("'Upload' : All orders in the CSV file at the specified path will now be reflected")
        print("'Home'   : Return to the home page without executing the upload")

        command = input("Enter your desired command here: ")
        
        while command not in ('Upload', 'Home'):
            print('Invalid Command\n')
            command = input("Enter your desired command here: ")

        if command == 'Home':
            return ('Home', self.portfolio)
        
        if command == 'Upload':
            self.update_portfolio(file_path)
            print("Upload Completed, returning you to the Home Page")
            return ('Home', self.portfolio)

    def update_portfolio(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                order_type, ticker, quantity, price, date = row
                order = Order(ticker, int(quantity), float(price), date)
                if order_type == 'Buy':
                    self.execute_purchase(order)
                elif order_type == 'Sell':
                    self.execute_sale(order)
                
    def execute_purchase(self, order):
        # If the stock exists in the portfolio
        found = False
        for stock in self.portfolio:
            if stock['Ticker'] == order.ticker:
                found = True
                added_value = order.quantity * order.price
                stock['Total Value'] += added_value
                stock['Quantity'] += order.quantity
                stock['Average Purchase Price'] = stock['Total Value'] / stock['Quantity']

        if not found:
            # If the stock does not exist in the portfolio
            new_stock = {"Ticker": order.ticker,
                        "Average Purchase Price": order.price,
                        "Quantity": order.quantity,
                        "Total Value": order.price * order.quantity}
            self.portfolio.append(new_stock)

    def execute_sale(self, order):
        # If the stock exists in the portfolio
        found = False
        for stock in self.portfolio:
            if stock['Ticker'] == order.ticker:
                found = True
                if order.quantity > stock['Quantity']:
                    print(f'Failed to execute order for {order.ticker} at {order.price} \n')
                    break
                lost_value = order.quantity * order.price
                stock['Total Value'] -= lost_value
                stock['Quantity'] -= order.quantity
                stock['Average Purchase Price'] = stock['Total Value'] / stock['Quantity']
            
        if not found:
            # If the stock does not exist in the portfolio
            print(f'Failed to execute order for {order.ticker} at {order.price}')

