def print_prime_dictionary(dictionary):
    prime_dictionary = {}
    for key in dictionary.keys():
        for number in range(2, key - 1):
            if key % number == 0:
                break
        else:
            prime_dictionary[key] = dictionary[key]
    print(prime_dictionary)


def is_valid_dictionary():
    dictionary = {}
    while True:
        key = int(input("insert key between 1 to 9: "))
        if key < 1 or key > 9:
            break
        dictionary[key] = key ** 2
    return dictionary


print_prime_dictionary(is_valid_dictionary())
