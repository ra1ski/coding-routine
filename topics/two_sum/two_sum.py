import pytest

from typing import List


class Solution(object):
    parameters = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Args:
            nums List[int]:
            target int:
        """
        n = len(nums)
        result = []
        for i in range(n):
            sum = 0
            sum = nums[i] + nums[i - 1]
            if sum == target:
                result.append(i - 1)
                result.append(i)

        return result


@pytest.mark.parametrize("nums, target, expected", Solution.parameters)
def test_two_sum(nums, target, expected):
    solution = Solution()

    assert  solution.two_sum(nums, target) == expected
