def bubble_sort(list_numbers):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(list_numbers) - 1):
            if list_numbers[index] > list_numbers[index + 1]:
                list_numbers[index], list_numbers[index + 1] = list_numbers[index + 1], list_numbers[index]
                swapped = True


def del_repeat(list_num):
    for i_num in list_num:
        if list_num.count(i_num) > 1:
            for _ in range(list_num.count(i_num) - 1):
                list_num.remove(i_num)


def merge_sorted_lists(list_1, list_2):
    if len(list_2) == 0 and len(list_1) == 0:
        return list_1
    elif len(list_1) == 0:
        del_repeat(list_2)
        return list_2
    elif len(list_2) == 0:
        del_repeat(list_1)
        return list_1
    else:
        list_1.extend(list_2)
        del_repeat(list_1)
        bubble_sort(list_1)
        return list_1


list1 = []
list2 = []
merged = merge_sorted_lists(list1, list2)
print(merged)
