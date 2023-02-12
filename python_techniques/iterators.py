text = 'abs'

for letter in text:
    print(letter)

iterable_text = iter(text)
print(next(iterable_text))
print(next(iterable_text))
print(next(iterable_text))


# StopIteration exception
# print(next(iterable_text))

class Reverse:
    def __init__(self, data: str):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1

        return self.data[self.index]


reverse_obj = Reverse('Hello')
iter(reverse_obj)

# for char in reverse_obj:
#     print(char)

print('\n')
print(next(reverse_obj))
print(next(reverse_obj))
print(next(reverse_obj))
print(next(reverse_obj))
print(next(reverse_obj))

print('\n')


# Generators
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


gen = reverse('golf')

# for char in gen:
#     print(char)

print(next(gen))