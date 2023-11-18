import zipfile


def unpacking_zip_file(zip_file_name):
    z_file = zipfile.ZipFile(zip_file_name, 'r')
    for i_file_name in z_file.namelist():
        z_file.extract(i_file_name)
        need_file_name = i_file_name
    z_file.close()
    return need_file_name


def find_count_all_letter(file_name):
    result = {}
    count_letter = 0
    if file_name.endswith('.zip'):
        file_name = unpacking_zip_file(file_name)
    text = open(file_name, 'r')
    for line in text:
        for letter in line:
            if letter.isalpha():
                count_letter += 1
                result[letter] = result.get(letter, 0) + 1
    for letter in result:
        result[letter] = str(round(result[letter] / count_letter, 6))
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


open('analysis_voina-i-mir.txt', 'w').write(find_count_all_letter('voina-i-mir.zip'))
