print('Задача 4. Успеваемость в классе')
count_students = int(input('Введите количество учеников: '))
count_excellent_students = 0
count_goodies_students = 0
count_triples_students = 0
for student in range(count_students):
    estimation = int(input(f'Введите оценку {student + 1} ученика: '))
    if estimation == 5:
        count_excellent_students += 1
    elif estimation == 4:
        count_goodies_students += 1
    else:
        count_triples_students += 1
if (count_excellent_students > count_goodies_students) and (count_excellent_students > count_triples_students):
    print('Сегодня в классе больше всего отличников!')
elif (count_goodies_students > count_excellent_students) and (count_goodies_students > count_triples_students):
    print('Сегодня в классе больше всего хорошистов!')
else:
    print('Сегодня в классе больше всего троечников!')
