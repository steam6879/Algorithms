from typing import List

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         count = 0
#         m = {0: 0,
#              1: 0,
#              2: 0}
        
#         for num in nums:
#             m[num] += 1

#         for _ in range(m[0]):
#             nums[count] = 0
#             count += 1

#         for _ in range(m[1]):
#             nums[count] = 1
#             count += 1

#         for _ in range(m[2]):
#             nums[count] = 2
#             count += 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

            else:
                mid += 1



if __name__ == "__main__":
    print(Solution.sortColors(Solution, nums=[2, 0, 2, 1, 1, 0]))