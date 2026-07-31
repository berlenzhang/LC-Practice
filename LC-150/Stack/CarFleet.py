class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(p, s) for p, s in zip(position, speed)]
        stack = []
        combined.sort()

        for p, s in combined[::-1]:
            hrs = (target - p) / s
            stack.append(hrs)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
