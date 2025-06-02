def inventory():

    counter = 0
    print("----------------------------ITEMS----------------------------------")
    for item in items:
        print("--------------------------------------------------------------------")
        print(f"{item}: price: Php{prices[counter]}, quantity: {quantity[counter]}")
        counter += 1
    
def add():

    item_add = input("Item to add:").capitalize()
    print("--------------------------------------------------------------------")
    price_add = int(input("Please enter the price for the item: Php"))
    print("--------------------------------------------------------------------")
    quantity_add = int(input("Please enter the quantity:"))

    items.append(item_add)
    prices.append(price_add)
    quantity.append(quantity_add)

isRunning = True

items = ["Apple", "Banana"]
prices= [25, 30]
quantity = [100, 150]

while isRunning:

    print("---------------------------INVENTORY------------------------------")
    print("Press 1 to show inventory, Press 2 to add on inventory, Press 3 to quit")
    pick = input("Pick a mode:")
    pick = int(pick)

    if pick == 1:
        inventory()
    elif pick == 2:
        add()
    elif pick == 3:
        print("THANK YOU, CHANGES HAS BEEN SAVED")
        break
    else:
        print("Invalid choice")