# https://leetcode.com/problems/first-bad-version/

import pytest
from typing import List


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """


@pytest.mark.parametrize('nums, target, expected', Solution.params)
def test_contains_duplicate(nums: List, target: int, expected: bool):
    s = Solution()

    assert expected == s.search(nums, target)
