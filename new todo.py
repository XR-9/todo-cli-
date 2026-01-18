# 1. load tasks from file into list
# 2. show menu
# 3. add / view / delete tasks (list only)
# 4. save list to file
# 5. exit
def load_tasks():
    tasks = []
    try :
        with open("test.txt" , "r") as f:
            tasks =f.read().splitlines()
    except FileNotFoundError:
        print("file does not exist")
        return []
    return tasks
tasks = load_tasks()
def save_tasks(tasks):
    with open("test.txt", "w") as f:
        f.write("\n".join(tasks))


def add_task(tasks):
    task = input("enter your task : ").strip()
    if not task:
        print("you did not enter a task")
        return
    tasks.append(task) 
    print("tasks has been added")
    save_tasks(tasks)

def view_task(tasks):
    if not tasks:
        print("you have not task to be viewed")
        return
    print("\n Your tasks")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
def delete_task(tasks):
    if not tasks:
        print("you have not task to be deleted")
        return
    choice = input("enter your task number to be removed : ")
    if not choice.isdigit():
        print("only digit numbers are allowed")
        return
    i = int(choice) - 1
    if i < 0 or i >= len(tasks):
        print("task number out of range")
        return
    tasks.pop(i)
    print("task has been removed")
    save_tasks(tasks)

is_running = True
print("WELCOME TO TODO TASKS")
while is_running:
    print("Enter your choices numbers")
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. EXIT")
    choice = input("Enter your choice : ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_task(tasks)
    elif choice== "3":
        delete_task(tasks)
    elif choice == "4":
        confirm = input("do you want to exit (y/n) : ")
        if confirm == "y":
           is_running = False
        elif confirm == "n":
            continue
        else :
            print("invalid input")
            continue
    elif choice not in ["1", "2", "3", "4"]:
        print("choice are allowed 1 to 4")
