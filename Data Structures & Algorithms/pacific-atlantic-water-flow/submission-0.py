class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        res = []

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.add((r, c))
                if r == rows - 1 or c == cols - 1:
                    atlantic.add((r, c))

        def dfs(r, c, ocean):
            if visited[r][c]:
                return 

            ocean.add((r, c))
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    heights[r][c] <= heights[nr][nc]
                ):
                    dfs(nr, nc, ocean)
            

        
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        pacific2 = set()
        for r, c in pacific:
            dfs(r, c, pacific2)

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic2 = set()
        for r, c in atlantic:
            dfs(r, c, atlantic2)

        pacific = pacific.union(pacific2)
        atlantic = atlantic.union(atlantic2)

        for cell in pacific:
            if cell in atlantic:
                res.append(list(cell))
        return res