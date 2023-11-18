print('Задача 5. Великий и могучий')
text = input('Введите текст: ')
max_length_word = 0
length_word = 0

for letter in text:
    if (letter != ' ') and (letter != '.') and (letter != ',') and (letter != '!') and (letter != '?') and (
            letter != ';') and (letter != ':') and (letter != '"'):
        length_word += 1
    else:
        if length_word > max_length_word:
            max_length_word = length_word
            length_word = 0
if length_word > max_length_word:
    max_length_word = length_word

print(f'Самое длинное слово состоит из {max_length_word} букв.')
