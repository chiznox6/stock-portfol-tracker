from services.transactions import log_transaction, delete_transaction
from services.portfolio import view_portfolio, view_profit_loss
from services.goals import set_goal, view_goals
from models.database import SessionLocal, engine, Base
from models.user import User

# Create all tables
Base.metadata.create_all(bind=engine)

# Default user ID for logging transactions
DEFAULT_USER_ID = 1

# Ensure a default user exists
session = SessionLocal()
user = session.get(User, DEFAULT_USER_ID)
if not user:
    user = User(id=DEFAULT_USER_ID, name="DefaultUser", email="default@example.com")
    session.add(user)
    session.commit()
session.close()

print("--- Logging some transactions ---")
log_transaction(DEFAULT_USER_ID, "AAPL", 10, 150.00, "BUY")
log_transaction(DEFAULT_USER_ID, "GOOGL", 5, 2800.00, "BUY")
log_transaction(DEFAULT_USER_ID, "AAPL", 5, 160.00, "SELL")

print("\n--- Viewing portfolio overview ---")
view_portfolio(DEFAULT_USER_ID)

print("\n--- Viewing profit/loss summary ---")
view_profit_loss(DEFAULT_USER_ID)

print("\n--- Setting an investment goal ---")
set_goal(DEFAULT_USER_ID, "Retirement", 1000000.00)

print("\n--- Viewing investment goals ---")
view_goals(DEFAULT_USER_ID)

print("\n--- Deleting a transaction ---")
delete_transaction(DEFAULT_USER_ID, 3)

print("\n--- Viewing portfolio overview after deletion ---")
view_portfolio(DEFAULT_USER_ID)
