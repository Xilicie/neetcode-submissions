class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in b:
                stack.append(i)
            elif stack and i == b[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
