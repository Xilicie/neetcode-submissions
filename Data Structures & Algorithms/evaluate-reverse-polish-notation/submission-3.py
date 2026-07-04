class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if not c in {'+', '-', '*', '/'}:
                stack.append(int(c))
            else:
                if c == '+':
                    a = stack.pop()
                    b = stack.pop()
                    val = b + a
                    stack.append(val)
                elif c == '-':
                    a = stack.pop()
                    b = stack.pop()
                    val = b - a
                    stack.append(val)
                elif c == '*':
                    a = stack.pop()
                    b = stack.pop()
                    val = b * a
                    stack.append(val)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    val = int(b / a)
                    stack.append(val)
                
        return stack[-1]
