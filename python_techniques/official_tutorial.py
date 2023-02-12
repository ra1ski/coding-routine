# -- 4 --
print(list(range(5, 10)))
# [5, 6, 7, 8, 9]

print(list(range(0, 10, 3)))
# [0, 3, 6, 9]

print(list(range(-10, -100, -30)))
# [-10, -40, -70]

print(sum(range(4)))


# - 4.6 - match
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print('Http error: ', http_error(400))

code = 404

match code:
    case 401 | 403 | 404:
        print('4** error')

point = (0, 3)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        print('Not a point')


# class match
class Point:
    x: int
    y: int


def where_is(point: Point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


"""
from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
"""


# - 4.7. Function
def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end='')
        a, b = b, a + b
        print()


f = fib
print(fib)
f(100)


def fib2(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result


fib_result = fib2(100)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)

    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -- 4.8.5. Unpacking arguments
print(list(range(3, 6)))
range_list = [3, 6]


def multiply(a, b):
    return a * b


print(multiply(*range_list))
print(list(range(*range_list)))


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(*d)
# voltage state action

parrot(**d)

# -- 5. Data Structures --
# - 5.1.2. Using Lists as Queues

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
eric = queue.popleft()
print(eric)
print(queue)

# 5.4. Sets
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

# 5.9 loop techniques
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# -- 7. Input and Output --
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))


# -- 8. Exceptions --
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
