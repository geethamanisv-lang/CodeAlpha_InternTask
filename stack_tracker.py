# Stock Portfolio Tracker
# # Hardcoded stock prices
stock_prices = {
    "RELIANCE": 131,
    "TCS": 243,
    "INFY": 150,
    "HDFCBANK": 737,
    "ICICIBANK": 424,
    "SBIN": 970,
    "ITC": 400,
    "WIPRO": 250
}
portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker!")

print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Get number of different stocks
number_of_stocks = int(input("\nHow many stocks do you want to buy? "))

# Get stock details
for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        portfolio[stock_name] = quantity

        total_investment += investment

        print("Investment for", stock_name, "=", investment)

    else:
        print("Stock not available!")

# Display portfolio
print("\n----- Your Stock Portfolio -----")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    print(stock, "| Quantity:", quantity,
          "| Price:", price,
          "| Total:", investment)

print("\nTotal Investment Value: $", total_investment)

# Save results in a text file
with open("portfolio.txt", "w") as file:

    file.write("Stock Portfolio Tracker\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():

        investment = stock_prices[stock] * quantity

        file.write(
            f"{stock} - Quantity: {quantity}, Investment: ${investment}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved successfully!")
