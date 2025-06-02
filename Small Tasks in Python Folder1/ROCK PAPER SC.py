import random

choices = ("rock" , "paper", "scissors")

running = True

while running:

    player = None
    computer = random.choice(choices)
   
    while player not in choices:

        player = input("Please enter your choice:")

        if player not in choices:

            print(f"The ({player}) choice is invalid")


    print(f"Player: {player}")
    print(f"Bot: {computer}")

    if player == computer:
        print("Tie game")

    elif player == "rock" and computer == "scissors":
        print("You have won the game")

    elif player == "paper" and computer == "rock":
         print("You have won the game")

    elif player == "scissors" and computer == "paper":
        print("You have won the game")

    else:
        print("You have lost the game")

    play_again = input("Play again?(y/n)").lower()

    if not play_again == 'y':
       running = False

print("THANK YOU FOR PLAYING THE GAME")