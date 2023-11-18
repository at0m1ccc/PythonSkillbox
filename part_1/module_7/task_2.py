print('Задача 2. Посчитай чужую зарплату...')
average_annual_salary = 0
for month in range(12):
    average_annual_salary += int(input(f'Введите зарплату за {month + 1} месяц в рублях: '))
print('Среднегодовая зарплата сотрудника:', average_annual_salary / 12, 'рублей')
