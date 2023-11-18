print('Задача 5. Функция')
start_section = int(input('Введите начало отрезка: '))
stop_section = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг: '))
if start_section > stop_section:
    start_section, stop_section = stop_section, start_section
if step > 0:
    step = -step
for number in range(stop_section, start_section - 1, step):
    function_value = number ** 3 + 2 * number ** 2 - 4 * number + 1
    print(f'В точке {number} функция равна {function_value}')
