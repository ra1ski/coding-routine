# https://leetcode.com/problems/remove-element/
import pytest
from typing import List


class Solution:
    params = [
        ([2, 1], False),
        ([3, 5, 5], False),
        ([0, 3, 2, 1], True),
        ([0, 2, 3, 4, 5, 2, 1, 0], True),
        ([0, 2, 3, 3, 5, 2, 1, 0], False),
    ]

    def validMountainArray(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        n = 0

        for i in range(arr_len - 1):
            if arr[i] < arr[i + 1]:
                n += 1
            else:
                break

        if n == 0 or n == arr_len - 1:
            return False

        for i in range(n, arr_len - 1):
            if arr[i] > arr[i + 1]:
                n += 1

        return n == arr_len - 1

    def validMountainArray2(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        n = 0

        while n < arr_len - 1:
            if arr[n] < arr[n + 1]:
                n += 1
            else:
                break

        if n == 0 or n == arr_len - 1:
            return False

        while n < arr_len - 1:
            if arr[n] > arr[n + 1]:
                n += 1
            else:
                break

        return n == arr_len - 1

    def validMountainArray3(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0

        # walk up
        while i + 1 < N and arr[i] < arr[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False

        # walk down
        while i + 1 < N and arr[i] > arr[i + 1]:
            i += 1

        return i == N - 1


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution(nums: list, expected: bool):
    s = Solution()

    assert s.validMountainArray(nums) == expected


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution2(nums: list, expected: bool):
    s = Solution()

    assert s.validMountainArray2(nums) == expected


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution3(nums: list, expected: bool):
    s = Solution()

    assert s.validMountainArray3(nums) == expected
