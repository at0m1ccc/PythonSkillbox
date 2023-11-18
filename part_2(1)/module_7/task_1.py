def find_all_interests_and_len_surname(data_dict):
    len_all_surname = 0
    result_list = []
    if len(data_dict) == 0:
        return [], 0
    for id, info in data_dict.items():
        if len(info) == 0:
            continue
        for key_info, value_info in info.items():
            if key_info == 'interests' and len(value_info) != 0:
                for interest in value_info:
                    result_list.append(interest)
            if key_info == 'surname':
                len_all_surname += len(value_info)
    return result_list, len_all_surname


students = {
1: {
'name': 'Bob',
'surname': 'Vazovski',
'age': 23,
'interests': ['biology, swimming']
},
2: {
'name': 'Rob',
'surname': 'Stepanov',
'age': 24,
'interests': ['math', 'computer games', 'running']
},
3: {
'name': 'Alexander',
'surname': 'Krug',
'age': 22,
'interests': ['languages', 'health food']
}
}

pairs = []
for id, info in students.items():
    for key_info, value_info in info.items():
        if key_info == 'age':
            pairs.append((id, value_info))

print(f'Список пар «ID студента — возраст»: {pairs}')
result_list, len_all_surname = find_all_interests_and_len_surname(students)

print(f'Полный список интересов всех студентов: {result_list}')
print(f'Общая длина всех фамилий студентов: {len_all_surname}')
