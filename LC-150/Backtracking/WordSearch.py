class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def dfs(r, c, i):
            if len(word) == i:
                return True
            
            if r >= len(board) or c >= len(board[0]) or \
                (r, c) in path or r < 0 or c < 0 \
                or word[i] != board[r][c]:
                return False
            
            path.add((r, c))
            if dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) \
                or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1):
                return True
            path.remove((r, c))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        
        return False
        

