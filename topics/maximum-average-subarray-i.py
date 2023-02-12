# https://leetcode.com/problems/maximum-average-subarray-i/
from typing import List

import pytest


class Solution:
    params = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
        ([0, 1, 1, 3, 3], 4, 2.0)
    ]

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        nums_sum = sum(nums[:k])
        avg = nums_sum / k

        for i in range(k, len(nums)):
            nums_sum = nums_sum + nums[i] - nums[i-k]
            avg = max(avg, nums_sum/k)

        return avg

@pytest.mark.parametrize("nums, k, expected", Solution.params)
def test_solution(nums, k, expected):
    s = Solution()

    assert s.findMaxAverage(nums, k) == expected
