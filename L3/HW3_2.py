# [12, 3, 4, 10] => [10, 12, 3, 4]
lst_1 = [12, 3, 4, 10]
print(lst_1)
if len(lst_1) == 0:
    print(lst_1)
else:
    a = lst_1.pop(len(lst_1) - 1)
    lst_1.insert(0, a)
    print(lst_1)

# [1] => [1]
lst_2 = [1]
print(lst_2)
if len(lst_2) == 0:
    print(lst_2)
else:
    a = lst_2.pop(len(lst_2) - 1)
    lst_2.insert(0, a)
    print(lst_2)

# [] => []
lst_3 = []
print(lst_3)
if len(lst_3) == 0:
    print(lst_3)
else:
    a = lst_3.pop(len(lst_3) - 1)
    lst_3.insert(0, a)
    print(lst_3)

# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
lst_4 = [12, 3, 4, 10, 8]
print(lst_4)
if len(lst_4) == 0:
    print(lst_4)
else:
    a = lst_4.pop(len(lst_4) - 1)
    lst_4.insert(0, a)
    print(lst_4)







