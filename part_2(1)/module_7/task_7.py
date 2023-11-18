def my_zip(col_1, col_2):
    return ((col_1[index], col_2[index]) for index in range(min(len(col_2), len(col_1))))


text = 'enubcuew'
tuple_nums = (10, 20, 30, 40, 50)
print(f'Строка: {text}')
print(f'Кортеж чисел: {tuple_nums}')

result = my_zip(text, tuple_nums)

print('Результат:')
print(result)
for i_tpl in result:
    print(i_tpl)
