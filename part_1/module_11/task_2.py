import math

print('Задача 2. Грубая математика')
count_number = int(input('Введите кол-во чисел: '))
for iteration_number in range(count_number):
    number = float(input('Введите число: '))
    if number >= 0:
        number = math.ceil(number)
        print(f'x = {number} log(x) = {math.log(number)}')
    else:
        number = math.floor(number)
        print(f'x = {number} exp(x) = {math.exp(number)}')
