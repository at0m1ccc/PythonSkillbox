shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_detail = input('Название детали: ').lower()
count_detail = 0
full_price = 0

for i_detail in range(len(shop)):
    if shop[i_detail][0] == name_detail:
        full_price += shop[i_detail][1]
        count_detail += 1

print(f'Количество деталей: {count_detail}')
print(f'Общая стоимость: {full_price}')
