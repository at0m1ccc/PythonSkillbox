def add_people(phone_book):
    name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split())
    if name in phone_book:
        print('Такой человек уже есть в контактах.')
    else:
        number_phone = int(input('Введите номер телефона: '))
        phone_book[name] = number_phone
    print(f'\nТекущий словарь контактов: {phone_book}\n')


def find_people(phone_book):
    surname = input('Введите фамилию для поиска: ').title()
    for i_person in phone_book:
        if surname in i_person:
            print(f'{i_person[0]} {i_person[1]} {phone_book[i_person]}')
    print()


phone_book = dict()

while True:
    action = int(input('Введите номер действия:\n \t1. Добавить контакт\n'
                       ' \t2. Найти человека\n \t3. Выйти из телефонной книги\nКоманда: '))
    if action == 1:
        add_people(phone_book)
    elif action == 2:
        find_people(phone_book)
    elif action == 3:
        print('Завершение работы')
        break
    else:
        print('Такой команды нет в списке. Попробуйте еще раз.')
