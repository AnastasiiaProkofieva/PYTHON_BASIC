lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = [1, 2, 3, 4, 5]
# lst = [1]
# lst = []
print(lst)

if len(lst) == 0:
    lst = [lst[:0], lst[0:]]
elif not len(lst) % 2:
    lst_1 = lst[:int(len(lst) / 2)]
    lst_2 = lst[int(len(lst) / 2):]
    lst = [lst_1, lst_2]
else:
    lst_1 = lst[:int(len(lst) // 2 + 1)]
    lst_2 = lst[int(len(lst) // 2 + 1):]
    lst = [lst_1, lst_2]
print(lst)
