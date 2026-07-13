class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        blocks = [0] * 9
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                val = int(board[r][c]) - 1 # convert to num in [0,8]
                mask = (1 << val)

                # check dupes
                if (rows[r] & mask):
                    return False
                if cols[c] & mask:
                    return False
                if blocks[(r // 3) * 3 + (c // 3)] & mask:
                    return False

                rows[r] |= mask
                cols[c] |= mask
                blocks[(r // 3) * 3 + (c // 3)] |= mask
        
        return True



        