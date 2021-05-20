import pytest

from typing import List


class Solution(object):
    parameters_highest = [
        ([1, 2, 3, 4, 5], 5),
        ([9, 8, 7, 6, 5], 9),
    ]

    parameters_lowest = [
        ([1, 2, 3, 4, 5], 1),
        ([9, 8, 7, 6, 5], 5),
    ]

    def highest(self, nums: List[int]) -> int:
        """
        Args:
            nums List[int]:
        """
        if len(nums) == 0:
            raise Exception('Provide a valid list')

        highest = nums[0]

        for i, num in enumerate(nums):
            if num > highest:
                highest = num

        return highest

    def lowest(self, nums: List[int]) -> int:
        """
        Args:
            nums List[int]:
        """
        if len(nums) == 0:
            raise Exception('Provide a valid list')

        lowest = nums[0]

        for i, num in enumerate(nums):
            if num < lowest:
                lowest = num

        return lowest


@pytest.mark.parametrize("nums, expected", Solution.parameters_highest)
def test_highest(nums, expected):
    solution = Solution()

    assert expected == solution.highest(nums)


@pytest.mark.parametrize("nums, expected", Solution.parameters_lowest)
def test_lowest(nums, expected):
    solution = Solution()

    assert expected == solution.lowest(nums)
