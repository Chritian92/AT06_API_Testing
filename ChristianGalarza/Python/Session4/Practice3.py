user_dictionary = {}


def dictionary():
    global user_dictionary
    flag = True
    while flag:
        print()
        response = input("Do you want insert a user? yes, no ")
        if response.lower() == "no":
            flag = False
        elif response.lower() == "yes":
            user_id = int(input("Insert user id: "))
            user_name = input("Insert username: ")
            if 1 <= user_id <= 100 and len(user_name) < 9:
                user_dictionary[user_id] = user_name
            else:
                print("user_id or user_name is out of range")
                continue


def print_group_of_users():
    global user_dictionary
    for key in user_dictionary:
        if 1 <= key <= 25:
            print(f"User {user_dictionary[key]} is from the Group 1")
        elif 26 <= key <= 50:
            print(f"User {user_dictionary[key]} is from the Group 2")
        elif 51 <= key <= 75:
            print(f"User {user_dictionary[key]} is from the Group 3")
        elif 76 <= key <= 100:
            print(f"User {user_dictionary[key]} is from the Group 4")


def give_me_a_number():
    global user_dictionary
    user_id_list = []
    number = int(input("Please insert a number: "))
    for key in user_dictionary.keys():
        if str(key).startswith(str(number)):
            user_id_list.append(key)
    return user_id_list


def give_me_a_letter():
    global user_dictionary
    user_name_list = []
    character = input("Please insert a character: ")
    for key in user_dictionary:
        if user_dictionary[key].startswith(character):
            user_name_list.append(user_dictionary[key])
    return user_name_list


dictionary()
print()
print(give_me_a_number())
print()
print(give_me_a_letter())
print()
print_group_of_users()