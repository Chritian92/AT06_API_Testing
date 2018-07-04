def calculate_ages(number: int):
    if number < 13:
        print("You are a child because you have {} years".format(number))
    elif 12 < number < 18:
        print("You are a teenager because you have {} years".format(number))
    elif 17 < number < 30:
        print("You are a young because you have {} years".format(number))
    else:
        print("You are a adult because you have {} years".format(number))

