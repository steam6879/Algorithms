class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        square = 0  # 네모의 갯수
        commonLine = 0  # 겹치는 라인 수 (겹치는 라인이 있으면 네모 하나씩 두번을 빼줘야함)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    square += 1
                    # 젤 위 / 젤 왼쪽 / 나머지 따로 계산
                    if i == 0 and j > 0 and grid[0][j-1] == 1:
                        commonLine += 1
                    elif j == 0 and i > 0 and grid[i-1][0] == 1:
                        commonLine += 1
                    elif i != 0 and j != 0:
                        if grid[i-1][j] == 1: commonLine += 1
                        if grid[i][j-1] == 1: commonLine += 1
        return (square*4) - (commonLine*2)
if __name__ == '__main__':
    sol = Solution()
    x = [1, 3]
    print(sol.searchInsert(x, 2))
    