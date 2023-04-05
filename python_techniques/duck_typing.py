# LBYL - Look before you leap
# EAFP - Easier to ask forgiveness than permission
import os


class Duck:
    def quack(self):
        print('Quack')

    def fly(self):
        print('Fly')


class Person:
    def quack(self):
        print('I quack like a duck')

    def fly(self):
        print('I fly like a duck')


def quack_and_fly_LBYL(bird):
    if hasattr(bird, 'quack'):
        bird.quack()

    if hasattr(bird, 'fly') and callable(bird.fly):
        bird.fly()

    if hasattr(bird, 'quack') and callable(bird.quack):
        bird.quack()


def quack_and_fly_EAFP(bird):
    try:
        bird.quack()
        bird.fly()
        bird.bark()
    except AttributeError as e:
        print(e)


# duck = Duck()
# person = Person()
#
# quack_and_fly_LBYL(duck)
# quack_and_fly_LBYL(person)
#
# quack_and_fly_EAFP(duck)
# quack_and_fly_EAFP(person)

worker = {'name': 'James', 'age': 20, }

# LBYL
if 'name' in worker and 'age' in worker and 'job' in worker:
    print('{name} is {age} yo. {job}'.format(**worker))
else:
    print('Key error')

# EAFP
try:
    print('{name} is {age} yo. {job}'.format(**worker))
except KeyError as e:
    print('Missing key {}'.format(e))

# Files and race condition

file_name = 'some_file.txt'

# Race condition
if os.access(file_name, os.R_OK):
    with open(file_name) as f:
        print(f.read())
else:
    print('File can not be accessed')

# No race condition
try:
    f = open(file_name)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())

# No race condition
try:
    with open(file_name) as f:
        print(f.read())
except IOError as e:
    print('File can not ne accessed')
