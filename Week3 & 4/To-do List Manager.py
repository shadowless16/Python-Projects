"""Todo List Manager """
import json
import os

global tasks
tasks = {}


while True:
    def add_task():
        global tasks
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task_status = input("Enter status: ")

        tasks[task_name] = {
            "task description" : task_description,
            "task status" : task_status
        }

        print(tasks)

    def view_tasks():
        if not tasks:
            print("Empty list")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}: {task}")


    def update_tasks():
        print("Task update")
        for task_lists in tasks:
            print(f"{task_lists}: {tasks[task_lists]}")
            task_name = input("Enter the task name you want to update: ")
            if task_name not in tasks:
                print("This task does not exist")
                task_name = input("Enter the task name you want to update: ")
            elif task_name in tasks:
                task_description = input("Enter task description: ")
                task_status = input("Enter status: ")

                tasks[task_name] = {
                    "task description": task_description,
                    "task status": task_status
                }

                print(f"The task {tasks} has been updated")
        else:
            print("No task has been created yet...")
                
    def delete_task():
        task_name = input("Enter the task name you want to delete: ")
        if task_name in tasks:
            del tasks[task_name]
            print(f"The task {task_name} has been deleted")
        else:
            print("This task does not exist")

    def save_tasks():
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Tasks saved successfully!")

    print("===================================")
    print("| What would you like to do       |")
    print("| 1. Create a todo action         |")
    print("| 2. Display current To do list   |")
    print("| 3. Update To do list            |")
    print("| 4. Delete a to do list          |")
    print("| 4. Save the to do list          |")
    print("| 4. Delete a to do list          |")
    print("| 5. Save the to do list          |")
    choice = input("Which of the following option would you like to pick from 1 - 4: ")

    choice = input("Which of the following option would you like to pick from 1 - 5: ")
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_tasks()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
    else:
        print("Invlaid choice")
