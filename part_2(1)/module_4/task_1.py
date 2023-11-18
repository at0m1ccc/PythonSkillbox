text = input('Введите текст: ')
vowel_letters = [x for x in text if x == 'у' or x == 'ё'
                 or x == 'е' or x == 'э' or x == 'о' or
                 x == 'а' or x == 'ы' or x == 'я' or x == 'и' or x == ('ю')]

print(f'Список гласных букв: {vowel_letters}')
print(f'Длина списка: {len(vowel_letters)}')
