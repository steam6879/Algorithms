from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        m = Counter(s)
        for i in s:
            if m[i] == 1:
                return s.index(i)
            
        return -1