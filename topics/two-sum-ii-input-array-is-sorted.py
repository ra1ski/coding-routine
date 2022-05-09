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
        if not numbers:
            return []

        left, right = 0, len(numbers) - 1

        while left <= right:
            target_sum = numbers[left] + numbers[right]

            if target_sum == target:
                return [left + 1, right + 1]
            else:
                if target_sum > target:
                    right -= 1
                else:
                    left += 1


@pytest.mark.parametrize('numbers, target, expected', Solution.params)
def test_contains_duplicate(numbers: list, target: int, expected: bool):
    s = Solution()

    assert expected == s.twoSum(numbers, target)
