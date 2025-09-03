from models.database import SessionLocal
from models.transaction import Transaction
from enum import Enum

class TransactionType(Enum):
    BUY = "buy"
    SELL = "sell"

def log_transaction(user_id: int, symbol: str, shares: int, price: float, t_type: str):
    """Log a BUY or SELL transaction for a given user."""
    session = SessionLocal()
    try:
        # Validate transaction type
        if t_type.upper() not in [item.name for item in TransactionType]:
            print(f"Invalid transaction type: {t_type}. Must be BUY or SELL.")
            return

        transaction = Transaction(
            symbol=symbol.upper(),
            shares=shares,
            price=price,
            type=t_type.lower(),
            user_id=user_id,  # Link transaction to user
        )
        session.add(transaction)
        session.commit()
        print(f"{t_type.upper()} logged: {shares} shares of {symbol.upper()} at ${price:.2f}")
    except Exception as e:
        session.rollback()
        print(f"Error logging transaction: {e}")
    finally:
        session.close()


def delete_transaction(user_id: int, transaction_id: int):
    """Delete a transaction by its ID."""
    session = SessionLocal()
    try:
        # Use modern SQLAlchemy get()
        transaction = session.query(Transaction).filter_by(id=transaction_id, user_id=user_id).first()
        if transaction:
            session.delete(transaction)
            session.commit()
            print(f"Transaction {transaction_id} deleted successfully.")
        else:
            print(f"No transaction found with ID {transaction_id} for this user.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting transaction: {e}")
    finally:
        session.close()
