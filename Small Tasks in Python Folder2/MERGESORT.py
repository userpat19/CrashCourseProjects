def merge_sort(arr):

    if len(arr) > 1:

        left_array = arr[:len(arr)//2]
        right_array = arr[len(arr)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):

            if left_array[i] < right_array[j]:

                arr[k] = left_array[i]

                i += 1

            else:

                arr[k] = right_array[j]

                j += 1

            k += 1


        while i < len(left_array):
            arr[k] = left_array[i]

            k += 1
            i += 1

        while j < len(right_array):
            arr[k] = right_array[j]

            k += 1
            j += 1

array_num = [8,6,3,1,4,5,9,2,7]

merge_sort(array_num)

print(array_num)