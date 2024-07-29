class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n \
                and grid[i][j] == "1" \
                    and (i, j) not in visited:

                visited.add((i, j))

                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
            else:
                return None

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    dfs(i, j)

        return count
