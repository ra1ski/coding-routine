# https://leetcode.com/problems/search-insert-position/
import pytest
from typing import List


class Solution:
    params = [
        ('hello', 'holle'),
        ('leetcode', 'leotcede'),
    ]

    def reverseVowels(self, s: str) -> str:
        s = list(s)

        l, r = 0, len(s) - 1
        vowels = 'aeiouAEIOU'

        while l < r:
            l_symbol, r_symbol = s[l], s[r]

            if l_symbol not in vowels:
                l += 1

            if r_symbol not in vowels:
                r -= 1

            if l_symbol in vowels and r_symbol in vowels:
                s[l], s[r] = s[r], s[l]

                r -= 1
                l += 1

        return ''.join(s)


@pytest.mark.parametrize('st, expected', Solution.params)
def test_contains_duplicate(st: str, expected: bool):
    s = Solution()

    assert expected == s.reverseVowels(st)
