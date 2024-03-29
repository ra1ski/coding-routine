from typing import List

import pytest


class Solution:
    params = [
        # ([1, 0, 1, 1, 0], 4),
        # ([1, 0, 1, 1, 0, 1], 4),
        ([1, 0, 0, 1, 1, 0, 1], 4),
    ]

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_sequence = 0
        left, right = 0, 0
        num_zeroes = 0

        while right < len(nums):  # while our window is in bounds
            if nums[right] == 0:  # add the right most element into our window
                num_zeroes += 1

            while num_zeroes == 2:  # if our window is invalid, contract our window
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1

            longest_sequence = max(longest_sequence, right - left + 1)  # update our longest sequence answer
            right += 1  # expand our window

        return longest_sequence


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_contains_duplicate(nums, expected):
    s = Solution()

    assert s.findMaxConsecutiveOnes(nums) == expected
