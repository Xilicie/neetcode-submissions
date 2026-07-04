class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, d):
            if (min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] < d):
                return
            
            grid[r][c] = d

            for dr, dc in directions:
                dfs(r + dr, c + dc, d + 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    for dr, dc in directions:
                        dfs(row + dr, col + dc, 1)
        