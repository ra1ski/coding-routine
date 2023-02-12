# https://leetcode.com/problems/guess-number-higher-or-lower/
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        left, right = 1, n

        while left <= right:
            middle = (left + right) // 2

            result = guess(middle)

            if result == 0:
                return middle

            if result == -1:
                right = middle - 1
            else:
                left = middle + 1

        return -1