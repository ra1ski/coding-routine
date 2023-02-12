class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {'{': '}', '[': ']', '(': ')'}

        result = []

        for i in s:
            if i in parantheses:
                result.append(i)
            else:
                if not result or parantheses[result.pop()] != i:
                    return False

        return not result


s = Solution()

print(s.isValid("()[]{}"))
