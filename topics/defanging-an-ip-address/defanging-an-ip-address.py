import pytest


class Solution(object):
    parameters = [
        ('1.1.1.1', '1[.]1[.]1[.]1'),
        ('255.100.50.0', '255[.]100[.]50[.]0'),
    ]

    def defang_ip_addr(self, address: str) -> str:
        """
        :type address: str
        :rtype: str
        """

        return address.replace('.', '[.]')

    def defang_ip_addr_two(self, address):
        """
        :type address: str
        :rtype: str
        """

        a_list = address.split('.')
        return '[.]'.join(a_list)


@pytest.mark.parametrize("nums, expected", Solution.parameters)
def test_highest(nums, expected):
    solution = Solution()

    assert expected == solution.defang_ip_addr(nums)
