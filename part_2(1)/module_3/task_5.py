violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]

song_count = int(input('Сколько песен выбрать? '))
general_time_songs = 0
for i_song_count in range(song_count):
    name_song = input(f'Название {i_song_count + 1}-й песни: ')
    for i_song in range(len(violator_songs)):
        if violator_songs[i_song][0] == name_song:
            general_time_songs += violator_songs[i_song][1]
            break
        if i_song == len(violator_songs) - 1:
            print('Такой песни нет в списке!')

print(f'Общее время звучания песен — {round(general_time_songs, 2)} минуты')

