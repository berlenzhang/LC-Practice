class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = [root]

        while q:
            rightMost = None
            for i in range(len(q)):
                node = q.pop(0)
                if node:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
            if rightMost:
                res.append(rightMost.val)
        
        return res