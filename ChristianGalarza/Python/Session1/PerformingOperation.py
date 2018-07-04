operate = input('enter a Math operation ')
number1 = int(input('Enter the first number '))
number2 = int(input('Enter the second number '))


def perform_operation(operate, number1, number2):
    if operate == '+':
        print(number1 + number2)
    if operate == '-':
        print(number1 - number2)
    if operate == '*':
        print(number1 * number2)
    if operate == '/':
        print(number1 / number2)
    if operate == '%':
        print(number1 % number2)
    if operate == '**':
        print(number1 ** number2)
    if operate == '//':
        print(number1 // number2)


perform_operation(operate, number1, number2)
