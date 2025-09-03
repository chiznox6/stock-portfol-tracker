from models.database import SessionLocal
from models.goal import Goal
from tabulate import tabulate

def set_goal(user_id: int, name: str, target_value: float):
    """Set a new investment goal for a user."""
    if not name.strip():
        print("Name cannot be empty.")
        return
    if target_value <= 0:
        print("Target value must be greater than 0.")
        return

    session = SessionLocal()
    try:
        goal = Goal(name=name.strip(), target_amount=target_value, user_id=user_id)
        session.add(goal)
        session.commit()
        print(f"Goal '{name}' with target ${target_value:.2f} added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding goal: {e}")
    finally:
        session.close()


def view_goals(user_id: int):
    """View all goals set by a specific user."""
    session = SessionLocal()
    try:
        goals = session.query(Goal).filter_by(user_id=user_id).all()

        if not goals:
            print("No goals found for this user.")
            return

        table = [[g.id, g.name, f"${g.target_amount:.2f}"] for g in goals]
        print(tabulate(table, headers=["ID", "Goal", "Target Value"], tablefmt="pretty"))
    finally:
        session.close()
