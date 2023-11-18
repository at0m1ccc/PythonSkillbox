print('Задача 2. Лестница')
user_number = int(input('Введите число: '))
for row in range(1, user_number + 1):
    for col in range(1, user_number + 1):
        if row >= col:
            print(row, end=' ')
    print()
