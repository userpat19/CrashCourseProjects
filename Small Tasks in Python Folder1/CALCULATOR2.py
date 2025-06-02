
Use = int(input("Do you want to calculate something(Type 1 for yes otherwise 2): "))

if Use == 1:
    while Use == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Pick a operation(+, -, *, /): ")
        #FOR ADDING
        if operation == '+':
            sum = num1 + num2
            print(f"The sum of the two numbers is {sum:.2f}")

            Use = int(input("Do you want to calculate something(Type 1 for yes otherwise 2): "))
            
            if Use == 1:
                continue
            elif Use == 2:
                print("GOODBYE THANK YOU FOR RUNNING THE PROGRAM")
                break
            else:
                print("That is an invalid choice")
                break
        #FOR SUBRACTING
        elif operation == "-":
            diff = num1 - num2
            print(f"The difference between the two numbers is {diff:.2f}")

            Use = int(input("Do you want to calculate something(Type 1 for yes otherwise 2): "))
            
            if Use == 1:
                continue
            elif Use == 2:
                print("GOODBYE THANK YOU FOR RUNNING THE PROGRAM")
                break
            else:
                print("That is an invalid choice")
                break

        #FOR Multiplying
        elif operation == "*":
            mult = num1 * num2
            print(f"The product of the two numbers is {mult:.2f}")

            Use = int(input("Do you want to calculate something(Type 1 for yes otherwise 2): "))
            
            if Use == 1:
                continue
            elif Use == 2:
                print("GOODBYE THANK YOU FOR RUNNING THE PROGRAM")
                break
            else:
                print("That is an invalid choice")
                break

         #FOR DIVIDING
        elif operation == "/":
            quotient = num1 / num2
            print(f"The quotient of the two numbers is {quotient:.2f}")

            Use = int(input("Do you want to calculate something(Type 1 for yes otherwise 2): "))
            
            if Use == 1:
                continue
            elif Use == 2:
                print("GOODBYE THANK YOU FOR RUNNING THE PROGRAM")
                break
            else:
                print("That is an invalid choice")
                break

elif Use == 2:
    print("GOODBYE THANK YOU FOR RUNNING THE PROGRAM")
else:
    print("Invalid, please run the program again")