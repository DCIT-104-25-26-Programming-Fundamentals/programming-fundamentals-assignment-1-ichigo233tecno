def display_menu():
    """Print the menu options."""
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """Prompt for a task description and add it to the list."""
    description = input("Enter task: ")
    tasks.append(description)
    print(f'Task added: "{description}"')


def view_tasks(tasks):
    """Display all tasks, numbered from 1. Show a message if empty."""
    if not tasks:
        print("Your to-do list is empty. Add a task to get started!")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    """Show tasks, ask which to remove, and delete it if valid."""
    if not tasks:
        print("Your to-do list is empty — nothing to delete.")
        return

    view_tasks(tasks)
    choice = input("Enter task number to delete: ")

    # Validate the input is actually a number
    if not choice.isdigit():
        print("Error: Please enter a valid task number.")
        return

    task_num = int(choice)

    # Validate the number is within range (1 to len(tasks))
    if task_num < 1 or task_num > len(tasks):
        print("Error: Invalid task number.")
        return

    # Convert to 0-indexed position and remove
    removed = tasks.pop(task_num - 1)
    print(f'Task "{removed}" has been removed.')


if __name__ == "__main__":
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a number between 1 and 4.")