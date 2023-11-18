import functools


app = dict()


def callback(_route: str):
    def callback_decorator(func):
        app[_route] = func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped

    return callback_decorator


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
