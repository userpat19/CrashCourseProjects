#EMPLOYEE SYSTEM USING OOP AND CLASS VARIABLES IN PYTHON(SOLO LEVELING THEME)


class Guild:

    NumUsers = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Guild.NumUsers += 1

    def view_salary(self):
        print("-------------------------------")
        print(f"{self.name} has a salary of ${self.salary}")
        print("-------------------------------")
    def view_pos(self):
        print("-------------------------------")
        print(f"{self.name}'s current position is {self.position} - Rank")
        print("-------------------------------")
def SignUp():

    while True: 

        Slayer_Name = input("Enter your name:")

        if Slayer_Name not in Member_list.keys():
            Member_list[Slayer_Name] = None
            break
        else:
            print("Username is taken")

    while True:
        Slayer_Rank = input("Enter Rank(E,D,C,B,A,S,S++):").upper()

        if Slayer_Rank == "E" or Slayer_Rank == "D" or Slayer_Rank == "C" or Slayer_Rank == "B" or Slayer_Rank == "A" or Slayer_Rank == "S" or Slayer_Rank == "S++":
            break
        else:
            print("Rank is invalid/non existent")

    if Slayer_Rank == 'E':
        Slayer_Salary = 10000
    elif Slayer_Rank == 'D':
        Slayer_Salary = 30000
    elif Slayer_Rank == 'C':
        Slayer_Salary = 70000
    elif Slayer_Rank == 'B':
        Slayer_Salary = 110000
    elif Slayer_Rank == 'A':
        Slayer_Salary = 200000
    elif Slayer_Rank == 'S':
        Slayer_Salary = 700000
    elif Slayer_Rank == 'S++':
        Slayer_Salary = 1000000
    else:
        print("Error occured")

    variable = Guild(Slayer_Name, Slayer_Rank, Slayer_Salary)

    Member_list[Slayer_Name] = variable

    print("Sign Up Finished")

def view_details():

   Slayer_Name = input("Enter your name:")

   if Slayer_Name not in Member_list:
       print("User dont exist in the database")
   else:
       print(f"Hello there {Slayer_Name}")

       while True:
           
           print("1.View Salary")
           print("2.View Position")
           print("3.Log out")

           choice = input("Choice:")

           match choice:
               
               case "1":
                   Var1 = Member_list.get(Slayer_Name)
                   Var1.view_salary()
               case "2":
                   Var2 = Member_list.get(Slayer_Name)
                   Var2.view_pos()
               case "3":
                  print("Logged out")
                  break
               case _:
                   print("Invalid input") 
           


def main():
    isRunning = True
    Member_list = {}


    while True:
        print("1.Sign Up")
        print("2.View User Info")
        print("3.View amount of users in the system")
        print("4.Exit App")

        menu_choice = input("Enter choice:")

        if menu_choice == "1":
            SignUp()
        elif menu_choice == "2":
            view_details()
        elif menu_choice == "3":
            print(f"The Current amount of users in the system is {Guild.NumUsers}")
        elif menu_choice == "4":
            print("Application Closed")
            break
        else:
            print("Pick a valid choice")

isRunning = True
Member_list = {}

if __name__ == "__main__":
    main()





   
    
