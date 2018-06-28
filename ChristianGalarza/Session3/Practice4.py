number_elements = int(input("Please enter a number of elements: "))
dictionary_global = {}


def create_dictionary(number_elements):
    for i in range(0, number_elements + 1):
        key_insert = key_insert_exist()
        value_insert = value_insert_exits()
        dictionary_global.update({key_insert: value_insert})
    return dictionary_global


def key_insert_exist():
    while True:
        key_insert_verify = input("Insert key: ")
        if return_the_key_dictionary(key_insert_verify):
            print("Invalid key")
        else:
            return key_insert_verify


def return_the_key_dictionary(key):
    return key in dictionary_global.keys()


def value_insert_exits():
    while True:
        value_insert_verify = input("Insert value: ")
        if return_the_value_dictionary(value_insert_verify):
            print("Invalid value")
        else:
            return value_insert_verify


def return_the_value_dictionary(value):
    return value in dictionary_global.values()


def print_dictionary_keys(dictionary_global):
   print(dictionary_global)


create_dictionary(number_elements)
print_dictionary_keys(dictionary_global)
