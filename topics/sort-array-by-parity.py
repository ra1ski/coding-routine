from typing import List

import pytest


class Solution:
    params = [
        ([3, 1, 2, 4], [2, 4, 3, 1]),
        ([0], [0])
    ]

    def replace-elements-with-greatest-element-on-right-side(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x % 2)
        # nums = [i for i in nums if i % 2 == 0] + [i for i in nums if i % 2 == 1]

        return nums

    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        nums = [i for i in nums if i % 2 == 0] + [i for i in nums if i % 2 == 1]

        return nums


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_contains_duplicate(nums, expected):
    s = Solution()

    assert expected == s.sortArrayByParity(nums)


@pytest.mark.parametrize('nums, expected', Solution.params)
def test_contains_duplicate2(nums, expected):
    s = Solution()

    assert expected == s.sortArrayByParity2(nums)
