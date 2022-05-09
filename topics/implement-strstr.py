import pytest


class Solution:
    params = [
        ('hello', 'll', 2)
    ]

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        l_needle = len(needle)

        for i in range(len(haystack) - l_needle):
            if haystack[i:l_needle+i] == needle:
                return i

        return -1

@pytest.mark.parametrize('haystack, needle, expected', Solution.params)
def test_solution(haystack, needle, expected):
    s = Solution()

    assert s.strStr(haystack, needle) == expected