Flag = None

the_word = input("Please enter the word:")

length_of_word = len(the_word)

reverse_index = []

for x in range(length_of_word):
    reverse_index.append(length_of_word - x - 1)

reverse_word = [the_word[num] for num in reverse_index]

for x in range(length_of_word):
    if the_word[x] != reverse_word[x]:
        Flag = False
        break

if not Flag == False:
    print("The word is a palindrome") 
else:
    print("The word is not a palindrome")