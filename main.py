from models.database import Base, engine
from models.user import User
from models.transaction import Transaction
from models.goal import Goal
from cli.menu import main_menu

# Create all tables if they do not exist
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main_menu()
