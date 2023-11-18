def numerals(list_peoples, number):
    start = 0
    while len(list_peoples) != 1:
        print(f'Текущий круг людей: {list_peoples}')
        print(f'Начало счёта с номера {list_peoples[start]}')
        start = (start + number) % len(list_peoples) - 1
        print(f'Выбывает человек под номером {list_peoples[start]}')
        list_peoples.remove(list_peoples[start])
        if start == -1:
            start = 0
        print()
    print(f'Остался человек под номером {list_peoples[0]}')


count_peoples = int(input('Количество человек: '))
number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number}-й человек\n')
peoples = list(range(1, count_peoples + 1))
numerals(peoples, number)
