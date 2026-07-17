class Solution:
    def climbStairs(self, n: int) -> int:
        one_step, two_step = 1, 1

        for i in range(n - 1):
            temp_one = one_step
            one_step = one_step + two_step
            two_step = temp_one

        return one_step