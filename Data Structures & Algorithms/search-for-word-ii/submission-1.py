class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        path = set()    # (r, c)
        res = []
        # checks if word from words is possible to form from current position(r, c)
        def dfs(r, c, i, word):
            if i == len(word):
                return True
            
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1, word) or
                   dfs(r - 1, c, i + 1, word) or
                   dfs(r, c + 1, i + 1, word) or
                   dfs(r, c - 1, i + 1, word))
            path.remove((r, c))
            return res

        for word in words:
            for r in range(ROWS):
                for c in range(COLS):
                    if dfs(r, c, 0, word) and word not in res:
                        res.append(word)
        return res