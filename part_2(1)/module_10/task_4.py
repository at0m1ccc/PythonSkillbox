import os


def users_chat():
    while True:
        try:
            user_name = input('Введите ваше имя: ').title()
            if not user_name.isalpha():
                raise NameError
        except NameError:
            print('\nОшибка при вводе имени')
            continue
        file_name = os.path.join('chat_history.txt')
        with open(file_name, 'a', encoding='utf-8') as chat_users_file:
            try:
                action = int(input('Выберите действие(число):\n'
                                   '1) Посмотреть текущий текст чата\n'
                                   '2) Отправить сообщение\n'
                                   '3) Выключить приложение\n'
                                   'Действие: '))
                if action == 1:
                    if os.stat(file_name).st_size == 0:
                        raise FileNotFoundError('Чат пуст начните общений')
                    else:
                        print('Сообщения чата:')
                        with open(file_name, 'r', encoding='utf-8') as users_file:
                            for line in users_file:
                                print(line.rstrip())
                elif action == 2:
                    message = input('Введите сообщение: ')
                    if isinstance(message, str):
                        chat_users_file.write(f'{user_name}: {message}\n')
                    else:
                        raise ValueError('Ошибка ввода сообщения')
                elif action == 3:
                    print('Приложение закрывается.')
                    break
                else:
                    raise Exception('Такое действие отсуствует.')
                print()
            except (FileNotFoundError, ValueError, Exception) as exc:
                print(exc)


users_chat()
