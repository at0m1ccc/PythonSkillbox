print('Задача 7. Сумма ряда')
need_number = int(input('Введите N: '))
summ = 0
for number in range(0, need_number):
    summ += ((-1) ** number) * (1 / 2 ** number)
print('Ответ:', summ)
