print('Задача 4. Калькулятор скидки')
price_chair_1 = int(input('Введите стоимость первого стула: '))
price_chair_2 = int(input('Введите стоимость второго стула: '))
price_chair_3 = int(input('Введите стоимость третьего стула: '))
check_amount = price_chair_1 + price_chair_2 + price_chair_3
if check_amount > 10000:
    check_amount = check_amount * 90 / 100
print('Итоговая сумма:', check_amount)
