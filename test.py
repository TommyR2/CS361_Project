from tabulate import tabulate

data = [{
                        "Ticker" : "AAPL",
                        "Average Purchase Price" : 205.34,
                        "Quantity" : 15,
                        "Total Value" : 2463.84
                    },
                    {
                        "Ticker" : "MSFT",
                        "Average Purchase Price" : 90.00,
                        "Quantity" : 2,
                        "Total Value" : 180.00                 

                    }]
headers = {'Ticker': "Ticker",
            "Average Purchase Price": "Average Purchase Price",
            "Quantity" : "Quantity",
            "Total Value" : "Total Value"}
print(tabulate(data, headers=headers))