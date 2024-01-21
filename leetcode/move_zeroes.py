from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countZero = nums.count(0)
        for i in range(countZero):
            nums.remove(0)
            nums.append(0)
            
        return nums
    
if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1]
    print(s.moveZeroes(nums))