# https://leetcode.com/problems/pascals-triangle/
from typing import List

import pytest


class Solution:
    params = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]])
    ]

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for r in range(numRows):
            row = [None] * (r + 1)
            row[0], row[-1] = 1, 1

            for i in range(1, r):
                row[i] = triangle[r - 1][i - 1] + triangle[r - 1][i]

            triangle.append(row)

        return triangle


@pytest.mark.parametrize('numRows, expected', Solution.params)
def test_solution(numRows, expected):
    s = Solution()

    assert s.generate(numRows) == expected
