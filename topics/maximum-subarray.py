# https://leetcode.com/problems/maximum-subarray/description/
from typing import List

import pytest


class Solution:
    params = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([5,4,-9,7,8], 15)
    ]
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        total_sum = nums[0]

        for i in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += i

            total_sum = max(current_sum, total_sum)

        return total_sum

    def maxSubArray_dynamic(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
            print(i, nums[i])
        return max(nums)



@pytest.mark.parametrize("nums, expected", Solution.params)
def test_solution(nums, expected):
    s = Solution()

    assert s.maxSubArray(nums) == expected

@pytest.mark.parametrize("nums, expected", Solution.params)
def test_solution_dynamic(nums, expected):
    s = Solution()

    assert s.maxSubArray_dynamic(nums) == expected