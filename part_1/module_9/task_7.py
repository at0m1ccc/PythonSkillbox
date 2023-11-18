print('Задача 7. Метод бутерброда')
word = input('Введите зашифрованное сообщение: ')
index_letter = 0
need_word = ''

print('Расшифрованное сообщение:', end=' ')
for letter in word[::-1]:
    if index_letter % 2 == 0:
        need_word += letter
    else:
        need_word = letter + need_word
    index_letter += 1

print(need_word)
