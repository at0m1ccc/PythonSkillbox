def count_uppercase_lowercase(text):
    list_low_letter = []
    list_up_letter = []
    for letter in text:
        if letter.isalpha() and letter.islower():
            list_low_letter.append(letter)
        elif letter.isalpha() and letter.isupper():
            list_up_letter.append(letter)
        else:
            continue
    return len(list_up_letter), len(list_low_letter)


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
