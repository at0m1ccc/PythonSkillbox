from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = OrderedDict()

    @property
    def cache(self):
        if self._cache:
            key, value = next(iter(self._cache.items()))
            return f"{key} : {value}"
        else:
            return "Cache is empty"

    @cache.setter
    def cache(self, new_elem):
        if new_elem[0] in self._cache:
            del self._cache[new_elem[0]]
        elif len(self._cache) == self.capacity:
            self._cache.popitem(last=False)
        self._cache[new_elem[0]] = new_elem[1]

    def print_cache(self):
        print(f'{self.__class__.__name__}:')
        for key, value in self._cache.items():
            print(f"{key} : {value}")

    def get(self, key):
        value = self._cache.pop(key)
        self._cache[key] = value
        return value


cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.print_cache()
