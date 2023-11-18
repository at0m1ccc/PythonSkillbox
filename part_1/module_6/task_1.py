print('Задача 1. Кубы чисел')
final_number = int(input('Введите число до которого нужно вычислять кубы чисел: '))
current_number = 1
while current_number <= final_number:
    print(f'Куб числа {current_number} равен {current_number ** 3}')
    current_number += 1
