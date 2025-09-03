from models.database import SessionLocal
from models.transaction import Transaction
from tabulate import tabulate

def view_portfolio(user_id: int):
    """Show a user's current portfolio with shares and average price."""
    session = SessionLocal()
    try:
        transactions = session.query(Transaction).filter_by(user_id=user_id).all()
        holdings = {}

        for t in transactions:
            if t.symbol not in holdings:
                holdings[t.symbol] = {"shares": 0, "cost": 0.0}

            if t.type == "buy":
                holdings[t.symbol]["shares"] += t.shares
                holdings[t.symbol]["cost"] += t.shares * t.price
            elif t.type == "sell":
                holdings[t.symbol]["shares"] -= t.shares
                holdings[t.symbol]["cost"] -= t.shares * t.price

        table = []
        for stock, data in holdings.items():
            avg_price = (data["cost"] / data["shares"]) if data["shares"] > 0 else 0
            table.append([stock, data["shares"], f"${avg_price:.2f}"])

        if table:
            print(tabulate(table, headers=["Stock", "Shares", "Avg Price"], tablefmt="pretty"))
        else:
            print("No holdings found for this user.")
    finally:
        session.close()


def view_profit_loss(user_id: int):
    """Show realized and unrealized profits for a user's portfolio."""
    session = SessionLocal()
    try:
        transactions = session.query(Transaction).filter_by(user_id=user_id).all()

        realized = 0.0
        holdings = {}

        for t in transactions:
            if t.symbol not in holdings:
                holdings[t.symbol] = {"shares": 0, "cost": 0.0}

            if t.type == "buy":
                holdings[t.symbol]["shares"] += t.shares
                holdings[t.symbol]["cost"] += t.shares * t.price
            elif t.type == "sell":
                # realized profit = sale proceeds - proportional cost basis
                avg_price = (
                    holdings[t.symbol]["cost"] / holdings[t.symbol]["shares"]
                    if holdings[t.symbol]["shares"] > 0 else 0
                )
                realized += (t.price - avg_price) * t.shares
                holdings[t.symbol]["shares"] -= t.shares
                holdings[t.symbol]["cost"] -= avg_price * t.shares

        # Unrealized = current cost basis (since no live market price provided)
        unrealized = sum(data["cost"] for data in holdings.values() if data["shares"] > 0)

        print(f"Realized Profit: ${realized:.2f}")
        print(f"Unrealized (book value of current holdings): ${unrealized:.2f}")
    finally:
        session.close()
