# https://leetcode.com/problems/group-anagrams/
from collections import Counter

import pytest
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_hash = {}

        for s in strs:
            joined_set = ''.join(sorted(s))

            if joined_set not in str_hash:
                str_hash[joined_set] = [s]
            else:
                str_hash[joined_set].append(s)

        return list(str_hash.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))