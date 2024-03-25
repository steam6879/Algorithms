from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return trust[0][1]
        judge = trust[0][1]

        for i in range(len(trust)):
            if trust[i][1] != judge:
                return -1
            
        return judge