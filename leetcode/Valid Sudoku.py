from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isDuplicated(nums):
            m = set()

            for num in nums:
                if num == ".":
                    continue
                elif num in m:
                    return True
                else:
                    m.add(num)

            return False

        # row check
        for i in range(9):
            if isDuplicated(board[i]):
                return False

        # column check
        for i in range(9):
            vertical = [x[i] for x in board]
            if isDuplicated(vertical):
                return False

        # 3*3 sub box check
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                sqare = [*(n for n in board[x][y:y+3]),
                         *(n for n in board[x+1][y:y+3]), 
                         *(n for n in board[x+2][y:y+3])]

                if isDuplicated(sqare):
                    return False

        return True
