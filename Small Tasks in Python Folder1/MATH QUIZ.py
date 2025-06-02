import math

print("                                               PYTHON MATH QUIZ GAME(MULTIPLE CHOICES)")

z = 81
mult = 3

low = 3
mid = 4
high = 5

correct = 0
Incorrect = 0

highest = max(low , mid , high)


round_up = 97
round_down = 96
sq = math.sqrt(z) 
mult *= 3 

print("1.What is 96.89 rounded up?")
print("a. 100")
print("b. 97")
print("c. 90")
print("d. 80")

round_up_user = input("ANSWER:")

print("2.What is the squareroot of 81?")
print("a. 9")
print("b. 10")
print("c. 2")
print("d. 100")

sq_user = input("ANSWER:")

print("3.What is 96.89 rounded down?")
print("a. 100")
print("b. 97")
print("c. 90")
print("d. 96")

round_down_user = input("ANSWER:")

print("4.What is 81 x 3?")
print("a. 100")
print("b. 243")
print("c. 11")
print("d. 99")

mult_user = input("ANSWER:")

print(f"5.What is the highest number between {low} , {mid} , {high}?")
print("a. 4")
print("b. 5")
print("c. 3")
print("d. 0")

highest_user = input("ANSWER:")

if round_up_user == "b":

    correct += 1

else:

    Incorrect += 1

if sq_user == "a":

    correct += 1

else:

    Incorrect += 1

if round_down_user == "d":

    correct += 1

else:

    Incorrect += 1

if mult_user == "b":

    correct += 1

else:

    Incorrect += 1

if highest_user == "b":

    correct += 1

else:

    Incorrect += 1

print(f"You have {correct} correct answer")
print(f"You have {Incorrect} Incorrect answer")
print("THANK YOU FOR PLAYING THE GAME")
