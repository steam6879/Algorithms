from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptr = 0
        n = len(min(str))
        m = {}
        for i in range(n):
            m[strs[i]] = i
