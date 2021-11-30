# https://leetcode.com/problems/search-insert-position/
import pytest
from typing import List


class Solution:
    params = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 7, 4),
        ([1,3,5,6], 2, 1),
    ]

    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return left


@pytest.mark.parametrize('nums, target, expected', Solution.params)
def test_contains_duplicate(nums: List, target: int, expected: bool):
    s = Solution()

    assert expected == s.searchInsert(nums, target)
