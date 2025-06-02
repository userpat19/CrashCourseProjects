print("PYTHON CALCULATOR")

operation = input("Enter the kind of operation you want to use (+, -, *, /):")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if operation == '+':
    result = num1 + num2
    print(f"The sum of the two numbers is {result}")

elif operation == '-':
    result2 = num1 - num2
    print(f"The difference of the two numbers is {result2}")

elif operation == '*':
    result3 = num1 * num2
    print(f"The product of the two numbers is {result3}")

elif operation == '/':
    result4 = num1 / num2
    print(f"The quotient is {round(result4, 2)}")

else:
    print("Invalid operation")