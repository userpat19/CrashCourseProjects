food_available = {"popcorn": 50,
                  "bbq": 20,
                  "shake": 10,
                  "sweet corn": 50}

cart = []
total = 0

print("------------MENU---------------")

for keys,values in food_available.items():
    print(f"{keys:10}: Php{values}")

print("-------------------------------")

while True:
    pick = input("Please pick a food to buy(press q to quit): ").lower()

    if pick == 'q':
        break

    elif food_available.get(pick) is not None:
        cart.append(pick)



print("------------CART---------------")

print("Pre-ordered: ", end="")

for food in cart:

    total += food_available.get(food)
    print(food, end="_")

print()

print(f"Total: Php{total}")