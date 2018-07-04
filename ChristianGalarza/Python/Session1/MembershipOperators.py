number1 = int(input('Enter the first number '))
number2 = int(input('Enter the second number '))
numbers_from_1_to_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def membership_in(number1, numbers_from_1_to_10):
    if number1 in numbers_from_1_to_10:
        print("Membership in: The first number exists in the numbers from 1 to 10")
    else:
        print("Membership in: The first number doesn't exist in the numbers from 1 to 10")


def membership_not_in(number2, numbers_from_1_to_10):
    if number2 not in numbers_from_1_to_10:
        print("Membership not in: The second number doesn't exist in the numbers from 1 to 10")
    else:
        print("Membership not in: The second number exist in the numbers from 1 to 10")


membership_in(number1, numbers_from_1_to_10)
membership_not_in(number2, numbers_from_1_to_10)
