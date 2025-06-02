import random



#● ┏ ─ ┐ │ └ ┘

"┏───────────┐"
"│           │"
"│           │"
"│           │"
"└───────────┘"

dice_art = {

    1: ("┏───────────┐",
        "│           │",
        "│     ●     │",
        "│           │",
        "└───────────┘"),
    2: ("┏───────────┐",
        "│   ●       │",
        "│           │",
        "│        ●  │",
        "└───────────┘"),

    3: ("┏───────────┐",
        "│   ●       │",
        "│           │",
        "│   ●      ●│",
        "└───────────┘"), 

    4: ("┏───────────┐",
        "│   ●       │",
        "│  ●        │",
        "│  ●       ●│",
        "└───────────┘"),

    5: ("┏───────────┐",
        "│   ●     ● │",
        "│   ●       │",
        "│ ●     ●   │",
        "└───────────┘"),

    6: ("┏───────────┐",
        "│   ●     ● │",
        "│   ●   ●   │",
        "│ ●     ●   │",
        "└───────────┘")    
}

dice = []
total = 0
num_of_dice = int(input("How many dices?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for num in range(num_of_dice):
    for line in dice_art.get(dice[num]):
        print(line)




for number in dice:
    total += number

print(f"Random Dices: {dice}")
print(f"Total value: {total}")