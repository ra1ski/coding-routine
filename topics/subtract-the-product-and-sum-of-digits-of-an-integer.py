import pytest


class Solution:
    parameters = [
        (234, 15),
        (4421, 21),
    ]

    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        n_product, n_sum = 1, 0

        for i in s:
            i = int(i)
            n_product *= i
            n_sum += i

        return n_product - n_sum


import math


class Solution2:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        return math.prod(digits) - sum(digits)


class Solution3:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        n_product, n_sum = 1, 0

        for i in s:
            i = int(i)
            n_product *= i
            n_sum += i

        return n_product - n_sum


@pytest.mark.parametrize('number, expected', Solution.parameters)
def test_palindrome(number, expected):
    solution = Solution()

    assert expected == solution.subtractProductAndSum(number)


@pytest.mark.parametrize('number, expected', Solution.parameters)
def test_palindrome2(number, expected):
    solution = Solution2()

    assert expected == solution.subtractProductAndSum(number)


@pytest.mark.parametrize('number, expected', Solution.parameters)
def test_palindrome3(number, expected):
    solution = Solution3()

    assert expected == solution.subtractProductAndSum(number)
