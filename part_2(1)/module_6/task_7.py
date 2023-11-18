def find_items_in_each_list(arr_1, arr_2, arr_3):
    result_list = []
    for num in arr_1:
        if num in arr_2 and num in arr_3:
            result_list.append(num)
    print('Решение без множеств: ', end='')
    for num in result_list:
        print(num, end=' ')
    print()


def find_items_in_each_list_with_sets(arr_1, arr_2, arr_3):
    print('Решение с множествами: ', end='')
    for num in (set(arr_1) & set(arr_2) & set(arr_3)):
        print(num, end=' ')
    print()


def find_lim_num_list_1(arr_1, arr_2, arr_3):
    result_list = []
    for num in arr_1:
        if num not in arr_2 and num not in arr_3:
            result_list.append(num)
    print('Решение без множеств: ', end='')
    for num in result_list:
        print(num, end=' ')
    print()


def find_lim_num_list_1_with_set(arr_1, arr_2, arr_3):
    print(f'Решение с множествами: ', end='')
    for num in (set(arr_1) - set(arr_2) - set(arr_3)):
        print(num, end=' ')
    print()


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Задача 1:')
find_items_in_each_list(array_1, array_2, array_3)
find_items_in_each_list_with_sets(array_1, array_2, array_3)

print('\nЗадача 2:')
find_lim_num_list_1(array_1, array_2, array_3)
find_lim_num_list_1_with_set(array_1, array_2, array_3)
