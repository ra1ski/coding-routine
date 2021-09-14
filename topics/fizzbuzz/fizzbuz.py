# https://leetcode.com/problems/fizz-buzz/
# Solution 1
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                result.append('FizzBuzz')
            else:
                if divisible_by_3:
                    result.append('Fizz')
                elif divisible_by_5:
                    result.append('Buzz')
                else:
                    result.append(str(i))

        return result


# Solution 2


class Solution2:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        if n < 1:
            return result

        common_divider = 15

        for i in range(1, n + 1):
            if i % common_devider == 0:
                result.append('FizzBuzz')
            else:
                if i % 3 == 0:
                    result.append('Fizz')
                elif i % 5 == 0:
                    result.append('Buzz')
                else:
                    result.append(str(i))

        return result
