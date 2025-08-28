from utils.db import SessionLocal
from models.transaction import Transaction, TransactionType
from tabulate import tabulate

def view_portfolio():
    session = SessionLocal()
    transactions = session.query(Transaction).all()
    holdings = {}

    for t in transactions:
        if t.stock_symbol not in holdings:
            holdings[t.stock_symbol] = {"shares": 0, "cost": 0}

        if t.type == TransactionType.BUY:
            holdings[t.stock_symbol]["shares"] += t.shares
            holdings[t.stock_symbol]["cost"] += t.shares * t.price_per_share
        else:  # SELL
            holdings[t.stock_symbol]["shares"] -= t.shares
            holdings[t.stock_symbol]["cost"] -= t.shares * t.price_per_share

    table = []
    for stock, data in holdings.items():
        if data["shares"] > 0:
            avg_price = data["cost"] / data["shares"]
        else:
            avg_price = 0
        table.append([stock, data["shares"], f"${avg_price:.2f}"])

    session.close()
    print(tabulate(table, headers=["Stock", "Shares", "Avg Price"], tablefmt="pretty"))

def view_profit_loss():
    session = SessionLocal()
    transactions = session.query(Transaction).all()

    realized = 0
    unrealized = 0
    holdings = {}

    for t in transactions:
        if t.stock_symbol not in holdings:
            holdings[t.stock_symbol] = {"shares": 0, "cost": 0}

        if t.type == TransactionType.BUY:
            holdings[t.stock_symbol]["shares"] += t.shares
            holdings[t.stock_symbol]["cost"] += t.shares * t.price_per_share
        else:  # SELL
            holdings[t.stock_symbol]["shares"] -= t.shares
            realized += t.shares * t.price_per_share

    for stock, data in holdings.items():
        if data["shares"] > 0:
            avg_price = data["cost"] / data["shares"]
            unrealized += data["shares"] * avg_price

    session.close()
    print(f" Realized Profit: ${realized:.2f}")
    print(f" Unrealized (current holdings): ${unrealized:.2f}")

def view_transactions():
    """Show all transactions with IDs (for delete/reference)."""
    session = SessionLocal()
    transactions = session.query(Transaction).all()

    table = []
    for t in transactions:
        table.append([
            t.id,                # Transaction ID
            t.stock_symbol,
            t.shares,
            f"${t.price_per_share:.2f}",
            t.type.name
        ])

    session.close()
    print(tabulate(table, headers=["ID", "Symbol", "Shares", "Price", "Type"], tablefmt="pretty"))
