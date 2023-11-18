print('Задача 5. Отрезок')

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
average = 0
count_number = 0
for number in range(first_number, second_number + 1):
    if number % 3 == 0:
        count_number += 1
        average += number
average = average / count_number
print(f'Среднее арифметическое всех чисел из отрезка [{first_number}; {second_number}], кратных 3 = {average}')
