from misc import *
from tabulate import tabulate

class PreviewPage:
    def display_preview_page(self, portfolio):
        """Display the preview page with command options"""

        # Initial Prompts
        print_stars()
        print("Here your portfolio after implementing the current order:\n")
        self.print_table(portfolio)
        
    def print_table(self, portfolio):
        """Display a given portfolio."""

        headers = {'Ticker': "Ticker",
            "Average Purchase Price": "Average Purchase Price",
            "Quantity" : "Quantity",
            "Total Value" : "Total Value"}
        print(tabulate(portfolio, headers=headers))



