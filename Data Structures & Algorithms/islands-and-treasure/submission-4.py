class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c, 0))

            while q:
                row, col, dis = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and 
                        grid[nr][nc] > dis + 1
                    ):
                        grid[nr][nc] = dis + 1
                        q.append((nr, nc, dis + 1))
                    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    bfs(row, col)


            