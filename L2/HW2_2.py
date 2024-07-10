number_1 = int(input())

rest1, n1 = divmod(number_1, 10)
rest2, n2 = divmod(rest1, 10)
rest3, n3 = divmod(rest2, 10)
rest4, n4 = divmod(rest3, 10)
rest5, n5 = divmod(rest4, 10)

# creating number_2 with returned digits' order
number_2 = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5
print(number_2)








