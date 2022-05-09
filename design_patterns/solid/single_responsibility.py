# Avoiding the GOD object
from typing import Any


class Entries:
    """ Collect entries """

    def __init__(self):
        self.entries = []
        self.count = 0

    def add(self, entry: Any):
        self.entries.append(entry)
        self.count += 1

    def remove(self, index: int):
        del self.entries[index]
        self.count -= 1

    def __str__(self):
        return ', '.join(self.entries)

    def save(self):
        """ Bad idea """
        ...


class Storage:
    """ Class responsible for storing, reading entries """

    @staticmethod
    def save_to_disk(entries: Entries, file_name: str):
        """
        Args:
            entries Entries:
            file_name file_name:
        """
        file = open(file_name, 'w')
        file.write(str(entries))
        file.close()

    @staticmethod
    def read_file(file_name: str) -> str:
        """
        Args:
            file_name str:
        Returns str:
        """
        with open(file_name) as fh:
            return fh.read()


if __name__ == '__main__':
    entries = Entries()
    entries.add('Hello')
    entries.add('World')
    entries.add('Nice')
    entries.add('to')
    entries.add('see')
    entries.add('you!')

    file_name = './entries.txt'

    Storage.save_to_disk(entries, file_name)

    print(Storage.read_file(file_name))
