from utils.db import SessionLocal
from models.transaction import Transaction, TransactionType

def log_transaction(symbol, shares, price, t_type):
    session = SessionLocal()
    transaction = Transaction(
        stock_symbol=symbol.upper(),
        shares=shares,
        price_per_share=price,
        type=TransactionType[t_type]
    )
    session.add(transaction)
    session.commit()
    session.close()
    print(f"{t_type} logged for {shares} shares of {symbol} at ${price}")

def delete_transaction(transaction_id: int):
    """Delete a transaction by its ID."""
    session = SessionLocal()
    transaction = session.query(Transaction).get(transaction_id)
    if transaction:
        session.delete(transaction)
        session.commit()
        print(f"Transaction {transaction_id} deleted successfully.")
    else:
        print(f"No transaction found with ID {transaction_id}.")
    session.close()
