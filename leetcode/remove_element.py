from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val):
            nums.remove(val)
        return len(nums)
    
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     ptr = 0
    #     i = len(nums) - 1

    #     while ptr != i:
    #         while nums[ptr] != val:
    #             ptr += 1

    #         while nums[i] == val:
    #             i -= 1


    #         nums[ptr] = nums[i]
    #         ptr += 1
    #         i -= 1
        
    #     return ptr + 1
    
if __name__ == '__main__':
    sol = Solution()
    x = [3, 2, 2, 3]
    print(sol.removeElement(x, 3))
    