# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List

import pytest


class Solution:
    params = [
        ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
        ([400], [-1]),
    ]

    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        if len(arr) == 1:
            return [-1]

        max_value = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            current = arr[i]
            arr[i] = max_value

            if current > max_value:
                max_value = current

        arr[-1] = -1

        return arr


@pytest.mark.parametrize('arr, expected', Solution.params)
def test_contains_duplicate(arr: List, expected: List):
    s = Solution()

    assert expected == s.replaceElements(arr)
