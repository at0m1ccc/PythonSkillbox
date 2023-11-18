def find_element(current_dict, key, lvl_deep=0):
    if key in current_dict:
        return current_dict[key]
    if lvl_deep - 1:
        for value in current_dict.values():
            if isinstance(value, dict):
                result = find_element(value, key, lvl_deep - 1)
                if result:
                    return result
    return None


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },

    'body': {
        'h2': 'Здесь будет мой заголовок',
        'div': 'Тут, наверное, какой-то блок',
        'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('Введите искомый ключ: ')
need_deep = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if need_deep == 'y':
    max_deep = int(input('Введите максимальную глубину: '))
    print(f'Значение ключа: {find_element(site, user_key, max_deep)}')
elif need_deep == 'n':
    print(f'Значение ключа: {find_element(site, user_key)}')
else:
    print('Ошибка ввода!')
