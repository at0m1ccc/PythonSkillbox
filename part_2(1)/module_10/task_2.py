import random


def play_vicious_cycle():
    sum_number = 0
    try:
        with open('out_file.txt', 'w') as out_file:
            while sum_number < 777:
                number = int(input('Введите число: '))
                if random.randint(0, 14) == 7:
                    raise ValueError('Вас постигла неудача!')
                sum_number += number
                out_file.write(str(number) + '\n')
    except ValueError:
        print('Вас постигла неудача!')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')


play_vicious_cycle()
