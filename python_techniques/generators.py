def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# print(sorted(g))
# print(list(g))

generator2 = (i for i in range(10))
print(next(generator2), next(generator2))