from services.transactions import log_transaction, delete_transaction
from services.portfolio import view_portfolio, view_profit_loss
from services.goals import set_goal, view_goals
from utils.db import SessionLocal
from models.transaction import Transaction, TransactionType
from tabulate import tabulate

def show_transactions():
    """Display all transactions with IDs"""
    session = SessionLocal()
    transactions = session.query(Transaction).all()
    table = []
    for t in transactions:
        table.append([t.id, t.stock_symbol, t.shares, f"${t.price_per_share:.2f}", t.type.name])
    session.close()
    if table:
        print(tabulate(table, headers=["ID", "Symbol", "Shares", "Price", "Type"], tablefmt="pretty"))
    else:
        print("No transactions found.")

def main_menu():
    while True:
        print("\n Stock Portfolio Tracker")
        print("1. Log transaction (Buy/Sell)")
        print("2. View portfolio overview")
        print("3. View profit/loss summary")
        print("4. Set investment goal")
        print("5. View goals")
        print("6. Exit")
        print("7. Delete transaction")

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

        elif choice == "7":
            show_transactions()
            try:
                transaction_id = int(input("Enter transaction ID to delete: "))
                delete_transaction(transaction_id)
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")

        else:
            print(" Invalid choice, try again.")
