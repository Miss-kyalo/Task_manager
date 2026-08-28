from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date


tasks = []

def add_task(title, description, due_date):
    """Validates inputs and appends a new task dictionary to global tasks."""
    if not validate_task_title(title) or not validate_task_description(description) or not validate_due_date(due_date):
        print("\nInvalid task details provided.")
        return
        
    next_id = len(tasks) + 1 if tasks else 1
    new_task = {
        "id": next_id,
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks.append(new_task)
    print("\nTask added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    """Locates a task by identifier or list index and sets completed status."""
    for task in tasks:
        if task["id"] == index:
            task["completed"] = True
            print("\nTask marked as complete!")
            return
            
    print("\nTask ID not found.")


def view_pending_tasks(tasks=tasks):
    """Filters tasks list to print pending items."""
    pending = [task for task in tasks if not task["completed"]]
    
    if not pending:
        print("\nNo pending tasks found.")
        return
        
    print("\n--- PENDING TASKS ---")
    for task in pending:
        print(f"[{task['id']}] {task['title']} - {task['description']} (Due: {task['due_date']})")


def calculate_progress(tasks=tasks):
    """Calculates overall task completion percentage."""
    if not tasks:
        print("\nNo working currently.")
        return 0.0
        
    total = len(tasks)
    completed_count = sum(1 for task in tasks if task["completed"])
    progress = (completed_count / total) * 100
    
    print(f"\nProgress: {completed_count}/{total} tasks completed ({progress:.1f}%)")
    return progress