class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, tr1, tr2):
        if not tr1 and not tr2:
            return True
        if not tr1 or not tr2:
            return False
        if tr1.val != tr2.val:
            return False
        
        return self.isSameTree(tr1.left, tr2.left) and self.isSameTree(tr1.right, tr2.right)