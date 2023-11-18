print('Задача 1. Должники')
debtor_sum = 0
for people in range(10):
    debtor = int(input(f'Введите номер {people + 1} гражданина: '))
    if (debtor % 2 == 0) and (debtor >= 0):
        debtor_sum += 1
print('Количество должников:', debtor_sum)
