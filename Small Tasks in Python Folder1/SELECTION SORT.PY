def sort_function(lst):

    for x in range(len(lst) - 1):

        minimum = x

        for y in range(x + 1, len(lst)):

            if lst[minimum] > lst[y]:

                minimum = y

        temp = lst[x]

        lst[x] = lst[minimum]

        lst[minimum] = temp
    return lst




num_list  = [9,3,5,2,3,5,2,4]

new_list = sort_function(num_list)

print(new_list)