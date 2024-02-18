from typing import Optional, List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        square = 0
        commonList = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    square += 1

                    if i == 0 and j > 0 and grid[0][j - 1] == 1:
                        commonList += 1
                    elif j == 0 and i > 0 and grid[i - 1][0] == 1:
                        commonList += 1

                    elif i != 0 and j != 0:
                        if grid[i][j - 1] == 1:
                            commonList += 1
                        
                        if grid[i - 1][j] == 1:
                            commonList += 1

        return (square*4) - (commonList*2)
                
if __name__ == '__main__':
    s = Solution()

    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(s.islandPerimeter(grid))