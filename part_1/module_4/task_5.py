print('Задача 5. Модуль числа')
number = int(input('Введите число: '))
module_number = number
if number < 0:
    module_number = -number
print('Модуль числа', number, '=', module_number)
