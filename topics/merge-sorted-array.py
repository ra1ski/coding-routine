# https://leetcode.com/problems/merge-sorted-array/

from typing import List

import pytest


class Solution:
    params = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
    ]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        p1 = p2 = 0

        for p in range(len(nums1)):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

        return nums1

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(len(nums1)-1, -1, -1):
            if p2 < 0 or p1 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

        return nums1


# @pytest.mark.parametrize("nums1, m, nums2, n, expected", Solution.params)
# def test_solution(nums1, m, nums2, n, expected):
#     s = Solution()
#
#     assert expected == s.merge(nums1, m, nums2, n)


@pytest.mark.parametrize("nums1, m, nums2, n, expected", Solution.params)
def test_solution2(nums1, m, nums2, n, expected):
    s = Solution()

    assert expected == s.merge2(nums1, m, nums2, n)
