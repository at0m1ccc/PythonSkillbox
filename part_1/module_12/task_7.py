import random

print('Задача 7. Недоделка')


def rock_paper_scissors():
    print('\nИгра "Камень, ноницы, бумага"\n')
    comp_choice = random.SystemRandom().choice(['камень', 'ножницы', 'бумага'])
    user_choice = input('Введите ваш выбор (камень, ножницы или бумага): ').lower()
    if (comp_choice == 'камень' and user_choice == 'ножницы') or (
            comp_choice == 'ножницы' and user_choice == 'бумага') or (
            comp_choice == 'бумага' and user_choice == 'камень'):
        print(f'Вы проиграли! Компьютер выбрал {comp_choice}\n')
    elif (comp_choice == 'камень' and user_choice == 'бумага') or (
            comp_choice == 'ножницы' and user_choice == 'камень') or (
            comp_choice == 'бумага' and user_choice == 'ножницы'):
        print(f'Вы выиграли! Компьютер выбрал {comp_choice}\n')
    elif comp_choice == user_choice:
        print(f'Ничья! Компьютер тоже выбрал {comp_choice}\n')
    else:
        print('Неверный ввод!!! Попробуйте снова!\n')
    mainMenu()


def guess_the_number():
    print('\nИгра "Угадай число"\n')
    random_num = random.randint(1, 100)
    attempts = 0
    while True:
        user_num = int(input('Введите число: '))
        attempts += 1
        if user_num > random_num:
            print('Число больше чем нужно. Попробуйте еще раз!')
        elif user_num < random_num:
            print('Число меньше чем нужно. Попробуйте еще раз!')
        else:
            print(f'Вы угадали число с {attempts} попытки\n')
            break
    mainMenu()


def mainMenu():
    choice = int(input(
        'Главное меню:\n1. Камень, ножницы, бумага\n2. Угадай число\n3. Выход из приложения\nВыберите действие: '))
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    elif choice == 3:
        print('Выход из приложения...')
    else:
        print('\nОшибка ввода!!!\n')
        mainMenu()


mainMenu()
