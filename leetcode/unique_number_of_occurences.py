from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        for i in range(len(arr)):
            if arr[i] in m:
                m[arr[i]] += 1
            else:
                m[arr[i]] = 1

        unique = set()
        for j in m:
            if m[j] in unique:
                return False
            else:
                unique.add(m[j])
                
        return True