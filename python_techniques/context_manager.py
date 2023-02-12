class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
        print('init: ', filename)

    def __enter__(self):
        self.file = open(self.filename, 'w')

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        if exc_type is not None:
            print('exception handled')
            print(exc_type, exc_val, exc_tb)

        print('exit')

        return True


with ManagedFile('lambda.py') as file:
    file.ss()

from contextlib import contextmanager


@contextmanager
def open_managed(filename):
    f = open(filename, 'w')

    try:
        print('inside manager')
        yield f
    finally:
        f.close()

with open_managed('lambda.py') as f:
    ...