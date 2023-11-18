def is_prime(index):
    if index < 2:
        return False
    for num in range(2, index):
        if index % num == 0:
            return False
    return True


def crypto(collection):
    return [value for index, value in enumerate(collection) if is_prime(index)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
