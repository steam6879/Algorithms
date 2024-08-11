from typing import List
import collections


class Solution:
    # 책 풀이. 단계별 리프 노드 제거
    # 내 풀이에서는 리프노드만을 걸러낸 뒤 dfs 탐색을 통해 최소 높이를 찾아다녔다.
    # 여기서는 리프 노드를 제거한 트리에서 다시 리프 노드를 걸러내 마지막까지 남아있는 노드들을 답으로 리턴한다.
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leave in leaves:
                neighbor = graph[leave].pop()
                graph[neighbor].remove(leave)

                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)

            leaves = newLeaves

        return leaves
