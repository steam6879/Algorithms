from typing import List


class Solution:
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