print('Задача 6. Игра в кубики')
player_cube = int(input('Введите число с кубика игрока: '))
owner_cube = int(input('Введите число с кубика владельца: '))
if player_cube >= owner_cube:
    print('Разность:', player_cube - owner_cube)
    print('Игрок платит!')
else:
    print('Сумма:', player_cube + owner_cube)
    print('Владелец платит!')
print('Игра окончена!')
