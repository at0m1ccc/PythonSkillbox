print('Задача 4. Марсоход 2')
position_x = 8
position_y = 10
while True:
    command = input(f'Марсоход находится на позиции {position_x}, {position_y}, введите команду: ')
    if (command == 'A') and (position_x > 0):
        position_x -= 1
    if (command == 'D') and (position_x < 15):
        position_x += 1
    if (command == 'S') and (position_y > 0):
        position_y -= 1
    if (command == 'W') and (position_y < 20):
        position_y += 1
