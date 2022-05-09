# https://leetcode.com/problems/height-checker/
from typing import List

import pytest


class Solution:
    params = [
        ([1, 1, 4, 2, 1, 3], 3),
        ([5, 1, 2, 3, 4], 5),
        ([1, 2, 3, 4, 5], 0)
    ]

    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        total = 0

        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                total += 1

        return total


@pytest.mark.parametrize('heights, expected', Solution.params)
def test_contains_duplicate(heights, expected):
    s = Solution()

    assert s.heightChecker(heights) == expected
