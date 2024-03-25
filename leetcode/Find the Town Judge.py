from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return trust[0][1]
        
        m = {key for key in range(n)}
        for i in range(trust):
            a, b = trust[0], trust[1]
            m[a] = m.get(a, []) + [b]

        
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n+1)
        for (a, b) in trust:
            count[a] -= 1
            count[b] += 1
            
        for i in range(1, len(count)):
            if count[i] == n-1:
                return i
        return -1