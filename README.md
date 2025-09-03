## Stock Portfolio Tracker

A simple Python CLI application that helps users manage and track their stock investments.
It is designed for beginner and small investors who find spreadsheets error-prone or existing apps too complex.

## GitHub Repository

[Stock Portfolio Tracker](https://github.com/your-username/stock-portfol-tracker)


## Demo Video

[Watch Demo] (https://drive.google.com/file/d/1Yxxnh5S8jdTasefDj1l5q59Z4H5PQNP3/view?usp=sharing)


## Features

1. Log Stock Transactions (Buy/Sell)
Record stock symbol, number of shares, price per share, and transaction type.

2. View Portfolio Overview
Displays current holdings with total shares and average price per stock.

3. View Profit/Loss Summary
Shows realized profits (from sold shares) and unrealized profits (current holdings).

4. Set Investment Goals
Define personal investment goals with a description and target value.

5. View Investment Goals
Lists all goals set.

6. Delete Transactions
Remove a transaction by its ID from the database.

7. Exit the Application

## Project Structure

stock-portfol-tracker/
│── cli/
│   ├── menu.py          # Menu logic
│
│── models/
│   ├── __init__.py
│   ├── user.py          # User model
│   ├── transaction.py   # Transaction model (buy/sell)
│   ├── goal.py          # Investment goals model
│
│── services/
│   ├── __init__.py
│   ├── transactions.py  # Transaction logic
│   ├── portfolio.py     # Portfolio calculations
│   ├── goals.py         # Goal tracking logic
│
│── utils/
│   ├── __init__.py
│   ├── db.py            # Database setup (SQLAlchemy engine, session, Base)
│
|__seed.py
│── migrations/          # Alembic migrations
│── requirements.txt     # Dependencies
│── Pipfile              # Dependencies (alternative to requirements.txt)
│── Pipfile.lock
│── README.md            # Documentation
│── main.py              # Runs the CLI (imports cli/menu.py)
│── portfolio.db         # SQLite database (auto-created at runtime)


## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/stock-portfol-tracker.git
cd stock-portfol-tracker
```

2. Install Pipenv (if not installed):

```bash
pip install pipenv
```

3. Install dependencies using Pipenv:

```bash
pipenv install
```

4. Activate the virtual environment:

```bash
pipenv shell
```


## Database & Alembic Migrations

1. This project uses Alembic for database migrations.

Initialize Alembic (already done in this repo):

```bash
alembic init migrations
```

2. Create a new migration after changing models:

```bash
alembic revision --autogenerate -m "description_of_change"
```

3. Apply migrations to the database:

```bash
alembic upgrade head
```

4. Check current migration history:

```bash
alembic history
```

## Presentation Workflow

This is a step-by-step guide to run the project for a clean demonstration from a fresh start.

**Step 1: Activate the Virtual Environment**
(You only need to do this once per terminal session)
```bash
pipenv shell
```

**Step 2: Clean Up the Old Database**
To ensure you start fresh for the demo, delete the old database file if it exists.
```bash
rm portfolio.db
```

**Step 3: Create the Database From Migrations**
This command reads the migration scripts and creates a new, empty `portfolio.db` file with the correct table structures.
```bash
alembic upgrade head
```

**Step 4: Seed the Database with Sample Data**
This populates the new database with sample data, making the demo more interesting.
```bash
python seed.py
```

**Step 5: Run the Application**
Now, start the main CLI application.
```bash
python main.py
```
The application menu will appear. You can now demonstrate its features, such as entering `2` to view the portfolio you just seeded.

## You will see:

```
Stock Portfolio Tracker
1. Log transaction (Buy/Sell)
2. View portfolio overview
3. View profit/loss summary
4. Set investment goal
5. View goals
6. Delete transaction
7. Exit
```

1 → Log a BUY or SELL transaction

2 → View current portfolio holdings

3 → View realized and unrealized profit/loss

4 → Set a new investment goal

5 → View all investment goals

6 → Exit the application

7 → Delete a transaction by its ID

## Requirements

Python 3.12

SQLAlchemy

Alembic

tabulate

## License

This project is for educational purposes only.
Not intended for actual financial trading.