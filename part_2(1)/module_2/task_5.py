def control_weight(container):
    if container > 200:
        print('Ошибка! Вес контейнера не может превышать 200 кг! Повторите попытку!')
        return True
    return False


containers_list = []
count_containers = int(input('Количество контейнеров: '))
while count_containers != 0:
    container = int(input('Введите вес контейнера: '))
    if control_weight(container):
        continue
    containers_list.append(container)
    count_containers -= 1

new_container = int(input('Введите вес нового контейнера: '))
while control_weight(new_container):
    new_container = int(input('Введите корректный вес нового контейнера: '))

for index in range(len(containers_list)):
    if new_container > containers_list[index]:
        print(f'Номер, который получит новый контейнер: {index + 1}')
        break
