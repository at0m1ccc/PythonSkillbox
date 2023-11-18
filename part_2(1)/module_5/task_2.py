text = input('Введите строку: ').split()
max_word = max(text, key=len)

print(f'Самое длинное слово: "{max_word}"')
print(f'Длина этого слова: {len(max_word)}')
