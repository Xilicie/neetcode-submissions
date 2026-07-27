class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if (board[r][c] not in rows[r] and
                    board[r][c] not in cols[c] and
                    board[r][c] not in boxes[r//3 * 3 + c//3]):

                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[r//3 * 3 + c//3].add(board[r][c])
                elif (board[r][c] == '.'):
                    continue
                else:
                    return False
        return True