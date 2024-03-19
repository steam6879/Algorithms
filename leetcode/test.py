import heapq
score= [10, 3, 8 ,9, 4]
heapq.heapify(score)
print(score)
#print(len(heap))


    scoreCopy = []
    for item in score:
        scoreCopy.append(item)

    heapq.heapify(scoreCopy)
    placing = {}
    index = len(score)
    while len(scoreCopy) > 0:
        item = heapq.heappop(scoreCopy)
        placing[item] = index
        index -= 1

    result = []
    for index in range(len(score)):
        match placing[score[index]]:
            case 1:
                result.append("Gold Medal")
            case 2:
                result.append("Silver Medal")
            case 3:
                result.append("Bronze Medal")
            case _:
                result.append(str(placing[score[index]]))

    return result




from typing import List
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = score
        heapq.heapify(heap)
        m = {}
        if len(heap) == 1:
            m[heapq.heappop(heap)] = 'Gold Medal'
        elif len(heap) == 2:
            m[heapq.heappop(heap)] = 'Gold Medal'
            m[heapq.heappop(heap)] = 'Silver Medal'
        elif len(heap) == 3:
            m[heapq.heappop(heap)] = 'Gold Medal'
            m[heapq.heappop(heap)] = 'Silver Medal'
            m[heapq.heappop(heap)] = 'Bronze Medal'

        elif len(heap) > 3:
            m[heapq.heappop(heap)] = 'Gold Medal'
            m[heapq.heappop(heap)] = 'Silver Medal'
            m[heapq.heappop(heap)] = 'Bronze Medal'

            for i in range(4, len(heap)):
                m[heapq.heappop(heap)] = f'{i}'

        for i in range(len(score)):
            score[i] = m[i]

        return score