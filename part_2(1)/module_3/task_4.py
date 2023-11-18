guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    answer = input('Гость пришёл или ушёл? ').lower()
    if answer == 'пришёл' or answer == 'пришел' or answer == 'ушёл' or answer == 'ушел':
        name_guest = input('Имя гостя: ')
        if answer == 'пришёл' or answer == 'пришел':
            if len(guests) == 6:
                print(f'Прости, {name_guest}, но мест нет.')
            else:
                print(f'Привет, {name_guest}!')
                guests.append(name_guest)
        elif answer == 'ушёл' or answer == 'ушел':
            print(f'Пока, {name_guest}!')
            guests.remove(name_guest)
    elif answer == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    else:
        print('Ошибка ввода! Такой команды нет!')
    print()
