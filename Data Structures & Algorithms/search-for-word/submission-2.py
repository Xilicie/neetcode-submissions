class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # write a recursive function search()
        # which takes i, j indices and searches in 4 directions (up, down, left, right)
        # It'll use backtracking principle
        # we'll also have for loop which will iterate through each letter in the board array
        # after it finds the first letter it'll call search() function
        # if word is there it'll return True, 
        # and there will be return False statement after for loop
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

