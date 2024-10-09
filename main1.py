import requests
from logo import logo
import time
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
#EVERYONE NEEDS TO ADD THEIR OWN API KEY ACCESSED THROUGH ALPHAVANTAGE
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
#FOR PROTECTION OF API KEY ENVIRONMENTAL VARIABLES ARE USED
API_KEY = os.getenv('API_KEY')
portfoliodata = {}

def stock_price(symbol):
    stock_params= {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(STOCK_ENDPOINT,params= stock_params)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    most_recent_data = data_list[0]
    return most_recent_data["4. close"]

def add_stock(symbol,purchase_price):
    if symbol not in portfoliodata:
        portfoliodata[symbol] = {"purchase_price": purchase_price}
        print(f"{symbol} added to the portfolio with purchase price: ${purchase_price}")
    else:
        print(f"{symbol} already present in portfolio.")

def remove_stock(symbol):
    if symbol in portfoliodata:
        del_symbol = portfoliodata.pop(symbol,None)
        print(f"Removed {symbol} from portfolio")
    else:
        print(f"{symbol} not present in portfolio.")

def track_stock_performance():
    for symbol,data in portfoliodata.items():
        current_stock_price = float(stock_price(symbol))
        purchase_price = data["purchase_price"]
        change_percentage= ((current_stock_price - purchase_price) / purchase_price) * 100
        print(f"{symbol} Purchase price:${purchase_price},Current price:${current_stock_price},Change in stock percentage: {change_percentage:.2f}%")

def main_loop():
    while True:
        print(logo)
        print("1. Press 1 to add stock")
        print("2. Press 2 to remove stock")
        print("3. Press 3 to Track stock performance")
        print("4. Press 4 to exit the stock portfolio tracker")
        user_input = input("Select an option from (1-4): ")

        if user_input == "1":
            symbol = input("Please enter the stock symbol: ").upper()
            purchase_price = float(input(f"Please enter the purchase price for {symbol}: $"))
            add_stock(symbol,purchase_price)

        elif user_input == "2":
            symbol = input(f"Enter the symbol of stock u want to remove: ").upper()
            remove_stock(symbol)

        elif user_input == "3":
            track_stock_performance()

        elif user_input == "4":
            print("Exiting the program")
            break

        else:
            print("Invalid input. Please enter a valid option from (1-4).")

        time.sleep(2)
main_loop()









