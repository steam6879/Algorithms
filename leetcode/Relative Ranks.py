from typing import List
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = score[:]
        heapq.heapify(heap)
        m = {}

        for i in range(len(score), 0, -1):
            item = heapq.heappop(heap)
            m[item] = i
        
        ans = []
        for i in range(len(score)):
            match m[score[i]]:
                case 1:
                    ans.append("Gold Medal")
                case 2:
                    ans.append("Silver Medal")
                case 3:
                    ans.append("Bronze Medal")
                case _:
                    ans.append(f"{m[score[i]]}")

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findRelativeRanks(score= [10, 3, 8 ,9, 4]))