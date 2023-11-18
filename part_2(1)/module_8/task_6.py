def split_list(current_list):
    support_number = current_list[len(current_list) - 1]
    return ([number for number in current_list if number < support_number],
            [number for number in current_list if number == support_number],
            [number for number in current_list if number > support_number])


def fast_sorted(current_list):
    if not current_list:
        return []
    first_list, second_list, third_list = split_list(current_list)
    return fast_sorted(first_list) + second_list + fast_sorted(third_list)


print(f'Отсортированный список: {fast_sorted([5, 8, 9, 4, 2, 9, 1, 8])}')
