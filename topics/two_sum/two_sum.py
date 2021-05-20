import pytest

from typing import List


class Solution(object):
    parameters = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]

    @staticmethod
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Args:
            nums List[int]:
            target int:
        """
        nums_hash = {}
        result = [0, 0]

        for i, num in enumerate(nums):
            subtraction = target - num

            if subtraction not in nums_hash:
                nums_hash[num] = i
            else:
                result = [nums_hash[subtraction], i]

        return result


@pytest.mark.parametrize("nums, target, expected", Solution.parameters)
def test_two_sum(nums, target, expected):
    solution = Solution()

    assert expected == solution.two_sum(nums, target)
