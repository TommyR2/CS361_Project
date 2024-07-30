from misc import *
from tabulate import tabulate

class ViewPage:
    def display_view_page(self, portfolio): 
        print_stars()
        print("Welcome to the VIEW Page.\n")
        print("Current Holdings")

        self.print_table(portfolio)


        command = input("Please Enter 'Home' to return to the Home page: ")
        while command != 'Home':
            print('Invalid Command\n')
            command = input("Please Enter 'Home' to return to the Home page: ")
        
        return 'Home'
    
    def print_table(self, portfolio):
        headers = {'Ticker': "Ticker",
            "Average Purchase Price": "Average Purchase Price",
            "Quantity" : "Quantity",
            "Total Value" : "Total Value"}
        print(tabulate(portfolio, headers=headers))

