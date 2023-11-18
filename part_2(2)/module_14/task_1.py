import functools


def how_are_you(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result_answer = input('Как дела? ')
        print('А у меня не очень!  Ладно, держи свою функцию.')
        return func(*args, **kwargs)

    return wrapper


@how_are_you
def test():
    print('Функция 0')


@how_are_you
def test1():
    print('Функция 1')


@how_are_you
def test2():
    print('Функция 2')


test()
test1()
test2()
