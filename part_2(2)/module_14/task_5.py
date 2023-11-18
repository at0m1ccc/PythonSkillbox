def memory(func):
    cache_dict = dict()

    def memory_func(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]

    return memory_func


@memory
def fibonacci(num):
    """
    Рекурсивная функция для вычисления чисел Фибоначчи.

    Args:
    - num (int): номер числа Фибоначчи

    Returns:
    - int: значение числа Фибоначчи
    """
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


number = 100
result = fibonacci(number)
print(f"{number}-е число Фибоначчи = {result}")
