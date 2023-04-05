import operator
from cgitb import small
from itertools import product, permutations, combinations, accumulate, groupby

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(prod)
print(list(prod))

a = [1, 2, 3]
print(list(permutations(a)))
print(list(combinations(a, 2)))
b = [1, 2, 3, 4, 5]
print(list(accumulate(b)))
print(list(accumulate(b, operator.mul)))


def smaller_than_3(x):
    return x < 3


c = [1, 2, 3, 4, 5]
# groupby_result = groupby(c, key=smaller_than_3)
groupby_result = groupby(c, key=lambda x: x < 3)

for k, v in groupby_result:
    print(k, list(v))

persons = [
    {"name": "John", "age":25},
    {"name": "Dan", "age":25},
    {"name": "Lisa", "age":27},
    {"name": "Claire", "age":28},
]

grouped_persons = groupby(persons, key=lambda x: x["age"])
for category, group in grouped_persons:
    print(category, list(group))

