import math

print('Задача 3. Аналог Steam')
size_update = int(input('Укажите размер файла для скачивания: '))
internet_speed = int(input('Какова скорость вашего соединения: '))
downloadMb = 0
count_second = 0
if size_update < 0 or internet_speed < 0:
    print('Не бывает отрицательной скорости интернета или размера файла')
elif size_update == 0:
    print('На текущий момент обновлений нет')
elif internet_speed == 0:
    print('Ошибка соединения')
else:
    while downloadMb != size_update:
        count_second += 1
        downloadMb += internet_speed
        if downloadMb > size_update:
            downloadMb = size_update
        print(
            f'Прошло {count_second} сек. Скачано {downloadMb} из {size_update}'
            f' Мб ({math.ceil(downloadMb / size_update * 100)}%)')
