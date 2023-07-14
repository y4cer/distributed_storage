from distributed_storage.value import Value
from storage import Storage


class NoSuchKeyInStoragePresent(Exception):
    def __init__(self, key):
        self.key = key


class DictionaryStorage(Storage):

    def get_value(self, key: str) -> Value:
        if key not in self.storage:
            raise NoSuchKeyInStoragePresent(key)
        return self.storage[key]

    def store_value(self, key: str, value: Value):
        self.storage[key] = value

    def __init__(self):
        self.storage = dict()