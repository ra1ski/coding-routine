# https://leetcode.com/problems/remove-element/
import pytest
from typing import List


class Solution:
    params = [
        ([3,2,2,3], 3, 2), # [2,2,'_','_']
        ([0,1,2,2,3,0,4,2], 2, 5), # [0,1,3,0,4,'_','_','_']
    ]

    def removeElement(self, nums: List[int], val: int) -> int:
        # pointer = 0
        #
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[pointer] = nums[i]
        #         pointer += 1
        # return pointer

        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                # reduce array size by one
                n -=1
            else:
                i +=1
        return n



@pytest.mark.parametrize('nums, k, expected', Solution.params)
def test_solution(nums: list, k:int, expected: bool):
    s = Solution()

    assert s.removeElement(nums, k) == expected
