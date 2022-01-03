# https://leetcode.com/problems/diagonal-traverse/
from collections import defaultdict
from typing import List
import pytest


class Solution:
    params = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9])
    ]

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        lines = defaultdict(list)
        len_cols, len_rows = len(mat), len(mat[0])

        for i in range(len_cols):
            for j in range(len_rows):
                lines[i + j].append(mat[i][j])

        for k in range(len_cols + len_rows - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]

        return res

    def findDiagonalOrder0(self, mat: List[List[int]]) -> List[int]:
        res = []
        lines = defaultdict(list)
        len_cols, len_rows = len(mat), len(mat[0])

        for i in range(len_cols):
            for j in range(len_rows):
                lines[i + j].append(mat[i][j])

        for i in range(len(lines)):
            if i % 2 == 0:
                lines[i] = lines[i][::-1]

        result = [n for line in lines for n in lines[line]]

        return result

    def findDiagonalOrder2(self, matrix: List[List[int]]) -> List[int]:

        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []

        # Variables to track the size of the matrix
        N, M = len(matrix), len(matrix[0])

        # The two arrays as explained in the algorithm
        result, intermediate = [], []
        m_len = N + M - 1

        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals
        for d in range(m_len):

            # Clear the intermediate array everytime we start
            # to process another diagonal
            intermediate.clear()

            # We need to figure out the "head" of this diagonal
            # The elements in the first row and the last column
            # are the respective heads.
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1

            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1

            # Reverse even numbered diagonals. The
            # article says we have to reverse odd
            # numbered articles but here, the numbering
            # is starting from 0 :P
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result


@pytest.mark.parametrize('mat, expected', Solution.params)
def test_solution(mat, expected):
    s = Solution()

    assert s.findDiagonalOrder(mat) == expected
