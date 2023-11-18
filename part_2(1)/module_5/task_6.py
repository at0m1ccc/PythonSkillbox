def reduction_data(data):
    result_data = []
    counter = 1
    for i_symbol in range(len(data)):
        if data[i_symbol] == data[i_symbol + 1:i_symbol + 2]:
            counter += 1
            continue
        result_data.append(data[i_symbol])
        result_data.append((str(counter)))
        counter = 1
    return ''.join(result_data)


list_data = input('Введите строку: ')
print(f'Закодированная строка: {reduction_data(list_data)}')
