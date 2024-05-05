from typing import List
from collections import Counter

class Solution: #실패
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 0


        prefixSum = [0] * len(nums)
        prefixSum[0] = -1 if nums[0] == 0 else 1

        for i in range(1, len(nums)):
            if nums[i] == 0:
                prefixSum[i] = prefixSum[i - 1] - 1
            else:
                prefixSum[i] = prefixSum[i - 1] + 1

        m = Counter(prefixSum)

        maxKey = max(m, key = m.get)
        i1 = prefixSum.index(maxKey)
        i2 = len(prefixSum) - 1 - prefixSum[::-1].index(maxKey)

        return i2 - i1



class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        maxLength = 0
        m = {0: -1}
        count = 0

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in m:
                maxLength = max(maxLength, i - m[count])
            else:
                m[count] = i

        return maxLength

if __name__ == "__main__":
    print(Solution.findMaxLength(Solution, nums=[0, 0, 1, 0, 0, 0, 1, 1]))
