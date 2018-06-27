number_list = [1, 2, 3, 4, 6, 88]
number = int(input('Enter a number please '))

if number / 2:
    print("The number {} is a even number ".format(number))
else:
    print("The number {} is a odd number ".format(number))

print("*----------------------------------*")


def prime(num):
    container = 0
    for i in range(1, num):
        if num % i == 0:
            container += 1
            if container > 1:
                return False
    return True


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in list:
    if prime(i):
        print("The number ", i, " is prime")
    else:
        print("The number ", i, " is not prime")
