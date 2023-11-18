print('Задача 4. Простые числа')
count_number = int(input('Введите количество чисел: '))
count_prime_number = 0
for iteration_number in range(count_number):
    number = int(input('Введите число: '))
    was_divider = 0
    for divider in range(2, number):
        if number % divider == 0:
            was_divider = 1
        if was_divider:
            break
    if not was_divider:
        count_prime_number += 1
print()
print(f'Количество простых чисел в последовательности: {count_prime_number}.')
