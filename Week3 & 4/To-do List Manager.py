import time
import json
print("")
print("======Welcome To The To Do list Appication======")

task_dict = {}


def add_task():
    task_title = input(f"Enter Name of task: ")
    description = input(f"Enter description for the task: ")
    task_deadline = input("Enter task deadline in this format (02/05/2025): ").replace(" ", "/")
    if task_title not in task_dict:
        task_dict[task_title] = {"description": description, "deadline": task_deadline}
        print("Task has been added successfully")
    else:
        print("This task already exists")

def display_task():
        if not task_dict:
            print("No tasks available.")
        else:
            for task_title, details in task_dict.items():
                print(f"Task: {task_title}")
                print(f"  Description: {details['description']}")
                print(f"  Deadline: {details['deadline']}")
                print("-" * 30)

def update_task():
    task_title = input("Enter the title of the task you want to update: ")
    if task_title in task_dict:
        choice = input("What would you like to update: Title(T) or description(D) \n: ").upper()
        if choice == "T":
            new_title = input("Enter new title: ")
            task_dict[new_title] = task_dict.pop(task_title)
            print("Task title updated successfully")
        elif choice == "D":
            new_description = input("Enter new description: ")
            task_dict[task_title]["description"] = new_description
            print("Task description updated successfully")
        else:
            print("Invalid option")
    else:
        print("Task not found")

def delete_task():
    task_title = input("Enter the task title you will like to pop: ")
    if task_title in task_dict:
        task_title = task_dict.pop(task_title)
    else:
        print("Task not found")

def save_task():
    with open("task.json", "w") as file:
        json.dump(task_dict, file)
    print("Data saved successfully")

while True: 

    print("===================================")
    print("| What would you like to do       |")
    print("| 1. Create a todo action         |")
    print("| 2. Display current To do list   |")
    print("| 3. Update To do list            |")
    print("| 4. Delete a to do list          |")
    print("===================================")

    option = input("Chose an option: ")

    if option == '1':
            add_task()
            time.sleep(1.5)

    elif option == '2':
        display_task()
        time.sleep(1.5)
    elif option == '3':
        update_task()
        time.sleep(1.5)
    elif option == '4':
        delete_task()
        time.sleep(1.5)
    elif option == '5':
        save_task()
        time.sleep(1.5)
    else:
        print("Print invlaid input \nPlease Enter a valid input")
        time.sleep(1.5)
