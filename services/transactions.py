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
    print(f" {t_type} logged for {shares} shares of {symbol} at ${price}")
