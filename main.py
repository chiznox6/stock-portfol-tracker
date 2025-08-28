from utils.db import Base, engine
from models.transaction import Transaction
from models.goal import Goal
from cli.menu import main_menu

# Create tables if not exist
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main_menu()
