lst = [0, 1, 7, 2, 4, 8]
# lst = [1, 3, 5]
# lst = [6]
# lst = []

print(lst)

if len(lst) == 0:
    print(0)
else:
    a = sum(lst[::2]) * lst[-1]
    print(a)



