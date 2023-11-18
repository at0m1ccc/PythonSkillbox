import datetime
import functools


def logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f'Вызов функции: {func.__name__}')
            print(f'Документация функции: {func.__doc__}')
            return func(*args, **kwargs)
        except Exception as exc:
            error = f'Ошибка в функции {func.__name__}: {str(exc)}\n'
            with open('function_errors.log', 'a', encoding="utf-8") as file:
                file.write(f'{datetime.datetime.now()}: {error}')
            print(error)

    return wrapper


@logging
def function_1():
    """
    Какая-то документация!!!
    """
    print('Hello world\n')


@logging
def function_2():
    """
    А это другая документация!!!
    """
    print('Goodbye world\n')
    print(123 / 0)


function_1()
function_2()
