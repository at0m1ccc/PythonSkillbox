def check_permission(required_permission: str):
    user_permissions_list = ['admin']

    def decorator_wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                if required_permission in user_permissions_list:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")
            except PermissionError:
                print(f'PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')

        return wrapper

    return decorator_wrapper


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
