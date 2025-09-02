# Stock Portfolio Tracker

A simple **Python CLI application** that helps users manage and track their stock investments.  
It is designed for beginner and small investors who find spreadsheets error-prone or existing apps too complex.

## GitHub Repository:

 [Stock Portfolio Tracker](https://github.com/chiznox6/stock-portfol-tracker.git)

---



## video link 

Here is the link to the video: https://drive.google.com/file/d/1J7L1gJEIoq4gjNOPj1V3nO9ghw4FulRB/view?usp=sharing



## Features


1. **Log Stock Transactions (Buy/Sell)**  
   Record stock symbol, number of shares, price per share, and transaction type.

2. **View Portfolio Overview**  
   Displays current holdings with total shares and average price per stock.

3. **View Profit/Loss Summary**  
   Shows realized profits (from sold shares) and unrealized profits (current holdings).

4. **Set Investment Goals**  
   Define personal investment goals with a description and target value.

5. **View Investment Goals**  
   Lists all goals set.

6. **Delete Transactions**  
   Remove a transaction by its ID from the database.



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

You will see a menu:

 Stock Portfolio Tracker
1. Log transaction (Buy/Sell)
2. View portfolio overview
3. View profit/loss summary
4. Set investment goal
5. View goals
6. Exit
7. Delete transaction


Option 1: Log a BUY or SELL transaction.

Option 2: View current portfolio holdings.

Option 3: View realized and unrealized profit/loss.

Option 4: Set a new investment goal.

Option 5: View all investment goals.

Option 6: Exit the application.

Option 7: Delete a transaction by its ID.


## REQUIREMENTS

Python 3.10+

SQLAlchemy

tabulate

Install them manually if needed:

pip install sqlalchemy tabulate



## LICENSE

This project is for educational purposes only.
Not intended for actual financial trading.