print('Задача 8. Игра «Компьютер угадывает число»')
low = 0
hight = 100
while low <= hight:
    mid = (low + hight) // 2
    answer_player = int(
        input(f'Твоё число равно, меньше или больше, чем число {mid}? (1 - равно, 2 - больше, 3 - меньше) '))
    if answer_player == 1:
        print(f'Загаданное число = {mid}')
        break
    elif answer_player == 2:
        low = mid + 1
    else:
        hight = mid - 1
