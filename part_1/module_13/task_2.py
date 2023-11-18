print('Задача 2. Функция максимума')


def maximum_of_two(first_number, second_number):
    return int((abs(first_number - second_number) + first_number + second_number) / 2)


def maximum_of_three(first_number, second_number, third_number):
    return maximum_of_two(maximum_of_two(first_number, second_number), third_number)


first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
third_num = int(input('Введите третье число: '))

print(f'Максимальное число в этой тройке: {maximum_of_three(first_num, second_num, third_num)}')
