Number_1 = int(input())

# splitting the number_1 on the separate digits
Dg_1 = Number_1 // 10000
Dg_2 = (Number_1 - Dg_1 * 10000) // 1000
Dg_3 = (Number_1 - Dg_1 * 10000 - Dg_2 * 1000) // 100
Dg_4 = (Number_1 - Dg_1 * 10000 - Dg_2 * 1000 - Dg_3 * 100) // 10
Dg_5 = Number_1 - Dg_1 * 10000 - Dg_2 * 1000 - Dg_3 * 100 - Dg_4 * 10

# changing the digits' order
print(Dg_5,Dg_4,Dg_3,Dg_2,Dg_1)







