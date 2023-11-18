print('Задача 4. Число наоборот')


def number_reverse(number):
    while number % 10 == 0:
        number //= 10
    reverse_num = int(str(number)[::-1])
    print('Число наоборот:', reverse_num)


while True:
    number = int(input('Введите число: '))
    if number == 0:
        print('Программа завершена!')
        break
    else:
        number_reverse(number)
