from itertools import accumulate
from typing import List

import pytest


class NumArray:
    parameters = [
        ([-2, 0, 3, -5, 2, -1], [[0, 2], [2, 5], [0, 5]], [None, 1, -1, -3]),
        ([1, 2, 3, 4, 5, 6, 7], [[0, 2], [2, 5], [0, 5]], [None, 6, 18, 21])
    ]

    def __init__(self, nums: List[int]):
        self.nums = self.get_prefix_sum(nums)
        # self.nums = self.get_prefix_sum2(nums)
        # self.nums = self.get_prefix_sum_accumulated(nums)

    def sumRange(self, left: int, right: int) -> int:
        if 0 == left:
            return self.nums[right]

        return self.nums[right] - self.nums[left - 1]

    # To check MVP
    def sumRangeTheEasiestWay(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])

    @staticmethod
    def get_prefix_sum_accumulated(nums):
        return list(accumulate(nums))

    @staticmethod
    def get_prefix_sum(nums):
        result = []

        for i in range(len(nums)):
            if 0 == i:
                result.append(nums[i])
            else:
                result.append(nums[i] + result[i - 1])

        return result

    @staticmethod
    def get_prefix_sum2(nums):
        result = [nums[0]]

        for i in range(1, len(nums)):
            result.append(nums[i] + result[i - 1])

        return result


def run(nums: List[int], cases: list) -> List[int]:
    result = [None]
    solution = NumArray(nums)

    for case in cases:
        result.append(solution.sumRange(case[0], case[1]))

    return result


@pytest.mark.parametrize("nums, cases, expected", NumArray.parameters)
def test_two_sum(nums, cases, expected):
    assert expected == run(nums, cases)
