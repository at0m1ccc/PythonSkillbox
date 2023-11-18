tournament_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
tour_list_day1 = []

for index, name in enumerate(tournament_list):
    if index % 2 == 0:
        tour_list_day1.append(name)

print('Первый день:', tour_list_day1)