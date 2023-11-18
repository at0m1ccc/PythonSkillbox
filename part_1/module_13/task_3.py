print('Задача 3. Число наоборот 2')


def reverse_number(number):
    while number % 10 == 0:
        number //= 10
    return int(str(number)[::-1])


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

reverse_first_num = reverse_number(first_number)
print('\nПервое число наоборот:', reverse_first_num)
reverse_second_num = reverse_number(second_number)
print('Второе число наоборот:', reverse_second_num)
sum_reverse_num = reverse_first_num + reverse_second_num
print('Сумма:', sum_reverse_num)
print('\nСумма наоборот:', reverse_number(sum_reverse_num))
