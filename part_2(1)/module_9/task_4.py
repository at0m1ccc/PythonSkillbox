def find_people_for_new_tour(file_name):
    file_first_tour = open(file_name, 'r')
    min_point = int(file_first_tour.readline())

    list_first_tour = [[players[1].strip().split()[2], players[1].split()[1][0] + '.', players[1].split()[0]]
                       for players in enumerate(file_first_tour)
                       if int(players[0]) > 0 and int(players[1].strip().split()[2]) > min_point]

    file_first_tour.close()
    list_first_tour.sort(reverse=True)
    file_second_tour = open('second_tour.txt', 'w')
    file_second_tour.write(str(len(list_first_tour)) + '\n')
    for index, people in enumerate(list_first_tour):
        file_second_tour.write(str(index + 1) + ')' + ' ' + people[1] + ' ' + people[2] + ' ' + people[0] + '\n')
    file_second_tour.close()


find_people_for_new_tour('first_tour.txt')
