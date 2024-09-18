class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

class Solution:
    def __init__(self):
        self.dp = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n not in self.dp:
            self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return self.dp[n]