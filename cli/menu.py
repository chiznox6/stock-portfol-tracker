from services.transactions import log_transaction, delete_transaction
from services.portfolio import view_portfolio, view_profit_loss
from services.goals import set_goal, view_goals
from models.database import SessionLocal
from models.transaction import Transaction
from tabulate import tabulate
from models.user import User

# Default user ID for logging transactions
DEFAULT_USER_ID = 1

def main_menu():
    # Ensure a default user exists
    session = SessionLocal()
    user = session.get(User, DEFAULT_USER_ID)
    if not user:
        user = User(id=DEFAULT_USER_ID, name="DefaultUser", email="default@example.com")
        session.add(user)
        session.commit()
    session.close()
    

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Log transaction (Buy/Sell)")
        print("2. View portfolio overview")
        print("3. View profit/loss summary")
        print("4. Set investment goal")
        print("5. View goals")
        print("6. Delete transaction")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            symbol = input("Stock symbol: ")
            try:
                shares = int(input("Number of shares: "))
                price = float(input("Price per share: "))
                t_type = input("Type (BUY/SELL): ").upper()
                if t_type not in ["BUY", "SELL"]:
                    print("Invalid type. Please enter BUY or SELL.")
                else:
                    log_transaction(DEFAULT_USER_ID, symbol, shares, price, t_type)
            except ValueError:
                print("Invalid number entered. Transaction not logged.")

        elif choice == "2":
            view_portfolio(DEFAULT_USER_ID)

        elif choice == "3":
            view_profit_loss(DEFAULT_USER_ID)

        elif choice == "4":
            name = input("Goal name: ")
            try:
                target = float(input("Target value ($): "))
                set_goal(DEFAULT_USER_ID, name, target)
            except ValueError:
                print("Invalid number. Goal not added.")

        elif choice == "5":
            view_goals(DEFAULT_USER_ID)

        elif choice == "6":

            try:
                transaction_id = int(input("Enter transaction ID to delete: "))
                delete_transaction(DEFAULT_USER_ID, transaction_id)
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

