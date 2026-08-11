class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return [True, 0]
            
            l, r = dfs(curr.left), dfs(curr.right)
            isBalanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1
            return [isBalanced, max(r[1], l[1]) + 1]
        
        return dfs(root)[0]