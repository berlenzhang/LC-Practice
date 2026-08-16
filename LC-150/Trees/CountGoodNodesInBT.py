class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(cur, maxVal):
            if not cur:
                return 0
            
            isGood = 1 if cur.val >= maxVal else 0
            maxVal = max(maxVal, cur.val)
            isGood += dfs(cur.left, maxVal)
            isGood += dfs(cur.right, maxVal)
            return isGood
        
        return dfs(root, root.val)