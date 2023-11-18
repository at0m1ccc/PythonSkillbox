print('Задача 8. Яма ')
number = int(input('Введите число: '))
for row in range(1, number + 1):
    for col in range(number * 2):
        if col < row:
            print(number - col, end='')
        elif col >= number * 2 - row:
            print(col - number + 1, end='')
        else:
            print('.', end='')
    print()
