print('Задача 1. Космическая еда')
buckwheat_count = 100
months = 0
for buckwheat_count in range(buckwheat_count - 4, -1, -4):
    months += 1
    print(f'Через {months} месяц у вас останется {buckwheat_count} кг гречки')
