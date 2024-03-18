from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]

if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1, 3]
    print(s.thirdMax(nums))