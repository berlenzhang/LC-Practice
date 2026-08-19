class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(idx, curSum, curList):
            if curSum == target:
                output.append(curList.copy())
                return
            if curSum > target or idx >= len(nums):
                return
            
            curList.append(nums[idx])
            dfs(idx, curSum + nums[idx], curList)
            curList.pop()
            dfs(idx + 1, curSum, curList)
        
        dfs(0, 0, [])
        return output