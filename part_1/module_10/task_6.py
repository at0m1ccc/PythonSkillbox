print('Задача 6. Пирамидка')
height = int(input('Введите высоту пирамидки: '))

for row in range(height):
    for col in range((height - 1) * 2 + 1):
        if height - row - 1 <= col <= height + row - 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()
