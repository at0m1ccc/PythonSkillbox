def count_letter_in_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as peoples:
        peoples_list = peoples.read().split('\n')
        count_letter = 0
        for i_people, people in enumerate(peoples_list):
            try:
                count_letter += len(people)
                if len(people) < 3:
                    raise ValueError
            except ValueError as exc:
                print(f'Ошибка: менее трёх символов в строке {i_people + 1}.')
                with open('errors.log', 'w', encoding='utf-8') as file_exception:
                    file_exception.write(f'Строка под номером {i_people + 1}: {type(exc)}')
    print(f'Общее количество символов: {count_letter}.')


count_letter_in_text('people.txt')
