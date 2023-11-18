from collections import defaultdict


def check_palindrom(text):
    counts_letter = defaultdict(int)
    for letter in text:
        if 97 <= ord(letter) <= 122:
            counts_letter[letter] += 1
    middle_letter = ""
    for letter in counts_letter:
        if middle_letter and counts_letter[letter] % 2 == 1:
            return False
        elif counts_letter[letter] % 2 == 1:
            middle_letter = letter
    return True


text = input('Введите строку: ').lower()

if check_palindrom(text):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
