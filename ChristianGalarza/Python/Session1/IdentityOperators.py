number1 = int(input('Enter the first number '))
number2 = int(input('Enter the second number '))


def identy_is(number1, number2):
    if number1 is number2:
        print("In the line 1 - the first number and the second number is the same number")
    else:
        print("'In the line 1 - the first number and the second number don't the same number")


def identity_is_not(number1, number2):
    if id(number1) == id(number2):
        print("In the line 2 - the first number and the second number have same the same number")
    else:
        print("In the line 2 - the first number and the second number don't have the same number")


identy_is(number1, number2)
identity_is_not(number1, number2)
