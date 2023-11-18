print('Задача 2. Поступление')
russian_language_scores = int(input('Введите количество баллов по русскому языку: '))
math_scores = int(input('Введите количество баллов по математике: '))
computer_science_scores = int(input('Введите количество баллов по информатике: '))
if russian_language_scores + math_scores + computer_science_scores >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')
