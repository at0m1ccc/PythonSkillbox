print('Задача 6. Коровы')
inf_about_stalls = input('Введите информацию о каждом из 10 стойлов (a - стойло свободно, b - занято): ')
milk_count = 0
index_stall = 0

for stall in inf_about_stalls:
    if (stall == ' ') or (stall == ',') or (stall == '.'):
        continue
    index_stall += 1
    if stall == 'b':
        milk_count += index_stall * 2

print(f'За день будет произведено  {milk_count} литров молока.')
