import math
radio = int(input("insert the radio "))


def area_of_circle(radio):
    if radio > 10:
        print("The area of the circle is ", math.pi * radio * radio)


area_of_circle(radio)
print("*----------------------------------*")

number = int(input("insert a number minor than 35 please "))


def sum_to(number):
    add = 0
    if number < 36:
        for i in range(number + 1):
            add += i
        print("The sum is", add)
    else:
        for i in range(35 + 1):
            add += i
        print("The sum_to function can only add up to 35, and the sum up to 35 was from", add)


sum_to(number)
print("*----------------------------------*")

