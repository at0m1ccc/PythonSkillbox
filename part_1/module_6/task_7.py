print('Задача 7. Игра «Угадай число»')
correct_number = 7
number_attempts = 0
while True:
    user_number = int(input('Введите число: '))
    number_attempts += 1
    if user_number == correct_number:
        print('Вы угадали! Число попыток:', number_attempts)
        break
    elif user_number > correct_number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
