# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fib(n+1)

    def fib(self, n: int):
        if n < 2:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

s = Solution()

print(s.climbStairs(3))