from typing import List

class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     ans = ''
    #     v = sorted(strs)
    #     n = len(min(strs))
    #     first = v[0]
    #     last = v[-1]

    #     for i in range(min(len(first), len(last))):
    #         if first[i] != last[i]:
    #             return ans
            
    #         ans += first[i]

    #     return ans
            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        z = zip(*strs)
        cnt = 0

        for i in z:
            if len(set(i)) != 1:
                break
            cnt += 1
        
        return strs[0][0:cnt]

if __name__ == '__main__':
    sol = Solution()
    s = '()[[}{}]]'
    
    s = list(s)
    print(s)
    print()

    s.sort()
    print(s)
