def singleton(cls):

    def wrapper():
        if cls.__copy is None:
            cls.__copy = cls()
        return cls.__copy

    cls.__copy = None
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
