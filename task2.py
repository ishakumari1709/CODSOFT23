# Define an empty to-do list
todo_list = []

# Function to add a task to the list
def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to update a task
def update_task():
    view_tasks()
    task_index = int(input("Enter the index of the task to update: ")) - 1
    if 0 <= task_index < len(todo_list):
        new_task = input("Enter the updated task: ")
        todo_list[task_index] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task():
    view_tasks()
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    if 0 <= task_index < len(todo_list):
        deleted_task = todo_list.pop(task_index)
        print(f"{deleted_task} has been deleted.")
    else:
        print("Invalid task index.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Select an option (1/2/3/4/5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
