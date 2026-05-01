class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                fresh = stack.pop()
                prev = stack.pop()
                stack.append(prev - fresh)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                fresh = stack.pop()
                prev = stack.pop()
                stack.append(int(prev / fresh))
            else:
                stack.append(int(t))
        
        return stack.pop()