import pytest
from typing import List


class Solution:
    params = [
        ([-1, 0, 3, 5, 9, 12], 9, 4)
    ]

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle

            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1


@pytest.mark.parametrize('nums, target, expected', Solution.params)
def test_contains_duplicate(nums: List, target: int, expected: bool):
    s = Solution()

    assert expected == s.search(nums, target)
