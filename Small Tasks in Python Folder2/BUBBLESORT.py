def bubble_sort(lst):

    for x in range(len(lst) - 1):

        for y in range(len(lst) - x - 1):

            if lst[y] < lst[y+1]:

                temp = lst[y]

                lst[y] = lst[y+1]

                lst[y+1] = temp


    return lst

num_list = [1,6,2,9,3]

new_list = bubble_sort(num_list)

print(new_list)

