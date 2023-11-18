def inverted_dict(dictionary):
    result_dict = dict()
    for letter, freq in dictionary.items():
        if freq in result_dict:
            result_dict[freq].append(letter)
        else:
            result_dict[freq] = [letter]
    return result_dict


def make_histogram(text):
    result_dict = dict()
    for letter in text:
        if letter in result_dict:
            result_dict[letter] += 1
        else:
            result_dict[letter] = 1
    return result_dict


text = input('Введите текст: ').lower()
origin_dict = make_histogram(text)

print('Оригинальный словарь частот:')
for letter, freq in origin_dict.items():
    print(letter, ':', freq)

inv_dict = inverted_dict(origin_dict)

print('Инвертированный словарь частот:')
for freq, letter_list in inv_dict.items():
    print(freq, ':', letter_list)
