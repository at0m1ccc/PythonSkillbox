import math

print('Задача 5. Вот это объёмы!')
radius_planet = float(input('Введите радиус теоретически возможной планеты: '))
volume_Earth = 1.08321 * 10 ** 12
volume_planet = 4 / 3 * math.pi * radius_planet ** 3
if volume_Earth > volume_planet:
    print(f'Объём планеты Земля больше в {round(volume_Earth / volume_planet, 3)} раз')
else:
    print(f'Объём планеты Земля меньше в {round(volume_planet / volume_Earth, 3)} раз')
