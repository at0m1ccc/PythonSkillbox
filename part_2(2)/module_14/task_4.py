import functools


def counter(func, count_calls=dict()):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        count_calls[func] = count_calls.get(func, 0) + 1
        print(f'Функция {func.__name__} была вызвана {count_calls[func]} раз.')
        return func(*args, **kwargs)
    return wrapped


@counter
def test_1():
    pass


@counter
def test_2():
    pass


for i in range(10):
    test_1()
    if i % 2 == 0:
        test_2()
