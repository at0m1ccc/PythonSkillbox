print('Задача 6. Новоселье')
price_flat = int(input('Введите стоимость квартиры: '))
area_flat = int(input('Введите площадь квартиры: '))
if (price_flat <= 10) and (area_flat >= 100) or (price_flat <= 7) and (area_flat >= 80):
    print('Квартира подходит!')
else:
    print('Квартира не подходит!')
