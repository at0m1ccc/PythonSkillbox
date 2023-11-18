def find_count_all_letter(file_name):
    str_text = open(file_name, 'r').read().lower()
    result = {}
    count_letter = 0
    for letter in str_text:
        if ord('a') <= ord(letter) <= ord('z'):
            count_letter += 1
            result[letter] = result.get(letter, 0) + 1
    for letter in result:
        result[letter] = str(round(result[letter] / count_letter, 3))
    return sort_frequency_analysis(result)


def sort_frequency_analysis(letter_count_dict):
    sort_letter_count = {}
    str_result = ''
    for letter in letter_count_dict:
        if letter_count_dict[letter] not in sort_letter_count:
            sort_letter_count[letter_count_dict[letter]] = [letter]
        else:
            sort_letter_count[letter_count_dict[letter]].append(letter)
    for letter_count in sorted(sort_letter_count.keys(), reverse=True):
        for sym in sorted(sort_letter_count[letter_count]):
            str_result += sym + ' ' + letter_count + '\n'
    return str_result


open('analysis.txt', 'w').write(find_count_all_letter('text.txt'))
