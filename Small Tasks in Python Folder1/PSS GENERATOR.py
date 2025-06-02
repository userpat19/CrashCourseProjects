import random

def pss_generator():

    Password = []
     
    length_of_password = int(input("Enter the length of the password you want to generate:"))
    for counter in range(length_of_password):
        random_num = random.randint(0,3)
        random_char = random.choice(all_chars[random_num])
        Password.append(random_char)

    print("------------------------------")
    print("Password Generated: " , end = "")
    for char in Password:
        print(char, end = "")
    print()
    print("------------------------------")

print("----------------------------------------")
print("    PYTHON:RANDOM PASSWORD GENERATOR")
print("----------------------------------------")

is_Generating = True

all_chars = (('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'),
             ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'),
             ('!', '@', '#', '$', '%', '^', '&', '*'),
             ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))


while is_Generating:

    while True:

        is_Generating = None

        choice = input("Enter (generate) to run and (quit) to exit:").lower()
        
        if choice == "generate":
            pss_generator()
            is_Generating = True
            break
        elif choice == "quit":
            break
            is_Generating = False
        else:
            print("------------------------------")
            print("  Invalid input, try again")
            print("------------------------------")

print("----------------------------------------")
print("            PROGRAM ENDED")
print("----------------------------------------")
   


