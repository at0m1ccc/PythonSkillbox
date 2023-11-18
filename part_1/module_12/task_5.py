print('Задача 5. Текстовый редактор')


def count_letters(text, figure, letter):
    print(f'\nКоличество цифр {figure}: {text.count(figure)}')
    print(f'Количество букв {letter}: {text.count(letter.lower())}')


text = input('Введите текст: ').lower()
figure = input('Какую цифру ищем? ')
letter = input('Какую букву ищем? ')
count_letters(text, figure, letter)
