a = int(input('Type your number_1: '))
b = int(input('Type your number_2: '))
operation = input('Type your operation: ')

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == '/' and b != 0:
    print(a / b)
elif operation == '/' and b == 0:
    print("Operation can't be completed")
else:
    print('Out of available options')




