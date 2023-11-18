print('Задача 5. Наибольшая сумма цифр')
count_number = int(input('Введите количество чисел: '))
max_number = 0
max_sum = 0
for iteration_number in range(count_number):
    number = int(input('Введите число: '))
    current_number = number
    sum_number = 0
    while current_number > 0:
        sum_number += current_number % 10
        current_number //= 10
    if sum_number > max_sum:
        max_sum = sum_number
        max_number = number
print(f'{max_number} - число наибольшее по сумме цифр, с суммой цифр = {max_sum}')
