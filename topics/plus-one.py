from typing import List

import pytest


class Solution:
    params = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
        ([1, 2, 9], [1, 3, 0]),
    ]

    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0: return digits
        if len(digits) == 1 and digits[0] == 9: return [1, 0]
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        return digits


@pytest.mark.parametrize('digits, expected', Solution.params)
def test_solution(digits, expected):
    s = Solution()

    assert s.plusOne(digits) == expected
