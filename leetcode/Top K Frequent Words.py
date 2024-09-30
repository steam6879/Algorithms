from collections import Counter, heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countMap = Counter(words)
        heap = [(-counter, word) for word, counter in countMap.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        candidates = list(count.keys())
        candidates.sort(key=lambda word: (-count[word], word))
        return candidates[:k]


class Solution3:    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:        
        word_count = dict(Counter(words))
        result = []
        max_heap = []
        heapq.heapify(max_heap)

        for k1, v in word_count.items():
            heapq.heappush(max_heap, (-v, k1))
        for i in range(k):
            item = heapq.heappop(max_heap)
            result.append(item[1])
        return result
