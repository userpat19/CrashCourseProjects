class BANKACCOUNT:
    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.balance = balance


     #SHOW BALANCE FUNCTION  
    def show_balance(self):
        print(f"Your current balance is Php{self.balance}")


     #DEPOSIT FUNCTION  
    def deposit_money(self):

        add = float(input("Enter amount to add:"))

        if add > 0:
            self.balance += add
            print(f"Successfully added Php{add} too your account")
        else:
            print("There is a problem with your input")

        
      #WITHDRAW FUNCTION  
    def withdraw_money(self):
        
        subtract = float(input("Enter amount to get:"))
        
        if subtract > 0:
            self.balance -= subtract
            print(f"Successfully withdrawn Php{subtract} from your account")
        else:
             print("There is a problem with your input")


#EMPTY DICTIONARies
All_Users = {}
Balances = {}

grant = True #variable for the main loop

while grant == True:

    print("SIGN UP")

    Username = input("Enter username:")
    AccountNum = input("Enter Bank Account Number:")
    Balance = float(input("Enter Starting Money:"))
    Username = BANKACCOUNT(AccountNum, Balance)

    if Username not in All_Users:
        All_Users[Username] = AccountNum
    else:
        print("ACCOUNT ALREADY EXISTS")
        print("redirecting to log in")

    while True:

        print("Press 1 to Log in")
        print("Press 2 to Exit Program")
        log_type = input("Enter:")

        if log_type == "1":
            print("LOG IN")
            user_login = input("Enter username:")
            AccountNum_login = input("Enter Bank Account Number:")

            #AUTHENTICATION

            if user_login in All_Users.keys():
                print("hello welcome to the system")

                while True:

                    print("1.Check Account Balance")
                    print("2.Deposit to Account")
                    print("3.Withdraw from Account")
                    print("4.Log Out from Account")

                    choice = input("Mode:")

                    match choice:

                        case "1":
                            Username.show_balance()
                        case "2":
                            Username.deposit_money()
                        case "3":
                            Username.withdraw_money()
                        case "4":
                            break
                        case _:
                            print("Choice is Invalid")

                print("BANK ACCOUNT CLOSED")
                
            else:
                None

        elif log_type == "2":
            grant = False
            break

        else:
            print("Input error")


print("EXIT THE PROGRAM")