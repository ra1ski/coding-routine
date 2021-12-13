# https://leetcode.com/problems/move-zeroes/
import pytest
from typing import List


class Solution:
    params = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
    ]

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        arr_len = len(nums)

        for i in nums:
            if i != 0:
                nums[pointer] = i
                pointer += 1

        for i in range(pointer, arr_len):
            nums[i] = 0

        return nums


        # pointer = 0
        #
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[pointer] = nums[i]
        #         pointer += 1
        #
        # while pointer < len(nums):
        #     nums[pointer] = 0
        #     pointer += 1
        #
        # return nums


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution(nums: list, expected: bool):
    s = Solution()

    assert expected == s.moveZeroes(nums)
