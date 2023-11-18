def caesar_cipher(letter, step):
    rus_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и",
                   "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                   "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь",
                   "э", "ю", "я"]
    if rus_letters.count(letter) == 0:
        return letter
    index_new_letter = rus_letters.index(letter) + step
    if index_new_letter >= len(rus_letters):
        index_new_letter %= len(rus_letters)
    return rus_letters[index_new_letter]


text = list(input('Введите сообщение: '))
step = int(input('Введите сдвиг: '))
result = ''.join([caesar_cipher(text[index], step) for index in range(len(text))])

print(f'Зашифрованное сообщение: {result}')
