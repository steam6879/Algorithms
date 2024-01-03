from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         res = ""
#         for a in zip(*strs):
#             if len(set(a)) == 1: 
#                 res += a[0]
#             else: 
#                 return res
#         return res

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]

        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            
            ans+=first[i]

        return ans   

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         cnt = 0
#         min_strs = min(strs)
#         n = len(min(strs))
#         m = {}

#         for i in range(n):  #hash map
#             m[min_strs[i]] = i
        
#         for ptr in strs:
#             for i in range(n):
#                 if ptr[i] not in m:
#                     return cnt
                
#                 else:
#                     if ptr == str[-1]:
#                         cnt += 1
                
#         return cnt

if __name__ == '__main__':
    sol = Solution()
    x = ['flower', 'flow', 'flight']
    a = sorted(x)
    print(a)
    # print(sol.longestCommonPrefix(x))