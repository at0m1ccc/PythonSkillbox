print('Задача 3. Слишком большие числа')
number = int(input('Введите число: '))
current_number = number
sum_digits = 0
while True:
    current_number //= 10
    sum_digits += 1
    if current_number == 0:
        break
print(f'В числе {number} содержится {sum_digits} цифр.')
