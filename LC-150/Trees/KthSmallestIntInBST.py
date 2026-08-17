class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []

        def inorder(curr):
            if curr == None:
                return 
            
            inorder(curr.left)
            in_order.append(curr.val)
            inorder(curr.right)

        inorder(root)
        return in_order[k - 1]