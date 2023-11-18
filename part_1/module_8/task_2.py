print('Задача 2. Долги')
debtors = int(input('Введите количество должников: '))
debtors_sum = 0
for debtor in range(0, debtors, 5):
    print(f'Должник с номером {debtor}')
    debtors_sum += int(input('Сколько должны? '))
print('Общая сумма долга:', debtors_sum)
