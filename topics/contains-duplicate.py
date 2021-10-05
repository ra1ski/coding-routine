# https://leetcode.com/problems/contains-duplicate
from collections import Counter

import pytest
from typing import List


class Solution:
    parameters = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        i = 0

        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                return True

            i += 1

        return False

    def containsDuplicate3(self, nums: List[int]) -> bool:
        c = Counter(nums)

        return len(nums) != len(c.keys())


@pytest.mark.parametrize('nums, expected', Solution.parameters)
def test_contains_duplicate(nums: List, expected: bool):
    s = Solution()

    assert expected == s.containsDuplicate(nums)


@pytest.mark.parametrize('nums, expected', Solution.parameters)
def test_contains_duplicate2(nums: List, expected: bool):
    s = Solution()

    assert expected == s.containsDuplicate2(nums)


@pytest.mark.parametrize('nums, expected', Solution.parameters)
def test_contains_duplicate3(nums: List, expected: bool):
    s = Solution()

    assert expected == s.containsDuplicate3(nums)
