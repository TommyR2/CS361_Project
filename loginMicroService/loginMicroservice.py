import time
import json

class LoginMicroservice:

    def __init__(self) -> None:
        self.request_path = 'login_requests.json'
        self.response_path = 'login_response.json'

    def monitor_requests(self):
        with open(self.request_path, 'r') as file:
            login_request = json.load(file)
            if login_request != {}:
                request_type = login_request['account_type']
                username = login_request['username']
                password = login_request['password']
                response = self.validate_requests(request_type, username, password)
                self.send_response(response)
                return True

    def validate_requests(self, request_type, username, password):
        if request_type == 'existing':
            with open('../portfolios.json', 'r') as file:
                portfolio_data = json.load(file)
                users = portfolio_data['Portfolios']
                for user in users:
                    if user['Username'] == username and password == user['Password']:
                        return user['Stocks']
                return 'Invalid Credentials'
            
        elif request_type == 'new':
            with open('../portfolios.json', 'r') as file:
                portfolio_data = json.load(file)
                users = portfolio_data['Portfolios']
                for user in users:
                    if user['Username'] == username:
                        return 'Duplicate User'
                self.add_user(username, password)
                return []

    def send_response(self, response_data):
        with open('login_response.json', 'w') as file:
            json.dump(response_data, file)
    
    def add_user(self, username, password):
        with open('../portfolios.json', 'r') as file:
            portfolio_data = json.load(file)
            users = portfolio_data['Portfolios']
            users.append({"Username": username,
                        "Password": password,
                        "Stocks": []})
            
            with open('../portfolios.json', 'w') as file:
                json.dump(portfolio_data, file, indent=4)

    def cleanup_data(self):
        time.sleep(1)
        with open('login_requests.json', 'w') as file:
            json.dump({}, file)
        
    def start(self):
        while True:
            action = self.monitor_requests()
            if action:
                self.cleanup_data()
            time.sleep(0.1)


if __name__ == '__main__':
    Service = LoginMicroservice()
    Service.start()