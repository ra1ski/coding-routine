# https://leetcode.com/problems/maximum-product-of-three-numbers/
import pytest
from typing import List


class Solution:
    params = [
        ([1, 2, 3], 6),
        ([1, 2, 3, 4], 24),
        ([-1, -2, -3], -6),
        ([-100, -98, -1, 2, 3, 4], 39200),
        ([-100, 0, 1, 2, 3, 4], 24),
    ]

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_contains_duplicate(nums: List, expected: bool):
    s = Solution()

    assert expected == s.maximumProduct(nums)
