print('Задача 6. НОД')


def find_GCD(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    print(f'Наибольший общий делитель = {first_number + second_number}')


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
find_GCD(first_number, second_number)
