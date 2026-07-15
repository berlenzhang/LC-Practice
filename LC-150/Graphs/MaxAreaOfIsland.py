class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            temp_area = 1

            while q:
                r, c = q.popleft()

                for x, y in directions:
                    if (r + x in range(rows) and 
                        c + y in range(cols) and 
                        (r + x, c + y) not in visited and
                        grid[r + x][c + y] == 1):
                        q.append((r + x, c + y))
                        visited.add((r + x, c + y))
                        temp_area += 1

            return temp_area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    max_area = max(max_area, bfs(r, c))
        
        return max_area