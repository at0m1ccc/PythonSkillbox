def shift_list(current_lst, shift):
    if shift >= len(current_lst):
        shift %= len(current_lst)
    return current_lst[-shift:] + current_lst[:-shift]


current_list = [1, 4, -3, 0, 10]
shift = int(input('Сдвиг: '))

print('Изначальный список:', current_list)

current_list = shift_list(current_list, shift)

print('Сдвинутый список:', current_list)
