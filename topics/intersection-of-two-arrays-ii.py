# https://leetcode.com/problems/intersection-of-two-arrays-ii/
import pytest
from typing import List


class Solution:
    params = [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9])
    ]

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:



@pytest.mark.parametrize('nums1, nums2, expected', Solution.params)
def test_solution(nums1: list, nums2: list, expected: bool):
    s = Solution()

    assert s.intersect(nums1, nums2) == expected
