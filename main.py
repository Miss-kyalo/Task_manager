from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        elif choice == "2":
            try:
                task_id = int(input("Enter Task ID to mark as complete: "))
                mark_task_as_complete(task_id)
            except ValueError:
                print("\nError: Please enter a valid numerical ID.")

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            calculate_progress()

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()