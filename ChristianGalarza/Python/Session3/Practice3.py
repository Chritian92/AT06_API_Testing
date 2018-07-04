string = input("Insert a sentence: ")
dictionary = {}


def table_of_letters(string, dictionary):
    convert_text = string.lower()
    for i in range(1, len(convert_text)):
        if not (convert_text[i] == " "):
            dictionary[convert_text[i]] = convert_text.count(convert_text[i])
    dictionary = sorted(dictionary.items())
    print("The sentence have quantity of letters: \n", dictionary)


table_of_letters(string, dictionary)
