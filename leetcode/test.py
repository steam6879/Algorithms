from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = Counter(s)
        even = [value for value in hm.values() if value % 2 == 0]
        odd = [value for value in hm.values() if value % 2 != 0]
        if odd: 
            use_odds = sum(odd) - (len(odd) - 1) 
            return sum(even) + use_odds
        else: 
            return sum(even)
        
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 2:
            return 1
        
        m = {}
        for char in s:
            if char in m:
                m[char] += 1
            else:
                m[char] = 1

        evenMap = []
        oddMap = []
        for i in m:
            if m[i] % 2 == 1:
                oddMap.append(m[i])
            else:
                evenMap.append(m[i])
        if len(oddMap) < 1:
            ans = sum(evenMap)
        else:
            ans = max(oddMap) + sum(evenMap)

        return ans
        