class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if not c in {'+', '-', '*', '/'}:
                stack.append(int(c))
            else:
                if c == '+':
                    val = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                elif c == '-':
                    val = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                elif c == '*':
                    val = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                else:
                    val = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                
        return stack[-1]
