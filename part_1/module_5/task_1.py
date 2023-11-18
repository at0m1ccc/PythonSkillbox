print('Задача 1. Калькулятор опыта')
experience_points = int(input('Введите количество опыта: '))
level = 1
if 1000 <= experience_points < 2500:
    level = 2
elif 2500 <= experience_points < 5000:
    level = 3
elif experience_points >= 5000:
    level = 4
print('Ваш уровень:', level)
