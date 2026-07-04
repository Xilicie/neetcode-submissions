class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]] 

        # let's do dfs from 'treasure chests' to lands
        def dfs(r, c, distance):
            if (min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] < distance):
                return 
            
            grid[r][c] = min(grid[r][c], distance)

            for dr, dc in directions:
                dfs(r + dr, c + dc, distance + 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    for dr, dc in directions:
                        dfs(row + dr, col + dc, 1)


        
            

