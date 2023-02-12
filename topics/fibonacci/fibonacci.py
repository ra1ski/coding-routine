def fib_bottom_up(n):
    cache = [0] * (n + 1)
    cache[1] = 1

    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache


print(fib_bottom_up(6))

cache = {0: 0, 1: 1}


def fib_top_down(n):
    if n in cache:
        return cache[n]

    cache[n] = fib_top_down(n - 1) + fib_top_down(n - 2)

    return cache[n]


print(fib_top_down(6))
print(cache)

# class Solution:
#     cache = {0: 0, 1: 1}
#
#     def fib2(self, n: int) -> int:
#         if n <= 1:
#             return n
#
#         cache = [0] * (n + 1)
#         cache[1] = 1
#
#         for i in range(2, n + 1):
#             cache[i] = cache[i - 1] + cache[i - 2]
#
#         return cache[n]
#
#     def fib(self, n: int) -> int:
#         if n in self.cache:
#             return self.cache[n]
#
#         self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
#
#         return self.cache[n]
#
#     def fib0(self, n: int) -> int:
#         if n <= 1:
#             return n
#
#         return self.fib(n - 1) + self.fib(n - 2)

#
#
#
# def get_fib(position):
#     fib = 0
#
#     if position == 0:
#         return fib
#
#     first, second = 0, 1
#
#     for i in range(1, position + 1):
#         if i == position:
#             return fib
#
#         fib = first + second
#
#         first = second
#         second = fib
#
#     return -1
#
#
# # Test cases
# print(get_fib(9))
# print(get_fib(11))
# print(get_fib(0))


# def fib(n: int):
#     first, second = 0, 1
#
#     for i in range(n):
#         if i in [0, 1]:
#             print(i)
#         else:
#             next = first + second
#             first = second
#             second = next
#             print(next)
#
#
# fib(5)

# calc = 0
#
#
# def fib(n: int):
#     if n < 2:
#         return n
#
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(2))
# print(calc)
#
# fib_hash = {0: 0, 1: 1}
# dynamic_calc = 0
#
#
# def dynamic_fib(n: int):
#     if n in fib_hash:
#         return fib_hash[n]
#     else:
#         fib_hash[n] = dynamic_fib(n - 1) + dynamic_fib(n - 2)
#         return fib_hash[n]
#
#
# print(dynamic_fib(4))
# print(dynamic_calc)


# def d_fib(n: int):
#     f = {0: 0, 1: 1}
#
#     for i in range(2, n+1):
#         f[i] = f[i - 1] + f[i - 2]
#
#     return list(f.values())
#
# print(d_fib(5))
#
