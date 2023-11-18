print('Задача 4. Поставьте оценку!')
positive_numbers_count = 0
negative_numbers_count = 0
while True:
    current_number = int(input('Введите число: '))
    if current_number == 0:
        print('Кол-во положительных чисел:', positive_numbers_count)
        print('Кол-во отрицательных чисел:', negative_numbers_count)
        break
    elif current_number > 0:
        positive_numbers_count += 1
    else:
        negative_numbers_count += 1
