goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',
}

store = {
'12345': [
{'quantity': 27, 'price': 42},
],
'23456': [
{'quantity': 22, 'price': 510},
{'quantity': 32, 'price': 520},
],
'34567': [
{'quantity': 2, 'price': 1200},
{'quantity': 1, 'price': 1150},
],
'45678': [
{'quantity': 50, 'price': 100},
{'quantity': 12, 'price': 95},
{'quantity': 43, 'price': 97},
],
}

for name, value in goods.items():
    count_product = 0
    sum_price_product = 0
    for store_value in store[value]:
        count_product += store_value['quantity']
        sum_price_product += store_value['quantity'] * store_value['price']
    print(f'{name} — {count_product} штуки, стоимость {sum_price_product} рублей.')

