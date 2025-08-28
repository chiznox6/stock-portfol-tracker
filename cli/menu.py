from services.transactions import log_transaction
from services.portfolio import view_portfolio, view_profit_loss
from services.goals import set_goal, view_goals

def main_menu():
    while True:
        print("\n Stock Portfolio Tracker")
        print("1. Log transaction (Buy/Sell)")
        print("2. View portfolio overview")
        print("3. View profit/loss summary")
        print("4. Set investment goal")
        print("5. View goals")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            symbol = input("Stock symbol: ")
            shares = int(input("Number of shares: "))
            price = float(input("Price per share: "))
            t_type = input("Type (BUY/SELL): ").upper()
            log_transaction(symbol, shares, price, t_type)

        elif choice == "2":
            view_portfolio()

        elif choice == "3":
            view_profit_loss()

        elif choice == "4":
            desc = input("Goal description: ")
            target = float(input("Target value ($): "))
            set_goal(desc, target)

        elif choice == "5":
            view_goals()

        elif choice == "6":
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice, try again.")
