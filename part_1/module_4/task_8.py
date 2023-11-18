print('Задача 8. Максимальное число (по желанию)')
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))
if first_number > second_number:
    if first_number > third_number:
        print('Максимальное число:', first_number)
    else:
        print('Максимальное число:', third_number)
else:
    if second_number > third_number:
        print('Максимальное число:', second_number)
    else:
        print('Максимальное число:', third_number)
