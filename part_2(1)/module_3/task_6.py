roller_skates = []
peoples = []

count_roller = int(input('Количество роликов: '))
for i_roller_count in range(count_roller):
    size_roller = int(input(f'Размер пары {i_roller_count + 1}: '))
    roller_skates.append(size_roller)

count_people = int(input('Количество людей: '))
for i_people_count in range(count_people):
    size_foot_people = int(input(f'Размер ноги человека {i_people_count + 1}: '))
    peoples.append(size_foot_people)

count_people_can_ride = 0
for i_people in range(count_people):
    if roller_skates.count(peoples[i_people]) != 0:
        count_people_can_ride += 1
        roller_skates.remove(roller_skates[roller_skates.index(peoples[i_people])])

print(f'Наибольшее количество людей, которые могут взять ролики: {count_people_can_ride}')
