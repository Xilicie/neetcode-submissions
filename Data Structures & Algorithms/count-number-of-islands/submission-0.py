class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = set() # contains (row, col) tuples which are part of the islands
        res = 0

        def bfs(r, c, islands):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or 
            grid[r][c] == '0' or (r, c) in islands):
                return
            
            islands.add((r, c))

            bfs(r + 1, c, islands)
            bfs(r - 1, c, islands)
            bfs(r, c + 1, islands)
            bfs(r, c - 1, islands)
            return

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in islands and grid[row][col] == '1':
                    bfs(row, col, islands)
                    res += 1
        return res


        
