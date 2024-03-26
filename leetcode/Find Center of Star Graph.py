from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = [0] * (len(edges) + 2)

        for a, b in edges:
            count[a] += 1
            count[b] += 1

        for i in range(1, len(count)):
            if count[i] == len(edges):
                return i
            
        return -1
         
if __name__ == "__main__":
    s = Solution()
    edges = [[1,2],[2,3],[4,2]]
    print(s.findCenter(edges))
