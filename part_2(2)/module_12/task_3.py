class MyDict(dict):
    """
    Класс MyDict унаследован от стандартного класса dict.
     Метод get переопределяется. Если ключа нет, то он возвращает 0.
    """

    def get(self, key, default=0):
        """
        Возвращает значение по ключу, если ключ присутствует, иначе 0.
        """
        return super().get(key, default)


my_dict = MyDict({'q': 10, 'w': 11})

print(f'Значение в словаре по ключу e = {my_dict.get('e')}')
print(f'Значение в словаре по ключу q = {my_dict.get('q')}')
print(f'Значение в словаре по ключу w = {my_dict.get('w')}')
