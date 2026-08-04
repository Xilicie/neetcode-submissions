class Solution:
    def isValid(self, s: str) -> bool:
        # stack solution
        stack = []
        opening = ('(', '[', '{')
        closing = (')', ']', '}')

        for i in range(len(s)):
            if s[i] in closing:
                if not stack:
                    return False
                last = stack.pop()
                if closing.index(s[i]) != opening.index(last):
                    return False
            else:
                stack.append(s[i])

        return True if not stack else False