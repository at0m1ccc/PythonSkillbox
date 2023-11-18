print('Задача 3. Рамка')
width = int(input('Введите ширину рамки: '))
height = int(input('Введите ввсоту рамки: '))

for row in range(height + 1):
    for col in range(width + 2):
        if (col == 0 or col == width + 1) and row != 0:
            print('|', end=' ')
        elif (row == 0 or row == height) and (col != 0 and col != width + 1):
            print('_', end=' ')
        else:
            print(' ', end=' ')
    print()
