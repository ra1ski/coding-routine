# https://leetcode.com/problems/kth-largest-element-in-an-array/
import pytest
from typing import List


class Solution:
    params = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


@pytest.mark.parametrize('nums, k, expected', Solution.params)
def test_findKthLargest(nums: List, k: int, expected: bool):
    s = Solution()

    assert expected == s.findKthLargest(nums, k)
