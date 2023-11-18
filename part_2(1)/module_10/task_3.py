def check_users(file_name):
    with (open(file_name, 'r', encoding='utf-8') as users_file,
          open('registrations_bad.log', 'w', encoding='utf-8') as bad_users,
          open('registrations_good.log', 'w', encoding='utf-8') as good_users):
        list_users = [line.strip().split() for line in users_file]
        for user in list_users:
            try:
                if len(user) < 3:
                    raise IndexError('НЕ присутствуют все три поля')
                if not user[0].isalpha():
                    raise NameError('Поле «Имя» содержит НЕ только буквы')
                if user[1].count('@') != 1 and user[1].count('.') != 1:
                    raise SyntaxError('Поле «Имейл» НЕ содержит @ и/или точку')
                if int(user[2]) < 10 or int(user[2]) > 99:
                    raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')
            except IndexError:
                bad_users.write(' '.join(user) + '\t' * 2 + 'НЕ присутствуют все три поля\n')
            except NameError:
                bad_users.write(' '.join(user) + '\t' * 2 + 'Поле «Имя» содержит НЕ только буквы\n')
            except SyntaxError:
                bad_users.write(' '.join(user) + '\t' * 2 + 'Поле «Имейл» НЕ содержит @ и/или точку\n')
            except ValueError:
                bad_users.write(' '.join(user) + '\t' * 2 + 'Поле «Возраст» НЕ представляет число от 10 до 99\n')
            else:
                good_users.write(' '.join(user) + '\n')
            finally:
                list_users = []


check_users('registrations.txt')
