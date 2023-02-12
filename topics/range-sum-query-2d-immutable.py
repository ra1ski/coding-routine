from itertools import accumulate
from typing import List

import pytest

matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]


class NumMatrix:
    params = [
        (matrix, [2, 1, 4, 3], 8),
        (matrix, [1, 1, 2, 2], 11),
        (matrix, [1, 2, 2, 4], 12),
    ]

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None

        self.dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.dp[row][col + 1] = matrix[row][col] + self.dp[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for row in range(row1, row2 + 1):
            total += self.dp[row][col2 + 1] - self.dp[row][col1]

        return total


@pytest.mark.parametrize("matrix, polygon, expected", NumMatrix.params)
def test_solution(matrix, polygon, expected):
    s = NumMatrix(matrix)
    result = s.sumRegion(polygon[0], polygon[1], polygon[2], polygon[3])

    assert result == expected


class NumMatrixDynamic:
    params = [
        (matrix, [2, 1, 4, 3], 8),
        (matrix, [1, 1, 2, 2], 11),
        (matrix, [1, 2, 2, 4], 12),
    ]

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None

        self.dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r][c + 1] + matrix[r][c] - self.dp[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - (self.dp[row1][col2 + 1] + self.dp[row2 + 1][col1] - self.dp[row1][col1])


@pytest.mark.parametrize("matrix, polygon, expected", NumMatrix.params)
def test_solution_dynamic(matrix, polygon, expected):
    s = NumMatrixDynamic(matrix)
    result = s.sumRegion(polygon[0], polygon[1], polygon[2], polygon[3])

    assert result == expected
