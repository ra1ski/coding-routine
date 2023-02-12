# https://leetcode.com/problems/longest-substring-without-repeating-characters/
import pytest


class Solution:
    params = [
        ('abcabcbb', 3)
    ]

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     cset = set()
    #     left = 0
    #     res = 0
    #     for right in range(len(s)):
    #         while s[right] in cset:
    #             cset.remove(s[left])
    #             left += 1
    #
    #         cset.add(s[right])
    #
    #         res = max(res, right - left + 1)
    #
    #     return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans



@pytest.mark.parametrize("st, expected", Solution.params)
def test_solution(st, expected):
    s = Solution()

    assert s.lengthOfLongestSubstring(st) == expected
