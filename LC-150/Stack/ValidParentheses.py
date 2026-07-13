class Solution:
    def isValid(self, s: str) -> bool:
        match = {']': '[', ')': '(', '}': '{'}
        stack = []

        for i in s:
            if i in match.values():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == match[i]:
                    stack.pop()
                else:
                    stack.append(i)

        return len(stack) == 0
            

