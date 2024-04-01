given_list = [('a', 1), ('b', 2), ('c', 3)]
swapped_list = []
for given in given_list:
    elements = list(given)
    new_list = [elements[1], elements[0]]
    swapped_list.append(tuple(new_list))
print(swapped_list)
