import random

def spin_row():
    
    emojis = ["🥸", "😊", "😒", "😁", "🤑"]

    random_emojis = [random.choice(emojis) for symbols in range(3)]

    return random_emojis

def print_row(row):
    print("---------------")
    print("  | ".join(row))
    print("---------------")

def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🤑":
            return bet * 20
        elif row[0] == "🥸":
            return bet * 20
        elif row[0] == "😁":
           return  bet * 5
        elif row[0] == "😊":
            return bet * 4
        elif row[0] == "😒":
            return bet * 3

    return 0

def main():
    balance = 100

    print("------------------------")
    print("PYTHON SLOT MACHINE GAME")
    print("SYMBOLS: 🥸  | 😊 | 😒 | 😁 | 🤑")
    print("------------------------")

    while balance > 0:
        print(f"Current balance - Php{balance}")

        bet = input("Enter bet amount: Php")
               
        if not bet.isdigit():
            print("Please enter a number for the amount of bet")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")

        balance -= bet

        row = spin_row()
        print("Spinning.....")
        print_row(row)

        payout = get_payout(row , bet)

        if payout > 0:
            print(f"You won Php{payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to play again?(Y/N):").upper()

        if not play_again == "Y":
            break

    print(f"GAME OVER, YOUR FINAL BALANCE IS PHP{balance}")

if __name__ == "__main__":
    main()
