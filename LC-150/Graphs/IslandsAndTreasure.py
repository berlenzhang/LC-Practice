class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def process(r, c):
            if (r < 0 or r >= ROWS or c >= COLS or c < 0 or
                (r, c) in visited or grid[r][c] == -1):
                return
            q.append((r, c))
            visited.add((r, c))
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                process(r + 1, c)
                process(r - 1, c)
                process(r, c + 1)
                process(r, c - 1)
            dist += 1
        
