class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super().__call__(*args, **kwargs)

        return self._instances[self]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Hello from __init__. Should be called once.')


def test_singleton():
    db1 = Database()
    db2 = Database()

    assert db1 == db2
    assert id(db1) == id(db2)
