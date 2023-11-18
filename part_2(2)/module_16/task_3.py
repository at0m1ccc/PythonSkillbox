import datetime
import time
import functools


def logged(cls, func, form_str):
    """Декоратор для логирования вызываемого метода класса."""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print(f'Запускается "{cls.__name__}.{func.__name__}". '
              f'Дата и время запуска: {datetime.datetime.now().strftime(form_str)}')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f'Завершение "{cls.__name__}.{func.__name__}", '
              f'время работы = {round(end, 3)}s')
        return result

    return wrapped


def log_methods(form_str: str):
    """Декоратор для логирования класса."""

    def wrapped(cls):
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            value = getattr(cls, i_method)
            if hasattr(value, '__call__'):
                decorated_a = logged(cls, value, form_str)
                setattr(cls, i_method, decorated_a)
        return cls

    return wrapped


@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1.')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num * 2 for i_num in range(10000)])
        return result


@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника.")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника.")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num * 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
