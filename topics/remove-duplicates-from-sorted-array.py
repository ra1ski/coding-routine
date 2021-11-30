# https://leetcode.com/problems/remove-element/
import pytest
from typing import List


class Solution:
    params = [
        ([1,1,2], 2),
        ([0,0,1,1,1,2,2,3,3,4], 5)
    ]

    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0

        for i in range(1, len(nums)):
            if nums[pointer] != nums[i]:
                pointer += 1
                nums[pointer] = nums[i]

        return pointer + 1


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution(nums: list, expected: bool):
    s = Solution()

    assert s.removeDuplicates(nums) == expected
