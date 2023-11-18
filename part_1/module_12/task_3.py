print('Задача 3. Апгрейд калькулятора')


def figure_sum(number):
    used_number = number
    summ = 0
    while used_number > 0:
        summ += used_number % 10
        used_number //= 10
    print(f'Сумма цифр числа {number} = {summ}')


def max_figure(number):
    used_number = number
    max_num = -1
    while used_number > 0:
        if used_number % 10 > max_num:
            max_num = used_number % 10
        used_number //= 10
    print(f'Максимальная цифра в числе {number} = {max_num}')


def min_figure(number):
    used_number = number
    min_num = 10
    while used_number > 0:
        if used_number % 10 < min_num:
            min_num = used_number % 10
        used_number //= 10
    print(f'Минимальная цифра в числе {number} = {min_num}')


while True:
    number = int(input('Введите число: '))
    choice = int(input(
        'Введите действие: 1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра, 4 - завершить работу: '))
    if choice == 1:
        figure_sum(number)
    elif choice == 2:
        max_figure(number)
    elif choice == 3:
        min_figure(number)
    elif choice == 4:
        print('Завершение работы программы.')
        break
    else:
        print('Ошибка ввода!!!')
