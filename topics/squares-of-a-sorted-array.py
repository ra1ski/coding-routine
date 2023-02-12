# https://leetcode.com/problems/squares-of-a-sorted-array/

import pytest
from typing import List


class Solution:
    params = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100])
    ]

    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        pointer = len(nums) - 1
        result = [0] * len(nums)

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                square = nums[l]
                l += 1
            else:
                square = nums[r]
                r -= 1

            result[pointer] = square * square

            pointer -= 1

        return result

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        return sorted([n * n for n in nums])

    def sortedSquares3(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        result = [0] * nums_len
        left, right = 0, nums_len - 1

        for n in range(nums_len - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1

            result[n] = square * square

        return result


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution(nums: list, expected: bool):
    s = Solution()

    assert s.sortedSquares(nums) == expected


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution2(nums: list, expected: bool):
    s = Solution()

    assert s.sortedSquares2(nums) == expected


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution3(nums: list, expected: bool):
    s = Solution()

    assert s.sortedSquares3(nums) == expected
