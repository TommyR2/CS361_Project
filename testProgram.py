import json
import time
import sys

# Function to update the ticker file
def update_ticker(ticker):
    with open('ticker.txt', 'w') as file:
        file.write(ticker)

# Function to read the stock summary
def read_stock_summary():
    with open('stock_summary.json', 'r') as file:
        stock_data = json.load(file)
        return stock_data

# Main function to process the ticker symbol
def main(ticker):
    update_ticker(ticker)
    print(f"Waiting for the microservice to process the ticker symbol '{ticker}'...")
    time.sleep(20) 

    # Read and print the stock summary 
    stock_data = read_stock_summary()
    print(json.dumps(stock_data, indent=4))

if __name__ == "__main__":
    # Check if a ticker symbol was provided as a command-line argument
    if len(sys.argv) != 2:
        print(f"Usage: python test_program.py")
        sys.exit(1)

    # Get the ticker symbol from the command-line argument
    ticker = sys.argv[1]

    # Run the main function with the provided ticker symbol
    main(ticker)