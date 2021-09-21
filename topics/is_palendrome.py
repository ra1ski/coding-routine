# https://leetcode.com/problems/valid-palindrome

import pytest


class Solution:
    parameters = [
        ('A man, a plan, a canal: Panama', True),
        ('raceacar', False),
        (' ', True),
        ('0P', False),
    ]

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()

        left_i, right_i = 0, len(s) - 1

        while left_i < right_i:
            if s[left_i] != s[right_i]:
                return False

            left_i += 1
            right_i -= 1

        return True


@pytest.mark.parametrize("word, expected", Solution.parameters)
def test_palindrome(word, expected):
    solution = Solution()

    assert expected == solution.isPalindrome(word)


class Solution2:
    parameters = [
        ('racecar', True),
        ('wow', True),
        ('nowd', False),
    ]

    def is_palindrome(self, word: str) -> bool:
        if not word or len(word) <= 0:
            return False

        left_i, right_i = 0, len(word) - 1

        while left_i < right_i:
            if word[left_i] != word[right_i]:
                return False

            left_i += 1
            right_i -= 1

        return True


@pytest.mark.parametrize("word, expected", Solution2.parameters)
def test_palindrome2(word, expected):
    solution = Solution2()

    assert expected == solution.is_palindrome(word)
