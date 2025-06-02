print("PASSWORD VALIDATOR")

special_char = ("&" ,"$", "#","!")
special_digit = ("1" , "2", "3","4", "5", "6", "7", "8", "9")


while True:

    valid = 0
    special_char_verify = False
    special_digit_verify = False

    password = input("Enter your password:")

    for letter in password:
        if letter in special_char:
            special_char_verify = True
            valid += 1
            break
        else:
            None

    for letter in password:
        if letter in special_digit:
            special_digit_verify = True
            valid += 1
            break
        else:
            None

    if len(password) >= 8:
        valid += 1
    else:
        print("The password must have atleast 8 characters")

    if special_char_verify == False:
        print("Password must contain a special character")
    if special_digit_verify == False:
        print("Password must contain a number")

    if valid == 3:
        break

print("Password is valid")
    


