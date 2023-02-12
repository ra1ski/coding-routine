x = lambda a: a * 2
print(x(5))

y = lambda a, b: a + b
print(y(5, 10))

z = lambda a, b, c: a + b + c
print(z(5, 10, 5))


def myfunc(n):
    return lambda a: a * n


doubler = myfunc(2)
print(doubler(100))

