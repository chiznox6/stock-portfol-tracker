from utils.db import SessionLocal
from models.goal import Goal
from tabulate import tabulate

def set_goal(description, target_value):
    session = SessionLocal()
    goal = Goal(description=description, target_value=target_value)
    session.add(goal)
    session.commit()
    session.close()
    print(" Goal added!")

def view_goals():
    session = SessionLocal()
    goals = session.query(Goal).all()
    table = [[g.description, f"${g.target_value:.2f}"] for g in goals]
    session.close()
    print(tabulate(table, headers=["Goal", "Target Value"], tablefmt="pretty"))
