import random

portfolio = {}

def add_stock():
    symbol = input("Enter stock symbol: ").upper()
    shares = int(input("Enter number of shares: "))
    price = round(random.uniform(100, 500), 2)
    portfolio[symbol] = {"shares": shares, "price": price}
    print(f"Added {shares} shares of {symbol} at ${price} each.")

def remove_stock():
    symbol = input("Enter stock symbol to remove: ").upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print("Stock not found.")

def view_portfolio():
    total = 0
    print("\nYour Portfolio:")
    for symbol, data in portfolio.items():
        current_price = round(random.uniform(90, 510), 2)
        value = data["shares"] * current_price
        total += value
        print(f"{symbol}: {data['shares']} shares @ ${current_price} = ${value:.2f}")
    print(f"Total Portfolio Value: ${total:.2f}\n")

while True:
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. View Portfolio")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_stock()
    elif choice == "2":
        remove_stock()
    elif choice == "3":
        view_portfolio()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
