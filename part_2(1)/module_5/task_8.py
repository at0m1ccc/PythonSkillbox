def cyclic_shift(first_str, second_str):
    if len(first_str) != len(second_str):
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
        return
    for shift in range(1, len(second_str)):
        if first_str == second_str[-shift:] + second_str[:-shift]:
            print(f'Первая строка получается из второй со сдвигом {shift}.')
            return
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
cyclic_shift(first_str, second_str)
