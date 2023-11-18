print('Задача 1. Урок информатики 2')


def transformToFloat(number):
    degree_number = 0
    if number >= 1:
        while number >= 10:
            degree_number += 1
            number /= 10
    else:
        while number < 1:
            degree_number -= 1
            number *= 10
        number = round(number, abs(degree_number))
    print(f'Формат плавающей точки: x = {number} * 10 ** {degree_number}')


number = float(input('Введите число: '))
if number <= 0:
    print('Ошибка ввода!!!')
else:
    transformToFloat(number)
