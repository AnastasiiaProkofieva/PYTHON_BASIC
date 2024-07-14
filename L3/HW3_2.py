lst = [12, 3, 4, 10]
# lst = [1]
# lst = []
# lst = [12, 3, 4, 10, 8]
print(lst)
if len(lst) == 0:
    print(lst)
else:
    a = lst.pop(len(lst) - 1)
    lst.insert(0, a)
    print(lst)








