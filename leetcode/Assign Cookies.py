from typing import Optional, List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gp, sp = 0, 0
        g.sort()
        s.sort()

        while gp < len(g) and sp < len(s):
            if g[gp] <= s[sp]:
                gp += 1
                sp += 1
            
            else:
                sp += 1

        return gp
    
if __name__ == '__main__':
    sol = Solution()
    g = [1,2,3]
    s = [1,1]

    print(sol.findContentChildren(g, s))