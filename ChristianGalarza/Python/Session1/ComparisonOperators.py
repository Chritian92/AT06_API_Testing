number1 = int(input('Enter the first number '))
number2 = int(input('Enter the second number '))


def comparation_equals(number1, number2):
    if number1 == number2:
        print("First number {} is equal to second number {}".format(number1, number2))
    elif number1 != number2:
        print("First number {} is not equal to second number {}".format(number1, number2))


def comparation_major_or_minor(number1, number2):
    if number1 > number2:
        print("First number {} is greater than the second number {}".format(number1, number2))
    elif number1 < number2:
        print("First number {} is less than to second number {}".format(number1, number2))


def comparation_major_equals_or_minor_equals(number1, number2):
    if number1 >= number2:
        print("First number {} is greater than or equal to second number {}".format(number1, number2))
    elif number1 <= number2:
        print("First number {} is less than or equal to  second number {}".format(number1, number2))


comparation_equals(number1, number2)
comparation_major_or_minor(number1, number2)
comparation_major_equals_or_minor_equals(number1, number2)

