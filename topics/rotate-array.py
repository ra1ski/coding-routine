# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
import pytest
from typing import List
from collections import deque


class Solution:
    params = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2], 5, [2, 1]),
    ]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_nums = len(nums)
        temp_nums = [0] * n_nums

        for i in range(n_nums):
            index = (i + k) % n_nums

            temp_nums[index] = nums[i]

        nums[:] = temp_nums

        """
            [5, 6, 7, 1, 2, 3, 4]
            >>> (1+3) % 7
            4
            >>> (0+3) % 7
            3
            >>> (2+3) % 7
            5
            >>> (3+3) % 7
            6
            >>> (4+3) % 7
            0
            >>> (5+3) % 7
            1
            >>> (6+3) % 7
            2
            >>> (7+3) % 7
            3
            >>> 
        """

        return nums

    # def rotate2(self, nums: List[int], k: int) -> None:
    #     # Fixes possible wrap around
    #     k %= len(nums)
    #     # Shuffles List
    #     nums[:] = nums[-k:] + nums[:-k]
    #
    #     return nums
    #
    # def rotate3(self, nums: List[int], k: int) -> None:
    #     # Fixes possible wrap around
    #     k %= len(nums)
    #
    #     for i in range(k):
    #         previous = nums[-1]
    #         for j in range(len(nums)):
    #             nums[j], previous = previous, nums[j]
    #
    #     return nums

    # def rotate4(self, nums: List[int], k: int) -> None:
    #     """
    #     Reverse 3 times
    #     """
    #     n = len(nums)
    #     k %= n
    #
    #     def reverse(nums, start: int, end: int):
    #         while start < end:
    #             nums[start], nums[end] = nums[end], nums[start]
    #             start += 1
    #             end -= 1
    #
    #     reverse(nums, 0, n - 1)
    #     reverse(nums, 0, k - 1)
    #     reverse(nums, k, n - 1)
    #
    #     return nums

@pytest.mark.parametrize('nums, k, expected', Solution.params)
def test_contains_duplicate(nums: list, k: int, expected: bool):
    s = Solution()

    assert s.rotate(nums, k) == expected


# @pytest.mark.parametrize('nums, k, expected', Solution.params)
# def test_contains_duplicate2(nums: list, k: int, expected: bool):
#     s = Solution()
#
#     assert s.rotate2(nums, k) == expected
#
# @pytest.mark.parametrize('nums, k, expected', Solution.params)
# def test_contains_duplicate3(nums: list, k: int, expected: bool):
#     s = Solution()
#
#     assert s.rotate3(nums, k) == expected

# @pytest.mark.parametrize('nums, k, expected', Solution.params)
# def test_contains_duplicate4(nums: list, k: int, expected: bool):
#     s = Solution()
#
#     assert s.rotate4(nums, k) == expected