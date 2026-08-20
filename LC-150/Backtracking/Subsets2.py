class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtracking(i, curr_list):
            if i == len(nums):
                copy = curr_list.copy()
                result.append(copy)
                return
            
            curr_list.append(nums[i])
            backtracking(i + 1, curr_list)
            curr_list.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtracking(i + 1, curr_list)
        
        backtracking(0, [])
        return result