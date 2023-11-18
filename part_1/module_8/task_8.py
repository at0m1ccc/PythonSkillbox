print('Задача 8. Кинотеатр')
boys_count = int(input('Введите количество мальчиков: '))
girls_count = int(input('Введите количество девочек: '))
answer = ''
if (boys_count / girls_count > 2) or (girls_count / boys_count > 2):
    print('Ответ: Нет решения')
elif girls_count > boys_count:
    difference = girls_count - boys_count
    for string_gbg in range(difference):
        answer += 'GBG'
    for string_gb in range(boys_count - difference):
        answer += 'GB'
else:
    difference = boys_count - girls_count
    for string_bgb in range(difference):
        answer += 'BGB'
    for string_bg in range(girls_count - difference):
        answer += 'BG'
print('Ответ:', answer)
