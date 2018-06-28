number_elements = int(input("Please enter a number of elements: "))


def create_array(number_elements):
    array_result = []
    for i in range(0, number_elements):
        array_result.append(input("Insert a value: "))
    return array_result


def print_array_result(array_result):
    print(array_result)


print_array_result(create_array(number_elements))
