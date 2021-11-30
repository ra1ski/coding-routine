# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq

import pytest
from typing import List


class Solution:
    params = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        n_largest = heapq.nlargest(k, nums)
        return n_largest[-1]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        h = []

        for i in nums:
            heapq.heappush(h, i)

            if len(h) > k:
                heapq.heappop(h)

        return heapq.heappop(h)


@pytest.mark.parametrize('nums, k, expected', Solution.params)
def test_findKthLargest(nums: List, k: int, expected: bool):
    s = Solution()

    assert expected == s.findKthLargest(nums, k)


@pytest.mark.parametrize('nums, k, expected', Solution.params)
def test_findKthLargest2(nums: List, k: int, expected: bool):
    s = Solution()

    assert expected == s.findKthLargest2(nums, k)


@pytest.mark.parametrize('nums, k, expected', Solution.params)
def test_findKthLargest3(nums: List, k: int, expected: bool):
    s = Solution()

    assert expected == s.findKthLargest3(nums, k)
