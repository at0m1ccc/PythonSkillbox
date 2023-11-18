print('Задача 6. Стипендия')
educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
expenses_sum = 0
for month in range(1, 11):
    if month != 1:
        expenses = expenses * 1.03
    expenses_sum += expenses - educational_grant
    print(f'{month}. месяц траты {expenses} не хватает {expenses_sum}')
print(f'Нужно попросить у родителей {expenses_sum} рублей')
