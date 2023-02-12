# https://leetcode.com/problems/permutation-in-string/
from collections import Counter

import pytest


class Solution:
    params = [
        ('ab', 'eidbaooo', True),
        ('hello', 'ooolleoooleh', False)
    ]

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = Counter(s1)
        len_s1 = len(s1_set)

        if not s2:
            return False

        for i in range(len(s2)):
            next_item = s2[i:len_s1 + i]

            if s1_set == Counter(next_item):
                return True

        return False


@pytest.mark.parametrize("s1, s2, expected", Solution.params)
def test_solution(s1, s2, expected):
    s = Solution()

    assert s.checkInclusion(s1, s2) == expected
