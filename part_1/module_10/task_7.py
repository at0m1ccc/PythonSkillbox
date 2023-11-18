print('Задача 7. Пирамидка 2')
height = int(input('Введите кол-в уровней пирамидки: '))
next_number = 1
for row in range(1, height + 1):
    print('\t' * (height - row), end='')
    for col in range(row):
        print(next_number, end='')
        next_number += 2
        print('\t' * 2, end='')
    print()
