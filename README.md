# Stock Portfolio Tracker

A simple **Python CLI application** that helps users manage and track their stock investments.  
It is designed for beginner and small investors who find spreadsheets error-prone or existing apps too complex.

GitHub Repository: [Stock Portfolio Tracker](https://github.com/chiznox6/stock-portfol-tracker.git)

---

## Features

- Log stock transactions (buy/sell trades with symbol, shares, price).
- View portfolio overview (current holdings, average prices, valuations).
- View profit/loss summary (realized and unrealized gains/losses).
- Set investment goals and track progress.
- Uses **SQLite with SQLAlchemy** for database storage.
- Uses **tabulate** for clean tabular display.

---

## Project Structure

│── cli/
│ ├── main.py # CLI entry point (menu and commands)
│── models/
│ ├── init.py # Package init
│ ├── database.py # Database setup (SQLAlchemy engine, session)
│ ├── transaction.py # Transaction model (buy/sell)
│ ├── goal.py # Investment goals model
│── services/
│ ├── init.py
│ ├── portfolio_service.py # Portfolio calculations
│ ├── transaction_service.py # Transaction logic
│ ├── goal_service.py # Goal tracking logic
│── requirements.txt # Dependencies
│── README.md # Documentation
│── main.py # Runs the CLI (imports cli/main.py)



---

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/chiznox6/stock-portfol-tracker.git
   cd stock-portfol-tracker

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows


3. Install dependencies:

pip install -r requirements.txt

4. Usage

Run the program with:

python main.py


Example session:

Stock Portfolio Tracker
1. Log transaction (Buy/Sell)
2. View portfolio overview
3. View profit/loss summary
4. Set investment goal
5. View goals
6. Exit
Enter choice: 1
Stock symbol: AAPL
Number of shares: 10
Price per share: 150
Type (BUY/SELL): BUY
BUY logged for 10 shares of AAPL at $150.0



## REQUIREMENTS

Python 3.10+

SQLAlchemy

tabulate

Install them manually if needed:

pip install sqlalchemy tabulate



## LICENSE

This project is for educational purposes only.
Not intended for actual financial trading.