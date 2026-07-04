class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we have to terminate our function if N closed = N open = n
        # add opening brackets if N open < n
        # add closing brackets if N closed < N open
        stack = []
        output = []

        def backtrack(opening, closing):
            if opening == closing == n:
                output.append(''.join(stack))
                return
            if opening < n:
                stack.append('(')
                backtrack(opening + 1, closing)
                stack.pop()
            if closing < opening:
                stack.append(')')
                backtrack(opening, closing + 1)
                stack.pop()
        backtrack(0, 0)
        return output

