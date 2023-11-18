print('Задача 5. Вася хочет выигрывать')
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))
if first_number == second_number == third_number:
    print('Количество одинаковых чисел: 3')
elif first_number == second_number or first_number == third_number or second_number == third_number:
    print('Количество одинаковых чисел: 2')
else:
    print('Количество одинаковых чисел: 0')
