from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        ans = []
        for num in nums:
            m[num] = abs(target - num)

        for key, value in m.items():
            if key + value == target:
                if key == value
                ans.append(nums.index(key))
                nums.remove(key)

if __name__ == "__main__":
    print(Solution.twoSum(Solution, nums=[2, 7, 11, 5], target=9))