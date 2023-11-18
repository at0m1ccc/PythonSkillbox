print('Задача 7. Хватит ли зарплаты')
hours = int(input('Введите количество отработанных часов: '))
credit = int(input('Введите остаток по кредиту: '))
price_food = int(input('Введите траты на еду: '))
salary = 200 * hours / 2 ** 3 + hours
if salary >= credit + price_food:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать больше!')
