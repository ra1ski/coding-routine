from typing import List

import pytest


class Solution:
    params = [
        # ([3, 6, 1, 0], 1),
        # ([1, 2, 3, 4], -1),
        # ([1], 0),
        ([0,0,3,2], -1),
    ]

    def dominantIndex(self, nums: List[int]) -> int:
        n_max, i_max = 0, - 1

        for i, x in enumerate(nums):
            if x > n_max:
                n_max, i_max = x, i

        for i, x in enumerate(nums):
            if x != n_max and n_max < x * 2:
                return -1

        return i_max

    def dominantIndex2(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1

        n_max, n_max_second, n_index = 0, 0, -1

        for i, n in enumerate(nums):
            if n > n_max:
                n_max_second = n_max
                n_max = n
                n_index = i
            elif n > n_max_second: n_max_second = n

        if n_max < n_max_second*2:
            n_index = -1

        return n_index

#
# @pytest.mark.parametrize('nums, expected', Solution.params)
# def test_solution(nums, expected):
#     s = Solution()
#
#     assert s.dominantIndex(nums) == expected

@pytest.mark.parametrize('nums, expected', Solution.params)
def test_solution2(nums, expected):
    s = Solution()

    assert s.dominantIndex2(nums) == expected