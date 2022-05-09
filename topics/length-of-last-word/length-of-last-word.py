# https://leetcode.com/problems/length-of-last-word/
# Solution 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(' ')

        if len(words) == 0:
            return 0

        return len(words.pop())


# Solution 2
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        element = s.strip().split(' ').pop()

        return len(element)
