from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0
        nums1.sort()
        nums2.sort()

        interNums = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                interNums.append(nums1[i])
                i += 1
                j += 1
            
        return interNums



# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         interNums = []
#         if len(nums1) > len(nums2):
#             uniNums, subNums = nums1, nums2
#         else:
#             uniNums, subNums = nums2, nums1

#         for i in subNums:
#             if i in uniNums:
#                 interNums.append(i)
#                 uniNums.remove(i)

#         return interNums

        # for i in uniNums:
        #     if i in m:
        #         interNum.append(i)
        #     else:
        #         m.add(i)
