from ChristianGalarza.Python.Session4.modules.ModuleConvertAges import *
from ChristianGalarza.Python.Session4.modules.ModulePrintAges import *


def constructor_dictionary():
    global dictionary
    amount_of_users = int(input("Put the amount of users: "))
    for i in range(amount_of_users):
        name = input("Put the name: ")
        age = int(input("Put the age: "))
        dictionary[name] = age
    return build_answer()


def build_answer():
    text = []
    for elements in dictionary:
        text.append(elements)
        text.append(print_calculate_time(elements))
        text.append(print_calculate_time(elements))
    return text


def print_calculate_time(elements):
    text = []
    text.append(convert_ages_to_days(dictionary.get(elements)))
    text.append(convert_ages_to_hours(dictionary.get(elements)))
    text.append(convert_ages_to_minutes(dictionary.get(elements)))
    return text


def the_user_are(elements):
    return calculate_ages(dictionary.get(elements))


print(constructor_dictionary())
