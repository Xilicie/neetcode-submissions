class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
        while q:
            r, c, d = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and 
                    grid[nr][nc] > d + 1
                ):
                    grid[nr][nc] = d + 1
                    q.append((nr, nc, d + 1))