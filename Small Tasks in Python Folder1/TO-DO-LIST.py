def view_tasks():

    current = 1

    if not main_tasks == {}:
        for keys,values in main_tasks.items():

            print("--------------------------------------------")
            print(f"             Task {current}:{keys}")
            print(f"             Due:{values}")
            print("--------------------------------------------")
            current += 1
    else:
        print("--------------------------------------------")
        print("       List Empty, please add a task")
        print("--------------------------------------------")



def add_task():
    TASK = input("Enter the task:")
    DUE = input("Enter Due(month/day/year):")

    main_tasks[TASK] = DUE

    print("--------------------------------------------")
    print("               Task Added")
    print("--------------------------------------------")


def del_task():
    remove_item = input("Enter the task to remove:")

    if remove_item in main_tasks.keys():
        del main_tasks[remove_item]
        print("--------------------------------------------")
        print("               ITEM DELETED")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print("    This task does not exist on the list")
        print("--------------------------------------------")


main_tasks = {}

print("---------------------------------")
print("|   TO-DO-LIST PYTHON PROGRAM   |")
print("---------------------------------")

confirm_open = None
isRunning = True

while not confirm_open == "open":
    confirm_open = input("Please type (open to turn on the program):").lower()

while isRunning:
    print("Type 1 to view list")
    print("Type 2 to add a task on the list")
    print("Type 3 to delete a task on the list")
    print("Type 4 to quit the program")
    choice = int(input("Enter your choice:"))

    while True:

        if choice == 1:
            view_tasks()
            break
        elif choice == 2:
            add_task()
            break
        elif choice == 3:
            del_task()
            break
        elif choice == 4 :
            print("--------------------------------------------")
            print("               Changes saved")
            print("--------------------------------------------")
            isRunning = False
            break
        else:
            print("--------------------------------------------")
            print("         Invalid input, try again")
            print("--------------------------------------------")
            break