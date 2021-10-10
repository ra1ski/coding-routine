# https://leetcode.com/problems/reverse-words-in-a-string-iii/
import pytest

class Solution:
    params = [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("God Ding", "doG gniD"),
    ]

    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        result = []

        for word in s_list:
            result.append(self.reverse_word(word))

        return ' '.join(result)

    def reverse_word(self, word: str) -> str:
        word = list(word)
        l, r = 0, len(word) - 1

        while l < r:
            word[l], word[r] = word[r], word[l]

            l += 1
            r -= 1

        return ''.join(word)


@pytest.mark.parametrize('words, expected', Solution.params)
def test_solution(words: str, expected: bool):
    s = Solution()

    assert expected == s.reverseWords(words)
