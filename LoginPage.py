import textwrap
from misc import *
import json

class LoginPage:

    def display_login(self):
        """Print the Login page and accept username credentials"""

        # Initial Prompts
        print_stars()
        print('Welcome to PortfolioTracker\n')
        intro_text = '''The program designed to track, update and analyze your equity
portfolio. Current features include 'Buy', 'Sell', and 'View' allowing
users to track their portfolio and view their holdings via sorted displays 
or filters. This portfolio helps users track their investments and will allow
future features to perform performance and risk analysis, helping users to make
more intelligent investing decisions.\n'''
        intro_text = textwrap.fill(intro_text, width=70)
        print(intro_text)
        
        # Continuously prompt login until successful
        portfolio = None
        while not portfolio:
            print('\nEnter Login Credentials here...\n')
            username = input('Username: ')
            password = input('Password: ')
            portfolio = self.validate_login(username, password)
            
        return ('Home', portfolio, username)

    def validate_login(self, username, password):
        """Check if the given credentials are in list of portfolios"""
        
        with open('portfolios.json', 'r') as file:
            portfolio_data = json.load(file)
            users = portfolio_data['Portfolios']

            for user in users:
                if user['Username'] == username and password == user['Password']:
                    return user['Stocks']
                else:
                    print('Invalid Credentials')
                    return None