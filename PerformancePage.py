from misc import *
import time
import json

class PerformancePage:
    def display_performance_page(self,portfolio):
        self.portfolio = portfolio
        print_stars()
        print("Welcome to the Performance Page.\n")
        print('Here you can see the performance of each of your holdings, as well as your portfolio.')

        self.send_performance_request(self.portfolio)
        print('\nLOADING\n')
        time.sleep(1)
        performance_data = self.performance_response()
        print(f"Your Portolio Return for current holdings has been: {performance_data['Portfolio_Performance']} \n")
        print("Individual Holding Performance: \n")
        for key, value in performance_data['Holding Performance'].items():
            print(f"{key:<5}: Average Purchase Price: {value[0]:>8}, Current Price: {value[1]:>8}, Performance: {value[2]:>8}")


        # Receive and Validate Command
        command = input("Please Enter 'Home' to return to the Home page: ")
        while command != 'Home':
            print('Invalid Command\n')
            command = input("Please Enter 'Home' to return to the Home page: ")
        return ('Home', self.portfolio)
    
    def send_performance_request(self, portfolio):
        with open('performanceMicroservice/performance_request.json', 'w') as file:
            json.dump(portfolio, file, indent=4)

    def performance_response(self):
        with open('performanceMicroservice/performance_response.json', 'r') as file:
            performance_data = json.load(file)
            return performance_data 

