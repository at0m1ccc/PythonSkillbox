while True:
    password = input('Придумайте пароль: ')
    password_num = [num for num in password if num.isalnum()]
    password_up_letter = [letter for letter in password_num if letter.isupper()]
    if len(password) >= 8 and len(password_num) >= 3 and len(password_up_letter) >= 1:
        print('Это надёжный пароль.')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
