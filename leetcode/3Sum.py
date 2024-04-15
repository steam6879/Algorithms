from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        m = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in nums:
                    if complement not in m:
                        m[complement] = [nums[i], nums[j]]
                        break
                    
        for key, value in m.items():
            ans.append([key] + value)

                    
        return m
    
if __name__ == "__main__":
    print(Solution.threeSum(Solution, nums = [-1,0,1,2,-1,-4]))