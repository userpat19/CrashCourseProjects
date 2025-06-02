import random 

low = 1
high = 100

guesses= 0
is_running = True

answer = random.randint(low, high)

print("PYTHON NUMBER GUESSING GAME")
print("Please pick number between 1 to 100")

while is_running:

    guess = input("Please enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess > high or guess < low:
            print("That number is out of range")
            print("Please pick number between 1 to 100")

        elif guess > answer:
            print("Too high!, please try again")

        elif guess < answer:
            print("Too low!, please try again")

        else:
            print(f"CORRECT!, the answer was {answer}")
            print(f"The number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid input")
        print("Please pick number between 1 to 100")