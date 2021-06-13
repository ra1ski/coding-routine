import pytest
from typing import List, Union


class QuickSort(object):
    """ Quick sort implementation with tests """
    parameters = [
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([5, 5, 3, 2, 3], [2, 3, 3, 5, 5]),
        ([5.0, 5.1, 3, 2.5, 3], [2.5, 3, 3, 5.0, 5.1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 9, 3, 4, 8, 2, 9, 8], [2, 3, 4, 5, 8, 8, 9, 9])
    ]

    def sort(self, items: Union[List[int], List[float]]) -> list:
        if len(items) <= 1:
            return items

        pivot = items.pop()
        left = []
        right = []

        for item in items:
            if item > pivot:
                right.append(item)
            else:
                left.append(item)

        return self.sort(left) + [pivot] + self.sort(right)


@pytest.mark.parametrize('items, expected', QuickSort.parameters)
def test_quick_sort(items: list, expected: list):
    quick_sort = QuickSort()

    assert expected == quick_sort.sort(items)
