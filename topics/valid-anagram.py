import collections

import pytest


class Solution:
    parameters = [
        ('anagram', 'nagaram', True),
        ('rat', 'car', False),
    ]

    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        return s == t

    def isAnagram2(self, s: str, t: str) -> bool:
        s = list(map(lambda ch: ord(ch), s))
        t = list(map(lambda ch: ord(ch), t))

        return sorted(s) == sorted(t)

    def isAnagram3(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


@pytest.mark.parametrize('word1, word2, expected', Solution.parameters)
def test_is_anagram(word1: str, word2: str, expected: bool):
    solution = Solution()

    assert expected == solution.isAnagram(word1, word2)


@pytest.mark.parametrize('word1, word2, expected', Solution.parameters)
def test_is_anagram2(word1: str, word2: str, expected: bool):
    solution = Solution()

    assert expected == solution.isAnagram2(word1, word2)


@pytest.mark.parametrize('word1, word2, expected', Solution.parameters)
def test_is_anagram3(word1: str, word2: str, expected: bool):
    solution = Solution()

    assert expected == solution.isAnagram3(word1, word2)
