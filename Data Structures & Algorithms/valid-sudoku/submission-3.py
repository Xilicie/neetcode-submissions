class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_sudoku_box(r0=0, c0=0, r1=3, c1=3):
            seen = set()    # stores numbers already visited
            for r in range(r0, r1):
                for c in range(c0, c1):
                    if board[r][c] == '.':
                        continue

                    num = int(board[r][c])
                    if num not in seen:
                        seen.add(num)
                    else:
                        return False
            return True 

        
        def valid_sudoku_row(r):
            seen = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                num = int(board[r][c])
                if num not in seen:
                    seen.add(num)
                else:
                    return False
            return True
        
        def valid_sudoku_col(c):
            seen = set()
            for r in range(9):
                if board[r][c] == '.':
                    continue
                num = int(board[r][c])
                if num not in seen:
                    seen.add(num)
                else:
                    return False
            return True

        # check every row
        for r in range(9):
            if not valid_sudoku_row(r):
                return False
        
        # check every column
        for c in range(9):
            if not valid_sudoku_col(c):
                return False
        
        # check each 3x3 box
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not valid_sudoku_box(r, c, r+3, c+3):
                    return False
        
        return True
