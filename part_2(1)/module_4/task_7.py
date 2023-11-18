nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
nice_list = [num for list_2lvl in nice_list for list_3lvl in list_2lvl for num in list_3lvl]
print(f'Ответ: {nice_list}')
