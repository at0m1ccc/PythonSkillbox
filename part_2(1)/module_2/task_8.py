def bubble_sort(list_numbers):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(list_numbers) - 1):
            if list_numbers[index] > list_numbers[index + 1]:
                list_numbers[index], list_numbers[index + 1] = list_numbers[index + 1], list_numbers[index]
                swapped = True


random_list_numbers = [1, 4, -3, 0, 10]
print('Изначальный список:', random_list_numbers)
bubble_sort(random_list_numbers)
print('Отсортированный список: ', random_list_numbers)
