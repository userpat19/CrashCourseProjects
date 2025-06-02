items = []
prices = []
total = 0

while True:
    item = input("Enter the name of the item (press q to quit):")

    if item.lower() == 'q':
        break
    
    else:
        price = float(input(f"Enter the price of a {item}: $"))
        items.append(item)
        prices.append(price)


print()
print()

print("----SHOPPING CART----")

for item in items:
    print(item, end = " ")

for price in prices:
    total += price

print()

print(f"The total price is $ {total}")