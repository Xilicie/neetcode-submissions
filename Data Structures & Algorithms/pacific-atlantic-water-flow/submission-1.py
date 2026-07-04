class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        pacific, atlantic = set(), set()
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)
        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows - 1, j, atlantic)
        
        return [list(cell) for cell in pacific & atlantic]