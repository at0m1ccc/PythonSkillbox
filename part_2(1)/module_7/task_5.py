def tuple_sort(tuple_numbers):
    list_numbers = list(tuple_numbers)
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(list_numbers) - 1):
            if type(list_numbers[index]) != int:
                print('Не все числа в кортеже целые. Сортировка не удалась.')
                return tuple_numbers
            if list_numbers[index] > list_numbers[index + 1]:
                list_numbers[index], list_numbers[index + 1] = list_numbers[index + 1], list_numbers[index]
                swapped = True
    print('Сортировка прошла успешно.')
    return tuple(list_numbers)


# tuple_nums = (6, 3, -1, 8, 4, 10, -5)
# print(f'Результат: {tuple_sort(tuple_nums)}')
