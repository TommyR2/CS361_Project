# Main Functionality of the Project will Reside Here
from HomePage import HomePage
from LoginPage import LoginPage
from BuyPage import BuyPage
from ViewPage import ViewPage
from PreviewPage import PreviewPage
from SellPage import SellPage
from UploadPage import UploadPage
from ResearchPage import ResearchPage
from PerformancePage import PerformancePage
from RiskPage import RiskPage
import time
import json

class PortfolioTracker:
    def __init__(self) -> None:
        self.Login = LoginPage()
        self.Home = HomePage()
        self.Buy = BuyPage()
        self.Sell = SellPage()
        self.View = ViewPage()
        self.Preview = PreviewPage()
        self.Upload = UploadPage()
        self.Research = ResearchPage()
        self.Performance = PerformancePage()
        self.Risk = RiskPage()
        self.command = 'Login'
        self.user = None
        self.portfolio = None

    def start(self):
        while True:
            time.sleep(0.1)
            if self.command == False:
                continue

            elif self.command == 'Login':
                self.command = False
                self.command, self.portfolio, self.user = self.Login.display_login()

            elif self.command == 'Home':
                self.command = False
                self.command, self.portfolio = self.Home.display_home_page(self.portfolio)

            elif self.command == 'Buy':
                self.command = False
                self.command, self.portfolio = self.Buy.display_buy_page(self.portfolio)

            elif self.command == 'Sell':
                self.command = False
                self.command, self.portfolio = self.Sell.display_sell_page(self.portfolio)


            elif self.command == 'Preview':
                self.command = False
                self.command = self.Preview.display_preview_page()


            elif self.command == 'View':
                self.command = False
                self.command = self.View.display_view_page(self.portfolio)

            elif self.command == 'Upload':
                self.command = False
                self.command, self.portfolio = self.Upload.display_upload_page(self.portfolio)

            elif self.command == 'Research':
                self.command = False
                self.command, self.portfolio = self.Research.display_research_page(self.portfolio)

            elif self.command == 'Performance':
                self.command = False
                self.command, self.portfolio = self.Performance.display_performance_page(self.portfolio)

            elif self.command == 'Risk':
                self.command = False
                self.command, self.portfolio = self.Risk.display_risk_page(self.portfolio)

            elif self.command == 'Logout':
                with open('portfolios.json', 'r') as old_file:
                    portfolios = json.load(old_file)
                    for portfolio in portfolios["Portfolios"]:
                        if portfolio['Username'] == self.user:
                            portfolio['Stocks'] = self.portfolio
                with open('portfolios.json', 'w') as new_file:
                    json.dump(portfolios, new_file, indent=4)
                self.command, self.portfolio, self.user = self.Login.display_login()
                

if __name__ == '__main__':
    PortfolioTracker = PortfolioTracker()
    PortfolioTracker.start()