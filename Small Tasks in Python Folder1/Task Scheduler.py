def task_Scheduler():
    Task = input("Please Enter the task:")
    Priority = input("Please Enter the level of priority(low,mid,high):")
    Due = input("Due Date(year/month/day):")

    Tasks.append(Task)
    Priorities.append(Priority)
    Dues.append(Due)


Tasks = []
Priorities = []
Dues = []
counter = 0

while True:

    while True:

         confirm = input("Do you want to add a task?(y/n):").lower()

         if confirm == "y" or confirm == "n":
             break
         else:
             print("Invalid code used")

    if not confirm == "n": 
        task_Scheduler()
    else:
        break

for task in Tasks:
    print("-----------------------------------------")
    print(f"Task: {task}")
    print(f"Priority Level: {Priorities[counter]}")
    print(f"Due Date: {Dues[counter]}")

    counter += 1




