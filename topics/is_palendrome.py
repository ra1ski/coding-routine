import pytest


class Solution:
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


@pytest.mark.parametrize("word, expected", Solution.parameters)
def test_palindrome(word, expected):
    solution = Solution()

    assert expected == solution.is_palindrome(word)
