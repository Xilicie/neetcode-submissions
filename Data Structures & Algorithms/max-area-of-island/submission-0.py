class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = [0]

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return
            
            grid[r][c] = 0
            visited[0] += 1
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    dfs(row, col)
                    res = max(res, visited[0])
                    visited[0] = 0
        return res