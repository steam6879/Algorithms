from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptr = 0
        n = len(min(str))
        m = {}
        for i in range(n):  #hash map
            m[strs[i]] = i
        
        j = 0

        for i in range(n):
            while j < len(strs):
                if strs[j][i] in m:
