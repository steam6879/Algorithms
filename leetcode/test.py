class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        def dfs(i, j):
            # Base cases
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or (i, j) in visited:
                return
            
            # Mark the cell as visited
            visited.add((i, j))
            
            # Explore all four directions
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    # Found a new island
                    count += 1
                    dfs(i, j)
        
        return count
