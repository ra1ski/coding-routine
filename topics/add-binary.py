import pytest


class Solution:
    params = [
        ('11', '1', '100'),
        ('1010', '1011', '10101'),
    ]

    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []

        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2

        if carry == 1:
            answer.append('1')
        answer.reverse()

        return ''.join(answer)

    def addBinary2(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))


@pytest.mark.parametrize('a,b,expected', Solution.params)
def test_solution(a, b, expected):
    s = Solution()

    assert s.addBinary(a, b) == expected
