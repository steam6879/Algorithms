import math
from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]



class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))


class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1

            total = 0
            if row + 1 < m:
                total += dfs(row + 1, col)

            if col + 1 < n:
                total += dfs(row, col + 1)

            return total

        return dfs(0, 0)
