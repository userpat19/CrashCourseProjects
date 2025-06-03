from rapidfuzz import fuzz

Content = {" What does the `len()` function do in Python?":"It returns the length of an object."
                , "What is a dictionary in Python?":" A collection of key-value pairs."}

def main_menu():
    isRunning = True
    while isRunning:
        print("Welcome to the Flashcard Program!")
        print("Choose an option:")
        print("1. Review flashcards")
        print("2. Test your knowledge")
        print("3. Exit")
        choice = input("Enter choice:")

        match choice:
            case "1":
                Review()

            case "2":
                Test()

            case "3":
                print("GOODBYE")
                isRunning = False
            case _:
                print("Invalid Output")


def Review():
    x = 1
    for keys,values in Content.items():
        print("-----------------------------------")
        print(f"FlashCard No.{x}")
        print(f"Q:{keys}")
        print(f"A:{values}")
        print()
        x += 1

def Test():

    score = 0
    
    for keys,values in Content.items():
        print(f"{keys}")
        user_input = input("Answer:")

        if fuzz.ratio(values.lower(), user_input.lower()) >= 80:
            print("Correct")
            score +=1

        else:
            print("Incorrect")

    score = score / 2 * 100

    print(f"Score:{score}%")


main_menu()