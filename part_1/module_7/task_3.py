print('Задача 3. Факториал')
user_number = int(input('Введите число: '))
factorial = 1
for number in range(1, user_number + 1):
    factorial *= number
print(f'Факториал числа {user_number} равен {factorial}')
