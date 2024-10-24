from typing import List


class Solution:
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


class Solution:
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
