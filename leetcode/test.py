class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isDuplicated(nums: List[str])->bool:
            num_set = set()
            for num in nums:
                if num == ".": continue
                if num in num_set: return True
                num_set.add(num)
            return False
        
        for horiz_num in range(9):
            horiz_line = board[horiz_num]
            if isDuplicated(horiz_line): return False
        
        for verti_num in range(9):
            verti_line = [x[verti_num] for x in board]
            if isDuplicated(verti_line): return False
 
        for x in range(0,9,3):
            for y in range(0,9,3):
                sqare = [*(n for n in board[x][y:y+3]),
                *(n for n in board[x+1][y:y+3]),
                *(n for n in board[x+2][y:y+3]),
                ]
                if isDuplicated(sqare): return False
        
        return True