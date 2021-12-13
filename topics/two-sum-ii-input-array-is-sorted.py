# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
import pytest
from typing import List


class Solution:
    params = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([2, 7, 11, 15], 22, [2, 4]),
    ]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            n_sum = numbers[l] + numbers[r]
            if n_sum == target:
                return [l + 1, r + 1]

            if n_sum < target:
                l += 1
            else:
                r -= 1


@pytest.mark.parametrize('numbers, target, expected', Solution.params)
def test_contains_duplicate(numbers: list, target: int, expected: bool):
    s = Solution()

    assert expected == s.twoSum(numbers, target)
