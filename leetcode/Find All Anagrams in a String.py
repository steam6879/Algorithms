from typing import List
from collections import Counter


class Solution:

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])

        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window

            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                ans.append(i-len(p)+1)   # append the starting index

            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window

            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0

        return ans


    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        ans = []
        m = {}
        for char in p:
            if char in m:
                m[char] += 1
            else:
                m[char] = 1

        for i in range(len(s) - n + 1):
            for j in range(n):
                if s[i + j] in m:
                    m[s[i + j]] -= 1
                    if m[s[i + j]] < 1:
                        m.pop(s[i + j])
                else:
                    break
            else:
                ans.append(i)

        return ans




if __name__ == "__main__":
    print(Solution.findAnagrams(Solution, s='cbaebabacd', p='abc'))