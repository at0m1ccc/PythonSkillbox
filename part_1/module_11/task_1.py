print('Задача 1. Конвертация')
price_euro = float(input('Введите цену в евро: '))
price_ruble = round(price_euro * 1.25 * 60.87, 2)
print(f'Стоимость покупки составляет: {price_ruble} рублей.')
