def selection_sort(arr):

    for x in range(len(arr) - 1):
        minimum = x

        for y in range(x + 1,len(arr)):
            if arr[y] < arr[minimum]:
                minimum = y

        temp = arr[minimum]
        arr[minimum] = arr[x]
        arr[x] = temp

def insertion_sort(arr):

    for x in range(1, len(arr)):
        priority = arr[x]
        left =  x - 1

        while left >= 0 and arr[left] > priority:
            arr[left + 1] = arr[left]
            left -= 1
        arr[left + 1] = priority


def bubble_sort(arr):

    for i in range(len(arr) - 1):

        for j in range(len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


array_num = [10,4,3,2,6,4]

bubble_sort(array_num)
print(array_num)

