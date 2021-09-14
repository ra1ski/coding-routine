import pytest


class Solution:
    parameters = [
        (['h', 'e', 'l', 'l', 'o'], ['o', 'l', 'l', 'e', 'h']),
        (['H', 'a', 'n', 'n', 'a', 'h'], ['h', 'a', 'n', 'n', 'a', 'H']),
    ]

    def reverseString(self, input_list: list) -> list:
        if not input_list or not isinstance(input_list, list):
            return []

        result = []
        right_i = len(input_list) - 1

        while right_i >= 0:
            result.append(input_list[right_i])
            right_i -= 1

        return result


@pytest.mark.parametrize('input_list, expected', Solution.parameters)
def test_palindrome(input_list, expected):
    solution = Solution()

    assert expected == solution.reverseString(input_list)
