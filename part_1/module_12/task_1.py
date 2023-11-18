print('Задача 1. Сумма чисел')


def summa_n(number):
    summ = 0
    for current_num in range(1, number + 1):
        summ += current_num
    print(f'Я знаю, что сумма чисел от 1 до {number} равна {summ}')


number = int(input('Введите число: '))
summa_n(number)
