class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0

        while r < len(nums) - 1:
            jump_range = 0
            for i in range(l, r + 1):
                jump_range = max(jump_range, i + nums[i])

            l = r + 1
            r = jump_range
            jumps += 1
        return jumps