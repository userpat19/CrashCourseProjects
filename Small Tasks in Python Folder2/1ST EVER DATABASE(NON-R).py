
     #SHOW BALANCE FUNCTION  
def show_balance():
        print(f"Your current balance is Php{virtual_storage.get(old_username)}")


     #DEPOSIT FUNCTION  
def deposit_money():

        add = float(input("Enter amount to add:"))

        if add > 0:
            var1 = virtual_storage.get(old_username)
            var1 += add
            virtual_storage[old_username] = var1
            print(f"Successfully added Php{add} too your account")
        else:
            print("There is a problem with your input")

        
      #WITHDRAW FUNCTION  
def withdraw_money():
        
        subtract = float(input("Enter amount to get:"))
        
        if subtract > 0:
            var2 = virtual_storage.get(old_username)
            var2 -= subtract
            virtual_storage[old_username] = var2
            print(f"Successfully withdrawn Php{subtract} from your account")
        else:
             print("There is a problem with your input")

main_run = True
All_Users = {}
Users_and_BankNum = {}
virtual_storage = {}
is_running = True

print("-------------------------------")
print("         MULTI USER ATM        ")
print("-------------------------------")

while main_run:
    print("-------------------------------")
    print("         1.Sign Up             ")
    print("         2.Log In              ")
    print("-------------------------------")
    log_type = input("Enter choice:")

    match log_type:

        case "1":
            #SIGN IN PART DRI
            print("-------------------------------")
            print("        Sign up tab")
            print("-------------------------------")

            new_user = input("Enter your Username:")
            new_password = input("Enter Password:")

            if new_user not in All_Users:
                All_Users[new_user] = new_password
                starting_money = float(input("Enter starting money:"))
                virtual_storage[new_user] = starting_money
                print(All_Users)

            else:
                print("--------------------------------------------")
                print("Username Already Exists, Please try again")
                print("--------------------------------------------")
            

        case "2":
            #LOG IN PART DRI
            print("-------------------------------")
            print("         Log in Tab")
            print("-------------------------------")
            old_username = input("Enter Username:")
            old_password = input("Enter password:")


            if old_username not in All_Users:
                print("--------------------------------------------")
                print("  Username does not exists on the database")
                print("             Please try again")
                print("--------------------------------------------")
            else:
                if old_password == All_Users.get(old_username):
                    print("---------------------------------")
                    print(f"Hello welcome back {old_username}")
                    print("---------------------------------")
                    is_running = True

                while is_running:  
                    print("-------------------------------")
                    print("    1.Create Bank Number")
                    print("   2.Use Bank Account Number")
                    print("-------------------------------")
                    bank_num_choice = input("Enter choice:")

                    if bank_num_choice == "1":
                        New_bankNum = input("Enter Bank Account Number:")

                        if New_bankNum not in Users_and_BankNum.values():
                            Users_and_BankNum[old_username] = New_bankNum
                            print(Users_and_BankNum)

                        else:
                            print("-------------------------------")
                            print("     Account Number error")
                            print("-------------------------------")

                    elif bank_num_choice == "2":

                        Old_bankNum = input("Enter account number:")

                        if Old_bankNum in Users_and_BankNum.values():

                            if Old_bankNum == Users_and_BankNum.get(old_username):
                                print("-------------------------------")
                                print("       Correct Number")
                                print("-------------------------------")

                               
                                while True:
                                   print("-------------------------------")
                                   print("   1.Check Account Balance")
                                   print("   2.Deposit to Account")
                                   print("   3.Withdraw from Account")
                                   print("   4.Log Out from Account")
                                   print("-------------------------------")

                                   choice = input("Mode:")


                                   match choice:
                                       
                                       case "1":
                                           print("SHOW BALANCE")
                                           
                                           show_balance()

                                       case "2":
                                           print("DEPOSIT")
                                           
                                           deposit_money()

                                       case "3":
                                           print("WITHDRAW")
                                           withdraw_money()

                                       case "4":
                                           print("LOG OUT")
                                           is_running = False
                                           break

                            else:
                                print("------------------------------------")
                                print(" This number belong to someone else")
                                print("------------------------------------")
                        else:
                            print("-------------------------------")
                            print("    Number does not exists")
                            print("-------------------------------")
                    

        case _:
            print("-------------------------------")
            print("    Please pick a Log type")
            print("-------------------------------")
            

        

