print('Задача 8. Древний палиндром')
text = input('Введите текст: ')
cleaned_text = ''
for letter in text:
    if letter.isalpha():
        cleaned_text += letter.lower()
if cleaned_text == cleaned_text[::-1]:
    print('Да, это палиндром!')
else:
    print('Нет, это не палиндром!')
