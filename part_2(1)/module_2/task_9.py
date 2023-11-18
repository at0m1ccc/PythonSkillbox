def reverse_sort_list(list_numbers):
    for index in range(len(list_numbers) // 2):
        list_numbers[-index - 1], list_numbers[index] = list_numbers[index], list_numbers[-index - 1]


def del_uneven_num(list_numbers):
    for index in range(len(list_numbers) - 1, -1, -1):
        if list_numbers[index] % 2 != 0:
            list_numbers.remove(list_numbers[index])


list_numbers = [-2, 33, 44, 4, 55, 66, -91, -20, 1019, 11, 100]
print('Начальный список:', list_numbers)
del_uneven_num(list_numbers)
reverse_sort_list(list_numbers)
print('Список четных чисел в обратном порядке:', list_numbers)
