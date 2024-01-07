from typing import List, Sequence

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        maxNums, minNums = max(nums1, nums2), min(nums1, nums2)
        interNums = []
        
        for i in range(len(minNums)):
            if minNums[i] in maxNums:
                interNums.append(minNums[i])
                
        interNums = list(set(interNums))
        
        return interNums
