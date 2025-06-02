
def bubble_sort(arr):

    for x in range(len(arr) - 1):

        for j in range(len(arr) - x - 1):

            if arr[j] > arr[j + 1]:

                temp = arr[j]

                arr[j] = arr[j + 1]

                arr[j + 1] = temp

    return arr

user_list = []


print("Enter 10 integers to sort")

for x in range(10):
    currentnum = int(input("Enter number:"))
    user_list.append(currentnum)

ascended_array = bubble_sort(user_list)

print(f"This is the ascended array:{ascended_array}")

maximum = ascended_array[-1]
minimum = ascended_array[0]
sum = 0

for num in ascended_array:
    sum += num

print(f"The highest number is {maximum}")
print(f"The lowest number is {minimum}")
print(f"The sum of all numbers in the list is {sum}")