class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hashmap = {}

        def dfs(curNode):
            if curNode in hashmap:
                return hashmap[curNode]
            
            copy = Node(curNode.val)
            hashmap[curNode] = copy

            for n in curNode.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node)