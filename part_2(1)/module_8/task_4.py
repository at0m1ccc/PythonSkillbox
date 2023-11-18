def my_sum(*args):
    result = 0
    for arg in enumerate(args):
        if isinstance(arg[1], int):
            result += arg[1]
        elif isinstance(arg[1], list):
            for elem in enumerate(arg[1]):
                result += my_sum(elem[1])
        else:
            continue
    return result


# print(f'Сумма = {my_sum([[1, 2, [3]], [1], 3])}')
# print(f'Сумма = {my_sum(1, 2, 3, 4, 5)}')
