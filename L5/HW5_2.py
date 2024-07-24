question = 'yes'

while question == 'yes' or question == 'y':

    a = float(input('Type your number_1: '))
    operation = input('Type your operation: ')
    b = float(input('Type your number_2: '))

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

    question = (input('Do you want to continue?: ')).lower()

print('The operation is completed')