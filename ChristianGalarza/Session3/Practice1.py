letter = "I love spom! Spom is my favorite food.Spom, spom, yum!"
letter1 = "Mississippi"
enter_new_letter = "I"
enter_new_letter1 = "am"
enter_new_letter2 = "a"
change_text = "i"
change_text1 = "om"
change_text2 = "o"


def change_letter(letter, change_text ,enter_new_letter):
    change_letter = letter.split(change_text)
    new_letter = enter_new_letter.join(change_letter)
    print(new_letter)


change_letter(letter, change_text1, enter_new_letter1)
change_letter(letter1, change_text, enter_new_letter)
change_letter(letter, change_text2, enter_new_letter2)
