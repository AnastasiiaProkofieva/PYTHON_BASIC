n = int(input('Please type your number: '))

while n > 9:
    x = 1
    for i in str(n):
        x *= int(i)
    n = x
print(n)
