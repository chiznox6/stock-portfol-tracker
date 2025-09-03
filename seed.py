from models.database import SessionLocal
from models.user import User
from models.goal import Goal
from services.transactions import log_transaction

def seed_data():
    session = SessionLocal()
    # Check for and create the default user if it doesn't exist.
    user = session.query(User).filter(User.id == 1).first()
    if not user:
        default_user = User(id=1, name="DefaultUser", email="default@example.com")
        session.add(default_user)
        session.commit()
        print("Default user created.")
    session.close()

    # Now log transactions, which will open their own sessions.
    print("Adding sample stock data...")
    log_transaction(user_id=1, symbol="AAPL", shares=10, price=150.75, t_type="BUY")
    log_transaction(user_id=1, symbol="GOOGL", shares=5, price=2750.25, t_type="BUY")
    log_transaction(user_id=1, symbol="MSFT", shares=15, price=305.50, t_type="BUY")
    print("Data seeding complete.")

if __name__ == "__main__":
    seed_data()