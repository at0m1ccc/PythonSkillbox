print('Задача 2. Кривой мессенджер')
text = input('Введите текст: ')
index_letter = 0
for letter in text:
    index_letter += 1
    if letter == '*':
        break
print(f'Символ «*» стоит на позиции {index_letter}.')
