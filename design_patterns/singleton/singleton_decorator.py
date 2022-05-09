def singleton(a_class):
    """
    Singleton decorator
    Returns:
        object:
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if a_class not in instances:
            instances[a_class] = a_class(*args, **kwargs)

        return instances[a_class]

    return get_instance


@singleton
class Database():
    def __init__(self):
        print('Hello from __init__. Should be called once.')


def test_singleton():
    db1 = Database()
    db2 = Database()

    assert db1 == db2
    assert id(db1) == id(db2)
