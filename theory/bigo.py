import math

# O(log n)
def logn(n):
    while n > 1:
        n = math.floor(n / 2)
