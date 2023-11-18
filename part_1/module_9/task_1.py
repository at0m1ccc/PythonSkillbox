print('Задача 1. Я стал новым пиратом!')
right_word_count = 0
for word_count in range(10):
    answer = input('Введите слово: ')
    if (answer == 'Карамба') or (answer == 'карамба'):
        right_word_count += 1
print(f'Слово "Крамба" было произнесено {right_word_count} раз.')
