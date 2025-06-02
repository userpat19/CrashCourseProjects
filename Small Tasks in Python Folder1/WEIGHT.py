print("WEIGHT CONVERTER")

weight = float(input("Enter your weight:"))
unit = input("What is the unit of the weight you just entered(K/L):")

if unit == 'K':
   weight = weight * 2.205
   unit = "POUNDS"
   print(f"Your weight is {round(weight, 1)} {unit}")

elif unit == 'L':
   weight = weight / 2.205
   unit = "KILOGRAMS"
   print(f"Your weight is {round(weight, 1)} {unit}")

else:
   print("Invalid input from the user")

