first_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]

first_list.extend(second_list)
print(f'Количество цифр 5 при первом объединении: {first_list.count(5)}')
for i_num_5 in first_list:
    if i_num_5 == 5:
        first_list.remove((i_num_5))
first_list.extend(third_list)
print(f'Количество цифр 3 при втором объединении: {first_list.count(3)}')
print(f'Итоговый список: {first_list}')