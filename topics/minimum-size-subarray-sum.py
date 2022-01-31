from typing import List

import pytest


class Solution:
    params = [
        ([2, 3, 1, 2, 4, 3], 7, 2),
        ([1,4,4], 4, 1),
        ([1,1,1,1,1,1,1,1], 11, 0),
    ]

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums_len = len(nums)
        ans = nums_len + 1
        nums_sum, left = 0, 0

        for right in range(nums_len):
            nums_sum += nums[right]

            while nums_sum >= target:
                ans = min(ans, right - left + 1)
                nums_sum -= nums[left]

                left += 1

        return ans if ans != nums_len + 1 else 0



@pytest.mark.parametrize('nums, target, expected', Solution.params)
def test_solution(nums, target, expected):
    s = Solution()

    assert s.minSubArrayLen(target, nums) == expected
