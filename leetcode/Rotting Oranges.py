from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        que = deque()
        fresh = 0
        count = 0

        # Initialize the queue with all the rotten oranges and count the fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # Early return if there are no fresh oranges
        if fresh == 0:
            return 0

        # BFS to rot oranges
        while que:
            for _ in range(len(que)):
                i, j = que.popleft()
                for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2  # Mark as rotten
                        que.append((x, y))
                        fresh -= 1

            count += 1

        # If there are no fresh oranges left, return the number of minutes passed
        if fresh == 0:
            return count - 1  # Subtract 1 because we add 1 after finishing the last minute

        # If there are still fresh oranges left, return -1
        return -1
