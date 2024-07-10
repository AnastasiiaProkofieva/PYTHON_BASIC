Number = int(input())

Digit_1, rest_1 = divmod(Number, 1000)
print(Digit_1)  # the 1st number's digit

x = Number - Digit_1 * 1000
Digit_2, rest_2 = divmod(x, 100)
print(Digit_2)  # the 2nd number's digit

y = x - Digit_2 * 100
Digit_3, rest_3 = divmod(y, 10)
print(Digit_3)  # the 3rd number's digit

Digit_4 = y - Digit_3 * 10
print(Digit_4)  # the 4th number's digit




