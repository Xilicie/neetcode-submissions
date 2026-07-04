class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                seen.add(board[i][j])
         
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in seen:
                        return False
                seen.add(board[j][i])
        
        for sq in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sq // 3) * 3 + i
                    col = (sq % 3) * 3 + j
                    if board[row][col] != '.':
                        if board[row][col] in seen:
                            return False
                    seen.add(board[row][col])
        return True

        


