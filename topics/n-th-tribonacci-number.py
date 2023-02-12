import pytest


class Solution:
    params = [
        (4, 4),
        (5, 7),
        (25, 1389537)
    ]

    def tribonacci(self, n: int) -> int:
        # 0:0, 1:1, 2:1
        if n < 2:
            return 1 if n else 0

        x, y, z = 0, 1, 1

        for _ in range(n - 2):
            x, y, z = y, z, x + y + z

        return z

    def tribonacci_hash(self, n: int) -> int:
        memo = {
            0: 0,
            1: 1,
            2: 1
        }

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

        return memo[n]

    def tribonacci_memo_recursive(self, n: int) -> int:
        memo = {
            0: 0,
            1: 1,
            2: 1
        }

        def dp(i):
            if i in memo:
                return memo[i]

            if i not in memo:
                memo[i] = dp(i - 1) + dp(i - 2) + dp(i - 3)

            return memo[i]

        return dp(n)




# @pytest.mark.parametrize('n, expected', Solution.params)
# def test_solution(n, expected):
#     s = Solution()
#
#     assert s.tribonacci(n) == expected

# @pytest.mark.parametrize('n, expected', Solution.params)
# def test_solution_hash(n, expected):
#     s = Solution()
#
#     assert s.tribonacci_hash(n) == expected


@pytest.mark.parametrize('n, expected', Solution.params)
def test_solution_memo_recursive(n, expected):
    s = Solution()

    assert s.tribonacci_memo_recursive(n) == expected
