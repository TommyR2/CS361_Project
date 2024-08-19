import textwrap
from misc import *
import json
import time

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
        print('\nLogin Credentials')
        print('\nAvailable commands are: ')
        print("'Login' :  Login to an existing account")
        print("'Create' : Create a new account")
        command = input('Enter your desired command here: ')
        while command not in ('Login', 'Create'):
            print('Invalid Command\n')
            command = input('Enter your desired command here: ')
        if command == 'Login':
            return self.accept_login_data()
        if command == 'Create':
            return self.accept_create_data()
        
    def accept_login_data(self):
        self.validated = False
        while not self.validated:
            print('\nEnter Login Credentials here...\n')
            username = input('Username: ')
            password = input('Password: ')
            confirmation = input("Enter 'Confirm' or 'Cancel' : ")
            while confirmation not in ('Confirm', 'Cancel'):
                print('Invalid Command\n')
                confirmation = input("Enter 'Confirm' or 'Cancel' : ")
            if confirmation == 'Confirm':
                response = self.validate_login(username, password)
                if response == 'Invalid Credentials':
                    print("INVALID CREDENTIALS\n")
                    print("Returning to Login Page")
                    time.sleep(1)
                    return ('Login', None, None)

                else:
                    return ('Home', response, username)

            elif confirmation == 'Cancel':
                return ('Login', None, None)

    def validate_login(self, username, password):
        """Check if the given credentials are in list of portfolios"""
        # Send login credentials to login microservice
        with open('loginMicroservice/login_requests.json', 'w') as file:
            login_data = {
                    "account_type": "existing",
                    "username" : username,
                    "password" : password
                    }
            json.dump(login_data, file)
        
        time.sleep(0.2)
        portfolio_data = self.get_login_response()
        return portfolio_data
            
    def get_login_response(self):
        with open('loginMicroService/login_response.json', 'r') as file:
            portfolio_data = json.load(file)
            return portfolio_data
                
    def accept_create_data(self):
        self.validated = False
        while not self.validated:
            print('\nEnter New Login Credentials here...\n')
            username = input('Username: ')
            password = input('Password: ')
            confirmation = input("Enter 'Confirm' or 'Cancel' : ")
            while confirmation not in ('Confirm', 'Cancel'):
                print('Invalid Command\n')
                confirmation = input("Enter 'Confirm' or 'Cancel' : ")
            if confirmation == 'Confirm':
                response = self.validate_create(username, password)
                if response == 'Duplicate User':
                    print("USERNAME ALREADY IN USE\n")
                    print("Returning to Login Page")
                    time.sleep(1)
                    return ('Login', None, None)

                else:
                    return ('Home', response, username)

            elif confirmation == 'Cancel':
                return ('Login', None, None)
            
    def validate_create(self, username, password):
        with open('loginMicroService/login_requests.json', 'w') as file:
            login_data = {
                    "account_type": "new",
                    "username" : username,
                    "password" : password
                    }
            json.dump(login_data, file)
        
        time.sleep(0.2)
        portfolio_data = self.get_login_response()
        return portfolio_data