class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(idx, curSum, curList):
            if curSum == target:
                result.append(curList.copy())
                return
            if curSum > target or idx >= len(candidates):
                return
            
            curList.append(candidates[idx])
            dfs(idx + 1, curSum + candidates[idx], curList)
            curList.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            
            dfs(idx + 1, curSum, curList)
        
        dfs(0, 0, [])
        return result
