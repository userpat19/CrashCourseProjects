principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount:"))
    if principle < 0:
      print("amount cant be less than zero")
    else:
       break

while True:
    rate = int(input("Enter the rate:"))
    if rate < 0:
      print("rate cant be less than zero")
    else:
       break

while True:
    time = int(input("Enter the value for the time:"))
    if time < 0:
      print("time cant be less than zero")
    else:
       break

total = principle * pow((1 + rate / 100), time)

print(f"The total amount that should be paid is ${total:.2f}")

