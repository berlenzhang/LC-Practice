class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                denom, num = stack.pop(), stack.pop()
                stack.append(int(num / denom))
            elif i == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            else:
                stack.append(int(i))
        
        return stack[0]