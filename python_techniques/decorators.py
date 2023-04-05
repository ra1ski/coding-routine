def print_start_end(func):
    def wrapper():
        print('start')
        func()
        print('end')

    return wrapper()


def print_name():
    print('Sam')


print_start_end(print_name)


@print_start_end
def print_name2():
    print('Sam 2')


def another_decorator(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')

        return result

    return wrapper


@another_decorator
def get_digit(x: int):
    return x


result = get_digit(5)
print(result)


class Power(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        value = self._func(args[0], args[1])
        return value ** 2

    # def __call__(self, a, b):
    #     value = self._func(a, b)
    #     return value ** 2


@Power
def multiply(a: int, b: int) -> int:
    return a * b


print(multiply(2, 2))
