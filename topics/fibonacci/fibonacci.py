import pytest


class Solution:
    params = [
        (2, 1),  # 0, 1, 1
        (3, 2),  # 0, 1, 1, 2
        (4, 3),  # 0, 1, 1, 2, 3
        (5, 5),  # 0, 1, 1, 2, 3, 5
        (6, 8),  # 0, 1, 1, 2, 3, 6, 8
    ]
    cache = {0: 0, 1: 1}

    def fib_recursion(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib_recursion(n - 1) + self.fib_recursion(n - 2)

    def dp_bottom_up(self, n: int) -> int:
        if n <= 1:
            return n

        cache = [0] * (n + 1)
        cache[1] = 1

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]

    def dp_top_down(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self.dp_top_down(n - 1) + self.dp_top_down(n - 2)

        return self.cache[n]


@pytest.mark.parametrize("n, expected", Solution.params)
def test_recursion(n: int, expected: int):
    s = Solution()
    result = s.fib_recursion(n)

    assert result == expected


@pytest.mark.parametrize("n, expected", Solution.params)
def test_dp_bottom_up(n: int, expected: int):
    s = Solution()

    result = s.dp_bottom_up(n)

    assert result == expected


@pytest.mark.parametrize("n, expected", Solution.params)
def test_dp_top_down(n: int, expected: int):
    s = Solution()

    result = s.dp_top_down(n)

    assert result == expected
