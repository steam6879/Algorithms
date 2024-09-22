from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        ans = nums[0]

        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)

            ans = max(ans, curMax)

        return ans


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        min_dp = [nums[0]]
        max_dp = [nums[0]]

        for idx in range(1, len(nums)):
            prev_idx = idx - 1

            num = nums[idx]
            cand0 = num
            cand1 = max_dp[prev_idx] * num
            cand2 = min_dp[prev_idx] * num

            max_val = max(cand0, cand1, cand2)
            min_val = min(cand0, cand1, cand2)

            max_dp.append(max_val)
            min_dp.append(min_val)

        max_product = max(max_dp)
        return max_product
