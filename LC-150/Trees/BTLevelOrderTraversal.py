class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        
        if not root:
            return []
        queue = [root]

        while len(queue) > 0:
            layer = []
            length = len(queue)
            for i in range(length):
                nxt = queue.pop(0)
                layer.append(nxt.val)
                if nxt.left:
                    queue.append(nxt.left)
                if nxt.right:
                    queue.append(nxt.right)
            output.append(layer)
        
        return output