count_pair_word = int(input('Введите количество пар слов: '))
synonyms_dict = dict()
for index_pair in range(count_pair_word):
    word_pair = input(f'{index_pair + 1}-ая пара: ').lower().split()
    synonyms_dict[word_pair[0]] = word_pair[len(word_pair) - 1]
    synonyms_dict[word_pair[len(word_pair) - 1]] = word_pair[0]

while True:
    word = input('Введите слово: ')
    if word in synonyms_dict:
        print(f'Синоним: {synonyms_dict[word].title()}')
        break
    print('Такого слова в словаре нет.')
