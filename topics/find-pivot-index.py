# https://leetcode.com/problems/find-pivot-index/
from typing import List

import pytest


class Solution:
    params = [
        ([1, 7, 3, 6, 5, 6], 3),
        # ([1, 2, 3], -1),
        # ([2, 1, -1], 0),
    ]

    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0

        for i, x in enumerate(nums):
            rightsum = (S - leftsum - x)
            if leftsum == rightsum:
                return i
            leftsum += x

        return -1


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_contains_duplicate(nums, expected):
    s = Solution()

    assert s.pivotIndex(nums) == expected
