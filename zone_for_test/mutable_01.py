list_of_lists = []
one_list = [0, 0, 0]
for _ in range(3):
    new_list = one_list
    list_of_lists.append(new_list)
one_list[1] = 1
print(list_of_lists)


list_of_lists = []
one_list = [0, 0, 0]
for _ in range(3):
    list_of_lists.append(one_list)
one_list[1] = 1
print(list_of_lists)