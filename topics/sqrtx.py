from typing import List

import pytest


class Solution:
    params = [
        # (4, 2),
        (16, 4),
        # (25, 5),
    ]

    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot

        return right


@pytest.mark.parametrize('x, expected', Solution.params)
def test_contains_duplicate(x: int, expected: bool):
    s = Solution()

    assert expected == s.mySqrt(x)
