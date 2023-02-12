import pytest
from typing import List


class Solution:
    params = [
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([4, 5, 6, 7, 8, 1, 2, 3], 4)
    ]

    def fined_rotate_index(self, nums: list):
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            ...

    # def search(self, nums: List[int], target: int) -> int:
    #     if not nums:
    #         return -1
    #
    #     left, right = 0, len(nums) - 1
    #
    #     while left <= right:
    #         middle = (left + right) // 2
    #
    #         if nums[middle] == target:
    #             return middle
    #
    #         if nums[middle] > target:
    #             right = middle - 1
    #         else:
    #             left = middle + 1
    #
    #     return -1


# @pytest.mark.parametrize('nums, target, expected', Solution.params)
# def test_contains_duplicate(nums: List, target: int, expected: bool):
#     s = Solution()
#
#     assert expected == s.search(nums, target)

@pytest.mark.parametrize('nums, expected', Solution.params)
def test_contains_duplicate(nums: List, expected: bool):
    s = Solution()

    assert s.fined_rotate_index(nums) == expected
