class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0: return False
        
        total //= 2

        dp = [0] * 20001
        dp[0] = 1
        
        for num in nums:
            idx = total
            while idx-num >= 0 :
                if dp[idx] or dp[idx-num]:
                    dp[idx] = 1
                idx -= 1

            if dp[total]: return True

        return False

 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        dp = [False for _ in range(target+1)]
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
            if dp[target]:
                return True
        return False