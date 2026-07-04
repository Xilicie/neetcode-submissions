class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        safe = set()

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r >= rows or c >= cols or
                (r, c) in safe or 
                board[r][c] != 'O'
            ):
                return
            
            safe.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
            
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X'
                    
            