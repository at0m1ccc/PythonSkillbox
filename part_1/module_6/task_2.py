print('Задача 2. Коллекторы')
name_debtor = input('Введите имя должника: ')
total_debt = int(input('Введите сумму долга: '))
amount_repaid = 0
print(f'{name_debtor}, ваша задолженность составляет {total_debt} рублей.')
while amount_repaid < total_debt:
    amount_repaid = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    if amount_repaid >= total_debt:
        print(f'Отлично, {name_debtor}! Вы погасили долг. Спасибо!')
        break
    print(f'Маловато, {name_debtor}. Давайте ещё раз.')
