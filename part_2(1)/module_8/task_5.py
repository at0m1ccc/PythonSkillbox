def make_list_of_lists(current_list):
    if not current_list:
        return []
    elif isinstance(current_list[-1], list):
        return make_list_of_lists(current_list[:-1]) + make_list_of_lists(current_list[-1])
    else:
        return make_list_of_lists(current_list[:-1]) + [current_list[-1]]


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(f'Ответ: {make_list_of_lists(nice_list)}')
