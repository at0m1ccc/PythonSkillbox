import functools
import time


def wait(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(5)
        return func(*args, **kwargs)
    return wrapper


@wait
def test():
    print('Функция сработала!')


test()
