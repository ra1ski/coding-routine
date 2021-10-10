import pytest


class Solution:
    parameters = [
        (['h', 'e', 'l', 'l', 'o'], ['o', 'l', 'l', 'e', 'h']),
        (['H', 'a', 'n', 'n', 'a', 'h'], ['h', 'a', 'n', 'n', 'a', 'H']),
    ]

    def reverseString(self, s: list) -> list:
        if not s or not isinstance(s, list):
            return []

        left_i, right_i = 0, len(s) - 1

        while left_i < right_i:
            s[left_i], s[right_i] = s[right_i], s[left_i]

            left_i += 1
            right_i -= 1

        return s


@pytest.mark.parametrize('input_list, expected', Solution.parameters)
def test_palindrome(input_list, expected):
    solution = Solution()

    assert expected == solution.reverseString(input_list)
