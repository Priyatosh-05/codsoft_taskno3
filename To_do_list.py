import os

# List to store tasks
tasks = []

def display_menu():
    print("\n============================")
    print("       TO-DO LIST APP       ")
    print("============================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Clear All Tasks")
    print("7. Exit")
    print("============================")

def view_tasks():
    os.system('cls')  # Clear screen (use 'cls' on Windows)
    print("\n======== Your To-Do List ========")
    if not tasks:
        print("You have no tasks! 🎉")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['completed'] else "❌"
            print(f"{i}. {task['task']} - {status}")
    print("=================================\n")

def add_task():
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "completed": False})
        print("Task added successfully! ✅\n")
    else:
        print("Task cannot be empty! ❌\n")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task_name = input("Enter the updated task: ").strip()
            if new_task_name:
                tasks[task_num - 1]['task'] = new_task_name
                print("Task updated successfully! ✅\n")
            else:
                print("Task cannot be empty! ❌\n")
        else:
            print("Invalid task number! ❌\n")
    except ValueError:
        print("Please enter a valid number! ❌\n")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted successfully! 🗑️\n")
        else:
            print("Invalid task number! ❌\n")
    except ValueError:
        print("Please enter a valid number! ❌\n")

def mark_task_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print("Task marked as completed! ✅\n")
        else:
            print("Invalid task number! ❌\n")
    except ValueError:
        print("Please enter a valid number! ❌\n")

def clear_tasks():
    confirmation = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
    if confirmation == 'y':
        tasks.clear()
        print("All tasks cleared! 🧹\n")
    else:
        print("Clear operation cancelled.\n")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-7): "))
            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                update_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                mark_task_completed()
            elif choice == 6:
                clear_tasks()
            elif choice == 7:
                print("Goodbye! 👋")
                break
            else:
                print("Invalid option! Please choose a number between 1 and 7.")
        except ValueError:
            print("Please enter a valid number!")

# Run the To-Do List app
main()
