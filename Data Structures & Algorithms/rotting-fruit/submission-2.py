class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and 
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            minutes += 1
                    

        return minutes if not fresh else -1