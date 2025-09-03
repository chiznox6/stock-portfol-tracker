from models.database import Base, engine
from models.user import User
from models.transaction import Transaction
from models.goal import Goal

print("Creating tables directly with SQLAlchemy...")
Base.metadata.create_all(bind=engine)
print("Tables created.")
