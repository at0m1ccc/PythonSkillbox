def order_add_people(data_dict, pizza_key, amount_value):
    data_dict[pizza_key] = data_dict.setdefault(pizza_key, 0) + int(amount_value)
    return data_dict


data = {}
for index_order in range(int(input('Введите кол-во заказов: '))):
    fcs, pizza, amount = input(f'{index_order + 1}-ый заказ: ').rsplit(maxsplit=3)
    data[fcs] = order_add_people(data.get(fcs, {}), pizza, amount)

for name in sorted(data):
    print(f'{name}:')
    for pizza, amount in sorted(data.get(name).items()):
        print(f'     {pizza}: {amount}')
