print('Задача 4. Отрезок')
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))
number_sum = 0
number_count = 0
for number in range(first_number, second_number + 1):
    if number % third_number == 0:
        number_sum += number
        number_count += 1
if number_count != 0:
    print(
        f'Среднее арифметическое чисел на отрезке [{first_number}; {second_number}]'
        f' кратных {third_number} = {number_sum / number_count}')
else:
    print(f'Среднее арифметическое чисел на отрезке [{first_number}; {second_number}] кратных {third_number} = 0')
