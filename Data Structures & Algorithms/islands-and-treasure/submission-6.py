class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # create a queue
        q = deque()

        # append all the treasure chests' (r, c) coordinates to q
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # perform bfs on the elements in the q to find distance
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if (
                    0 <= nr < len(grid) and
                    0 <= nc < len(grid[0]) and
                    grid[nr][nc] > grid[r][c]
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
            