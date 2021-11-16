# https://leetcode.com/problems/duplicate-zeros/
import pytest

from typing import List


class Solution:
    params = [
        ([8, 4, 5, 0, 0, 0, 0, 7], [8, 4, 5, 0, 0, 0, 0, 0]),
        ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 1, 7, 6, 0, 2, 0, 7], [0, 0, 1, 7, 6, 0, 0, 2]),
    ]

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n_duplicates = 0
        n_arr = len(arr) - 1

        for i in range(len(arr)):
            if i > n_arr - n_duplicates:
                break

            if arr[i] == 0:
                if i == n_arr - n_duplicates:
                    arr[-1] = 0
                    n_arr -= 1

                    break

                n_duplicates += 1

        last = n_arr - n_duplicates

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + n_duplicates] = 0
                n_duplicates -= 1
                arr[i + n_duplicates] = 0
            else:
                arr[i + n_duplicates] = arr[i]

        return arr


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution(nums: list, expected: bool):
    s = Solution()

    assert s.duplicateZeros(nums) == expected
