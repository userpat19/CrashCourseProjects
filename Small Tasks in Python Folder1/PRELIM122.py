def insertion_sort(arr):
    
    for x in range(1, len(arr)):
        key = arr[x]
        y = x - 1

        while y >= 0 and arr[y] > key:
            arr[y + 1] = arr[y]
            y -= 1
        arr[y + 1] = key
    
    return arr


amount_num = int(input("Amount of numbers to input:"))

list_num = []
average = 0
sum = 0

for x in range(amount_num):
    current_num = int(input("Enter a number:"))
    list_num.append(current_num)
    sum += current_num

average = sum / amount_num

sorted_array = insertion_sort(list_num)
reversed_array = sorted_array[::-1]

print(f"Average: {average}")
print(f"Sum: {sum}")
print(f"Sort: {sorted_array}")
print(f"Reverse: {reversed_array}")

