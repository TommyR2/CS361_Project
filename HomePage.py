import json
import textwrap
from misc import *

class HomePage:

    def display_home_page(self, portfolio):
        print_stars()
        print('Welcome to the Portfolio Home\n')
        print('You can use this as a central hub to access all of the application features.\n')
        print("'Logout' : Navigate to the login page")
        print("'Buy'  : Enter a purchase order")
        print("'Sell' : Enter a sell order")
        print("'View' : View your current portfolio")
        print("'Upload' : Upload a file containing past orders to quickly create a portfolio")
        print("'Reset' : Completely Reset Your Current Portfolio From Scratch")

        command = input('Enter your desired command here: ')
        while command not in ('Logout', 'Buy', 'Sell', 'View', 'Upload', 'Reset'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')
        
        if command == "Reset":
            confirmation = input("\n**** WARNING You are about to reset all portfolio history. Please type 'CONFIRM' to execute this command ****.\n")
            if confirmation == "CONFIRM":
                portfolio = {}
                print(" \nPortfolio has been reset. \n")
            else:
                return self.display_home_page(portfolio)

        return command, portfolio
        



