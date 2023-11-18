import copy


def search_key(struct, key, value):
    if key in struct:
        struct[key] = value
        return site
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            sub_result = search_key(sub_struct, key, value)
            if sub_result:
                return site


def make_site(result_list, count_site):
    for _ in range(count_site):
        result_site = copy.deepcopy(site)
        product_name = input('Введите название продукта для нового сайта: ')
        key = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
        for index in key:
            search_key(result_site, index, key[index])
        result_list.append({product_name: result_site})
        for cuurent_site in result_list:
            for key, value in cuurent_site.items():
                print(f'Сайт для {key}:')
                print(value, '\n')


site = {
'html': {
'head': {
'title': 'Куплю/продам телефон недорого'
},
'body': {
'h2': 'У нас самая низкая цена на iPhone',
'div': 'Купить',
'p': 'Продать'
}
}
}

make_site([], int(input('Сколько сайтов: ')))
