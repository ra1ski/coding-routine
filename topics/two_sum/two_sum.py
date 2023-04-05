import pytest


class Solution(object):
    parameters = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return []

        hashmap = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[difference], i]

        return []

    def twoSumTwoPassHash(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]

        return []

    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return []

        nums_len = len(nums)

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                difference = target - nums[i]

                if difference == nums[j]:
                    return [i, j]

        return []


@pytest.mark.parametrize("nums, target, expected", Solution.parameters)
def test_two_sum(nums, target, expected):
    solution = Solution()

    assert solution.twoSum(nums, target) == expected


@pytest.mark.parametrize("nums, target, expected", Solution.parameters)
def test_brute_force(nums, target, expected):
    solution = Solution()

    assert solution.twoSumBruteForce(nums, target) == expected


@pytest.mark.parametrize("nums, target, expected", Solution.parameters)
def test_two_pass_hash(nums, target, expected):
    solution = Solution()

    assert solution.twoSumTwoPassHash(nums, target) == expected
