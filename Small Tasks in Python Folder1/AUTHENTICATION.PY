name = input("Enter your name:")

length = len(name)
space_detect = name.find(" ")
ifDigit = name.isalpha()

if length > 12:
    print("The username is too long")
else:
    print("The username length is valid")

if space_detect == -1:
    print("There was no spaces detected, you are good to go")
else:
    print("Invalid, there is a space detected")
if ifDigit == True:
    print("Nice username, you are good to go")
else:
    print("There is a special character or number detected(invalid username)")