print('Задача 2. Функция в функции')


def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


def test():
    number = int(input('Введите число: '))
    if number >= 0:
        positive()
    else:
        negative()


test()
