import pytest


class Solution:
    params = [
        (4, 4),
        (5, 7),
        (25, 1389537)
    ]
    memo = {0: 0, 1: 1, 2: 1}

    def dp_bottom_up(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1

        for i in range(3, n + 1):
            self.memo[i] = self.memo[i - 1] + self.memo[i - 2] + self.memo[i - 3]

        return self.memo[n]

    def top_down(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.memo[n - 1] + self.memo[n - 2] + self.memo[n - 3]

        return self.memo[n]

    def recursion(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1

        return self.recursion(n - 1) + self.recursion(n - 2) + self.recursion(n - 3)


@pytest.mark.parametrize('n, expected', Solution.params)
def test_bottom_up(n, expected):
    s = Solution()

    assert s.dp_bottom_up(n) == expected


@pytest.mark.parametrize('n, expected', Solution.params)
def test_top_down(n, expected):
    s = Solution()

    assert s.top_down(n) == expected


@pytest.mark.parametrize('n, expected', Solution.params)
def test_recursion(n, expected):
    s = Solution()

    assert s.recursion(n) == expected
