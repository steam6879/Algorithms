from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         m = {}
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 complement = -(nums[i] + nums[j])
#                 if complement in nums:
#                     if complement not in m:
#                         m[complement] = [nums[i], nums[j]]
#                         break
                    
#         for key, value in m.items():
#             ans.append([key] + value)

                    
#         return m

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return None
        
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                target = num + nums[left] + nums[right]
                if target > 0:    right -= 1
                elif target < 0:    left += 1

                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return ans


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i in range(len(nums) - 2):
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])

                if complement in seen:
                    triplet = [nums[i], nums[j], complement]
                    triplets.add(tuple(sorted(triplet)))

                seen.add(nums[j])

        return list(triplets)


class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == num[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                target = num + nums[left] + nums[right]

                if target > 0:
                    right -= 1
                elif target < 0:
                    left += 1

                else:
                    triplets.append([num, nums[left], nums[right]])
                    left += 1
                    right += 1

            return triplets


class Solution4:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for i in range(len(nums) - 2):
            low, high = i + 1, len(nums) - 1

            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                if three_sum < 0:
                    low += 1
                elif three_sum > 0:
                    high -= 1

                else:
                    triplets.add((nums[i], nums[low], nums[high]))
                    low += 1

                    while low < high and nums[low] == nums[low - 1]:
                        low += 1

        return list(triplets)



if __name__ == "__main__":
    print(Solution.threeSum(Solution, nums = [-1,0,1,2,-1,-4]))