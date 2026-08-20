class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []


        def helper_fn(num_o, num_c):
            if num_o == num_c == n:
                output.append("".join(stack))

            if num_o < n:
                stack.append('(')
                helper_fn(num_o + 1, num_c)
                stack.pop()
            
            if num_c < num_o:
                stack.append(')')
                helper_fn(num_o, num_c + 1)
                stack.pop()
        
        helper_fn(0, 0)
        return output
