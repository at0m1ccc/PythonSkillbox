films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
         'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
like_films = []
count_films = int(input('Сколько фильмов хотите добавить? '))

if count_films > 9:
    print(f'Упс. В нашем списке фильмов меньше, чем вы хотите добавить.'
          f' Кол-во желаемых фильмов уменьшено до {len(films)}.')
    count_films = 9
for _ in range(count_films):
    film = input('Введите название фильма: ')
    if any(cinema in film for cinema in films):
        like_films.append(film)
    else:
        print(f'Ошибка: фильма {film} у нас нет :(')

print('Ваш список любимых фильмов: ', end='')
for index in range(len(like_films)):
    if index != len(like_films) - 1:
        print(f'{like_films[index]}, ', end='')
    else:
        print(like_films[index], end='')
