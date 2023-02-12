# https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split()])

#     def reverseWords(self, s: str) -> str:
#         s_list = s.split(' ')
#         result = []

#         for word in s_list:
#             result.append(self.reverse_word(word))

#         return ' '.join(result)

#     def reverse_word(self, word: str) -> str:
#         word = list(word)
#         l, r = 0, len(word) - 1

#         while l < r:
#             word[l], word[r] = word[r], word[l]

#             l += 1
#             r -= 1

#         return ''.join(word)