lst = [0, 1, 0, 12, 3]
# lst = [0]
# lst = [1, 0, 13, 0, 0, 0, 5]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print(lst)
for el in lst:
    if el == 0:
        a = lst.index(0)
        b = lst.pop(a)
        lst.append(b)
print(lst)

