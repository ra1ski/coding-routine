from typing import List

import pytest


class Solution:
    params = [
        ([1, 2, 3, 1], 4),
        ([8, 1, 3, 10, 7], 18),
        ([2, 1, 1, 2], 4),
    ]

    def rob(self, nums: List[int]) -> int:
        return self.top_down(nums)

    def bottom_up(self, nums: List[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)

        if len_nums == 1:
            return nums[0]

        if len_nums == 2:
            return max(nums[0], nums[1])

        dp = [0] * len_nums
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])

        for i in range(2, len_nums):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[len_nums - 1]

    def top_down(self, nums: List[int]) -> int:
        def dp(i):
            # base case
            if i == 0:
                return nums[0]

            if i == 1:
                return max(nums[0], nums[1])

            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])

            return memo[i]

        memo = {}
        return dp(len(nums) - 1)


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution(nums, expected):
    s = Solution()

    assert s.rob(nums) == expected
