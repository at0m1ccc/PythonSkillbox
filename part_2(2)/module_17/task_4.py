def count_unique_characters(text: str) -> int:
    unique_chars = set(text.lower())
    unique_chars.discard(' ')
    result = list(filter(lambda x: text.count(x) == 1, unique_chars))
    print(result)
    return len(result)


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке -", unique_count)
