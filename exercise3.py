my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_2 = []
for i in my_list_1:
    if my_list_1.count(i)==1:
        my_list_2.append(i)
print(my_list_2)